from pypresence import Presence, ActivityType
from anilist_model import Activity
from dotenv import load_dotenv
from os import getenv

load_dotenv()
CLIENT_ID = getenv('CLIENT_ID')

class RPC:

	def __init__(self):
		self.presence = Presence(CLIENT_ID)
		self.presence.connect()

	def update(self, activity: Activity):
		self.presence.update(
			activity_type=ActivityType.WATCHING,
			large_image='anilist_logo_svg',
			name=activity.title,
			details='Last AniList activity',
			state=activity.__str__(),
			buttons=[
				{
					'label': 'see on AniList',
					'url': activity.site_url
				}
			]
		)