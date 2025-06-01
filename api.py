from flask import Flask, jsonify
from instagrapi import Client
import os

app = Flask(__name__)

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

@app.route("/reels", methods=["GET"])
def get_saved_reels():
    cl = Client()
    cl.login(USERNAME, PASSWORD)

    collection_id = "ALL_MEDIA_AUTO_COLLECTION"
    medias = cl.collection_medias_v1(collection_id)

    output = []
    for media in medias:
        output.append({
            "title": media.caption_text or "",
            "url": f"https://www.instagram.com/reel/{media.code}/",
            "video_url": str(media.video_url),
            "thumbnail": str(media.thumbnail_url),
            "username": media.user.username
        })

    return jsonify(output)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
