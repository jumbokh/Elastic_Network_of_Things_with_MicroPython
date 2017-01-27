# coding: utf-8

import sys

# 'esp8266' or 'win32'
# SYS_PLATFORM = sys.platform

# 'micropython' or 'cpython'
# SYS_IMPLEMENTATION = sys.implementation.name
IS_MICROPYTHON = sys.implementation.name == 'micropython'
 

# DEBUG_MODE = True



# Shared ************************
## Must config ******************
HUB_PORT = 9662
## Must config ******************
SERVER_NAME = 'Hub'
BUFFER_SIZE = 4096
PACKAGE_START = b'---PACKAGE_START---'
PACKAGE_END = b'---PACKAGE_END---'



# Hub ***************************
## Must config ******************
BIND_IP = '0.0.0.0'   # the ip which broker listens to.
## Must config ******************
MAX_CONCURRENT_CONNECTIONS = 200
SERVER_POLLING_REQUEST_TIMEOUT_SECONDS = 60 
HEART_BEAT_PROBING_PER_SECONDS = 60  



# Client ************************
## Must config ******************
BROKER_HOST = '192.168.0.105'
## Must config ******************
CLIENT_RETRY_TO_CONNECT_AFTER_SECONDS = 3
CLIENT_RECEIVE_TIME_OUT_SECONDS = 1
REQUESTS_NEED_RESULT_TIME_TO_LIVE = 60
ASYNCH_RESULT_TIMEOUT = 3
ASYNCH_RESULT_RETRY_DELAY = 0.01  
MICROPYTHON_SOCKET_CONNECTION_RESET_ERROR_MESSAGE = '[Errno 104] ECONNRESET' 
MICROPYTHON_SOCKET_RECEIVE_TIME_OUT_ERROR_MESSAGE = 'timed out' 

