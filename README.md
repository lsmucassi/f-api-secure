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
**Defination**

`GET api/v1/listMessages`
`POST api/v1/createMessage`
`Delete api/v1/message`

**Response**

 - `200 OK` on success

```json
{
  "title": "message title, can be arbitrary string (with limited lengths)",
  "content": "body of the message, can be arbitrary string (with limited lengths)",
  "sender": "sender of the message, can be arbitrary string (with limited lengths)",
  "url": "Url should be a valid url"
}
```
