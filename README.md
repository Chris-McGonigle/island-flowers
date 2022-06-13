# Island Flowers by Sarah

Island Flowers by Sarah is a sole trader floristry business based in Enniskillen, County Fermanagh, Northern Ireland.

After losing her role as a childcare social worker during the pandemic, the client set about turning her flower arranging hobby into a viable business.

Up until this point the client has been relying on word of mouth, Facebook and Instagram to drive business leads. 

After a succesful launch, the client now wants to build on her business, and seeing how useful a website has been for competitors, she now feels the time is right to set up her own dedicated web presence.

You can view a live version of the [website](https://island-flowers.herokuapp.com/)

## Desktop
![Desktop View](/readme-images/desktop.png)

## Mobile

![Mobile View](/readme-images/mobile.png)

## Table of Contents

1. [Site Design Considerations](#site-design-considerations)
    * [Colour Scheme and Font](#colour-scheme-and-font)
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

Before commencing to design the site layout, I met with the client to discuss their needs and aspirations to ultimately try and discover the main aims behind having a website.

The client currently operates via word of mouth and facebook and instagram posts. Whilst these social media channels are useful, on their own they do have a number of limitations, for example time sensitive posts could get lost in a facebook timeline, and not appear until a couple of days after the event.

The site is envisiged to have a variety of visitor types, although female customers will make up the largest protion of these. Women are the largest consumers of flowers, with almost 80% percent of flower sales being attributed to female customers, *[Source](https://www.hanafloristpos.com/flower-shop-statistics/#:~:text=Women%20are%20the%20largest%20consumers,who%20is%20actually%20buying%20them.)* so the site should be geared towards a female audience in colour choice and even down to the tone of language used in blog posts.

The client currently operates on a cash only basis, so the ability to take payments via an ecommerce platform will make it: a) easier for customers to pay, and b) it will be easier to track orders via the django database than the current system of receipt books. It will also enable the client to receive orders outside of normal business hours, therefore increasing the chance of sales as the store will be available 24 hours a day.

The client hopes that having a web presence will expand her customer base. Analtyics carried out on her current social media channels show that her content is only being served to a small number of very close potential customers, so an enhanced online presence should result in a larger viewing base.

The client also wanted the product management element of the site to be as easy as possible, as the mother of two young children she finds it hard to deal with all the admin that can surround a site. To that end, a product and blog interface was included in the scope of the project so that the client could carry out as many actions as possible on the site as a superuser without having to log into the admin panel.

The client was also keen that the site was future proofed as much as possible. For example, the client does not currently charge for delivery, but in case they decide to in the future a delivery cost variable was included in the data models, but set to zero, so this could easily be implemented in future. SKU was also treated in this manner. The client does not currently use SKU to manage products, but by including the field in the data models, this again can be used by the client when required.


### Colour Scheme and Font 

To assist the client in tying together her business elements in one cohesive brand, the decision was taken that the website styling should match as closely as possible the existing store logo that the client had designed when first setting up her business.

The site logo was uploaded to [imagecolorpicker.com](https://imagecolorpicker.com/en) to determine the colours used in the existing site logo.

![Site Logo Colours](/readme-images/logo-colors.JPG)

* [#063549 - Tarawera](https://chir.ag/projects/name-that-color/#063549) was chosen for the site background

* [#fcffff - Twilight Blue](https://chir.ag/projects/name-that-color/#FCFFFF) was chosen as the main text colour for the site

* [#c7becd - Chatelle](https://chir.ag/projects/name-that-color/#C7BECD) was chosen as an accent colour for the product and blog cards

* [#cfb87f - Tan](https://chir.ag/projects/name-that-color/#CFB87F) was selected as a highlighter colour, especially around hyperlinks on hover to bring the users attention to a call to action link.

Using these existing colours means that the client does not have to start from fresh to rebrand her business, ultimately saving her time and money. This now ensures a consistency of branding and imaging across the clients social media platforms and now also her website.

The [Poppins](https://fonts.google.com/specimen/Poppins) font from Google Fonts was then selected as the site font across all pages.

It was chosen as it is a modern, clean legible font, that looks well across all screen sizes. It is a plain enough style as well that it does not conflict with the existing font used in the site logo, but instead compliments it.


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

#### Homepage

![Homepage](/readme-images/wireframes/home.png)

#### Products page

![Products](/readme-images/wireframes/products.png)

#### Single product page

![Single Product](/readme-images/wireframes/single-product.png)

#### Bag page

![Bag](/readme-images/wireframes/bag.png)

#### Checkout page

![Checkout](/readme-images/wireframes/checkout.png)

#### Blog

![Blog](/readme-images/wireframes/blog.png)

<br>

[Back to top](#table-of-contents)

<br>

### Project Management

The Kanban Boards feature of Github Projects was used as the project management tool during the production of this website. User stories were assigned two labels, one an EPIC label, and the second using the MoSCoW prioritisation technique.

EPICS were defined as User Accounts, Shop Browsing, Checkout & Bag, Site Admin and Blog. User Stories were then generated and designated as Must Have, Should Have, Could Have and Won't Have.

Must Have User stories were prioritised for completion first, and these were all implemented by project end. Once completed, tasks were moved to the Done pile. 

You can view the [Kanban Boards](https://github.com/Chris-McGonigle/island-flowers/projects/1?fullscreen=true) to see the project progress. Three tasks remain outstanding at this time. It would be envisaged that these tasks would be completed in future iterations.

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

#### Navigation Bar

The navigation bar contains a number of features vital to the smooth journey of a site visitor.

The navbar contains the site logo, which also doubles as a site wide link back to the homepage. A search bar is also present, which will search by name and/or description. 

Next is the account sign in icon. This will change depending on whether the user is a superuser or not. 

Finally, the bag icon contains a running subtotal of items added to it. It also serves as the link to open the site shopping bag page, and finally, toast warning messages appear in the section to convey information and confirmation to the user through out any tasks carried out, such as email sign up.

![Navigation Bar](/readme-images/navbar.JPG)

##### Ordinary User Menu

![User Menu](/readme-images/ordinary-user.JPG)

##### SuperUser Menu

![Superuser Menu](/readme-images/superuser.JPG)

##### Toast Message

![Toast message](/readme-images/toast.JPG)

#### Nav Links

Under the nav bar are three further navigation links. The first, Products, allows a user to filter all products by price or category. The category link allows the user to filter by category, and finally, the blog link directs the user to the main blog page.

![Nav links](/readme-images/nav-links.JPG)

#### Image Carousel and Home button

The image carousel on the homepage serves two purposes. First it displays an example of the products on offer, and second it holds the button to direct the user to the main products page.

![Carousel](/readme-images/carousel.JPG)

<br>

[Back to top](#table-of-contents)

<br>

#### Latest Blog Posts

The blog posts section renders out the last three blog posts made to the site and displays them to the user with a short description and the time created. A user can navigate to the blog post by clicking on the post image, or via the 'Read more...' link.

![Latest Blog](/readme-images/latest-blog.JPG)

<br>

[Back to top](#table-of-contents)

<br>

#### About section

The about section gives a little personal info about the client, and then gives text directions to the clients studio. A interactive Google map is also included here, with a marker set at the studio, to assist site users if they should require to visit the client.

![About](/readme-images/about.JPG)

<br>

[Back to top](#table-of-contents)

<br>

#### Footer

The site footer houses a number of very important features.
First of all, the owner contact details such as email, phone, and social media channels are all contained here. Each link is clickable and opens in a new window.

The footer also displays the site opening hours, and also contains a quick links section to the site, with links similar to the nav bar, apart from the inclusion of the Privacy Policy. The privacy policy is hosted by a third party and opens in a new window.

Finally, the newsletter sign up field is held in the footer. Users can enter their email to sign up to receive a newsletter. A link to unsubscribe from the newsletter is also included.

![Footer](/readme-images/footer.JPG)

A Back to top button also in the bottom right of the user viewport. Users can use this to navigate quickly to the top of the screen.

<br>

[Back to top](#table-of-contents)

<br>

#### All Products Page

The all products page lists all products currently available for purchase on the store. Users are displayed an image, category and price of each item. Clicking on an individual card brings the user to the specific product page for that item.

Users can also filter products by price, category, or name using the dropdown provided.

Edit and Delete Product links are displayed for the superuser only for ease of product management. 

![All Products Page](/readme-images/products.JPG)

<br>

[Back to top](#table-of-contents)

<br>

#### Individual Product Page

The individual products page lists all the product details of the item selected. Users are displayed an image, category and price of each item, in addition to a full description of the item. 

Users can then select a quantity of the item to add to their bag, amend the amount of a current bag item, or use the 'Keep Shopping' button to return to the all products page.

Should a user add an item to their bag, a confirmation message pops up, along with a current bag summary that directs the user to check out. They can of course continue shopping and add more products to their bag.

As with the all products page, Edit and Delete Product links are displayed for the superuser only for ease of product management. 

![Individual Product Page](/readme-images/single-product.JPG)

<br>

[Back to top](#table-of-contents)

<br>

#### Shopping Bag

When a user selects either the bag icon, or the Secure Checkout link in the toast pop up, the shopping bag page opens and displays to the user a summary of the items they have selected.

Users are shown an image, description and price. They also have the ability to adjust the quantty of the item in the bag, ot to remove the bag altogether. All of these actions are displayed to the user via the toast pop up.

A user can then opt to continue shopping, or to carry on to the checkout page.

![Shopping Bag](/readme-images/bag.JPG)

<br>

[Back to top](#table-of-contents)

<br>

#### Checkout Page

The checkout page is the second to last page on a users purchasing journey. On this page, a user is prompted to fill in their delivery details. They are also shown a final summary of their order.

If logged in, a user is given the option to save their delivery details for later. If not logged in, a user is prompted to sign in to save their details. A user of course can continue a purchase without signing in, however, if they have signed in and already agreed to have details saved previously, the user's delivery details are entered by default.

The user can also return to adjust their bag.

The stripe payment field is also contained here, and retunrs warning messages to the user if any validation errors occur.

Finally, if a user opts to complete their order, a loading overlay appears, and if successful they are directed to the checkout success page.

![Checkout](/readme-images/checkout.JPG)

<br>

[Back to top](#table-of-contents)

<br>

#### Checkout Success

Upon succesful completion of an order, a user is directed to the checkout success page.

Here they receive confirmation of their order and their order number. This is also communicated to them via a toast pop up. Users are then asked if they would like to visit the blog. This is to try and direct people to investigate other areas of the website that they might otherwise ignore.

![Checkout Success](/readme-images/success.JPG)

<br>

[Back to top](#table-of-contents)

<br>

#### My Profile page

The profile page serves two purposes. Here a user can update and save their delivery details. In addition, if a user has been logged on during a purchase, they can view a history of their orders on their profile page.

Clicking on one of these orders opens up the checkout success page from that order, but users are notified that they are viewing a historical order.

![Profile](/readme-images/profile.JPG)

![Historical order](/readme-images/order-history.JPG)

<br>

[Back to top](#table-of-contents)

<br>

#### Blog Page

The main blog page lists the most recent blog posts with the latest blog post appearing first. User are shown an image, descripiton and date posted

Users can click on the image or the read more link to open an individual blog post.

Superusers have the option to edit or delete blog posts from here. Superusers also have the option to use the 'Add Blog Post' button to add new content. As with the rest of the site, these options are hidden for all other users.

![Blog page](/readme-images/blog.JPG)

<br>

[Back to top](#table-of-contents)

<br>

#### Individual Blog Post

The individual blog page lists all of the post content shown on the main blog page, but in addition, users can also comment on the blog if they are logged in.

Nonlogged in users can still read all comments made, but they have to create an account or log in to make a comment. This is communicated to the user inplace of the comment box window when logged in. 

Comments display the commenters name, the time since commenting, and the comment body.

![Blog post](/readme-images/blog-post.JPG)

<br>

[Back to top](#table-of-contents)

<br>

#### Product and Blog Management (Superusers only)

Superusers can add and edit product and blog posts using the form management avaiable to them.

Accesed from a link in the nav dropdown, or via a link on each post/product, a user can use either the product form or blog form to make their content. The superuser can add images if desired, and if not a placeholder image is used instead.

Both these forms take the exact same format, with only the field labels being different.

The below image shows a composite of these screens for illustration purposes only, but in production, each of these forms has their own page.

![Admin](/readme-images/admin.JPG)

<br>

[Back to top](#table-of-contents)

<br>

#### Sign In/Up

The sign in page allows users to create an account or sign into an existing account. Each action is confirmed by a toast pop up relayed to the user. 

User input to these forms is handled by the built in allauth module.

The below image shows a composite of these screens for illustration purposes only, but in production, each of these forms has their own page.

![Sign Up/In](/readme-images/sign.JPG)

<br>

[Back to top](#table-of-contents)

<br>


### Future Features

There are a number of features that could be introduced in future iterations. Some of these could include:

1. Delivery charging
2. Ability to like blog posts
3. Single sign on with social media account/apple ID or google ID
3. Email notification to superuser of new order received
4. Newsletter templates and mass email issue mechanism

<br>

[Back to top](#table-of-contents)

<br>

## Technologies Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5) was used for the site markup.
* [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3) was used to style the HTML content.
* [Javascript](https://en.wikipedia.org/wiki/JavaScript) was used for the interactive elements.
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

After initial setup, stripe webhooks were failing. Stripe still received the order perfectly, but in the event of a system crash during ordering or similar, the webhook to create the order in the database was not happening, so theoretically, a user could place an order but the store might never receive it in the django database.

After investigation, an extra underscore when setting the webhook signing handshake variable in settings.py was discovered. With this underscore removed, webhooks were now being sucessfully received, and where necessary, these webhooks can now create orders in the database.

#### Quantity Selector error

As outlined in project walkthroughs, an error on larger devices results in the expected outcome of the minus quantity button being blanked out when the quantity selector is at zero. I was unable to rectify this within the timescale, but as it does not effect the functionality of the site, this was deemed to be acceptable at this time. It is something I would look to fix in future iterations.

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

To improve the search index rating on Google, research was carried out using a number of tools, such as [Wordtracker](https://www.wordtracker.com/) to search for relevant keywords to use in meta tags in the project head element.

Search terms such as florist and flowers were used to return popular keywords. A number of short and long tail keywords were then selected and inputted into the head element of base.html.

The selected keywords are:

* flowers
* florist
* mothers day
* florist in fermanagh
* florist near me
* enniskillen
* sympathy flowers

These keywords remain a work in progress however. As is normal practise, in production these keywords would be monitored via, for example, Google Analytics, to determine which terms are driving traffic to the site. 

These terms could then be added to, or removed as deemed necessary, and with continual improvement and refinement of these over time should utlimately assist in the site ranking higher on Google.

<br>

[Back to top](#table-of-contents)

<br>

## Marketing

The client employs a number of marketing strategies to try and drive business leads. Due to the rural location of the business, word of mouth is a very important tool, but cannot be quantified, so a number of measurable activites is required which will in turn assist in showing the most effective strategies that convert into actual sales.

The website will build on existing social media channels. A facebook page was set up for the client, but as the client already has an existing facebook presence, the page was then deleted to ensure it did not interfere with the clients existing business, or be suspected as a cloned account.

Before deletion a screenshot was taken of the page setup.

![Facebook page](/readme-images/facebook-page.png)

Alongside Instagram, this is the current main method of conversing with potential customers for the client.

The addition of the blog to the website is hoped to have two outcomes. First, regular, high quality blog content helps the website search ranking on Google. A higher placement in search results due to continually adding content, instead of just leaving the site as is should in turn lead to more custom.

The blog also highlights to site vistors other products they may not have considered, and also highlights flash sales and other promotions that the client may choose to run. Having this blog provides an extra free resource to get messaging out to the public. The commenting section of the blog also helps to drive customer engagement and start conversation, all of which should help to turn leads into sales.

A newsletter section was also added to reinforce this message. By utilising this format, the client can ensure that all customers on her list will receive news of upcoming offers etc in a way that the blog cannot (i.e. a blog post can only be read by a site vistor, where the newsletter will appear in all signed up users mailboxes) The newsletter however could contain links to blog posts, so both means of communication to customers can be interlinked, instead of being standalone methods.

Analytical tracking of blog visitors, and email tracking of the newsletter could then be implemented so the client has a better picture of the journey users take to her store, and in turn, with this information, she can tailor content to an even greater degree, which should hopefully result in an improvement of sales.

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