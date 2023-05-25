"""
    Course Dashboard Test Module
"""


from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.ios.pages.ios_login_smoke import IosLoginSmoke


class TestIosCourseDashboard(IosLoginSmoke):
    """
    Course Dashboard screen's Test Case

    """

    def test_validate_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that from My Courses list tapping any Course will load Course
            Dashboard screen/contents(of this specific course) in its tab
            Verify that Course Dashboard screen will show following contents,
                Header contents, Back icon, Specific "<course name>" as Title, Share icon,
                Footer Content,
                        Course, Videos, Discussion, Dates, Resources
            Verify that user should be able to view these Course contents:
                Course Image, Course Name, Course Provider, Course Ending date,
                Last accessed(if any), Course Content
        """

        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)

        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        if ios_course_dashboard_page.get_my_courses_list_row():
            course_name = ios_course_dashboard_page.get_my_courses_list_row().text
            assert ios_course_dashboard_page.load_course_details_screen().text in course_name

        assert ios_course_dashboard_page.get_share_icon().text == strings.COURSE_DASHBOARD_SHARE_COURSE
        assert ios_course_dashboard_page.get_course_image()
        assert ios_course_dashboard_page.get_course_title().text in course_name
        assert ios_course_dashboard_page.get_course_date()
        resume_element = ios_course_dashboard_page.get_course_resume_row()
        assert resume_element.get_attribute('label') == strings.COURSE_DASHBOARD_RESUME_ROW
        assert ios_course_dashboard_page.get_course_section_header()
        assert ios_course_dashboard_page.get_course_item_title()
        assert ios_course_dashboard_page.get_course_item_download_icon()

    def test_load_contents_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify on tapping "Videos" tab will load Videos screen
            Verify on tapping "Discussion" tab will load Discussions screen
            Verify on tapping "Dates" tab will load Dates screen
            Verify on tapping "Resources" tab will load Resources list
            Verify on tapping "Handouts" tab will load Handouts screen
            Verify on tapping "Announcements" tab will load Announcements screen
        """

        global_contents = Globals(setup_logging)
        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)

        assert ios_course_dashboard_page.get_courses_tab().text == global_contents.is_selected
        assert ios_course_dashboard_page.get_videos_tab().text == strings.COURSE_DASHBOARD_VIDEOS_TAB
        ios_course_dashboard_page.load_videos_tab()
        assert ios_course_dashboard_page.get_videos_tab().text == global_contents.is_selected
        assert ios_course_dashboard_page.get_discussion_tab().text == strings.COURSE_DASHBOARD_DISCUSSION_TAB
        ios_course_dashboard_page.load_discussion_tab()
        assert ios_course_dashboard_page.get_discussion_tab().text == global_contents.is_selected
        assert ios_course_dashboard_page.get_dates_tab().text == strings.COURSE_DASHBOARD_DATES_TAB
        ios_course_dashboard_page.load_dates_tab()
        assert ios_course_dashboard_page.get_dates_tab().text == global_contents.is_selected
        assert ios_course_dashboard_page.get_resources_tab().text == strings.COURSE_DASHBOARD_RESOURCES_TAB
        ios_course_dashboard_page.load_resources_tab()
        assert ios_course_dashboard_page.get_handouts_row_title().text == strings.COURSE_DASHBOARD_HANDOUTS_TITLE
        assert ios_course_dashboard_page.get_handouts_row_name().text == strings.COURSE_DASHBOARD_HANDOUTS_ROW
        announcement_title = ios_course_dashboard_page.get_announcements_row_title()
        assert announcement_title.text == strings.COURSE_DASHBOARD_ANNOUNCEMENT_TITLE
        assert ios_course_dashboard_page.get_announcements_row_name().text == strings.COURSE_DASHBOARD_ANNOUNCEMENT_ROW
        ios_course_dashboard_page.load_handouts_row()
        ios_course_dashboard_page.get_resources_back_icon().click()

        ios_course_dashboard_page.load_announcement_row()
        ios_course_dashboard_page.get_resources_back_icon().click()

        assert ios_course_dashboard_page.get_resources_tab().text == global_contents.is_selected
        assert ios_course_dashboard_page.get_courses_tab().text == strings.COURSE_DASHBOARD_COURSES_TAB
        ios_course_dashboard_page.load_courses_tab()
        assert ios_course_dashboard_page.get_courses_tab().text == global_contents.is_selected

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

        setup_logging.info(f'{global_contents.login_user_name} is successfully logged out')
        setup_logging.info('Ending Test Case')
