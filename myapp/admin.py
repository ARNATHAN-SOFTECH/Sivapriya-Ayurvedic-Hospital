from django.contrib import admin
from .models import Doctor
from .models import Gallery
from .models import FAQCategory, FAQ
from .models import OPRegistration



@admin.register(OPRegistration)
class OPRegistrationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'op_number',
        'patient_name',
        'mobile',
        'gender',
        'age',
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
        'gender',
        'marital_status',
        'diabetes',
        'high_bp',
        'cancer',
        'arthritis',
        'asthma',
        'allergy',
    )

    search_fields = (
        'op_number',
        'patient_name',
        'mobile',
        'telephone',
        'email',
        'ip_number',
        'diagnosis',
    )

    readonly_fields = (
        'op_number',
        'created_at',
    )

    ordering = (
        '-created_at',
    )

    fieldsets = (

        (
            'OP Registration',
            {
                'fields': (
                    'op_number',
                    'registration_date',
                    'status',
                    'token_number',
                )
            }
        ),

        (
            'Patient Details',
            {
                'fields': (
                    'patient_name',
                    'address',
                    'nationality',
                    'gender',
                    'age',
                    'height',
                    'weight',
                    'mobile',
                    'telephone',
                    'email',
                    'marital_status',
                )
            }
        ),

        (
            'Hospital Details',
            {
                'fields': (
                    'ip_number',
                    'room_number',
                    'date_of_admission',
                    'date_of_discharge',
                    'diagnosis',
                )
            }
        ),

        (
            'Doctor & Appointment',
            {
                'fields': (
                    'doctor',
                    'appointment_date',
                    'symptoms',
                )
            }
        ),

        (
            'Present Illness',
            {
                'fields': (
                    'presenting_complaints',
                    'history_present_illness',
                )
            }
        ),

        (
            'Medical History',
            {
                'fields': (
                    'diabetes',
                    'diabetes_details',
                    'high_bp',
                    'high_bp_details',
                    'cancer',
                    'cancer_details',
                    'arthritis',
                    'arthritis_details',
                    'asthma',
                    'asthma_details',
                    'allergy',
                    'allergy_details',
                    'history_past_illness',
                )
            }
        ),

        (
            'System Information',
            {
                'fields': (
                    'created_at',
                )
            }
        ),
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
        "grand_total",
        "paid_amount",
        "balance_amount",
        "status",
        "payment_method",
        "bill_date",
    )

    list_filter = (
        "status",
        "payment_method",
        "bill_date",
    )

    search_fields = (
        "bill_number",
        "patient__name",
        "patient__op_number",
        "payment_reference",
    )

    readonly_fields = (
        "bill_number",
        "bill_date",
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