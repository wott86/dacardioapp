# dacardioapp

[TOC]

## Install instructions

Create a [virtual environment](https://virtualenv.pypa.io/en/latest/) with these commands

```
$ cd /path/to/project/root/
$ virtualenv .env
$ source .env/bin/activate # this activates your virtual environment

```

Then, install requirements files in __conf/requirements.txt__ (virtual env must be activated)

```
(.env)$ pip install -r conf/requirements.txt

```

### Setup database

Create a database in postgres, use the name you want

Add __postgis__ extension to database, if you are using pgadmin3, just right click over database and then select __add extension__ menu item.

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

```
(.env)$ ./manage.py syncdb

```

It will ask you if you want to create a superuser, say yes and fill data required.


### Cities

[Django cities](https://github.com/coderholic/django-cities) is a django plugin wich contains info about countries, regions, postal codes and of course, cities.

After setting up database you must fill cities data

```
$ source .env/bin/activate
(.env)$ ./manage.py cities --import=all

```

It will take some time, have a cup of coffee, a snack and read a book.