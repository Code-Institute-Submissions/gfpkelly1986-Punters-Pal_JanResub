# Punters Pal - A diary structred for, and aimed at, the Horse-Racing Community.

  <p align="center">
  <img src="static/images/readme-images/Am-I-responsive.png"?raw=true alt="Responsive image of project"></p>

# <p href="#intro" id="intro"> - Intended Purpose of This Website:</p>

  - The intended purpose of this website was to build a simple diary that a race-goer could use to enter race information relating to a horses run. The user has access to a form field on login where they can quickly enter an entry to their diary. The diary is formatted to allow the user enter details about the track, race type, horses name, grade, distance, going, trainer, jockey, number of runners, resulting position of entry, result of the race (1,2,3), and a text area where they can enter some of their own insights about the race or why they are following the horse to begin with. Only registered users can use the diary feature. A blog was provided to give unregistered users something to browse after landing on the website.


## Table of contents
- <a href="#ui">UI/UX</a>
- <a href="#thm">Themes</a>
- <a href="#epi">Epics</a>
- <a href="#us">User Stories</a>
- <a href="#de">Design</a>
- <a href="#wire">Wireframes</a>
- <a href="#erd">ERD Diagram</a>
- <a href="#lf">Live Features</a>
- <a href="#df">Desired Features</a>
- <a href="#tpy">Automated Testing(Python)</a>
- <a href="#mnts">Manual Testing</a>
- <a href="#dep">Deployment</a>
- <a href="#b">Bugs During Development</a>
- <a href="#ub">Unsolved Bugs</a>
- <a href="#tu">Technologies Used</a>
- <a href="#cr">Credits</a>


<p align="right"><a href="#intro">Return to table of contents</a></p><p id="ui"></p>

# UI-UX

  ## Site Purpose

  - The Purpose of this website is to have a structured note taking application for members of the Racing Community so they can keep a record of horses they want to follow in the future and why they chose to follow them. It will allow users to make structured but personalised entries into the diary and act as a personal database for them. They should have full CRUD functionality for their diary entries.

  ## Site Goal and Intended Audience

  - Appeal to members of the Racing Community. Give these users a personal, digitalized option to store and track information relating to horses they wish to follow.


<p align="right"><a href="#intro">Return to table of contents</a></p><p id="thm"></p>

# Themes

- Design a site that is useful for people who want to track horses they like.

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="epi"></p>

# Epics

- The Unregistered User

- The Registered User


<p align="right"><a href="#intro">Return to table of contents</a></p><p id="us"></p>

# User Stories

## As an unregistered user I can relate to the appeal of this website so that I am encouraged to sign up.

  ### Acceptance Criteria
  - Landing page content must appeal to the target audience.

  - Title must communicate the sites goals clearly.

  - Imagery used must appeal to the target audience.

  ### Tasks
  - Source images for landing page to appeal to a racing audience.

  - Create a title that will explain what the sites purpose is.

## As an unregistered user I can sign up easily so that I can use the websites full features.

  ### Acceptance Criteria
  - Users must understand when on the landing page that the diary is for registered users only.

  - Functionality to create an account must be present in more than one location.
  
  ### Tasks
  - Explain the sites purpose clearly in the content description.

  - Create sign up button in the nav-bar.

  - Build a 'create account' button under the landing page content area.

## As an unregistered user I can have the option to authenticate my email address as an option during sign in

  ### Acceptance Criteria
   - All-auth is implemented correctly.

   - Users can login successfully with allauth.

  ### Tasks
   - Implement all-auth for user sign in.

## As an unregistered user I can have the option to authenticate myself using my google account as an option during sign in

  ### Acceptance Criteria
  - Users can succesfully login with their google account credentials.

  ### Tasks
  - Implement sign in via google. 

## As a registered user I can login and logout of my account so that my account is unique to me.

  ### Acceptance Criteria
  - Users are taken to the correct locations on the site when logged in an logged out.

  ### Tasks
  - Implement login and logout redirects for all-auth.

  - Login will bring user to the create new entry page.

  - Logout will bring the user to the landing page.

