import requests
from activity import Activity

URL = "https://graphql.anilist.co"

def get_user_id(name: str) -> int|None:
	query = """
	query ($name: String!) {
	  User(name: $name) {
	    id
	  }
	}
	"""
	variables = {
		"name": name,
		"userId": 7416947
	}

	response = requests.post(
		URL,
		json={"query": query, "variables": variables}
	)
	data = response.json()

	if data.get('errors'):
		print('Error: Anilist user "{name}" not found')
		return None

	return int(data['data']['User']['id'])


def get_last_activity(userId: int) -> Activity|None:
	query = """
	query ($userId: Int) {
	  Page(page: 1, perPage: 2) {
		activities(userId: $userId, sort: ID_DESC, type: MEDIA_LIST) {
		  ... on ListActivity {
		    id
			status
			progress
			media {
			  title { romaji }
			}
		  }
		}
	  }
	}
	"""
	variables = {
		"userId": userId
	}

	response = requests.post(
		URL,
		json={"query": query, "variables": variables}
	)
	data = response.json()

	if data.get('errors'):
		print(f'Error while getting activities: {data['errors'][0]['message']}')
		return None

	activity_data = data['data']['Page']['activities'][0]
	_id = activity_data['id']
	status = activity_data['status']
	progress = activity_data['progress']
	title = activity_data['media']['title']['romaji']
	return Activity(
		_id,
		status,
		title,
		progress
	)