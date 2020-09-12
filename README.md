# PYTHON REST API
> Implement a simple message board web application. The application should have two services: createMessage
and listMessages. The services should be implemented using a protocol (of your choice) running on HTTP.

> 1. CreateMessage receives a message in the request and persists it in the application. The message should have 4 fields: 
> - title     ---> can be arbitrary strings (with limited lengths)
> - content   ---> can be arbitrary strings (with limited lengths)
> - sender    ---> can be arbitrary strings (with limited lengths)
> - url       ---> Url should be a valid url

> 2. ListMessages service lists all the messages persisted in the application. The service should support two response versions within the same endpoint. The caller is able to define which response version he can handle.

### Requirements
``` 
python
django
django rest framework
```

### Setup
- Clone project to your desired destination 
- cd to cloned project
- create virtual env & activate env (optional)
- cd to main project (to directory with manage.py)
- make migrations
- migrate & runserver
- start sending queries 
```
$> cd f-api-secure
$> python -m venv env
$> source env/bin/activate
$> cd api
$> python manage.py makemigrations
$> python manage.py migrate
$> python manage.py runserver
```
### Testing API


## Overview
### Documentation 

**Endpoint**

- `Get api/v1/sender` : returns a message based on a given url

- `GET api/v1/listMessages` : displays all messages

- `POST api/v1/createMessage` : creates a message and stores to the server

- `Delete api/v1/deleteMessage` : deletes a message

**Responses**
 - `200 OK` on success
 - `404 Not Found` no such a message or url

```json
{
  "title": "message title, can be arbitrary string (with limited lengths)",
  "content": "body of the message, can be arbitrary string (with limited lengths)",
  "sender": "sender of the message, can be arbitrary string (with limited lengths)",
  "url": "Url should be a valid url"
}
```

### TODO:

- [x] create a django project
- [x] create an app inside django project
- [x] config setting and & urls
- [x] create a message model
- [x] link model to mysql - using makemigrations andmigrate
- [x] create a message model
- [x] create endpoint services
- [x] create api/v1/createMessage
- [x] create api/v1/listMessages
- [ ] create api/v1/getMessage/<str:sender>
- [ ] create api/v1/deleteMessage/<str:sender>
- [ ] create api/v1/createMessage
- [ ] create api/v1/listMessages
- [ ] create api/v1/getMessage/<str:sender>
- [ ] create api/v1/deleteMessage/<str:sender>

