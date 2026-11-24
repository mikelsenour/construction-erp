from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

ROLES = [
    "Managing Director",
    "Project Manager",
    "Site Engineer / Supervisor",
    "Quantity Surveyor",
    "Architect / Design Coordinator",
    "Procurement Officer",
    "Storekeeper",
    "Accountant / Finance Officer",
    "HR Officer",
    "Health and Safety Officer",
    "Quality Control Officer",
    "Client / Client Representative",
]


class Command(BaseCommand):
    help = "Create the standard ERP roles (safe to run more than once)."

    def handle(self, *args, **options):
        for name in ROLES:
            group, created = Group.objects.get_or_create(name=name)
            status = "Created" if created else "Already exists"
            self.stdout.write(f"{status}: {name}")