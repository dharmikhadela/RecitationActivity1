from database import mongo_client

# This is the users database
auth_db = mongo_client["auth-db"]
sessions = auth_db["users"]

# This checks if a token is valid or not.
def validate_token(token):
    if not token:
        return False

    session = sessions.find_one({"auth_token": token})
    if not session:
        return False

    return True
