import imp
from flask import Flask, render_template
from .controllers.home import home
from datetime import datetime


def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('..\config.py')
    
    # Jinja custom filters
    @app.add_template_filter
    def extract_date(date_time):
        return date_time.date()

    @app.add_template_filter
    def extract_time(date_time):
        return date_time.time()

    @app.add_template_filter
    def convert_time_24_to_12(time):
        if type(time) != type(" "):
            time = str(time)
        if '.' in time:
            time = time.split(".")[0]
        time_obj = datetime.strptime(time, "%H:%M:%S")
        return time_obj.strftime("%I:%M %p")

    @app.add_template_filter
    def get_month(date_time):
        return date_time.strftime("%b")

    @app.add_template_filter
    def get_date_day(date_time):
        return date_time.strftime("%d")

    # Registring blueprints
    app.register_blueprint(home)
    
    # Error Handlers
    def bad_request(e):
        return render_template('errors/400.html'), 400

    def unauthorized(e):
        return render_template('errors/401.html'), 401

    def forbidden(e):
        return render_template('errors/403.html'), 403

    def page_not_found(e):
        return render_template('errors/404.html'), 404

    def internal_server_error(e):
        return render_template('errors/500.html'), 500

    app.register_error_handler(400, bad_request)
    app.register_error_handler(401, unauthorized)
    app.register_error_handler(403, forbidden)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)
 
    return app


APP = create_app()