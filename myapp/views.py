from django.shortcuts import get_object_or_404, render, redirect
from .models import (
    Doctor,
    Gallery,
    FAQCategory,
    OPRegistration,
    Patient,
)


def op_registration(request):

    doctors = Doctor.objects.filter(available=True)

    if request.method == "POST":

        op = OPRegistration.objects.create(
            patient_name=request.POST.get('patient_name'),
            mobile=request.POST.get('mobile'),
            age=request.POST.get('age'),
            gender=request.POST.get('gender'),
            doctor_id=request.POST.get('doctor') or None,
            appointment_date=request.POST.get('appointment_date'),
            symptoms=request.POST.get('symptoms'),
        )

        # Create corresponding Patient record for Billing
        Patient.objects.get_or_create(
            op_number=op.op_number,
            defaults={
                "name": op.patient_name,
                "age": op.age,
                "gender": op.gender,
                "phone": op.mobile,
            }
        )

        return render(
            request,
            'op_success.html',
            {
                'op': op
            }
        )

    return render(
        request,
        'op_registration.html',
        {
            'doctors': doctors
        }
    )

def faq(request):
    categories = FAQCategory.objects.prefetch_related('faqs').all()

    return render(request, 'faq.html', {
        'categories': categories
    })

def gallery(request):
    images = Gallery.objects.all().order_by('-created_at')

    return render(
        request,
        'gallery.html',
        {
            'images': images
        }
    )
def doctors(request):
    doctors = Doctor.objects.filter(available=True)
    return render(request, 'doctors.html', {
        'doctors': doctors
    })

def home(request):
    return render(request, 'home.html')
def treatments(request):
    return render(request, 'treatments.html')



def doctor_detail(request, slug):
    doctor = get_object_or_404(Doctor, slug=slug)
    return render(request, 'doctor_detail.html', {
        'doctor': doctor
    })


def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, "about.html")


from django.shortcuts import render
from django.http import Http404


# =========================================================
# BLOG DATA
# =========================================================

