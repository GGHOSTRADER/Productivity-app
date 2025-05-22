# effects.py
import webbrowser


def open_url(url):
    try:
        webbrowser.open_new(url)
    except Exception as e:
        print(f"Failed to open URL {url}: {e}")
