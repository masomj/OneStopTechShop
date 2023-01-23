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
The site aims to generate revenue by providing an online store for users to purchase items.
### Target User

This site is aimed at Gamers. The products on this site were gleamed from an online respository,that had the products from GameStop.com. I used this JSON file create the products in my store.
### User Stories
## Design
In order to style the website, I used the Material Design Bootstrap framework(MDB). This allowed me to get elements such as the large category selector up and running with less CSS to write, and focus on the back end of the application.
The website is written with semantic and accessible HTML where applicable, providing ALT attributes for images and endeavouring to make the page accessible for screen readers.

The website is respnsives accross all standard screen sizes, this was made easier by the usage of MDB elemements, as I didnt have to write custom CSS for a different screen sizes.


### Wireframes
### Color Prototypes
### Entity Relationship Diagram
### Colours
### Iconography 
For the icons in the site, I used Font Awesome. This is the industry standard.
The hero image was gleamed from Canva, during the colour prototyping stage. This is a free to use image, with no copyright implications to doing so.

## Site Usage
### Navigation
#### Navigation bar
The ever present navigation bar ensures that the user can access a multitude of pages no matter where they are in the website. The category selector is dynamically generated, with data passed to it via a context processor. Any updates to the different categories are instantly reflected in that.

In order to undertake administration of the products and categories. The Admin page is a navigation link. This is only visisble if you are logged in and have the 'super_user' permission.
#### Footer
The footer provides some basic information and informs the user they have reached the end of a given page. It has the website name and a copyright disclaimer.
#### Homepage

## Site Management
### Product Management
    In order to avoid staff users having access to Django's built in admin page, I implemented CRUD functionality for users with the is_staff flag. This functionality will not be visible to standard users and they are blocked from accessing the page. 
    Via this admin page, a staff user can edit any fields of the selected product and related Categories. 
    At present, a product can only be edited by entering the 'productInfo' page. If you are logged in and have 'is_staff' permissions, you will then be able to either delete or update the product.
    The Admin page also provides update and create functionality for the Cateogory and Parent category model. I Chose not to implement the delete functionality here, as I would not like to give permissions to staf to remove entire categories of products at once. 
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
