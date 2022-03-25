from flask import (Blueprint,
                   url_for,
                   redirect,
                   request,
                   render_template,
                   current_app,
                   abort
                   )


home = Blueprint('home', __name__,
                  template_folder='templates',
                  static_folder='static',
                  static_url_path='/static/'
                  )

@home.route("/")
def home_page():
    return render_template('/home.html')