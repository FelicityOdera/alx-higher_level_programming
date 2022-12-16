#!/usr/bin/python3
''' url requests, added error handling  '''
import requests
from sys import argv

if __name__ == "__main__":
    reqst = requests.get(argv[1])
    if reqst.status_code >= 400:
        print("Error code: {}".format(reqst.status_code))
    else:
        print(reqst.text)
