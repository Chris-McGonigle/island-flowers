# Testing for the website 'Island Flowers by Sarah'

The following document outlines all testing carried out on the website 'Island Flowers by Sarah'

During the construction process, the Dev Tools functionality of Chrome was used to test CSS code initially, where it was then tweaked to the desired outcome.

## Table of Contents

 1. [Validator testing](#validator-testing)
    * [HTML](#html)
    * [CSS](#css)
    * [Lighthouse](#lighthouse)
    * [Javascript](#javascript)
    * [Pep8](#pep8)
2. [Manual testing](#manual-testing)
    * [Responsive testing](#responsive-testing)
    * [Element testing](#element-testing)



## Validator testing

To view testing images please click on each individual hyperlink. These files can also be found in the [testing images](/testing/images) folder.

### HTML

All HTML pages were passed through for testing via [W3C](https://validator.w3.org/) and the results are as follows:

1. [Home page](/testing/images/home.png)

A total of 22 errors and warnings were received on the first pass through the W3C validator. 

The <li> tag as child of a nav element errors were ignored as this was the same process as used in the project walkthrough videos.

The duplicate id 'user-options' warning was ignored as the validator is picking up the mobile and desktop versions of the nav bar account dropdowns.

The javascript type warnings were also ignored, again as the code matches that as shown by the instructor videos.

All other errors listed were addressed and on retest only the previously ignored warnings remain.

2. [Products](/testing/images/products.png), [Blog](/testing/images/blog.png) and [Checkout Pages](/testing/images/checkout.png)

Tests on all three pages returned the same errors that were ignored in the previous testing of the homepage. No other errors were returned so these pages were left as is.

3. [Bag](/testing/images/bag-errors.jpg)

Running the bag app through the validator returned two errors. one was an unclosed outer div element which was added.

The body tag error seemed to be rendered by the base.html template. Code was checked against the wlakthrough project and seen to be the same so this error was ignored.

<br>

[Back to top](#table-of-contents)

<br>

### CSS

The CSS was tested using [Jigsaw](https://jigsaw.w3.org/css-validator/).


<br>

[Back to top](#table-of-contents)

<br>

### Lighthouse

The site was tested for accessibility, performance and best practise using Google's [Lighthouse](https://developers.google.com/web/tools/lighthouse) tool. The results were as follows:



<br>

[Back to top](#table-of-contents)

<br>

### Javascript


<br>

[Back to top](#table-of-contents)

<br>

### Pep8


<br>

[Back to top](#table-of-contents)

<br>

## Manual testing

 #### Responsive testing

 The site was tested extensively using the dev tools facilties of Chrome, Safari and Firefox. It was tested against most popular makes of phones and tablets. 

 It was found to be responsive across all tested platforms.


<br>

[Back to top](#table-of-contents)

<br>


 #### Element testing

 All elements were tested for functionailty and were found to have passed as expected. The below screeshot details the tests carried out and is also available as an [excel spreadsheet](/testing/manual-testing.xlsx).

 ![Manual Testing Results](/testing/images/manual-testing.jpg)


<br>

[Back to top](#table-of-contents)

<br>

