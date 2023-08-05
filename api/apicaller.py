from . import cmlapi, gns3api, eveapi
from getpass import getpass

def createAuthedAPISession():
    apiObject = cmlapi.API(baseURL="https://ktl-csco-cml01.lab.trankelvin.com/api/v0",
                            username=input("Enter your username: "),
                            password=getpass("Enter your password: "))

    if apiObject.authAPI() is not None:
        print("Authentication error. Validate your credentials/parameters and try again.")
        exit(-1)
    
    return apiObject