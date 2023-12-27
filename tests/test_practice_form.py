from pages.registration_page import RegistationPage
import allure
from data.users import ivan






@allure.title("Successful fill form")
def test_form_submit_checker():

    with allure.step("Open registrations form"):

        registration_page = RegistationPage()

    with allure.step("Fill form"):
        registration_page.open()

    # WHEN
        registration_page.register(ivan)

    # THEN
    with allure.step("Check form results"):
        registration_page.user_register_form(ivan)