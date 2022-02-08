--> For To Create Project Run The Command     "django-admin startproject CRM"
--> Next create the customer app using the command     "django-admin startapp Customer"
--> Next create the customerOrder app using the command  "django-admin startapp CustomerOrder"
--> Next create the customerOrderItem app using the command  "django-admin startapp OrderItem"
--> Next create the Product app using the command    "django-admin startapp Product"

section.py :

--> Go to setting.py file add  'rest_framework','corsheaders', in INSTALLED_APPS section.
--> Next add CORS_ALLOW_ALL_ORIGINS = True . Other wise you can specify the perticular url to allow resquest.
--> Next Add all the apps in the "INSTALLED_APPS" section , which we are created above .
--> Next Add "corsheaders.middleware.CorsMiddleware" inside the "MIDDLEWARE" section in settings.py file.
--> Next add the templates path ( BASE_DIR / 'templates',..... ) inside the 'DIRS' which is present in the TEMPLATES Section.
--> Next add the Data base Propertices inside the "DATABASES" Section . Defaultly db.sqlite3 is added . you can change this your own database.
--> Next Change the TIME_ZONE = 'Asia/Kolkata' so that storing time date and time is taken by this Time zone. you can change your own Time zone.
--> Next add the Static Files path ( BASE_DIR / 'static',... ) inside the STATICFILES_DIRS . 
--> Next Add the images path (BASE_DIR / 'static/images') to the MEDIA_ROOT.


Creating Model Classes :

--> After Completion of above Steps we create the models classes based on our requirements.
--> We create our model classes in models.py file . Every App Has it's models.py files . So we can write our models classes based on the app.
--> After Ceating the models classes in all Apps , We run the command " py manage.py makemigrations".
--> py manage.py makemigrations is scan all our model classes and create database related commands . we can see those commands in migration folder of every App.
--> So here we dont need to write the database commands , Django Automatically create those commands.
--> So now we execute the all database commands which are created by the above command.
--> For to execute the All database commands we run the Command " py manage.py migrate ".
--> So this Command execute all our database commands and create the tables in side the database.


CRM -> urls.py:

--> Here CRM.urls.py is the base urls to th all application. When we run the project server first go to the base url ,from there we can give the path of urls based on our requirement.
--> So here i create urls.py file in every app so that we can differenciate the urls of a perticula app .
--> After creating the Urls in all apps i Registered all the urls.py files in to the base Urls (CRM -> urls.py) file. 


admin.py :

--> admin.py file is present in every app. 
--> Here We can register our model in admin site. 
--> Syntax : admin.site.register(modelClassName).  modelClassName like Customer,CustomerOrder,.....
--> So register after register your models in admin site we can see those in admin site. 

Note : --> For to go to admin site we need username and password . so for to create username and password we create the superuser. 
       --> For to Create Superuser Run the command " python manage.py createsuperuser ". 
       --> After run the above command it will ask all your details like username,password,mailid....etc.
       --> So next you go to the admin login page and use you credentials for to login.
       --> After login you will see the models which you register in the admin site.





