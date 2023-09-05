# Movie Ticket Booking System
## Project Overview 
This project implements a Movie Ticket Booking System, allowing users to browse movies, view showtimes, select seats, and make bookings. Users will receive email confirmations with QR codes for their bookings, and they can scan these QR codes for ticket information. Additionally, users can access their booking history.

## Features
### Login
![image](https://github.com/devdarsshan/Movie_Ticket_booking/assets/75977040/b4c0bed3-39d4-4c3d-946e-3fcd8ab46fea)
### Signup
![image](https://github.com/devdarsshan/Movie_Ticket_booking/assets/75977040/1c669cd0-49e9-4a0f-b237-e66e6b82dde5)

- User Registration and Authentication

  Users can securely register for an account. 
  Users can log in using their email and password.

### Browse Movies
![image](https://github.com/devdarsshan/Movie_Ticket_booking/assets/75977040/81ba9e65-c063-4f6d-89e3-168ee4264e0e)
![image](https://github.com/devdarsshan/Movie_Ticket_booking/assets/75977040/88455afc-5d9a-4e34-855d-22caa7c67b28)

- Browse Movies 

   Movies are stored in the database and categorized by release year. Users can browse a list of available movies.

### Showtime
![image](https://github.com/devdarsshan/Movie_Ticket_booking/assets/75977040/f1a36255-96c7-4a55-a5e0-48dbc576f284)
  
- View Showtimes 
  
   Users can view showtimes (10AM, 2PM, 6PM, 10PM) for a selected movie. Showtimes Showdate, time, and theater location.

### Seat Selection
![image](https://github.com/devdarsshan/Movie_Ticket_booking/assets/75977040/9834c80f-07b0-4a90-868c-831ce9f8be1e)

- Seat Selection

     Users can select seats for the desired showtime. Multiple seats (up to 10) can be booked.

- Booking 

    Users can add selected seats to their booking cart. They can proceed to confirmation (no payment required).

### Email
![image](https://github.com/devdarsshan/Movie_Ticket_booking/assets/75977040/8ac994e0-c016-4fd7-b2b4-793c643089cf)

- Booking Confirmation and Notifications 

    Upon successful booking, users receive an email confirmation. The confirmation email includes movie name, showtime, seat details, and a QR code. QR code contains essential booking information.

### QR Code
![image](https://github.com/devdarsshan/Movie_Ticket_booking/assets/75977040/db5f1768-cc1e-427d-8563-0a815efec027)

- QR Code Scanning

     Users can scan the QR code from their confirmation email to retrieve ticket information. Scanning provides details such as movie name, showtime, and seat information.

### Booking History
![image](https://github.com/devdarsshan/Movie_Ticket_booking/assets/75977040/dbfa2b8e-ddc1-4bf3-bb39-331fb4fd8f09)

- Booking History 

    Users have access to a booking history, listing past and upcoming bookings. They receive booking confirmation emails for reference.

## Technologies Used 
Django: Backend framework 

HTML, CSS, JavaScript: Frontend 

MySQL: Database

### Installation 
1.Clone the repository: 

    git clone https://github.com/yourusername/movie-ticket-booking-system.git 

    cd movie-ticket-booking-system 

2.Set up a virtual environment (recommended): 

    python -m venv venv source venv/bin/activate

3.Install dependencies: 

    pip install -r requirements.txt 

4.Create and configure your .env file with secret keys, database settings, and email service credentials. 

5.Run database migrations:

    python manage.py migrate 
 
6.Start the development server:

    python manage.py runserver 
 
7.Access the application in your browser at http://localhost:8000.

## Usage 

- Register an account or log in. 

- Browse movies, view showtimes, and select seats. 

- Add seats to your booking cart and proceed to confirmation. 

- Check your email for booking confirmations with QR codes. 

- Scan the QR code from your email to retrieve ticket information. 

- View your booking history.
