import alpaca_trade_api as tradeapi
import configparser

configFile = '../resources/private-info.properties' #CHANGE TO api-config.properties or your own config file
config = configparser.RawConfigParser()
config.read(configFile)

keyid = config.get('Config', 'keyid')
secretKey = config.get('Config', 'secretkey')
endpoint = config.get('Config','endpoint')

api = tradeapi.REST(
    key_id=keyid,
    secret_key=secretKey,
    base_url=endpoint
)


#api.submit_order('AAPL',5,'buy','market','gtc') #Uncomment to purchase 5 shares of Apple
#print(api.list_positions()) #Uncomment to see current stock positions

print(api.get_barset('MSFT','1D'))
print(api.get_account()) #Uncomment to see account info

