
from coingecko import CoinGeckoAPI

cgapi = CoinGeckoAPI()

#xid = "0-5x-long-algorand-token"
xid = "usd-coin"
info = cgapi.get_coin_by_id(xid)
#print (info)
print (info.keys())
print (info['contract_address'])
# print (info['developer_data'])

# l = cgapi.get_coins_list()
# for x in l:
#     #print (x)
#     if x['id'][0] == "u":
#         print (x)