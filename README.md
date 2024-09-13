# The Enchanted Library 
![image](https://github.com/hubkinza/django-fullstack-project/assets/76822546/e2ef83bf-c44c-4272-b751-8a941d915112)



Welcome to The Enchanted Library, an enchanting digital realm where librarians orchestrate the magic of book management and members embark on captivating reading adventures. The Enchanted Library provides a whimsical platform for librarians to seamlessly organize their collections and for members to curate their own mystical reading journeys.

Within The Enchanted Library, librarians wield powerful tools to effortlessly catalog, categorize, and track their vast collections. With a sprinkle of digital magic, administrative tasks become a breeze, allowing librarians to dedicate more time to nurturing their literary communities.

For members of The Enchanted Library, the journey begins with creating an account and stepping into a world of wonder. As they wander through the virtual aisles, members can discover treasures from the vast catalog and add them to their magical wishlists. 

Join us at The Enchanted Library and unlock the secrets of seamless library management and captivating book discovery. Whether you're a librarian weaving the threads of literary magic or a member seeking the next thrilling adventure, The Enchanted Library invites you to embark on a voyage through the wonders of the written word. Enroll today and let the enchantment begin!

# Purpose


The Enchanted Library utilizes Django, a robust Python web framework, to facilitate seamless functionality and user interaction. Employing CRUD operations (Create, Read, Update, Delete), the website empowers users to manage library Books with ease:

Create: Users, including librarians and members, can create accounts and wishlists.

Read: Visitors explore a wide variety of books.

Update: Administrators maintain homepage content, ensuring visitors are can get to the latest books.

Delete: Obsolete books can be removed by the library adminstration.

In essence, Django serves as the backbone of The Enchanted Library, facilitating intuitive Book management and ensuring a seamless user experience.
The live website can be accessed [here](https://hubkinza-capstone-project-f145d100cd87.herokuapp.com/).
___

# UX Design

Target audience:
-The target audience for The Enchanted Library encompasses both librarians and avid book enthusiasts. 

Librarians: Professionals tasked with managing library managemnet. The website provides them with tools to organize and administer library resources efficiently.

Book Enthusiasts: Individuals passionate about literature, seeking a platform to discover new literature. They can create accounts, explore the available book, and save books that catch their intrests.

In essence, The Enchanted Library caters to a diverse audience united by their love for books and literary experiences, offering a digital sanctuary where they can connect, explore, and indulge in their passion for literature.

## User stories

### Epic: Account Mangemnet 

- As a new user, I want to create an account on The Enchanted Library so I can access exclusive Books and features.
- As a book enthusiast, I want a simple registration process on The Enchanted Library to quickly join the community and start exploring literary Books.
- As a librarian, I want users to register on The Enchanted Library to ensure access control and foster engagement within the library community.
- As a returning member, I want to easily log in to The Enchanted Library with my existing credentials to access my account and personalized features.
- As a site user I can **register/login** so that I can **access content only for logged-in users**.
- As a site user I can **logout** .


### Epic: Book Display Catalog 


- As a user, I want to browse the catalog of books available in The Enchanted Library to discover new literary gems.
- As a librarian, I need to add new books to the catalog of The Enchanted Library to keep the collection up-to-date.
- As a book enthusiast, I want to search the catalog of The Enchanted Library by genre, author, or title to find specific books of interest.
- As a user, I want to see detailed information about each book in the catalog, including summaries, authors.
- As a librarian, I want to update the information for books in the catalog, such as adding new editions or removing books no longer available.
-  As a member, I want to create and manage personalized book lists or wishlists within The Enchanted Library to keep track of books I want to read.


### Epic: Wishlist and Search functionality 

- As a user, I want to create a wishlist on The Enchanted Library to keep track of books I desire to read in the future.
- As a member, I need the ability to add and remove books from my wishlist on The Enchanted Library to manage my reading preferences effectively.
- As a user, I want to search for specific books within The Enchanted Library's catalog by title, author, or genre to quickly find desired titles.
- As a member, I expect the search functionality on The Enchanted Library to provide relevant and accurate results, enhancing my browsing experience.
- As a user, I want the wishlist and search functionalities on The Enchanted Library to be seamlessly integrated, allowing me to add desired books directly from search results to my wishlist.


## Administrator user stories

### Epic: Site Administration

- As an administrator, I need access to a secure login page to authenticate and gain entry to the administrative dashboard.
- As an administrator, I want the ability to manage user accounts, including creating, editing, and deactivating accounts as needed.
- As an administrator, I require the ability to manage books, including, editing, or removing books from the database.

## UAC

### User Acceptance Criteria Derived From User Stories

- The registration process should be easily accessible from the homepage.
- New users should be prompted to provide necessary information such as username, email, and password.
- Upon successful registration, users should be able to login.
- The registration form should be user-friendly and require minimal information from the user.
- Error handling should be in place to provide clear feedback if any required fields are missing or if the chosen username or email is already in use.
- Users must be registered and logged in to access exclusive features such as creating wishlists and accessing library content.
- Access to certain sections of the website, such as Adding and deleting  books should be restricted to admin users only.
- The book catalog should be organized and easily navigable, with options to search by genre, author, or title.
- Each book entry in the catalog should display detailed information including title, author.
- The search functionality should be prominently displayed and easily accessible from any page within the website.
- Users should be able to search the catalog by title, author, or genre and receive relevant and accurate results.
- Librarians should have access to a dedicated interface for adding new books to the catalog.
- The process of adding new books should be straightforward and include fields for entering all relevant book information.
- Logged-in users should have the option to create and manage personalized wishlists within the website.
- Users should be able to add and remove books from their wishlist with ease, directly from the book catalog or search results.

#  UI Design


### Colour Scheme

![Color Palette](https://github.com/hubkinza/django-fullstack-project/assets/76822546/9b1a579c-d3bc-44ff-8fb4-58cff7615ae7)


### Typography

[EB Garamond] - Used for titles
[Roboto] - Used as the main font
[serif]- Added as a failsafe in case another font doesnt load 


### Images

The images in this project were all sourced from [pixby](https://pixabay.com/) and [FreeP!c](https://www.freepik.com/popular-photos)

The favicon was sourced from  [Favicon.io](https://favicon.io/emoji-favicons/#google_vignette)


___
# Agile Process
## Scope

### High-level Essential Features

 - Home page
 - Navigation menu
 - User Registration
 - An Avaialbe Books page
 - An Add books page
 - A search bar 
 - User wishlist 
 - Registration, login and logout pages


| Feature  |  Priority |
|---|---|
| Home Page | 1 |
| User Registration | 1  |
| User Login/Logout| 1  |
| Navbar|  1 |
| Footer | 3 |
| Admin Can Add books | 1 |
| Users Can Add books to wishlist | 1  |
| Admin Can delete books | 1 |
| Users cannot see the Add Book page| 2|
| Not logged in users are unable to access available book page|1|
| Admin Can edit wishlist of all users | 3 |
|Signout page|1|


The Project Board for The enchnated Library can be found [here](https://github.com/users/hubkinza/projects/7).

The following categories were applied as custom labels to prioritize user-stories:
- Must Have
- Should Have
- Could Have
- Will Have


### User Story Based on priority

![User Story Priorities ](https://github.com/users/hubkinza/projects/7/views/2?visibleFields=%5B%22Title%22%2C%22Assignees%22%2C%22Labels%22%5D)
)

___

# Wireframes

## Low-fidelity Mobile Wireframes:

### Home Page  
<details><summary>click to expand</summary>
  ![Home page](https://github.com/hubkinza/django-fullstack-project/assets/76822546/86ba85cf-af0d-4655-88c0-7c4ab9690898)
</details>


### Registration and Login Pages
<details><summary>click to expand</summary>
![Register](https://github.com/hubkinza/django-fullstack-project/assets/76822546/1311fcc0-6ffa-486a-81a5-9ad12f34b030)
![login](https://github.com/hubkinza/django-fullstack-project/assets/76822546/a353a9bf-d044-4d5b-bc4b-5fc802209fe1)


</details>

### Avaiable Books Page
<details><summary>click to expand</summary>
[Admin After sign in](https://github.com/hubkinza/django-fullstack-project/assets/76822546/611ddf34-1c98-44a1-b5c6-d42293475864)
</details>


### Book detail Pages
<details><summary>click to expand</summary>
![Book detail](https://github.com/hubkinza/django-fullstack-project/assets/76822546/b1b09a20-b8c7-49d9-91d0-5990aaa04023)

</details>


### Add to wishlist Page
<details><summary>click to expand</summary>
![Wishlist](https://github.com/hubkinza/django-fullstack-project/assets/76822546/93d65672-9637-4dae-9345-340bc47bfd66)

</details>

### Signout Page
<details><summary>click to expand</summary>
![sign out](https://github.com/hubkinza/django-fullstack-project/assets/76822546/57cf6810-ecc3-4a6f-a320-8859832614ba)
</details>




## Structure

### Home Page

![The Enchanted Library]
![image](https://github.com/hubkinza/django-fullstack-project/assets/76822546/ffb139fe-7242-48db-b189-883b00e4b2bc)



- Uses Headings and images to explain what the site is about
- Offers options for what users can do next such as browse books or Register or Login



    #### User Goals:
    > Understand what the website is for.
    > Sign up easily.
    > Explore what's available without logging in.
    > Connect with the site on social media
    
    #### Website Goals:
    >   - Ensure the site looks good and is easy to use throughout.
    >   - Capture users' interest and encourage them to join.
    >   - Engage users and interest potential memebers.
    >   - Prompt users to take action.
    >   - Clearly state the website's purpose.




### Sign Up Page

![![The Enchanted Library](.JPG)

- Lets new users create accounts to access the site

    #### User Goal:
    > Create an account.

    #### Website Goals:
    > Allow users to sign up.
    > Ensure the sign-up process fits with the site's design.


### Sign In Page

![![The Enchanted Library](.JPG)


- Lets registered users log in

    #### User Goal:
    >   - Log in.

    #### Website Goals:
    >   - Allow users to sign in to access content.
    >   - Keep the sign-in process visually consistent with the site.

### Available Books Page

![![The Enchanted Library](.JPG)


Displays books approved by admins, sorted by newest first.
Each Card has a link for more details. it is Only accessible to logged-in users.

  #### User Goals:
   >   - Look through available books.
   >   - Read more about specific books.

  #### Website Goals:
   >   - Show a list of available books.
   >   - Provide previews of books.
   >   - Maintain a consistent look and feel.

### Book Detail Page
 
![![The Enchanted Library](.JPG)



- Gives details about the Book title genre and a brief summary of the book
- Contains a Wishlist button so users can add a book to their wishlist

   #### User Goals:
    >   - User Goals:
    >   - Read about available books.
    >   - Add books to their wishlist.
    >   - 
   #### Website Goals:
    >   - Display available books with descriptions
    >   - Enable admin to edit or delete books.
    >   - Keep the design consistent and attractive.
  

### Add BOOK

IMAGE

- Allows admin users to create a new Book


    #### User Goals:
    >   - Create a new Book.
    >   - Update existing Books.

    #### Website Goals:
    >   - Let Admin users create or update books.
    >   - Ensure a visually pleasing experience and consistent design.
    
### Wishlist 
Displays books Added by users to their wishlist 


  #### User Goals:
   >   - Create a custom wishlist
   >   - View books they added to wishlist
>      - Remove Books from wishlist

  #### Website Goals:
   >   - Show a list of books added by user in their wishlist
   >   - Provide previews of books.
   >   - Maintain a consistent look and feel.

# Technologies Used
 - Django
   was used as the python framework in the project.Django all auth was used to handle user authentication and related tasks i.e. sign in, sign up, sign out.
- Heroku
  Used to deploy the page and make it publicly available.
- Elephant SQL 
  Used for the database during development and in deployment.
- HTML
  HTML was the base language used to layout the skeleton of all templates.
- CSS
   used to style the page and make the appearance look a little more unique.
- Bootstrap 5.1.3
  Used to style HTML, CSS.
- UX Wing iconshttps://uxwing.com/ 
  All icons throughout the page.
- Cloudinary was use to host all images 


# Testing 
I have included testing details in a separate document called [TESTING.md](https://github.com/hubkinza/django-fullstack-project/blob/main/TESTING.md)

# Deployment
## Github
The base environment for this project was created by navigating to the gitpod CI template and clicking 'Use this template'.

After making a new respository for my  project from the CI template, I created a workspace in gitpod where all of my development took place.

Development Environment Set-Up
the enchanted Library makes use of many Django packages. For ease of set-up I pasted the contents of the requirements.txt file from our third hackathon into my workspace and used the following command to install all base packages I believed I needed at the start of the project:

pip3 install -r requirements.txt

I then created a Procfile and added a line of code for Heroku deployment: web: gunicorn wellread.wsgi

After doing this I set up external services(covered below) in gitignored env.py, added any packages to INSTALLED_APPS in settings.py where necessary and then used the following commands to perform any database migrations (these steps were repeated later in development as I developed my own models):

python3 manage.py makemigrations

python3 manage.py migrate

To commit the changes to my Github repo I used the following terminal commands:

git add . git commit -m "commit message here" git push

I had my basic project and app structure in place before preparing for early Heroku deployment

## Heroku
Heroku is used to host the enchanted library . Heroku is a container-based cloud Platform for building, deploying and managing apps. This project was first deployed to Heroku in the very early stages following app structure setup.

The steps are as follows:

Login or create an account on Heroku.

Click new in the top right corner and choose create new app.

Choose a unique app name and your region and click create app.

Navigate to the Settings tab, and click Reveal Config Vars.

Setup External Services:

Log in or create an account on Cloudinary. Navigate to the Dashboard on Cloudinary, copy and store the value of the 'API Environment Variable" ( begins with cloudinary:// ) and paste it into your config vars CLOUDINARY_URL = cloudinary://<your_value>

Log in or create an account on ElephantSQL. Create a new instance. Select the free plan Tiny Turtle and leave the tags blank. Select the region and choose the nearest data centre to your location or the one that works. Click 'review' and check the details and click the button to create the instance. Click on the instance you created copy the ElephantSQL database URL from the instance details and paste it into your config vars DATABASE_URL = postgres://<your_value>

Navigate to the Deploy tab and select GitHub as a deployment method. Find the repository to connect to and choose the branch to deploy. Wait for the app to build, click on View.

Towards the end of the project I regenerated the SECRET_KEY and did the following;

Add Django secret key to config vars SECRET_KEY


Prior to submitting the finished project I ensured I had DEBUG=False in settings.py
___
# Credits 
 - Balsamiq was used to create the wireframes.
 - The site was developed using GITPOD.
 - GitHub was used to store my repository.
 - Screenshot made using Snagit
 - Guidance on file structure for templates folder from ChatGPT
 - W3cschool
 - Fonts were taken from Google Fonts
 - Mc DEE Walkthrought project for recipe website was refrenced to structure the website https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy
 - Inspo for read me https://github.com/dnlbowers/jobs-a-gooden?tab=readme-ov-file#honorable-mentions
 - https://github.com/hiboibrahim/thebookbooth1/tree/main
 - I think therefore I BLOG 
    General references:
     Geeks for Geeks
     Stack Overflow
     Code Institute Learning Platform
     Django Documentation
     Bootstrap Documentation


