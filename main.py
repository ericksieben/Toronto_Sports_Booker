import browser_utils
import webpage_data
import user_data

# Initiate the browser
browser = browser_utils.get_chrome_browser()

# Login
browser_utils.login(
    browser
)

# Go to pickleball reservations
browser_utils.go_to_sport(
    browser,
    webpage_data.VALUES["SPORT_RESERVATION_NAME"]
)
