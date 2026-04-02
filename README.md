# NeighborFix

Neighborhood issue tracker — report local problems (potholes, streetlights, noise) and track status. Built for coursework: **Railway PaaS**, Postgres, and CI/CD.

## Stack

- **Backend:** Python / Flask  
- **Database:** PostgreSQL on Railway (local dev uses SQLite in `instance/neighborfix.db` when `DATABASE_URL` is unset)  
- **ORM / migrations:** Flask-SQLAlchemy, Flask-Migrate (Alembic)  
- **Deploy:** Railway + GitHub auto-deploy  

## Local setup

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

Apply migrations and optionally load three demo rows:

```bash
set FLASK_APP=wsgi:app
flask db upgrade
flask seed-demo
```

(PowerShell: `$env:FLASK_APP = "wsgi:app"` before the `flask` commands.)

## License

Course project — educational use.
