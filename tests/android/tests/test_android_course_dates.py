"""
    Course Dates Test Module
"""

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_discussions_dashboard import AndroidDiscussionsDashboard
from tests.android.pages.android_login_smoke import AndroidLoginSmoke
from tests.common import strings
from tests.common.globals import Globals
from tests.android.pages import android_elements


class TestAndroidCourseDates(AndroidLoginSmoke):
    """
    Course Dates screen's Test Case

    """

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify that Course Dates screen will show following contents,
        Header contents,
            Back icon,
            "Important Dates" as Title Date
            Share icon to share specific date
            Information about specific dates,
        Verify that user should be able to view these contents:
            Dates banner title,
            Dates banner information
            Dates sync title
            Dates sync information
            Dates start date
            Dates start title
        Verify all screen contents have their default values
        """

        global_contents = Globals(setup_logging)
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        assert android_main_dashboard_page.load_courses_tab()
        if android_my_courses_list_page.get_my_courses_list_row():
            android_my_courses_list_page.get_second_course().click()
        else:
            setup_logging.info('No course enrolled by this user.')

        dates_tab_element = android_course_dashboard_page.get_dates_tab()
        dates_tab_element.click()
        assert dates_tab_element.get_attribute('selected') == 'true'

        navigation_icon = android_course_dashboard_page.get_navigation_icon()
        assert navigation_icon.get_attribute('content-desc') == strings.COURSE_DASHBOARD_NAVIGATION_ICON

        assert android_course_dashboard_page.get_all_text_views()[0].text == strings.DATES_HEADER_TITLE
        assert android_course_dashboard_page.get_course_share_icon().get_attribute('content-desc') \
            == strings.COURSE_DASHBOARD_SHARE_COURSE_ANDROID

        dates_banner_title = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.dates_banner_title)
        assert dates_banner_title.text == strings.DATES_COURSE_BANNER_TITLE

        dates_banner_info = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.dates_banner_info)
        assert dates_banner_info.text == strings.DATES_COURSE_BANNER_INFO

        dates_sync_title = android_course_dashboard_page.get_all_text_views()[4]
        assert dates_sync_title.text == strings.DATES_CALENDAR_SYNC_TITLE

        dates_sync_info = android_course_dashboard_page.get_all_text_views()[5]
        assert dates_sync_info.text == strings.DATES_CALENDAR_SYNC_INFO

        dates_course_date_id = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.dates_course_date_id)
        assert dates_course_date_id.text

        dates_course_start_title = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.dates_course_start_title)
        assert dates_course_start_title.text == strings.DATES_COURSE_STARTS_TITLE

    def test_scroll_dates_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify that user should be able to scroll from top to bottom of dates screen
        Verify that user should be able to scroll from bottom to top of dates screen
        """

        global_contents = Globals(setup_logging)
        all_info_containers = global_contents.get_all_elements_by_id(
            set_capabilities,
            android_elements.dates_info_container
        )

        global_contents.scroll_from_element(set_capabilities, all_info_containers[1])

        dates_course_start_title = global_contents.get_all_elements_by_id(
            set_capabilities,
            android_elements.dates_course_start_title)

        assert dates_course_start_title[3].text == strings.DATES_COURSE_ENDS_TITLE
        course_end_description = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.dates_course_end_description
        )
        assert course_end_description.text == strings.DATES_COURSE_ENDS_DESCRIPTION

        global_contents.scroll_screen(set_capabilities, all_info_containers[0], all_info_containers[3])

        dates_banner_title = global_contents.get_element_by_id(
            set_capabilities,
            android_elements.dates_banner_title)
        assert dates_banner_title.text == strings.DATES_COURSE_BANNER_TITLE

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can logout from course Dates screen
        """

        discussions_dashboard_page = AndroidDiscussionsDashboard(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        discussions_dashboard_page.get_navigation_icon().click()
        assert android_main_dashboard_page.get_logout_account_option().text == strings.PROFILE_OPTIONS_SIGNOUT_BUTTON
        assert android_main_dashboard_page.log_out() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info('Ending Test Case --')
