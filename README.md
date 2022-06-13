# Island Flowers by Sarah

Island Flowers by Sarah is a sole trader floristry business based in Enniskillen, County Fermanagh, Northern Ireland.

After losing her role as a childcare social worker during the pandemic, the client set about turning her flower arranging hobby into a viable business.

Up until this point the client had been relying on word of mouth, Facebook and Instagram to drive business leads. 

After a succesful launch, the client now wants to build on her business, ad seeing how useful a website has been for competitors, she now feels the time is right to set up her own dedicated website.

## Desktop
![Desktop View](/readme-images/desktop.png)

## Mobile

![Mobile View](/readme-images/mobile.png)

You can view a live version of the [website](https://island-flowers.herokuapp.com/)

## Table of Contents

1. [Site Design Considerations](#site-design-considerations)
    * [User Stories](#user-stories)
        * [EPIC 1 - User Accounts](#epic-1---user-accounts)
        * [EPIC 2 - Shop Browsing](#epic-2---shop-browsing) 
        * [EPIC 3 - Checkout & Bag](#epic-3---checkout-and-bag)
        * [EPIC 4 - Site Admin](#epic-4---site-admin)
        * [EPIC 5 - Blog](#epic-5---blog)
    * [Wireframes](#wireframes)
    * [Project Management](#project-management)
2. [Data Models](#data-models)
3. [Features](#features)
    * [Initial Deployment Features](#initial-deployment-features)
    * [Future Features](#future-features)    
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
    * [Bugs](#bugs)
    * [User Story Testing](#user-story-testing)
        * [EPIC 1 Testing](#epic-1-testing)
        * [EPIC 2 Testing](#epic-2-testing) 
        * [EPIC 3 Testing](#epic-3-testing)
        * [EPIC 4 Testing](#epic-4-testing)
        * [EPIC 5 Testing](#epic-5-testing)
6. [Search Engine Optimisation](#search-engine-optimisation)
7. [Marketing](#marketing)        
8. [Deployment](#deployment)
9. [Credits](#credits)


## Site Design Considerations

### User Stories

#### EPIC 1 - User accounts

1. As a User, I want to be able to register for an account using my email address, so that I can save my details for future use.

2. As a User, I want to be able to register for an account using a social media account, so that I can save my details for future use.

3. As a User, I want to receive confirmation I have registered, so that I check that my account was created successfully and that my email address was correctly entered

4. As a User, I want to be able to reset my password, so that I can regain access to my account in case I forget my password.

5. As a User, I want to have a personalised profile page, so that I can view a history of my purchases.

<br>

[Back to top](#table-of-contents)

<br>

#### EPIC 2 - Shop Browsing

1. As a User, I want to view al list of products, so that I can select the item I want to purchase

2. As a User, I want to be able to select an individual product, so that I can see the full details of that item including price, description and sizes if applicable

3. As a User, I want to be able to sort the products by price, so that I can see products in my price range.

4. As a User, I want to be able to sort the products by category, so that I can filter to the type of product I am interested in

5. As a User, I want to be able to search for a product by name or description, so that I find a specific product I am interested in.

6. As a User, I want to filter the search results by price or category, so that I can further narrow down my search to find the item I am interested in.

7. As a User, I want to be able to add items to a basket, so that I can add multiple items before having to checkout.

<br>

[Back to top](#table-of-contents)

<br>

#### EPIC 3 - Checkout and Bag

1. As a User, I want to be able to see a list of my chosen products, so that I can confirm what I wish to purchase.

2. As a User, I want to be able to amend the size and quantity selected, so that I easily amend my order if I have made an error.

3. As a User, I want to be clearly shown the subtotal and shipping costs, so that I easily identify the total amount I have to pay.

4. As a User, I want to to be able to choose different billing and shipping addresses, so that I can have the item sent elsewhere if required.

5. As a User, I want to receive an email confirmation of my order, so that I can ensure that it was received by the vendor.

6. As a User, I want to be able to purchase an item with out creating an account, so that I do not have to have my details saved by the vendor.

7. As a User, I want to view an order success confirmation on screen, so that I can ensure my order was processed properly.


<br>

[Back to top](#table-of-contents)

<br>

#### EPIC 4 - Site Admin

1. As a Site Owner, I want to be notified when a new account is created, so that I am able to confirm if the account is legitimate or a bot or a duplicate account.

2. As a Site Owner, I want to be able to easily add new products, so that I am able to spend as little time as possible when updating the site.

3. As a Site Owner, I want to be able to easily update exisiting products, so that I can change descriptions, sizes or prices easily.

4. As a Site Owner, I want to be able to easily delete an exisiting product, so that I .can remove items that are no longer for sale.

<br>

[Back to top](#table-of-contents)

<br>

#### EPIC 5 - Blog

1. As a Site Owner, I want to be able to create blog posts, so that I can highlight any new products or events coming up.

2. As a Site Owner, I want to have users to be able to comment on my posts, so that I produce interaction and receive feedback from customers.

3. As a Site Owner, I want to give users ability to like posts, so that I can reaction to the product or post.

4. As a Site Owner, I want to have users create an acount before they can comment, so that I can moderate comments and stop anonymous commenting.

5. As a Site Owner, I want to display most recent blog posts on the homepage, so that I showcase news and new products without a user having to navigate to the blog page.


<br>

[Back to top](#table-of-contents)

<br>

### Wireframes



<br>

[Back to top](#table-of-contents)

<br>

### Project Management

The Kanban Boards feature of Github Projects was used as the project management tool during the production of this website. User stories were assigned two labels, one an EPIC label, and the second using the MoSCoW prioritisation technique.

EPICS were defined as User Accounts, Shop Browsing, Checkout & Bag, Site Admin and Blog. User Stories were then generated and designated as Must Have, Should Have, Could Have and Won't Have.

Must Have User stories were prioritised for completion first, and these were all implemented by project end. Once completed, tasks were moved to the Done pile. 

You can view the [Kanban Boards](https://github.com/Chris-McGonigle/island-flowers/projects/1?fullscreen=true) to see the project progress. Three tasks remain outstanding at this time. It would be invisaged that these tasks would be completed in future iterations.

<br>

[Back to top](#table-of-contents)

<br>

## Data Models

The following data models were used in the production of this website:

### Products App

#### Category Model

| Key | Name | Type |
|---|---|---|
| pk | name | CharField |
|  | friendly_name | CharField |

#### Product Model

| Key | Name | Type |
|---|---|---|
| pk | name | CharField |
| fk | category | Category Model |
|  | SKU | CharField |
|  | description | TextField |
|  | price | DecimalField |
|  | image | ImageField |

<br>

[Back to top](#table-of-contents)

<br>

### Checkout App

#### Order Model

| Key | Name | Type |
|---|---|---|
| pk | order_number | CharField |
| fk | user_profile | UserProfile Model |
|  | full_name | CharField |
|  | email | EmailField |
|  | phone_number | CharField |
|  | country | CountryField |
|  | postcode | CharField |
|  | town_or_city | CharField |
|  | street_address1 | CharField |
|  | street_address2 | CharField |
|  | county | CharField |
|  | date | DateTimeField |
|  | delivery_cost | DecimalField |
|  | order_total | DecimalField |
|  | grand_total | DecimalField |
|  | original_bag | TextField  |
|  | stripe_pid | Charfield |

#### OrderLineItem Model

| Key | Name | Type |
|---|---|---|
| fk | order | Order Model |
| fk | product | Product Model |
|  | quantity | IntegerField |
| | lineitem_total | DecimalField |


<br>

[Back to top](#table-of-contents)

<br>

### Profiles App

#### UserProfile Model

| Key | Name | Type |
|---|---|---|
| fk | user | User Model |
|  | default_phone_number | CharField |
|  | default_street_address1 | CharField |
|  | default_street_address2 | CharField |
|  | default_town_or_city | CharField |
|  | default_county | CharField |
|  | default_postcode | CharField |
|  | default_country | CountryField |

<br>

[Back to top](#table-of-contents)

<br>

### Blog App

#### Post Model

| Key | Name | Type |
|---|---|---|
| fk | author | User Model |
| fk | category | Category Model |
|  | title | CharField |
|  | body | TextField |
|  | image | ImageField |
|  | created_on | DateTimeField

#### Comment Model

| Key | Name | Type |
|---|---|---|
| fk | author | User Model |
| fk | post | Post Model |
|  | body | TextField |
|  | created | DateTimeField

<br>

[Back to top](#table-of-contents)

<br>

### Newsletter App

#### Subscriber Model

| Key | Name | Type |
|---|---|---|
| pk | email | EmailField |
|  | date_added | DateTimeField |

<br>

[Back to top](#table-of-contents)

<br>

## Features

### Initial Deployment Features



<br>

[Back to top](#table-of-contents)

<br>

### Future Features



<br>

[Back to top](#table-of-contents)

<br>

## Technologies Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5) was used for the site markup.
* [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3) was used to style the HTML content.
* [Javascript](https://en.wikipedia.org/wiki/JavaScript) was used for the Browse Subjects pop up.
* [Python3](https://en.wikipedia.org/wiki/Python_programming_language) and the Django Framework was the language used to produce the databases.
* [Black](https://github.com/psf/black) was used to format the Python Code
* [Balsamiq](https://balsamiq.com/) was used to produce the site wireframes.
* [Adobe Photoshop](https://www.adobe.com/uk/products/photoshop.html) was used to create the site icon.
* [Font Awesome](https://fontawesome.com/) was used for the site icons.
* [Google Fonts](https://fonts.google.com/) provided all of the fonts used on the site.
* [Firefox Developer tool](https://developer.mozilla.org/en-US/docs/Tools) was used to test site responsiveness and to test code.
* [Google Chrome Developer tools](https://developer.chrome.com/docs/devtools/) was used to test site responsiveness and to test code.
* [Safari Developer tools](https://support.apple.com/en-gb/guide/safari/sfri20948/mac) was used to test site responsiveness and to test code.
* [Github](https://github.com/Chris-McGonigle) was used as the repository hosting service.
* [Gitpod](https://www.gitpod.io/) was used as the Code Editor for the site.
* [W3C Markup](https://validator.w3.org/) and [Jigsaw validation](https://jigsaw.w3.org/) tools were used to validate the HTML and CSS used.
* [JSHint](https://jshint.com/) was used to validate the javascript used on site.
* [Pep8 Online](http://pep8online.com/) was used to validate the Python code.
* [Prettier](https://prettier.io/) was used to format the HTML Code
* [Heroku](https://www.heroku.com) was used to deploy the application.

<br>

[Back to top](#table-of-contents)

<br>

## Testing

A dedicated testing section covering validator and manual testing can be found in the [testing.md](/testing/testing.md) documentation

### Bugs

During the course of development, a number of bugs were found that are detailed below. 

#### Order total not showing on Checkout Success

On checkout success, it was discovered that the Order total was not being displayed to the user, despite the line items showing correctly on the order, and the shopping bag icon showing the correct amount. Checking stripe also showed the correct amount for the order being charged.

This item was rectified by amending an indent in the orderlineitem totals function in the checkout app. Removing the indent brought the save call out of the function and order totals then worked correctly.

#### Webhook errors

After initial setup, stripe webhooks were failing. Stripe still received the order perfectly, but in the event of a system crash during ordering or similar, the webhook to create the order in the database was not happening, so theoretically, a user could place an order but the store never received it in the django database.

After investigation, it was discoverd an extra underscore when setting the webhook signing handshake variable in settings.py. With this underscore removed, webhooks were now being sucessfully received, and where necessary, these webhooks can now create orders in the database.

#### Quantity Selector error

As outlined in project walkthroughs, an error on larger devices results in the expected outcome of the minus quantity buttn being blanked out when the quantity selector is at zero. I was unable to rectify this within the timescale, but as it does not effect the functionality of the site, this was deemed to be acceptable at this time. It is something I would look to fix in future iterations.

<br>

[Back to top](#table-of-contents)

<br>

### User Story Testing

#### EPIC 1 Testing

1. As a User, I want to be able to register for an account using my email address, so that I can save my details for future use.
    * RESULT - TEST PASSED

2. As a User, I want to be able to register for an account using a social media account, so that I can save my details for future use.
    * RESULT - TEST FAILED - TO BE INTRODUCED IN FUTURE ITERATION

3. As a User, I want to receive confirmation I have registered, so that I check that my account was created successfully and that my email address was correctly entered.
    * RESULT - TEST PASSED

4. As a User, I want to be able to reset my password, so that I can regain access to my account in case I forget my password.
    * RESULT - TEST PASSED

5. As a User, I want to have a personalised profile page, so that I can view a history of my purchases.
    * RESULT - TEST PASSED

<br>

[Back to top](#table-of-contents)

<br>

#### EPIC 2 Testing

1. As a User, I want to view all list of products, so that I can select the item I want to purchase.
    * RESULT - TEST PASSED

2. As a User, I want to be able to select an individual product, so that I can see the full details of that item including price, description and sizes if applicable.
    * RESULT - TEST PASSED

3. As a User, I want to be able to sort the products by price, so that I can see products in my price range.
    * RESULT - TEST PASSED

4. As a User, I want to be able to sort the products by category, so that I can filter to the type of product I am interested in.
    * RESULT - TEST PASSED

5. As a User, I want to be able to search for a product by name or description, so that I find a specific product I am interested in.
    * RESULT - TEST PASSED

6. As a User, I want to filter the search results by price or category, so that I can further narrow down my search to find the item I am interested in.
    * RESULT - TEST PASSED

7. As a User, I want to be able to add items to a basket, so that I can add multiple items before having to checkout.
    * RESULT - TEST PASSED

<br>

[Back to top](#table-of-contents)

<br>


#### EPIC 3 Testing

1. As a User, I want to be able to see a list of my chosen products, so that I can confirm what I wish to purchase.
    * RESULT - TEST PASSED

2. As a User, I want to be able to amend the size and quantity selected, so that I easily amend my order if I have made an error.
    * RESULT - TEST PASSED

3. As a User, I want to be clearly shown the subtotal and shipping costs, so that I easily identify the total amount I have to pay.
    * RESULT - TEST PASSED

4. As a User, I want to to be able to choose different billing and shipping addresses, so that I can have the item sent elsewhere if required.
    * RESULT - TEST PASSED

5. As a User, I want to receive an email confirmation of my order, so that I can ensure that it was received by the vendor.
    * RESULT - TEST PASSED

6. As a User, I want to be able to purchase an item with out creating an account, so that I do not have to have my details saved by the vendor.
    * RESULT - TEST PASSED

7. As a User, I want to view an order success confirmation on screen, so that I can ensure my order was processed properly.
    * RESULT - TEST PASSED

<br>

[Back to top](#table-of-contents)

<br>

#### EPIC 4 Testing

1. As a Site Owner, I want to be notified when a new account is created, so that I am able to confirm if the account is legitimate or a bot or a duplicate account.
    * RESULT - TEST FAILED - TO BE INTRODUCED IN FUTURE ITERATION

2. As a Site Owner, I want to be able to easily add new products, so that I am able to spend as little time as possible when updating the site.
    * RESULT - TEST PASSED

3. As a Site Owner, I want to be able to easily update exisiting products, so that I can change descriptions, sizes or prices easily.
    * RESULT - TEST PASSED

4. As a Site Owner, I want to be able to easily delete an exisiting product, so that I .can remove items that are no longer for sale.
    * RESULT - TEST PASSED

<br>

[Back to top](#table-of-contents)

<br>

#### EPIC 5 Testing

1. As a Site Owner, I want to be able to create blog posts, so that I can highlight any new products or events coming up.
    * RESULT - TEST PASSED

2. As a Site Owner, I want to have users to be able to comment on my posts, so that I produce interaction and receive feedback from customers.
    * RESULT - TEST PASSED

3. As a Site Owner, I want to give users ability to like posts, so that I can reaction to the product or post.
    * RESULT - TEST FAILED - TO BE INTRODUCED IN FUTURE ITERATION

4. As a Site Owner, I want to have users create an acount before they can comment, so that I can moderate comments and stop anonymous commenting.
    * RESULT - TEST PASSED

5. As a Site Owner, I want to display most recent blog posts on the homepage, so that I showcase news and new products without a user having to navigate to the blog page.
    * RESULT - TEST PASSED

<br>

[Back to top](#table-of-contents)

<br>

## Search Engine Optimisation

<br>

[Back to top](#table-of-contents)

<br>

## Marketing

<br>

[Back to top](#table-of-contents)

<br>

## Deployment

Local deployment was carried out using the Command Line Interface. to enable this the following steps were carried out:

1. Create a repository on GitHub.
2. Clone the repository on your chosen source code editor (GitPod in my case) using the clone link.
3. Open the terminal within GitPod
4. Enter "python3 manage.py runserver into the terminal.
5. Go to localhost address on my web browser.
6. All locally saved changes will show up here.

For the final deployment to Heroku, the following was carried out:
1. Create Heroku App
2. Install dj_database_url and psycopg2-binary in my local environment
3. Freeze requirements.txt file
4. In settings.py import dj_database_url
5. Back up the local database using "./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json" in the terminal window.
6. Comment out the local default database
7. Add the Heroku database url via dj_database_url.parse()
8. Run migrations to the Postgres database
9. Restore the database using this command "./manage.py loaddata db.json" in the terminal windows.
10. Create a SuperUser for the Postgres database
11. Configure the database so that when the app is running on Heroku it uses the Postgres database and when it's running locally it uses the SQLite database
12. Create Procfile so that Heroku creates a web dyno so that it will run gunicorn and serve the Django app
13. Disable Heroku collect static
14. Add the Heroku hostname to allowed hosts in settings.py
15. Generate a new Django secret key and add this to the Heroku config variables
16. Replace the secret key in settings.py to grab it from the environment
17. Set debug to True only if the environment is a development environment
18. Commit changes and deploy to GitHub and Heroku
19. Create an AWS account
20. Create an S3 bucket
21. Configure the S3 bucket settings and policies
22. Create and configure the IAM service
23. In the terminal install Boto3 and Django-storages
24. Freeze requirements.txt file
25. Add a statement to the AWS bucket if the environment is "USE_AWS"
26. Add AWS keys to the Heroku config variables
27. Create custom storage classes for media and static files
28. In settings.py add a statement to use the static and media storage class and locations
29. Commit and push to GitHub and Heroku
30. In the S3 bucket create a new folder for media
31. Upload all used images to the media file in the S3 bucket
32. Add the Stripe keys to the Heroku config variables
33. Create a new webhook endpoint from the Stripe dashboard
34. Add all the Stripe keys to the Heroku config variables

<br>

[Back to top](#table-of-contents)

<br>

## Credits

1. The code for the home page carousel was taken from the [Bootstrap documentation](https://getbootstrap.com/docs/4.0/components/carousel/) and amended for this project. I also used tutorials on [easyhtml5video.com](https://easyhtml5video.com/articles/bootstrap-carousel-image-680.html) to help in getting the images to display correctly.

2. The ecommerce portion of the website was adapted from the Code Institute 'Boutique Ado' walkthrough project.

3. Tutorials from [Code with Stein](https://www.youtube.com/playlist?list=PLpyspNLjzwBkvj8eSmGcQLC50k55NXWRP) and [Codemy](https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi) assisted in the production of the blog pages.

4. Tutorials from [KenBrotech](https://www.youtube.com/watch?v=hWtlskOaFNI) and [Master Code Online](https://www.youtube.com/watch?v=TBVsILIt4HM) assisted in the creation of the newsletter app.

5. An article on [Open Classrooms](https://openclassrooms.com/en/courses/7107341-intermediate-django/7264795-include-multiple-forms-on-a-page) helped in how to use multiple crispy forms on one page.

6. The site Privacy Policy was generated using [gdprprivacynotice.com](https://www.gdprprivacynotice.com).

7. The site favicon was created on [favicon.io](https://favicon.io/favicon-converter/).

8. Product images and text were taken from the [Memento Floral Design](https://www.mementofloraldesign.com/) website.

9. Images and text for the blog post were sourced from the clients existing Facebook page.

10. The site logo was provided by the client.

<br>

[Back to top](#table-of-contents)

<br>