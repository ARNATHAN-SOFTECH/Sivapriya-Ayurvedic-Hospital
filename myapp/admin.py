from django.contrib import admin
from .models import Doctor
from .models import Gallery
from .models import FAQCategory, FAQ
from .models import OPRegistration


@admin.register(OPRegistration)
class OPRegistrationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'patient_name',
        'mobile',
        'doctor',
        'appointment_date',
        'token_number',
        'status',
        'created_at',
    )

    list_filter = (
        'status',
        'appointment_date',
        'doctor',
    )

    search_fields = (
        'patient_name',
        'mobile',
    )

    ordering = (
        '-created_at',
    )

@admin.register(FAQCategory)
class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    ordering = ('order', 'name')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'is_active', 'order')
    list_filter = ('category', 'is_active')
    search_fields = ('question', 'answer')
    ordering = ('category', 'order')

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    list_filter = ['category']
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'specialization', 'available')



from django.contrib import admin

from .models import (
    Patient,
    Treatment,
    Medicine,
    Bill,
    BillItem,
)


# ============================================================
# PATIENT ADMIN
# ============================================================

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

    list_display = (
        "op_number",
        "name",
        "age",
        "gender",
        "phone",
        "created_at",
    )

    search_fields = (
        "op_number",
        "name",
        "phone",
    )

    list_filter = (
        "gender",
        "created_at",
    )

    ordering = (
        "-created_at",
    )


# ============================================================
# TREATMENT ADMIN
# ============================================================

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "amount",
        "is_active",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "name",
    )


# ============================================================
# MEDICINE ADMIN
# ============================================================

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "amount",
        "stock",
        "is_active",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "name",
    )


# ============================================================
# BILL ITEM INLINE
# ============================================================

class BillItemInline(admin.TabularInline):

    model = BillItem

    extra = 0

    fields = (
        "item_type",
        "item_name",
        "quantity",
        "unit_price",
        "total_amount",
        "treatment",
        "medicine",
    )

    readonly_fields = (
        "total_amount",
    )


# ============================================================
# BILL ADMIN
# ============================================================

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):

    list_display = (
        "bill_number",
        "patient",
        "bill_date",
        "grand_total",
        "paid_amount",
        "balance_amount",
        "payment_method",
        "status",
    )

    search_fields = (
        "bill_number",
        "patient__op_number",
        "patient__name",
        "patient__phone",
    )

    list_filter = (
        "payment_method",
        "status",
        "bill_date",
    )

    readonly_fields = (
        "bill_number",
        "bill_date",
        "grand_total",
        "balance_amount",
        "status",
    )

    ordering = (
        "-bill_date",
    )

    inlines = (
        BillItemInline,
    )


# ============================================================
# BILL ITEM ADMIN
# ============================================================

@admin.register(BillItem)
class BillItemAdmin(admin.ModelAdmin):

    list_display = (
        "bill",
        "item_type",
        "item_name",
        "quantity",
        "unit_price",
        "total_amount",
    )

    search_fields = (
        "item_name",
        "bill__bill_number",
    )

    list_filter = (
        "item_type",
    )

    ordering = (
        "-id",
    )