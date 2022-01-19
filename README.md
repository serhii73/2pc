# Робота з розподіленими (двофазними) транзакціями

[The task](https://docs.google.com/document/d/1761CvJCks_f_2hrAH7nHjL4fRggpS1rHkBs6YkFgl-o/edit)

## Create db table

Commands to create the db table:

> docker ps 

Used to identify the CONTAINER ID of postgres

> docker exec -it <CONTAINER_ID> bash

> psql postgres://username:secret@localhost:5432/database
