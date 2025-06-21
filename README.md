# D3 Baseball API

## Local Development

### Poetry
- Make sure you have poetry installed `brew install poetry`
- Install dependencies `poetry install`

### Docker
- Start containers `docker compose up -d`

### PGAdmin
- Open pgadmin by navigating to `http://localhost:5050`
- Login
    - Email: peterxavierolsen@gmail.com
    - Password: zZzd3baseball!
- Add the postgres server inside pgadmin
    - Name: anything you want (e.g. Local Docker DB)
    - Host: db
    - Port: 5432
    - Username: d3_base_user
    - Password: zZzd3baseball!
    - Save Password [X]

### DB Migrations (Yoyo)
- Apply migrations `poetry run yoyo apply`
- Check migrations `poetry run yoyo status`