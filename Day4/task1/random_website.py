import random
import webbrowser

websites = [
    "https://google.com",
    "https://youtube.com",
    "https://github.com",
    "https://wikipedia.org",
    "https://reddit.com"
]

site = random.choice(websites)
print(f"opening {site}")
webbrowser.open(site)
