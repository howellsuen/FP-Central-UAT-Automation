from helpers.select_utils import select_option_by_csv_value
from helpers.select_utils import is_field_already_selected


def fill_basic_info(page, client, folder_name):
    """
    Fill Client > Basic Info section using one CSV row (dict).
    """

    # ✅ Wait until Basic Info form is ready (strict-safe)
    page.get_by_label("English Name").wait_for()

    # -------------------------
    # Salutation ✅ FIXED
    # -------------------------
    if client.get("Salutation"):
        select_option_by_csv_value(
            page,
            label="Saluation",
            csv_value=client["Salutation"],  # "Mr" → matches "Mr. 先生"
        )

    # -------------------------
    # English / Chinese Name
    # -------------------------
    page.get_by_label("English Name").fill(client["Name"])

    if client.get("Chinese Name"):
        page.get_by_label("Chinese Name").fill(client["Chinese Name"])

    # -------------------------
    # Date of Birth
    # -------------------------
    if client.get("Birthday"):
        page.get_by_label("Date of Birth").fill(client["Birthday"])

    # -------------------------
    # Phone
    # -------------------------
    if client.get("Mobile"):
        page.get_by_label("Phone Number").fill(client["Mobile"])

    # -------------------------
    # Gender ✅ FIXED
    # -------------------------
    if client.get("Gender"):
        select_option_by_csv_value(
            page,
            label="Gender",
            csv_value=client["Gender"],
        )

    # -------------------------
    # Occupation
    # -------------------------
    if client.get("Occupation"):
        page.get_by_label("Occupation").fill(client["Occupation"])

    # -------------------------
    # Email
    # -------------------------
    if client.get("Email"):
        page.get_by_label("Email").fill(client["Email"])

    # -------------------------
    # Education Level ✅ FIXED
    # -------------------------
    if client.get("Education Level"):
        select_option_by_csv_value(
            page,
            label="Education Level",
            csv_value=client["Education Level"],
        )

    # -------------------------
    # Marital Status ✅ FIXED
    # -------------------------
    if client.get("Marital Status"):
        select_option_by_csv_value(
            page,
            label="Marital Status",
            csv_value=client["Marital Status"],
        )

    # -------------------------
    # Nationality
    # -------------------------
    if client.get("Nationality"):
        if not is_field_already_selected(page, "Nationality", client["Nationality"]):
            select_option_by_csv_value(
                page,
                label="Nationality",
                csv_value=client["Nationality"],
            )

    # -------------------------
    # Residential Country
    # -------------------------
    if client.get("Residential Country"):
        if not is_field_already_selected(
            page, "Residential Country", client["Residential Country"]
        ):
            select_option_by_csv_value(
                page,
                label="Residential Country",
                csv_value=client["Residential Country"],
            )

    # -------------------------
    # Country of Birth
    # -------------------------
    if client.get("Place of Birth"):
        if not is_field_already_selected(
            page, "Country of Birth", client["Place of Birth"]
        ):
            select_option_by_csv_value(
                page,
                label="Country of Birth",
                csv_value=client["Place of Birth"],
            )

        # page.keyboard.press("Tab")

        page.wait_for_timeout(1000)

        page.screenshot(
            path=f"evidence/screenshots/{folder_name}/filled_client_basic_info.png"
        )

    # -------------------------
    # Next
    # -------------------------
    page.get_by_role("button", name="Next").click()