## As a registered user I can access the capability of using the diary so that I can keep track of horses I like

  ### Acceptance Criteria
  - Registered users have full use of the site. Unregistered can only read the blog.

  ### Tasks
  - Give registered users only access to the create entry page using 'if is_authenticated'.

## As a registered user I can be redirected to the 'create new diary entry page' so that I can make a rapid entry

  ### Acceptance Criteria
  - Users should have multiple options available to get back to the create new entry page from all locations within the site which make sense to have the option.

  ### Tasks
  - Build create new entry button into navbar on page for viewing entries.

  - Build create new entry button into every entry in the diary alongside the edit entry button.

## As a registered user I can have access to a structured note entry functionality so that all of my notes are structured and organised

  ### Acceptance Criteria
  - Users have all the fields necessary to take a detailed note on the result of a horse race.

  ### Tasks
  - Build all the fields on the 'Create Entry' data model based on the fields that would be typically given on a result/form so users can record relevant information.

## As a registered user I can see my notes presented to me organised and visually appealing so that I can re-read my notes comfortably

  ### Acceptance Criteria
  - Build a seperate page where users can see the information they entered presented back to them clean, organised, easy to read.

  ### Tasks
  - Create a view entry page. All data to be organised logically and easy to read. 

## As a registered user I can perform full CRUD functionality on my notes so that I can I can control all of the entries

  ### Acceptance Criteria
  - Users can Create, Read, Update and Delete notes from their diary.

  ### Tasks
  - Implement full CRUD functionality for users note entries.

## As a registered user I can search my notes so that they are easy to find when needed

  ### Acceptance Criteria
  - Users can search their note entries.

  ### Tasks
  - Implement a search diary functionality.

  - Users can be redirected to the same page but only view the searched entry.

## As a registered user I can comment, like, and share posts in the blog so that the website is more appealing

  ### Acceptance Criteria
  - Users can can read, comment, like and share blog posts.

  ### Tasks
  - Populate the blog with some interesting articles.
  
  - Implement functionality to comment on the blog posts.

  - Implement functionality to like the blog posts.

  - Implement functionality to share the blog posts.

## As a User I can access the blog so that read articles and chat to people in my community

  ### Acceptance Criteria
  - All users should be able to view the blog regardless of whether they have an account.

  ### Tasks
  - Allow all users to view the blog

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="de"></p>

# Design

  - Color Pallete
    - #f4f5f7
    - #261717
    - #cdb06f
    - #d9d3cf 

  - Fonts
    - Railway
    - Nunito

<p align="center">
  <img src=""?raw=true alt=""></p>


<p align="right"><a href="#intro">Return to table of contents</a></p><p id="wire"></p>

# Wireframes

  - Title of the wireframe

<p align="center">
  <img src="static/images/readme-images/Landing-Page-PP.png"?raw=true alt=""></p>

<p align="center">
  <img src="static/images/readme-images/Login-Page-PP.png"?raw=true alt=""></p>

<p align="center">
  <img src="static/images/readme-images/Sign-up-Page-PP.png"?raw=true alt=""></p>

<p align="center">
  <img src="static/images/readme-images/Note-Entry-PP.png"?raw=true alt=""></p>

<p align="center">
  <img src="static/images/readme-images/Note-Display-PP.png"?raw=true alt=""></p>

<p align="center">
  <img src="static/images/readme-images/Blog-Chat-PP.png"?raw=true alt=""></p>

<p align="center">
  <img src="static/images/readme-images/Blog-Detail-PP.png"?raw=true alt=""></p>



<p align="right"><a href="#intro">Return to table of contents</a></p><p id="erd"></p>

# ERD Diagram

  - Title of ERD Diagram

<p align="center">
  <img src="static/images/readme-images/ERD diagram Project4.png"?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="lf"></p>

# Live Features

  ## Landing page with option to create a new account.

