import json
import requests
import time

MY_EMAIL = ""
MY_PASSWORD = "" 
# Run "anaconda auth api-key" (or "anaconda auth api-key --at nucleus-staging" for staging) 
# at the command line and place the value here:
MY_API_KEY = ""
HOSTNAME = "https://repo.anaconda.cloud" # "https://repo-latest.dev-us-east-1.anaconda.cloud" for staging

def create_session(**kwargs):
    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {MY_API_KEY}"})
    return session


with create_session(username=MY_EMAIL, password=MY_PASSWORD) as session:
    begin = time.time()
    response = session.get(       
        f"{HOSTNAME}/repo/main/sboms/sha256/669be0a9dd85d7e46497ef0f86ec66683b54c30d4a3e769b1945a7499b2f2b1c?mode=view"
    )
    end = time.time()
    run_time = end-begin
    print(f"Run time is {run_time:0.2f}s\n")
    print(response)
    print(json.dumps(response.json(), indent=4))
    
    begin = time.time()
    response = session.get(
        f"{HOSTNAME}/repo/main/sboms/by-properties/conda/7za/win-64/920?build=haa95532_0"
    )
    end = time.time()
    run_time = end-begin
    print(f"Run time is {run_time:0.2f}s\n")
    print(response)
    print(json.dumps(response.json(), indent=4))