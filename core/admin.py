from django.contrib import admin

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Only one company for now
        return not Company.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False