# OneStopTechShop

## Introduction

One Stop Tech Shop is an online store using data retrieved from a public library. It is a fully functioning e-commerce site, built using the python framework Django.
It was styled using Material design bootstrap, which offers more functionality than standard bootstrap 5. Users of this website can find products via the category selector in the navigation bar, search for products using keywords found in the title or description and scroll through the all products page to view our full catalogue. Users can also create an account to store order history and their preferred delivery address. 

![Homepage](/docs/img/responsive) 
Live deployment link

## Table of contents
* [Introduction](#introduction)
* []


## Ux
### Site Goals
### Target User
### User Stories
## Design
### Wireframes
### Color Prototypes
### Entity Relationship Diagram
### Colours
### Iconography 
    - font, images, icon packs, logo,

## Site Usage
### Navigation
#### Navigation bar
#### Footer
#### Homepage

## Site Management
### Product Management
    In order to avoid staff users having access to Django's built in admin page, I implemented CRUD functionality for users with the is_staff flag. This functionality will not be visible to standard users and they are blocked from accessing the page. 
    Via this admin page, a staff user can edit any fields of the selected product and related Categories. 
### User management
    I don't want staff level users to have access to manage user accounts, so for now I am leaving User account administration to the site owner, with access to the Admin console in Django. The user themselves will be able to reset their password, update their name and address without having to contact the site owner. 
## Testing
### Manual testing - link
### Django Unit Test
    using Django's built in unit test library, I implemented tests for all of the database models in the applications. I also wrote tests for the major view functions, ensuring that all pages will render as intended. 
## Technologies
* Python / Django
    * Django is the python framework used to create this web application
    * Django contains many useful libraries, such as AllAuth, to make development smoother. I used aul Auth to implement user accounts. 
* Javascript
* Material Design Bootstrap (MDB)
* Font Awesome - for icons
* Custom CSS alongside MDB
* HTML 5
* VSCode
* Python VENV to manage development environment
* Git + Github for version control
* Balsamiq 
    * Basic Design wireframs
* Canva 
    * Prototype colour designs of the website

## Deployment

## References 
 - The Django / Python Documentation websites were consulted when looking into new features, such as Forms.
 - The MDB Website for styling documentation
 - The Code Institute course material as a reference for previously written code or examples on how certain things are implemented, such as django Fixtures
 - Any code requiring a reference to another source will have be commented with the source
