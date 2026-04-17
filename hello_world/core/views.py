from django.shortcuts import render

from collections import defaultdict

from mythical_mane.models import Patient, PatientNote

def index(request):
    context = {
        "title": "Django example",
        "patient_count": Patient.objects.count(),
    }
    return render(request, "index.html", context)


def patient_list(request):
    sort = request.GET.get("sort", "patient_id")
    direction = request.GET.get("dir", "asc")

    sort_map = {
        "patient": "name",
        "color": "color",
        "dob": "dob",
        "owner": "owner__name",
        "universe": "universe__name",
    }

    order_field = sort_map.get(sort, "patient_id")
    if direction == "desc":
        order_field = f"-{order_field}"

    patients = list(Patient.objects.select_related("owner", "universe").order_by(order_field)[:20])
    note_rows = PatientNote.objects.order_by("-created_at")
    notes_by_patient_name = defaultdict(list)
    for note in note_rows:
        notes_by_patient_name[note.patient_name].append(note)

    for patient in patients:
        patient.patient_notes = notes_by_patient_name.get(patient.name, [])

    context = {
        "title": "Patients",
        "patients": patients,
        "current_sort": sort,
        "current_direction": direction,
        "notes_by_patient_name": notes_by_patient_name,
    }
    return render(request, "patients.html", context)
