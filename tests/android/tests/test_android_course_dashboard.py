"""
    Course Dashboard Test Module
"""

from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_login_smoke import AndroidLoginSmoke
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidCourseDashboard(AndroidLoginSmoke):
    """
    Course Dashboard screen's Test Case

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

        home_tab = android_course_dashboard_page.course_dashboard_get_all_tabs()[3]
        videos_tab = android_course_dashboard_page.course_dashboard_get_all_tabs()[4]
        discussions_tab = android_course_dashboard_page.course_dashboard_get_all_tabs()[5]
        dates_tab = android_course_dashboard_page.course_dashboard_get_all_tabs()[6]
        handouts_tab = android_course_dashboard_page.course_dashboard_get_all_tabs()[7]

        assert home_tab.get_attribute('content-desc') == 'Home'
        assert home_tab.get_attribute('selected') == 'true'

        assert videos_tab.get_attribute('content-desc') == 'Videos'
        assert videos_tab.get_attribute('selected') == 'false'

        assert discussions_tab.get_attribute('content-desc') == 'Discussion'
        assert discussions_tab.get_attribute('selected') == 'false'

        assert dates_tab.get_attribute('content-desc') == 'Dates'
        assert dates_tab.get_attribute('selected') == 'false'

        assert handouts_tab.get_attribute('content-desc') == 'Handouts'
        assert handouts_tab.get_attribute('selected') == 'false'

    def test_load_contents_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify on tapping "Videos" tab will load Videos screen
            Verify on tapping "Discussion" tab will load Discussions screen
            Verify on tapping "Dates" tab will load Dates screen
            Verify on tapping "Resources" tab will load Resources list
            Verify on tapping "Handouts" tab will load Handouts screen
            Verify on tapping "Announcements" tab will load Announcements screen
            Verify on tapping "Home" tab will load Home screen
        """

        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        home_tab = android_course_dashboard_page.course_dashboard_get_all_tabs()[3]
        videos_tab = android_course_dashboard_page.course_dashboard_get_all_tabs()[4]
        discussions_tab = android_course_dashboard_page.course_dashboard_get_all_tabs()[5]
        dates_tab = android_course_dashboard_page.course_dashboard_get_all_tabs()[6]
        handouts_tab = android_course_dashboard_page.course_dashboard_get_all_tabs()[7]

        videos_tab.click()
        assert videos_tab.get_attribute('selected') == 'true'
        assert videos_tab.get_attribute('content-desc') == 'Videos'

        discussions_tab.click()
        assert discussions_tab.get_attribute('selected') == 'true'
        assert discussions_tab.get_attribute('content-desc') == 'Discussion'

        dates_tab.click()
        assert dates_tab.get_attribute('selected') == 'true'
        assert dates_tab.get_attribute('content-desc') == 'Dates'

        handouts_tab.click()
        assert handouts_tab.get_attribute('selected') == 'true'
        assert handouts_tab.get_attribute('content-desc') == 'Handouts'

        announcements_tabs = android_course_dashboard_page.course_dashboard_get_all_tabs()[7]
        announcements_tabs.click()
        assert announcements_tabs.get_attribute('selected') == 'true'
        assert announcements_tabs.get_attribute('content-desc') == 'Announcements'

        discussions_tab.click()
        assert discussions_tab.get_attribute('selected') == 'true'
        assert discussions_tab.get_attribute('content-desc') == 'Discussion'

        home_tab.click()
        assert home_tab.get_attribute('content-desc') == 'Home'
        assert home_tab.get_attribute('selected') == 'true'

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can logout from course dashboard screen
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        set_capabilities.back()
        profile_tab = android_main_dashboard_page.get_all_tabs()[2]
        assert profile_tab.text == 'Profile'
        profile_tab.click()

        assert android_main_dashboard_page.log_out() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info('Ending Test Case')
