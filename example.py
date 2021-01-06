from coingecko import CoinGeckoAPI

cgapi = CoinGeckoAPI()
x = cgapi.get_coin_by_id('lido-dao')
print (x['name'])
print (x['links']['homepage'])
print (x['image']['large'])
#telegram_channel_identifier