# Vendor-Management-System

## Introduction
A vendor management system using django and django-rest-framework.
This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.

## Installation
### 1. clone repository
`git clone https://github.com/SalmanSaalu/Vendor-Management-System.git`
### 2. Navigate to project directory
`cd backend`
### 3. Setup a virtual Environment and activate it
vms is the env name used <br/><br/>
`python -m venv vms` <br/>
`vms\scripts\activate`
### 4. Installing dependencies
`pip install -r requirements.txt`
### 5. Apply migrations and Run the development Server
`python manage.py makemigrations`<br/>
`python manage.py migrate` <br/>
`python manage.py runserver`

## Configuration
### 1. Create a superuser
`python manage.py createsuperuser`
### 2. Create a token for superuser / Admin
`python manage.py drf_create_token <superusername>`

simple jwt setup

installation
adjusting requirements in settings.py 
adding /api/token url 
adding refresh and access token expiration time in settings.py

setting up endpoints
1. /api/vendor - create a vendor

   only want name, contact details , address atribute
   vendor code,and others are generated automaticaaly and initially others are 0 values , since there is no previos purchase trach records

   
