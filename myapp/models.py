from django.db import models
from django.utils.text import slugify
from django.utils import timezone



class OPRegistration(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    MARITAL_STATUS_CHOICES = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Widowed', 'Widowed'),
        ('Other', 'Other'),
    )

    YES_NO_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    # =========================================================
    # BASIC PATIENT DETAILS
    # =========================================================

    op_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True
    )

    registration_date = models.DateField(
        default=timezone.localdate
    )

    patient_name = models.CharField(
        max_length=150
    )

    address = models.TextField(
        blank=True
    )

    nationality = models.CharField(
        max_length=100,
        blank=True
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    age = models.PositiveIntegerField()

    height = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Height in cm"
    )

    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Weight in kg"
    )

    mobile = models.CharField(
        max_length=15
    )

    telephone = models.CharField(
        max_length=15,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    # =========================================================
    # HOSPITAL DETAILS
    # =========================================================

    ip_number = models.CharField(
        max_length=30,
        blank=True
    )

    room_number = models.CharField(
        max_length=30,
        blank=True
    )

    date_of_admission = models.DateField(
        null=True,
        blank=True
    )

    date_of_discharge = models.DateField(
        null=True,
        blank=True
    )

    diagnosis = models.TextField(
        blank=True
    )

    marital_status = models.CharField(
        max_length=20,
        choices=MARITAL_STATUS_CHOICES,
        blank=True
    )

    # =========================================================
    # DOCTOR / APPOINTMENT
    # =========================================================

    doctor = models.ForeignKey(
        'Doctor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    appointment_date = models.DateField()

    symptoms = models.TextField(
        blank=True
    )

    # =========================================================
    # MEDICAL HISTORY
    # =========================================================

    presenting_complaints = models.TextField(
        blank=True
    )

    history_present_illness = models.TextField(
        blank=True
    )

    # =========================================================
    # PREVIOUS CONDITIONS
    # =========================================================

    diabetes = models.CharField(
        max_length=10,
        choices=YES_NO_CHOICES,
        blank=True
    )

    diabetes_details = models.TextField(
        blank=True
    )

    high_bp = models.CharField(
        max_length=10,
        choices=YES_NO_CHOICES,
        blank=True
    )

    high_bp_details = models.TextField(
        blank=True
    )

    cancer = models.CharField(
        max_length=10,
        choices=YES_NO_CHOICES,
        blank=True
    )

    cancer_details = models.TextField(
        blank=True
    )

    arthritis = models.CharField(
        max_length=10,
        choices=YES_NO_CHOICES,
        blank=True
    )

    arthritis_details = models.TextField(
        blank=True
    )

    asthma = models.CharField(
        max_length=10,
        choices=YES_NO_CHOICES,
        blank=True
    )

    asthma_details = models.TextField(
        blank=True
    )

    allergy = models.CharField(
        max_length=10,
        choices=YES_NO_CHOICES,
        blank=True
    )

    allergy_details = models.TextField(
        blank=True
    )

    history_past_illness = models.TextField(
        blank=True
    )

    # =========================================================
    # OP STATUS
    # =========================================================

    token_number = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # =========================================================
    # AUTOMATIC OP NUMBER
    # =========================================================

    def save(self, *args, **kwargs):

        if not self.op_number:

            last_op = (
                OPRegistration.objects
                .order_by('-id')
                .first()
            )

            last_patient = (
                Patient.objects
                .order_by('-id')
                .first()
            )

            last_number = 0

            if last_op and last_op.op_number:
                try:
                    last_number = max(
                        last_number,
                        int(
                            last_op.op_number.replace(
                                "OP",
                                ""
                            )
                        )
                    )
                except ValueError:
                    pass

            if last_patient and last_patient.op_number:
                try:
                    last_number = max(
                        last_number,
                        int(
                            last_patient.op_number.replace(
                                "OP",
                                ""
                            )
                        )
                    )
                except ValueError:
                    pass

            self.op_number = f"OP{last_number + 1:05d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.op_number} - {self.patient_name}"

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

    op_registration = models.OneToOneField(
        OPRegistration,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="patient"
    )

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

    ip_number = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    room_number = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    doctor = models.ForeignKey(
        'Doctor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    date_of_admission = models.DateField(
        null=True,
        blank=True
    )

    date_of_discharge = models.DateField(
        null=True,
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

    payment_reference = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="UPI Transaction ID / Card Ref No"
    )

    diagnosis = models.TextField(
        blank=True,
        help_text="Doctor diagnosis at billing time"
    )

    prescription_notes = models.TextField(
        blank=True,
        help_text="Medicine instructions"
    )

    collected_by = models.CharField(
        max_length=100,
        blank=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
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

        # Auto update balance
        self.balance_amount = self.grand_total - self.paid_amount

        # Auto update status
        if self.paid_amount >= self.grand_total:
            self.status = "Paid"
        elif self.paid_amount > 0:
            self.status = "Partial"
        else:
            self.status = "Pending"

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