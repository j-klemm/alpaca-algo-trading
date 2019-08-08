import alpaca_trade_api as tradeapi
import configparser
import datetime

configFile = '../resources/private-info.properties' #CHANGE TO api-config.properties or your own config file
config = configparser.RawConfigParser()
config.read(configFile)

keyid = config.get('Config', 'keyid')
secretKey = config.get('Config', 'secretkey')
tradingEndpoint = config.get('Config','endpoint')
dataEndpoint = 'https://data.alpaca.markets'

api = tradeapi.REST(
    key_id=keyid,
    secret_key=secretKey,
    base_url=tradingEndpoint
)

data = tradeapi.REST(
    key_id=keyid,
    secret_key=secretKey,
    base_url=dataEndpoint
)


#api.submit_order('AAPL',5,'buy','market','gtc') #Uncomment to purchase 5 shares of Apple
#print(api.list_positions()) #Uncomment to see current stock positions


#print(api.get_account()) #Uncomment to see account info
msftData = data.get_barset('MSFT','15Min',1000) #Gather data for last 38 days of trading for every 15 mins
msftDict = msftData['MSFT']

for bar in msftDict:
    print(str(bar.t.strftime('%m-%d %H:%M')) + ': ' + str(bar.o)) #Print all the 15 minute intervals with price at end of that interval