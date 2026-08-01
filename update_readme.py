import re
import urllib.request
import json
from datetime import datetime

# 1. Fetch unique data (Using a public joke API as a placeholder)
# Swap this URL out later for Spotify, WakaTime, or your own custom API!
url = "https://official-joke-api.appspot.com/random_joke"
try:
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    joke = f"{data['setup']} <br> *{data['punchline']}*"
except Exception as e:
    joke = "Taking a quick coffee break... (API offline)"

# 2. Get the current time to prove it is updating live
current_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

# 3. Format the exact Markdown you want injected into your profile
new_content = f"""
> **Last Automated Update:** {current_time}
> 
> **Random Dev Joke of the Hour:** 
> {joke}
"""

# 4. Open and read the current README.md
with open("README.md", "r", encoding="utf-8") as file:
    readme_text = file.read()

# 5. Use Regex to find the markers and replace the text between them
pattern = r"(<!-- START_SECTION:dynamic_data -->\n)(.*)(\n<!-- END_SECTION:dynamic_data -->)"
updated_readme = re.sub(pattern, rf"\1{new_content.strip()}\3", readme_text, flags=re.DOTALL)

# 6. Save the newly updated text back to the README.md
with open("README.md", "w", encoding="utf-8") as file:
    file.write(updated_readme)

print("README.md updated successfully!")
