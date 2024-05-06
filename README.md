# Vendor-Management-System

## Intruduction
A vendor management system using django and django-rest-framework.
This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.
: Environment Setup

vms is the env name used  
`python -m venv vms
vms\scripts\activate`


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

   
