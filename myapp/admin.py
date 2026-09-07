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