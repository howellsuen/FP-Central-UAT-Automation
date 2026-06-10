def login(page, base_url, email, password, folder_name):

    # Reusable login function.
    # Supports future OTP change via manual checkpoint.
    base_url = base_url.rstrip("/")
    page.goto(f"{base_url}/login")

    page.get_by_label("Email").fill(email)

    # Password login (current)
    if page.get_by_label("Password").is_visible():
        page.get_by_label("Password").fill(password)

    page.screenshot(path=f"evidence/screenshots/{folder_name}/login_before_signin.png")

    page.get_by_role("button", name="Sign in").click()

    # OTP login (future-proof)
    # elif page.get_by_role("button", name="Send OTP").is_visible():
    #     page.get_by_role("button", name="Send OTP").click()
    #     input("⏸ Enter OTP manually, then press ENTER to continue")

    # Wait until home appears
    page.wait_for_selector("text=Home")

    page.screenshot(path=f"evidence/screenshots/{folder_name}/login_after_signin.png")
