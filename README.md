# Movie Ticket Booking System
Project Overview
This project implements a Movie Ticket Booking System, allowing users to browse movies, view showtimes, select seats, and make bookings. Users will receive email confirmations with QR codes for their bookings, and they can scan these QR codes for ticket information. Additionally, users can access their booking history.

##Features
1. User Registration and Authentication
Users can securely register for an account.
Users can log in using their email and password.
2. Browse Movies
Movies are stored in the database and categorized by release year.
Users can browse a list of available movies.
3. View Showtimes
Users can view hard-coded showtimes (10AM, 2PM, 6PM, 10PM) for a selected movie.
Showtimes display date, time, and theater location.
4. Seat Selection
Users can select seats for the desired showtime.
Multiple seats (up to 10) can be booked.
5. Booking
Users can add selected seats to their booking cart.
They can proceed to confirmation (no payment required).
6. Booking Confirmation and Notifications
Upon successful booking, users receive an email confirmation.
The confirmation email includes movie name, showtime, seat details, and a QR code.
QR code contains essential booking information.
7. QR Code Scanning
Users can scan the QR code from their confirmation email to retrieve ticket information.
Scanning provides details such as movie name, showtime, and seat information.
8. Booking History
Users have access to a booking history, listing past and upcoming bookings.
They receive booking confirmation emails for reference.

##Technologies Used
Django: Backend framework
HTML, CSS, JavaScript: Frontend
MySQL: Database

##Installation
1.Clone the repository:
git clone https://github.com/yourusername/movie-ticket-booking-system.git
cd movie-ticket-booking-system
2.Set up a virtual environment (recommended):
python -m venv venv
source venv/bin/activate
3.Install dependencies:
pip install -r requirements.txt
4.Create and configure your .env file with secret keys, database settings, and email service credentials.
5.Run database migrations:
python manage.py migrate
6.Start the development server:
python manage.py runserver
7.Access the application in your browser at http://localhost:8000.

##Usage
Register an account or log in.
Browse movies, view showtimes, and select seats.
Add seats to your booking cart and proceed to confirmation.
Check your email for booking confirmations with QR codes.
Scan the QR code from your email to retrieve ticket information.
View your booking history.
