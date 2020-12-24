Pequeño programa en Python que se conecta con una base de datos postgres y ejecuta los parametros existentes en "**config.yml**" bajo el apartado "**sql**"

El fichero de configuración se puede especificar con la variable de entorno **CONFIG_FILE**.

La conexion a la base de datos se puede configurar con estas variables de entorno. 

 - DB_HOST
 - DB_PORT
 - DB_DATABASE
 - DB_USER
 - DB_PASSWORD

Por defecto los parametros de conexion y las setencias a ejecutar son estas:

``` 
postgres:
 host: localhost
 port: 5432
 database: prueba
 user: postgres
 password: example
sql: 
  - delete from tabla1
  - insert into tabla1 values(1,'aa')
  - insert into tabla1 values(2,'bb')
```

Creación imagen docker: 

    docker build -t psql .


Ejemplo de uso: 

    docker  run -e DB_HOST=192.168.80.174 -it  psql