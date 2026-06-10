from playwright.sync_api import sync_playwright
from helpers.auth import login
from helpers.browser import get_page
from helpers.csv_loader import load_csv

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE_URL = "https://demo.megafintech-hk.com"  # 🔁 replace with real demo URL
FOLDER_NAME = "TC_CLIENT_001"


def run_tc_client_001():
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

    try:
        # ===============================
        # Step 1: Open vendor website
        # ===============================
        page.goto(BASE_URL)

        # ===============================
        # Step 2: Login
        # ===============================
        page.get_by_label("Email").fill("oliver.kwan@fwd.com")
        page.get_by_label("Password").fill("fwdts")
        page.screenshot(path="evidence/screenshots/TC_CLIENT_001_01_login.png")
        page.get_by_role("button", name="Sign in").click()

        # Wait until home appears
        page.wait_for_selector("text=Home")

        page.screenshot(path="evidence/screenshots/TC_CLIENT_001_02_after_login.png")

        # ===============================
        # Step 3: Navigate to Create Client
        # ===============================
        page.click("text=Client")
        page.click("text=Add New")

        page.wait_for_selector("text=New Client")

        # ===============================
        # Step 4: Fill Client Information
        # ===============================

        # Wait until Client Types section is visible
        page.get_by_text("Client Types").wait_for()

        # Select Individual client type
        page.get_by_text("Individual 個人", exact=True).click()

        # (Optional) Assertion – make sure it's selected
        page.locator("label:has-text('Individual 個人')").wait_for(state="attached")

        # Click Next
        page.get_by_role("button", name="Next").click()

        page.fill("#lastName", "CHAN")
        page.fill("#firstName", "TAI MAN")

        page.select_option("#idType", "HKID")
        page.fill("#idNumber", "A123456(7)")

        page.screenshot(path="evidence/screenshots/TC_CLIENT_001_03_before_submit.png")

        # ===============================
        # Step 5: Submit
        # ===============================
        page.click("text=Submit")

        # ===============================
        # Step 6: Validate Result
        # ===============================
        page.wait_for_selector("text=Client created successfully")

        page.screenshot(path="evidence/screenshots/TC_CLIENT_001_04_success.png")

        print("✅ TC_CLIENT_001 — PASS")

    except Exception as e:
        page.screenshot(path="evidence/screenshots/TC_CLIENT_001_ERROR.png")
        print("❌ TC_CLIENT_001 — FAIL")
        print(str(e))

    finally:
        context.close()  # ✅ saves video
        browser.close()


if __name__ == "__main__":
    run_tc_client_001()
