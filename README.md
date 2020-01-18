# basic_flask_template
Basic flask template for quick deployment


## Setup python environment and install required packages

```
virtualenv -p python3 ENV
pip install -r deploy/requirements.txt
```


## Setup nginx 



## Use supervisord to monitor and control your processes 

```
cp deploy/basic_flask_template.ini ~/etc/services.d/
supervisorctl reread
supervisorctl update
supervisorctl status basic_flask_template
supervisorctl start basic_flask_template
supervisorctl stop basic_flask_template
```


# Random

```
pkill -F project_name.pid
```
