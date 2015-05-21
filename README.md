# dacardioapp

[TOC]

## Install instructions

Create a [virtual environment](https://virtualenv.pypa.io/en/latest/) with these commands

```bash
$ cd /path/to/project/root/
$ virtualenv .env
$ source .env/bin/activate # this activates your virtual environment

```

Then, install requirements files in __conf/requirements.txt__ (virtual env must be activated)

```bash
(.env)$ pip install -r conf/requirements.txt

```

### Setup database

Create a role and a database in postgres, use the name you want

In our example we use dacardiouser and dacardiodb, you can change it to any names you like.

Creating role

```SQL
CREATE ROLE dacardiouser LOGIN
  ENCRYPTED PASSWORD 'md58d856455f3a6138c3e0f7da406bb3d14'
  NOSUPERUSER INHERIT CREATEDB NOCREATEROLE NOREPLICATION;
```

Creating database
```SQL
CREATE DATABASE dacardiodb
  WITH OWNER = dacardiouser
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'en_US.UTF-8'
       LC_CTYPE = 'en_US.UTF-8'
       CONNECTION LIMIT = -1;
```

Add __postgis__ extension to database, you need to install it before

	Important: postgresql-9.3-postgis-scripts is only needed in Ubuntu 14.04, just in case it fails in another distro don't pay atention to it.


```bash
$ sudo apt-get install postgis postgresql-9.3-postgis-scripts
```


If you are using pgadmin3, just right click over database and then select __add extension__ menu item.


If not using pgadmin3, use the console

```
$ sudo su - postgres
$ psql -d <DATABASE_NAME>
# CREATE EXTENSION postgis;
# \q

```

Create a file named __local_settings.py__ in project root and include your database settings

```
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'dacardio',                      # database name
        'USER': 'dacardio',                      # database user
        'PASSWORD': '34gregrr',                  # database password
        'HOST': 'localhost',                     # database server
        'PORT': ''                               # empty for default
    }
}

```

After setting database, activate virtual environment if not active and sync database, this will create all the tables

```bash
(.env)$ ./manage.py syncdb

```

It will ask you if you want to create a superuser, say yes and fill data required.


### Cities

[Django cities](https://github.com/coderholic/django-cities) is a django plugin wich contains info about countries, regions, postal codes and of course, cities.

After setting up database you must fill cities data

```bash
$ source .env/bin/activate
(.env)$ ./manage.py cities --import=all

```

It will take some time, have a cup of coffee, a snack and read a book.

### Installing static dependencies

#### Setting up Nodejs and Bower

Install [Nodejs](https://nodejs.org/), last version at the moment is 0.12, you can find installing instructions [here](https://nodesource.com/blog/nodejs-v012-iojs-and-the-nodesource-linux-repositories) (for Linux)

After installing Nodejs, you need to install [Bower](http://bower.io/) in order to get static libraries dependencies (Bootstrap, JQuery, etc)

```bash
$ npm install -g bower
```

Then go to app __static__ folder and install dependencies

```bash
$ cd /path/to/app/static/
$ bower install
```

#### Linking admin static files

In case you are running this app as a wsgi app, you need to link admin static files, otherwise this step can be ignored.

Remember to change __path_to_your_virtual_env__ to your .env folder path and __path_to_your_app__ to your app folder.

```bash
$ ln -s /path_to_your_virtual_env/lib/python2.7/site-packages/django/contrib/admin/static/admin/ /path_to_your_app/static/
```

### Running app

First, activate virtualen if not already activated, ant then run server


```bash
$ source .env/bin/activate
(.env)$ ./manage.py runserver

```

__Important__: this is a development server, not suitable for production environment or massive usage. In order to use it as a production server, you will need [Gunicorn](http://gunicorn.org/) or any other wsgi server. And you will also need a HTTP server, such as [Nginx](http://nginx.org/) (I recommend this one) or [Apache](http://httpd.apache.org/).

### Deployment

__Following steps are only for deployment, in development mode this is completely optional__

## Roadmap

+ Finish deployment docs
