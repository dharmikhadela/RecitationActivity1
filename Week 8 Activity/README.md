# Mr. Nilo’s Buggy Feedback Website

Mr. Nilo now agreed that maybe he is not as experienced as he thought. 
However, he is still working on his website. 
He's grumpy but still an average grandpa.
He thought it would be nice to have people put gifs along with feedback.

Now, was time for Jesse review:
> “I'm kinda busy making the 116 OH app this week...”

Still grumpy, he went to the students.

> "You all are way too young to even be at my level of knowledge!"

---

## New Files Overview

### `multipart/parse_multipart_test.py`
This has a test case that Mr. Nilo tried to write when he first saw the Homework 3 handout.

`He has 3 major bugs in his test.`

Find these bugs prove to Mr. Nilo that you are smarter than him.

----
### `multipart/store_image.py`
Stores the feedback text and gif (if present) in the database. 
However, Mr. Nilo is having trouble with the gifs. 
They won't show up in the submissions even though the response is OK.

----

There is a Cat.gif in Week 8 Activity folder if required for testing.

----
## Objective

Prove Mr. Nilo that you all have a better understanding of multipart requests and storing and retrieving the images.

### Run the application. Upload a gif. Try viewing the database. Find the bugs. Fix them.
If you fix it, he is going to turn into a ball and die of embarrassment.

![Mr. Nilo](../public/Mr.%20Nilo%20Ball.jpeg)



----
## Previous Backend Files (Not required for this task)
### `server.py`
Main Flask application.  
Handles routing, request processing, authentication flow, and redirects.  
#### `Jesse approved this file. Do not worry about it.`

---

### `docker-compose.yml`
Defines the multi-container setup for the application and MongoDB database.

---

### `Dockerfile`
Contains instructions to build the application container image.

---

### `database.py`
Handles database connection logic. Connects to either:
- The Docker Compose MongoDB service  
- A local MongoDB instance  

---

### `authentication/login_auth.py`
- Validates username and password.  
- Returns a status code indicating whether the user is authorized to log in.

---

### `authentication/register_auth.py`
- Registers a new user in the authentication database.  
- Stores user credentials and initializes authentication data.

---

### `authentication/set_cookie.py`
Builds the authentication cookie string.


---

### `authentication/token_auth.py`
Locates and validates a user’s `auth_token`.

