# Carriage Challange

## How to run API
### Install dependencies
Use `virtualenv` to create sandbox environment
#### step 1: Install virtualenv
`pip install virtualenv`
#### step 2: Create virtualenv
`virutalenv -p $(which python3) carriage`
#### step 3: Activate virutalenv
`source carriage/bin/activate`
#### step 4: Install depandencies
`pip install -r requirements.txt`

### Run API
Browse to project dir and run this command and make sure virutalenv is activated

`python manage.py runsever`

### Run client code
Browse to project dir and run this command and make sure virutalenv is activated

`python client.py`