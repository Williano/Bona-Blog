# Bona Blog
An Open-Source Blogging platform.


## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)
* [License](#license)
* [Contributing](#contributing)


## General info
An Open-Source bloggig plaform like [Medium](https://medium.com/) and [Real Python](https://realpython.com/) built with Python and Django. It has a number of [features](#features) needed for a standard bloggin platform.

## Screenshots

Home Page            |  Categories List
:-------------------------:|:-------------------------:
![Home](https://user-images.githubusercontent.com/19711677/56363189-264fb200-61db-11e9-9bba-77a3e7f7c1de.jpg) | ![Categories List](https://user-images.githubusercontent.com/19711677/56363187-264fb200-61db-11e9-8a90-0af49eb33758.jpg)

Category Articles List          |  Author Articles List
:-------------------------:|:-------------------------:
![Category Article List](https://user-images.githubusercontent.com/19711677/56363188-264fb200-61db-11e9-8fef-fc83fb29f056.png) | ![Author Articles](https://user-images.githubusercontent.com/19711677/56363185-25b71b80-61db-11e9-9a42-2fffaa369d28.jpg)



Authors List     
![Authors List](https://user-images.githubusercontent.com/19711677/56363186-25b71b80-61db-11e9-9a0b-7f9daa6f30e9.png) 



Article Detail
![Article Detail](https://user-images.githubusercontent.com/19711677/56364113-55672300-61dd-11e9-869d-5a30adea9e21.jpg)


## Technologies
* Python 3.7
* Django 2.2
* HTML5
* CSS3 
* Bootstrap 
* Ion Icons
* Font awesome
* TinyMCE
* SQLite

### Setup
## Installation on Linux and Mac OS

* [Follow the guide here](https://help.github.com/articles/fork-a-repo) on how to clone or fork a repo
* [Follow the guide here](http://simononsoftware.com/virtualenv-tutorial/) on how to create virtualenv

* To create a normal virtualenv (example _myvenv_) and activate it (see Code below).

  ```
  sudo apt-get install python-virtualenv
  
  virtualenv --python=python3.6.5 myvenv
  
  source myvenv/bin/activate

  (myvenv) $ pip install -r requirements.txt

  (myvenv) $ python manage.py makemigrations

  (myvenv) $ python manage.py migrate

  (myvenv) $ python manage.py runserver
  ```
* Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at 127.0.0.1....).
* Open the address in the browser
* Don't forget to Change ALLOWED_HOSTS = ['127.0.0.1'] in settings.py
* `Note`: It is important that when you create your virtualenv, do not create it in the same folder as the code you downloaded.


## Installation on Windows

* [Follow the guide here](https://help.github.com/articles/fork-a-repo) on how to clone or fork a repo
* [Follow the guide here](http://pymote.readthedocs.io/en/latest/install/windows_virtualenv.html) on how to create virtualenv

* To create a normal virtualenv (example _myvenv_) and activate it (see Code below).

  ```
  1. Create main project folder with name of your choice (eg.Bona-Blog-Project) 
  
  2. Clone (git clone url) the project into that folder.
   
  3. Open the command prompt and navigate the project folder (Bona-Blog-Project)
  
  4. virtualenv bona-blog-project-env   # Create a virtual environment for the project with it's own packages.
  
  5. bona-blog-project-env\Scripts\activate    # Move into the virtual environment folder and activate the environment.
  
  6. cd Bona-Blog    # Move into second (bona_blog) folder.
  
  7. pip install -r requirements.txt  # install the requirements.

  8. python manage.py migrate   # Migrate the data into the database.

  9. python manage.py runserver   # Run the server.
  
  NOTE: You can use any text editor or IDE of your choice. 
  ```
* Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at 127.0.0.1....).
* Open the address in the browser
* Don't forget to Change ALLOWED_HOSTS = ['127.0.0.1'] in settings.py
* `Note`: It is important that when you create your virtualenv, do not create it in the same folder as the code you downloaded.


## Features

* [iOS Mobile App](https://github.com/Williano/Bona-Mobile.git)
* Dashboard for Authors
* Author Login
* Author Password Reset
* Authors List
* Author Articles List
* Category List
* Category Articles List
* Related Articles
* Comments
* Article Newsletter Subscribe
* Articles Search
* Article Social Media Share
* Article Minute Read
* Article Number of Words
* Article Number of Views
* Markdown Support
* Responsive on all devices
* Pagination
* Clean Code
* 80% test coverage

## Status
Project is: _in progress_

## Inspiration
This project is based on the goal of imporving my skills as a developer. I wanted to improve my skills and also contribute to the open source community at the same time and decided to build this project. I have learnt different technologies for the project and I keep on learning new skills as i add features to the project.

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
