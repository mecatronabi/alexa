# A lambda function to interact with AWS RDS MySQL

import pymysql
import sys
import random

REGION = 'us-east-1'

rds_host  = "boschdb.cyeg.us-east-1.rds.amazonaws.com"
name = "boschdb"
password = "robertbosch2018"
db_name = "sensores"

"""
def save_events(event):
    
    This function fetches content from mysql RDS instance

    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
      #  cur.execute(insert into temperatura (temperatura) values( %s) % (event['temperatura']))
        cur.execute(select temperatura from temperatura order by id desc limit 1)
        registro=cur.fetchone()
        conn.commit()
        cur.close()
        
    print (registro)
   
"""    
    
def lambda_handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    with conn.cursor() as cur:
      #  cur.execute("""insert into temperatura (temperatura) values( %s)""" % (event['temperatura']))
        cur.execute("""select temperatura from temperatura order by id desc limit 1""")
        registro=cur.fetchone()
        conn.commit()
        cur.close()
        
    print (registro)      
       
       
    print(event)
    upperLimitDict = event['request']['intent']
    
    number=random.randint(0,100)
    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': 'The temperature of X D K Sensor Bosch is ' + str(registro),
            }
        }
    }

    return response

# event = {
#   "id": 777,
#   "name": "appychip"
# }
# context = ""
# main(event, context)


