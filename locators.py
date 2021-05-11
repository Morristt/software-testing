from selenium.webdriver.common.by import By

locator = {
    "sign_in_link": (By.CLASS_NAME, "login"),
    "email_field": (By.ID, "email_create"),
    "create_account_button": (By.ID, "SubmitCreate"),
    "gender_radiobutton": (By.ID, "id_gender1"),
    "firstname": (By.ID, "customer_firstname"),
    "lastname": (By.ID, "customer_lastname"),
    "password": (By.ID, "passwd"),
    "days_dropdown": (By.ID, "days"),
    "months_dropdown": (By.ID, "months"),
    "years_dropdown": (By.ID, "years"),
    "newsletter_checkbox": (By.ID, "newsletter"),
    "optin_checkbox": (By.ID, "optin"),
    "address": (By.ID, "address1"),
    "city": (By.ID, "city"),
    "state_dropdown": (By.ID, "id_state"),
    "postcode": (By.ID, "postcode"),
    "mobile": (By.ID, "phone_mobile"),
    "register_button": (By.ID, "submitAccount"),
    "logout_button": (By.XPATH, "//*[@id='header']/div[2]/div/div/nav/div[2]/a"),
    "email": (By.ID, "email"),
    "login_button": (By.ID, "SubmitLogin"),
    "search": (By.ID, "search_query_top"),
    "search_botton": (By.CLASS_NAME, "button-search")
}
