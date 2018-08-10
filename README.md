### Prerequisites
* [Python 3.7](https://www.python.org/downloads/release/python-370/)
* [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/)

### Installation
```
$ git clone git@github.com:bmwant/escot.git
$ cd escot
$ mkvirtualenv -p python3.7 escot
$ pip install -r requirements.txt
```

### Launch
* Make sure `REQUIRED FIELDS` section is filled in your `config_local.py` file
```
$ workon escot
$ python runserver
``` 

### Work manually with Telethon
```
$ pip install Telethon==1.1.1
```
See `scripts` directory and [docs](https://github.com/LonamiWebs/Telethon).
