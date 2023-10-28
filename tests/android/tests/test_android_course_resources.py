"""
    Course Resources Test Module
"""

from appium.webdriver.common.mobileby import MobileBy
from tests.android.pages import android_elements
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_login_smoke import AndroidLoginSmoke
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidCourseResources(AndroidLoginSmoke):
    """
    Course Resources screen's Test Case

    """

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that Course Dashboard tab will show following contents,
            Header contents,
                Back icon,
                Specific "<course name>" as Title, Share icon, Course,
            Verify that user should be able to go back by clicking Back icon
            Verify that user should be able to view these Course contents:
                Course Image, Course Name, Course Provider, Course Ending date,
                Last accessed(if any), Course Content,
            Verify all screen contents have their default values
        """

        global_contents = Globals(setup_logging)
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        if android_my_courses_list_page.get_my_courses_list_row():
            course_name = android_my_courses_list_page.get_second_course().text
            android_my_courses_list_page.get_second_course().click()
        else:
            setup_logging.info('No course enrolled by this user.')

        assert android_course_dashboard_page.course_dashboard_toolbar_dismiss_button().get_attribute(
            'clickable') == strings.TRUE
        android_course_dashboard_page.course_dashboard_toolbar_dismiss_button().click()
        assert android_main_dashboard_page.on_screen() == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME
        android_my_courses_list_page.get_second_course().click()

        if course_name:
            # Verifing the title of the screen
            assert course_name in android_course_dashboard_page.course_dashboard_course_title().text

        assert android_course_dashboard_page.course_dashboard_course_organization().text \
            == strings.LOGIN_EDX_LOGO
        assert android_course_dashboard_page.course_dashboard_course_expiry_date().text

    def test_handouts_tab_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that value of handouts tab is false by default
            Verify that clicking handouts will set its value to true
            Verify that webview is loaded after clicking handouts
        """

        global_contents = Globals(setup_logging)
        scrollable_tab = set_capabilities.find_element(MobileBy.ID, android_elements.course_dashboard_tabs)
        tab_elements = scrollable_tab.find_elements(MobileBy.CLASS_NAME, android_elements.course_layout)

        handouts_tab = tab_elements[4]
        assert handouts_tab.get_attribute('selected') == strings.FALSE
        handouts_tab.click()
        assert handouts_tab.get_attribute('selected') == strings.TRUE

        hanouts_page_element = global_contents.wait_and_get_element(
            set_capabilities, android_elements.course_handouts_webview_element)
        assert hanouts_page_element.get_attribute('displayed') == strings.TRUE
        assert hanouts_page_element.get_attribute('enabled') == strings.TRUE

    def test_announcements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that value of handouts tab is false by default
            Verify that clicking handouts will set its value to true
            Verify that webview is loaded after clicking handouts
        """

        global_contents = Globals(setup_logging)
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)

        announcements_tabs = android_course_dashboard_page.course_dashboard_get_all_tabs()[8]
        announcements_tabs.click()
        announcements_webview_element = global_contents.wait_and_get_element(
            set_capabilities, android_elements.course_handouts_webview_element)
        assert announcements_webview_element.get_attribute('enabled') == strings.TRUE

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can logout from course dashboard screen
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        set_capabilities.back()
        set_capabilities.back()
        assert android_main_dashboard_page.get_profile_tab().text == strings.PROFILE_SCREEN_TITLE
        android_main_dashboard_page.get_profile_tab().click()

        assert android_main_dashboard_page.log_out() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info('Ending Test Case')
