# Protein Planner

The Protein Planner is a meal planning app which is designed to target users who want to maximise their daily protein intake. The app allows users to create a meal plan for every meal for every day of the week!

The site acts as a repository for recipes whereby users can store their own recipes and also browse other users' recipes. Users can get organised for the week ahead by adding recipes to their meal planner for each meal for every day of the week. 

The live link can be found here - [Protein Planner](https://proteinplanner-f5152efcdae3.herokuapp.com/)

![Responsive](docs/readme/testing/imgs/responsive.png)
## Table of Contents

- [Protein Planner](#protein-planner)
  - [Table of Contents](#table-of-contents)
  - [User Experience (UX)](#user-experience-ux)
    - [User Stories](#user-stories)
      - [EPIC | User Profile](#epic--user-profile)
      - [EPIC | User Navigation](#epic--user-navigation)
      - [EPIC | Recipe Management](#epic--recipe-management)
      - [EPIC | Mealplan Management](#epic--mealplan-management)
      - [EPIC | Site Administration](#epic--site-administration)
      - [User stories not yet implemented](#user-stories-not-yet-implemented)
    - [Design](#design)
      - [Imagery](#imagery)
      - [Fonts](#fonts)
  - [Agile Methodology](#agile-methodology)
  - [Data Model](#data-model)
  - [Testing](#testing)
  - [Security Features and Defensive Design](#security-features-and-defensive-design)
    - [User Authentication](#user-authentication)
    - [Form Validation](#form-validation)
    - [Database Security](#database-security)
    - [Custom error pages:](#custom-error-pages)
  - [Features](#features)
    - [Header](#header)
    - [Footer](#footer)
    - [Home Page](#home-page)
    - [User Account Pages](#user-account-pages)
    - [Browse Recipes](#browse-recipes)
    - [Recipe Detail Page](#recipe-detail-page)
    - [Profile](#profile)
    - [Meal Planner](#meal-planner)
  - [Add Recipe](#add-recipe)

## User Experience (UX)

A visitor to Protein Planner would be someone who is most likely an adult who enjoys exercisegreat food and wants to maximise their protein intake through delicious meals.They also want the convience of a meal planner that is orientated to maximise their protein intake.

### User Stories

#### EPIC | User Profile
- As a Site User I can register an account so that I can add/edit/delete my recipes and add recipes to my meal planner.
- As a Site User, I can log in or log out of my account so that I can keep my account secure.
- As a Site User I can manage my profile image, description and display my latest recipes.

#### EPIC | User Navigation
- As a Site User I can immediately understand the purpose of the site so that I can decide if it meets my needs.
- As a Site User, I can intuitively navigate around the site so that I can find content and understand where I am on the site.
- As a Site User, I can view a paginated list of recipes so that I can select a recipe to view.
- As a Site User, I can click on a recipe so that I can read the full recipe, ingredients required, instructions on how to prepare, and view Protein and calorie count.

#### EPIC | Recipe Management
- As a Site User, I can input my favourite recipes onto the app through an easy to use interface so that I can share them with other users.
- As a Site User, I can edit and delete recipes that I have created so that I can easily make changes without having to start over.
- As a Site User I can view my recipes so that I can see and manage all recipes I have created in the one location.


#### EPIC | Mealplan Management
- As a Site User, I can add/delete recipes to my weekly meal planner for a particular meal type for a paricular day of the week so that I can create a full meal plan for the week ahead.
- As a Site User, I can view my meal plan for the week when I log into my account so that I can plan for the week ahead.

#### EPIC | Site Administration
- As a Site Administrator, I can create, read, update and delete recipes, and meal plan items so that I can manage the app content.

#### User stories not yet implemented

The following user stories were scoped out of the project due to time constraints and labelled as "Future Features" on the project board on Github. It is intended that these user stories will be implemented at a later date. 

- As a Site User I can use search box so that I can search existing recipes to find the one I require
- As a Site User I can create a monthly meal planner so that I have all my meals planned out for a month

### Design

The site has a very simple and clean design which was purposely chosen in order to keep in theme with the site's goal. i.e. invoking a sense of calm in the user and reducing stress when it comes to everyday meal planning. 

#### Imagery
There are 2 static images assigned to this site. The first is the protein planner logo situated top left of the header. The second is the protein circle image on the homepage displaying the different types of high protein foods with associated values.The rest of the imagery will be uploaded by users for their individual recipes. 

#### Fonts
The Roboto font is the main font used for the body of the website. This fonts were imported via Google Fonts. Serif is the backup font, in case for any reason the main font isn't being imported into the site correctly.

## Agile Methodology

Github projects was used to manage the development process using an agile approach. Please see link to project board [here](https://github.com/users/PatrickG0308/projects/13/views/1)

The 11 User Stories were broken down in accordance with apps being worked on during the project.There is a brief description of the required outcome with each story. The stories were moved across the kanban board as the stories were completed.


## Data Model
I used principles of Object-Oriented Programming throughout this project and Django’s Class-Based Generic Views.  

Django AllAuth was used for the user authentication system.

In order for the users to create recipes a custom recipe model was required. The recipe author is a foreign key to the User model given a recipe can only have one author.


The meal plan item model allows users to add recipes to a meal plan for a particular meal for a particular day. A meal plan item can only have one user and one recipe and is therefore linked to the User and Recipe models through foreign keys.

The diagram below details the database schema.

![Database Schema](docs/readme_images/database_schema.png)

## Testing

Testing and results can be found [here](/TESTING.md)

## Security Features and Defensive Design

### User Authentication

- Django's LoginRequiredMixin is used to make sure that any requests to access secure pages by non-authenticated users are redirected to the login page. 
- Django's UserPassesTestMixin is used to limit access based on certain permissions i.e. to ensure users can only edit/delete recipes and comments for which they are the author. If the user doesn't pass the test they are shown an HTTP 403 Forbidden error.

### Form Validation
If incorrect or empty data is added to a form, the form won't submit and a warning will appear to the user informing them what field raised the error. 

### Database Security
The database url and secret key are stored in the env.py file to prevent unwanted connections to the database and this was set up before the first push to Github.

Cross-Site Request Forgery (CSRF) tokens were used on all forms throughout this site.

### Custom error pages:

Custom Error Pages were created to give the user more information on the error and to provide them with buttons to guide them back to the site.

- 400 Bad Request - Protein Planner is unable to handle this request.
- 403 Page Forbidden - Looks like you're trying to access forbidden content. Please log out and sign in to the correct account.
- 404 Page Not Found - The page you're looking for doesn't exist.
- 500 Server Error - Protein Planner is currently unable to handle this request

## Features

### Header

![header](docs/readme_images/features/nav_loggedout.png)

**Logo**
- A customised logo was created using Hatchful by Shopify which is a free logo generator.
- This logo is positioned in the top left of the navigation bar. The logo is linked to the home page for ease of navigation for the user.

**Navigation Bar**

- The navigation bar is present at the top of every page and includes all links to the various other pages.
- The My Account navigation link is a drop down menu which includes the Sign up and Log in links. 
- When the user has logged in, the My Account drop down menu changes to display the user's name and a profile icon.

![header](docs/readme_images/features/header.png)

- The options to Sign up or Log in will change to the option to log out once a user has logged in.
- Once a user has signed in, more options such as 'Add Recipe', 'My Meal Plan', 'My Recipes' and 'My Bookmarks' become available.
- The navigation bar is fully responsive, collapsing into a hamburger menu when the screen size becomes too small.
- Hovering over the links will lighten the font.


### Footer

![header](docs/readme_images/features/footer.png)

- The footer section includes links to Linkedin, Instagram, Github and Facebook.
- Clicking the links in the footer opens a separate browser tab to avoid pulling the user away from the site.

### Home Page

**Call to Action Section**

![header](docs/readme_images/features/homepage.png)

- The home page includes a call to action section which encourages the user to sign up to the site.
- The CTA includes a sign up button which takes the user to the sign up page.
- The homepage outlines what the features of the site are and outlines some of the benefits of a protein based meals

**Logged in User section**
- If a user is signed in the message changes to 'Welcome back to your Protein Planner' and the user is encouraged to add a new recipe or create a meal plan.
 

![header](docs/readme_images/features/home_loggedin.png)

### User Account Pages

**Sign Up**

![header](docs/readme_images/features/signup_page.png)

**Log In**

![header](docs/readme_images/features/signin_page.png)

**Log Out**

![header](docs/readme_images/features/sign_out.png)

- Django allauth was installed and used to create the Sign up, Log in and Log out functionality. 


### Browse Recipes

![header](docs/readme_images/features/recipes.png)

- This page displays all recipes with the most recent recipes displayed first.
- Each card displays the recipe's image, Title and a short description. 
- Clicking anywhere inside the recipe card will take you directly to that recipe's detailed page.

### Recipe Detail Page

![header](docs/readme_images/features/recipe_detail.png)

- The recipe header section at the top of the page shows the recipe image, title, author, created date and time.
- A brief description of the meal is shown as well as the Calorie count in kcals and the protein count in grams
- A Edit and Delete button is available allowing the authorised user to edit the recipe or delete the recipe, if user is not hte creator of the recipe the Edit or delete buttons will not appear.

**Edit Recipe**

![header](docs/readme_images/features/edit_recipe.png)

**Delete Recipe**

![header](docs/readme_images/features/delete_recipe.png)

- The recipe detail page also contains a list of ingredients and instructions on how to prepare the dish.

**Ingredients & Instructions**

![header](docs/readme_images/features/recipe_prep.png)

### Profile

- When a user sign's in they are presented with a "Profile" button on the NavBar
- In the profile section the user is presented with the following
      
    * Image\Avatar of user it provided by user
    * Username
    * Date user joined    
    * Number of recipes user has added
    * Edit Profile button
    * Meals button
    * List of Latest Recipes

![header](docs/readme_images/features/profile_main.png)

**Edit Profile**

- Allows user to edit their image and biography.

![header](docs/readme_images/features/edit_profile.png)

### Meal Planner

- The Meal Planner is only accessible through the authenticated user Profile page through the "Meals" button 
- The Weekly Meal planner page is based on accordian design provided by Bootstrap
- Lists 7 Days starting on Monday finishing on Sunday 

![header](docs/readme_images/features/meal_planner_home.png)

- When user chooses the date they are presented with a choice
  * Add or Update Meals 
  * Choose Breakfast, Lunch, or Dinner

![header](docs/readme_images/features/meal_planner.png)

- When user selects meal type they are presented with a choice
  1. Choose by Max Protein in grams
  2. Search for a recipe by keyword
  3. Use the "Find Random Recipe" button
  4. Once happy with selection they press the "Add Meal" button.

![header](docs/readme_images/features/meal_type.png)

- The meal is added to the users planner

![header](docs/readme_images/features/meal_planner_list.png)

## Add Recipe

- All authenticated users can add recipes to the site
- Other authenticated users can view these recipes and if desired can add other users recipes to their own meal plans.
- Only the recipe creator or site admin can edit or delete their recipes

![header](docs/readme_images/features/add_recipe.png)
![header](docs/readme_images/features/add_recipe_2.png)