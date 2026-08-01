# Welcome to my completely unique profile!

Here is my live data:

<!-- START_SECTION:dynamic_data -->
import re
import urllib.request
import json

# 1. Fetch your unique data (Example: A random programming quote)
# To be truly unique, replace this with Spotify APIs, Strava APIs, or your own custom backend!
url = "https://official-joke-api.appspot.com/random_joke"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

new_content = f"**Live Status:** Just heard a joke: *{data['setup']}* - {data['punchline']}"

# 2. Read the current README.md
with open("README.md", "r", encoding="utf-8") as file:
    readme_text = file.read()

# 3. Replace the text between the markers using Regex
pattern = r"(<!-- START_SECTION:dynamic_data -->\n)(.*)(\n<!-- END_SECTION:dynamic_data -->)"
replacement = rf"\1{new_content}\3"
updated_readme = re.sub(pattern, replacement, readme_text, flags=re.DOTALL)

# 4. Write the changes back to README.md
with open("README.md", "w", encoding="utf-8") as file:
    file.write(updated_readme)

print("README.md updated successfully!")
<!-- END_SECTION:dynamic_data -->

Thanks for visiting.
