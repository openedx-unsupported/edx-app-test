"""
    My Courses List Test Module
"""

from tests.android.pages.android_login_smoke import AndroidLoginSmoke
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidMyCoursesList(AndroidLoginSmoke):
    """
    My Courses List's Test Case
    """

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

        global_contents = Globals(setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        assert android_main_dashboard_page.get_my_courses_dropdown().text == strings.MAIN_DASHBOARD_MY_COURSES_DROPDOWN
        learn_tab = android_main_dashboard_page.get_all_tabs()[1]
        assert learn_tab.text == 'Learn'
        assert learn_tab.get_attribute('selected') == strings.TRUE

        discover_tab = android_main_dashboard_page.get_all_tabs()[0]
        assert discover_tab.text == 'Discover'
        assert discover_tab.get_attribute('selected') == strings.FALSE

        profile_tab = android_main_dashboard_page.get_all_tabs()[2]
        assert profile_tab.text == 'Profile'
        assert profile_tab.get_attribute('selected') == strings.FALSE

        if android_my_courses_list_page.get_my_courses_list_row():
            course_name = android_my_courses_list_page.get_second_course().text
            android_my_courses_list_page.get_second_course().click()
        else:
            setup_logging.info('No course enrolled by this user.')

        assert course_name in android_course_dashboard_page.course_dashboard_course_title().text
        assert android_course_dashboard_page.course_dashboard_toolbar_dismiss_button().get_attribute(
            'clickable') == strings.TRUE
        android_course_dashboard_page.course_dashboard_toolbar_dismiss_button().click()
        assert android_main_dashboard_page.on_screen() == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME

        discover_tab = android_main_dashboard_page.get_all_tabs()[0]
        assert discover_tab.text == 'Discover'
        assert discover_tab.get_attribute('selected') == strings.FALSE
        discover_tab.click()
        assert discover_tab.get_attribute('selected') == strings.TRUE

        learn_tab = android_main_dashboard_page.get_all_tabs()[1]
        assert learn_tab.text == strings.MAIN_DASHBOARD_LEARN_TAB
        learn_tab.click()
        assert learn_tab.get_attribute('selected') == strings.TRUE

    # @pytest.mark.skip(reason="Not getting any element to scroll in landscape mode, will figure it out later")
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
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        global_contents.turn_orientation(set_capabilities, global_contents.LANDSCAPE_ORIENTATION)
        assert android_main_dashboard_page.get_my_courses_dropdown().text == strings.MAIN_DASHBOARD_MY_COURSES_DROPDOWN
        learn_tab = android_main_dashboard_page.get_all_tabs()[1]
        assert learn_tab.text == strings.MAIN_DASHBOARD_LEARN_TAB
        assert learn_tab.get_attribute('selected') == strings.TRUE

        discover_tab = android_main_dashboard_page.get_all_tabs()[0]
        assert discover_tab.text == strings.DISCOVER_COURSES_SCREEN_TITLE
        assert discover_tab.get_attribute('selected') == strings.FALSE

        profile_tab = android_main_dashboard_page.get_all_tabs()[2]
        assert profile_tab.text == strings.PROFILE_SCREEN_TITLE
        assert profile_tab.get_attribute('selected') == strings.FALSE

        if android_my_courses_list_page.get_my_courses_list_row():
            course_name = android_my_courses_list_page.get_first_course().text
            android_my_courses_list_page.get_first_course().click()
        else:
            setup_logging.info('No course enrolled by this user.')

        assert course_name in android_course_dashboard_page.course_dashboard_course_title().text
        assert android_course_dashboard_page.course_dashboard_toolbar_dismiss_button().get_attribute(
            'clickable') == strings.TRUE
        android_course_dashboard_page.course_dashboard_toolbar_dismiss_button().click()
        assert android_main_dashboard_page.on_screen() == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME

        discover_tab = android_main_dashboard_page.get_all_tabs()[0]
        assert discover_tab.text == strings.DISCOVER_COURSES_SCREEN_TITLE
        assert discover_tab.get_attribute('selected') == strings.FALSE
        discover_tab.click()
        assert discover_tab.get_attribute('selected') == strings.TRUE

        learn_tab = android_main_dashboard_page.get_all_tabs()[1]
        assert learn_tab.text == strings.MAIN_DASHBOARD_LEARN_TAB
        learn_tab.click()
        assert learn_tab.get_attribute('selected') == strings.TRUE

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can logout from my courses list screen
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        global_contents.turn_orientation(set_capabilities, global_contents.PORTRAIT_ORIENTATION)
        assert android_main_dashboard_page.get_profile_tab().text == strings.PROFILE_SCREEN_TITLE
        android_main_dashboard_page.get_profile_tab().click()

        assert android_main_dashboard_page.log_out() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info(f'{global_contents.login_user_name} is successfully logged out')
