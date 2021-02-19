# coding=utf-8
"""
    Course Dashboard Test Module
"""


from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_my_courses_list import IosMyCoursesList
from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.ios.pages.ios_whats_new import IosWhatsNew


class TestIosCourseDashboard:
    """
    Course Dashboard screen's Test Case

    """

    def test_start_main_dashboard_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully after successful login
        """

        global_contents = Globals(setup_logging)

        setup_logging.info('-- Starting Test Case --')
        if login:
            setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))

        ios_whats_new_page = IosWhatsNew(set_capabilities, setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)

        if global_contents.is_first_time:
            assert ios_whats_new_page.exit_features().text == strings.BLANK_FIELD
        else:
            assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME

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
        ios_my_courses_list = IosMyCoursesList(set_capabilities, setup_logging)

        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        if ios_my_courses_list.get_my_courses_list_row():
            course_name = ios_my_courses_list.get_my_courses_list_row().text
            assert ios_my_courses_list.load_course_details_screen().text in course_name

        assert ios_course_dashboard_page.get_share_icon().text == strings.COURSE_DASHBOARD_SHARE_COURSE
        assert ios_course_dashboard_page.get_course_image()
        assert ios_course_dashboard_page.get_course_title().text in course_name
        assert ios_course_dashboard_page.get_course_date()
        assert ios_course_dashboard_page.get_course_header_outline()
        assert ios_course_dashboard_page.get_course_header_subtitle()
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
        set_capabilities.back()
        set_capabilities.back()
        ios_course_dashboard_page.load_announcement_row()
        set_capabilities.back()
        set_capabilities.back()
        assert ios_course_dashboard_page.get_resources_tab().text == global_contents.is_selected
        assert ios_course_dashboard_page.get_courses_tab().text == strings.COURSE_DASHBOARD_COURSES_TAB
        ios_course_dashboard_page.load_courses_tab()
        assert ios_course_dashboard_page.get_courses_tab().text == global_contents.is_selected
        setup_logging.info('-- Ending Test Case --')
