import urllib3
import json
import time
import csv

import logging
import boto3
from botocore.exceptions import ClientError
import os
import sys
import requests
import shutil
import os

#= `https://raw.githubusercontent.com/mcaps-com/registry/master/tokens/${symbol}/logo.png`

app_bucket = "app.rapidtrade.io"
region = 'ap-southeast-1'
s3_client = boto3.client('s3',region_name = region)

from coingecko import CoinGeckoAPI

cgapi = CoinGeckoAPI()

def store_logo(xid):
    info = cgapi.get_coin_by_id(xid)
    imgurl = info['image']['large']
    print ("> ",xid,imgurl)
    dest_fpath = os.getcwd() + '/tokens/' + xid
    print ("dest_fpath ",dest_fpath)
    if not os.path.exists(dest_fpath):
        os.mkdir(dest_fpath)
    path = dest_fpath + '/logo.png'
    download_file(imgurl, path)

def store_all():

    l = cgapi.get_coins_list()
    print (len(l))
    for x in l[:10]:
        #print (x)
        info = cgapi.get_coin_by_id(x['id'])
        try:
            ca = info['contract_address']
        except:
            ca = "NA"
        #if ca != "NA"
        imgurl = info['image']['large']
        print ("> ",x['symbol'],imgurl)
        download_file(imgurl, cid + '.png')
        #arr = info_arr(x['id'])
        #'image': {'thumb': '', 'small': '', 'large': ''}, 

def download_file(url, local_filename):
    #local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename

def download_logo(cid):
    info = cgapi.get_coin_by_id(cid)
    url_img = info['image']['large']
    #print ()
    download_file(url_img, cid + '.png')

store_logo('tosdis')