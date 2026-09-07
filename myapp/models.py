from django.db import models
from django.utils.text import slugify

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    specialization = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    experience = models.PositiveIntegerField()
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='doctors/')
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# main/models.py

class Gallery(models.Model):
    CATEGORY_CHOICES = (
        ('hospital', 'Hospital'),
        ('doctors', 'Doctors'),
        ('treatment', 'Treatment'),
        ('events', 'Events'),
    )

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class FAQCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "FAQ Categories"

    def __str__(self):
        return self.name


class FAQ(models.Model):
    category = models.ForeignKey(
        FAQCategory,
        on_delete=models.CASCADE,
        related_name='faqs'
    )
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.question




from django.db import models
from django.utils import timezone


# ============================================================
# PATIENT
# ============================================================

class Patient(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    op_number = models.CharField(
        max_length=30,
        unique=True
    )

    name = models.CharField(
        max_length=150
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.op_number} - {self.name}"


# ============================================================
# TREATMENT
# ============================================================

class Treatment(models.Model):

    name = models.CharField(
        max_length=200
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


# ============================================================
# MEDICINE
# ============================================================

class Medicine(models.Model):

    name = models.CharField(
        max_length=200
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.PositiveIntegerField(
        default=0
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


# ============================================================
# BILL
# ============================================================

class Bill(models.Model):

    PAYMENT_CHOICES = [
        ("Cash", "Cash"),
        ("UPI", "UPI"),
        ("Card", "Card"),
        ("Bank Transfer", "Bank Transfer"),
    ]

    STATUS_CHOICES = [
        ("Paid", "Paid"),
        ("Partial", "Partial"),
        ("Pending", "Pending"),
    ]

    bill_number = models.CharField(
        max_length=50,
        unique=True,
        blank=True
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.PROTECT,
        related_name="bills"
    )

    bill_date = models.DateTimeField(
        auto_now_add=True
    )

    treatment_total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    medicine_total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    grand_total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    paid_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    balance_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    payment_method = models.CharField(
        max_length=30,
        choices=PAYMENT_CHOICES,
        default="Cash"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    notes = models.TextField(
        blank=True
    )

    def save(self, *args, **kwargs):

        if not self.bill_number:

            today = timezone.now().strftime("%Y%m%d")

            last_bill = (
                Bill.objects
                .filter(bill_number__startswith=f"BILL-{today}")
                .order_by("-id")
                .first()
            )

            if last_bill:
                try:
                    last_number = int(
                        last_bill.bill_number.split("-")[-1]
                    )
                except (ValueError, IndexError):
                    last_number = 0
            else:
                last_number = 0

            self.bill_number = (
                f"BILL-{today}-{last_number + 1:04d}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.bill_number


# ============================================================
# BILL ITEM
# ============================================================

class BillItem(models.Model):

    ITEM_TYPE_CHOICES = [
        ("Treatment", "Treatment"),
        ("Medicine", "Medicine"),
    ]

    bill = models.ForeignKey(
        Bill,
        on_delete=models.CASCADE,
        related_name="items"
    )

    item_type = models.CharField(
        max_length=20,
        choices=ITEM_TYPE_CHOICES
    )

    treatment = models.ForeignKey(
        Treatment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    medicine = models.ForeignKey(
        Medicine,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    item_name = models.CharField(
        max_length=200
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.item_name} - {self.quantity}"