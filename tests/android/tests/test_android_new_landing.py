# coding=utf-8
"""
    New Landing Test Module
"""

from tests.common import strings
from tests.common.globals import Globals
from tests.android.pages.android_new_landing import AndroidNewLanding


class TestAndroidNewLanding:
    """
    New Landing screen's Test Case
    """

    def test_start_new_landing_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify New Landing screen is loaded successfully
        """

        setup_logging.info('-- Starting {} Test Case'.format(TestAndroidNewLanding.__name__))
        global_contents = Globals(setup_logging)
        android_new_landing = AndroidNewLanding(set_capabilities, setup_logging)

        assert android_new_landing.on_screen() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Verify following contents are visible on screen,
            "edX logo", "Message" text-field, "Search Courses" edit-field, "Register" button, "Sign In" button
        Verify all contents have their default values
        """

        android_new_landing = AndroidNewLanding(set_capabilities, setup_logging)

        assert android_new_landing.get_edx_logo().text == strings.BLANK_FIELD
        assert android_new_landing.get_welcome_message().text == strings.NEW_LANDING_MESSAGE_ANDROID
        assert android_new_landing.get_search_course_icon().text == strings.NEW_LANDING_SEARCH_COURSES
        assert android_new_landing.get_search_course_editfield().text == strings.NEW_LANDING_SEARCH_COURSES
        assert android_new_landing.get_signin_button().text == strings.NEW_LANDING_LOG_IN
        assert android_new_landing.get_register_button().text == strings.NEW_LANDING_CREATE_YOUR_ACCOUNT

    def test_search_courses_smoke(self, set_capabilities, setup_logging):
        """
        Verifies that user can search courses, and back to New Landing screen
        """

        global_contents = Globals(setup_logging)
        android_new_landing = AndroidNewLanding(set_capabilities, setup_logging)

        search_courses_screen = android_new_landing.search_courses(global_contents.new_landing_search_courses)
        assert search_courses_screen == global_contents.WITHOUT_LOGIN_DISCOVERY_ACTIVITY_NAME
        set_capabilities.back()
        assert android_new_landing.on_screen() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME

    def test_back_and_forth_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify tapping "Login" will load "Sign In" screen
                Verify tapping back/cross icon from 'Sign In' screen navigate user
                    back to 'New Landing' screen
                Verify tapping "Create your Account" loads "Register" screen
                Verify tapping back/cross icon from "Register" screen
                    navigate user back to 'New Landing' screen
        """

        android_new_landing = AndroidNewLanding(set_capabilities, setup_logging)

        assert android_new_landing.back_and_forth_login()
        assert android_new_landing.back_and_forth_register()

        setup_logging.info('-- Ending {} Test Case'.format(TestAndroidNewLanding.__name__))