<p align="center">
  <img src="static/images/readme-images/landing page.png"?raw=true alt="landing page feature"></p>

  ## Sign up page. Users can use the custom styled all auth forms or use their google accounts to sign up/login.

  <p align="center">
  <img src="static/images/readme-images/sign-up-page.png"?raw=true alt="sign up page feature"></p>
  <p align="center">
  <img src="static/images/readme-images/google sign in.png"?raw=true alt="google sign in page feature"></p>
  <p align="center">
  <img src="static/images/readme-images/login.png"?raw=true alt="login feature"></p>

  ## Custom styled form structured for input related to racing. User welcomed by name.

  <p align="center">
  <img src="static/images/readme-images/new-entry.png"?raw=true alt="new entry feature"></p>

  ## Diary entries sorted and displayed nicely. Users can edit and delete entries in their diary.

  <p align="center">
  <img src="static/images/readme-images/diary entries.png"?raw=true alt="diary display feature"></p>
  <p align="center">
  <img src="static/images/readme-images/edit-entry.png"?raw=true alt="edit diary feature"></p>

  ## Search diary by Horse Name to find selections.

  <p align="center">
  <img src="static/images/readme-images/search-entry.png"?raw=true alt="search entry feature"></p>

  ## Blog content

  <p align="center">
  <img src="static/images/readme-images/blog-1.png"?raw=true alt="blog content"></p>
  <p align="center">
  <img src="static/images/readme-images/blog-2.png"?raw=true alt="blog content"></p>

  ## Blog Detail
  <p align="center">
  <img src="static/images/readme-images/blog-detail.png"?raw=true alt="search entry feature"></p>


<p align="right"><a href="#intro">Return to table of contents</a></p><p id="df"></p>

# Desired Features

  ### Chat room
    - Users given the opportunity to build a community and chat to like minded people
  ### Search notes (All criteria)
    - Users given the functionality to search the diary by any criteria they want to use
  ### Expand information relating to an entry
    - Users given another window where they can fill out detailed bio on any of their entries. Specific to the entry in question. Age, sire, value, breeder etc.
  ### External API
    - Use an external API to grab result data and populate the diary. API could also be used to access video content relating to each entry.

  <p align="center">
  <img src="static/images/readme-images/API.png"?raw=true alt="The betfair API"></p>

  ### Full google auth functionality
    - Currently users can only sign in with google via a seperate page. Users should have immediate sign-up/login functionality using googles custom buttons.
  ### Batch diary entries
    - When the diary has hundreds of entries it would be nice to have the ability to batch the entries by trainer, age, ability etc and store them together so they can be accessed more easily.



<p align="right"><a href="#intro">Return to table of contents</a></p><p id="tpy"></p>

# Testing (Python)

  ### Run 14 automated tests using Python's UnitTest
  - Testing here is for the diary app of this project.
  
<p align="center">
  <img src="static/images/readme-images/test-forms.png"?raw=true alt="result of all tests"></p>

  ### Coverage Report
  <p align="center">
  <img src="static/images/readme-images/test-views.png"?raw=true alt="coverage report"></p>


<p align="right"><a href="#intro">Return to table of contents</a></p><p id="mnts"></p>

# Manual Testing

  ### Lighthouse Test
    - Lighouse report indicated good accesibility, SEO and Best practices scores.

