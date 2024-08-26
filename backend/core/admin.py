from django.contrib import admin

from core.models import Sales
from core.models import Invoice
from core.models import Customer


# Register your models here.
@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "fiscal_year",
        "party_name",
        "payment_mode",
        "party_pan",
        "address",
        "category",
        "particulars",
        "quantity",
        "price",
    ]

    search_fields = [
        "id",
        "fiscal_year",
        "party_name",
    ]

    list_filter = [
        "fiscal_year",
        "payment_mode",
    ]


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "sales__price",
        "sales__particulars",
        "customer",
        "date",
    ]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "address",
        "phone_number",
    ]
