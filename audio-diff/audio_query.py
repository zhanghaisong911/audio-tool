import requests
import json
import time
import uuid
import pandas as pd
import sys
import getopt
import os


accessKey ="Wm3sYivMpGvmY1TmWSwb"
appId="default"
audioType = "POLITICAL_ABUSE_PORN_AD_MOAN_ANTHEN"

def log(level, info):
    print("logLev=[{}]    info={}".format(level, info))


#btId  |  url  |   type
def readData():
    with open("./tmp.csv", "r") as f:
        datas = f.readlines()
    return datas

def predict(argv):
    log("DEBUG", argv)
    if len(argv) != 2:
        log("ERROR", "argv len != 3")
        return
    path    = argv[0]
    saasUrl = argv[1]

    datas = readData()
    datas = datas[1:]
    count = 0
    res = {}

    for line in datas:
        items = line.split(",")
        if len(items) != 3:
            log("ERROR", "items len !=3")
            continue
        count = count + 1
        if count % 10 == 0:
            print(count)
        headers = {
            'Content-Type': 'application/json'
        }
        btId = "2oppotest-" + items[0]
        data=dict()
        data["accessKey"] = accessKey
        data["btId"] = btId
        log("DEBUG", data)
        try:
            result = requests.post(saasUrl, data=json.dumps(data), headers=headers).content.decode()
            log("INFO", result)
            res[btId] = result
        except:
            log("ERROR", "query")
            continue
        time.sleep(0.008)
     
    with open(path, "w") as f:
        f.write(json.dumps(res) + "\n")

if __name__ == "__main__":
    predict(sys.argv[1:])
