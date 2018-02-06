"""
    New Logistrtion Test Module
"""

from common.globals import Globals
from android.pages.android_new_logistration import AndroidNewLogistration
from common import strings

class TestAndroidNewLogistration:
    """
    New Logistration screen's Test Cases
    """

    def test_start_new_logistration_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify New Logistration screen is loaded successfully
        """

        driver = set_capabilities
        log = setup_logging
        log.info('-- Starting {} Test Case'.format(TestAndroidNewLogistration.__name__))

        android_new_logistration_page =  AndroidNewLogistration(set_capabilities, setup_logging)
        assert android_new_logistration_page.load_app() == Globals.NEW_LOGISTRATION_ACTIVITY_NAME

        log.info('Into New Logistration screen')

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify "edX logo", "Discover Courses", "Register" & "Sign In"
                      fields are visible on screen 
                Verify all screen contents have their default values
        """

        android_new_logistration_page = AndroidNewLogistration(set_capabilities, setup_logging)

        image_edx_logo = android_new_logistration_page.get_edx_logo()
        assert image_edx_logo is not None

        button_discover_courses = android_new_logistration_page.get_discover_course_button()
        assert button_discover_courses is not None
        assert button_discover_courses.text == strings.NEW_LOGIS_DISCOVER_COURSES

        button_login = android_new_logistration_page.get_register_button()
        assert button_login is not None
        assert button_login.text == strings.NEW_LOGIS_REGISTER

        button_register = android_new_logistration_page.get_signin_button()
        assert button_register is not None
        assert button_register.text == strings.NEW_LOGIS_LOGIN

    def test_back_and_forth_smoke(self, set_capabilities, setup_logging):
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

        log = setup_logging
        android_new_logistration_page = AndroidNewLogistration(set_capabilities, setup_logging)

        assert android_new_logistration_page.back_and_forth_login()
        assert android_new_logistration_page.back_and_forth_register()
        assert android_new_logistration_page.back_and_forth_dicover_courses()


        log.info('-- Ending {} Test Case'.format(TestAndroidNewLogistration.__name__))
