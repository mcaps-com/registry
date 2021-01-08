import urllib3

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

def show_syms():

    l = cgapi.get_coins_list()
    print (len(l))
    for x in l[:]:
        #print (x)
        #print ('..')
        #print (x['symbol'][0])
        if x['name'][:4] == 'Shop':
            print (x)

    #info = cgapi.get_coin_by_id(x['id'])
    #print (info['symbol'],info['name'],info['public_notice'])
    #print (info.keys())
    #,info['public_interest_stats'])
    #'public_interest_stats': {'alexa_rank': 5253,
    #asset_platform_id
    #total_supply
    #max_supply
    #'links': {'homepage': ['https://ftx.com/tokens/TRYBHALF', '', ''], 'blockchain_site': ['', '', '', '', ''], 'official_forum_url': ['', '', ''], 'chat_url': ['', '', ''], 'announcement_url': ['', ''], 'twitter_screen_name'
    #telegram_channel_identifier
    #'image': {'thumb': 'https://assets.coingecko.com/coins/images/12033/thumb/683JEXMN_400x400.png?1596698919', 'small': 'https://assets.coingecko.com/coins/images/12033/small/683JEXMN_400x400.png?1596698919', 'large':

import requests
import shutil

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
    download_file(url_img, cid + '.jpeg')


#show_syms()
cid = 'shopping-io'
download_logo(cid)

#telegram_channel_identifier
#https://assets.coingecko.com/coins/images/13574/large/nftx.png
#https://assets.coingecko.com/coins/images/13573/large/Lido_DAO.png
#//https://raw.githubusercontent.com/mcaps-com/registry/master/tokens/LDO/logo.png