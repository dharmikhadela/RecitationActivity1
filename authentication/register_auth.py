import uuid
from database import mongo_client
import bcrypt
from password_strength import PasswordPolicy

# This is the users database
auth_db = mongo_client["auth-db"]
user_credentials = auth_db["users"]

# Password constraints: length, uppercase/lowercase, special characters
policy = PasswordPolicy.from_names(length=8, uppercase=1, special=1)

# This function takes in the input from /register page
# Returns a status code and response message.
def register_user(username, email, password, confirm_password):

    # Ensures to throw error if passwords do not match.
    if password != confirm_password:
        status_code = 400
        response_message = "Passwords do not match"
        return status_code, response_message

    # Finding the user from the database
    user = user_credentials.find_one({
        "username": username.lower(),
    })

    # Ensures to throw error if username is already taken
    if user:
        status_code = 400
        response_message = "Username already taken"
        return status_code, response_message

    # Checks for constraints in password
    if policy.test(password):
        return 400, "Password must be 8+ chars and include upper, lower, and special characters."

    # If passwords match, stores user in database along with a unique ID and blank auth_token field.
    else:
        user_id = str(uuid.uuid4())
        user_credentials.insert_one({
            "id": user_id,
            "username": username.lower(),
            "email": email.lower(),
            "password": bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode(),
            "auth_token": None
        })
        status_code = 200
        response_message = "OK"

    return status_code, response_message