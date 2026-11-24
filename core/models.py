from django.db import models
from django.conf import settings
from django.db import models
from simple_history.models import HistoricalRecords


class AuditedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True, editable=False,
        on_delete=models.PROTECT, related_name="+",
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True, blank=True, editable=False,
        on_delete=models.PROTECT, related_name="+",
    )
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True

class Company(AuditedModel):
    MONTHS = [
        (1, "January"), (2, "February"), (3, "March"), (4, "April"),
        (5, "May"), (6, "June"), (7, "July"), (8, "August"),
        (9, "September"), (10, "October"), (11, "November"), (12, "December"),
    ]

    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="company/", blank=True)
    registration_number = models.CharField(max_length=100, blank=True)
    kra_pin = models.CharField("KRA PIN", max_length=20, blank=True)
    vat_number = models.CharField(max_length=50, blank=True)
    physical_address = models.TextField(blank=True)
    postal_address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    currency_code = models.CharField(max_length=3, default="KES")
    financial_year_start_month = models.PositiveSmallIntegerField(
        choices=MONTHS, default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Company profile"
        verbose_name_plural = "Company profile"

    def __str__(self):
        return self.name