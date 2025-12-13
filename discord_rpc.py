from pypresence import Presence, ActivityType
from anilist_model import Activity
from dotenv import load_dotenv
from os import getenv

load_dotenv()
CLIENT_ID = getenv('CLIENT_ID')


def connect_rpc() -> Presence:
	rpc: Presence = Presence(CLIENT_ID)
	rpc.connect()
	return rpc

def update_rpc(rpc: Presence, activity: Activity):
	rpc.update(
		activity_type=ActivityType.WATCHING,
		large_image='anilist_logo_svg',
		name=activity.__str__(),
		details='Last AniList activity',
		state=activity.__str__(),
		buttons=[
			{
				'label': 'Voir sur AniList',
				'url': activity.site_url
			}
		]
	)