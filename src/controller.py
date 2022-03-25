from flask import (Blueprint,
                   url_for,
                   redirect,
                   request,
                   render_template,
                   current_app,
                   abort
                   )


app = Blueprint('routes', __name__,
                  template_folder='templates',
                  static_folder='static',
                  static_url_path='/static/'
                  )

@app.route("/")
def index():
    return render_template('/home.html')

@app.route("/login")
def login_page():
    return render_template("/login.html")

@app.route("/login", methods=["POST"])
def login_submit():
    return redirect(url_for('routes.customer_home'))

@app.route("/register")
def register_page():
    return render_template("/register.html")

@app.route("/register", methods=["POST"])
def register_submit():
    print(request.form)
    id = request.form.get('cid')
    name = request.form.get('name')
    email = request.form.get('email')
    return render_template("/register-success.html", id=id, name=name, email=email)

@app.route("/home")
def customer_home():
    return render_template("customer-home.html")

@app.route("/choose-policy")
def choose_policy_page():
    return render_template("/choose-policy.html")

@app.route("/choose-policy", methods=["POST"])
def choose_policy_page_submit():
    return redirect(url_for('routes.customer_home'))

@app.route("/view-my-policies")
def view_policies_page():
    return render_template("/view-my-policies.html")