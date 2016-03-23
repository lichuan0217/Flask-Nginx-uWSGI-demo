Intro
=====

This is a simple demo web application using Flask, Nginx, uWSGI. This demo will guide you through the process of installing and configuring Nginx server and uWSGI to host Flask based applications.

Reference
----------
[Serving flask with nginx on ubuntu](http://vladikk.com/2013/09/12/serving-flask-with-nginx-on-ubuntu/)

Nginx
------

```shell
sudo add-apt-repository ppa:nginx/stable
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install nginx
```

Virtual Environment
-------------------

Install the virtualenv package:

```sudo apt-get install python-virtualenv```

Create and active a virtual environment:

```shell
cd /home/chuanl/code/flask/demo
virtualenv venv
source venv/bin/activate
```

Flask
------

Install Flask in virtual enviroment:

```pip install flask```


Flask-script
------------

We will use Flask-script to manage our Flask application:

```pip install Flask-script```


Manager and application files
--------------------------------

Create *manager.py* to handle flask.
*app* directory contains the flask appliction and configuration files.


Config Nginx
-------------

Remove the default configuration file of Nginx.

```shell
sudo rm /etc/nginx/site-enabled/default
#or
sudo rm /etc/nginx/conf.d/default
```

Link our Nginx configuration file to nginx.

```shell
sudo ln -s /home/chuanl/code/flask/demo/demo_nginx.conf /etc/nginx/conf.d/
sudo service nginx restart
```

Config uWSGI
-------------

*demo_uwsgi.ini* contains the configuration about our flask application.

Create a dirctory to store the uWSGI logs.

```shell
sudo mkdir -p /var/log/uwsgi
sudo chown chuanl:chuanl /var/log/uwsgi
```

Now we can start uWSGI, and access our flask application.

```shell
uwsgi --ini /home/chuanl/code/flask/demo/demo_uwsgi.ini
```
Access the applictioan by *localhost* in Chrome.


uWSGI Emperor
-------------

Using uWSGI Emperor, we can run our uwsgi background.

Create uWSGI Emperor configuration file in /etc/init/uwsgi.conf. (You can copy *demo_uwsgi_emperor.conf*)

In this configuration, we will find the uWSGI configuration files in /etc/uwsgi/vassals. So create this directory and link our uWSGI configuration file here.

```shell
sudo mkdir -p /etc/uwsgi/vassals
sudo ln -s /home/chuanl/code/flask/demo/demo_uwsgi.ini /etc/uwsgi/vassals
```

Now we can start or stop our uWSGI by command:

	sudo start uwsgi
	sudo stop uwsgi



