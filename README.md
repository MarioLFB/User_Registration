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
4. As a user, I want to have access to Real Time search options.
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

### Register

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

### Login

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

### Check the weather

- It's the first option on the main page. After selecting this option, the user is prompted to choose the city they want to receive information about. If the city is valid, real-time weather condition information is returned.
 If the city is invalid, the user receives the message "City not found" and is taken back to the main screen.
 After conducting the search, the user is given the option to "Return to the menu" for further searches or "Exit" to leave the program immediately.
 - User stories covered: 4, 5, 6, 7, 10, 11, 12, 14 and 15
 <details><summary>Check the weather</summary>
<img src="assets\screenshots\weather.png">
<img src="assets\screenshots\weather2.png">
</details>

### Check the temperature

- It's the second option on the main page. After selecting this option, the user is prompted to choose the city they want to receive information about. If the city is valid, real-time temperature information is returned.
If the city is invalid, the user receives the message "City not found" and is taken back to the main screen.
 After conducting the search, the user is given the option to "Return to the menu" for further searches or "Exit" to leave the program immediately.
 - User stories covered: 4, 5, 6, 7, 10, 11, 12, 14 and 15  
  <details><summary>Check the temperature</summary>
<img src="assets\screenshots\temperature.png">
<img src="assets\screenshots\temperature2.png">
</details>

### Check the sunrise and sunset times

- t's the third option on the main page. After selecting this option, the user is prompted to choose the city they want to receive information about. If the city is valid, real-time sunrise and sunset times information is returned.
If the city is invalid, the user receives the message "City not found" and is taken back to the main screen.
 After conducting the search, the user is given the option to "Return to the menu" for further searches or "Exit" to leave the program immediately.
 - User stories covered: 4, 5, 6, 7, 10, 11, 12, 14 and 15  
  <details><summary>Check the sunrise and sunset times</summary>
<img src="assets\screenshots\sunrise_sunset.png">
<img src="assets\screenshots\sunrise_sunset2.png">
</details>

## Testing
- Manual assessment of user stories
- Browser compatibility testing
- Validation testing

# Manual assessment
<details><summary>User stories assessments</summary>

1. User accesses the home screen with the options: 1 - Register; 2 - Login; 3 - Exit.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Home display | Type 1, 2 or 3 | 1: Register / 2: Login / 3: Exit | Works as expected
<details>
    <summary>Screenshot</summary>
    <p>Home display</p>
    <img src="assets\screenshots\manual_main_page.png" alt="Home display">
</details> 

2. Option 1 -  Register: The user is prompted to enter their name (How would you like to be called?) and is invited to choose a 6-digit password (Choose a password with 6 digits:).
If the registration is valid, they are directed to the login screen with the message (Thank You {name}! Registration successfully completed!).
If the registration is invalid, they receive the message (Name already registered).

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Register | Type Name and Password | Registration successfully completed! or Name already registered  | Works as expected
<details>
    <summary>Screenshot</summary>
    <p>Register</p>
    <img src="assets\screenshots\manual_register.png" alt="Register 1">
    <img src="assets\screenshots\manual_register2.png" alt="Register 2">
    <img src="assets\screenshots\manual_register3.png" alt="Register 3">
</details> 

3. Option 2 -  Login: The user is prompted to enter their name (Enter your name:) and is invited to enter their password (Enter your password:).
If the login is valid, the user receives the message (Login successfully completed!).
If the login is invalid, the user receives the message (Invalid name or password) and returns to the input to enter their name again.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Login | Type Name and Password | Login successfully completed! or Invalid name or password  | Works as expected
<details>
    <summary>Screenshot</summary>
    <p>Login</p>
    <img src="assets\screenshots\manual_login.png" alt="Login 1">
    <img src="assets\screenshots\manual_login2.png" alt="Login 2">
</details> 

4. Option 3 -  Exit: The user promptly leaves the application and receives the message (Goodbye!).

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Exit |  Type option 3 | leaves the application  | Works as expected
<details>
    <summary>Screenshot</summary>
    <p>Exit</p>
    <img src="assets\screenshots\manual_exit.png" alt="Exit">
</details>

5. User accesses the Main screen with the the options: 1 - Check the weather; 2 - Check the temperature; 3 - Check the sunrise and sunset times; 4 - Exit.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Main screen | Type 1, 2, 3 or 4 | 1: Check the weather / 2: Check the temperature / 3: Check the sunrise and sunset times / 4: Exit | Works as expected
<details>
    <summary>Screenshot</summary>
    <p>Main screen</p>
    <img src="assets\screenshots\manual_main_screen.png" alt="Main Screen">
</details>

6. Option 1 - Check the weather. User types option 1; User receives the prompt to enter the desired city (Enter the city:); User receives information about the weather condition (The sky in {city} is currently {weather}); the following options are presented: 1 - Return to the menu or 2 - Exit.
If the city is invalid, the user receives an error message (City not found!) and is prompted again to enter the city.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Check the weather | Type Option 1 and City | receives information or City not found! Message | Works as expected
<details>
    <summary>Screenshot</summary>
    <p>Check the weather</p>
    <img src="assets\screenshots\manual_weather.png" alt="Check the weather">
    <img src="assets\screenshots\manual_weather_error.png" alt="Check the weather error">