<p align="center">
  <img src="static/images/readme-images/Lighthouse-report.png"?raw=true alt="Lighthouse Report"></p>

  ### HTML validator
    - HTML validation was done using the W3C validator and the some issues were found and subsequently fixed. There is an error which persists in relation to an unclosed ul tag and a trailing p tag which I believe to be related to misinterpreting django syntax when parsing the code for the pages affected.

  <p align="center">
  <img src="static/images/readme-images/homepage-validation.png"?raw=true alt="Validator Testing"></p>

  <p align="center">
  <img src="static/images/readme-images/signup-noerrors.png"?raw=true alt="Validator Testing"></p>

  <p align="center">
  <img src="static/images/readme-images/edit-entry-no-errors.png"?raw=true alt="Validator Testing"></p>

  <p align="center">
  <img src="static/images/readme-images/blog-no-errors.png"?raw=true alt="Validator Testing"></p>

  - These warnings appear for some of the pages in which there are no unclosed ul tags or trailing p tags/div tags. Errors most likely due to misinterpreting django syntax.
  <p align="center">
  <img src="static/images/readme-images/django-syntax-error.png"?raw=true alt="Validator Testing - Django syntax error"></p>

  <p align="center">
  <img src="static/images/readme-images/Odd-errors.png"?raw=true alt="Validator Testing - Django syntax error"></p>

  - Some errors fixed during validation
  <p align="center">
  <img src="static/images/readme-images/Fixing-errors-sign-up.png"?raw=true alt="Validator Testing"></p>

  ### CSS validator
    - The CSS was passed by the validator as valid CSS.

  <p align="center">
  <img src="static/images/readme-images/CSS-validation.png"?raw=true alt="CSS Validator"></p>

  ### Pycodestyle
    - Pycodestyle linter was used in gitpod to test all the python code. The only issues were line too long errors in the original settings.py file and the urls.py file.

  ### User Story Validation/Acceptance Criteria 1
  - User Story to test and validate:

    - As an unregistered user I can have the option to authenticate my email address as an option during sign in

    ### Acceptance Criteria
      - All-auth is implemented correctly.
      - Users can login successfully with allauth.

  ### Validation: 
    - When the user clicks on the signup button in the navbar they are brought to a page to create a new account. During this process they are using the all-auth library. The user can enter their email address and select a suitable password and username. Once the form is submitted the user is taken successfully to the intended redirect url of 'create-new-entry'. The user is presented with a form which they can fill out if they wish to add a new entry to their diary.


### User Story Validation/Acceptance Criteria 2
  - User Story to test and validate:

    - As an unregistered user I can have the option to authenticate myself using my google account as an option during sign in

    ### Acceptance Criteria
      - Users can succesfully login with their google account credentials.

  ### Validation: 
    - When the user is taken to the sign up page they are presented with a link which, if clicked, will bring them to a page that will allow them to use their google account details to set up an account with this website. When they select their account from the google popup window they are redirected to the correcr redirect url and are greeted by their name they use with their google account. Their details are successfully registered within the django admin portal.


<p align="right"><a href="#intro">Return to table of contents</a></p><p id="dep"></p>

# Deployment Guide

  ### Setting up the application before deployment:

  - Install the LTS(Long Term Support) version of Django onto your machine.
  
    > pip3 install 'django<4'
    
  - Install Gunicorn using the command:

    > pip3 install gunicorn
    
      - Gunicorn is a web server that is designed to run Python web applications. It does this by using the WSGI (Web Server Gateway Interface) protocol, which is a standard way for Python web applications to interface with web servers. A web server is a software program that runs on a computer and listens for requests from client computers over the internet. When a request is received, the web server processes the request and sends back a response.
  
  - You will need install the  'dj-database-url' package so can use its parse() function which takes a database URL as an argument. The parse function allows you to specify your database connection settings in your Django project's settings file. The command to install this package is:

    > pip3 install dj_database_url

  - In your settings file you will need to set your database connection:

    > DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
            }

      - The 'DATABASE_URL' in this example is set to a postgres database url in a separate env.py file. This allows you to commit changes to the settings file to GitHub but have sensitive information like Secret Keys and Database Url's kept hidden. The env.py file is then added to the .gitignore file.

  - Install psycopg2 using the following command:

    > pip3 install psycopg2

      - psycopg2 is a PostgreSQL adapter for Python. This allows Python scripts to connect to a PostgreSQL database.
  
  - If your project has image and media requirements then you may want to use Cloudinary to host your files. To install run the following command:

    > pip3 install dj3-cloudinary-storage.

      - dj3-cloudinary-storage is a Django storage backend for the Cloudinary media management service. It allows you to store and serve media files.

  - Create a requirements.txt file:

    > pip3 freeze --local > requirements.txt

      - This will be needed by Heroku to build the needed requirements for the project to run.

  - Create a new Django project:
    > django-admin startproject -project name here.-

  - Create an 'app' (Each app in a django project should handle a specific bit of functionality):

    > python3 manage.py startapp -app name goes here-
  
  - Add app to the installed apps variable in settings.py

    > In the INSTALLED_APPS list:<br> 
      [...,<br>
        'app_name goes here',<br>
        ...]

  - Migrate Changes (These migrations are for the apps that were installed out of the box.)

    > python3 manage.py migrate

  - Run local server and test:

    > python3 manage.py runserver
    
      - If all steps were correctly followed you will see a django congratulations page when you run the server.
  
  - END APPLICATION SET UP.

  ### How to deploy the project to Heroku.

    - Create Heroku app
    - Attatch to the database
    - Prepare settings and environment
    - Set up Cloudinary for static and media file storage.
    - Create some necessary folders and files on the top level directory
