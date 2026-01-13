from pystray import Icon, Menu, MenuItem 
from PIL import Image
import threading
from server import Server
from dotenv import load_dotenv
from os import getenv
import os, sys

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

load_dotenv()
ICON_PATH = getenv('ICON_PATH')

stop_event = threading.Event()

server = Server()


def on_update_clicked(icon, item):
	server.manual_update()

def on_quit_clicked(icon, item):
	stop_event.set()
	icon.stop()


threading.Thread(
	target=server.run,
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