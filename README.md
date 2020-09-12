# PYTHON REST API
> Implement a simple message board web application. The application should have two services: createMessage
and listMessages. The services should be implemented using a protocol (of your choice) running on HTTP.

1. CreateMessage receives a message in the request and persists it in the application.

> The message should have 4 fields: 
> - title     ---> can be arbitrary strings (with limited lengths)
> - content   ---> can be arbitrary strings (with limited lengths)
> - sender    ---> can be arbitrary strings (with limited lengths)
> - url       ---> Url should be a valid url the others 

2. ListMessages service lists all the messages persisted in the application.
The service should support two response versions within the same endpoint. The caller is able to define which
response version he can handle.

[![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]


## Documentation 
- how the project is created and structured

### Setup
- Clone project to your desired destination 
- cd to project and install dep
```
cd mytasa
npm install
```
- run app
```
npm start
```
(or sudo if you get permission errors: on linux)
```
sudo npm start
```
### Overview Project Structure
```
.
│   bower.json
|   CHANGELOG.md
|   gulpfile.js
|   jsconfig.json
|   LICENSE.md
|   package.json
|   package-lock.json
|
└───public
│   │   favicon.ico
│   │   index.html
|
|   README.md
|
└───src
│   └─── assets
|   │       └─── css
|   │       └─── demo
|   │       └─── fonts
|   │       └─── img
|   │       └─── fonts
|   │       └─── jss
|   │       └─── scss
│   │
│   └─── components
|   │       └─── Badge
|   │       └─── Card
|   │       └─── Clearfix
|   │       └─── CustomButtons
|   │       └─── CustomDropdown
|   │       └─── CustomInput
|   │       └─── CustomLinearProgress
|   │       └─── Customtabs
|   │       └─── Footer
|   │       └─── Grid
|   │       └─── Header
|   │       └─── InfoArea
|   │       └─── NavPills
|   │       └─── Pagination
|   │       └─── Parallax
|   │       └─── Snackbar
|   │       └─── Typography
│   │       
│   │    index.js
│   │       
│   └─── variables
│   │
│   └─── views
|   │       └─── Components
|   │       |       └─── Sections
|   │       └─── Landing
|   │       |       └─── Sections
```
### TODO:

- [x] Create A Landing page
- [ ] Add Navbar link routing
- [ ] Create A full 'About Page' ==> allows routing
- [ ] Create A full 'Events Page' ==> allows routing
- [ ] Create A full 'Projects Page' ==> allows routing
- [ ] Create A full 'Projects ->  Educational Page' ==> allows routing
- [ ] Create A full 'Projects ->  The Constitutio + Code Of Conduct + TASA Docs Page' ==> allows routing
- [ ] Create A full 'Projects ->  Magazine Page' ==> allows routing
- [ ] Create A full 'Projects ->  Other Projects Page' ==> allows routing
- [ ] Create Contact List for Branch, Provincial and National Execs
- [ ] Contact Us route to all branch, Provincial and National Execs contact information Page
- [ ] Change 'Register to Login'
- [ ] Login routes to 'Login Page + Register Page'
- [ ] Groups Page( For logged in users to converse and share)
- [ ] Join TASA button routes to Cantact information + allows email sending for inquery
- [ ] Fix vision + Mission Padding
- [ ] Fix Gallery Images
- [ ] Events routes to 'More info for the event' + 'Youtube" + 'Social Media' (Event live streaming)
- [ ] Video Streaming
- [ ] Virtual Meeting Rooms
- [ ] Gallery Blog => allows commenting + posting + sharing + liking + streaming


#### Usage

all responses will be in the form:

```json
{
  "data": "Mixed type holding content of the response",
  "message": "Describes what happened"
}
```
### List All Messages
**Definations**

- `GET api/v1/listMessages`

- `POST api/v1/createMessage`

- `Delete api/v1/message`

**Responses**
 - `200 OK` on success
 - `404 Not Found` no such a message or url
 - `204 No content` no data returned

```json
{
  "title": "message title, can be arbitrary string (with limited lengths)",
  "content": "body of the message, can be arbitrary string (with limited lengths)",
  "sender": "sender of the message, can be arbitrary string (with limited lengths)",
  "url": "Url should be a valid url"
}
```
