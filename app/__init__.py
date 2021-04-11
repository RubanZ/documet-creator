import sentry_sdk
from flask import Flask
from flask_cors import CORS
from sentry_sdk.integrations.flask import FlaskIntegration

# sentry_sdk.init(
#     dsn="https://8fa3bc66a2b44bceb1f08a37bf6eae93@o503776.ingest.sentry.io/5694402",
#     integrations=[FlaskIntegration()],

#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     # We recommend adjusting this value in production.
#     traces_sample_rate=1.0
# )
application = Flask(__name__)
CORS(application)

# from app import routes
from .routes import test, doc