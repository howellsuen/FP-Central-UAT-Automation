import re
from helpers.select_utils import select_option_by_csv_value
from helpers.select_utils import is_field_already_selected


def add_address(page, client, folder_name):
    """
    Add Address using data from clients.csv
    """

    # ✅ FIX: wait for Add button instead of ambiguous "Address"
    page.get_by_role("button", name="Add").wait_for()

    # Click "Add"
    page.get_by_role("button", name="Add").click()

    # -------------------------
    # Address Type
    # -------------------------
    ADDRESS_TYPE_MAP = {
        "individual": "Residental",
        "corporate": "Correspondence",
    }

    client_type = client.get("Client Type", "").strip().lower()

    page.get_by_text(ADDRESS_TYPE_MAP[client_type], exact=False).click()

    # -------------------------
    # Address Lines (✅ safer)
    # -------------------------
    address = client["Address"]
    lines = [x.strip() for x in address.split(",")]
    print(f"Filling [{address}], [{lines[0]} + {lines[1]} + {lines[2]} + {lines[3]}]")

    # ✅ Fill fields
    page.get_by_label("Address Line 1").fill(f"{lines[0]}, {lines[1]}")
    page.get_by_label("Address Line 2").fill(lines[2])
    page.get_by_label("City").fill(lines[3])
    page.get_by_label("State").fill(lines[4])

    # -------------------------
    # Country
    # -------------------------
    label = "Country"
    csv_value = client["Residential Country"]
    field = page.get_by_label(label).last
    field.click()

    listbox = page.locator("div[id$='-items']:visible")

    pattern = re.compile(f"^{re.escape(csv_value)}\\b", re.IGNORECASE)

    print(f"Selecting [{csv_value}] for [{label}]")

    option = listbox.locator("div[role='option']").filter(has_text=pattern)

    option.first.click()

    page.screenshot(
        path=f"evidence/screenshots/{folder_name}/filled_client_address.png"
    )

    # -------------------------
    # Save
    # -------------------------
    dialog = page.locator("div[role='dialog']:visible").last

    save_btn = dialog.locator("button", has_text="Save")

    save_btn.wait_for()
    save_btn.scroll_into_view_if_needed()

    save_btn.click()

    page.screenshot(path=f"evidence/screenshots/{folder_name}/saved_client_address.png")

    # -------------------------
    # Next
    # -------------------------
    page.get_by_role("button", name="Next").click()
