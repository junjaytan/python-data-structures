pip install virtualenv

cd my_project_folder
virtualenv venv

# you can also use a Python interpreter of your choice
virtualenv -p /usr/bin/python2.7 venv

# to begin using it needs to be activated
source venv/bin/activate
pip install requests
deactivate

# export requirements
pip freeze > requirements.txt

# import requirements
pip install -r requirements.txt
