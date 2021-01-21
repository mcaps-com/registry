import urllib3
import json
import time
import csv

from coingecko import CoinGeckoAPI

cgapi = CoinGeckoAPI()
#TOKEN = 'nftx'

def get_logo(TOKEN):
    x = cgapi.get_coin_by_id(TOKEN)
    #print (x['name'])
    #print (x['links']['homepage'])
    print (x['image']['large'])

#TOKEN = 'lido-dao'
#TOKEN = 'cover'
#get_logo(TOKEN)

#dict_keys(['id', 'symbol', 'name', 'asset_platform_id', 'block_time_in_minutes', 'hashing_algorithm', 'categories', 'public_notice', 'additional_notices', 'localization', 'description', 'links', 'image', 'country_origin', 'genesis_date', 'sentiment_votes_up_percentage', 'sentiment_votes_down_percentage', 'market_cap_rank', 'coingecko_rank', 'coingecko_score', 'developer_score', 'community_score', 'liquidity_score', 'public_interest_score', 'market_data', 'community_data', 'developer_data', 'public_interest_stats', 'status_updates', 'last_updated', 'tickers'])


def get_list():
    syms = list()
    with open('addr.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                #print(f'\t{row}')
                line_count += 1
                syms.append(row)
    return syms

def na(x):
    if x == None:
        return "NA"
    else:
        return x

def info_arr(xid):
    info = cgapi.get_coin_by_id(xid)
    #print(info)

    s = info['symbol']            
    try:
        ca = info['contract_address']
        print (">>>> ",ca)
    except:
        ca = "NA"
        
    #
    #'total_supply'
    #'max_supply': 
    #'circulating_supply'
    #'fully_diluted_valuation'
    #
    #telegram_channel_identifier
    # subreddit_url
    # twitter_screen_name
    # links': {'homepage'
    # 'image': {'large': , 
    # 'block_time_in_minutes'
    # 'hashing_algorithm'
    # 'categories'
    # 'genesis_date'
    # 'last_updated'
    mr = info['market_cap_rank']
    mr = str(na(mr))
    
    ap = info['asset_platform_id']
    ap = na(ap)
    hp = info['links']['homepage'][0]
    hp = na(hp)
    arr = [xid,s,info['name'],ap,str(info['coingecko_rank']),mr,hp,ca]
    
    return arr


def fetch_syms_addr(lastsym, startFilter):
    print ("fetch from ",lastsym)
    l = cgapi.get_coins_list()
    print (len(l))
    i = 0
    sd = {}    
    ff = False
    with open('addr.csv', 'a') as f:
        
        for x in l[:]:
            print (x['id'])
            
            if ff or not startFilter:
                arr = info_arr(x['id'])
                print(arr)
                st = ';'.join(arr)
                f.write(st + '\n')
                print (str(i) + " " + st)
                i+=1
                time.sleep(0.5)

            if x['id'] == lastsym: 
                ff = True

    #print (ca)


def fetch():
    l = cgapi.get_coins_list()
    print ("coins ",len(l))


    syms = get_list()
    print ("stored ",len(syms))
    lastsym = ""
    try:
        lastsym = syms[-1][0]
        print ("lastsym ",lastsym)
        startFilter = True
    except:
        i=0
        startFilter = False
    
    #lastsym = "none"
    fetch_syms_addr(lastsym, startFilter)

def match_file():
    slist = get_list()
    with open('addrmap.csv','w') as f:
        for l in slist:
            ca = l[-1]
            #'id';'symbol';'name';'address';'asset_platform_id';'coingecko_rank';'market_cap_rank';'homepage';'contract
            s = l[1]
            p = l[3]
            if ca != "NA" and p == "ethereum":
                print (ca,s)
                f.write(ca + ';' + s + '\n')

if __name__=='__main__':
    # syms_addr()
    match_file()
    
    # aid = 'ethereum' #info['asset_platform_id']
    # contract_address = "0x38c4102d11893351ced7ef187fcf43d33eb1abe6"
    # xinfo = cgapi.get_coin_info_from_contract_address_by_id(aid, contract_address)
    # print (xinfo)
