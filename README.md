![image](https://github.com/SalmanSaalu/Vendor-Management-System/assets/87108862/08394c0d-45ea-451a-94b5-04aedae040a6)# Vendor-Management-System

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
`python manage.py runserver` <br/>
Run `http://localhost:8000/api/` or `http://127.0.0.1:8000/api/` in Web Browser to check setup is successful.

## Configuration
### 1. Create a superuser
`python manage.py createsuperuser`
### 2. Create a token for superuser / Admin 
Using postman pass username and password as POST request to return token of the corresponding user (eg: Login Form) <br/>
`api/auth/login/` <br/>

note:&nbsp; For every user registered in django user model will return a token when the `api/auth/login/` with the POST request is called.
But only the token corresponding to the adminUser can access the API endpoints (permissionClass=isAdminUser).


## Overview
- A Vendor Profile Management System containing models such as Vendor,PurchaseOrder and HistoricalPerformance.<br/>
- For API development used django rest framework and Postman for checking API functionality.<br/>
- API endpoints are secured using Token based Authentication where only admin(token) can access.
- In this system there are :<br/><br/>
&nbsp; &nbsp; &nbsp; &nbsp; **Admin**  - manages vendors,purchase orders and historical Performance  <br/>
&nbsp; &nbsp; &nbsp; &nbsp; **Vendor** - returns acknowledgement for a purchase order <br/>

## API Endpoints
### I. Vendor Profile Management
In vendor profile management **all the api endpoints are secured using token authentication**, where admin with the token can only access the endpoints.
Postman is used to manage the API functionalities.So in Postman tool,Headers we pass a variable **Authorization** `(eg : Authorization - Token 3fcf22caed8e2863745d9effd957f2c376313da0)`
to access the functionality.

**1. POST `/api/vendors/` - Posting a vendor**<br/><br/>
- Passing variables such as **name,contact_details and address**<br/><br/>
&nbsp; &nbsp; &nbsp; &nbsp; eg: **{ "name":"vivek",
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"contact_details":"9978675645",
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"address":"123 street" }**

- The fields such as:<br/><br/>
&nbsp; &nbsp; &nbsp; &nbsp; **- fulfillment_rate <br/>
&nbsp; &nbsp; &nbsp; &nbsp; - on_time_delivery_rate<br/>
&nbsp; &nbsp; &nbsp; &nbsp; - quality_rating_avg<br/>
&nbsp; &nbsp; &nbsp; &nbsp; - average_response_time**<br/><br/>
      are not passed because these are the fields which has to be filled based on the vendor performance.
- The **vendor_code** is stored based on a backend logic (random number generation)
- Return a response in JSON format containing 



setting up endpoints
1. /api/vendor - create a vendor

   only want name, contact details , address atribute
   vendor code,and others are generated automaticaaly and initially others are 0 values , since there is no previos purchase trach records

   
