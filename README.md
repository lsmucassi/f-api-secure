# PYTHON REST API

### Usage

all responses will be in the form:

```json
{
  "data": "Mixed type holding content of the response",
  "message": "Describes what happened"
}
```
### List All Messages
**Definations**

`GET api/v1/listMessages`
`POST api/v1/createMessage`
`Delete api/v1/message`

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
