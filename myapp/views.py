from django.shortcuts import get_object_or_404, render
from .models import Doctor
from .models import Gallery
from .models import FAQCategory


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
