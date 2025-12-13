from anilist_model import get_last_activity, get_user_id
from discord_rpc import connect_rpc, update_rpc
from dotenv import load_dotenv
from os import getenv
import time

load_dotenv()
ANILIST_USERNAME=getenv('ANILIST_USERNAME')
ANILIST_USERID=get_user_id(ANILIST_USERNAME)
UPDATE_FREQUENCE=int(getenv('UPDATE_FREQUENCE'))

rpc = connect_rpc()

activity = get_last_activity(ANILIST_USERID)

update_rpc(rpc, activity)

print('rpc active')

try:
    while True:
        new_activity = get_last_activity(ANILIST_USERID)
        if activity != new_activity:
            activity = new_activity
            update_rpc(rpc, activity)
            print('rpc updated')
        time.sleep(UPDATE_FREQUENCE)
except KeyboardInterrupt:
    rpc.clear()
    rpc.close()
