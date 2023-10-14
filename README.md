# sqlserver
Bare minimum sqlserver in docker with client tools


`docker build --no-cache -t sqlserver-2022:v1 .`
`docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=Passw0rd' -p 1433:1433 -d --name sqlserver-2022 sqlserver-2022:v1`
`docker run -d -t <CONTAINER>`      #keep the container running (tty)

`docker-compose build`
`docker-compose run sqlservr-2022`
`docker-compose up -d`