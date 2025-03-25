import allure

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class MyInfoPage(BasePage):
    PAGE_URL = Links.PERSONAL_PAGE
    INPUT_NAME = ("xpath", "//input[@name='firstName']")
    SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

    def change_name(self, name):
        with allure.step(f"Change Name"):
            first_name = self.wait.until(EC.element_to_be_clickable(self.INPUT_NAME))
            first_name.send_keys(Keys.COMMAND + "A")
            first_name.send_keys(Keys.BACKSPACE)
            first_name.send_keys(name)
            self.name = name

    @allure.step("Save Changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Changes Saved")
    def is_changes_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
        self.wait.until(EC.visibility_of_element_located(self.INPUT_NAME))
        self.wait.until(EC.text_to_be_present_in_element_value(self.INPUT_NAME, self.name))
