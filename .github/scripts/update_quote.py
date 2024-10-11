import requests
import json
from datetime import date

def fetch_quote():
    response = requests.get("https://zenquotes.io/api/today")
    data = json.loads(response.text)
    return data[0]['q'], data[0]['a']

def update_readme(quote, author):
    with open("README.md", "r") as file:
        content = file.read()

    start = content.find("### Quote of the Day")
    end = content.find("###", start + 1)
    if end == -1:
        end = len(content)

    today = date.today().strftime("%B %d, %Y")
    new_section = "### Quote of the Day\n\n"
    new_section += f'> "{quote}"\n>\n'
    new_section += f"> — {author}\n\n"
    new_section += f"*Updated on {today}*\n\n"

    updated_content = content[:start] + new_section + content[end:]

    with open("README.md", "w") as file:
        file.write(updated_content)

if __name__ == "__main__":
    quote, author = fetch_quote()
    update_readme(quote, author)
