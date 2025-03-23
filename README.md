# grid-cloud-task1
## Description
Simple Django web-server with PosgreSQL database wrapped in Docker container
## Building and launching
Open root folder in terminal and type following commands
```
docker build . -t myapp
docker-compose up --build
```
## Requests
* `curl -X GET "http://localhost:8000/"` - returns string representation of all entries of main relation
* `curl -X POST "http://localhost:8000/{text}/"` - to insert a new entry in main relation. Replace `{text}` with your own string
