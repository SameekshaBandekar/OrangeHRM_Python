import os


def take_screenshot(driver, test_name):
    screenshot_path =  os.path.join(os.getcwd(), "reports", "screenshots")
    os.makedirs(screenshot_path, exist_ok=True)
    path = os.path.join(screenshot_path, f"{test_name}.png")
    driver.save_screenshot(path)
    return path