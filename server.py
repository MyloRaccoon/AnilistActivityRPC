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

    def __init__(self, on_activity_changed=None):
        self.rpc = RPC()
        self.activity = None
        self.on_activity_changed = on_activity_changed

    def manual_update(self) -> Activity:
        self.activity = get_last_activity(ANILIST_USERID)
        self.rpc.update(self.activity)
        if self.on_activity_changed:
            self.on_activity_changed()

        log(f'RPC updated, new activity: {self.activity}')


    def run(self, stop_event):

        log('AniList Discord RPC Launched')

        self.manual_update()

        log('RPC active')

        while not stop_event.is_set():
            new_activity = get_last_activity(ANILIST_USERID)
            if self.activity != new_activity:
                self.activity = new_activity
                self.rpc.update(activity)
                if self.on_activity_changed:
                    self.on_activity_changed()

                log(f'RPC updated, new activity: {self.activity}')
            time.sleep(UPDATE_FREQUENCE)

        self.rpc.close()
        log('RPC Closed')
        log('AniList Discord RPC stopped')
