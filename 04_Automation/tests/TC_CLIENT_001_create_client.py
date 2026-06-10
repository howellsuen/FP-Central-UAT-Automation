from helpers.auth import login
from helpers.browser import get_page
from helpers.csv_loader import load_csv
from helpers.client_identity import fill_client_identity
from helpers.company_client_basic_info import fill_company_basic_info
from helpers.client_basic_info import fill_basic_info
from helpers.client_address import add_address
from helpers.client_consultant import select_consultants

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE_URL = "https://demo.megafintech-hk.com"  # 🔁 replace with real demo URL


def run_tc_client_001():
    users = load_csv("data/login_users.csv")
    clients = load_csv("data/clients.csv")
    user = users[0]
    client = clients[0]
    # for user in users:
    #     for client in clients:
    print(f"▶ TC_CLIENT_001 | " f"{client['Client Code']} | " f"{user['role']}")
    folder_name = f"TC_CLIENT_001_{user['test_user_id']}_{client['Client Code']}"
    p, browser, context, page = get_page()

    try:
        # ===============================
        # Step 1: Login (REUSED)
        # ===============================
        login(
            page=page,
            base_url=BASE_URL,
            email=user["email"],
            password=user["password"],
            folder_name=folder_name,
        )

        # ===============================
        # Step 2: Navigate to Create Client
        # ===============================
        page.click("text=Client")
        page.click("text=Add New")
        page.wait_for_selector("text=New Client")

        # ===============================
        # Step 3: Select Client Type
        # ===============================
        page.get_by_text("Client Types").wait_for()

        CLIENT_TYPE_LABEL_MAP = {
            "individual": "Individual 個人",
            "corporate": "Corporate 公司",
            "staff": "Staff 員工",
            "consultant": "Consultant 經紀",
        }

        client_type_key = client.get("Client Type", "").strip().lower()

        label_text = CLIENT_TYPE_LABEL_MAP.get(client_type_key)

        if not label_text:
            raise ValueError(f"Unsupported Client Type: {client['Client Type']}")

        page.get_by_text(label_text, exact=True).click()

        page.screenshot(
            path=f"evidence/screenshots/{folder_name}/selected_client_type.png"
        )

        page.get_by_role("button", name="Next").click()

        # ===============================
        # Step 4: Fill Client Identity
        # ===============================
        fill_client_identity(page, client, folder_name)

        # ===============================
        # Step 5: Fill Client Basic Info
        # ===============================
        if client_type_key == "corporate":
            fill_company_basic_info(page, client, folder_name)
        else:
            fill_basic_info(page, client, folder_name)

        # ===============================
        # Step 6: Address Section
        # ===============================
        add_address(page, client, folder_name)

        # ===============================
        # Step 7: Consultant Section
        # ===============================
        select_consultants(page, client, folder_name)

        # ===============================
        # Step 8: Confirm
        # ===============================
        page.get_by_role("button", name="Confirm").wait_for()
        page.get_by_role("button", name="Confirm").click()

        page.wait_for_selector("text=add successfully")

        page.screenshot(
            path=f"evidence/screenshots/{folder_name}/{user['test_user_id']}_success.png"
        )

        print(f"✅ TC_CLIENT_001 PASS ({user['role']})")

    except Exception as e:
        page.screenshot(
            path=f"evidence/screenshots/{folder_name}/{user['test_user_id']}_error.png"
        )
        print(f"❌ TC_CLIENT_001 FAIL ({user['role']})")
        print(e)

    finally:
        context.close()
        browser.close()
        p.stop()


if __name__ == "__main__":
    run_tc_client_001()
