from flask import Flask
from flask_cors import CORS

from app_container.controllers.data_source_controller import data_source_controller
from app_container.controllers.query_controller import query_controller
from app_container.controllers.metric_controller import metric_controller
from app_container.controllers.auth_controller import auth_controller
from app_container.controllers.organization_controller import organization_controller
from app_container.controllers.user_controller import user_controller


app = Flask(__name__)
CORS(app)


app.register_blueprint(data_source_controller, url_prefix='/data-source')
app.register_blueprint(query_controller, url_prefix='/query')
app.register_blueprint(auth_controller, url_prefix='/auth')
app.register_blueprint(organization_controller, url_prefix='/organization')
app.register_blueprint(user_controller, url_prefix='/user')
app.register_blueprint(metric_controller, url_prefix='/metric')


if __name__ == '__main__':
    app.run()
