
  <h3 align="center">Food Delivery App</h3>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li>
      <a href="#Notes">Notes</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project



This project is a simple Food Delivery app, it uses Django for backend , docker for deployement , JWT for token authentication, swagger for api documentaion and deployed on Heroku <br>

you can also find this app on Doker-Hub under the name fekrii/food_app:latest

you can run it locally, or with docker-compose or you can check it online on Heroku from this <a href="food-delivery-app22.herokuapp.com/admin">Link</a>


you can check the api swagger documentaion from : <i>swagger\/schema/<i/> either locally or with liveserver <br>
also you can check basic model and views documentaion from : <i>admin\/doc/<i/>






<!-- GETTING STARTED -->
## Getting Started

You can run this app locally or with Docker-compose

### Locally


* create virtual environment, and activate it then install the required packages from requirements.txt file
  ```sh
  pip install -r requirements.txt
  ```

* then run the local server 
  ```sh
  pip manage.py runserver
  ```
 
* then open your local server
  ```sh
  localhost:8000
  ```

#### at local host i used SQL lite DB but in production you can use MYSQL, you will find it's configuration commented in settings.py file

### Using Docker



* first build docker image
  ```sh
  docker-compose build
  ```

* then run the image
  ```sh
  docker-compose up
  ```
  
* then open the server
  ```sh
  localhost:8000
  ```

<!-- Notes -->
## Notes

<ul>
  <li>superuser account is :
    <ul>
      <li>email: admin@mail.com</li>
      <li>password: admin</li>
    </ul>
  </li>
  <li>you will find a postman collection with all the requestes and its bodies</li>
  <li>while testing the api with swagger you must send <i>bearer</i> auth token with the requests</li>
</ul>