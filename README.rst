#########
Flask
#########

Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.

----

License
=======

All relevant legal information can be found here

* https://www.palletsprojects.com/governance/licenses-and-copyright/



Installation
============

The name of the application you are going to set up is called **basic_flask_template**. If you wish to use another name make sure to replace **basic_flask_template** in all of the following steps with the name of your choice.



Create the application directory
-----------------------------------------

::

  [isabell@stardust ~]$ mkdir basic_flask_template
  [isabell@stardust ~]$

Alternatively clone this repo which comes with all the files you need for this tutorial: https://github.com/bwiessneth/basic_flask_template.git



Setup python environment and install required packages
------------------------------------------------------

You definitely want to create a isolated python environment. That way the required packages you are going to install with ``pip`` are encapsulated form your systemwide python installation.

::

  [isabell@stardust ~]$ cd basic_flask_template
  [isabell@stardust basic_flask_template]$ virtualenv -p python3 ENV
  [isabell@stardust basic_flask_template]$ pip install -r deploy/requirements.txt
  [isabell@stardust basic_flask_template]$ 

For more info check https://virtualenv.pypa.io/en/latest/

You can activate your new python environment like this:

::

  [isabell@stardust basic_flask_template]$ source ENV/bin/activate
  (ENV) [isabell@stardust basic_flask_template]$

Once you're done playing with it, deactivate it with the following command:

::
  
  (ENV) [isabell@stardust basic_flask_template]$ deactivate
  [isabell@stardust basic_flask_template]$ 



Setup nginx
-----------

Create an endpoint where the app will be served from. I chose that my application **basic_flask_template** should run be served using http under ``/basic_flask_template`` using port ``1024``.

On uberspace you'll want to use the built-in ``uberspace`` tool.

:: 

  [isabell@stardust ~]$ uberspace web backend set /basic_flask_template --http --port 1024


Start your application 
----------------------

Using Werkzeug for development
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use Werkzeug which get's shipped with Flask to spin up a small development server. But be aware: **Do not use it in a production deployment.** For more info head to https://www.palletsprojects.com/p/werkzeug/.

::

  [isabell@stardust basic_flask_template]$ ./run_werkzeug.sh
   * Serving Flask app "app" (lazy loading)
   * Environment: production
     WARNING: This is a development server. Do not use it in a production deployment.
     Use a production WSGI server instead.
   * Debug mode: on
   * Running on http://0.0.0.0:1024/ (Press CTRL+C to quit)
   * Restarting with stat
   * Debugger is active!
   * Debugger PIN: 262-417-928
  [isabell@stardust basic_flask_template]$ ^C
  [isabell@stardust basic_flask_template]$




UWSGI
^^^^^

:: 
  [isabell@stardust basic_flask_template]$ ./run_uwsgi.sh


Use supervisord to monitor and control your processes 
-----------------------------------------------------

::

  [isabell@stardust ~]$ cp basic_flask_template/deploy/basic_flask_template.ini ~/etc/services.d/
  [isabell@stardust ~]$ supervisorctl reread
  [isabell@stardust ~]$ supervisorctl update
  [isabell@stardust ~]$ supervisorctl status basic_flask_template
  [isabell@stardust ~]$ supervisorctl stop basic_flask_template
  [isabell@stardust ~]$ supervisorctl start basic_flask_template
  [isabell@stardust ~]$ 
