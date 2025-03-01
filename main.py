from playwright.sync_api import sync_playwright

def test_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Visible for testing
        page = browser.new_page()
        page.goto('https://www.google.com')
        print("Title:", page.title())
        browser.close()

if __name__ == "__main__":
    test_playwright()