import uuid
from database import mongo_client

# This is the users database
auth_db = mongo_client["auth-db"]
user_credentials = auth_db["users"]


# This function sets an auth_token cookie for a given user ID
def set_cookie(user_id):

    # Generates a random token and stores it in the database.
    auth_token = str(uuid.uuid4())
    user_credentials.update_one({"id": user_id},
                                {"$set":
                                     {"auth_token": auth_token}})

    # This represents the key and the value pair of a cookie.
    # Any directives (if required) should be added to the value part with a '; '
    value = auth_token
    cookie = {"auth_token": value}

    return cookie






