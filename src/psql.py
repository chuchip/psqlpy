import psycopg2

import yaml
import logging
import sys
import os

logging.basicConfig(level=logging.INFO)

cfgFile=os.environ.get('CONFIG_FILE','config.yml')
yaml_file= open(cfgFile,"r")
cfg=yaml.load(yaml_file, Loader=yaml.FullLoader)

conn = None
try:
    cfgPost=cfg['postgres']

    host=os.environ.get('DB_HOST',cfgPost["host"])
    port=os.environ.get('DB_PORT',cfgPost["port"])
    database=os.environ.get('DB_DATABASE',cfgPost["database"])
    user=os.environ.get('DB_USER',cfgPost["user"])
    password=os.environ.get('DB_PASSWORD',cfgPost["password"])

    logging.info("Intentando conectar a base de datos Host: {} Puerto: {} database: {} user {}  ".format(host,port,database,user))
    conn = psycopg2.connect(host=host, port =port, database=database, 
        user=user, password=password)
    logging.info('Conectado a base de datos')
    cur = conn.cursor()
    
    for sql in cfg['sql']:
        logging.info("Ejecuantando sentencia {}".format(sql))
        try:
            cur.execute(sql)
        except ( psycopg2.DatabaseError  ) as errorsql:
            logging.error("Error al ejecutar sentencia {}".format(errorsql))
            conn.close()
            sys.exit(1)        
    conn.commit()
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
        logging.error("Error al conectar a base de datos: ",error)
finally:
        if conn is not None:
            conn.close()
            logging.info('Database connection closed.')
