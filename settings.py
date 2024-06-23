import os

def get_badge_size():
    try:
        size = int(os.getenv("INPUT_BADGE_SIZE", "110"))
        return max(min(size, 300), 50)  # Clamp between 50 and 300
    except ValueError:
        print("Warning: Invalid BADGE_SIZE. Using default of 110.")
        return 110

START_COMMENT = "<!--START_SECTION:badges-->"
END_COMMENT = "<!--END_SECTION:badges-->"

REPOSITORY = os.getenv("INPUT_REPOSITORY")
GH_TOKEN = os.getenv("INPUT_GH_TOKEN")
GH_API_URL = os.getenv("INPUT_GH_API_URL")
COMMIT_MESSAGE = os.getenv("INPUT_COMMIT_MESSAGE")
CREDLY_USER = os.getenv("INPUT_CREDLY_USER")
CREDLY_SORT = os.getenv("INPUT_CREDLY_SORT")

# BADGE_SIZE = int(os.getenv("INPUT_BADGE_SIZE", "110"))
BADGE_SIZE = get_badge_size()
try:
    NUMBER_LAST_BADGES = int(os.getenv("INPUT_NUMBER_LAST_BADGES"))
except:
    NUMBER_LAST_BADGES = 0

CREDLY_BASE_URL = "http://www.credly.com"

LIST_REGEX = f"{START_COMMENT}[\\s\\S]+{END_COMMENT}"
