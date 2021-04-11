import os
from app import application


if __name__ == "__main__":    
    application.debug = True
    application.run(host="localhost", port=5555) #host='0.0.0.0', port=80 ssl_context='adhoc'