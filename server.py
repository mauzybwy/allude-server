################################################################################
# Import
################################################################################
import sys
from flask import Flask, send_file, jsonify

# sys.path.append("./allude_screenshot")
# from allude_screenshot.blueprint import screenshot_blueprint

sys.path.append("./allude_subtitles")
from allude_subtitles.blueprint import subtitle_blueprint

sys.path.append("./allude_reddit")
from allude_reddit.blueprint import reddit_blueprint

################################################################################
# Setup
################################################################################
# Init Flask app
app = Flask(__name__)

################################################################################
# Routes
################################################################################

### Blueprints
app.register_blueprint(subtitle_blueprint, url_prefix="/subtitles")
# app.register_blueprint(screenshot_blueprint, url_prefix="/screenshot")
app.register_blueprint(reddit_blueprint, url_prefix="/reddit")

### Other Routes
print("READY TO SERVE")
@app.route("/test")
def main():
    print("ALIVE")
    return "ALIVE"


