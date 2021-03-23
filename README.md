# sp_exchange_rates
This repo is a basic ETL mini project. The main ideas are:
- Fetch data from https://exchangeratesapi.io/
- Store it raw in the format retrieved
- Transform it and save into a csv file
- Load into a local DB
## Installation
- create a virtual enviroment with `python 3.8`
- Install  all depedendencies with `pip install -r requirements.txt`
- intall Docker if you wish to use a clean local DB otherwise just execute `sp_mysql_load.sql`
- [OPTIONAL] pull and install mysql 8 with Docker `docker pull mysql:8`
- [OPTIONAL]Create the container for the DB`docker exec -i sp-mysql sh -c 'exec mysql -uroot -p"root"' < sp_mysql_load.sql`
- [OPTIONAL]Execute some commands to create a fresh database schema and create the main table that we are going to work with `docker run --name sp-mysql -p 3306:3306 -h 127.0.0.1 -e MYSQL_ROOT_PASSWORD=root -d mysql:8`
- Last but not least create a local settings file called `settings.ini` in the root directory. It has to look something like this:
```

```
## Running the project
- run the ETL with `python src/main.py` that will run all  the processed
