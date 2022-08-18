"""
    Course Dates Test Module
"""


from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_my_courses_list import IosMyCoursesList
from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.ios.pages.ios_course_resources import IosCourseResources
from tests.ios.pages.ios_login_smoke import IosLoginSmoke
from tests.ios.pages.ios_discussions_dashboard import IosDiscussionsDashboard
from tests.ios.pages import ios_elements


class TestIosCourseDates(IosLoginSmoke):
    """
    Course Dates screen's Test Case

    """

    def test_validate_ui_elements_smoke(self, set_capabilities, setup_logging):
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
            Dates start date
            Dates start title
        Verify all screen contents have their default values
        """

        global_contents = Globals(setup_logging)
        ios_discussions_page = IosDiscussionsDashboard(set_capabilities, setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)
        ios_my_courses_list = IosMyCoursesList(set_capabilities, setup_logging)
        ios_course_resources_page = IosCourseResources(set_capabilities, setup_logging)

        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        if ios_my_courses_list.get_my_courses_list_row():
            course_name = ios_my_courses_list.get_my_courses_list_row().text
            assert ios_my_courses_list.load_course_details_screen().text in course_name

        assert ios_course_dashboard_page.get_dates_tab().text == strings.COURSE_DASHBOARD_DATES_TAB
        ios_course_dashboard_page.load_dates_tab()

        assert ios_course_dashboard_page.get_share_icon().text == strings.COURSE_DASHBOARD_SHARE_COURSE
        assert ios_course_resources_page.get_subsection_title()[0].text == strings.DATES_HEADER_TITLE
        assert ios_course_resources_page.get_navigation_back_icon()[0].text == 'Courses'
        assert ios_course_dashboard_page.get_share_icon().text == strings.COURSE_DASHBOARD_SHARE_COURSE
        banner_title = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.dates_banner_title)
        assert banner_title.text == strings.DATES_COURSE_BANNER_TITLE

        banner_info = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.dates_banner_info)
        assert banner_info.text == strings.DATES_COURSE_BANNER_INFO_IOS

        all_text = global_contents.get_all_views_on_ios_screen(
            set_capabilities,
            ios_elements.all_textview_type
        )

        assert all_text[1].text == strings.DATES_COURSE_STARTS_TITLE

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can logout from course dashboard screen
        """

        global_contents = Globals(setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        set_capabilities.back()
        assert ios_main_dashboard_page.load_account_screen().text == strings.PROFILE_SCREEN_TITLE
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN
        assert ios_main_dashboard_page.load_ios_landing_page(
            set_capabilities, setup_logging).text == strings.NEW_LANDING_MESSAGE_IOS

        setup_logging.info('{} is successfully logged out'.format(global_contents.login_user_name))
        setup_logging.info('-- Ending Test Case --')
