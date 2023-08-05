from . import cmlapi, gns3api, eveapi
from getpass import getpass

def createAuthedAPISession(url, verify):
    apiObject = cmlapi.API(baseURL=f"https://{url}/api/v0",
                            username=input("Enter your username: "),
                            password=getpass("Enter your password: "),
                            verifyStatus=verify)

    if apiObject.authAPI() is not None:
        print("Authentication error. Validate your credentials/parameters and try again.")
        exit(-1)
    
    return apiObject