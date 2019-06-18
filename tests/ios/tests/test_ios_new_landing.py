# coding=utf-8
"""
    New Landing Test Module
"""

from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_new_landing import IosNewLanding


class TestIosNewLanding(object):
    """
    New Landing screen's Test Case
    """

    def test_start_new_landing_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify New Landing screen is loaded successfully
        """

        setup_logging.info('-- Starting {} Test Case'.format(TestIosNewLanding.__name__))

        ios_new_landing = IosNewLanding(set_capabilities, setup_logging)
        assert ios_new_landing.get_welcome_message().text == strings.NEW_LANDING_MESSAGE_IOS

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Verify following contents are visible on screen, 
            "edX logo", "Message" text-field, "Search Courses" edit-field, "Register" button, "Sign In" button
        Verify all contents have their default values
        """

        ios_new_landing = IosNewLanding(set_capabilities, setup_logging)

        assert ios_new_landing.get_edx_logo().text == strings.LOGIN_EDX_LOGO
        assert ios_new_landing.get_welcome_message().text == strings.NEW_LANDING_MESSAGE_IOS
        assert ios_new_landing.get_search_course_editfield().text == strings.NEW_LANDING_SEARCH_COURSES
        assert ios_new_landing.get_signin_button().text == strings.NEW_LANDING_LOG_IN
        assert ios_new_landing.get_register_button().text == strings.NEW_LANDING_CREATE_YOUR_ACCOUNT

    def test_search_courses_smoke(self, set_capabilities, setup_logging):
        """
        Verifies that user can search courses, and back to New Landing screen
        """

        global_contents = Globals(setup_logging)
        ios_new_landing = IosNewLanding(set_capabilities, setup_logging)
        search_courses = ios_new_landing.search_courses(global_contents.new_landing_search_courses).text
        assert search_courses == strings.DISCOVER_CANCEL
        ios_new_landing.cancel_discovery_screen()
        assert ios_new_landing.get_welcome_message().text == strings.NEW_LANDING_MESSAGE_IOS

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

        ios_new_landing = IosNewLanding(set_capabilities, setup_logging)
        assert ios_new_landing.back_and_forth_login()
        assert ios_new_landing.back_and_forth_register()

        setup_logging.info('-- Ending {} Test Case'.format(TestIosNewLanding.__name__))

    def test_landscape_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Landscape support is added for New Landing screen with following cases,
                     Change device orientation to Landscape mode
                     Verify all screen contents
                     Verify search courses
                     Verify back and forth from Login screen
                     Verify back and forth from Register Screen
        """

        ios_new_landing = IosNewLanding(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        global_contents.turn_orientation(set_capabilities, global_contents.LANDSCAPE_ORIENTATION)
        assert ios_new_landing.get_edx_logo().text == strings.LOGIN_EDX_LOGO
        assert ios_new_landing.get_welcome_message().text == strings.NEW_LANDING_MESSAGE_IOS
        assert ios_new_landing.get_search_course_editfield().text == strings.NEW_LANDING_SEARCH_COURSES
        assert ios_new_landing.get_signin_button().text == strings.NEW_LANDING_LOG_IN
        assert ios_new_landing.get_register_button().text == strings.NEW_LANDING_CREATE_YOUR_ACCOUNT

        search_courses = ios_new_landing.search_courses(global_contents.new_landing_search_courses).text
        assert search_courses == strings.DISCOVER_CANCEL
        ios_new_landing.cancel_discovery_screen()
        assert ios_new_landing.get_welcome_message().text == strings.NEW_LANDING_MESSAGE_IOS

        assert ios_new_landing.back_and_forth_login()
        assert ios_new_landing.back_and_forth_register()

        global_contents.turn_orientation(set_capabilities, global_contents.PORTRAIT_ORIENTATION)
