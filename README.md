# Inventory Management System

## Overview

This is an Inventory Management System built using Python, Flask, SQLAlchemy, HTML, CSS, and Bootstrap. The system allows administrators to manage products, view inventory, and manage users. The project is structured to separate concerns and make the codebase more maintainable.

## Features

- **Admin Dashboard:** Manage products, inventory, and users.
- **User Authentication:** Secure login and user management.
- **Product Management:** Add, edit, delete, and view products.
- **Inventory Tracking:** Keep track of product quantities and restock alerts.
- **Responsive Design:** User-friendly interface with Bootstrap.

## Project Structure

```plaintext
inventory_management_system/
├── app/
│   ├── admin/                # Admin-related routes and views
│   ├── products/             # Product-related routes and views
│   ├── templates/            # HTML templates
│   │   ├── admin/            # Admin-specific templates
│   │   ├── products/         # Product-specific templates
│   │   └── user/             # User-specific templates
│   ├── users/                # User-related routes and views
├── instance/                 # Application instance folder
├── static/                   # Static files (CSS, JS, images)
├── README.md                 # Project documentation
├── app.py                    # Main application file
```