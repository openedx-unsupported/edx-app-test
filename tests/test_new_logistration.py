"""
    New Logistrtion Test Module
"""
from pages.new_logistration import NewLogistration
from common.strings import Strings
from common.globals import Globals
from testdata.input_data import InputData


class TestNewLogistration:
    """
    New Logistration screen's Test Cases
    """
    @staticmethod
    def test_start_new_logistration_smoke(set_capabilities):
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

    @staticmethod
    def test_ui_elements_smoke(set_capabilities):
        """
        Scenarios:
                Verify "edX logo", "Discover Courses", "Register" & "Sign In"
                      fields are visible on screen 
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

    @staticmethod
    def test_back_and_forth_smoke(set_capabilities):
        """
        Scenarios:
                Verify tapping "Sign In" loads Sign In screen
                Verify tapping back icon from 'Sign In' screen navigate user
                    back to 'New Logistration' screen.
                Verify tapping "Register" loads Register screen
                Verify tapping back icon from 'Register' screen navigate user
                    back to 'New Logistration' screen. 
                Verify tapping "Discover Courses" loads Discovery screen
                Verify tapping back icon from 'Discover Courses' screen
                    navigate user back to 'New Logistration' screen.
        """
        new_logistration_page = NewLogistration(set_capabilities)
        assert new_logistration_page.back_and_forth_login()
        assert new_logistration_page.back_and_forth_register()
        assert new_logistration_page.back_and_forth_dicover_courses()

