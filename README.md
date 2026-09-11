# SBOM API Demo

A demo project with sample API calls to endpoints that enable SBOM retrieval by package SHA256:
```bash
https://repo.anaconda.cloud/repo/{channel_name}/sboms/sha256/{package_sha256}
```
- query params: 
  - mode: *view | download, (default=view)* <br> <br>


and by package properties:
```bash
https://repo.anaconda.cloud/repo/{channel_name}/sboms/by-properties/{artifact_family}/{common_name}/{platform}/{version} 
```
- query params: 
  - mode: *view | download, (default=view)*
  - build: *build string*


## Restrictions
These endpoints only retrieve SBOMs for `main` and `main-x` channels in SPDX format as JSON (view) or stream (download). View mode should work for most applications.

## Prerequisites
A user must have a seat in an organization with a business subscription

## Setup Environment

- Install conda
- Run `conda env create -f environment.yml`
- Run `conda activate sbom_api_test`

## Create an API key 

### From CLI
- Run `conda install anaconda-auth`
- Create an API key from CLI as described in comments (`anaconda auth api-key`)

### From the Anaconda Platform UI
- Navigate to `Account Settings` → `API Keys` and select `Create API Key`
- Create an API Key and update `sbom_api_demo.py` with the value

## Update Run Script
- Add your API key, password and email address to `sbom_api_demo.py` where indicated

## Run

- Run `python sbom_api_demo.py`

## curl examples

Create and save API key
```bash
export MYAPIKEY==$(anaconda auth api-key)
```

Retrieve SBOM by SHA256
```bash
curl -X GET -H "Authorization: Bearer $MYAPIKEY" https://repo.anaconda.cloud/repo/main/sboms/sha256/669be0a9dd85d7e46497ef0f86ec66683b54c30d4a3e769b1945a7499b2f2b1c | jq
```

Retrieve SBOM by properties
```bash
curl -G -H "Authorization: Bearer $MYAPIKEY" --data-urlencode "build=gpu_4" 
"https://repo.anaconda.cloud/repo/main/sboms/by-properties/conda/_py-xgboost-mutex/win-64/2.0" | jq
```
