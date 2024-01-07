import json
import requests

def lambda_handler(event, context):

    try:
        ip = requests.get("http://checkip.amazonaws.com/")
    except requests.RequestException as e:
        print(e)

        raise e

    samplelist = ['sampleString1', 'sampleString2', 'sampleString3']
    concatenatedstring = ''
    for item in samplelist:
        # Noncompliant: inefficient string concatenation inside a loop is used.
        concatenatedstring += item + "\n"

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": samplelist,
            "location": ip.text.replace("\n", "")
        }),
    }