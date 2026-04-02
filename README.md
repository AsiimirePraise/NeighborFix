# NeighborFix · Uganda

NeighborFix is a **neighbourhood issue tracker** for **Uganda**: residents report street problems (potholes, lighting, drainage, waste), track status from open through resolved, and keep everything in one transparent queue. The UI uses a **greyscale** design (no brand accent colours) for clarity and fast loading.

Default examples reference **Kampala**, **Entebbe**, **Jinja**, and other towns; you can report from any ward or district your deployment serves.

---

## Run the app and open the UI (Windows)

Use **PowerShell** in the project folder.

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

**3. (Optional) Starter reports**

```powershell
flask seed
```

**4. Start the server**

```powershell
flask run
```

**5. Open the site**

**http://127.0.0.1:5000/** — times shown in the app follow **East Africa Time (EAT, UTC+3)** when you host in-region.

---

## Stack

- **Backend:** Python / Flask  
- **Database:** PostgreSQL in production (Railway); local dev uses SQLite in `instance/neighborfix.db` when `DATABASE_URL` is not set  
- **Migrations:** Flask-Migrate (Alembic)  

### Environment variables

| Variable | Purpose |
|----------|---------|
| `SECRET_KEY` | Required in production for sessions and flashes |
| `DATABASE_URL` | PostgreSQL URL. Omit locally to use SQLite |

Copy `.env.example` to `.env` and adjust (do not commit `.env`).

---

## License

Educational / course use where applicable.
