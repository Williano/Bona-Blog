HTML Forms

    - Use <button></button> for html forms submit button and make the 
      type "submit". Set the "action" of the form to the url you want 
      to post the data to. Do not use "<a></a>" for the "form" 
      submit button. Example:
      
      ```htm5
           <form action="" method="POST">
             <input type="email">
             <button type="submit"></button> 
      ```
 
    - Use "<a></a>" for links to other pages and use the "button" styles 
      to style it. Example:
      <a href=""></a> 
 
 
 Django
 
    - By default function based views returns get() method. 
      Unless you explicitly check the for post it will 
      return only get() method.
      
   
      
Error
   
   -  Error: 
        ```Traceback (most recent call last):
        File "manage.py", line 8, in <module>
         from django.core.management import execute_from_command_line
        ImportError: No module named django.core.management
   - To fix the above error in any Django project, just install the requirements.txt file 
   
       ```pip install -r requirements.txt   ```   
      
      
   - Running Specific test
   
   ``
        python manage.py test blog.tests.models.test_comment_models.CommentTestCase

    ``  