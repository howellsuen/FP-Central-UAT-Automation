from playwright.sync_api import sync_playwright

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


def get_page():
    p = sync_playwright().start()

    # 1️⃣ Launch system Chrome
    browser = p.chromium.launch(
        executable_path=CHROME_PATH,
        headless=False,  # ✅ keep False during UAT for visibility
    )

    # # 2️⃣ Create browser context (for video evidence)
    # context = browser.new_context(
    #     record_video_dir="evidence/videos"
    # )

    # ✅ NO video for now
    context = browser.new_context()

    page = context.new_page()

    return p, browser, context, page
