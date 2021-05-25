# MessagesAPI


## About the app
The app is a REST API which enables the user to create, edit, delete and display messages. I used Django with Django REST Framework.

Unit tests are based on pytest, the test coverage of Django _models_ and _views_ is 100%.

## Deployment
The API was deployed to Heroku through Git, with the help of django-heroku extension which significantly simplified the process.

The used database engine on Heroku is PostgreSQL, since SQLite which was used in production is not available on Heroku.

## How to use

* Main view is under: https://message-manager-api.herokuapp.com/messages/
Here, you can see the messages' titles and view counters and their URLs. Each URL takes the user to a detailed view of the message (with its' contents).
In this view, you can also add messages.

* The URLs are uniform, for example in order to access the first message, go to URL: https://message-manager-api.herokuapp.com/messages/1/.
Analogically, the second message is under https://message-manager-api.herokuapp.com/messages/2/ and so on.

* Under such URL you can edit or delete a message with primary key equal to the number in the URL.
You can change the title (up to 50 characters), content (up to 160 characters). If you try to change view counter, server will just ignore the value you supplied.
You can also delete the whole message.

* Anyone can view messages, but you need to log in to create, edit or delete them. In order to log in press the login button at the upper right corner and enter the correct credentials (not leaving any on public GitHub to avoid spam or denial of service attack, but I did send them via e-mail)
The login page is also available under this link: https://message-manager-api.herokuapp.com/api-auth/login/?next=/messages/
The authentication is implemented with standard Django authentication methods.

* Django REST Framework allows you to test the API by making the standard requests (e.g. POST, GET) using frontend which is automatically supplied. 
However, it is also possible via other means, like _curl_. However, in order to do anything else than GET in _curl_ and other tools like it, you need to supply credentials with every request (in a standard way).
