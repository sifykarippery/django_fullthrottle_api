# Django Full Throttle API Test

## Verification Steps

### 1. App Deployed multiple environments

#### Seed Data using Command Management (Refer below Local setup section for the Steps)
      
      Seed Data is dynamically created Data, user can run th below commands as many times, every time Faker will generate meanigful data
      
      python manage.py seed-db 10 -- For 10 Users with each User will have 5 Activity Periods
      

#### Test (Heroku Git + Postgres)  

      https://djangosifyapp.herokuapp.com/
      
      API Endpoint for Users
      https://djangosifyapp.herokuapp.com/api/v1/fullthrottle/
    
#### Automated Deployes (Heroku + Github + Postgres)

      https://django-fullthrottle-stage.herokuapp.com/
      https://django-fullthrottle-stage.herokuapp.com/api/v1/fullthrottle/


## Step to run Run in LOCAL (with Sqlite DB)

#### 1. Update Settings.py(root level folder)
      Uncomment below lines
      ```
      # DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
         }
      }
      ```
     Comment below lines
      
      ```
      DATABASES ={'default':dj_database_url.config()
      }```
#### 2. Create and Activate Virtual Enviroments
      virtualenv venv
      .\venv\Scripts\Activate

#### 3. Install requirements
        ```
        pip3 install -r requirements.txt
        
        ```
#### 4. Run Project
        ```
        python manage.py runserver
        
        ```
#### 5. Run Migrations
        ```
        python manage.py makemigrations
        python manage.py migrate
        ```

#### 6. Seed Database with Command Management 
        Seed Database with Fake data using Faker.
        
        first argument will be number of users 
        second argument (optional) if nothing then it will insert 5 records for each user of if you want to sepcify the logs
        seed-db 10 (10 Users, 10*5 = 50 Activity periods will be inserted)
        seed-db 10 --logs 20 > 10 Users, 200 total activities
        All the data will be geneated using Faker to give some real data
        
        ```
        python manage.py seed-db 10
        ```

#### 7. Browse the below Urls to Verify

        http://127.0.0.1:8000/ - **Main Dashboard to List Users**
        http://127.0.0.1:8000/api/v1/fullthrottle/  - **API endpoint for the Data in the Database**
        U can see the Users , Clicking on Actiivity Logs will get corresponding User Activities also
        
    
