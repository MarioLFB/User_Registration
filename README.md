# Real-Time Weather Forecast

- Real-Time Weather Forecast is an application created in Python and deployed through Heroku. It was designed to provide users with real-time information about the weather conditions in their chosen city, including the current temperature, as well as the maximum and minimum temperatures for the current day, along with the sunrise and sunset times.

[Link to the website](https://authentication19-5b29c2e044bf.herokuapp.com/)

![An image previewing all devices](assets/screenshots/ps_authentication19.png)

## Contents
- [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Manual](#user-manual)
- [User Stories](#user-stories)
    - [Users](#users)
    - [Site Owner](#site-owner)
- [Teachnical Design](#technical-design)
    - [Flowchart](#flowchart)
- [Technology Used](#technology-used)
    - [Language used](#language-used)
    -[Python Libraries used](#python-libraries-used)
    - [Other websites/tools used](#other-websitestools-used)
    - [3rd Party Python Libraries used](#3rd-party-python-libraries-used)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Features to be implemented](#features-to-be-implemented)
- [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Tested Devices with Browsers](#tested-devices-with-browsers)
    - [Validator Testing](#validator-testing)
    - [Bugs and Fixes](#bugs-and-fixes)
    - [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
    - [Deploying in Heroku](#deploying-the-website-in-heroko)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Cloning of Repository i GitHub](#cloning-the-repository-in-github)
- [Credits](#credits)
    - [Content](#content)
    - [Code](#code)
- [Thank You](#thank-you)

## Project Goals
### User Stories

- Create a login as a new user.
- Log in as a user.
- The user selects the city to be consulted
- Check the current weather forecast.
- Check minimum and maximum temperatures.
- Check the sunrise and sunset times for the current day.
- Users can access the application again at any time.

## User Experience
### Target Audience

- The application can be accessed by any and all types of users.
- The application does not contain any sensitive information for any age group.

### User Requirements and Expectations

- Secure and fast user registration and login
- Quick access to weather forecast information
- Easy navigation through the application
- Quick and optimized information

### User Manual
<details><summary>Click here to view instructions</summary>

#### Home Screen

- Upon launching the app, you will be greeted with the home screen, displaying the options for "Register", "Login", and "Exit".
- Operation: Choose an option by typing "1" for Register, "2" for Login, or "3" to Exit.

#### Registration

- If you are a new user, select "1" to register.
- You will be prompted to enter how you wish to be called and choose a 6-digit password.
- After registration, you will be directed to login.

#### Login

- If you are already a registered user, select "2" at the home screen to log in.
- Enter your name and password.
- Once your credentials are verified, you will be directed to the main menu of the app.

#### Main Menu

In the main menu, you will have the following options:
"1 - Check the weather"
"2 - Check the temperature"
"3 - Check sunrise and sunset times"
"4 - Exit"
Choose the desired option by typing the corresponding number.

#### Checking the Weather

- After choosing to check the weather, temperature, or sunrise and sunset times, you will be prompted to enter the name of the city.
- The weather information for the chosen city will be displayed.
- After viewing the information, you can choose to return to the main menu or exit the application.

#### Exiting the App

- To exit the application at any time, select the exit option in the menu you are in.
- A farewell message will be displayed.

</details>

## User Stories

### Users

1. As a user, I want to have the option to login or register a new account. 
2. As a user, I want to have my data saved.
3. As a user, I want to access the main menu after logging in.
4. As a user, I want to have access to weather search options.
5. As a user, I want to choose the city to get the desired information.
6. As a user, I want to have the option to return to the menu and perform more searches.
7. As a user, I want to exit the application once I finish my searches.

### Site Owner

8. As the site owner, I want users to have quick access to the login and user registration area.
9. As the site owner, I want users names and passwords to be securely stored.
10. As the site owner, I want users to receive clear error messages in case of incorrect inputs.
11. As the site owner, I want users to have a positive experience by providing accurate, up-to-date weather information.
12. As the site owner, I want users to make multiple searches, constantly returning to the main menu.

### Returning User

13. As a returning user, I want to log in without the need for new registration, to quickly access my account.
14. As a returning user, I want to have real-time information available on all accesses to the application, ensuring that weather forecasts are always up to date.
15. As a returning user, I want to quickly access the necessary information and exit the application quickly.

## Technical Design

## FlowChart
- [Lucidchart](https://www.lucidchart.com) was used to build flowchart

<details>
    <summary>Flowchart</summary>
    <p>Real-Time Weather Forecast</p>
    <img src = "assets\screenshots\weather_forecast.png" alt = "A screenshot of flowchart">
</details>

## Technology Used
### Language Used

- Python

### Python Libraries used

- import json - Imports the JSON module, allowing manipulation of JSON data.
- import getpass - Imports the getpass module, which prompts the user for a password without echoing it.
- import os - Imports the os module, which provides a portable way of using operating system-dependent functionality.
- import time - Imports the time module, providing functions for working with time, such as delays and timestamps.

### Other websites/tools used

- [Lucidchart](https://www.lucidchart.com) was used to build flowchart
- [GitHub](https://github.com/) was used for saving and storing files.
- [VS Code](https://code.visualstudio.com/) was used for writing code.
- [Heroku](https://www.heroku.com/) was used as the deploying platform for this site.

### 3rd Party Python Libraries used

- Weather API - It is an interface that provides access to weather data from various sources such as meteorological organizations or weather stations. It typically allows developers to retrieve current weather conditions, forecasts, and historical data for specific locations. This data can be utilized in applications ranging from weather forecasting services to travel and event planning, enhancing user experience and decision-making processes.
[Weather API](https://openweathermap.org/api)

## Features
Consists of an application with 15 features.

### Home page display

- Welcome message and the user registration/login area.
On the initial page displayed, the first message is "Welcome to Real-Time Weather Forecast," followed by options for user registration, login, and exit.
This area display an instruction for signup for new users
- User stories covered: 1, 8 and 13
<details><summary>Image Logo and Main Text Slogan</summary>
<img src="assets\screenshots\login_area.png">
</details>

### Option 1 -  Register

- Registration Process
The user receives instructions to register a username and password.
The password input undergoes the getpass treatment and is not displayed on the screen for security reasons.
Once meeting the registration standards, the user returns to the login area followed by the message, "Thank you, Code! Registration successfully completed!" followed by the available options:
1 - Return to the menu; 2 - Login; 3 - Exit.
- User stories covered: 1, 2 and 8
<details><summary>Register</summary>
<img src="assets\screenshots\register.png">
<img src="assets\screenshots\register2.png">
</details>

### Option 2 -  Login

- The user is instructed to enter their name and then the password. If the login is successful, the user gains access to the main page of the app. If the login is invalid, a message "Invalid name or password" is displayed, prompting the user to try logging in again.
- User stories covered: 3, 8, 10 and 13
<details><summary>Login</summary>
<img src="assets\screenshots\login.png">
<img src="assets\screenshots\login2.png">
</details>

### Data Security

- User data is saved in a separate .json data file and protected within the .gitignore.
- User stories covered: 2 and 9
<details><summary>Data Security</summary>
<img src="assets\screenshots\security.png">
</details>

### Main Page - Weather Information

- Right after logging in, the user accesses the main page with the options: 1 - Check the weather; 2 - Check the temperature; 3 - Check the sunrise and sunset times; 4 - Exit
The user is asked to choose an option.
If an invalid option is chosen, the user will receive the message "Invalid Option" and will be prompted to choose the correct option again.
- User stories covered: 3, 4, 7, 14 and 15
<details><summary>Main Page - Weather Information</summary>
<img src="assets\screenshots\main_page.png">
</details>