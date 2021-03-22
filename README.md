# sp_exchange_rates
This repo is a basic ETL mini project. The main ideas are:
- Fetch data from https://exchangeratesapi.io/
- Store it raw in the format retrieved
- Transform it and save into a csv file
- Load into a local DB
## local database install
`docker pull mysql:8`
`docker exec -i sp-mysql sh -c 'exec mysql -uroot -p"root"' < sp_mysql_load.sql`
`docker run --name sp-mysql -p 3306:3306 -h 127.0.0.1 -e MYSQL_ROOT_PASSWORD=root -d mysql:8`
docker pull mysql:8
