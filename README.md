# TODO webapp
Simple todo list REST API

## Prerequisites
* Python3.6+
* Python IDE
* Redis server (for caching)


Make sure to install [redis](https://redis.io/topics/quickstart) before you proceed

## Setup
1. Clone the repo and install the requirements 
(```pip install -r requirements.txt```)

2. Create ```.env``` file and configure environmental variables

Example content:
``` 
SECRET_KEY=Some-Generated-Secret-Key
DATABASE_URL=sqlite:///db.sqlite3
REDIS_CACHE_URL=redis://localhost:6379/1
DEBUG=True
```

3. Make migrations & migrate
```
python manage.py makemigrations
python manage.py migrate
```

It's ready! Unless you want to deploy it elsewhere...

## Deployment

Make sure to install [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/) before we start

1. Change env variables in Dockerfile, currently:

```
ENV SECRET_KEY=Some-Generated-Secret-Key
ENV DATABASE_URL=sqlite:///db.sqlite3
ENV REDIS_CACHE_URL=redis://redis:6379/1
ENV DEBUG=False
```

Note: it will override ```.env``` file that is currently in app directory

2. Run
 
    To build ```docker-compose build``` 

    To run ```docker-compose up```

Docker compose will run two containers: django app and redis server


#Example requests

All the requests can be found [here](https://www.getpostman.com/collections/76c181d50423507a0174) (Postman)

Here is some request - response snippets:

1. ```
   POST /categories
   {
        "title": "In progress",
        "description": "in progress todos",
        "todos": [
            {
                "title": "appboxo task",
                "description": "appboxo screening task"
            },
            {
                "title": "spring mvc pet-project",
                "description": "just for fun"
            }
        ]
   }
   ```
    Response:
    ```
    201 CREATED
    
    {
        "id": 1,
        "title": "In progress",
        "description": "in progress todos",
        "todos": [
            {
                "id": 1,
                "title": "appboxo task",
                "description": "appboxo screening task"
            },
            {
                "id": 2,
                "title": "spring mvc pet-project",
                "description": "just for fun"
            }
        ]
    }
    ```

2. ```
   GET /todo/1
   
   {
      "id": 1,
      "title": "appboxo task",
      "description": "appboxo screening task",
      "category": "In progress"
   }
   ```