<hr>
  - Create a new Heroku App:

      1. Navigate to Heroku dashboard once you have set up an account.<br> 
      2. Choose an app name and a location (Europe or United States).<br>
      3. Add a database to the app resources. Navigate to the resources tab for this, select Add-ons and add 'Heroku PostGres'.
      4. Navigate to settings tab and click on reveal config vars and copy the DATABASE_URL.

  - Attach the database:
      1. Create an env.py file in the top level directory of your workspace.
      2. Within this file, import the os library.
      3. Set the DATABASE_URL to the copied Heroku URL<br>
        - os.environ["DATABASE_URL"]='The copied URL'
      4. Set a SECRET_KEY environment variable
        - os.environ["SECRET_KEY"]='Create your secret key'
      5. Head back to Heroku and add your new SECRET_KEY variable to the config vars.

  - Prepare settings and environment:
      1. Import os and dj_database_url at the top of the settings.py file
      2. Write code to look for env.py file and import it if found. This will be found in local development enviornment only <br>
        - if os.path.isfile('env.py'):<br>
          import env
      3. Overwrite any insecure secret keys in the settings.py file
        - SECRET_KEY = os.environ.get('SECRET_KEY')
      4. Comment out the constant DATABASES which connects the local sql lite database and create a new variable that connects to the Heroku database:
        - <br>DATABASES = {<br>
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))<br>}
      5. Save files and run:
        - python3 manage.py migrate again.

  - Set up Cloudinary for static and media file storage.
      1. Set up an account
      2. Navigate to the dashboard and copy the API Environment variable
      3. Copy this to a CLOUDINARY_URL variable in the env.py file.
        - os.environ['CLOUDINARY_URL']= "paste URL in here"
      4. Add this URL to a the convig vars in Heroku.
      5. Temporarily disable 'collectstatic' in Heroku by creating a constant called DASABLE_COLLECTSTATIC and set its value to 1.
      6. Make sure all Cloundinary libraries are installed in the apps section of the settings file as follows, noting the order:
        - <br>INSTALLED_APPS = [ <br>
          'cloudinary_storage',<br>
          'django.contrib.staticfiles',<br>
          'cloudinary',<br>
          ]
      7. You will also need to tell django where to look for the files:
    
          STATIC_URL = 'The URL prefix for static files in your Django project'

          STATICFILES_STORAGE = 'This specifies the storage backend to use for static files'

          STATICFILES_DIRS = [This is a list of directories where Django will look for static files]

          STATIC_ROOT = os.path.join(
            This is the directory where Django will collect all of the static files from the STATICFILES_DIRS directories. The collected static files will be stored in this directory, and can then be served by a web server.
          )

          MEDIA_URL = 'This is the URL prefix for media files'

          DEFAULT_FILE_STORAGE = 'Name of a backend storage class'
    
      - Some useful links on this topic:

        - [Static files in Django](" https://docs.djangoproject.com/en/3.1/howto/static-files/ ")
        - [Managing static files](" https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-STATICFILES_STORAGE ")
        - [Storage backends](" https://docs.djangoproject.com/en/3.1/ref/files/storage/#module-django.core.files.storage ")

        - [Django storage backend for Cloudinary](" https://github.com/cloudinary/dj3-cloudinary-storage ") 
        - [Integrating Django and Cloudinary - Part 1](" https://cloudinary.com/blog/integrating_django_and_cloudinary_part_1 ")
        - [Integrating Django and Cloudinary - Part 2](" https://cloudinary.com/blog/integrating_django_and_cloudinary_part_2 ")
        - [Cloudinary Django SDK](" https://cloudinary.com/documentation/django_integration")

      8. Link the file to the templates directory in Heroku:
        - TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
      9. Place this variable as the value for the DIRS key in the TEMPLATES list in settings.py
      10. Add Heroku hostname to the ALLOWED HOSTS list in settings.py
        - ALLOWED_HOSTS is a security setting in Django that specifies a list of host/domain names that your Django site is allowed to serve<br>
        It is used to prevent an attacker from using your Django site as a host for phishing attacks.
      
  - Create some necessary folders and files on the top level directory and push changes to GitHub
    1. Create media, static and templates folders in the top level directory
    2. Create a Procfile
      - A Procfile is a text file that is used to specify the commands that are needed to start your application. It is used in web applications that are deployed to a Platform as a Service (PaaS) provider, such as Heroku
    3. In the Procfile type in the command: web: gunicorn PROJ_NAME.wsgi
      - The gunicorn command is used to start the Gunicorn web server
    4. Commit and push all code to git hub
    5. Choose manual or automatic deploys in Heroku under the 'deploy tab'.
    6. Run and test project works when deployed.

  - **SIDENOTE: Early deployment is best with a Django project to avoid complicated errors and issues further into a Project.**
