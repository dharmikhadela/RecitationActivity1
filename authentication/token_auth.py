import hashlib

from database import mongo_client

# This is the users database
auth_db = mongo_client["auth-db"]
sessions = auth_db["users"]

# This checks if a token is valid or not.
def validate_token(token):
    if not token:
        return False

    hashed_token = hashlib.sha256(token.encode()).hexdigest()
    session = sessions.find_one({"auth_token": hashed_token})
    if not session:
        return False

    return True
