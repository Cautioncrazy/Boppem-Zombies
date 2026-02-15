from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8000/fps_game.html")

        # Wait for the FPS mode indicator
        page.wait_for_selector("#fps-mode")

        # Wait a bit for the game loop to render a few frames
        time.sleep(1)

        # Take screenshot
        page.screenshot(path="verification_fps.png")
        browser.close()

if __name__ == "__main__":
    run()
