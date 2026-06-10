import re


def select_consultants(page, client, folder_name):

    consultants = []

    if client.get("Consultant 1"):
        consultants.append(client["Consultant 1"])

    if client.get("Consultant 2"):
        consultants.append(client["Consultant 2"])

    if not consultants:
        return

    # Wait for the Consultant tab panel to be visible
    consultant_panel = page.get_by_role("tabpanel", name="Consultant")
    consultant_panel.wait_for()

    # Locate the consultant combobox inside the panel
    combobox = consultant_panel.locator("div[role='combobox']").first
    combobox.wait_for()

    for consultant in consultants:
        combobox.click()

        listbox = page.locator(
            "div[id$='-items']:visible, div[role='listbox']:visible"
        ).first
        listbox.wait_for()

        print(f"Selecting consultant: {consultant}")
        pattern = re.compile(re.escape(consultant), re.IGNORECASE)

        option = listbox.locator("div[role='option']").filter(has_text=pattern)

        if option.count() == 0:
            raise Exception(f"Consultant option not found: {consultant}")

        option.first.click()

    page.wait_for_timeout(1000)

    page.screenshot(path=f"evidence/screenshots/{folder_name}/selected_consultant.png")

    page.get_by_role("button", name="Next").click()
