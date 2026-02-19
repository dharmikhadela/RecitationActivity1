from authentication.set_cookie import set_cookie
from database import mongo_client

# This is the users database
auth_db = mongo_client["auth-db"]
user_credentials = auth_db["users"]


# This function takes in the input from /register page
# Returns a status code and response message.
def login_user(username, password):

    # Finding the user from the database
    user = user_credentials.find_one({
        "username": username.lower(),
        "password": password
    })

    # If user found, sets an auth_token cookie for the id.
    if user:
        status_code = 200
        response_message = "OK"
        cookie = set_cookie(user.get("id"))

    # If user not found, an error message is sent
    else:
        status_code = 400
        response_message = "Incorrect username or password"
        cookie = {}

    return status_code, response_message, cookie