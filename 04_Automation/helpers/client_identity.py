from helpers.select_utils import select_option_by_csv_value


def fill_client_identity(page, client, folder_name):

    # Wait until Client Identity panel is ready
    page.get_by_label("ID Type").wait_for()

    # ID Type (HKID → HK ID 香港身份證)
    if client.get("ID Type"):
        select_option_by_csv_value(
            page,
            label="ID Type",
            csv_value=client["ID Type"],
        )

    # ID Number
    if client.get("ID Number"):
        page.get_by_label("Please enter the ID").fill(client["ID Number"])

    # ID Issue Country (Hong Kong → Hong Kong 香港)
    if client.get("Id Issue Country"):
        select_option_by_csv_value(
            page,
            label="ID Issue Country",
            csv_value=client["Id Issue Country"],
        )

    page.screenshot(
        path=f"evidence/screenshots/{folder_name}/filled_client_identity.png"
    )

    # Next
    page.get_by_role("button", name="Next").click()
