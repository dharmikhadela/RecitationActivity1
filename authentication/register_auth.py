import uuid
from database import mongo_client

# This is the users database
auth_db = mongo_client["auth-db"]
user_credentials = auth_db["users"]


# This function takes in the input from /register page
# Returns a status code and response message.
def register_user(username, email, password, confirm_password):

    # Ensures to throw error if passwords do not match..
    if password != confirm_password:
        status_code = 400
        response_message = "Passwords do not match"

    # If passwords match, stores user in database along with a unique ID and blank auth_token field.
    else:
        user_id = str(uuid.uuid4())
        user_credentials.insert_one({
            "id": user_id,
            "username": username.lower(),
            "email": email.lower(),
            "password": password,
            "auth_token": None
        })
        status_code = 200
        response_message = "OK"

    return status_code, response_message