</details>

7. Option 2 - Check the temperature. User types option 2; User receives the prompt to enter the desired city (Enter the city:); User receives information about the temperature (Dude, it's like {temperature}°C in {city} right now. It's hitting up to {temperature}°C and falling to {temperature}°C in {city}. It feels like {temperature}°C in {city}.); the following options are presented: 1 - Return to the menu or 2 - Exit.
If the city is invalid, the user receives an error message (City not found!) and is prompted again to enter the city.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Check the temperature | Type Option 2 and City | receives information or City not found! Message | Works as expected
<details>
    <summary>Screenshot</summary>
    <p>Check the temperature</p>
    <img src="assets\screenshots\manual_temperature.png" alt="Check the temperature">
</details>

8. Option 3 - Check the sunrise and sunset times. User types option 3; User receives the prompt to enter the desired city (Enter the city:); User receives information about the sunrise and sunset times (In {city}, the sunrise time is {time} and the sunset time is {time}.); the following options are presented: 1 - Return to the menu or 2 - Exit.
If the city is invalid, the user receives an error message (City not found!) and is prompted again to enter the city.

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Check the sunrise and sunset times | Type Option 3 and City | receives information or City not found! Message | Works as expected
<details>
    <summary>Screenshot</summary>
    <p>Check the sunrise and sunset times</p>
    <img src="assets\screenshots\manual_sunrise_sunset.png" alt="Check the sunrise and sunset times">
</details>

9. Option 4 -  Exit: The user promptly leaves the application and receives the message (Goodbye!).

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Exit |  Type option 4 | leaves the application  | Works as expected
<details>
    <summary>Screenshot</summary>
    <p>Exit</p>
    <img src="assets\screenshots\manual_main_exit.png" alt="Exit">
</details>

### Testing on Browsers
- I conducted trials to ensure compatibility of this game across various browsers such as Chrome and Firefox, and subsequently managed to execute the deployment without any issues.

### Validator Testing
#### PEP8 Python Validator
[PEP8 Python Validator](https://pep8ci.herokuapp.com/) was used to validate the code.

This validator was provided by Code Institute.

No errors were found.

<details>
    <summary>run.py</summary>
    <p>Result: run.py</p>
    <img src = "assets\screenshots\pep8ci_run.png" alt = "A screenshot of run.py result">
</details>

<details>
    <summary>weather.py</summary>
    <p>Result: weather.py</p>
    <img src = "assets\screenshots\pep8ci_weather.png" alt = "A screenshot of weather.py result">
</details>

### Bugs and Fixes

| **Bugs** | **Fixes** |
| ------- | ------- |
| The "Exit" option lacks a return message to the user | Add a goodbye message for all program exits| commit d619308
| Double space in: print(f"The sky in {city} is all like") | Remove double spacing | commit b0fcd9d

### Unfixed Bugs

- No unfixed bugs

## Deployment

## Deployment & Local Development
The website was deployed to [Heroku](https://id.heroku.com/) using the following process:
1. Login or create an account at [Heroku](https://dashboard.heroku.com/)
<img src="assets\screenshots\heroku_login.png">

2. Begin by navigating to the top right of the screen and clicking on "New" followed by "Create new app."
<img src="assets\screenshots\heroku_create_app.png">

3. Provide a name for your app and specify its location, then proceed by clicking on 'create app'.
<img src="">

4. On the subsequent page, head to the deploy tab and opt for connecting to GitHub.
4.1. Upon prompt, log into your GitHub account.
<img src="">

5. Choose the repository you wish to link with your Heroku app.
<img src="">

6. Access the settings tab.
<img src="">

7. Locate the config vars section and ensure the Key is set to "PORT" with the Value being "8000".
<img src="">

8. After configuring the vars, move down to the buildpacks section (still within settings).
8.1. Add the Python and Node.js buildpacks to your app, maintaining the order: Python followed by Node.js.
<img src="">

9. Return to the settings tab.
9.1. Enable automatic deploys to allow Heroku to incorporate new changes from GitHub each time they're pushed.
<img src="">

10. Verify that in the 'manual deploy' section, the branch selected is 'main', then proceed to deploy the branch.
<img src="">




This repository can be forked using the following process:
1. On the repository's page, go to the top-right of the page underneath the dark ribbon.
1. Click on the fork button
1. You can now work on a fork of this project. 

This repository can be cloned using the following process:
1. Go to this repository's page on GitHub.
1. Click on the code button (not the one in the navbar, but the one right above the file list).
1. Select an option, HTTPS, SSH, GitHub CLI.
1. Copy the url below to your clipboard.
1. Open Git Bash/your IDE terminal.
1. Ensure the directory you are working in is the correct one you want to paste the project into.
1. Type the command '$ git clone'
1. Paste the URL of the repository after this.
1. Hit enter on your keyboard and the project will be cloned.