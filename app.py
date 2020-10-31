import webview
from server import app
webview.create_window('Flask example', app)
webview.start()