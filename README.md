## Usage Guide

This document explains how to upload synthetic or anonymized data into the IFC OBP Sandbox.

Python Scripts are provided which read the spreadsheets and call the OBP APIs.
The following bank_ids are existing:
* 'UNIL',
* 'Telenor',
* 'ALFH',
* 'JSBL',
* 'HABB',
* 'Mobilink'

If you registered with your official business email domain, you will be granted permission to use all restricted
 apis needed for the data upload.

*The granting of permission will take place when you login, and it can take some minutes till it is completed for the first time!*
### Register a User and Api Key

* get obp username and password as registered with official! bank email address [here](https://ifcsandbox.openbankproject.com/user_mgt/sign_up).
* create api keys [here](https://ifcsandbox.openbankproject.com/consumer-registration).

  For a sandbox we can use an easy access authentication, we only need the consumer_key for that.
### Configure the script

Copy the script config and modify it - and add our username / password and consumer key.

* copy env_example to .env
  ```shell
  cp env_example .env
  ```
* add your [username / password](https://ifcsandbox.openbankproject.com/user_mgt/sign_up) and [consumer key](https://ifcsandbox.openbankproject.com/consumer-registration) 

### Copy your data set to  the data  sheet

We need to copy the spreadsheet template and then add your own data. Please do not change the structure of the spreadsheet in any way.

* copy resources/obp-data-import_template.xlsx to resources/obp-data-import.xlsx
  ```shell
  cp resources/obp-data-import_template.xlsx resources/obp-data-import.xlsx
  ```
* import your data set into the spreadsheet resources/obp-data-import.xlsx

### Use the script

* create a virtual env for python:
  ```shell
  python -m venv venv
  ```
* install dependencies :
  ```shell
  pip install -r requirements.txt
  ```
* to import data run:

   python main.py
   
