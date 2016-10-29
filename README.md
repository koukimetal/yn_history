**Set up**

* $ docker-compose build
* $ docker-compose up
* Access http://localhost:5000 or http://0.0.0.0:5000

**What this project does**

* cron
    * Every 30min, access to yah** news
    * Get lists of news
    * Push them to mongodb
* web
    * Show list of news in mongodb

**Set up with debugger for Intellij or PyCharm**

* $ source ./setup_debug.sh
* Make Remote Python Debug with ip = you got above command($DOCKER0_IP), port = 5678 or port = 5679
* $ docker-compose build
* Start Remote Python Debug
* $ docker-compose up
* Access http://localhost:5000 or http://0.0.0.0:5000