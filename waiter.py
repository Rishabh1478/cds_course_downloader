from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def waiter(driver, flocator):
    """Wait for the element specified by the XPath locator."""
    wait_1 = WebDriverWait(driver, 10)
    flocator = (By.XPATH, flocator)
    element = wait_1.until(EC.presence_of_element_located(flocator))
    return element