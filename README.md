# Phase 2 Databases Course Project

This repository contains the Phase 2 template structure for the organization and view of your project. This phase only requires Frontend but WILL have Database connectivity and dynamic interactions. Each student group will be provided with the credentials and resources for a database online server.

## Login Information:

- **Email:** javier.quinones3@upr.edu
- **Password:** pass1234

## Initialization:

Initialize the project by installing Flask, pymysql, and passlib through your terminal.

```bash
pip install Flask pymysql passlib
```

For Phase 2, MySQL and MySQL Workbench are needed.

### Functions:

#### Working Functions:
- **Login (Database connection)**
- **View products (DB)**
- **Add products to cart (Sessions)**
- **View profile info (DB)**
- **Edit basic profile info (DB)**
- **Edit/add addresses (DB)**
- **Enter checkout page and edit profile info from such page (Sessions/DB)**
- **Validate if any info is missing before processing the checkout (DB)**

#### Functions for Students to Work On:
- **Register (Database connection)**
- **Change password (DB)**
- **Filters and sorting (DB or potential Python data structures)**
- **Edit cart and remove from cart (Sessions)**
- **Edit/add payment methods (DB)**
- **Processing an order (DB)**
- **Invoice (DB)**
- **View orders (DB)**

### Database Connection:

The DB Server credentials are found in `frontend_model/connectDB.py`.

### Additional Information:

The base from which each HTML page extends is found in `frontend/base.html`.
