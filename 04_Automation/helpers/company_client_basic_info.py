from helpers.select_utils import select_option_by_csv_value
from helpers.select_utils import is_field_already_selected


def fill_company_basic_info(page, client, folder_name):
    """
    Fill Client > Basic Info section for corporate clients.
    """

    # ✅ Wait until Basic Info form is ready
    page.get_by_label("English Name (Company Name)").wait_for()

    # -------------------------
    # English / Chinese Company Name
    # -------------------------
    if client.get("Name"):
        page.get_by_label("English Name (Company Name)").fill(client["Name"])

    if client.get("Chinese Name"):
        page.get_by_label("Chinese Name (Company Name)").fill(client["Chinese Name"])

    # -------------------------
    # Phone
    # -------------------------
    if client.get("Phone"):
        page.get_by_label("Phone Number").fill(client["Phone"])

    # -------------------------
    # Email
    # -------------------------
    if client.get("Email"):
        page.get_by_label("Email").fill(client["Email"])

    # -------------------------
    # Contact Person
    # -------------------------
    if client.get("Contact Person - Name"):
        page.get_by_label("Contact Person").fill(client["Contact Person - Name"])

    # -------------------------
    # Parent Company
    # -------------------------
    if client.get("Parent Company"):
        select_option_by_csv_value(
            page,
            label="Parent Company",
            csv_value=client["Parent Company"],
        )

    # -------------------------
    # Professional Investor
    # -------------------------
    if client.get("Professional Investor"):
        value = str(client["Professional Investor"]).strip().lower()
        if value in ("yes", "true", "1", "y"):
            page.get_by_label("Professional Investor").click()

    page.wait_for_timeout(500)

    page.screenshot(
        path=f"evidence/screenshots/{folder_name}/filled_company_basic_info.png"
    )

    # -------------------------
    # Next
    # -------------------------
    page.get_by_role("button", name="Next").click()
