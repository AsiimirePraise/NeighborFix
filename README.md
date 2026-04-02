# NeighborFix

NeighborFix is a **neighborhood issue tracker**: residents report street problems (potholes, lighting, sanitation, safety), track status from open through resolved, and keep everything in one transparent queue—similar in spirit to professional service sites, built for reliability on **PostgreSQL** and **Railway**.

---

## Run the app and open the UI (Windows)

Use **PowerShell** in the project folder (e.g. `D:\New folder\NeighborFix`).

**1. Virtual environment and dependencies**

```powershell
cd "D:\New folder\NeighborFix"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**2. Database (creates `instance\neighborfix.db` with SQLite)**

```powershell
$env:FLASK_APP = "wsgi:app"
flask db upgrade
```

**3. (Optional) Starter reports** so the list is not empty on first load:

```powershell
flask seed
```

**4. Start the server**

```powershell
flask run
```

**5. Open the site**

In your browser go to: **http://127.0.0.1:5000/**

You should see the home page, **Reports**, and **Report an issue**. Use **Ctrl+C** in the terminal to stop the server.

---

## Stack

- **Backend:** Python / Flask  
- **Database:** PostgreSQL in production (Railway); local dev uses SQLite in `instance/neighborfix.db` when `DATABASE_URL` is not set  
- **Migrations:** Flask-Migrate (Alembic)  
- **Deploy:** Railway + GitHub (set `SECRET_KEY` and `DATABASE_URL` in production)

### Environment variables

| Variable | Purpose |
|----------|---------|
| `SECRET_KEY` | Required in production for sessions and flashes |
| `DATABASE_URL` | PostgreSQL URL (Railway). Omit locally to use SQLite |

Copy `.env.example` to `.env` and adjust (do not commit `.env`).

---

## License

Educational / course use where applicable.
