from gevent import pywsgi
from app import app
server = pywsgi.WSGIServer(('0.0.0.0', 2024), app)
print('Running...')
server.serve_forever()
