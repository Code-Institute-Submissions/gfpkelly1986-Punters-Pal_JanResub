# Punters Pal - A diary structred for, and aimed at, the Horse-Racing Community.

  <p align="center">
  <img src=""?raw=true alt=""></p>

# <p href="#intro" id="intro"> - Intended Purpose of This Website:</p>

  - Fill in: What the purpose of the website is.

  - Fill in: What the purpose of the website is.

  - Fill in: What the purpose of the website is.

  - Fill in: What the purpose of the website is.


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
- <a href="#tpy">Testing(Python)</a>
- <a href="#tjs">Testing(Javascript)</a>
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

   - Users can login successfully with an email address.

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

  - Fonts

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

  - Live Features

<p align="center">
  <img src=""?raw=true alt=""></p>


<p align="right"><a href="#intro">Return to table of contents</a></p><p id="df"></p>

# Desired Features

  - Desired Features

<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="tpy"></p>

# Testing (Python)

  - Unit-Testing-Python

<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="tjs"></p>

# Testing (JavaScript)

  - Unit-Testing-JavaScript

<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="dep"></p>

# Deployment

  - Early Deployment

  - Final Deployment

<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="b"></p>

# Bugs (During Development)

  - Bug One

  - Bug Two

<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="ub"></p>

# Bugs (Unsolved)

  - Bug One

  - Bug Two

<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="tu"></p>

# Technologies Used

  - Tech One

  - Tech Two

<p align="center">
  <img src=""?raw=true alt=""></p>

<p align="right"><a href="#intro">Return to table of contents</a></p><p id="tu"></p>

# Credits

  - Images

  - Media

  - Walkthrough Code
  
  - External Code

<p align="center">
  <img src=""?raw=true alt=""></p>


