# COSC315 Database App (Django + Supabase)

This is a class project that uses Django with a Supabase PostgreSQL database.

The project includes:
- Reverse-engineered models from existing Supabase tables (`inspectdb` output)
- Django admin registrations for core domain models
- A Tailwind-styled patient directory page with sortable columns
- A managed Django model (`PatientNote`) migrated into Supabase

## Tech Stack

- Python 3.12
- Django 5.2
- Supabase PostgreSQL
- Tailwind CSS (CDN in templates)

## Project Structure

- `hello_world/`
	- project settings, URL routing, views, templates, static assets
- `mythical_mane/`
	- database models, admin registration, migrations
- `AI_Log.md`
	- AI collaboration log for class documentation

## Environment Variables

Create a `.env` file (or set environment variables in Codespaces) with values like:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=postgres://...supabase...
```

If `DATABASE_URL` is not set, Django falls back to local SQLite (`db.sqlite3`).

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run migrations (includes managed `patient_note` table):

```bash
python manage.py migrate
```

3. (Optional) collect static files:

```bash
python manage.py collectstatic
```

4. Start the app:

```bash
python manage.py runserver
```

## Main Routes

- `/` - Landing page
- `/patients/` - Patient directory (first 20 records)
	- Shows: patient name, color, DOB, owner, universe
	- Sortable columns
	- Clear sorting button
	- Notes popover (closed by default) per patient
- `/admin/` - Django admin portal

## Admin Models Registered

Minimum required registrations are included:
- `Universe`
- `Owner`
- `Patient`
- `Employee`
- `Visit`
- `Diagnosis`
- `ProcedureDefinition`

Also registered:
- `MythicalMane`
- `PatientNote` (managed model)

## Managed vs Unmanaged Models

Most models in `mythical_mane/models.py` came from `inspectdb`, so they are marked:

```python
managed = False
```

This means Django does not try to create/alter/delete those existing Supabase tables.

`PatientNote` is intentionally Django-managed and created by migration:
- Migration: `mythical_mane/migrations/0002_patient_note.py`
- Table: `patient_note`

## Regenerating Models from Supabase

If Supabase schema changes, regenerate inspectdb output and copy into app models:

```bash
python manage.py inspectdb > models.py
cp models.py mythical_mane/models.py
```

Then review model changes before running migrations.

## Verification Checklist

- `python manage.py check` runs without errors
- `http://127.0.0.1:8000/patients/` loads
- Sorting links update row order
- Notes popover opens without breaking table layout
- `/admin/` shows required models and `PatientNote`

## Notes

- If `runserver` says port 8000 is in use, either stop the existing server process or use another port.
- For assignment traceability, see `AI_Log.md`.
