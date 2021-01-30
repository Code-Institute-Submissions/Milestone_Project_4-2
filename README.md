https://poster-django-app.herokuapp.com/     -- deployment



Movie Poster Store is an online store for all your movie posters.

## UX

The website is a super simple design to ensure an easy to use layout and smooth streamed selling service. The website features both a sticky header and a sticky footer so cart is always displayed and a large easy to find checkout button.
The header allows the users to easily find their profile and navigate through the different poster genres. 

### User Stories

#### Store Owner
The site owners want to easily perform CRUD tasks as lots of posters are continually added and removed from site depending on stock.


Posters


- Create: The store owners can log in using an admin super user account. Once logged into this account an admin task button will be displayed in the header. This will provide links to add and remove posters are poster info and details.

- Read: The store owner wants to view the posters available for sale. This can be compleated regardless of log in status. The top navigation bar hosts a drop down menu displaying all posters or by a specific category. 

- Update: The store owner can log in using the superuser account credential provided. Once logged in the product to be modified can be searched for inthe search bar.

- Delete: Once store owner is logged in as superuser they can also remove item using the displayed delete button.

Blog

All the same CRUD applications also apply to the Blog section where the owner can also write blogs and post pictures.

#### Customer:

Register: The main navigation bar hosts a profile drop down menu. When no user is logged in, this will show a register button. By following this link, the customer will be brought to a registration form. Completing this form, a user account and a user profile will be generated. The visitor will also be sent an email confirmation that is required to fully authenticate the account creation.

Login: The main navigation bar also hosts a login button in the profile drop down menu when no user is logged in. The link leads to a standard login page where the user can use either their username or email address to login alongside their password.

Purchase: The customer can add products on the cart. Once ready to make the purchase, the checkout button is always on display in the footer. This payment can be made as a registered user or as a guest. If the visitor is logged and has made a purchase in the past, the form will be populated with the default shipping and contact information. The customer can also enter different information and then choose whether or not to update their user profile with the information in the form. A stripe credit card payment section at the bottom allows visitor to pay with a various cards.


## Features

The store owner has full CRUD functionality available via the frontend for both products and blogs.

The customer is able to purchase products both as as a guest and as a registered user.

The search functionality available allows the users to search through product title, short description, full description, category, and also by the unique ISBN numbers.

The sorting fearure allows the products to be sorted by price, name, rating, and category. 

The order profile page provides a clear view of the users personal account and also provides the ability to update default shipping and contact information.

The points feature allows the users to collect points on every purchase made. Each dollar earns the user 100 points. The points balance in the user profile accumulates as the user continues to shop.

The total savings feature allows the user to constantly track how much they are saving by utlizing the discounted price. This value is always present in the sticky footer acting as a constant reminder of their savings. To further assist the user in making the purchase and taking advantage of the savings, a large checkout button is also present in the footer.

## Technologies used

JS/jQuery - Used to conduct interactive functions on the front end of the website.
Python/Django - Used to create the apps.
HTML - Used to build basic content of the website.
CSS - Used for complete styling of the website.
Bootstrap - Used to apply layout style to the website.
Heroku - Used to deploy the app.
Postgres - Used as a database to store the data on heroku.
Font Awesome - Used to insert icons on the page.
Whitenoise - Used to allow Heroku to load static files as AWS.
All Auth - Used as an authentication platform for users on the website.
Miniwebtool - Used to generate a secret key
Stripe - Used to recieve payments from the users for their purchase
Crispy Forms - Used to style the forms in Django


## Deployment

The website was pushed to github using gitpod to maintain version control. Once the final version of the website was committed and pushed, the website was hosted using heroku and postgres as the deployment database. 

Please find the live website here: (https://poster-django-app.herokuapp.com/)

