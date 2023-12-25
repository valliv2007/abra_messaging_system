# abra_messaging_system

### Description of the project:
"Messaging system" is a simple rest API backend system that is responsible for handling
messages between users.

### Tools and stack:
Python 3.11.5, Django 5.0, djangorestframework 3.14.0, djoser 2.2.2

### How to launch the project:
To run the project: Clone the repository and open it in the command line:
```
git clone git@github.com:valliv2007/abra_messaging_system.git
cd abra_messaging_system
```
Create and activate a virtual environment:
```
python -m venv venv
source venv/Scripts/activate (for Windows) or source venv/bin/activate (for Linux and MacOs)
```
Install the dependencies from the *requirements.txt* file:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
cd messaging_system
```
Set ```DEBUG = True``` in *messaging_system/settings.py*

Run migrations:
```
python manage.py migrate
```
Create superuser for Django admin:
```
python manage.py createsuperuser
```
Launch the project:
```
python manage.py runserver

```
Enter to Django admin at http://127.0.0.1:8000/foradmin/

## API documentation
See *messaging_system/static/redoc.yaml* or after running on localhost at http://127.0.0.1:8000/redoc/ (DEBUG must be True)
### Request examples

#### endpoints for all users
- path: **/api/users/** method: **POST** (create account for new user (sign up) , required fields: username, password)
- path: **/api/jwt/create/** method: **POST** (get a Bearer token (sign in), required fields: username, password)

#### endpoints only for logged user (need authorization with Bearer token)
- path: **/api/messages/** method: **GET** (User can see all messages in which he is the sender and the receiver)
- path: **/api/messages/?unread=1** method: **GET** (User can see only unread messages in which he is the sender and the receiver)
- path: **/api/messages/?receiver=username** method: **GET** (User can see only messages which send to specified receiver. In query have to use username not id) User can combine two previos filters
- path: **/api/messages/** method: **POST** (User can write a message to exsisting user. Required fields: receiver (username not id), message_text, subject)
- path: **/api/messages/{id}/** method: **GET** (User can read a message. If the user is the receiver the field "unread" will be "False")
- path: **/api/messages/{id}/** method: **DELETE** (Sender or receiver can delete message)
