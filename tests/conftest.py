"""
   Module helps to login where ever needed, accessible in all test cases
"""
import pytest
from pages.new_logistration import NewLogistration
from pages.login import Login
from testdata.input_data import InputData
from common.globals import Globals
from common.strings import Strings


@pytest.fixture(scope="module")
def login(set_capabilities):
    """
    Login will login user based on env given, it will be reusable in tests
    """

    new_logistration_page = NewLogistration(set_capabilities)
    login_page = Login(set_capabilities)

    if InputData.target_environment == Strings.ANDROID:
        assert new_logistration_page.load_app() == Globals.NEW_LOGISTRATION_ACTIVITY_NAME
        assert new_logistration_page.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME
        print('Login screen successfully loaded')
        login_output = login_page.login(InputData.login_user_name, InputData.login_password)
        assert login_output == Globals.WHATS_NEW_ACTIVITY_NAME

    elif InputData.target_environment == Strings.IOS:
        assert new_logistration_page.load_app().text == Strings.NEW_LOGIS_DISCOVER_COURSES
        assert new_logistration_page.load_login_screen().text == Strings.LOGIN_SCREEN_TITLE
        print('Login screen successfully loaded')
        login_output = login_page.login(InputData.login_user_name, InputData.login_password).text
        assert login_output == Strings.WHATS_NEW_IOS_SCREEN_TITLE

    print(InputData.login_user_name, 'is successfully logged in')
    return True
