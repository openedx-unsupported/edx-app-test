"""
    Course Dashboard Test Module
"""


from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_my_courses_list import IosMyCoursesList
from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.ios.pages.ios_videos_dashboard import IosVideosDashboard
from tests.ios.pages.ios_login_smoke import IosLoginSmoke


class TestIosCourseVideosDashboard(IosLoginSmoke):
    """
    Course Videos Dashboard screen's Test Case

    """

    def test_validate_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that from My Courses list tapping any Course will load Course
            Dashboard screen/contents(of this specific course) in its tab
        """

        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)
        ios_my_courses_list = IosMyCoursesList(set_capabilities, setup_logging)

        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        if ios_my_courses_list.get_my_courses_list_row():
            course_name = ios_my_courses_list.get_my_courses_list_row().text
            assert ios_my_courses_list.load_course_details_screen().text
        assert ios_course_dashboard_page.get_course_title().text in course_name

    def test_videos_dashboard_navigations(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify on tapping "Discussion" tab will load Discussions screen
            Verify on tapping "Dates" tab will load Dates screen
            Verify on tapping "Resources" tab will load Resources list
            Verify on tapping "Videos" tab will load Videos screen
            Verify that Course Videos Dashboard screen will show following contents,
        """

        global_contents = Globals(setup_logging)
        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)

        assert ios_course_dashboard_page.get_courses_tab().text == global_contents.is_selected
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

        assert ios_course_dashboard_page.get_videos_tab().text == strings.COURSE_DASHBOARD_VIDEOS_TAB
        ios_course_dashboard_page.load_videos_tab()
        assert ios_course_dashboard_page.get_videos_tab().text == global_contents.is_selected

    def test_load_contents_smoke(self, set_capabilities, setup_logging):
        """
        Verify that Course Videos Dashboard screen will show following contents,
            Header contents, Back icon, Specific "<course name>" as Title, Share icon,
            Footer Content,
                    Course, Videos, Discussion, Dates, Resources
        Verify that user should be able to view these contents:
            videos download header,
            Videos download switch
        """

        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)
        ios_videos_dashboard_page = IosVideosDashboard(set_capabilities, setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert ios_course_dashboard_page.get_share_icon().text == strings.COURSE_DASHBOARD_SHARE_COURSE
        assert ios_course_dashboard_page.get_course_section_header()
        assert ios_course_dashboard_page.get_course_item_title()
        assert ios_course_dashboard_page.get_course_item_download_icon()

        assert ios_videos_dashboard_page.get_video_download_switch()
        ios_videos_dashboard_page.get_video_download_switch()

        assert ios_videos_dashboard_page.get_video_download_header()
        set_capabilities.back()
        assert ios_main_dashboard_page.load_account_screen().text == strings.PROFILE_SCREEN_TITLE
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN
        assert ios_main_dashboard_page.load_ios_landing_page(
            set_capabilities, setup_logging).text == strings.NEW_LANDING_MESSAGE_IOS
        setup_logging.info('{} is successfully logged out'.format(global_contents.login_user_name))
        setup_logging.info('-- Ending Test Case --')
