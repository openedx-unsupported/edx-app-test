"""
    My Courses List Test Module
"""
from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_my_courses_list import IosMyCoursesList
from tests.ios.pages.ios_login_smoke import IosLoginSmoke


class TestIosMyCoursesList(IosLoginSmoke):
    """
    My Courses List's Test Case
    """

    def test_validate_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify following contents on Header, Profile icon, "Courses" title, Account Icon
                Verify that My Courses(enrolled) List has following contents in each course,
                    Course Name, Course Start/End date
            Verify that "Looking for a new challenge?" label and "Find a Course" button are available
        """
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        ios_my_courses_list = IosMyCoursesList(set_capabilities, setup_logging)

        assert ios_main_dashboard_page.get_title_textview_portrait_mode().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        assert ios_main_dashboard_page.get_courses_tab().text == strings.SELECTED_BY_DEFAULT
        assert ios_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB

        assert ios_my_courses_list.get_my_courses_list_row()

        if ios_my_courses_list.get_my_courses_list_row():
            assert ios_my_courses_list.get_my_course_name()
            assert ios_my_courses_list.get_my_course_details()
        else:
            setup_logging.info('No course enrolled by this user.')

        # assert ios_my_courses_list.get_find_courses_message().text == strings.MY_COURSES_LIST_FIND_COURSES_MESSAGE
        # assert ios_my_courses_list.get_find_course_button().text == strings.MY_COURSES_LIST_FIND_COURSES_BUTTON_IOS

    def test_load_course_details_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that tapping any course should load specific Course Dashboard screen
            Verity that from Course Dashboard tapping back should load My Courses List screen
            Verify that user should be able to scroll courses
            Verify on tapping "Find a Course" button will load Discovery screen
            Verity that from Course Dashboard tapping back should load My Courses List screen

        """

        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        ios_my_courses_list = IosMyCoursesList(set_capabilities, setup_logging)

        if ios_my_courses_list.get_my_courses_list_row():
            course_name = ios_my_courses_list.get_my_courses_list_row().text
            assert ios_my_courses_list.load_course_details_screen().text in course_name
            set_capabilities.back()

        # assert ios_my_courses_list.load_discovery_screen().text == strings.COURSES_DISCOVERY_BROWSE_BY_SUBJECT_LABEL
        setup_logging.info(set_capabilities.context)
        assert ios_main_dashboard_page.load_courses_tab().text == strings.SELECTED_BY_DEFAULT

    def test_landscape_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Change device orientation to Landscape mode
                Verify that from Main Dashboard tapping Courses tab will load My Courses
                list(of specific logged in user) in its tab
                Verify following contents on Header, Profile icon, "Courses" title, Account Icon
                Verify that My Courses(enrolled) List has following contents in each course,
                    Course Name, Course Start/End date
                Verify that "Looking for a new challenge?" label and "Find a Course" button are available
                Verify that tapping any course should load specific Course Dashboard screen
                Verity that from Course Dashboard tapping back should load My Courses List screen
                Verify that user should be able to scroll courses
                Verify on tapping "Find a Course" button will load Discovery screen
                Verity that from Course Dashboard tapping back should load My Courses List screen
                Verify user is able to change device orientation back to Portrait Mode
        """

        global_contents = Globals(setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        ios_my_courses_list = IosMyCoursesList(set_capabilities, setup_logging)

        global_contents.turn_orientation(set_capabilities, global_contents.LANDSCAPE_ORIENTATION)

        # assert ios_main_dashboard_page.get_profile_icon().text == strings.MAIN_DASHBOARD_PROFILE
        assert ios_main_dashboard_page.get_title_textview_landscape_mode().text == strings.BLANK_FIELD
        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        assert ios_main_dashboard_page.get_courses_tab().text == strings.SELECTED_BY_DEFAULT
        assert ios_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB

        if ios_my_courses_list.get_my_courses_list_row_landscape():
            assert ios_my_courses_list.get_my_courses_list_row_landscape()
            assert ios_my_courses_list.get_my_course_details()
            course_name = ios_my_courses_list.get_my_courses_list_row_landscape().text
            assert ios_my_courses_list.get_my_courses_list_row_landscape().text in course_name
            set_capabilities.back()
        else:
            setup_logging.info('No course enrolled by this user.')

        # assert ios_my_courses_list.get_find_courses_message().text == strings.MY_COURSES_LIST_FIND_COURSES_MESSAGE
        # assert ios_my_courses_list.get_find_course_button().text == strings.MY_COURSES_LIST_FIND_COURSES_BUTTON_IOS

        ios_my_courses_list.load_discovery_screen()
        setup_logging.info(set_capabilities.context)
        assert ios_main_dashboard_page.load_courses_tab().text == strings.SELECTED_BY_DEFAULT

    def test_logout_smoke(self, set_capabilities, setup_logging):
        """
        Verify user is able to change device orientation back to Portrait Mode
        Verify user is able to logout
        Verify after logout landing page should visible
        """
        global_contents = Globals(setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        global_contents.turn_orientation(set_capabilities, global_contents.PORTRAIT_ORIENTATION)
        set_capabilities.back()
        assert ios_main_dashboard_page.load_account_screen().text == strings.PROFILE_SCREEN_TITLE
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN
        assert ios_main_dashboard_page.load_ios_landing_page(
            set_capabilities, setup_logging).text == strings.NEW_LANDING_MESSAGE_IOS
        setup_logging.info('{} is successfully logged out'.format(global_contents.login_user_name))
        setup_logging.info('-- Ending Test Case')
