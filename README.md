# E-Commerce Backend

A scalable full-stack e-commerce backend built using Django and Django REST Framework. This backend powers the 
fashion e-commerce platform by handling authentication, product, cart management, wishlist, checkout, orders
and payment integration.

---

## Features

- User Authentication using JWT
- User Registration & Login
- Product Categories API
- Checkout API
- Razorpay Payment Integration
- Protected Routes using JWT Authentication

---

## Technologies used

- Python
- Django
- Django REST Framework
- Simple JWT Authentication
- Razorpay API
- SQLite

## Project Structure

```
backend/
|
|--- accounts/
|    |--- models.py
|    |--- views.py
|    |--- serializers.py
|    |--- urls.py
|
|--- backend/
|    |--- settings.py
|    |--- urls.py
|
|--- categories/
|    |--- models.py
|    |--- views.py
|    |--- serializers.py
|    |--- urls.py
|
|--- orders/
|    |--- models.py
|    |--- views.py
|    |--- serializers.py
|    |--- urls.py
|
|--- products
|    |--- fixtures/
|    |--- models.py
|    |--- views.py
|    |--- serializers.py
|    |--- urls.py
|--- manage.py

```

### Razorpay Payment Integration
This backend supports Razorpay Test Mode Integration.

#### Payment Features
- Razorpay Test Payments
- Payment Status Handling
- Order Storage After Successful Payment

### Note

This project is built for learning purposes to practice real-world django backend development 
and REST API architecture.