BLOGS = [
    {
        "id": 1,
        "title": "The Healing Power of Ayurveda",
        "category": "Ayurveda",
        "date": "August 18, 2026",
        "author": "Sivapriya Ayurvedic Hospital",
        "image": "images/ayurveda-healing.jpg",
        "excerpt": "Discover how Ayurveda supports natural healing and helps restore balance between the body, mind and spirit.",
        "content": """
Ayurveda is one of the world's oldest holistic healthcare
systems. It focuses on maintaining harmony between the body,
mind and environment.

Ayurvedic healthcare emphasizes prevention, healthy living,
appropriate nutrition, natural therapies and personalized
treatment approaches.

At Sivapriya Ayurvedic Hospital, we believe that every
individual is unique. Ayurvedic treatments are therefore
planned according to the individual's health condition,
lifestyle and body constitution.

Ayurveda encourages us to understand our body, listen to
its needs and develop healthy daily routines.
"""
    },

    {
        "id": 2,
        "title": "Benefits of Panchakarma Therapy",
        "category": "Treatments",
        "date": "August 12, 2026",
        "author": "Dr. Sabu",
        "image": "images/panchakarma.jpg",
        "excerpt": "Learn how Panchakarma therapies can support detoxification, rejuvenation and overall wellbeing.",
        "content": """
Panchakarma is a traditional Ayurvedic therapeutic approach
designed to support the body's natural processes.

Panchakarma treatments are selected according to the
individual's health condition and Ayurvedic assessment.

The therapies may include different procedures such as
Abhyanga, Swedana and other specialized Ayurvedic treatments.

Proper assessment and supervision by a qualified Ayurvedic
practitioner are important before undergoing Panchakarma.
"""
    },

    {
        "id": 3,
        "title": "Ayurvedic Tips for a Healthy Lifestyle",
        "category": "Wellness",
        "date": "August 08, 2026",
        "author": "Sivapriya Wellness Team",
        "image": "images/healthy-lifestyle.jpg",
        "excerpt": "Simple Ayurvedic lifestyle practices that can help you maintain energy, balance and wellbeing every day.",
        "content": """
A healthy lifestyle is an important part of Ayurveda.

Maintaining regular sleeping and eating patterns, eating
wholesome foods, staying physically active and practising
relaxation techniques can contribute to overall wellbeing.

Ayurveda also encourages individuals to develop routines
that are suitable for their personal constitution and
lifestyle.

Small and consistent changes can make healthy living easier
to maintain over time.
"""
    },

    {
        "id": 4,
        "title": "Understanding Your Body Constitution",
        "category": "Ayurveda",
        "date": "August 03, 2026",
        "author": "Sivapriya Ayurvedic Hospital",
        "image": "images/dosha.jpg",
        "excerpt": "Understand the Ayurvedic concept of Vata, Pitta and Kapha and how they influence individual wellbeing.",
        "content": """
Ayurveda describes three fundamental doshas known as Vata,
Pitta and Kapha.

These doshas are traditionally used to understand different
physiological and behavioural characteristics.

Ayurvedic practitioners consider an individual's constitution
when recommending lifestyle practices, diet and therapies.

Understanding your constitution can help you make more
personalized choices about wellness and daily routines.
"""
    },

    {
        "id": 5,
        "title": "Ayurveda for Stress Management",
        "category": "Wellness",
        "date": "July 28, 2026",
        "author": "Sivapriya Wellness Team",
        "image": "images/stress-management.jpg",
        "excerpt": "Explore natural Ayurvedic approaches that may help promote relaxation and emotional wellbeing.",
        "content": """
Modern lifestyles can often be demanding and stressful.

Ayurveda encourages a balanced lifestyle that includes
appropriate rest, healthy food, physical activity and
relaxation.

Practices such as yoga, meditation, breathing exercises and
Abhyanga are commonly associated with Ayurvedic wellness
routines.

Developing a consistent daily routine can also support
relaxation and general wellbeing.
"""
    },

    {
        "id": 6,
        "title": "The Importance of Ayurvedic Diet",
        "category": "Nutrition",
        "date": "July 22, 2026",
        "author": "Sivapriya Ayurvedic Hospital",
        "image": "images/ayurvedic-food.jpg",
        "excerpt": "Discover why Ayurveda considers food an important part of maintaining health and balance.",
        "content": """
Food plays an important role in traditional Ayurveda.

Ayurveda considers digestion, food quality, meal timing and
individual needs when discussing diet and wellbeing.

Fresh and balanced foods, appropriate portion sizes and
regular meal patterns are often encouraged.

Individual dietary recommendations should be discussed with
a qualified healthcare professional, especially when there
are existing health concerns.
"""
    },
]


# =========================================================
# BLOG PAGE
# =========================================================

def blog(request):

    context = {
        "blogs": BLOGS
    }

    return render(
        request,
        "blog.html",
        context
    )


# =========================================================
# BLOG DETAIL PAGE
# =========================================================

def blog_detail(request, blog_id):

    # Find the blog inside the Python list
    selected_blog = None

    for item in BLOGS:

        if item["id"] == blog_id:

            selected_blog = item

            break


    # If the blog ID does not exist
    if selected_blog is None:

        raise Http404("Blog article not found")


    # =====================================================
    # RELATED BLOGS
    # =====================================================

    related_blogs = []

    for item in BLOGS:

        if (
            item["id"] != blog_id
            and item["category"] == selected_blog["category"]
        ):

            related_blogs.append(item)


    # Show maximum 3 related articles
    related_blogs = related_blogs[:3]


    # =====================================================
    # CONTEXT
    # =====================================================

    context = {
        "blog": selected_blog,
        "related_blogs": related_blogs,
    }


    return render(
        request,
        "blog_detail.html",
        context
    )












from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BillForm
from .models import (
    Treatment,
    Medicine,
    Bill,
    BillItem,
)


# ============================================================
# BILLING PAGE
# ============================================================

