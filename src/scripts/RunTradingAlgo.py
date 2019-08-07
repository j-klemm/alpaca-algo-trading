import alpaca_trade_api as tradeapi
import configparser

configFile = 'resources/api-config.properties'
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

print(api.get_account())
