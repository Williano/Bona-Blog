# Bona-Blog
A blog project built with Django 2.1. 



## Getting Started
This section describes how to set up an environmet to run and test the project.

### Prerequisites
* You have a working installation of Python 3.6.*
* You can install software on your system.
* You can create and activate Python virtual environments.

### Setup
## Installation on Linux

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
  1. Create main project folder with name of your choice (eg.Bona Blog Project) and clone (git clone url) the project into that folder.
   
  2. Open the command prompt and navigate the project folder (Bona Blog Project)
  
  3. virtualenv bona-blog-project-env   # Create a virtual environment for the project with it's own packages.
  
  4. bona-blog-project-env\Scripts\activate    # Move into the virtual environment folder and activate the environment.
  
  5. cd ..   # move back into main project folder.
  
  6. cd bona_blog    # Move into second (bona_blog) folder.
  
  7. pip install -r requirements.txt  # install the requirements.

  8. python manage.py migrate   # Migrate the data into the database.

  9. python manage.py runserver   # Run the server.
  
  NOTE: You can use any text editor or IDE of your choice. 
  ```
* Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at 127.0.0.1....).
* Open the address in the browser
* Don't forget to Change ALLOWED_HOSTS = ['127.0.0.1'] in settings.py
* `Note`: It is important that when you create your virtualenv, do not create it in the same folder as the code you downloaded.
