# Vendor-Management-System

## Introduction
A vendor management system using django and django-rest-framework.
This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.

## Installation
### 1. clone repository
`git clone https://github.com/SalmanSaalu/Vendor-Management-System.git`
### 2. Navigate project Directory
`cd backend`
### 3. Setup a virtual Environment and activate it
vms is the env name used 
`python -m venv vms
vms\scripts\activate`
### 4. Installing dependencies
`pip install -r requirements.txt`


## Step 2 : Project Setup

Project name is given as backend


simple jwt setup

installation
adjusting requirements in settings.py 
adding /api/token url 
adding refresh and access token expiration time in settings.py

setting up endpoints
1. /api/vendor - create a vendor

   only want name, contact details , address atribute
   vendor code,and others are generated automaticaaly and initially others are 0 values , since there is no previos purchase trach records

   
