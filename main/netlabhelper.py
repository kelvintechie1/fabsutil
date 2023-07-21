# Net Lab Helper
# By Kelvin Tran
# Version DEV.0.1

# Import dependencies
from sys import platform
from time import sleep
from subprocess import run, Popen, DEVNULL
from argparse import ArgumentParser
from pathlib import Path
from os import remove
import requests
import yaml


# Define class for main utility elements
class Utility:
    def __init__(self, options, acceptableOS=["win32"]):
        self.options = options
        self.acceptableOS = acceptableOS

    # Check system compatibility - Windows only for now
    def checkOS(self):
        if platform not in self.acceptableOS:
            print("Your operating system is not compatible with this utility.")
            exit(-1)

    # Define and accept user input for menu option indicating desired utility functionality
    def askMenuOption(self):
        print("-----------------\nMain Menu")
        for i in self.options:
            print(f"{i} - {self.options[i]}")
        while True:
            try:
                if (choice := int(input("Enter the number of one of the above options (i.e., 1): "))) in list(
                        self.options.keys()):
                    return choice
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid option.")

    # Parse optional command-line arguments for utility
    def parseArgs(self):
        parser = ArgumentParser(prog="CML Enhancement Utility",
                                description="Utility to enhance features within the Cisco Modeling Labs (CML) network emulation software")
        parser.add_argument("-c", "--choice", help="Define the menu option choice prior to running the utility",
                            type=int, required=False, choices=list(self.options.keys()))

        return parser.parse_args()

    def callFunctionality(self, choice):
        if choice == 1:
            breakoutUtil = BreakoutUtility(breakoutWorkingDir=r"C:\Users\kelvintr\Documents\breakout")
            self.labs = breakoutUtil.activateBreakout()
        elif choice == 2:
            breakoutUtil = BreakoutUtility(breakoutWorkingDir=r"C:\Users\kelvintr\Documents\breakout")
            breakoutUtil.launchSessions(labs=self.labs, type="serial")
        elif choice == 3:
            breakoutUtil = BreakoutUtility(breakoutWorkingDir=r"C:\Users\kelvintr\Documents\breakout")
            vncDirectory = r"C:\Program Files\RealVNC\VNC Viewer"
            breakoutUtil.launchSessions(labs=self.labs, type="vnc", workingDir=vncDirectory)
        elif choice == 4:
            breakoutUtil = BreakoutUtility(breakoutWorkingDir=r"C:\Users\kelvintr\Documents\breakout")
            breakoutUtil.stopBreakout()
        elif choice == 5:
            exit(0)

        print("-----------------\nFunction completed!")


class BreakoutUtility:
    def __init__(self, breakoutWorkingDir=".", breakoutName="breakout.exe", labConfigName="labs.yaml",
                 configName="config.yaml"):
        self.breakoutWorkingDir = breakoutWorkingDir
        self.breakoutName = breakoutName
        self.labConfigName = labConfigName
        self.configName = configName

    def activateBreakout(self):
        print("Deleting labs.yaml file...")
        try:
            remove(f"{self.breakoutWorkingDir}\\{self.labConfigName}")
        except FileNotFoundError:
            print("labs.yaml not found - good to go!")
        run(["powershell.exe", f"./{self.breakoutName}", "init"], cwd=self.breakoutWorkingDir)

        with open(Path(f"{self.breakoutWorkingDir}\{self.labConfigName}"), "r") as labConfigFile:
            labsFromConfig = yaml.load(labConfigFile, Loader=yaml.FullLoader)
        labsFromConfig[list(labsFromConfig.keys())[0]]["enabled"] = True
        with open(Path(f"{self.breakoutWorkingDir}\{self.labConfigName}"), "w") as labConfigFile:
            labConfigFile.write(yaml.dump(labsFromConfig))

        runBreakout = Popen(["powershell.exe", f"./{self.breakoutName}", "run", "-config", self.configName],
                            cwd=self.breakoutWorkingDir, stdout=DEVNULL)
        sleep(5)
        if runBreakout.returncode is None:
            print("Breakout Execution Successful!")

        return labsFromConfig

    def launchSessions(self, labs, type, workingDir="."):
        listOfLabs = [labs[lab] for lab in labs]
        for lab in listOfLabs:
            nodeList = [lab["nodes"][node] for node in sorted(lab["nodes"], key=lambda x: lab["nodes"][x]["label"])]
            for node in nodeList:
                for line in [device for device in node["devices"] if type in device["name"]]:
                    if type == "serial":
                        print(
                            "Launching terminal session for node {} in lab {}".format(node["label"], lab["lab_title"]))
                        Popen(
                            ["securecrt", "/T", "/N", node["label"], "/telnet", "127.0.0.1", str(line["listen_port"])],
                            cwd=workingDir)
                    elif type == "vnc":
                        print("Launching VNC session for node {} in lab {}".format(node["label"], lab["lab_title"]))
                        Popen(["powershell.exe", "./vncviewer.exe", "127.0.0.1:{}".format(line["listen_port"]),
                               "-VerifyId=0", "-WarnUnencrypted=0"], cwd=workingDir)
                    sleep(1.5)

    def stopBreakout(self):
        run(["powershell.exe", "Stop-Process", "-Name", "breakout"])


def main():
    print("CML Enhancement Utility\nVersion DEV.0.0\nBy Kelvin Tran\n------")

    options = {1: "Activate Breakout", 2: "Auto-Launch SSH Sessions (Requires SecureCRT)",
               3: "Auto-Launch VNC Sessions (Requires RealVNC Viewer)", 4: "Kill Breakout", 5: "Quit Program"}
    utilObject = Utility(options)
    utilObject.checkOS()

    args = utilObject.parseArgs()

    while True:
        choice = None

        if args.choice is not None:
            choice = args.choice
        else:
            choice = utilObject.askMenuOption()

        utilObject.callFunctionality(choice)

        if args.choice is not None:
            break


if __name__ == "__main__":
    main()