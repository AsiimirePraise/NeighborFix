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

**2. Database (creates `instance\neighborfix.db` with SQLite)**

```powershell
$env:FLASK_APP = "wsgi:app"
flask db upgrade
```

**3. (Optional) Starter rows in `issues`**

Use `flask seed` (or the older alias `flask seed-demo` — same behaviour):

```powershell
flask seed
```

**4. Staff dashboard (triage: open / in progress / resolved)**

Set a password in `.env`, then restart the server:

```env
ADMIN_PASSWORD=your-long-secret-here
```

Open **http://127.0.0.1:5000/admin** and sign in. Changes update the existing **`issues.status`** column in the database (no extra migration needed for status).

**5. Start the server**

```powershell
flask run
```

**6. Open the site**

**http://127.0.0.1:5000/** — times follow **East Africa Time (EAT, UTC+3)** when you host in-region.

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
| `ADMIN_PASSWORD` | Enables **/admin** staff dashboard (updates `issues.status`) |

Copy `.env.example` to `.env` and adjust (do not commit `.env`).

---

## Troubleshooting

### `Could not find platform independent libraries <prefix>`

Windows can show this when the active `python` is not the venv interpreter. Activate `.venv` first, then use `python` and `flask` from that environment. If it persists, recreate the venv: remove `.venv`, run `python -m venv .venv`, then `pip install -r requirements.txt`.

### `Error: No such command 'seed-demo'`

Use **`flask seed`**. If you still use `seed-demo`, it is registered again as an alias of `seed` in this project.

---

## License

Educational / course use where applicable.