<hr>

  ### Final Deployment

  - Set Debug to False for final deployment and remove commented out local database code.

<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="b"></p>

# Bugs (During Development)

  - Unable to get google authentication to work properly due to the random URI that gitpod generates. I could not get google to recognise the URI but managed a workaround for now. I might clone the project at a later date in VS code and add the full functionality in. At present the {% provider_login_url 'google' %} link will take you to the sign in page which runs the correct login URL on sign up.

  - Difficulty getting the bootstrap header to behave on various screen sizes. Setting the Viewport with to 70vw on the navbarbrand bootstrap class and floating the logo right solved this in the end.

  - Inconsistent migration history. I two seperate instances of messing up the database history.

  - One when we had to switch over to elephant sql for the database. I tried to use the local database to run some tests and when I went back to the deployment database it did not recognise me.

  - Another instance was adding a social account to the database from the admin before I saved the django.contrib.sites to the APPS list in settings.py. I had to wipe the database and start again after making this mistake

<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="ub"></p>

# Bugs (Unsolved)

  - The racetype charfield in the diaryentry model threw a not null exception even though other charfields did not. A value of race remains for the field value. I believe it was due to the fact that this field was added after the database was created. To solve it I might need to clean the database completely and delete the migrations file and re-make new migrations again.


<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="tu"></p>

# Technologies Used

  - Django

  - Python

  - CSS

  - Javascript

  - HTML

  - Bootstrap

  - PostgreSQL

# Libraries/Frameworks and Other Tools Used

  - Balsamiq for wireframes

  - Fiverr Logo maker for logo and favicon

  - GitPod as the IDE

  - Github for version control

  - Django allauth (including social account)

  - Django crispy forms

  - gunicorn

  - Cloudinary

<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="cr"></p>

# Credits

  - Images
    - Pexels.com for most of the images. (Some imagery used in the blog is credited in the blog itself in the comments section)

  - Media
    - The content for the blog is credited in the comments section of each post. 

  - Walkthrough Code from Code Institute for the blog. Only minor style changes were made to the blog code.

  - Tutor Support

    - Help from Sean in Tutor support with the following code on the 16-10-2022:
            <p>
              instance = new_entry.save(commit=False)<br>
              instance.created_by = User.objects.get(username=request.user.username)<br>
              instance.save()
            </p>

    - The code above helped to solve a technical issue whereby I was rendering a form for the user to enter data and I did not want the created_by field to be seen by the user but it was a ForeignKey field and threw a violates not null exception when left blank. This code helped me to create an instance of the new_entry and set its ForeignKey to the users username before committing it to the database thus resolving the error.

  - External Code

    - This code was taken from stack overflow to help with using an anchor tag as a button to avoid nesting one inside the other and causing invalid HTML code.
            <p>
             a.button {<br>
            -webkit-appearance: button;<br>
            -moz-appearance: button;<br>
            appearance: button;<br>
            text-decoration: none;<br>
            color: initial;<br>
            }
            </p>

    - Bootstrap: Used for responsive footer and navbar and its grid layout.
<p align="center">
  <img src=""?raw=true alt=""></p>


