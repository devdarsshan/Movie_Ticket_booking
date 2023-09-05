from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from datetime import datetime, timedelta
from django.core.mail import send_mail,EmailMessage
from movie_booking.settings import EMAIL_HOST_USER
import pyqrcode
from PIL import Image
from django.contrib import messages
from io import BytesIO
from .models import *
from .forms import *


# Create y  our views here.
def signup(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        si_username = request.POST.get('si_username')
        si_pass = request.POST.get('si_pass')
        if username:
            Customer.objects.create(username=username, email=email, password=password)
        if si_username:
            user = Customer.objects.filter(username=si_username, password=si_pass).first()
            if user:
                # data = {'user_id':user.id}
                return redirect('movies_list', user_id=user.id)
                # return render(request,"bookings/movies_list.html",data)


    return render(request,"bookings/signup.html")


def movies_list(request,user_id):
    
    customer = Customer.objects.get(pk=user_id)
    movies = Moviesdata.objects.all().order_by('-Release_date')
    items_per_page = 9
    paginator = Paginator(movies, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    # context = {'products': page,'cartItems':cartItems, 'page': page}

    
    context = {'movies': movies, 'user_id': user_id,'customer': customer,'page': page, 'Name': customer.username}
    return render(request, 'bookings/movies_list.html', context)

def show_timings(request,user_id,movie_id):
    customer = Customer.objects.get(pk=user_id)
    start_date = datetime(2023, 9, 10)

    # End date
    end_date = datetime(2023, 9, 16)

    # Generate the date list
    date_list = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

    
    # Define sample showtimings (you can replace this with your actual data)
    showtimings = {
        date_list[0]: ["10:00 AM", "2:00 PM", "6:00 PM", "10:00 PM"],
        date_list[1]: ["10:00 AM", "2:00 PM", "6:00 PM", "10:00 PM"],
        date_list[2]: ["10:00 AM", "2:00 PM", "6:00 PM", "10:00 PM"],
        date_list[3]: ["10:00 AM", "2:00 PM", "6:00 PM", "10:00 PM"],
        date_list[4]: ["10:00 AM", "2:00 PM", "6:00 PM", "10:00 PM"],
    }

    movie = Moviesdata.objects.get(pk=movie_id)
    context = {
        'dates': date_list,
        'showtimings': showtimings,
        'user_id':user_id,
        'movie_id':movie_id,
        'movie' : movie,
        'Name': customer.username,
    }

    return render(request, 'bookings/show_timings.html', context)


def view_tickets(request,user_id,movie_id, showtime,date_event):
    customer = Customer.objects.get(pk=user_id)
    movie = Moviesdata.objects.get(pk=movie_id)
    if request.method == 'POST':
        selected_seats = request.POST.getlist('check')
        # selected_seats = [seat[1:] for seat in selected_seats]
        if selected_seats:
            booking = Booking.objects.create(
                user=customer,  
                movie=movie,  
                showtime=showtime,
                booked_date = datetime.strptime(date_event, "%Y-%m-%d").date(),
                booked_seats=','.join(selected_seats)
            )
            booking.save()
            showtime_mapping = {1: "10AM",2: "2PM",3: "6PM",4: "10PM"}
            showtime_value = showtime_mapping.get(showtime, "10 AM")

            email_subject = "Your Movie Ticket Booking Confirmation"
            email_body = f"Thank you for booking tickets for {movie.Movie_name} on {date_event} at {showtime_value}. Your booked seats are: {', '.join(selected_seats)}"
            user_email = f"{customer.email}"
            to_email = [user_email,]  # Replace with the user's email address

            details = f"Movie: {movie.Movie_name}\nShowtime: {date_event}\nSeat: {', '.join(selected_seats)}"
            #QR Code
            url = pyqrcode.create(details)

            url.png('myqr.png', scale=6)

            # Read the QR code image from the saved PNG file
            with open('myqr.png', 'rb') as qr_image_file:
                qr_img_data = qr_image_file.read()

            email = EmailMessage(email_subject,email_body,EMAIL_HOST_USER,to_email,)

            # Attach the QR code to the email
            email.attach("booking_qr.png", qr_img_data, "image/png")

            try:
                email.send()
                # Add a success message
                messages.success(request, "Email sent successfully!")
            except Exception as e:
                print(f"Failed to send email: {str(e)}")
                # Add an error message
                messages.error(request, "Failed to send email. Please try again.")


            # send_mail(email_subject, email_body,EMAIL_HOST_USER,to_email, fail_silently=False)

            return HttpResponseRedirect(reverse('movies_list', args=[user_id]))
    else:
        show = Moviesdata.objects.get(pk=movie_id) 
        existing_bookings = Booking.objects.filter(user=user_id,movie=movie_id,showtime=showtime,booked_date=date_event)
        booked_seats = [seat for booking in existing_bookings for seat in booking.booked_seats.split(',')]
        # booked_seats = [seat[1:] for seat in booked_seats]
        context = {'Name': customer.username,'show': show,'booked_seats': booked_seats,'user_id':user_id,'movie_id':movie_id,'showtime':showtime,'date_event':date_event}
        return render(request, 'bookings/seat1.html',context)


def booking_history(request,user_id):
    
    customer = Customer.objects.get(pk=user_id)
    bookings = Booking.objects.filter(user=customer).order_by('-booking_date')
    context = {'bookings': bookings,'user_id':user_id,'Name': customer.username}
    return render(request, 'bookings/booking_history.html',context)

