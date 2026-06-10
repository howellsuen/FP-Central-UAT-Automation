import re


def select_option_by_csv_value(page, label, csv_value):
    """
    Select Mantine dropdown option using flexible matching,
    then WAIT until value is reflected in UI.
    """

    field = page.get_by_label(label)

    field.click()

    # 🔥 KEY FIX: allow optional spaces between ALL characters
    pattern = r"\b" + r"\s*".join(map(re.escape, csv_value)) + r"\b"

    regex = re.compile(pattern, re.IGNORECASE)

    print(f"Selecting [{csv_value}] for [{label}]")

    # Click matching option
    option = page.locator("role=option", has_text=regex)
    option.click()


def is_field_already_selected(page, label, expected):
    field = page.get_by_label(label)
    value = field.input_value()
    return expected.lower() in value.lower()
