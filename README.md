 # wizeinout



Step 1: Set Up Your Django Project for Deployment
Create CloudSQL MySQL Instance Ensure you have CloudSQL MySQL Instance created and one database for application is created.

Update settings.py: Add the necessary configurations for static files and allowed hosts.

    DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'HOST': '/cloudsql/tt-dev-001:us-central1:dev',
         'PORT' : '3306',
         'USER': 'root',
         'PASSWORD': 'mysql',
         'NAME': 'appdb',
     }
   }
Create requirements.txt: Generate a requirements.txt file for the dependencies.

   Django
   mysqlclient
Download and install the Cloud SQL Auth Proxy to your local machine. Right-click https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.11.3/cloud-sql-proxy.x64.exe and select Save Link As to download the Cloud SQL Auth Proxy. Rename the file to cloud-sql-proxy.exe. In seperate terminal run Cloud SQL Auth Proxy

   ./cloud-sql-proxy PROJECT_ID:REGION:INSTANCE_NAME
Run the Django migrations to set up your models on New Database i.e Cloud SQL.

   python manage.py makemigrations
   python manage.py migrate
Now run and Test Application locally

Start the Development Server:

python manage.py runserver
Access the Application: Open your browser and navigate to http://127.0.0.1:8000/ to see your notes application in action.

Create app.yaml: Create an app.yaml file in your project's root directory.
   runtime: python39
   service: noteapp
Create main.py: Add the necessary configurations for static files and allowed hosts.
   from notes_project.wsgi import application
   app = application

   
Step 2: Deploy to Google App Engine
Install Google Cloud SDK: If you haven’t already, install the Google Cloud SDK by following the installation guide.

Initialize Your Google Cloud Project:

gcloud init
Authenticate Your Google Cloud Account:

gcloud auth login
Set the Project:

gcloud config set project YOUR_PROJECT_ID
Deploy Your Application: Deploy your application to Google App Engine.

gcloud app deploy
Browse Your Application: Open your browser to view the deployed application.

gcloud app browse
To Map custom Domain Use Below Link - Mapping custom Domain to Google App Engine

Conclusion
This guide walks you through setting up a Django application for deployment on Google App Engine. It includes steps for configuring your Django project, preparing it for deployment, and deploying it using the Google Cloud SDK. By following these steps, you can ensure your application is ready for a scalable and reliable deployment on Google App Engine.

