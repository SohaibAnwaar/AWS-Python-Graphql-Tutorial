from app_sync import gq_client
import json
import boto3
from aws_config import settings

access_key = settings.access_key
access_secret = settings.access_secret

# Initilizing the lambda function
lambda_client = boto3.client('lambda', region_name='us-east-1', aws_access_key_id=access_key,
            aws_secret_access_key=access_secret)


def insert(name):
  """Insert A car record into the app sync

  Args:
      name (string): Name of the car

  Returns:
      response: Response which is saved in the db
  """
  lambda_payload = {
    "name": name
  }
  res = lambda_client.invoke(FunctionName='MyCarInsert', 
                      InvocationType='RequestResponse',
                      Payload=json.dumps(lambda_payload))

  return res


def get():
  """Get all of the elements present in App Sync

  Return:
   Json
  """  

  result = gq_client.execute(
            query="""
            query MyQuery {
              listMyCars {
                items {
                  id
                  name
                }
              }
            }
            """,
    operation_name='listMyCars'
)

  return result



# insert
insert("bugatti")
print(get())



