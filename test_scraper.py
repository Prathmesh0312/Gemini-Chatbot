from services.webfetch import fetch_main_text

try:
    text = fetch_main_text("https://en.wikipedia.org/wiki/Starbucks")
    print(" Success:\n")
    print(text[:1000])
except Exception as e:
    print(" Failed to fetch:", e)