@login_required
def billing_page(request):

    treatments = (
        Treatment.objects
        .filter(is_active=True)
        .order_by("name")
    )

    medicines = (
        Medicine.objects
        .filter(is_active=True)
        .order_by("name")
    )

    patients = (
        Patient.objects
        .all()
        .order_by("-created_at")
    )

    # --------------------------------------------------------
    # GET
    # --------------------------------------------------------

    if request.method == "GET":

        return render(
            request,
            "billing/billing.html",
            {
                "form": BillForm(),
                "patients": patients,
                "treatments": treatments,
                "medicines": medicines,
            }
        )

    # --------------------------------------------------------
    # POST
    # --------------------------------------------------------

    patient_mode = request.POST.get(
        "patient_mode",
        "existing"
    )

    try:

        with transaction.atomic():

            # =================================================
            # EXISTING PATIENT
            # =================================================

            if patient_mode == "existing":

                patient_id = request.POST.get(
                    "existing_patient"
                )

                if not patient_id:

                    raise ValueError(
                        "Please select an OP number / patient."
                    )

                patient = get_object_or_404(
                    Patient,
                    id=patient_id
                )

            # =================================================
            # NEW PATIENT
            # =================================================

            elif patient_mode == "new":

                name = request.POST.get(
                    "new_patient_name",
                    ""
                ).strip()

                age = request.POST.get(
                    "new_patient_age",
                    ""
                ).strip()

                gender = request.POST.get(
                    "new_patient_gender",
                    ""
                ).strip()

                phone = request.POST.get(
                    "new_patient_phone",
                    ""
                ).strip()

                address = request.POST.get(
                    "new_patient_address",
                    ""
                ).strip()

                if not name:

                    raise ValueError(
                        "Please enter the patient's name."
                    )

                # ---------------------------------------------
                # Generate OP Number
                # ---------------------------------------------

                last_patient = (
                    Patient.objects
                    .order_by("-id")
                    .first()
                )

                if last_patient and last_patient.op_number:

                    try:

                        last_number = int(
                            ''.join(
                                filter(
                                    str.isdigit,
                                    last_patient.op_number
                                )
                            )
                        )

                    except ValueError:

                        last_number = 0

                else:

                    last_number = 0

                new_op_number = (
                    f"OP{last_number + 1:05d}"
                )

                # ---------------------------------------------
                # Create patient
                # ---------------------------------------------

                patient = Patient.objects.create(

                    op_number=new_op_number,

                    name=name,

                    age=int(age)
                    if age
                    else None,

                    gender=gender,

                    phone=phone,

                    address=address,
                )

            else:

                raise ValueError(
                    "Invalid patient selection."
                )

            # =================================================
            # TREATMENT / MEDICINE IDS
            # =================================================

            treatment_ids = request.POST.getlist(
                "treatment_id[]"
            )

            treatment_quantities = request.POST.getlist(
                "treatment_quantity[]"
            )

            medicine_ids = request.POST.getlist(
                "medicine_id[]"
            )

            medicine_quantities = request.POST.getlist(
                "medicine_quantity[]"
            )

            if not treatment_ids and not medicine_ids:

                raise ValueError(
                    "Please add at least one treatment or medicine."
                )

            # =================================================
            # PAYMENT
            # =================================================

            paid_amount = Decimal(
                request.POST.get(
                    "paid_amount",
                    "0"
                )
                or "0"
            )

            payment_method = request.POST.get(
                "payment_method",
                "Cash"
            )

            notes = request.POST.get(
                "notes",
                ""
            ).strip()

            if paid_amount < 0:

                raise ValueError(
                    "Paid amount cannot be negative."
                )

            # =================================================
            # CREATE BILL
            # =================================================

            bill = Bill.objects.create(

                patient=patient,

                treatment_total=Decimal("0.00"),

                medicine_total=Decimal("0.00"),

                grand_total=Decimal("0.00"),

                paid_amount=paid_amount,

                payment_method=payment_method,

                notes=notes,
            )

            treatment_total = Decimal("0.00")

            medicine_total = Decimal("0.00")

            # =================================================
            # TREATMENTS
            # =================================================

            for index, treatment_id in enumerate(
                treatment_ids
            ):

                if not treatment_id:
                    continue

                treatment = get_object_or_404(
                    Treatment,
                    id=treatment_id,
                    is_active=True
                )

                try:

                    quantity = int(
                        treatment_quantities[index]
                    )

                except (
                    IndexError,
                    ValueError
                ):

                    quantity = 1

                if quantity < 1:

                    raise ValueError(
                        "Treatment quantity must be at least 1."
                    )

                total = (
                    treatment.amount *
                    quantity
                )

                treatment_total += total

                BillItem.objects.create(

                    bill=bill,

                    item_type="Treatment",

                    treatment=treatment,

                    item_name=treatment.name,

                    quantity=quantity,

                    unit_price=treatment.amount,

                    total_amount=total,
                )

            # =================================================
            # MEDICINES
            # =================================================

            for index, medicine_id in enumerate(
                medicine_ids
            ):

                if not medicine_id:
                    continue

                medicine = get_object_or_404(
                    Medicine,
                    id=medicine_id,
                    is_active=True
                )

                try:

                    quantity = int(
                        medicine_quantities[index]
                    )

                except (
                    IndexError,
                    ValueError
                ):

                    quantity = 1

                if quantity < 1:

                    raise ValueError(
                        "Medicine quantity must be at least 1."
                    )

                if medicine.stock < quantity:

                    raise ValueError(
                        f"Insufficient stock for "
                        f"{medicine.name}. "
                        f"Available stock: "
                        f"{medicine.stock}"
                    )

                total = (
                    medicine.amount *
                    quantity
                )

                medicine_total += total

                BillItem.objects.create(

                    bill=bill,

                    item_type="Medicine",

                    medicine=medicine,

                    item_name=medicine.name,

                    quantity=quantity,

                    unit_price=medicine.amount,

                    total_amount=total,
                )

                # Reduce stock

                medicine.stock -= quantity

                medicine.save(
                    update_fields=["stock"]
                )

            # =================================================
            # TOTAL
            # =================================================

            grand_total = (
                treatment_total +
                medicine_total
            )

            if paid_amount > grand_total:

                raise ValueError(
                    "Paid amount cannot be greater "
                    "than the grand total."
                )

            balance_amount = (
                grand_total -
                paid_amount
            )

            # =================================================
            # STATUS
            # =================================================

            if paid_amount >= grand_total:

                status = "Paid"

            elif paid_amount > 0:

                status = "Partial"

            else:

                status = "Pending"

            # =================================================
            # UPDATE BILL
            # =================================================

            bill.treatment_total = (
                treatment_total
            )

            bill.medicine_total = (
                medicine_total
            )

            bill.grand_total = (
                grand_total
            )

            bill.balance_amount = (
                balance_amount
            )

            bill.status = status

            bill.save()

        # =====================================================
        # SUCCESS
        # =====================================================

        messages.success(
            request,
            f"Bill {bill.bill_number} created successfully."
        )

        return redirect(
            "bill_detail",
            bill_id=bill.id
        )

    except ValueError as error:

        messages.error(
            request,
            str(error)
        )

        return redirect("billing")


# ============================================================
# PATIENT DETAILS
# ============================================================

@login_required
def patient_details(
    request,
    patient_id
):

    patient = get_object_or_404(
        Patient,
        id=patient_id
    )

    return JsonResponse({

        "id": patient.id,

        "op_number": patient.op_number,

        "name": patient.name,

        "age": patient.age or "",

        "gender": patient.gender or "",

        "phone": patient.phone or "",

        "address": patient.address or "",
    })


# ============================================================
# BILL DETAIL
# ============================================================

@login_required
def bill_detail(
    request,
    bill_id
):

    bill = get_object_or_404(
        Bill.objects.select_related(
            "patient"
        ),
        id=bill_id
    )

    return render(
        request,
        "billing/bill_detail.html",
        {
            "bill": bill,
            "items": bill.items.all(),
        }
    )


# ============================================================
# BILL LIST
# ============================================================

@login_required
def bill_list(request):

    bills = (
        Bill.objects
        .select_related("patient")
        .order_by("-id")
    )

    return render(
        request,
        "billing/bill_list.html",
        {
            "bills": bills
        }
    )