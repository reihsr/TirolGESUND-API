from flask import render_template
from models import Participant, ParticipantSchema
from jproperties import Properties

import config

configsProperty = Properties()
with open('config.properties', 'rb') as config_file:
    configsProperty.load(config_file)

# Get the application instance
connex_app = config.connex_app
# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")
app = connex_app.app


@connex_app.route('/')
def hello_world():
    return render_template("home.html")


if __name__ == '__main__':
    connex_app.run(host=configsProperty.get("HOST").data, debug=configsProperty.get("DEBUG").data)
