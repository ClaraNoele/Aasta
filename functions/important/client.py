import os
import boto3
import json
import gspread
from google.oauth2 import service_account


key1 = os.environ['aws_key1']
key2 = os.environ['aws_key2']
s3 = boto3.resource(
    service_name='s3',
    region_name='us-west-1',
    aws_access_key_id=key1,
    aws_secret_access_key=key2
) #Keys to S3

content_object = s3.Object('aastaclient','client_secret.json') #Finds the file
file_content = content_object.get()['Body'].read().decode('utf-8') #Reads the file
json_content = json.loads(file_content) #Changes the file contents to Json

credentials = service_account.Credentials.from_service_account_info(
    json_content) #Reads the Json Library

scoped_credentials = credentials.with_scopes(
    ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"])

client = gspread.authorize(scoped_credentials) #Authorizes the credentials