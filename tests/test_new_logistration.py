from pages.new_logistration import NewLogistration
from common.strings import Strings
from common.globals import Globals
from testdata.input_data import InputData


class TestNewLogistration():
    """
    New Logistration screen's Test Case
    """

    def test_start_new_logistration_smoke(self, set_capabilities):
        """
        Scenarios:
            Verify New Logistration screen is loaded successfully
        """

        print('-- Starting ', TestNewLogistration.__name__, 'Test Case')
        new_logistration_page = NewLogistration(set_capabilities)

        if InputData.target_environment == Strings.ANDROID:
            assert new_logistration_page.load_app() == Globals.NEW_LOGISTRATION_ACTIVITY_NAME
        elif InputData.target_environment == Strings.IOS:
            assert new_logistration_page.load_app().text == Strings.NEW_LOGIS_DISCOVER_COURSES
        print("Into New Logistration screen ")

    def test_ui_elements_smoke(self, set_capabilities):
        """
        Scenarios:
                Verify "edX logo", "Discover Courses", "Register" & "Sign In" fields are visible on screen 
                Verify all screen contents have their default values
        """

        new_logistration_page = NewLogistration(set_capabilities)

        imgage_edx_logo = new_logistration_page.get_edx_logo()
        assert imgage_edx_logo is not None
        if InputData.target_environment == Strings.IOS:
            assert imgage_edx_logo.text == Strings.NEW_LOGIS_EDX_LOGO

        button_discover_courses = new_logistration_page.get_discover_course_button()
        assert button_discover_courses is not None
        assert button_discover_courses.text == Strings.NEW_LOGIS_DISCOVER_COURSES

        button_login = new_logistration_page.get_register_button()
        assert button_login is not None
        assert button_login.text == Strings.NEW_LOGIS_REGISTER

        button_register = new_logistration_page.get_signin_button()
        assert button_register is not None
        assert button_register.text == Strings.NEW_LOGIS_LOGIN

        print('-- Ending ', TestNewLogistration.__name__, 'Test Case')