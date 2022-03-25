

# QVY-Insurance
QVY-Insurance Web App TCS Case Study


# Project Setup

    # Install Python3 & VS Code on your PC
    # Open CMD and enter following commands
    
    git clone https://github.com/saipavannagireddy/QVY-Insurance.git
    cd QVY-Insurance
    pip install virtualenv
    virtuealenv venv
    code .
    
    # Enter the following commands in VS Code Terminal
    venv/Scripts/activate
    pip install -r requirements.txt
    
# Run App

    # Enter the following commands in VS Code Terminal
    set FLASK_APP=src
    set FLASK_ENV=development
    flask run

# App Usage
Go to http://127.0.0.1:5000/ (Address & Port may vary. Please check console after flask run command)
## Available Routes
/ - Home Page
/login - Login Page
/register - Customer Registration Page
/home - Customer Home page
/choose-policy - Choose Policy Page
