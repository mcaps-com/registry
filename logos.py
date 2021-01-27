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

from cg_universe import *

#= `https://raw.githubusercontent.com/mcaps-com/registry/master/tokens/${symbol}/logo.png`

app_bucket = "app.rapidtrade.io"
region = 'ap-southeast-1'
s3_client = boto3.client('s3',region_name = region)

from coingecko import CoinGeckoAPI

cgapi = CoinGeckoAPI()

def store_logo(xid):
    """ store a logo given a CG id. path is defined by symbol """
    try:
        info = cgapi.get_coin_by_id(xid)
    except:
        print ("no info for ", xid)
        return
    imgurl = info['image']['large']
    sym = info['symbol']
    print ("store ",sym,imgurl)
    dest_fpath = os.getcwd() + '/tokens/' + sym
    print ("dest_fpath ",dest_fpath)
    if not os.path.exists(dest_fpath):
        os.mkdir(dest_fpath)
    path = dest_fpath + '/logo.png'    
    if not os.path.exists(path):
        download_file(imgurl, path)
    else:
        print ("already exists ",path)

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

#sym = 'paid-network'
#sym = 'tosdis'
#store_logo(sym)

def store_all(tokens):
    #tokens = get_tokens()
    #slist = get_sym_list()
    print ("tokens ",len(tokens))
    #'id';'symbol';'name';'address';'asset_platform_id';'coingecko_rank';'market_cap_rank';'homepage';'contract
    for t in tokens[:]:
        #sym = t[0]
        print ("store ",t)
        try:
            store_logo(t)
        except:
            print ("failed to store ",t)
            continue


# get the directory contents which are symbols
# and map to id
idmap = map_file() # symbol => id
syms = get_tokens_syms()
s = list()
ex = os.listdir("./tokens")
for x in syms: 
    if x not in ex:
        try:
            s.append(idmap[x])
        except:
            print ("not found ",x)
#print (syms)

print ("existing ",len(ex))
print ("to update ",len(s))
print (ex[:10])
print (s[:10])
#store_all(s[:])

print ('pipt' in ex)
#print ('morc' in s)

# info = cgapi.get_coin_by_id('999')
# print (info)

ctr = '0xbf05571988daab22d33c28bbb13566eae9dee626'
info = cgapi.get_info_from_contract(ctr)
print (info['symbol'])