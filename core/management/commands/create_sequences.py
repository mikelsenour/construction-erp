from django.core.management.base import BaseCommand

from core.models import DocumentSequence

SEQUENCES = [
    ("CLT", "Client"),
    ("PRJ", "Project"),
    ("CON", "Contract"),
    ("BOQ", "Bill of quantities"),
    ("VAR", "Variation"),
    ("SUP", "Supplier"),
    ("REQ", "Material requisition"),
    ("RFQ", "Request for quotation"),
    ("LPO", "Purchase order"),
    ("GRN", "Goods received note"),
    ("MIN", "Material issue note"),
    ("INV", "Client invoice"),
    ("SI", "Site instruction"),
    ("NCR", "Non-conformance report"),
    ("IPC", "Interim payment certificate"),
]


class Command(BaseCommand):
    help = "Create the standard document number sequences (safe to repeat)."

    def handle(self, *args, **options):
        for code, name in SEQUENCES:
            _, created = DocumentSequence.objects.get_or_create(
                code=code, defaults={"name": name, "prefix": code}
            )
            status = "Created" if created else "Already exists"
            self.stdout.write(f"{status}: {code} - {name}")