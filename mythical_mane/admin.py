from django.contrib import admin

from mythical_mane.models import (
    Diagnosis,
    Employee,
    MythicalMane,
    PatientNote,
    Owner,
    Patient,
    ProcedureDefinition,
    Universe,
    Visit,
)


@admin.register(Universe)
class UniverseAdmin(admin.ModelAdmin):
    list_display = ("universe_id", "name")
    search_fields = ("name",)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ("owner_id", "name", "phone", "email", "universe")
    search_fields = ("name", "phone", "email")
    list_filter = ("universe",)


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ("patient_id", "name", "color", "owner", "universe")
    search_fields = ("name", "color")
    list_filter = ("owner", "universe")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee_id", "name", "job_role", "hire_date", "phone", "email")
    search_fields = ("name", "job_role", "phone", "email")
    list_filter = ("job_role", "hire_date")
    date_hierarchy = "hire_date"


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ("visit_id", "patient", "start_at", "end_at", "vet")
    search_fields = ("patient__name", "reason")
    list_filter = ("vet", "start_at")
    date_hierarchy = "start_at"


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ("diagnosis_id", "name", "code")
    search_fields = ("name", "code", "description")


@admin.register(ProcedureDefinition)
class ProcedureDefinitionAdmin(admin.ModelAdmin):
    list_display = ("procedure_id", "name", "standard_cost")
    search_fields = ("name", "description")


@admin.register(MythicalMane)
class MythicalManeAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at")
    date_hierarchy = "created_at"


@admin.register(PatientNote)
class PatientNoteAdmin(admin.ModelAdmin):
    list_display = ("patient_note_id", "title", "patient_name", "author_name", "created_at")
    search_fields = ("title", "note", "patient_name", "owner_name", "universe_name", "author_name")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"
