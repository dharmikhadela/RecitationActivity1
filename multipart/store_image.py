import base64
import uuid
from datetime import datetime
from database import mongo_client

# This database stores user feedback
feedback_db = mongo_client["feedback-db"]
feedback_collection = feedback_db["feedback"]

# This function stores the feedback and optional gif into the database
# It returns a status code and response message.
def store_feedback_with_image(text, file_obj):
    # Remove spaces in case text exists or "" in case of None
    text = (text or "").strip()

    # If only image present return error as feedback should be with text.
    if not text:
        return 400, "Feedback text is required."

    doc = {
        "text": text,
        "ts": datetime.utcnow(),
        "image": None,
        "image_mime": None
    }

    # Optional image
    # If image present, take the mimetype
    if file_obj and getattr(file_obj, "filename", ""):
        mime = getattr(file_obj, "mimetype", None)

        # If mimetype not accepted, return error.
        if mime != "image/gif":
            return 400, "Only .gif images are allowed"

        # Read the gif data
        data = file_obj.read().decode(errors='replace')
        if not data:
            return 400, "Uploaded image file was empty"

        # Store the gif locally and store the path in db.
        file_name = str(uuid.uuid4()) + ".gif"
        with open("public/imgs/"+file_name, 'w') as f:
            f.write(data)

        # Store the file content into the database.
        doc["image"] = file_name
        doc["image_mime"] = mime

    feedback_collection.insert_one(doc)
    return 200, "Feedback saved"