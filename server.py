from anilist_model import get_last_activity, get_user_id
from activity import Activity
from discord_rpc import RPC
from logger import log
from dotenv import load_dotenv
from os import getenv
import time

load_dotenv()
ANILIST_USERNAME=getenv('ANILIST_USERNAME')
ANILIST_USERID=get_user_id(ANILIST_USERNAME)
UPDATE_FREQUENCE=int(getenv('UPDATE_FREQUENCE'))


class Server:

    def __init__(self):
        self.rpc = RPC()

    def manual_update(self) -> Activity:
        activity = get_last_activity(ANILIST_USERID)
        self.rpc.update(activity)

        log(f'RPC updated, new activity: {activity}')

        return activity

    def run(self, stop_event):

        log('AniList Discord RPC Launched')

        activity = self.manual_update()

        log('RPC active')

        while not stop_event.is_set():
            new_activity = get_last_activity(ANILIST_USERID)
            if activity != new_activity:
                activity = new_activity
                self.rpc.update(activity)
                log(f'RPC updated, new activity: {activity}')
            time.sleep(UPDATE_FREQUENCE)

        self.rpc.clear()
        self.rpc.close()
        log('RPC cleared')
        log('AniList Discord RPC stopped')