# Carriage Challange

## How to run API
### Install dependencies
Use `virtualenv` to create sandbox environment
#### step 1: Install virtualenv
`pip install virtualenv`
#### step 2: Create virtualenv
``` bash
virutalenv -p $(which python3) carriage
source carriage/bin/activate
```
#### step 3: Install depandencies
`pip install -r requirements.txt`

### Run API
Browse to project dir and run this command
`python manage.py runsever`

### Run client code
Browse to project dir and run this command `python client.py`