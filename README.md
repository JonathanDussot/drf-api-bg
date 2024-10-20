# DRF-API-BG

This is the backend for the *BoardGamers* app, built using Django Rest Framework. *BoardGamers* is a site that has been created solely with the purpose of sharing the passion of playing boardgames. The site allows users to create posts with some of their favourite games and others to give their personal reviews on the game, aswell as a like and/or rating of the game.

You can check the Github for *BoardGamers* by clicking [here](https://github.com/JonathanDussot/boardgamers).

### Live Deployment
- The live link for "BoardGamers" can be found [HERE](https://boardgamers-ci-364d7fb71032.herokuapp.com/)

## Table of Contents
+ [BoardGamers Github (Frontend)](# "BoardGamers")
+ [Live Deployment](#live-deployment "Live Deployment")
+ [User Stories](#user-stories "User Stories")
  + [Profile User stories](#profile "Profile User stories")
  + [Games User stories](#games "Games User stories")
  + [Reviews User stories](#reviews "Reviews User stories")
  + [Likes User stories](#likes "Likes User stories")
  + [Ratings User stories](#ratings "Ratings User stories")
+ [Models used and their datafields](#models-used-and-their-datafields "Models used and their datafields")
  + [Profile Model](#profile-model "Profile Model")
  + [Games Model](#games-model "Games Model")
  + [Reviews Model](#reviews-model "Reviews Model")
  + [Likes Model](#likes-model "Likes Model")
  + [Ratings Model](#ratings-model "Ratings Model")
+ [CRUD Functionality](#crud-functionality "CRUD Functionality")
  + [Profile Data](#profile-data "Profile Data")
  + [Games Data](#games-data "Games Data")
  + [Reviews Data](#reviews-data "Reviews Data")
  + [Likes Data](#likes-data "Likes Data")
  + [Ratings Data](#ratings-data "Ratings Data")
  + [Typography](#typography "Typography")
  + [Imagery](#imagery "Imagery")
+ [Features](#features "Features")
  + [Existing Features](#existing-features "Existing Features")
  + [C.R.U.D](#crud "C.R.U.D")
+ [Testing](#testing "Testing")
  + [Validator Testing](#validator-testing "Validator Testing")
  + [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
+ [Technologies Used](#technologies-used "Technologies Used")
  + [Main Languages Used](#main-languages-used "Main Languages Used")
  + [Frameworks, Libraries & Programs Used](#frameworks-libraries-programs-used "Frameworks, Libraries & Programs Used")
+ [Deployment](#deployment "Deployment")
+ [Credits](#credits "Credits")
  + [Content](#content "Content")
  + [Media](#media "Media")

## User Stories
- Here is a list of all my user stories which can be found in my backend [project](https://github.com/users/JonathanDussot/projects/5)which employs the Agile methodology approach in an organized manner, each with their labels as per MoSCoW prioritization of tasks. ![kanbanboard](images/kanban-board.png)

### Profile

- [x] As a site/admin I can view a list of all created profiles.
- [x] As a site admin I can login and logout so that I can create, edit or delete data.
- [x] As a site admin I can enter a profile so that I can see all profile details.
- [x] As a site admin I can edit and update personal information.
- [x] As a site admin I can Delete a profile from the API.

### Games

- [x] As a site admin I can view a list of games created.
- [x] As a site admin I can create a game with all requested details.
- [x] As a site admin I can open a created game on the list so that I can see all of its details.
- [x] As a site admin I can edit all game details.
- [x] As a site admin I can Delete a game and its information stored in the API

### Reviews

- [x] As a site admin I can view a list of all reviews posted by users.
- [x] As a site admin I can view a single review posted.
- [x] As a site admin I can create a review for a game post.
- [x] As a site admin I can edit the review information.
- [x] As a site admin I can Delete a Review from the API.

### Likes

- [x] As a site admin I can add a like for a games post.
- [x] As a site admin I can edit and change a like saved in the API.
- [x] As a site admin I can remove a like from the API.

### Ratings

- [x] As a site admin I can create a rating for a game post.
- [x] As a site admin I can edit a rating given.
- [x] As a site admin I can delete a rating from the API

## Models used and their datafields

### Profile Model

owner = models.OneToOneField(User, on_delete=models.CASCADE)<br>
created_at = models.DateTimeField(auto_now_add=True)<br>
updated_at = models.DateTimeField(auto_now=True)<br>
name = models.CharField(max_length=255, blank=True)<br>
favourite_game = models.CharField(max_length=255, blank=True)<br>
image = models.ImageField(upload_to='images/', default='../default_profile_yqtpvj')

### Games Model

owner = models.ForeignKey(User, on_delete=models.CASCADE)<br>
title = models.CharField(max_length=255)<br>
description = models.TextField()<br>
designer = models.CharField(max_length=255, blank=True, null=True)<br>
artist = models.CharField(max_length=255, blank=True, null=True)<br>
publisher = models.CharField(max_length=255, blank=True, null=True)<br>
min_players = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])<br>
max_players = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])<br>
solo_play = models.BooleanField(default=False)<br>
image = models.ImageField(upload_to='images/', default='../default_post_ynmksg', blank=True)<br>
genre_filter = models.CharField(max_length=32, choices=genre_filter_choices, default='none')<br>
created_at = models.DateTimeField(auto_now_add=True)<br>
updated_at = models.DateTimeField(auto_now=True)

### Reviews Model

owner = models.ForeignKey(User, on_delete=models.CASCADE)<br>
game = models.ForeignKey(Game, on_delete=models.CASCADE)<br>
created_at = models.DateTimeField(auto_now_add=True)<br>
updated_at = models.DateTimeField(auto_now=True)<br>
content = models.TextField()

### Likes Model

owner = models.ForeignKey(User, on_delete=models.CASCADE)<br>
game = models.ForeignKey(Game, related_name='likes', on_delete=models.CASCADE)<br>
created_at = models.DateTimeField(auto_now_add=True)

### Ratings Model

rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)],default=3,)<br>
game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='ratings')<br>
owner = models.ForeignKey(User, on_delete=models.CASCADE)<br>
created_at = models.DateTimeField(auto_now_add=True)

## CRUD Functionality

- The following images show the full CRUD functionality given to each of the models in the API.

### Profile Data
![Profile Data CRUD](PENDING PHOTO)

### Games Data
![Games Data CRUD](PENDING PHOTO)

### Reviews Data
![Reviews Data CRUD](PENDING PHOTO)

### Likes Data
![Likes Data CRUD](PENDING PHOTO)

### Ratings Data
![Ratings Data CRUD](PENDING PHOTO)




### Features Left to Implement
- This can be found within the *BoardGamers* [README.md file](PENDING)

## Testing

### Validator Testing
| **TEST** | **ACTION** | **EXPECTATION** | **RESULT** |
| ----------------------------- | ----------------------- | --------------------------- | ---------- |
| gems - settings.py | PEP8 validator | [No issues found](static/images-readme/pep8-validator-python.png) | ✅ |
| gems - urls.py | PEP8 validator | No issues found | ✅ |
| blog app - forms.py | PEP8 validator | No issues found | ✅ |
| blog app - models.py | PEP8 validator | No issues found | ✅ |
| blog app - views.py | PEP8 validator | No issues found | ✅ |
| blog app - urls.py | PEP8 validator | No issues found | ✅ |
| blog app - admin.py | PEP8 validator | No issues found | ✅ |
| about app - forms.py | PEP8 validator | No issues found | ✅ |
| about app - models.py | PEP8 validator | No issues found | ✅ |
| about app - views.py | PEP8 validator | No issues found | ✅ |
| about app - urls.py | PEP8 validator | No issues found | ✅ |
| about app - admin.py | PEP8 validator | No issues found | ✅ |
| newsletter app - forms.py | PEP8 validator | No issues found | ✅ |
| newsletter app - models.py | PEP8 validator | No issues found | ✅ |
| newsletter app - views.py | PEP8 validator | No issues found | ✅ |
| newsletter app - urls.py | PEP8 validator | No issues found | ✅ |
| newsletter app - admin.py | PEP8 validator | No issues found | ✅ |
| resources app - forms.py | PEP8 validator | No issues found | ✅ |
| resources app - models.py | PEP8 validator | No issues found | ✅ |
| resources app - views.py | PEP8 validator | No issues found | ✅ |
| resources app - urls.py | PEP8 validator | No issues found | ✅ |
| resources app - admin.py | PEP8 validator | No issues found | ✅ |
| style.css | [W3C - Jigsaw](https://jigsaw.w3.org/css-validator/) validator | [No issues found](static/images-readme/w3c-validator-css.png) | ✅ |
| Home page - html | [W3C](https://validator.w3.org/) validator - source code | [No issues found](static/images-readme/w3c-validator-html.png) | ✅ |
| About page - html | W3C validator - source code | No issues found | ✅ |
| Post Details page - html | W3C validator - source code | No issues found | ✅ |
| Resources page - html | W3C validator - source code | No issues found | ✅ |
| Newsletter page - html | W3C validator - source code | No issues found | ✅ |
| Sign-in page - html | W3C validator - source code | No issues found | ✅ |
| Home page - html | lighthouse | [Acceptable scores](static/images-readme/lighthouse.png) | ✅ |
| About page - html | lighthouse | Acceptable scores | ✅ |
| Post-Details page - html | lighthouse | Acceptable scores | ✅ |
| Resources page - html | lighthouse | Acceptable scores | ✅ |
| Newsletter page - html | lighthouse | Acceptable scores | ✅ |
| Sign-in page - html | lighthouse | Acceptable scores | ✅ |
| WAVE results | WAVE | [Acceptable scores](static/images-readme/wave.png) | ✅ |
| Microsoft Edge browser | Launch site | Site opens without issue | ✅ |
| Google Chrome browser | Launch site | Site opens without issue | ✅ |

### Responsiveness testing

| **TEST**                      | **ACTION**              | **EXPECTATION**             | **RESULT** |
| ----------------------------- | ----------------------- | --------------------------- | ---------- |
| Home page - responsiveness    | Size site down to 320px | all elements stay on screen | ✅         |
| Home page - responsiveness    | Size site up to 1920px  | all elements stay on screen | ✅         |
| About page - responsiveness   | Size site down to 320px | all elements stay on screen | ✅         |
| About page - responsiveness   | Size site up to 1920px  | all elements stay on screen | ✅         |
| Post-Details page - responsiveness  | Size site down to 320px | all elements stay on screen | ✅         |
| Post-Details page - responsiveness  | Size site up to 1920px  | all elements stay on screen | ✅         |
| Resources page - responsiveness    | Size site down to 320px | all elements stay on screen | ✅         |
| Resources page - responsiveness    | Size site up to 1920px  | all elements stay on screen | ✅         |
| Newsletter page - responsiveness   | Size site up to 1920px  | all elements stay on screen | ✅         |
| Newsletter page - responsiveness   | Size site up to 1920px  | all elements stay on screen | ✅         |
| Sign-in page - responsiveness | Size site down to 320px | all elements stay on screen | ✅         |
| Sign-in page - responsiveness | Size site up to 1920px  | all elements stay on screen | ✅         |

### C.R.U.D. testing

| **TEST**          | **ACTION**             | **EXPECTATION**          | **RESULT** |
| ----------------- | ---------------------- | ------------------------ | ---------- |
| Newsletter subscription - Create     | Add new instance to DB | Instance created         | ✅         |
| Newsletter subscription - Read       | Retrieve all instances | Instances visible in UI  | ✅         |
| Newsletter subscription - Update     | Modify an instance     | Mods saved & visible     | ✅         |
| Newsletter subscription - Delete     | Delete an instance     | Instance removed from UI | ✅         |
| Comments - Create | Add new instance to DB | Instance created         | ✅         |
| Comments - Read   | Retrieve all instances | Instances visible in UI  | ✅         |
| Comments - Update | Add new instance to DB | Mods saved & visible     | ✅         |
| Comments - Delete   | Retrieve all instances | Instance removed from UI | ✅         |
| Like - Create | Add new instance to DB | Instance created         | ✅         |
| Like - Delete | Delete an instance     | Instance removed from UI | ✅         |

### FEATURES

| **TEST**                      | **ACTION**             | **EXPECTATION**                                           | **RESULT** |
| ----------------------------- | ---------------------- | --------------------------------------------------------- | ---------- |
| Navigation bar                | Click on nav link      | user routed to correct page                               | ✅         |
| Footer links                  | Click on footer links  | user routed to new browser tab                            | ✅         |
| Like button                   | Click "like"           | Post liked/unliked accordingly                            | ✅         |
| Comment section                   | Written empty message           | does not submit, prompts to write a message                            | ✅         |
| Comment section                   | Write message and submit           | user informed on pending approval                            | ✅         |
| Edit button                   | Click edit button      | user allowed to edit comment only if previously approved                             | ✅         |
| Delete button                 | Click delete button    | user allowed to delete comment only if previously approved                                | ✅         |
| Collaboration form                | Submit form    | user alerted on successful form                                | ✅         |
| External links in Resources                | Click link             | User routed to appropriate webpage                           | ✅         |
| Subscription                | enter invalid email             | User prompted to write a valid email                           | ✅         |
| Subscription CRUD buttons                | Click buttons            | User routed to appropriate page and UI updated                    | ✅         |
| Login                         | User logs in           | UI updates & user is logged in                            | ✅         |
| Sign up                       | User signs up          | new account created for the user                          | ✅         |
| Logout                        | User clicks logout     | UI updates, user is logged out, user cannot create a post | ✅         |

### BUG TESTING:
1. Heroku logs--tail error when deploying to Heroku:
 - Added correctly-written web: gunicorn gems.wsgi to ProcFile to link it correctly.

2. 'unexpected chunk number 1 (expected 0)' error:
 - This was caused be corrupted Data upon using loaddata with json.file according to Tutor Support.
 - Uncommented sqlite database and commented out external database to temporarily work on project before eventually providing a solution (mentioned in bug #3)

3. Opening new external Database:
 - Did pip install and pip freeze with all requirements, created env.py file, added new DB URL and secret key, collectstatic, updated CSRF, did makemigrations and migrate command and yet page would not load correctly.
 - The cloudinary URL was missing within the env.py, this allowed the page to load correctly.

4. CSS styles would not load:
 - Upon using terminal command to copy staticfiles into a template folder, accidently created and nested everything within an additional templates folder so url path did not connect.
 - Moved everything out to the correct template folder and css styles were loading correctly.

5. Admin interface content lacked RichText Editor for content fields in resources app:
 - summernote_fields was not correctly linked to content containers within the admin.py file.

6. Likes generated an error:
 - within the blog's models.py the model's related name for the like button clashed with the comment section, I changed the name so code could correctly distinguish model and this fixed the bug.

7. Validator error message <o:p>:
 - This was due to my population of the content fields having used my microsoft word to draft the tet before adding them to the admin interface, could not be seen in my code.
 - Manually accessed and edited code from Admin interface and deleted the tags.

8. Page would break when screen size was below 768px and only provide images:
 - Deleted 'flex: no-wrap' to fix this issue and correctly display text with the images so users can access post details for each post.

9. Editing a comment while awaiting approval:
 - Page would crash is user were to click on the edit button before comment had been approved.
 - Fixed the issue by removing the edit button for comments awaiting approval.

10. Navbar overflow:
 - Navbar displayed overflow off page between 1150px and 990px on all pages.
 - Reduced the logo size, nav-link size and text-muted size so elements would not cause navbar to overflow before collapsing as media response styles take effect.

11. Like button with a reverse path error:
 - Upon correcting some of the hyphens and underscores, the blog's urls.py path had the correct pattern, but the views.py file still had **'post-detail'** instead of **post_detail** within the reverse function call.

### Unfixed Bugs
1. Sign up form - HTML Validator errors:
- Upon validating, I noticed [4 errors with tags](static/images-readme/signup-html-errors.png) which were nowhere to be found within my code.
- With help from Tutor Support, we determined this was from Django's Allauth's error and that I could do nothing to fix it from my end.

## Technologies Used
### Main Languages Used
- Python

### Frameworks, Libraries & Programs Used
- [Google Fonts](https://fonts.google.com/) - for the font families: 
- [Font Awesome](fontawesome.com) - for the page icons.
- [GitPod](https://www.gitpod.io/) - for creating python files.
- [GitHub](https://github.com/) - to store my repository for submission.
- Google Dev tools - to test and fix issues detected.
- [Heroku](https://id.heroku.com/login) - for live deployments.
- [Pexels](https://www.pexels.com/) to use free images for signup/signin image.
- [iconos8](https://iconos8.es/) to get favicon for my site.
- [Balsamiq](https://balsamiq.com/) - for the wireframe mockups of my webpage.
- [Am I Responsive?](https://ui.dev/amiresponsive) - to ensure the webpage displayed well on all devices.
- [Tiny PNG](https://tinypng.com/) to compress images.
- [FreeLogoDesign](https://app.freelogodesign.org/)
- [Colormind.io](http://colormind.io/) to generate color palette used. 
- [cdnjs](https://cdnjs.com/libraries/bootstrap) for bootstrap.
- Django
- Bootstrap

### Installed Packages:
- asgiref==3.3.4
- cloudinary==1.25.0
- cryptography==3.4.8
- dj-database-url==0.5.0
- dj-rest-auth==2.1.9
- Django==3.2.4
- django-allauth==0.50.0
- django-cloudinary-storage==0.3.0
- django-cors-headers==3.7.0
- django-filter==2.4.0
- djangorestframework==3.12.4
- djangorestframework-simplejwt==4.7.2
- gunicorn==20.1.0
- oauthlib==3.1.1
- Pillow==8.2.0
- psycopg2==2.9.9
- PyJWT==2.1.0
- python3-openid==3.2.0
- pytz==2021.1
- requests-oauthlib==1.3.0
- sqlparse==0.4.1
- urllib3==1.26.18

## Deployment

### Heroku

This site is deployed using Heroku and all the steps for a success deployment are on the following:

1. Create a list of requirements in the requirements.txt file by using the command _pip3 freeze > requirements.txt_.
2. Log in (or sign up) to Heroku.
3. Click on the _New_ button and select _Create new app_.
4. Give it a unique name and choose the region.
5. Click the Settings tab, go to the _Config Vars_ section and click on the _Reveal Config Vars_ button.
6. Add all variables from env.py to _ConfigVars_ of Heroku.
7. Click the _Add_ button.
8. Click the Deploy tab, go to the _Deployment method_ section, select _GitHub_ and confirm this selection by clicking on the _Connect to Github_ button.
9. Search for the repository name on github and click the _Connect_ button.
10. Add in the setting.py the Heroku app URL into ALLOWED HOSTS.
11. Gather all static files of the project by using the command _python3 manage.py collectstatic_ in the terminal.
12. Make sure that DEBUG=FALSE in settings.py.
13. Create a _Procfile_ in the root directory and add web: gunicorn fv_api.wsgi.
13. In Heroku enable the automatic deploy or manually deploy the code from the main branch.

### Local deployment

1. Generate an env.py file in the root directory of the project.
2. Configure the environment variables within this file.
3. Create a virtual environment, if neccessary.
4. Install all required dependencies using _pip install_ command (into the .venv).
5. Add dependencies to the requirements.txt file using _pip3 freeze > requirements.txt_ command.

### Forking this GitHub repository
1.  Log in to GitHub.
2.  Navigate to the repository for this project by selecting [drf-api-bg](https://github.com/JonathanDussot/drf-api-bg)
3. Click at the top of the repository on the **Fork** button on the right side

### Clone this repository
1. Log in to GitHub.
2. Navigate to the repository for this project by selecting [drf-api-bg](https://github.com/JonathanDussot/drf-api-bg)
3. In the top-right corner, click on the green *Code* button
4. Copy the HTTPS URL in the tab *Local*
5. Go to the code editor of your choice and open the terminal
5. Type `git clone` and paste the URL you copied into your terminal
6. Press the enter key

### Cloudinary
1. Navigate to [Cloudinary](https://cloudinary.com/)
2. Sign up or log in to account
3. Go to the dashboard
4. Click on _Go to API Keys_ button
5. Generate a new API Key
6. Provide the API environment variable in format: *CLOUDINARY_URL=cloudinary://<your_api_key>:<your_api_secret>@dzzfvef0g* in _env.py_ and _Config Vars_
7. Update settings.py

### Create PostgreSQL using Code Institute Database Maker
1. [CI Database Maker](https://dbs.ci-dbs.net/)
2. Input your email address
3. Paste the provided URL in as your DATABASE_URL value

## Credits

### Code and images

- The original setup for this API was provided mainly with the guidance from the Moments Walkthrough project which help me grasp the necessary information I needed in order to then customize my models and experiment with features I wanted to add myself to make this my unique project.

- The following websites were used as a source of knowledge: <br>
  - [Google](www.google.com)
  - [Stack Overflow](https://stackoverflow.com/)
  - [W3C](https://www.w3.org/)
  - [W3schools](https://www.w3schools.com/)
  - [DevDocs](https://devdocs.io/)
  - [Atlassian](https://www.atlassian.com/)
  - [forum djangoproject](https://forum.djangoproject.com/)
  - [Django](https://www.djangoproject.com/), [Django Rest Framework]((https://www.django-rest-framework.org/)), [Cloudinary](https://cloudinary.com/documentation)
  - Slack Community

### Acknowledgements

- I would like to thank the tutors and my mentor at Code Institute for continuously offering me support throughout this journey and helping me to learn so much.