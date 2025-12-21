from pystray import Icon, Menu, MenuItem 
from PIL import Image
import threading
import server
from dotenv import load_dotenv
from os import getenv

load_dotenv()
ICON_PATH = getenv('ICON_PATH')

stop_event = threading.Event()

app = server.App()


def on_update_clicked(icon, item):
	app.manual_update()

def on_quit_clicked(icon, item):
	stop_event.set()
	icon.stop()


threading.Thread(
	target=app.run,
	args=(stop_event,),
	daemon=True
).start()


icon = Icon(
	'AniList Activity RPC',
	icon= Image.open(ICON_PATH),
	menu= Menu(
		MenuItem('Update', on_update_clicked),
		MenuItem('Quit', on_quit_clicked)
	)
)

icon.run()