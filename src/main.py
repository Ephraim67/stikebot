# Main Python Scripts
import json

def load_broker_config():
    with open("config/broker_config.json") as f:
        return json.load(f)
    
def load_bot_settings():
    with open("config/settings.json") as f:
        return json.load(f)
    
broker_config = load_broker_config()
bot_settings = load_bot_settings()