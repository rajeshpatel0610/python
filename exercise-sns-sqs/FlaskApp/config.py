# Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except
# in compliance with the License. A copy of the License is located at
#
# https://aws.amazon.com/apache-2-0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
"Central configuration"
import os

PHOTOS_BUCKET = 'edxprojphoto' #os.environ['PHOTOS_BUCKET']
FLASK_SECRET = '1323dsfd' #os.environ['FLASK_SECRET']

DATABASE_HOST = 'edx-photos-db.c41ff2jywpdd.us-west-2.rds.amazonaws.com' #os.environ['DATABASE_HOST']
DATABASE_USER = 'web_user' #os.environ['DATABASE_USER']
DATABASE_PASSWORD = 'ec021039' #os.environ['DATABASE_PASSWORD']
DATABASE_DB_NAME = 'Photos' #os.environ['DATABASE_DB_NAME']

AWS_REGION = "us-west-2"
COGNITO_POOL_ID = "us-west-2_tTaNAIhka" #os.environ['COGNITO_POOL_ID']
COGNITO_CLIENT_ID = "43abkccfut9pk7094cv1dvjmfa" #os.environ['COGNITO_CLIENT_ID']
COGNITO_CLIENT_SECRET = "1a027et1rnn6m681i29b319qhba50j7o0j8sbdsoev3vu32uc84m" #os.environ['COGNITO_CLIENT_SECRET']
COGNITO_DOMAIN = "photolables.auth.us-west-2.amazoncognito.com" #os.environ['COGNITO_DOMAIN']
BASE_URL = "https://1ef0c6a54d2841afa092f66eb0d51118.vfs.cloud9.us-west-2.amazonaws.com" #os.environ['BASE_URL']

