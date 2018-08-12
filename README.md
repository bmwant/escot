### Prerequisites
* [Python 3.7](https://www.python.org/downloads/release/python-370/)
* [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/)
* [npm](https://www.npmjs.com/get-npm)

### Installation
```
$ git clone git@github.com:bmwant/escot.git
$ cd escot
$ mkvirtualenv -p python3.7 escot
$ pip install -r requirements.txt
$ npm install
```

### Launch
* Make sure `REQUIRED FIELDS` section is filled in your `config_local.py` file
```
$ workon escot
$ python runserver
``` 

### Launching auxiliary scripts
```
$ pip install -r requirements-dev.txt
```
See `scripts` directory and [docs](https://github.com/LonamiWebs/Telethon).


### Deployment
```
$ pip install -r requirements-dev.txt
$ cd deployment
$ ansible-playbook -vv init.yml  # for the first time
$ ansible-playbook update.yml  # when doing updates
```
