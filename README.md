# The Enchanted Library 

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
The live website can be accessed [here]().
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
<img src=.png>
</details>


### Registration and Login Pages
<details><summary>click to expand</summary>
<img src=.png>
</details>

### Avaiable Books Page
<details><summary>click to expand</summary>
<img src=.png>
</details>


### Book detail Pages
<details><summary>click to expand</summary>
<img src=png>
</details>


### Add to wishlist Page
<details><summary>click to expand</summary>
<img src=.png>
</details>

### Signout Page
<details><summary>click to expand</summary>
<img src=.png>
</details>


# Database Design


![ERD]()

## Structure

### Home Page

![The Enchanted Library]( add screenshot)

- Uses text and images to communicate the site purpose
- Presents opportunities for further actions 

    #### User Goals:
    >   - Understand the main purpose of the website.
    >   - Have access to registration.
    >   - Be able to navigate publically available content.
    >   - Connect with affiliated social media.

    #### Website Goals:
    >   - Communicate main purpose of the page.
    >   - Engage users and interest potential memebers.
    >   - Call to action.
    >   - Provide an aesthetically pleasing user experience with site-wide consistent styling.

### Sign Up Page

![![The Enchanted Library](.JPG)

- Allows users to register so that they can access site content

    #### User Goal:
    >   - Register

    #### Website Goals:
    >   - Allow user registration
    >   - Provide an aesthetically pleasing user experience with site-wide consistent styling.


### Sign In Page

![![The Enchanted Library](.JPG)


- Allows users to sign in

    #### User Goal:
    >   - Sign in.

    #### Website Goals:
    >   - Allows users to sign in so that they can access content.
    >   - Provide an aesthetically pleasing user experience with site-wide consistent styling.

### Available Books Page

![![The Enchanted Library](.JPG)


- Shows admin-approved, user-created Books in order of the most recent first.
- List of Books is paginated by 6 so as not to overwhelm the user.
- Each card has a link the user can click on for more details. 
- Available only to view by authenticated users.

    #### User Goals:
    >   - Browse the Books
    >   - Open the Books to see them in more detail.

    #### Website Goals:
    >   - Provide a list of Books.
    >   - Provide some information on each Book in a preview.
    >   - Provide an aesthetically pleasing user experience with site-wide consistent styling.

### Book Detail Page
 
![![The Enchanted Library](.JPG)


- Shows the details of the run such as how many people the organiser is looking to have join them, the location and what other users are going. 
- Allows authenticated users to see and write comments on the Book, as well as manage their own comments.
- Allows authenticated users to say they will attend the Book, also allows them the option of cancelling their own attendance.
- Allows the Book organiser to manage the Book post.
- Allows superusers/site admin to delete the post and/or any comments on it.
- Available only for authenticated users.

    #### User Goals:
    >   - See the details of books available in the libraray .
    >   - Add favourite books to their wishlist .
    >   - Manage and  organise book availbale in the library .


    #### Website Goals:
    >   - Show Avaiable Books.
    >   - Allows users to read description .
    >   - Allow  Admin to Edit and delete books.
    >   - Provide an aesthetically pleasing user experience with site-wide consistent styling.

### Create/Update Post Page

IMAGE

- Allows authenticated users to create a new Book
- Allows Book organisers to update their own Book.
- Validates image file input to prBook uploading of file-types outside of those specified.

    #### User Goals:
    >   - Create a new Book.
    >   - Update existing Books.

    #### Website Goals:
    >   - Allow the user to create/update an Book
    >   - Provide an aesthetically pleasing user experience with site-wide consistent styling.


