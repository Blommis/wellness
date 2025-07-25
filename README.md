# Wellness Website
Visit the live version of the project here:  
[**Wellness Website**](https://wellness-website-7aba5e2a6dc3.herokuapp.com/)
![Mock up](readme_images/Images/mockup-image.png)

# Table of Contents

- [Wellness Website](#wellness-website)
- [Live Version](#live-version)
- [Description](#description)
- [UX](#ux)
  - [Design goals](#design-goals)
  - [Project goals](#project-goals)
  - [User Goals](#user-goals)
  - [User Stories](#user-stories)
    - [Must haves](#must-haves)
    - [Should have](#should-have)
    - [Could have](#could-have)
- [Wireframes](#wireframes)
- [Design Choices](#design-choices)
  - [Colors](#colors)
  - [Font](#font)
- [Relationship Diagram](#relationship-diagram)
- [Features](#features)
- [Future Features Implements](#future-features-implements)
- [Technologies Used](#technologies-used)
  - [Frontend](#frontend)
  - [Backend](#backend)
- [Bugs Discovered](#bugs-discovered)
  - [Bugs Fixed](#bugs-fixed)
- [Testing](#testing)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [JavaScript Validation](#javascript-validation)
  - [Python Validation](#python-validation)
  - [Lighthouse Testing](#lighthouse-testing)
  - [User Stories Testing](#user-stories-testing)
    - [Order Products & Display Order History](#user-story-order-products--display-order-history)
    - [Review and Rate Services](#user-story-review-and-rate-services)
    - [Register Account](#user-story-register-account)
    - [First Time Exploring Website](#user-story-first-time-exploring-website)
    - [Show Upcoming Events](#user-story-show-upcoming-events)
    - [Search Function](#user-story-search-function)
  - [Web Browser Testing](#web-browser-testing)
  - [Buttons & Links Testing](#buttons--links-testing)
  - [Responsiveness Testing](#responsiveness-testing)
  - [Family Testing](#family-testing)
  - [Stripe Testing](#stripe-testing)
- [Deployment](#deployment)
- [Credits](#credits)




# Description
Wellness is a digital platform designed to make health and well-being simple and accessible for everyone. Through intuitive navigation, clear information, and personalized recommendations, the platform offers a seamless experience where users can explore, purchase, and apply health solutions without unnecessary complexity.
# UX
The user experience for the **Wellness** project was designed to provide an inviting, supportive and efficient environment for anyone looking to improve their health and nutrition. Focus areas include clarity, responsiveness and seamless interaction at every step.

## Design goals
- **Clarity & Simplicity**  
  Presents information in a clean layout; make it easy to find supplements, meal plans and recipes.  
- **Responsive Layout**  
  Ensure the site looks and works great on desktop, tablet and mobile.  
- **Guidance & Encouragement**  
  Highlight top-rated products, popular recipes and upcoming wellness events to keep users motivated.  
- **Smooth Checkout**  
  Provide a guest-checkout option and an account-based flow so users can purchase with minimal friction.

## Project goals
The Wellness platform aims to be the go-to online destination for anyone seeking to explore, purchase, and apply health solutions—without unnecessary complexity. Our primary objectives include:

- Intuitive navigation – A user-friendly website that ensures seamless browsing and a hassle-free purchasing experience.
- Accessibility for all – The platform must be inclusive, catering to users with diverse needs and abilities.
- Personalized wellness experience – Wellness solutions should align with individual users' needs, offering tailored recommendations and relevant insights.


## User Goals
Wellness serves three main audiences—new visitors, returning members and health-conscious explorers—and meets their core needs.

### What Users Want
- **Convenience**  
  Quick access to place orders (with or without signing up) and receive confirmations.  
- **Inspiration**  
  Fresh, healthy recipes and meal plans that are easy to find and follow.  
- **Trust & Security**  
  Clear pricing, secure checkout and privacy of personal data.  
- **Community & Engagement**  
  A calendar of upcoming events and the ability to track past orders and progress.

## User stories
### User roles
1. New user – someone who hasn’t used the site yet and wants to explore.
2. Returning user – someone who has an account and uses the platform regularly.
3. Health-conscious visitor – someone passionate about health, looking for recipes or plans, but might not be registered yet.

### **Must haves**
### Order products

As a **user (whether I’m new, returning, or just health-conscious)** I can **order Wellness services ( supplement & meal plans)** so that **I can gain quick access to tailored health solutions, with or without creating an account**

#### Acceptance criteria
- I can browse and add any Wellness service to my cart without logging in
- If I check out as a guest, I provide only essential information (name, email, payment) and still receive an order confirmation
- If I check out logged in, my order is saved under my profile and appears in my order history
- I receive a confirmation (on-screen and via email) regardless of checkout method


### Review and rate services

As a **returning user** I can **leave a review on Wellness services** so that **others can benefit from my experience**

#### Acceptance criteria
- I can select a rating (1–5)/star rating
- I can write a short comment
- The review appears under the correct service


### View order history
As a **returning user** I can **see my order history** so that **I can keep track of my previous purchases and reorder easily**

#### Acceptance criteria
- I can access an "Order History" page from my account/dashboard
- I can see a list of all past orders with date, items, and total


### Register account
As a **new user** I can **register an account** so that **leave reviews**

#### Acceptance criteria
- A registration form is available
- Form includes validation (e.g., email format, password strength)
- I receive confirmation after successful registration

### First time exploring website 
As a **new user** I can **browse wellness services without logging in** so that **I can explore the platform before creating an account**

#### Acceptance criteria
- I can view the websites services without need to log in
- I can open a recipe, nutritions or meal plan and read full details
- I’m not asked to log in to view content


### **Should have**
### Show upcoming events 
As a **visitor or user of the platform** I can **view upcoming events** so that **I can stay informed and decide if I want to attend or get involved**

#### Acceptance criteria
- I can see a list of upcoming events without needing to log in
- Each event shows a title, date, time and short description
- Events are sorted by date, with the nearest event shown first

### **Could have**
### Search function
As a **health-conscious visitor** I can **search for recipes by ingredients or health goals** so that **I find relevant content.**

#### Acceptance criteria
- I can type a keyword in a search bar
- Results show recipes with matching ingredients or tags
- I get a message if no results are found


## Wireframes 

### Homepage 
![Homepage wireframe](readme_images/Images/homepageWF.png)
### Supplement page 
![supplement wireframe](readme_images/Images/supplementsWF.png)
### Mealplan page 
![mealplan page wireframe](readme_images/Images/mealplansWF.png)
### Recipe page 
![recipe page wireframe](readme_images/Images/recipespageWF.png)
### About page 
![Aboutpage wireframe](readme_images/Images/aboutpageWF.png)
### bag and checkout page
![bag and checkout wireframe](readme_images/Images/checkoutpageWF.png)
### Account
![account wireframe](readme_images/Images/accountpageWF.png)


## Design choices 
### Colors
The color choices are intended to balance clarity, usability, and aesthetics. A black font on a white background is planned to ensure high contrast and improve readability. Green is considered for buttons to indicate success and guide users toward key actions, while red may be used for price tags to quickly signal a discount or reduced price. A linear gradient — such as background: linear-gradient(135deg, #14d188, #01f737) — could be applied to the navbar and footer to add a modern and visually appealing element to the overall design.

![Colors choiced](readme_images/Images/colors.png)
![navbar and footer color](readme_images/Images/nav-footer-color.png)

### Font

For the typography, I choose the 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif stack for the body text. This font combination was chosen because it offers a clean, modern look while remaining highly readable across different devices and operating systems. It's a widely supported system font stack that ensures consistency and performance without requiring any external font loading.

![font family](readme_images/Images/font.png)


## Relationship diagram

This ER diagram represents the data structure for the **Wellness** project, a Django-based web application focused on health, nutrition, and e-commerce functionality. The goal of this diagram is to give a clear overview of the data models and how they interact.

---

### Core Tables and Descriptions

- **`auth_user`**  
  Django’s default user table for authenticated users.

- **`guest`**  
  Stores temporary guest data for users who order without an account.

- **`user_profile`**  
  Extends the user model to include saved shipping details and order history.

- **`order`**  
  Stores details about each purchase. An order can be linked to either a `user_profile` or a `guest`.

- **`order_line_item`**  
  Each item in an order. Uses Django’s `content_type` framework to support multiple product types (e.g., supplements, meal plans).

- **`supplement` / `meal_plan`**  
  Products that can be added to the shopping bag and ordered.

- **`recipe_breakfast`, `recipe_lunch`, `recipe_snack`**  
  Categories of recipes. Each has fields for description, ingredients, and instructions.

- **`review`**  
  Authenticated users can leave a rating and comment on a product or recipe using Django’s generic relation fields.

- **`content_type`**  
  Allows for generic linking between reviews or order items and their related product types.

- **`event`**  
  Lists upcoming wellness events visible to all users.

- **`gallery_image`**  
  Stores images shown in the gallery using Cloudinary.

---

### Key Relationships

- `user_profile` → `auth_user` (One-to-One)
- `order` → `user_profile` or `guest` (Optional)
- `order_line_item` → `order` (Many-to-One)
- `order_line_item` → `supplement` or `meal_plan` via `content_type`
- `review` → `auth_user` (Many-to-One)
- `review` → `recipe_*` (via `content_type`)
- Recipes are **reviewable**, but only by logged-in users.

---

### Logic Summary

- Guests can view all content and place orders.
- Logged-in users can:
  - Leave reviews on recipes.
  - Save shipping details and view past orders via `user_profile`.

---

### Notes & Conventions

- Decimal fields are written as `decimal(x, y)` for clarity.
- Text and `varchar(n)` fields follow Django model declarations.
- Cloudinary is used for storing image fields in `event` and `gallery_image`.

---

![diagram for database model relations](readme_images/Images/diagram-model-tool.png)

# Features 

The project includes several core features aimed at creating a smooth and engaging user experience.
![home page](readme_images/Images/homepage.png)

* Users can create an account and log in securely to access personalized features. 
* The site supports both registration and authentication.
![sign up page](readme_images/Images/sign-up-page.png)
![Sign in page](readme_images/Images/login-page.png)
![profile page](readme_images/Images/profilepage.png)


* Once logged in, they can leave reviews recipes, place orders for both supplements and meal plans, and receive a confirmation email after completing a purchase.  
![supplement page](readme_images/Images/supplement-page.png)
![mealplan page](readme_images/Images/mealplan-page.png)
![recipes page](readme_images/Images/recipe-page.png)
![reviews](readme_images/Images/review.png)
![checkout page](readme_images/Images/checkout.png)
![checkout success page](readme_images/Images/checkout_Success-page.png)
![email confirm](readme_images/Images/email-confirmation.png)


The layout is fully responsive across devices, and visual elements like green action buttons and red price highlights guide the user through the interface. A linear gradient is applied to the navbar and footer for a modern look, and the clean system font stack enhances readability throughout the site. 



## Future features implements 

* Update bag functionality: Allow users to adjust quantities or remove items directly in the shopping bag before checkout.

* Newsletter confirmation email, Send an automatic confirmation email when a user signs up for the newsletter (currently only a visual JS message is shown).

* Expanded site content: Add blog posts and more detailed company information to improve SEO and help the site rank better in search engines.

* Event sign-up system: Enable users to register for upcoming events (currently only show event dates and place is displayed).

* Create a combined services page:  
  Build a view and HTML template that displays all available services (Supplements, Meal Plans, and Recipes) in one place, making it easier for users to explore the full offering of the platform.

* Modular CSS and JavaScript structure:
  Currently, all pages share a single global `style.css` and `script.js`. In a larger or production-ready project, it is recommended to separate CSS and JS files per app or page—for example, dedicated files for `checkout`, `products`, and `recipes`. 


# Technologies used 
## Frontend 
* HTML5 – for semantic structure and clean markup
* Bootstrap - used for fast, responsive layout and pre-built UI components such as buttons, forms.
* CSS – styling and responsives devices
* JavaScript – used for interactivity such as dynamic messages and cart behavior, carousel, loading page for ordering 

## Backend 
* Python – core programming language
* Django – main web framework for building views, models, and templates
* Django Allauth – for user authentication and registration
* PostgreSQL – as the relational database management system
* Stripe API – for handling secure payments
* Cloudinary API – for image hosting and media management
* SMTP (Email Backend) – for sending order confirmation and (planned) newsletter emails

# Bugs discovered 
### Bugs fixed 
#### JavaScript error on pages without the carousel
During testing in the browser's DevTools console, " Uncaught TypeError: Cannot read properties of null (reading 'addEventListener')", I encountered the following error on pages that did not include the event carousel component:


This error occurred because the script attempted to attach `addEventListener` to `btnLeft`, an element that does not exist on pages without the carousel. As a result, `btnLeft` was `null` when the script ran, which caused the JavaScript to crash.'

##### Solution 
To resolve this issue, I added a conditional check to ensure that all necessary carousel elements (`track`, `btnLeft`, `btnRight`, and `slides`) are present before executing any functionality:

```javascript
if (track && btnLeft && btnRight && slides.length > 0) {
  // carousel logic runs safely here
}
```
This prevents the script from attempting to run on pages where the carousel does not exist, ensuring stability across all pages.


#### Duplicate orders created in the admin

While testing the checkout process, I discovered that **two different orders** were being created in the Django admin after a single purchase. This occurred because both the `checkout` view and the Stripe `webhook_handler` were independently creating an order. When the user submitted the checkout form, the `checkout` view created one order. Shortly after, the Stripe webhook fired a `payment_intent.succeeded` event, which triggered a second order to be created with the same data.

##### Solution 
- I **removed the order creation logic from the `checkout` view** entirely.
- Now, the **Stripe webhook** is solely responsible for creating the order after payment is successfully completed.
- To prevent race conditions (i.e., the webhook firing before the user is redirected to the `checkout_success` page), I added a **JavaScript-based delay** with a **loading overlay** that gives the webhook time to complete backend processing.

```html
<div id="loading-overlay" class="d-none">
    <div class="text-center">
        <div class="spinner-border text-primary" role="status" style="width: 4rem; height: 4rem;">
            <span class="visually-hidden">Loading...</span>
        </div>
        <p class="mt-3 fs-5 fw-semibold">Processing your order... Please wait.</p>
    </div>
</div>
```
```javascript
if (result.paymentIntent.status === "succeeded") {
    const overlay = document.getElementById("loading-overlay");
    if (overlay) overlay.classList.remove("d-none");
    setTimeout(function () {
        window.location.href = `/checkout/checkout_success/${result.paymentIntent.id}/`;
    }, 3000);
}
```
This ensures that the webhook has time to process the order before the success page is loaded, preventing duplicate entries and improving the reliability of the checkout flow.

# Testing 
## HTML validation 
All HTML files were validated using the [W3C Markup Validation Service](https://validator.w3.org/). During the process, three issues were identified:

* Index page (index.html): One of the < div > elements had duplicate class attributes. This is invalid HTML and was flagged as an error. The issue was resolved by changing the second on to a 'id' instead. 

* About Us page (about.html): The page included two < h1 > tags, which triggered a semantic warning. While not technically invalid, it is recommended to use only one < h1 > per page for better accessibility and SEO structure. The second < h1 > was changed to < h2 > to maintain proper heading hierarchy.

* Recipe page (recipe.html): An unclosed < div > tag caused a structural error in the document flow, leading to unexpected rendering. This was corrected by properly closing the tag.

After correcting these issues, all pages passed validation with no remaining errors or warnings.



![html validation error 1 ](readme_images/Images/html-val-error.png)
![html validation error 2 ](readme_images/Images/html-val-error2.png)
![html validation error 3 ](readme_images/Images/html-val-error3.png)
![html validation approved ](readme_images/Images/html-val-approved.png)


## CSS validation 
The CSS file (style.css) was tested using the [W3C CSS Validation Service (Jigsaw)](https://jigsaw.w3.org/css-validator/). During the validation, one error and one warning were detected:

* Error: A flex-start value was mistakenly used with the flex-direction property, which is invalid. The value was corrected to column, which is a valid direction keyword in flexbox layout.

* Warning: The use of the -webkit-transition property triggered a vendor-specific warning. Since it was not essential to the layout or animations, the entire CSS rule containing -webkit-transition was removed to improve code clarity.

After addressing these issues, the CSS file passed validation with no remaining errors or warnings.

![css validation error  ](readme_images/Images/css-val-error.png)
![css validation warning ](readme_images/Images/css-val-warning.png)
![css validation approved ](readme_images/Images/css-val-approved.png)

##  JavaScript Validation

The JavaScript used in this project is contained in a single file: `script.js`. To validate the code, I used [JSHint](https://jshint.com/). Initially, multiple warnings and errors were displayed during the validation process.

However, these were not actual syntax issues — they appeared because I had not declared the ECMAScript version or defined global variables used by external libraries. Once I added the following directives at the top of the file, all warnings disappeared:

```javascript
/* jshint esversion: 6 */
/* global Stripe */

```
## Python Validation

All Python files in the project were tested for PEP8 compliance using the [PEP8 CI Validator](https://pep8ci.herokuapp.com/). During the validation, I received several warnings, mainly related to:

- **Trailing whitespace** at the end of lines
- **Lines exceeding the recommended length** (more than 79 characters)

These were addressed by cleaning up unnecessary spaces and breaking up longer lines where appropriate to follow PEP8 style guidelines. After making the changes, all Python files passed the validation without any remaining issues.


## Lighthouse testing

All main pages of the site were tested using Lighthouse in Chrome DevTools. The results varied slightly between pages, but overall performance and accessibility were acceptable.

However, Lighthouse identified several areas for improvement:

- **Color contrast:** Some color combinations, especially red text on light backgrounds, did not meet accessibility standards. Adjusting the shades to provide better contrast would improve readability for users with visual impairments.
- **Image optimization:** Several images were flagged as being larger than necessary. Reducing image file sizes and using more efficient formats (such as WebP) could improve load speed and overall performance.
- **Form accessibility:** The quantity input field on product pages lacked an associated < label >, which is important for screen reader support. This has been addressed by adding a visually hidden label.

These insights have been noted and will be prioritized in future updates to improve user experience and accessibility across the site.


![lighthouse validation home](readme_images/Images/lighthouse-home.png)
![lighthouse validation recipe page](readme_images/Images/lighthouse-recipe.png)
![lighthouse validation account](readme_images/Images/lighthouse-account.png)
![lighthouse validation supplement detail](readme_images/Images/lighthouse-supp-detail.png)
![lighthouse validation mealplans](readme_images/Images/lighthousemealplans.png)
![lighthouse validation about](readme_images/Images/lighthouse-about.png)



## User stories testing 

### User Story: Order Products & display order history
As a **user (whether I’m new, returning, or just health-conscious)** I can **order Wellness services ( supplement & meal plans)** so that **I can gain quick access to tailored health solutions, with or without creating an account**

| **Feature**                              | **Action**                                                                                   | **Expected Result**                                                                                     | **Actual Result**                                                                                       |
|------------------------------------------|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| Order without logging in                 | Add supplement or meal plan to bag and proceed to checkout as a guest                        | Able to complete purchase with name, email, and payment only; confirmation is displayed and emailed     | Worked as expected – guest checkout completed successfully, with confirmation shown and emailed         |
| Order while logged in                    | Log in, place an order                                                                        | Order is linked to user profile and visible in order history                                             | Worked as expected – order appeared in user’s profile after successful payment                          |
| Confirmation on all methods              | Place order as both guest and logged-in user                                                  | Confirmation message on-screen and email confirmation sent in both cases                                | Confirmations were successfully shown on screen and emails were received in both scenarios              |
| Browse and add products freely           | View products and add to cart without logging in                                              | Able to browse site freely and add items to bag without account                                          | Fully functional – cart worked for both anonymous and logged-in users                                   |


![shopping bag page](readme_images/Images/shopping-bag.png)
![checkout page](readme_images/Images/checkout.png)
![checkout success page](readme_images/Images/checkout_Success-page.png)
![checkout success page](readme_images/Images/order-confirm.png)
![checkout success page inlogged](readme_images/Images/order-history.png)
![email confirm](readme_images/Images/email-confirmation.png)
![email confirm inlogged](readme_images/Images/email-confirm-email2.png)


### User Story: Review and Rate Services

| **Feature**                | **Action**                                                                 | **Expected Result**                                                            | **Actual Result**                                                            |
|----------------------------|----------------------------------------------------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Select a star rating       | Choose a rating between 1 and 5 for a supplement or meal plan              | Rating is saved and displayed alongside the review                             | Worked as expected – rating displayed correctly with stars                    |
| Write a short comment      | Enter a written comment in the review form                                | Comment is submitted and appears publicly under the selected recipe           | Worked as expected – comment visible under the correct recipe                |
| Review placement accuracy  | Submit a review on a specific recipe detail                                | Review is saved and shown under the correct recipe only                       | Fully functional – reviews were attached to the correct recipe               |


![Review page](readme_images/Images/recipe&review.png)
![ no review yet](readme_images/Images/noreviewsyet.png)
![ a review](readme_images/Images/review2.png)


### User Story: Register Account

| **Feature**                   | **Action**                                                      | **Expected Result**                                                               | **Actual Result**                                                               |
|-------------------------------|------------------------------------------------------------------|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| Registration form available   | Click "sign up" on login page to access the signup page            | Registration form is displayed with relevant input fields                         | Worked as expected – form loaded with required fields (username, email, password) |
| Form validation               | Enter invalid email or weak password                            | Validation messages are shown preventing submission until input is corrected      | Functioned correctly – validation errors were shown for incorrect inputs         |
| Registration confirmation     | Complete the form with valid credentials and submit             | Account is created and user receives a success message or redirect confirmation   | Registration completed successfully – confirmation was displayed on screen       |

if user is logged in
![ logged in icon](readme_images/Images/if-user-loggedIn-icon.png)

![ sign up page](readme_images/Images/sign-up-page.png)
![ a verification page ](readme_images/Images/email-verifaction-page.png)
![ confirm EMAIL page](readme_images/Images/confirm-email-page.png)
![ log in page](readme_images/Images/login-page.png)
![ invalid email](readme_images/Images/invalid-email.png)
![ invalid password](readme_images/Images/invalid-password.png)



### User Story: First Time Exploring Website

| **Feature**                          | **Action**                                                               | **Expected Result**                                                                      | **Actual Result**                                                                      |
|--------------------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| View services without logging in     | Navigate to homepage and browse supplements, meal plans, recipes and about     | All content is visible without requiring login                                            | Worked as expected – no login prompts while browsing                                    |
| Access detailed content              | Click on a recipe or nutrition info to view more details     | Full details are displayed (ingredients, descriptions, benefits, etc.)                   | Worked as expected – user could view all content pages without restriction              |
| No forced login prompts              | Continue browsing site as anonymous user                                 | User is never asked to log in unless trying to perform restricted actions (e.g. review)  | Correct behavior – browsing and reading content worked freely without login prompts     |

if user visiting as a guests, havent logged in yet or hasnt a account. this icon shows in navbar 

![ guest icon](readme_images/Images/guest-icon.png)
![ supplement page](readme_images/Images/supplement-page.png)
![ supplement  detail page](readme_images/Images/supplement-detail.png)
![ mealplan page](readme_images/Images/mealplan-page-as-guests.png)
![ recipe page](readme_images/Images/recipe-page-as-guest.png)
![ recipe detail page](readme_images/Images/recipe-detail-page.png)
![ about page](readme_images/Images/about-page-as-guest.png)


### User Story: Show Upcoming Events

| **Feature**                       | **Action**                                                         | **Expected Result**                                                                 | **Actual Result**                                                                  |
|-----------------------------------|---------------------------------------------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| View events without logging in    | Visit the events section as a visitor or user                      | Events are visible without login                                                     | Worked as expected – events were accessible to all users                            |
| Event details shown               | Look at an individual event listing                                | Each event displays a title, date, time, and short description                       | Fully functional – all key information was displayed for each event                 |
| Events sorted by date             | Visit the events section with multiple upcoming events             | Events appear in chronological order, with the nearest upcoming event listed first   | Functioned correctly – events sorted by date with closest one shown first           |

![ event ](readme_images/Images/event1.png)
![ event ](readme_images/Images/event2.png)
![ event ](readme_images/Images/event3.png)
![ event ](readme_images/Images/event4.png)


### User Story: Search Function

| **Feature**                     | **Action**                                                      | **Expected Result**                                                                       | **Actual Result**                                                                     |
|----------------------------------|------------------------------------------------------------------|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Enter keyword in search bar     | Type an ingredient or supplement into the search input         | Matching word are displayed based on title, ingredients, or relevant tags              | Worked as expected – relevant right supplement were shown based on search term                 |
| Results reflect query           | Search for specific ingredients (e.g. "avocado")                 | Only recipes that include or are tagged with "avocado" are shown                          | Fully functional – only relevant recipes were returned                                 |
| No results message              | Search with a random or misspelled keyword                      | A clear message is shown indicating that no matching results were found                   | Worked as expected – user was informed when no content matched the search             |


![ search for magnesium ](readme_images/Images/search-supplement.png)
![ search for avocado ](readme_images/Images/search-avocado.png)
![ search incorrect word ](readme_images/Images/search-invalid-word.png)



### Web Browser Testing

The website was manually tested on the following modern web browsers to ensure consistent layout, responsiveness, and functionality:

| **Browser**       | **Tested Version**     | **Result**                             |
|-------------------|------------------------|----------------------------------------|
| Google Chrome     | Latest (Windows/macOS) |  Fully functional, no issues found   |
| Safari            | Latest (macOS/iOS)     | All pages displayed as expected     |
| Microsoft Edge    | Latest (Windows)       |  Fully functional, consistent layout |

#### Test scope included:
- Responsive layout on desktop and mobile views
- Navigation bar and hamburgermenu functionality
- Carousel interaction 
- Form behavior (register, login, password reset)
- Stripe checkout flow and overlays
- Search, review, and order features
- Font rendering and color contrast

All tested browsers displayed the site correctly with no critical issues.

![ chrome browser ](readme_images/Images/googlechrome.png)
![ microsoft edge browser](readme_images/Images/microsoft-edge.png)
![ safari browser ](readme_images/Images/safaritesting.jpg)


### Buttons & Links Testing

All interactive buttons and links across the site were manually tested to ensure they are functional, responsive, and lead to the correct destinations.

| **Element**                    | **Page(s)**                         | **Expected Behavior**                                                                     | **Actual Result**                                                                 |
|-------------------------------|-------------------------------------|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| "Buy Now" buttons             | supplement and mealplan pages                | Adds item to bag and stays on page                                    |  Worked as expected                                                             |
| "More Details" buttons        | supplement detail page                    | Opens supplement detail page                                                  |  Redirects to correct supplement detail page                                       |
| Newsletter input & button     | Footer                              | User can enter email and get visual confirmation                                           |  Input accepts email, JS confirmation message displayed                         |
| "Proceed to Checkout"         | Shopping bag                        | Takes user to checkout form                                                                |  Redirected to `/checkout/`                                                     |
| Checkout form                 | `/checkout/`                        | Inputs are editable, and clicking "Place Order" redirects to success page                 |  Order submitted and redirected to `/checkout/checkout_success/`                |
| "Register" and "Login"        | Navbar (all pages)                  | Opens corresponding authentication forms                                                   |  Fully functional                                                               |
| "Logout"                      | profile page (when logged in)             | Logs out and redirects to homepage                                                         |  Session ended and redirected properly                                          |
| "Search" button               | Header/search bar                   | Submits query and displays relevant content                                                |  Results returned or error message shown if no matches                          |
| "View More" on search result  | Search results                      | Opens detailed product view for the matched keyword                                        |  Worked as expected – opened the correct product                                |
| Password reset flow           | Reset via email link                | Goes through reset, key, set, and done pages                                               |  All steps worked with expected feedback                                        |
| "Submit Review" button        | Recipe page              | Submits rating and comment and refreshes with updated review                              |  Review saved and shown immediately                                             |
| "Delete Review" button        | Recipe page              | Removes selected review                                                                    |  Review deleted and no longer displayed                                         |
| "Back to Home" / "Log in"     | Success pages (e.g. password reset) | Redirects to homepage or login page                                                        |  Navigation worked as expected                                                  |
| Footer buttons                | Footer (all pages)                  | Every link works except "Services" (no page exists yet)                                    |  All links functional; "Services" is not clickable by design                    |

All buttons and links were manually tested and worked as intended, with the exception of the non-clickable "Services" footer heading, which is intentionally inactive until the services overview page is created.

### Responsiveness Testing

The site was tested using Chrome DevTools to simulate different devices. Key components such as navigation, layout, buttons, forms, and readability were reviewed to ensure they worked across screen sizes.

| **Device**     | **Screen Type** | **Test Method**      | **Expected Result**                                       | **Actual Result**                                        |
|----------------|------------------|------------------------|------------------------------------------------------------|-----------------------------------------------------------|
| iPhone XR      | Mobile           | Chrome DevTools        | All content scales properly, menu is mobile-friendly       |  Mobile navigation collapsed correctly, layout was responsive |
| iPad Mini      | Tablet           | Chrome DevTools        | Content adjusts to medium screen, columns stack as needed  |  Worked as expected, content displayed clearly            |
| Desktop (1920px)| Desktop         | Chrome DevTools        | Full layout visible, no overflow, balanced white space     |  Layout remained consistent and clean                     |

All breakpoints and interactive elements responded well across tested devices.


### Family Testing

The site was tested by family members with varying levels of digital experience to evaluate usability, clarity, and accessibility. Each tester was given specific tasks to complete and provided feedback based on their experience.

| **Tester**         | **Device Used**   | **Tasks Assigned**                                               | **Expected Result**                                           | **Actual Result**                                               |
|--------------------|-------------------|------------------------------------------------------------------|----------------------------------------------------------------|------------------------------------------------------------------|
| Parent (age 60+)   | iPad Mini         | Navigate site, search for a recipe, and read it                  | Easily access recipe with clear layout and readable text       |  Completed task, found layout easy to understand               |
| Sibling (age 30)   | iPhone XR         | Add a supplement to cart and complete guest checkout             | Smooth mobile experience and clear checkout steps              |  Checkout worked, only feedback was to improve field spacing   |
| Teenager (age 22)  | Laptop (Windows)  | Create account and leave a review on a meal plan                 | Form validation, confirmation message, and review display      |  Account created and review posted successfully                |

Family feedback confirmed that the site was user-friendly across ages and devices, and helped identify a improvement for the future, a updated bag function in shopping bag.



### Stripe Testing

The Stripe integration was tested in test mode using Stripe's provided test cards. Key parts of the checkout process, including payment intent creation, redirection, and webhook handling, were verified to ensure orders were processed correctly.

| **Test Scenario**                       | **Action Performed**                                                             | **Expected Result**                                                   | **Actual Result**                                                   |
|----------------------------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------|
| Valid card payment (4242 4242...)      | Completed checkout with Stripe's standard test card                              | Payment succeeds, user redirected to success page                     |  Payment succeeded, redirected to `/checkout/checkout_success/`   |
| Webhook order creation                 | Waited for backend webhook after payment                                         | Order is created via webhook, email confirmation is sent              |  Order created by webhook only, confirmation email triggered       |
| Incorrect card number                  | Tried to pay with invalid test card                         | Stripe returns error, payment fails                                   |  Error message displayed, no order created                         |
| Delayed redirect test                  | Observed 3-second overlay after payment before reaching success page             | Loading spinner shows before redirect                                 |  Overlay displayed, redirect happens smoothly after delay          |
| No double order creation               | Completed order and checked admin for duplicates                                 | Only one order should exist                                            |  Confirmed only one order created in admin                         |

Stripe testing confirmed that payment flow, error handling, and backend logic (including webhook usage) function as intended in test mode.


![ checkout page](readme_images/Images/stripecheckout.png)
![ process loading order](readme_images/Images/processen-order.png)
![ order confirm](readme_images/Images/stripe-order-confirm.png)
![ order in admin](readme_images/Images/admin-confirm.png)
![ webhooks page](readme_images/Images/webhooks.png)
![ email confirm order](readme_images/Images/stripe-email-confirm.png)
![ invalid card number](readme_images/Images/invalid-card-number.png)
![ invalid card year](readme_images/Images/invalid-card-year.png)


# Deployment

This project was deployed using [Heroku](https://heroku.com) with automatic deployment from GitHub.

## Prerequisites
Before deployment, ensure your project includes the following:

- **Heroku account** – [Sign up for free](https://signup.heroku.com)
- `Procfile` – Specifies how to run the app on Heroku
- `requirements.txt` – Lists all Python dependencies
- `runtime.txt` – Specifies Python version (e.g. `python-3.12.1`)
- `.gitignore` – Excludes unnecessary files from being pushed
- `settings.py` – Includes your Django configuration (instead of `config.py`)

##  Step-by-Step Deployment Instructions

### 1. Create a Heroku App
- Log in to your Heroku Dashboard
- Click **New** → **Create new app**
- Choose a unique app name and region (Europe or United States)
- Click **Create app**

### 2. Connect to GitHub
- In the app dashboard, go to the **Deploy** tab
- Under **Deployment method**, select **GitHub**
- Connect your GitHub account and search for your repository
- Click **Connect**

### 3. Set Environment Variables
- Go to the **Settings** tab
- Click **Reveal Config Vars**
- Add necessary variables, such as:
  - `SECRET_KEY`
  - `DATABASE_URL`
  - `DISABLE_COLLECTSTATIC`
  - `STRIPE_PUBLIC_KEY`, `STRIPE_SECRET_KEY`, etc.

#### 4. Deployment
- In the **Deploy** tab, choose either:
  - **Manual deploy** (select branch and click *Deploy Branch*)
  - **Automatic deploys** (deploy on every push to `main`)

Heroku will build and deploy the app. Once complete, click **Open App** to view your live site.


# Credits

The following resources, tools, and references were used during the development of this project:

---

## Content & Media
-  **[Canva](https://www.canva.com/)** – Used to create mockup for the website by using frame from canva 
- **[Canva AI](https://www.canva.com/ai)** – Used to generate AI-based images, particularly for supplement product visuals.
- **[Unsplash](https://unsplash.com/)** – Source of high-quality stock images used throughout the website.
- **[FreeConvert](https://www.freeconvert.com/jpg-to-webp)** – Used to convert image files to `.webp` format for improved web performance.

---

## Stripe Integration

- **Boutique Ado Project** – Provided helpful reference code and logic for implementing Stripe Elements, setting up the payment flow, and handling webhooks in Django.

---

## Tools for Testing & Development

- **[Temp Mail](https://temp-mail.org/)** – Used to create temporary email addresses when testing registration, password reset, and confirmation flows.
- **Chrome DevTools** – Used for responsive testing and debugging on multiple screen sizes and devices.


---

## Database Diagram

- **[dbdiagram.io](https://dbdiagram.io/)** – Used to visually plan, structure, and document the Entity Relationship Diagram (ERD) for the Django project. It helped clarify how models like `Order`, `UserProfile`, and `Review` interact, including support for generic relations through Django’s content type framework.

---

Thank you to all the creators and services that made this project possible.


