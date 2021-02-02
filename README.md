# Bona Blog
An Open-Source Web Blogging platform.



[![GitHub license](https://img.shields.io/github/license/Williano/Bona-Blog?style=for-the-badge)](https://img.shields.io/github/license/Williano/Bona-Blog?style=for-the-badge)
[![GitHub stars](https://img.shields.io/github/stars/Williano/Bona-Blog?style=for-the-badge)](https://img.shields.io/github/stars/Williano/Bona-Blog?style=for-the-badge)
[![GitHub forks](https://img.shields.io/github/forks/Williano/Bona-Blog?style=for-the-badge)](https://img.shields.io/github/forks/Williano/Bona-Blog?style=for-the-badge)
[![GitHub issues](https://img.shields.io/github/issues/Williano/Bona-Blog?style=for-the-badge)](https://img.shields.io/github/issues/Williano/Bona-Blog?style=for-the-badge)


## Table of contents
* [General info](#general-info)
* [Django Package or App](#django-package-or-app)
* [Screenshots](#screenshots)
* [Features](#features)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)
* [License](#license)
* [Contributing](#contributing)


## General info
An Open-Source blogging platform like [Medium](https://medium.com/) and [Real Python](https://realpython.com/) built with Python and Django. It has [features](#features) of a standard blogging platform.

## Django Package or App
This project has been converted into a django package. You can install it from [PyPI](https://pypi.org/project/django-bona-blog/) or its [GitHub Repo](https://github.com/Williano/django-bona-blog).

## Screenshots

 Authors Dashboard Page
:-------------------------:
![Screenshot_2020-06-25 Bona Dashboard Home](https://user-images.githubusercontent.com/19711677/85830207-d4e17200-b751-11ea-9de2-0a86b5bd296a.png)

 Create Article Page
:-------------------------:
![Screenshot_2020-06-26 Bona Dashboard Create Article(2)](https://user-images.githubusercontent.com/19711677/85830197-d1e68180-b751-11ea-9a10-9653fc0c1a9d.png)


Authors Profile Details Page
:-------------------------:
![Screenshot_2020-06-25 Bona Dashboard Profile Details](https://user-images.githubusercontent.com/19711677/85830204-d317ae80-b751-11ea-86ff-c7b5683ffea5.png)


Home Page            |  List of Categories Page
:-------------------------:|:-------------------------:
![Home](https://user-images.githubusercontent.com/19711677/56363189-264fb200-61db-11e9-9bba-77a3e7f7c1de.jpg) | ![Categories List](https://user-images.githubusercontent.com/19711677/56363187-264fb200-61db-11e9-8a90-0af49eb33758.jpg)

Category Articles List Page       |  Author Articles List Page
:-------------------------:|:-------------------------:
![Category Article List](https://user-images.githubusercontent.com/19711677/56363188-264fb200-61db-11e9-8fef-fc83fb29f056.png) | ![Author Articles](https://user-images.githubusercontent.com/19711677/56363185-25b71b80-61db-11e9-9a42-2fffaa369d28.jpg)

Article Detail Page 
:-------------------------:
![Screenshot_2020-11-22 BONA Django CKEditor installation Testing](https://user-images.githubusercontent.com/19711677/99898873-a0bf9e00-2c6a-11eb-8e4a-8e24af9dce94.jpg)
 


## Features

* [Mobile App Version](https://github.com/Williano/Bona-Blog-Mobile)
* Dashboard for Authors
* WYSIWYG Editor
* Account Verification
* Author Login
* Author Password Reset
* API for Clients
* Category List
* Category Articles List
* New Category Submission
* Related Articles
* Comments
* Articles Search
* Article Social Media Share
* Article Minute Read
* Article Number of Words
* Article Number of Views
* Article Tags
* Tag Related Articles
* Markdown Support
* Responsive on all devices
* Pagination
* Clean Code
* 90% test coverage


## Technologies
* Python 3
* Javascript
* Jquery
* PrismJS
* Django 3
* HTML5
* CSS3 
* Bootstrap 4
* Ion Icons
* Font awesome
* CKEditor
* SQLite
* PostgreSQL


## Setup

To run this app, you will need to follow these 3 steps:

#### 1. Requirements
  - a Laptop

  - Text Editor or IDE (eg. vscode, PyCharm)

  - [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed on your Laptop.


#### 2. Install Python and Pipenv
  - [Python3](https://www.python.org/downloads/)
  

  - [Pipenv](https://pipenv-es.readthedocs.io/es/stable/)

#### 3. Local Setup and Running on Windows, Linux and Mac OS

  ```
  # Clone this repository into the directory of your choice
  $ git clone https://github.com/Williano/Bona-Blog.git

  # Move into project folder
  $ cd Bona-Blog

  # Install from Pipfile
  $ pipenv install

  # Activate the Pipenv shell
  $ pipenv shell

  # Create database tables
  (Bona-Blog-XXXX) $ python manage.py migrate
  
  # Create superuser account
  (Bona-Blog-XXXX) $ python manage.py createsuperuser

  # Start server
  (Bona-Blog-XXXX) $ python manage.py runserver
  
  # Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at 127.0.0.1....).
  
  # Open the address in the browser
  >>> http://127.0.0.1:XXXX
  
  # Login into Dashboard and write articles
  >>> http://127.0.0.1:8000/author/dashboard/home/
  
  # Django Admin
  >>> http://127.0.0.1:XXXX/admin/
  
  # Run Tests
  $ python manage.py test blog.tests
  ```


## Status
Project is: _in progress_

## Inspiration
This project is based on the goal of improving my skills as a Software Engineer and the best way to improve is by building projects. I wanted to gain a deeper understanding of Django and Object-oriented programming in Python whiles I also contribute to the open-source community at the same time. I have learnt different technologies for the project and I keep on learning new skills as I add new features to the project.

## Contact
Created by [Williano](https://williano.github.io/) - feel free to contact me!

## License
>You can check out the full license [here](https://github.com/Williano/Bona-Blog/blob/master/LICENSE.md)

This project is licensed under the terms of the **MIT** license.

## Contributing

1. Fork it (<https://github.com/Williano/Bona-Blog.git>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
