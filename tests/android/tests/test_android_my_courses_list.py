# coding=utf-8

"""
    My Courses List Test Module
"""

from tests.android.pages.android_login import AndroidLogin
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.android.pages.android_new_landing import AndroidNewLanding
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidMyCoursesList:
    """
    My Courses List's Test Case
    """

    def test_start_my_courses_list_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that from Main Dashboard tapping Courses tab will load My Courses
                list(of specific logged in user) in its tab
        """

        setup_logging.info('-- Starting {} Test Case'.format(TestAndroidMyCoursesList.__name__))

        global_contents = Globals(setup_logging)
        android_new_landing_page = AndroidNewLanding(set_capabilities, setup_logging)
        android_login_page = AndroidLogin(set_capabilities, setup_logging)
        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        assert android_new_landing_page.on_screen() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
        assert android_new_landing_page.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME
        assert android_login_page.login(
            global_contents.login_user_name,
            global_contents.login_password,
            global_contents.is_first_time
        ) == Globals.WHATS_NEW_ACTIVITY_NAME
        setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))

        android_whats_new_page.navigate_features()
        assert android_whats_new_page.navigate_features().text == strings.WHATS_NEW_DONE
        assert android_whats_new_page.exit_features() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME
        assert android_main_dashboard_page.load_courses_tab()

    def test_validate_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that from Main Dashboard  tapping Courses tab will load My Courses
                contents(of specific logged in user) in its tab
            Verify that Courses tab/screen will show following header contents,
            Header Contents
                Profile icon
                "Courses" title
                Account Icon
            Courses Tab
            Discovery Tab
            Verify that My Courses(enrolled) List with followings in each course,
                Course image
                Course Name
                Course Start/End date
            "Looking for a new challenge?" label
            "Find a Course" button

        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)

        assert android_main_dashboard_page.get_profile_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_title_textview().text == strings.MAIN_DASHBOARD_SCREEN_TITLE
        assert android_main_dashboard_page.get_menu_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert android_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB

        if android_my_courses_list_page.get_my_courses_list_row():
            assert android_my_courses_list_page.get_my_courses_list_row()
            android_my_courses_list_page.get_contents_from_list()
            android_my_courses_list_page.scroll_course_list_and_click_find_course_button()
        else:
            setup_logging.info('No course enrolled by this user.')

        find_courses_message = android_my_courses_list_page.get_find_courses_message().text
        assert find_courses_message == strings.MY_COURSES_LIST_FIND_COURSES_MESSAGE
        find_courses_button = android_my_courses_list_page.get_find_course_button().text
        assert find_courses_button == strings.MY_COURSES_LIST_FIND_COURSES_BUTTON_ANDROID

    def test_load_course_details_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that tapping any course should load specific Course Dashboard screen
            Verity that from Course Dashboard tapping back should load My Courses List screen
            Verify that user should be able to scroll courses
            Verify on tapping "Find a Course" button will load Discovery screen
            Verity that from Course Dashboard tapping back should load My Courses List screen

        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        if android_my_courses_list_page.get_my_courses_list_row():
            course_dashboard_screen = android_my_courses_list_page.load_course_details_screen()
            assert course_dashboard_screen == global_contents.COURSE_DASHBOARD_ACTIVITY_NAME
            set_capabilities.back()
            assert android_main_dashboard_page.on_screen() == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME
            global_contents.swipe_screen(set_capabilities)

        course_discovery_screen = android_my_courses_list_page.load_discovery_screen()
        assert course_discovery_screen == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME
        # set_capabilities.back()
        assert android_main_dashboard_page.on_screen() == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME

    def test_landscape_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Change device orientation to Landscape mode
            Verify that from Main Dashboard tapping Courses tab will load My Courses
            list(of specific logged in user) in its tab
            Verify that from Main Dashboard  tapping Courses tab will load My Courses
            contents(of specific logged in user) in its tab
            Verify that Courses tab/screen will show following header contents,
            Header Contents
                Profile icon
                "Courses" title
                Account Icon
                Courses Tab
                Discovery Tab
            Verify that My Courses(enrolled) List with followings in each course,
                Course image
                Course Name
                Course Start/End date
            "Looking for a new challenge?" label
            "Find a Course" button
            Verify that tapping any course should load specific Course Dashboard screen
            Verity that from Course Dashboard tapping back should load My Courses List screen
            Verify that user should be able to scroll courses
            Verify on tapping "Find a Course" button will load Discovery screen
            Verity that from Course Dashboard tapping back should load My Courses List screen
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        global_contents.turn_orientation(set_capabilities, global_contents.LANDSCAPE_ORIENTATION)
        android_main_dashboard_page.load_courses_tab()

        assert android_main_dashboard_page.get_profile_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_title_textview().text == strings.COURSES_DISCOVERY_COURSES_TAB
        assert android_main_dashboard_page.get_menu_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert android_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB

        if android_my_courses_list_page.get_my_courses_list_row():
            assert android_my_courses_list_page.get_my_courses_list_row()
            android_my_courses_list_page.get_contents_from_list()
            course_dashboard_screen = android_my_courses_list_page.load_course_details_screen()
            assert course_dashboard_screen == global_contents.COURSE_DASHBOARD_ACTIVITY_NAME
            set_capabilities.back()
            assert android_main_dashboard_page.on_screen() == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME
            # global_contents.swipe_screen(set_capabilities)
            android_my_courses_list_page.scroll_course_list_and_click_find_course_button()

        else:
            setup_logging.info('No course enrolled by this user.')

        find_courses_message = android_my_courses_list_page.get_find_courses_message().text
        assert find_courses_message == strings.MY_COURSES_LIST_FIND_COURSES_MESSAGE
        find_courses_button = android_my_courses_list_page.get_find_course_button().text
        assert find_courses_button == strings.MY_COURSES_LIST_FIND_COURSES_BUTTON_ANDROID

        course_discovery_screen = android_my_courses_list_page.load_discovery_screen()
        assert course_discovery_screen == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME
        # set_capabilities.back()
        assert android_main_dashboard_page.on_screen() == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME

        global_contents.turn_orientation(set_capabilities, global_contents.PORTRAIT_ORIENTATION)

        setup_logging.info('-- Ending {} Test Case'.format(TestAndroidMyCoursesList.__name__))
