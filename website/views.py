import urllib.parse
from django.shortcuts import render, redirect
from .models import CustomOrder

def home(request):
    return render(request, 'home.html')

def collection(request):
    return render(request, 'collection.html')

def weddings(request):
    return render(request, 'weddings.html')

import urllib.parse
from django.shortcuts import render


def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        whatsapp_message = f"""
New Contact Inquiry

Name: {name}

Email: {email}

Phone: {phone}

Message:
{message}
"""

        encoded_message = urllib.parse.quote(whatsapp_message)

        whatsapp_url = (
            f"https://wa.me/919370968201?text={encoded_message}"
        )

        return redirect(whatsapp_url)

    return render(request, "contact.html")

def order_success(request):
    return render(request,'order_success.html')


def custom_orders(request):

    if request.method == 'POST':

        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')

        country = request.POST.get('country')
        city = request.POST.get('city')
        address = request.POST.get('address')

        order_type = request.POST.get('order_type')

        selected_pheta = request.POST.get('selected_pheta')

        quantity = request.POST.get('quantity', 1)

        event_date = request.POST.get('event_date')

        CustomOrder.objects.create(

            full_name=full_name,
            phone_number=phone_number,
            email=email,

            country=country,
            city=city,
            address=address,

            order_type=order_type,

            selected_pheta=selected_pheta,

            quantity=quantity,

            event_date=event_date

        )

        whatsapp_message = f"""
Hello Chavan Pheta,

New Order Details:

Name: {full_name}

Phone: {phone_number}

Email: {email}

Country: {country}

City: {city}

Address: {address}

Order Type: {order_type}

Selected Pheta: {selected_pheta}

Quantity: {quantity}

Event Date: {event_date}
"""

        encoded_message = urllib.parse.quote(
            whatsapp_message
        )

        whatsapp_url = (
            f"https://wa.me/919370968201?text={encoded_message}"
        )

        return render(
            request,
            'order_success.html',
            {
                'whatsapp_url': whatsapp_url
            }
        )

    selected_pheta = request.GET.get('pheta', '')

    return render(
        request,
        'custom_orders.html',
        {
            'selected_pheta': selected_pheta
        }
    )