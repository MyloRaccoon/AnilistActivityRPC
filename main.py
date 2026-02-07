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

def on_title_clicked(icon, item):
	if server.activity:
		os.open(server.activity.site_url)

def build_menu():
	return Menu(
		MenuItem(
			lambda item: server.activity.title if server.activity else "loading...", 
			action= None,
			enabled=False
		),
		MenuItem('Update', on_update_clicked),
		MenuItem('Quit', on_quit_clicked)
	)

icon = Icon(
	name='AniList Activity RPC',
	icon= Image.open(ICON_PATH)
)

def update_menu():
	icon.menu = build_menu()
	icon.update_menu()

server.on_activity_changed = update_menu
threading.Thread(
	target=server.run,
	args=(stop_event,),
	daemon=True
).start()

icon.run()