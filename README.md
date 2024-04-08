# Phase 3 Databases Course Project

This repository contains the Phase 3 template structure for the organization and view of your project. This phase requires BOTH Frontend and Backend. It WILL have Database connectivity and dynamic interactions. Each student group will be provided with the credentials and resources for a database online server.

## Backend Login Information:

- **Email:** javier@dragonflydrones.com
- **Password:** pass1234

## Initialization:

Initialize the project by installing Flask, pymysql, and passlib through your terminal.
The phase 3 template has additional libraries and components you may need to install. (datetime, werkzeuq, os, functools)

```bash
pip install Flask pymysql passlib
```

For Phase 3, MySQL and MySQL Workbench are needed.

### Backend Functions:

#### Working Functions:
- **Login (Database connection)**
- **Hash password (Database connection)**
- **View products (DB)**
- **Add products (DB)**
- **View and sort orders (DB)**
- **Generate sales report for a single product (DB)**
- **View accounts (DB)**
- **Edit customer/admin account (DB)**

#### Functions for Students to Work On:
- **Edit product (Database connection)**
- **View and edit order (DB, including editing ship_date, status, and any other relevant fields)**
- **Generate sales report for all products (DB)**
- **Generate stock report (DB)**
- **Add customer/admin account (DB)**
- **View personal account (DB)**
- **Edit personal account (DB)**

### Database Connection:

The DB Server credentials are found in `backend_model/connectDB.py`.

### Additional Information:

The base from which each HTML page extends is found in `backend/base.html`.

This template only contains the additional backend portion to implement. Students should combine this with their revised frontend portion.
