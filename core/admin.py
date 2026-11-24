from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from .models import Company, DocumentSequence


class AuditedAdmin(SimpleHistoryAdmin):
    """Base admin: fills in created_by / updated_by and shows history."""

    readonly_fields = ("created_by", "created_at", "updated_by", "updated_at")

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Company)
class CompanyAdmin(AuditedAdmin):
    def has_add_permission(self, request):
        return not Company.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
@admin.register(DocumentSequence)
class DocumentSequenceAdmin(admin.ModelAdmin):
    list_display = (
        "code", "name", "prefix", "next_number",
        "include_year", "reset_yearly",
    )

    def get_readonly_fields(self, request, obj=None):
        # The code is fixed once created, because the programs refer to it
        return ("code",) if obj else ()

    def has_delete_permission(self, request, obj=None):
        return False