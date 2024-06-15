## Run program
### Migrations

create migrations folder
```bash
alembic init migrations
```

Auto generate the migrations

```bash
alembic revision --autogenerate -m "add cloumnName to table TableName"
```
Upgrade the Database
```bash
alembic upgrade head
```
