# Testing for the website 'Island Flowers by Sarah'

The following document outlines all testing carried out on the website 'Island Flowers by Sarah'

During the construction process, the Dev Tools functionality of Chrome was used to test CSS code initially, where it was then tweaked to the desired outcome.

## Table of Contents

 1. [Validator testing](#validator-testing)
    * [HTML](#html)
    * [CSS](#css)
    * [Lighthouse](#lighthouse)
    * [Javascript](#javascript)
    * [Contrast Checker](#contrast-checker)
    * [Pep8](#pep8)
2. [Manual testing](#manual-testing)
    * [Responsive testing](#responsive-testing)
    * [Element testing](#element-testing)
3. [Customer purchase testing](#customer-purchase-testing)
    * User not logged in
    * User logged in
    * User kicked out during submit process


## Validator testing

To view testing images please click on each individual hyperlink. These files can also be found in the [testing images](/testing/images/) folder.

### HTML

All HTML pages were passed through for testing via [W3C](https://validator.w3.org/) and the results are as follows:

1. [Homepage](/testing/images/home.png)

A total of 22 errors and warnings were received on the first pass through the W3C validator. 

The 'li' tag as child of a nav element errors were ignored as this was the same process as used in the project walkthrough videos.

The duplicate id 'user-options' warning was ignored as the validator is picking up the mobile and desktop versions of the nav bar account dropdowns, again matching the style as per the walkthrough videos so this was ignored.

The javascript type warnings were also ignored, again as the code matches that as shown by the instructor videos.

All other errors listed were addressed and on retest only the previously ignored warnings remain.

2. [Products](/testing/images/products.png), [Blog](/testing/images/blog.png), [Profile](/testing/images/profile.png) and [Checkout Pages](/testing/images/checkout.png)

Tests on all four of these pages returned the same errors that were ignored in the previous testing of the homepage. No other errors were returned so these pages were left as is.

3. [Bag](/testing/images/bag-errors.jpg)

Running the bag app through the validator returned two errors. One was an unclosed outer div element which was added. Closing this div removed the body tag error that had been received as well.

<br>

[Back to top](#table-of-contents)

<br>

### CSS

The CSS was tested using [Jigsaw](https://jigsaw.w3.org/css-validator/).

1. Homepage

 ![Home CSS Errors](/testing/images/css-home.JPG)

 CSS testing returned three errors. The first error was fixed by removing the superfluous comma operator.

 Error two was fixed by changing the selector name from align to align-items.

 Error three was fixed by removing the additional colon.

 The 697 warnings received were all ignored apart from line 363 where the background-color and border has been set to the same color, so the border field was removed. All other warnings related to vendor extensions and pseudo-elements were also ignored.

 The page was retested and all errors were cleared.

 2. [Products](/testing/images/css-products.JPG), [Blog](/testing/images/css-blog.JPG), [Profile](/testing/images/css-profile.JPG), [Bag](/testing/images/css-bag.JPG) and [Checkout Pages](/testing/images/css-checkout.JPG)

 Tests on the remaining pages generated no errors at all, and the same warnings that were returned for the homepage, so these were also ignored.


<br>

[Back to top](#table-of-contents)

<br>

### Lighthouse

The site was tested for accessibility, performance and best practise using Google's [Lighthouse](https://developers.google.com/web/tools/lighthouse) tool. The results were as follows:

<br>

[Back to top](#table-of-contents)

<br>

### Contrast Checker

The background and foreground color were checked for contrast using the [WebAIM](https://webaim.org/resources/contrastchecker/) contrast checker tool.

The main site colours of #063549 and #fcffff were fed into the tool and the contrast ratio passed with a score of 12.94:1

![Contrast Checker](/testing/images/contrast.JPG)

<br>

[Back to top](#table-of-contents)

<br>

### Javascript

[JS Hint](https://jshint.com/) was used to to check for any errors within the JavaScript script files. 

Stripe_elements.js in the checkout app returned three warnings and no errors. The first two regarding template literal syntax was ignored, and the missing semicolon highlighted was added in.

![stripe-elements.js](/testing/images/stripe-elements.JPG)

The js within quantity_input_script.html in the products app returned three warnings and no errors. Again these warnings were template literal warnings and could be ignored.

![quantity_input_script.html](/testing/images/quantity-input.JPG)

Countryfield.js within the profiles app retunred only two warnings. The first was ignored as it was highlighting the use of 'let' to set a variable. The unnecessary semicolon highlighted was removed.


<br>

[Back to top](#table-of-contents)

<br>

### Pep8

To check against Pep8 standards, all apps were first passed through the [Black](https://pypi.org/project/black/) code formatting tool to correct any formatting issues.

Code was then checked for errors via the terminal command "python3 -m flake8". This returned a number of whitespace and indentation errors which were rectified where possible. (The unfixed errors were situated in root files such as .vscode/artictern)

Other errors regarding unused imports were ignored as these did not alter the functionality of the site.

Line too long errors were kept to an absolute minimum. On occasion such as in settings.py files, due to the importance of these files, the warnings were ignored. Warnings were also ignored where splitting a f-string would change the onscreen rendering layout so these were also left as it, but as stated previous were kept to an absolute minumum.


<br>

[Back to top](#table-of-contents)

<br>

## Manual testing

 ### Responsive testing

 The site was tested extensively using the dev tools facilties of Chrome, Safari and Firefox. It was tested against most popular makes of phones and tablets, as well as varying desptop screen resolutions. 

 It was found to be responsive across all tested platforms.


<br>

[Back to top](#table-of-contents)

<br>


 ### Element testing

 All elements of the website were then manually tested to ensure they were working as expected, and expected customer journeys through the site with customer interaction points were also tested. These are detailed in the following tables.

 #### Navigation Bar

| Page/Element | Expected Outcome | Pass/Fail |
|---|---|---|
| Site Logo | Clicking site logo returns user to homepage | Pass|
| All products link | Clicking link shows product dropdown | Pass |
| Categories link | Clicking link shows categories dropdown | Pass |
| Blog link | Clicking link redirects to blog page | Pass |
| My Account link - User logged out | Clicking link shows account register and login | Pass |
| My Account link - User logged in | Clicking link profile and log out links | Pass |
| My Account link - SuperUser logged in | Clicking link add product, add blog, profile and logout links | Pass |
| Shopping Bag link | Clicking link redirects to shopping bag | Pass |
| Mobile Nav Bar | Mobile nav appears on screens below 992px wide | Pass |
| Mobile Nav Bar Toggle | Clicking link opens navigation dropdown | Pass |
| Mobile Nav Bar Search Icon | Clicking link opens search dropdown | Pass |
| Back to top arrow | Clicking returns user to top of browser window | Pass |

<br>

[Back to element testing top](#element-testing)

<br>


#### Footer

| Page/Element | Expected Outcome | Pass/Fail |
|---|---|---|
| Contact Us Links - Social Sites | Clicking links opens each site in new window  | Pass|
| Contact Us Links - Telephone | Clicking link opens dialling window (mobile) | Pass |
| Contact Us Links - Email | Clicking link opens mail editor window | Pass|
| Quick Links - Internal site links | Clicking link opens site page in original window | Pass|
| Quick Links - My profile link | Clicking link directs user to sign up/in page if not logged in | Pass |
| Privacy Policy | Clicking link opens privacy policy in new window | Pass |
| Newsletter | Entering email and submitting returns confirmation message dependant on user state (new email, duplicate email) | Pass |
| Newsletter Unsubscribe link | Clicking link opens Unsubscribe field in new window | Pass |

<br>

[Back to element testing top](#element-testing)

<br>

#### Home page

| Page/Element | Expected Outcome | Pass/Fail |
|---|---|---|
| Carousel | Images scroll as expected, navigation arrows cycle through images | Pass |
| Shop Now Button | Clicking link opens Products page | Pass |
| Blog Posts Heading | Clicking link opens Blog page | Pass |
| Blog Image | Clicking link opens respective Blog page article | Pass |
| Blog 'Read More' link | Clicking link opens respective Blog page article | Pass |

<br>

[Back to element testing top](#element-testing)

<br>

#### Products page

| Page/Element | Expected Outcome | Pass/Fail |
|---|---|---|
| List filter | Products return correct items only dependant on filter option selected | Pass |
| Product count | Counter shows correct number of items on screen at time dependant on filter selected | Pass |
| Product card image | Clicking image opends individual product page | Pass |
| Product card category | Clicking category filters products shown as per category selected | Pass |
| Edit Link (superuser only) | Edit link only appears for superuser and when pressed edit product page opens and confirmation message given | Pass |
| Delete Link (superuser only) | Delete link only appears for superuser and when pressed product is deleted and user given confirmation message | Pass |

<br>

[Back to element testing top](#element-testing)

<br>

#### Individual Product page

| Page/Element | Expected Outcome | Pass/Fail |
|---|---|---|
| Product Image | Clicking image opens image in a new tab | Pass |
| Quantity Selectors | Up and down buttons change quantity amount | Pass |
| Quantity Selectors minus disabled | Down buttons unhighlighted when selction at 1 | Fail |
| Edit Link (superuser only) | Edit link only appears for superuser and when pressed edit product page opens and confirmation message given | Pass |
| Delete Link (superuser only) | Delete link only appears for superuser and when pressed product is deleted and user given confirmation message | Pass |
| Keep Shopping Button | Clicking button returns user to main products page | Pass |
| Add to bag Button | Clicking button adds item to bag, confirmation popup of shopping bag appears | Pass |
| Add to bag button on quantity update | Clicking button adds adjust item count to bag, confirmation popup of shopping bag appears | Pass |

<br>

[Back to element testing top](#element-testing)

<br>

#### Product Management (Superuser Only)

| Page/Element | Expected Outcome | Pass/Fail |
|---|---|---|
| Add Product link in navigation | Clicking link opens add product page | Pass |
| Cancel button | Clicking link returns user to products page | Pass |
| Add product button | Clicking link adds product to store. User returned confirmation message, product appears in main product page | Pass |
| Edit Product link on product cards | Clicking link opens edit product page with exsiting details prepopulated, confirmation message appears | Pass |
| Cancel button | Clicking link returns user to products page | Pass |
| Update product button | Clicking link adds product to store. User returned confirmation message, new product details appears in main product page | Pass |

<br>

[Back to element testing top](#element-testing)

<br>

#### Main Blog Page

| Page/Element | Expected Outcome | Pass/Fail |
|---|---|---|
| Blog card image | Clicking image opens individual blog page | Pass |
| Blog Read more link | Clicking image opens individual blog page | Pass |
| Add Blog Post Button (superuser only) | Button only appears for superuser and when pressed add blog page opens and confirmation message given | Pass |
| Edit Link (superuser only) | Edit link only appears for superuser and when pressed edit blog page opens and confirmation message given | Pass |
| Delete Link (superuser only) | Delete link only appears for superuser and when pressed blog post is deleted and user given confirmation message | Pass |

<br>

[Back to element testing top](#element-testing)

<br>

#### Individual Blog page

| Page/Element | Expected Outcome | Pass/Fail |
|---|---|---|
| Blog Image | Clicking image opens image in a new tab | Pass |
| Edit Link (superuser only) | Edit link only appears for superuser and when pressed edit blog page opens and confirmation message given | Pass |
| Delete Link (superuser only) | Delete link only appears for superuser and when pressed blog post is deleted and user given confirmation message | Pass |
| Comment Box | Comment box only appears if signed in, otherwise user prompted to log in or sign up to comment | Pass |
| Submit Button | Clicking button adds comment to blog post, confirmation popup appears | Pass |
| Delete Comment (comment author only) | Delete comment only appears if user is original commenter | Pass |
| Delete Comment (comment author only) | When pressed, comment is deleted and confirmation message appears | Pass |

<br>

[Back to element testing top](#element-testing)

<br>

#### Blog Management (Superuser Only)

| Page/Element | Expected Outcome | Pass/Fail |
|---|---|---|
| Add Blog link in navigation | Clicking link opens add blog page | Pass |
| Cancel button | Clicking link returns user to blog page | Pass |
| Add Post button | Clicking link adds blog to website. User returned confirmation message, blog appears in latest blog posts on homepage, and on main blog page | Pass |
| Price field | Warning message appears if incorrect figure format entered | Pass |
| Edit Post link | Clicking link opens edit post page with exsiting details prepopulated, confirmation message appears | Pass |
| Cancel button | Clicking link returns user to blog post page | Pass |
| Edit post button | Clicking link adds updated blog post product to website. User returned confirmation message, new blog details appears in main blog page and homepage if recent blog post | Pass |

<br>

[Back to element testing top](#element-testing)

<br>

#### Shopping Bag

| Page/Element | Expected Outcome | Pass/Fail |
|---|---|---|
| Bag Icon link (bag empty) | Clicking link opens bag with 'bag empty' warning message | Pass |
| Bag Icon link (items in bag) | Clicking link opens bag with correct items selected shown | Pass |
| Quantity selector | Clicking icons adjust quantity to desired number | Pass |
| Quantity selector down arrow | Arrow is muted when quantity is one | Fail |
| Quantity selector update link | Clicking link adjusts quantity in bag, warning message received | Pass |
| Quantity selector remove link | Clicking link removes item from bag | Pass |
| Keep shopping button | Clicking link returns user to main products page | Pass |
| Secure Checkout button | Clicking link brings user to checkout page | Pass |

<br>

[Back to element testing top](#element-testing)

<br>

#### Checkout Page

| Page/Element | Expected Outcome | Pass/Fail |
|---|---|---|
| Order Summary | Correct summary of items selected for purchase rendered on screen | Pass |
| Stripe field | Charge amount matches amount in order summary | Pass |
| User not logged in| User returned prompt to sign in or create account | Pass |
| User logged in| User returned check box to save delivery information if wanted | Pass |
| Adjust Bag button | Clicking link returns user to main shopping bag page | Pass |
| Complete Order button | Clicking link starts loading overlay, order summary page appears and success message | Pass |

<br>

[Back to element testing top](#element-testing)

<br>

#### Checkout Success Page

| Page/Element | Expected Outcome | Pass/Fail |
|---|---|---|
| Order Summary | Correct summary of items selected for purchase rendered on screen | Pass |
| Order Summary Success message | Correct summary of items selected for purchase rendered on screen | Pass 
| Blog button | Clicking link directs user to main blog page | Pass |

<br>

[Back to element testing top](#element-testing)

<br>

#### Custom 404 page

| Page/Element | Expected Outcome | Pass/Fail |
|---|---|---|
| Entering incorrect URL| Custom 404 page rendered | Pass |
| Return Home button | Clicking link directs user to main home page | Pass |

<br>

[Back to element testing top](#element-testing)

<br>

## Customer purchase testing

To test customer purchases, three scenarios were tested using the testing card details from the Stripe documentation.

For each test, a purchase of the same three items was made. Test one was a check to ensure a not logged in user could make a purchase. Test two was to check a logged in user could make a purchase, and test three was to check that a order was still submitted via a webhook if the browser closed during the submit process.

### User not logged in

This test would be deemed a success if the order was received in the database, but did not have a user profile attached to it, meaning it was made by someone not in the user database.

![Not logged in result](testing/images/not-logged-in.JPG)

The order was processed with no user profile attached, the test was deemed a success.

### User Logged in

This test would be deemed a success if this time a user profile was attached to the order. This could also be tested by the profile page, ensuring that the order history appears on this page as well.

![Logged in result](testing/images/logged-in.JPG)

![Order History](testing/images/order-history.JPG)

The order was processed and attached to the correct profile, and the order history page returned the correct details. This test was deemed a success.

### Browser crash during order

For this test, the aim was to simulate a browser crash, or power cut or similar as the user has just hit the submit button. During the submit overlay, the broswer will be closed on purpose to simulate this event.

This check is to ensure that the order was still processed. This would be measured successfull if the stripe webhook handler returned a Created Order message. This would be the same for both logged in and logged out users.

![Webhook result](testing/images/webhook.JPG)

![Order Confirmed](testing/images/order.JPG)

The test was deemed passed. As per the screenshots, the order was succesfully created in the database, and stripe confirms this with the Order created webhook message response.


<br>

[Back to top](#table-of-contents)

<br>

