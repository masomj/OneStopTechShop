# OneStopTechShop

## Introduction

One Stop Tech Shop is an online store using data retrieved from a public library. It is a fully functioning e-commerce site, built using the python framework Django.
It was styled using Material design bootstrap, which offers more functionality than standard bootstrap 5. Users of this website can find products via the category selector in the navigation bar, search for products using keywords found in the title or description and scroll through the all products page to view our full catalogue. Users can also create an account to store order history and their preferred delivery address.

There are differing permissions levels, allowing a staff user to manage the products on the site. 


[Live deployment link](https://one-stop-tech-shop.herokuapp.com/) 

## Table of contents
* [Introduction](#introduction)
* [UX](#ux)
* [Design](#design)
* [Deployment](#deployment)
* [Site Management](#site-management)


## Ux
### Site Goals
The site aims to generate revenue by providing an online store for users to purchase items.
### Target User

This site is aimed at Gamers. The products on this site were gleamed from an online repository (kaggle),that had the products from GameStop.com. I used this JSON file create the products in my store.

### User Stories

| Site User   | Register for an account                           | so i can view my previous orders and store my details           |
|-------------|---------------------------------------------------|-----------------------------------------------------------------|
| Site User   | Login / Logout                                    | access / secure my account information                          |
| site user   | manage my details                                 | change my details if required                                   |
| site user   | be provided visual feedback on interactions       | so i know if my interaction succeeded                           |
| site user   | access order history                              | so i can re-order an item should i desire                       |
| shopper     | add an item to shopping back                      |  in order to purchase it                                        |
| shopper     | view product details                              | to make an informed buying decision                             |
| shopper     | view the total of my bag                          | manage my budget                                                |
| shopper     | remove items from my bag                          | manage my budget                                                |
| shopper     | sort the list of products in a variety of manners | to filter down an item i am looking for                         |
| shopper     | search the site for keywords                      | find a specific item                                            |
| shopper     | purchase multiple of the same item                | bulk buy products                                               |
| shopper     | easily enter payment info                         | purchase items with 0 hassle                                    |
| shopper     | checkout as guest                                 | not have to have an account to checkout                         |
| shopper     | have safe and secure data                         | ensure using this site doesn't become a personal security breach|
| shopper     | leave a review of items                           | show other shoppers what is worth buying                        |
| store owner | add a product                                     | add new items to the store                                      |
| store owner | add a new category / parent category              | sort products into the respective categories                    |
| store owner | delete a product                                  | remove items that are no longer being sold                      |
## Design
In order to style the website, I used the Material Design Bootstrap framework(MDB). This allowed me to get elements such as the large category selector up and running with less CSS to write, and focus on the back end of the application.
The website is written with semantic and accessible HTML where applicable, providing ALT attributes for images and endeavouring to make the page accessible for screen readers.

The website is responsive across all standard screen sizes, this was made easier by the usage of MDB elements, as I didn't have to write custom CSS for a different screen sizes.

### Color Prototypes
Before starting the project, I created some color prototypes to help guide the overall design process. The colour scheme has deviated from these designs, being replaced with a more neutral theme, instead of the black and white. These mockups helped guide the overall look of the site though.
![Landing Page](/docs/images/color_landingPAge.png)
![Products Page](/docs/images/color_products.png)
![Login Page](/docs/images/color_login.png)
![Bag Page](/docs/images/color_bag.png)
### Entity Relationship Diagram
Before creating the project, I used the user stories to devise what would be required, and produced the following entity relationship diagram. Some fields have been altered in this diagram since it was first created, as whilst developing I found the need, or lack thereof, for other fields.
![Entity RelationShip Diagram](/docs/images/One%20Stop%20Tech%20shop%20entity%20relationship.png)
### Colours
The initial colours were intended to be black, white and purple. I decided that these were to strong, so reverted to using black, white and an off-white. Using bootstraps standard color themes for buttons throughout the site.
### Iconography
For the icons in the site, I used Font Awesome. This is the industry standard.
The hero image was gleamed from Canva, during the colour prototyping stage. This is a free to use image, with no copyright implications to doing so.

## Site Usage
### Navigation
#### Navigation bar
The ever present navigation bar ensures that the user can access a multitude of pages no matter where they are in the website. The category selector is dynamically generated, with data passed to it via a context processor. Any updates to the different categories are instantly reflected in that.

In order to undertake administration of the products and categories. The Admin page is a navigation link. This is only visible if you are logged in and have the 'super_user' permission.
#### Footer
The footer provides some basic information and informs the user they have reached the end of a given page. It has the website name and a copyright disclaimer.
#### Homepage

The homepage is a standard landing page, enticing the user to click and visit the products page, without overwhelming a potential first time user.
## Site Management
### Product Management
    In order to avoid staff users having access to Django's built in admin page, I implemented CRUD functionality for users with the is_staff flag. This functionality will not be visible to standard users and they are blocked from accessing the page. 
    Via this admin page, a staff user can edit any fields of the selected product and related Categories. 
    At present, a product can only be edited by entering the 'productInfo' page. If you are logged in and have 'is_staff' permissions, you will then be able to either delete or update the product.
    The Admin page also provides update and create functionality for the Category and Parent category model. I Chose not to implement the delete functionality here, as I would not like to give permissions to staff to remove entire categories of products at once. 
### User management
    I don't want staff level users to have access to manage user accounts, so for now I am leaving User account administration to the site owner, with access to the Admin console in Django. The user themselves will be able to reset their password, update their name and address without having to contact the site owner. 
## Testing
### Manual testing
I undertook manual functionality testing continually whilst developing the site. After completing an aspect of the functionality, I ensured that any components of the site it interact with worked as intended and the original function was intact also.

In addition to performing the testing manually, after deploying the site to heroku, I had family members use the app as if they were buying an item. This uncovered an issue with the navigation bar, specifically the category selector. On mobile, as it originally used a :hover class selector, it didn't function as desired. I changed the style the Mega Menu it is currently. this helps with more direct category based navigation anyway. In addition, as the category selector is rendered dynamically, on every view, it would have required the data passing to it. In order to combat this, I implemented a context processor to store the category objects.

The application passed several standard validators, such as PEP8 and the W3schools HTML validator.

Upon lighthouse testing, it was reveled that the performance of my site is not as it could be. This is due to pulling the product images from Gamestop's website via a url. I chose to leave this implementation in place though, as for the purposes of this project, changing the method, to store the product image file myself, would result in incurring costs from the AWS S3 host. After the initial deployment, I had already used up 85% of the free allocation, so I felt it prudent to reduce request to service.

Another aspect of the performance issues is that on the product pages, nearly 300 products are loaded. In future, I would implement pagination to resolve this, do display maybe 30 products at a time instead. I am not aware of how to implement this at the moment, and decided to devote my time and resources into other features, like the reviews app.
### Django Unit Test
    In order to ensure future updates don't break the site, I implemented some test cases on models in the app. This was done using Django's built in testing library
## Technologies
* Python / Django
    * Django is the python framework used to create this web application
    * Django contains many useful libraries, such as AllAuth, to make development smoother. I used all Auth to implement user accounts.
* Javascript
* Postgresql - Elephant provided the hosting
* Heroku - Hosting
* Material Design Bootstrap (MDB)
* Font Awesome - for icons
* Custom CSS alongside MDB
* HTML 5
* VSCode
* Python VENV to manage development environment
* Git + Github for version control
* Canva 
    * Prototype colour designs of the website

## Deployment
### Postgres
1. Due to heroku removing free access to postgres add ons, we now need to host our projects database's on Elephant Sql
2. Navigate to ```https://www.elephantsql.com/``` and create an account
3. Select new instance and follow the wizard through the set up process, ensuring you select the region closest to you
4. Once completed, ensure you capture the database url, for the below config variables. 
5. I would recommend doing this as soon as you spin up a new django project, rather than using the built in SQLite database, as you will have to migrate data and models over to a new database otherwise
6. In your .settings file, ensure you have the following section:

```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

7. Ensure that you run migrations on both databases,if you want to use the SQLite DB as a development databse, otherwise ensure that the postgres database's migrations are up to date

### Heroku

1. Ensure all the required packages in the Requirements.txt file by running ``` pip3 freeze > requirements.txt```
2. Crate a Heroku procfile, named 'Procfile', with no extension. The contents of this need to be ```web: gunicorn OneStopTechShop.wsgi:application ```
3. Push these changes to GitHub, using ```git add .```, ```git commit -m``` and ```git push```
4. Navigate to [Heroku](https://www.heroku.com/), and login or create an account
5. Once logged in, click on 'resources'
6. From the app's dashboard, click on 'settings', and then 'reveal config vars' in order to set the necessary configuration variables for the project. 
It should look like this:

| Key                   | Value                      |
|-----------------------|----------------------------|
| AWS_ACCESS_KEY_ID     | AWS Access Key             |
| AWS_SECRET_ACCESS_KEY | AWS Secret Access Key      |
| DATABASE_URL          | Database URL               |
| EMAIL_HOST_PASS       | Email Password             |
| EMAIL_HOST_USER       | Email Address              |
| SECRET_KEY            | Django Secret Key          |
| STRIPE_PUBLIC_KEY     | Stripe Public Key          |
| STRIPE_SECRET_KEY     | Stripe Secret Key          |
| STRIPE_WH_SECRET      | Stripe WH Key              |
| USE_AWS               | TRUE                       |

9. Back on the main dashboard, click on 'deploy', and then under the 'Deployment' method section, select GitHub and 'Automatic Deploys'. If you plan on making many more commits, it may be wise to leave this unticked until its required, as it will aid with AWS and other resource usage. 

11. Make migrations using the following:
```
python3 manage.py makemigrations
```
and migrate the database models to the Postgres database using:
```
python3 manage.py migrate
```
I recommend running makemigrations with the --dry-run flag to ensure that migrations are going to be as intended, before they are created

12. In order to populate the database with data, I used django's fixtures method. If spinning up a new database, the data.json already contains the products and category data that is required. To add this to the database, run ```python3 manage.py loaddata data.json ```

13. Create a superuser with the following command:
```
python3 manage.py createsuperuser
```
and then enter chosen email, username and password.

15. Disable 'COLLECTSTATIC' with the following code: ``` heroku config:set DISABLE_COLLECTSTATIC=1 ``` This will create and environment variable in your heroku app, so that Heroku doesn't attempt to collect the static files. As this will be done once AWS is ready for use.
16. Add ```ALLOWED_HOSTS = ['<heroku Deployed app address>', 'localhost']``` to settings.py. You may also need to add your local development IP of '127.0.0.1'
17. Add Stripe environment variables to your .env file
18. Push to Heroku using the following command:
```git push heroku main``` Heroku will then attempt to build the app.

### Amazon Web Services Static File Storage:

Heroku cannot handle to static data for this app, so we will use AWS to host it. AWS's S3 platform has a free offering that will suit our usecase, if used correctly. 
In order to create your own bucket, please follow the instructions on the AWS website
[Here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html)

1. In the terminal, install boto3 and django-storages using:
```pip3 install boto3 ``` and ```pip3 install django-storages```
2. Freeze the new requirements into the 'requirements.txt' file using ```pip3 freeze > requirements.txt```
3. Add 'storages' to INSTALLED_APPS in settings.py.

4. The following excerpt from settings.py is what allows us to tell django to use AWS when deployed to heroku, or if run locally, keep to standard methods
```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME='onestoptechshop'
    AWS_S3_REGION_NAME='eu-west-1'
    AWS_ACCESS_KEY_ID= os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY= os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION =   'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION ='media'
    
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
5. custom_storage.py app, in the root of the project, is to point to the correct storage location. It should contain the following:
```from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
6. Now that AWS is set up, remove the 'collectstatic' environment variable from your heroku variables.

7. Git add, commit and push the changes to your repository, prompting heroku to rebuild the app if automatic deployments are not enabled

### Making a Local Clone:

1. To create a local clone of the repository, open a terminal window in VS code, provided git CLI is installed and use the following :

``` git clone https://github.com/masomj/OneStopTechShop.git ```
2. Create a .env file and include the below

The following code needs to be added to the .env.py file:
```
STRIPE_PUBLISHABLE_KEY=
STRIPE_SECRET_KEY=
DATABASE_URL=
SECRET_KEY=
DEVELOPMENT=True
EMAIL_HOST_USER=
EMAIL_HOST_PASS=
  
```

3. Then make sure that the required packages are installed by running the following command: 
```pip install -r requirements.txt```

4. Make migrations and then migrate in order to create a database, by running the following commands:
```python3 manage.py makemigrations``` and ```python3 manage.py migrate```.

5. Load the fixtures from the 'data.json' file. This contains the data for the category Parent category and Product models.
This is done by using the following:
```
python3 manage.py loaddata data.json
```

6. Create a superuser with the following command: ```python3 manage.py runserver``` and entering your credentials.

Run the app by entering the following command:
```python3 manage.py runserver```
## References 
 - The Django / Python Documentation websites were consulted when looking into new features, such as Forms.
 - The MDB Website for styling documentation
 - The Code Institute course material as a reference for previously written code or examples on how certain things are implemented, such as django Fixtures
 - The boutique ado project, for guidance on how to create context processor, how to implement stripe and some logic for that, and the logic for the product sort selector on the product page. Any code that     isn't referenced, but is used from this project is either coincedntal code, or an error in not referencing it inline.
 - Stackoverflow for bug fixing and error source hunting
 - Slack community for previous fixes for similar issues, such as using django's load data when migrating from sqlite to postgres
 - Any code requiring a reference to another source will have be commented with the source
