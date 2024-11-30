import mimetypes
import socket

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = INTERNAL_IPS = [ip[:-1] + "1" for ip in ips] + ["127.0.0.1"]
mimetypes.add_type("application/javascript", ".js", True)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
    "INSERT_BEFORE": "</head>",
    "RENDER_PANELS": True,
}
