# NeighborFix · Uganda

NeighborFix is a **neighbourhood issue tracker** for **Uganda**: residents report street problems (potholes, lighting, drainage, waste), track status from open through resolved, and keep everything in one transparent queue. The UI is **greyscale-first** with a single **accent** colour for actions and focus.

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

**2. Database migrations**

```powershell
$env:FLASK_APP = "wsgi:app"
flask db upgrade
```

**3. Optional seed data**

- **`flask seed`** — sample **issues** plus default **staff** users (if tables are empty).
- **`flask seed-admins`** — only default staff users in **`admin_users`** (if empty).

```powershell
flask seed
```

Default staff logins (hashed in the database): **asiimire** and **Pearl**, password **1234** each. Change these in production.

**4. Start the server**

```powershell
flask run
```

**5. URLs**

| URL | Purpose |
|-----|---------|
| **http://127.0.0.1:5000/** | Home (fixed Unsplash background; text stays readable while scrolling) |
| **http://127.0.0.1:5000/admin** | Staff dashboard — sign in, then update **issues.status** |

If **/admin** returned 404 before, pull latest code, run **`flask db upgrade`**, then **`flask seed-admins`**, and use **`http://127.0.0.1:5000/admin`** (with or without a trailing slash).

---

## Stack

- **Backend:** Python / Flask  
- **Database:** PostgreSQL in production (Railway); local dev uses SQLite in `instance/neighborfix.db` when `DATABASE_URL` is not set  
- **Migrations:** Flask-Migrate (Alembic)  
- **Staff auth:** `admin_users` table (username + password hash), not environment passwords  

### Environment variables

| Variable | Purpose |
|----------|---------|
| `SECRET_KEY` | Required in production for sessions |
| `DATABASE_URL` | PostgreSQL URL. Omit locally to use SQLite |

Copy `.env.example` to `.env` and adjust (do not commit `.env`).

---

## Troubleshooting

### `Could not find platform independent libraries <prefix>`

Activate `.venv` first, then use `python` and `flask` from that environment. If it persists, recreate the venv.

### `Error: No such command 'seed-demo'`

Use **`flask seed`**. **`flask seed-demo`** is kept as an alias.

---

## License

Educational / course use where applicable.
