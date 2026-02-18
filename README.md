# Simple E-commerce Application

A minimal yet fully functional e-commerce platform built with Django and PostgreSQL. This project demonstrates core e-commerce functionality with user management, product catalog, shopping cart, and order processing.

## Overview

This repository contains a complete e-commerce application scaffold including authentication, product management, shopping cart, checkout process, and administrative interface.

**Version:** 1.0.0  
**Language:** Python (Django)  
**Database:** PostgreSQL (SQLite for local development)

### Key Features

* **User Management** — Registration, login, logout, password reset, and profile management
* **Product Catalog** — Browse products with detailed product pages
* **Shopping Cart** — Session-based cart with add/remove functionality
* **Order Management** — Complete checkout process with order creation and tracking
* **Admin Dashboard** — Django admin interface for content and user management
* **Authentication** — Secure user authentication with Django auth framework

---

## Getting Started

### Requirements

- Python 3.8+
- PostgreSQL 12+ (optional; SQLite used for local development by default)
- pip and virtualenv

### Installation & Setup

1. **Clone the repository** and navigate to the project directory:

```bash
cd ~/Documents/sast/ecommerce
```

2. **Create and activate a virtual environment:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Configure environment variables** (optional for local development):

```bash
cp .env.example .env
# Edit .env with your database credentials
```

### Database Configuration

**Local Development (SQLite):**
No configuration needed. SQLite database file will be created automatically.

**Production (PostgreSQL):**
Set the following environment variables in `.env`:

```bash
DB_NAME=ecommerce_db
DB_USER=ecom_user
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=5432
```

### Running the Application

1. **Apply database migrations:**

```bash
python manage.py migrate
```

2. **Create a superuser account:**

```bash
python manage.py createsuperuser
```

3. **Start the development server:**

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

### Admin Access

Access the Django admin interface at `http://127.0.0.1:8000/admin/` using your superuser credentials.

---

## Project Structure

```
ecommerce/
├── ecommerce_project/     # Main Django project settings
│   ├── settings.py        # Project configuration
│   ├── urls.py            # URL routing
│   └── wsgi.py            # WSGI application
├── accounts/              # User authentication app
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── shop/                  # Product catalog app
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── urls.py
├── orders/                # Order management app
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── templates/             # HTML templates
│   ├── base.html
│   ├── accounts/
│   ├── shop/
│   ├── orders/
│   └── registration/
├── manage.py
├── requirements.txt
└── README.md
```

---

## API/Feature Overview

### Authentication Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/accounts/register/` | GET, POST | User registration |
| `/accounts/login/` | GET, POST | User login |
| `/accounts/logout/` | GET | User logout |
| `/accounts/password_reset/` | GET, POST | Password reset request |
| `/accounts/profile/` | GET | View user profile |
| `/accounts/profile/edit/` | GET, POST | Edit user profile |

### Shop Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Product list view |
| `/product/<slug>/` | GET | Product detail view |
| `/cart/add/<slug>/` | POST | Add product to cart |
| `/cart/remove/<slug>/` | GET | Remove product from cart |
| `/cart/` | GET | View shopping cart |

### Order Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/orders/checkout/` | GET, POST | Checkout process |
| `/orders/thank-you/` | GET | Order confirmation |

---

## Development

### Adding Products

1. Log in to the admin interface (`/admin/`)
2. Navigate to **Products**
3. Click **Add Product** and fill in the required fields:
   - Name
   - Slug (auto-generated from name)
   - Description
   - Price
   - Inventory

### Extending the Project

The modular app structure allows easy expansion:

- **New Payment Gateway:** Extend `orders/views.py` checkout logic
- **Additional Features:** Create new Django apps and register in `INSTALLED_APPS`
- **Custom Admin Pages:** Customize `admin.py` files in each app

---

## Testing

To run the development server with test data:

```bash
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/` and interact with the application.

---

## Deployment

### Production Checklist

- [ ] Set `DEBUG=0` in environment variables
- [ ] Configure a production-grade database (PostgreSQL recommended)
- [ ] Set `SECRET_KEY` to a secure random value
- [ ] Configure `ALLOWED_HOSTS` in `settings.py`
- [ ] Use a production WSGI server (Gunicorn, uWSGI)
- [ ] Set up static file serving (WhiteNoise, Nginx)
- [ ] Configure HTTPS/SSL certificates
- [ ] Set up error logging and monitoring

### Deployment with Gunicorn

```bash
pip install gunicorn
gunicorn ecommerce_project.wsgi:application --bind 0.0.0.0:8000
```

---

## Contribution Guidelines

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Include docstrings for complex functions

### Making Changes

1. Create a new branch for your feature
2. Make your changes with clear commit messages
3. Test thoroughly before submitting
4. Submit a pull request with a detailed description

### Testing Changes

```bash
python manage.py test
```

---

## Support & Contact

For issues, questions, or contributions:

- **Project Owner:** [Your Name]
- **Email:** [Your Email]
- **Repository:** [Repository URL]

---

## License

This project is provided as-is for educational and development purposes.

---

## Changelog

### Version 1.0.0
- Initial release
- User authentication system
- Product catalog with shopping cart
- Order processing and admin interface
