from django.db import transaction
from django.utils import timezone

from .models import DocumentSequence


def next_document_number(code):
    """Return the next number for a document type, e.g. 'PRJ-2026-0001'."""
    with transaction.atomic():
        seq = DocumentSequence.objects.select_for_update().get(code=code)
        year = timezone.localdate().year

        if seq.reset_yearly and seq.last_year != year:
            seq.next_number = 1
        seq.last_year = year

        number = seq.next_number
        seq.next_number = number + 1
        seq.save()

    digits = str(number).zfill(seq.padding)
    if seq.include_year:
        return f"{seq.prefix}-{year}-{digits}"
    return f"{seq.prefix}-{digits}"