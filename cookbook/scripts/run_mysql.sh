docker run -d \
  -e MYSQL_ROOT_PASSWORD=bitca \
  -e MYSQL_DATABASE=bitca \
  -e MYSQL_USER=bitca \
  -e MYSQL_PASSWORD=bitca \
  -p 3306:3306 \
  -v mysql_data:/var/lib/mysql \
  -v $(pwd)/cookbook/mysql-init:/docker-entrypoint-initdb.d \
  --name mysql \
  mysql:8.0
