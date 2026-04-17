# AI Collaboration Log

This document records major AI-assisted tasks completed in this project.

## 1) Inspectdb model interpretation and unmanaged table explanation
- What I asked the AI to do:
  - Explain generated inspectdb models, identify existing tables, and explain why Django marked them unmanaged.
- What code or explanation the AI produced:
  - Explained that inspectdb reflects existing database tables and sets managed = False by default to prevent Django migrations from altering legacy/existing schema.
  - Mapped generated model classes to existing database tables.
- What I changed after reviewing it:
  - Continued with admin registration and schema alignment work based on that explanation.
- How I verified that the result worked:
  - Confirmed generated models matched introspected tables and continued with Django checks.

## 2) Initial admin registration setup
- What I asked the AI to do:
  - Register Mythical Mane models in Django admin.
- What code or explanation the AI produced:
  - Added mythical_mane app to installed apps.
  - Registered model(s) in admin.
- What I changed after reviewing it:
  - Requested minimum required registration set for specific domain models.
- How I verified that the result worked:
  - Ran manage.py check and confirmed no issues.
  - Confirmed model registration list from admin registry in Django shell.

## 3) Supabase connection and write-back verification
- What I asked the AI to do:
  - Confirm admin writes back to Supabase through DATABASE_URL.
- What code or explanation the AI produced:
  - Verified active DB backend/host was Supabase PostgreSQL.
  - Performed ORM create, update, read, and delete tests.
  - Cross-checked at least one value with direct SQL query.
- What I changed after reviewing it:
  - Requested broader schema alignment and inspectdb refresh steps.
- How I verified that the result worked:
  - Command output showed successful insert/update/delete round trip.
  - Direct SQL read matched ORM value.

## 4) Required model registration strategy
- What I asked the AI to do:
  - Ensure minimum required registrations for Universe, Owner, Patient, Employee, Visit, Diagnosis, ProcedureDefinition.
- What code or explanation the AI produced:
  - Added explicit registration logic and then switched to concrete ModelAdmin classes with useful list_display, search_fields, list_filter, and date_hierarchy.
- What I changed after reviewing it:
  - Requested practical, field-correct admin config rather than placeholder config.
- How I verified that the result worked:
  - Listed registered models in admin registry and confirmed all required entries present once models were in app models file.

## 5) Handling inspectdb output path confusion
- What I asked the AI to do:
  - Verify why inspectdb command returned no output.
- What code or explanation the AI produced:
  - Explained output was redirected to a file.
  - Found generated file at repo root models.py and synced it into mythical_mane/models.py.
- What I changed after reviewing it:
  - Continued with admin and UI updates now that correct models were loaded by app.
- How I verified that the result worked:
  - Django check passed.
  - Admin registry showed required models from mythical_mane app.

## 6) Patient list page implementation with related data
- What I asked the AI to do:
  - Build a Tailwind-styled patient page showing patient, owner, and universe data.
- What code or explanation the AI produced:
  - Added /patients route.
  - Added view querying Patient with select_related for owner and universe.
  - Added Tailwind template rendering at least 20 rows and required fields.
- What I changed after reviewing it:
  - Requested landing page link and later sortable headers/filter reset.
- How I verified that the result worked:
  - Confirmed endpoint rendered and included real patient names from DB.
  - Django check passed.

## 7) Sortable table headers and filter reset
- What I asked the AI to do:
  - Make column labels clickable to sort and add a way to remove filters.
- What code or explanation the AI produced:
  - Added query-parameter sorting logic in view.
  - Added clickable header links with direction toggle indicators.
  - Added clear sorting control to reset to default list order.
- What I changed after reviewing it:
  - Requested additional UI polish and consistency updates.
- How I verified that the result worked:
  - Confirmed generated links had sort and dir params.
  - Confirmed sorted output changed and reset option appeared conditionally.

## 8) Homepage redesign and consistency pass
- What I asked the AI to do:
  - Improve landing page UI to better match patient page and look more professional.
- What code or explanation the AI produced:
  - Reworked homepage into structured dashboard-style layout.
  - Added clear navigation, professional copy, and live patient count.
- What I changed after reviewing it:
  - Requested another professionalism pass to reduce visual noise and improve intended usage.
- How I verified that the result worked:
  - Django check passed.
  - Rendered page content confirmed updated sections and dynamic patient count.

## 9) New managed model and migration into Supabase
- What I asked the AI to do:
  - Create a new Django-managed model, migrate it into Supabase, and register in admin.
- What code or explanation the AI produced:
  - Added PatientNote model and admin registration.
  - Created a focused migration for patient_note table.
  - Applied migration to Supabase and verified table exists.
  - Verified create/delete through ORM.
- What I changed after reviewing it:
  - Accepted a self-contained note schema after FK migration constraints with unmanaged inspectdb models.
- How I verified that the result worked:
  - Migration succeeded.
  - Table existence check returned true.
  - ORM write and delete both succeeded.

## 10) Patient notes in UI and admin improvements
- What I asked the AI to do:
  - Add patient note visibility to patient page via closed-by-default dropdown and keep note in admin.
- What code or explanation the AI produced:
  - Added notes column with per-patient dropdown.
  - Wired note data into patient view context.
  - Kept PatientNote in admin with search/list/filter settings.
  - Seeded one sample note for demonstration.
- What I changed after reviewing it:
  - Requested fixes when dropdown expansion broke table layout and later overflowed off-page.
- How I verified that the result worked:
  - Confirmed note summary and note content rendered on patient page.
  - Confirmed admin registration remained active.

## 11) Notes dropdown layout fixes
- What I asked the AI to do:
  - Fix messy note UI and off-page overflow.
- What code or explanation the AI produced:
  - Converted note panel from in-flow expansion to overlay popover.
  - Re-anchored popover alignment to avoid going off-screen.
- What I changed after reviewing it:
  - Reported overflow issue after first fix, prompting right-aligned popover adjustment.
- How I verified that the result worked:
  - Django check passed.
  - Rendered HTML confirmed overlay classes and note content remained accessible.

## Summary
The project currently includes:
- Supabase-backed inspectdb models for existing schema.
- Admin registrations for required domain models.
- A professional patient directory page with sorting and clear sorting.
- A managed patient_note table created by Django migration and shown in admin.
- Patient note visibility in the patient list via closed-by-default note popovers.
