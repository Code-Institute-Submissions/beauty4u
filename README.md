<h1 align="center">
Milestone Project 4 - Beauty4U - David O Neill
</h1>
<h2 align="center"><a href="https://beauty4u.herokuapp.com/">Visit Beauty4U</a></h2>
<h4> About Beauty4U </h4>

Beauty4U is a website designed for a hair and beauty salon. It offers the salon a visually appealing ecommerce site while also allowing them to offer online booking to their customers. The salon can manage multiple aspects of their business from one single location.

## Contents

1. [**User-Stories**](#User-Stories)
2. [**Features-Implemented**](#Features-Implemented)
3. [**Technologies-Used**](#Technologies Used)
4. [**App-Breakdown**](#App-Breakdown)
5. [**Testing**](#Testing)
6. [**Deployment**](#deployment)


## User-Stories

After working closely with salons for some time developing websites and offering online booking solutions,  the needs of a salon and their customers became very clear. Beauty4U is designed to meet said needs. First, let’s define broadly what those needs are from both the salon owner’s perspective and the salon customer.

### Salon Owner
- Have a visually appealing website that can be used to attract new customers online through various marketing channels 
- Sell hair and beauty products online to their customers 
- Offer online booking to their customers while keeping the control 
- Stay in touch with current customers to keep them informed about offers, new services etc 
- Keep track of website performance 

### Salon Customer
- Shop online for hair and beauty products in a modern ecommerce environment 
- Make bookings online 
- Get in touch with the salon 

These are the broad goals from both perspectives. The development of Beauty4U was entirely driven by these clearly defined goals. Each of these goals will be described in more detail below along with how each goal was achieved 

### A Visually Appealing and Easy to Use Website 
The salon industry, as one can imagine,  is a very visual one. While also being visual, it is not notoriously known for being a technical one. Customers vary widely in age. Therefore, in order to attract customers and impress potential clients, a salon must have a visually appealing website that is simple and easy to use. Beauty4U was designed with this in mind. Colour Schemes are bright and contrasting for ease of use. Navigation menus are short and simple with descriptive ‘call to actions’. Shop menus are broken down into intuitive sections such as ‘Brands’ or ‘Categories’. User feedback is provided throughout to give both the salon owner and the customer the confidence and safety to use all features comfortably. 

### (The Customer) Shop online for hair and beauty products in a modern ecommerce environment

Customers are used to seamless shopping experiences and have a set expectation when shopping online. These expectations must be met in order for the salon to have a successful ecommerce site. Beauty4U is built with these in mind. Products are laid out cleanly and prices easily visible. The user can easily search for products or navigate menus to find what they are looking for. Users can read and add reviews for each product. Users can create accounts and keep a record of their orders. They can add/remove items to/from a user friendly shopping cart. They can checkout in a secure environment with all checkout information easily available to them (shipping costs, shipping methods). 

### (The Salon Owner) Sell hair and beauty products online to their customers

In order to run a successful ecommerce website, the salon owner requires a number of things. Firstly, the shop must be easily managed.  Salon owners can find clunky CMS’s like Woocommerce intimidating and difficult to use. Beauty4U provides the salon with an easy to use management dashboard where they can perform key shop management duties. They can add/remove products, make updates to existing products, add/remove product categories & brands, upload/change product images, put products on sale, and manage product stock. 

Offering customers incentives to buy online is key to running a successful ecommerce website. Within the beauty4U management dashboard, shop owners can easily create  coupon discount codes that they can offer to customers. They can send out marketing emails to all their customers informing them of discount offers for the online shop.

Salon owners can also set a free shipping offer from within their dashboard and choose whether or not to activate it. They can set the threshold for free shipping.

Salons can also choose whether or not to offer a ‘Click & Collect’ service with the simple toggle of a button.

### (The Salon Owner) Keep track of website performance 

It’s important for the salon owner to know how well their website and ecommerce shop are performing so they can make adjustments accordingly. The Beauty4U management dashboard offers the owner insights into unique website visitors and advises them when website traffic has reduced. They can view their shop earnings and number of products they have sold. 

### (The Customer) Make bookings online 

Online booking has become very popular in recent times. When a customer visits a salon website, they expect to be able to book services online. Beauty4U offers the customer the ability to select services for booking, select dates,times, and staff members and request a booking. They will then receive an email from the salon once their booking has been confirmed. 

### (The Salon Owner) Offer online booking 

Online booking is a must for any salon. Customers expect to be able to make bookings online. However, most salons still want to keep control over their books! Customers often don’t know how long a service might take, what staff member is best fit etc.. Beauty4U offers the salon an online booking system that keeps the control with the salon. Customers request a booking online and the salon receives an email with the booking details. They can check the details and see if the request is possible.  They can enter their management dashboard and from there and confirm the booking with one click. Once a booking is confirmed, the customer will receive an email to say their booking has been confirmed. If the booking is not suitable, the salon owner can contact the customer using the details provided in their management dashboard.   

Salon owners can also input their opening hours in the dashboard which will map to their booking system. If they are closed on Mondays, they can mark Monday closed and customers will not be able to request bookings for that day. Opening hours are also displayed in the footer of the website. 


### (The Salon Owner ) Stay in touch with current customers to keep them informed about offers, new services etc 

Salon Owners can send marketing emails to all their registered customers directly from their management dashboard; making it easy to keep customers informed about the latest news and offers 

### (The Customer ) Get in touch with the salon

Beauty4U offers an easy to use contact us form so that customers can easily get in touch with the salon 

## Features-Implemented  

### Public Website 
- Home page with dynamic opening hours and free shipping banner 
- User registration and login 
- Online Shop with dynamically generated menus, pop out cart, shipping options, coupons and sale prices 
- Profile with history of orders, online bookings 
- Booking system with staff, date/time, and services selection 
- Contact Us form 
- Custom 404 page 

### Management Dashboard Features 
- Overview of website stats 
- Capturing of unique website visits and chart displayed 
- Send marketing email to customers 
- Manage products, brands, and categories  in shop 
- Create and manage coupons 
- Create free shipping threshold and display banner 
- Activate click and collect option for shop 
- View online orders and shipping details 
- Manage booking system staff, services, and opening hours
- Confirm online bookings and get alerted of unconfirmed bookings 


## Wireframes 

Wireframes are available <a href="https://github.com/davidosongschool/beauty4u/tree/master/wireframes">here</a>


## Technologies Used

### Languages Used
- HTML5, CSS3, PYTHON, JAVASCRIPT 

### Framework / Libraries Used
- Django 3 - Main python framework used
- Django AllAuth - Django package used for user account management 
- Django Crispy Forms - Used to render Django forms with bootstrap styling
- Django Countries - Used for county form field in checkout 
- Stripe - Used to process online payments 
- Bootstrap 4 - CSS & JS library used to styling 
- JQuery - JS Library used for AJAX and user interaction
- JQuery UI - Used for mobile menu animation 
- Chart.js - Used to render website stat chat in dashboard 
- Font Awesome - Icons  
- Google Fonts - Typography
- NGrok - For a local url when testing stripe webhooks before deployment  
- Github - Version control
- VSCode - Code Editor 
- Venv - Virtual Environment on local machine 
- Heroku - Used to host the app 
- Beautify (VSCode Extension) - Used for HTML, CSS, Javascript styling 
- HTMLHint (VSCode Extension) - Used to validate HTML &  CSS 
- Flake8 - Python linting 


## App Breakdown

This section will provide a technical breakdown of each app - highlighting any notable approaches taken

### HOME
Home app is made up of a small number of views. It contains the Opening Hours model which stores the salons opening hours. It also handles the contact us page and email templates for contact email


### PRODUCTS
The products app handles the display of the shop front, category, brands and results.It handles the individual product displays and product reviews. It contains the models for products, categories, brands, and reviews.  It has a context processor which returns all the brands and categories to each page to be displayed in the menu. 

It also handles AJAX requests from product.js to add reviews to the website in a seamless manner without the need for a page refresh 


### CART
This app handles the display of the pop out cart. Notably, it takes AJAX requests from cart.js which allows for seamless adding and removal of products to the cart. 
It also has a context processor which returns the contents of the cart to be used on every page.

The cart app also handles changes in shipping methods selected. Each time the shipping method is changed, the stripe payment intent, created at checkout, is modified to reflect the new cost of the order


### CHECKOUT
This app handles the shop checkout. It contains the Order models which stores all orders with a unique order number. It contains the webhook handler which takes AJAX requests from stripe.js and creates stripe payment intents 

It also handles coupons being applied at checkout 

### PROFILE
This app handles the display of users order history and booking history - It returns all booking and orders made by the user that is logged in 

### MANAGEMENT
This app handles the display of the management dashboard and the associated data processing.

It takes AJAX requests from postsettings.js which allows for seamless database interaction without the need for page refreshes. For example, you can toggle a booking as ‘confirmed’ or toggle a site setting as ‘on/off’ without the need to refresh the page each time. 

It contains multiple Django forms that are used to manage products, categories, brands etc

The app also uses Chart.js to display website visits as a graph

## Testing

### General Site Tests
- All interactive elements were checked first. On Desktop, any hover effects/color changes were checked (social media links). On mobile, the same effects were checked when links were clicked.
- Every link on the page was checked to ensure that it directed the user to the correct page. Every button was clicked and checked that it directed the user to the correct page.
- Any links that activated modals were checked that they functioned correctly. 
- The site was then tested on multiple screen sizes and orientations (horizontal & vertical) using Chrome Developer Tools. All text was checked to make sure it was easily readable on any screen size. Item spacing was checked to make sure there was sufficient spacing between all elements on all screen sizes.

### User Testing
I tested the functionality of the site as a customer and site administrator.


#### Booking
- I attempted to access the booking app without being logged in and checked that a login was required 
- I logged in to my account and then tested that the booking system asked for a name and phone number before allowing the customer to use it 
- I tested that each service was selectable and that the total cost of the booking was adding and subtracting as expected 
- I then continued the booking and tested that i could select a staff member and continue - I tried to continue without selecting a staff member to check that it would not allow this action 
- I then repeated this over each stage of the booking process
- Throughout this, I was tested each view to ensure that it displayed correctly 


#### Shop
- I filtered products using the navigation menus and made sure the correct products were displayed 
- I searched for terms and checked that results were displayed as expected 
- I clicked into various products and checked that the information was displayed correctly 
- I checked that I was able to add a view for the product - I made sure that I wasn’t able to submit a review without selected a star rating and entering a review in the text box 
- I checked that my review saved correctly by refreshing the page 
- I added an item to my cart and made sure the cart popped out correctly and all information was displayed correctly 
- I removed the item and made sure my cart updated accordingly 
- I tried to access the checkout and made sure it was redirected when my cart was empty
- After adding items to my cart, I accessed the checkout and made sure all forms rendered correctly 
- I selected different shipping methods and made sure my total updated correctly 
- I tested the coupon function by entering an expired coupon, a coupon that requires a minimum spend, and a valid coupon and ensured all functioned correctly 
- I tested the checkout using the stripe test card and made sure that my order was played correctly 
- I checked the stripe logs and made sure the payment intent was created and the payment was successful 

#### Contact 
- I tested the contact form to make sure that all form validation was functioning and that the success message was correctly displayed after sending an email 

#### Dashboard 
- On the dashboard home, I checked that unique website visits were registering. I refreshed the homepage many times with the current session to make sure only unique visits were being recorded 
- I checked that the correctly website traffic message was being displayed if traffic was up or town from the previous week records 
- I checked the shop stats against by orders and bookings in the django admin panel to make sure stats were displaying correctly 
- For shop management, I checked that products, categories, brands could be added and deleted 
- I checked that setting a ‘sale’ price on an item rendered the sale badge 
- I checked that adding the item as a ‘featured product’ added it to the first list of products on the shop 
- I checked the coupon function by creating coupons with various settings and testing them at checkout 
- For the booking system, I checked that services and service categories could be added and deleted 
- I checked that all bookings appeared in the booking - I checked that when the toggle was checked, the status of the booking changed to true in the database 
- I checked that opening hours could be changed. I marked some days as closed and checked that those days could not be selected in the booking system when selecting a date 
- I checked that you could add and remove staff and made sure that the availability setting matched their appearance when selecting staff members in the booking system 
- I set Django to log emails to the console and checked that the marketing emails form was sending emails to all customers in the list without revealing a list of customer emails in the email header
- I checked that turning the ‘free shipping threshold’ setting on and off changed whether the free shipping banner displayed or not across the site. I checked that changing the free shipping threshold mapped correctly to free shipping been given on checkout 
- I checked that changing the standard shipping fee charged the customer correctly on checkout 
- I checked that toggling the click and collect option on or off correctly displayed or hide the option on checkout 


#### Profile
- I checked that i was able to access my profile and that my booking was listed in my profile 
- I checked that any orders I had made appeared in my profile 
- I updated my details and checked that they saved correctly 


### Unit Testing 
For Unit testing,  I followed  the ‘Don’t Test The Framework’ principle when it came to testing well established and tested code such as  Django, All Auth, Stripe etc.
I tried to test aspects of the site that didn't fall under this category. Unit tests can be found in the respective tests.py file in each app.

#### Booking App
Both the booking and checkout app use a similar system to generate an id associated with the booking/order 

- To test this, I wrote a test to check that whenever a booking is created, a booking id is created with it 
- I tested that the length of the booking id was as expected
- I tested that when the booking view was accessed without being logged in, the user was redirected  

#### Management 
The management app uses a decent amount of AJAX.

- I tested that when information is posted to the site settings view with the name of the setting and a value (E.g: ‘Click & Collect’ = False), that the view correctly changes the setting status 
- I tested the confirm booking view to check that when it receives a post request with a booking id that it correctly changes the status of the booking to ‘confirmed’ 

#### Beta Testing 
   A link to the link was distributed to a small number of people to test the user experience and functionality. Ajustments were made from feedback provided 
   - For example, when making a booking, one user suggested that they might not have a preference for a staff member and that 'No Preference' should be an option in the booking widget 
- Another user noted an error when retrieving cart items after pressing the back botton and not refreshing the page. The cart as then adjusted to make AJAX calls everytime the 
open cart button was selected



### Validation 

- HTML, CSS, and Javascript validation was carried out using a VS Extention (HTMLHint) to check that there were no errors
- Due to jinja template language being used in the html and also html files ‘extending’ other files, some related errors were ignored. 
- Python was validated using Flake8


## Deployment

### Preparation 
I set all config variables to the necessarily environment variables in my settings.py file. This included pointing my database to 

### Github 

- I used git init to initialise a local repository.
- I used git add . - to add the base directory of project code into the local git repository
- I used git commit -m ".." to commit to the local repository with a message containing information on the version
- I used git push to push the local repository to the remote repository on GitHub
- I made sure to include a .gitignore file with the file containing sensitive environment variables listed
- I used pip to freeze my app requirements to a text file 


### Heroku 
- I went to Heroku.com and created an account
- I then created an new App on the Heroku platform
- I set up a new Postgres database 
- I connected my Django app to the postgres database 
- I migrated my app models to the postgres database using (python manage.py migrate)
- I then dumped my model data from my .sqllite3 local database into a json file and loaded it into the new database (using loaddata and dumpdata)  
- I navigated to the 'deploy' tab and selected the github button
- I linked my master branch on Github to my Heroku app (with automatic deploys disabled)
- After pushing to my master branch using the steps above, I navigated to the github section in the deploy tab
- I scrolled down to the manual deploy and selected the master branch - then clicked 'Deploy Branch'
- I waited for the site to deploy
- I navigated to the 'config vars' section in the settings tab
- I set up the necessary environmental variables for the app and saved them

### AWS
I used an S3 bucket to store static files for this project
- I began by creating an AWS account 
- I then created an S3 bucket with public access 
- I created a group, user, and access policy and connected each appropriately 
- I set my AWS access key and secret key in Heroku environment variables


I reloaded the heroku app and checked that everything was working as expected

## Credits / Sources

- Drawings are free to use and were created using a plugin 'unDraw' in Adobe Xd
- Product images and information was obtained from the Xpert Hair database of product images (a distributor of hair and beauty products)  which, as a result of my affiliation with them, have access to for the purposes of testing and development. All products are displayed for demonstration purposes only 
- Credit for Stripe integration goes to Django instructor from Code Institude 
- For Payment Intent Modification - Stripe's Official Documentation 
- Django Unit Testing - DJango Official Documentation 




