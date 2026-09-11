# SBOM API Demo

A demo project with sample SBOM API calls

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
