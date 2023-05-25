"""
    Course Dashboard Test Module
"""


from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.ios.pages.ios_videos_dashboard import IosVideosDashboard
from tests.ios.pages.ios_course_subsection import IosCourseSubsection
from tests.ios.pages.ios_login_smoke import IosLoginSmoke


class TestIosVideoSubsection(IosLoginSmoke):
    """
    Course Videos Subsection screen's Test Case

    """

    def test_validate_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that from My Courses list tapping any Course will load Course
            Dashboard screen/contents(of this specific course) in its tab
            Verify on tapping "Videos" tab will load Videos screen
        """

        global_contents = Globals(setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)

        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        if ios_course_dashboard_page.get_my_courses_list_row():
            course_name = ios_course_dashboard_page.get_my_courses_list_row().text
            assert ios_course_dashboard_page.load_course_details_screen().text
        assert ios_course_dashboard_page.get_course_title().text in course_name

        assert ios_course_dashboard_page.get_videos_tab().text == strings.COURSE_DASHBOARD_VIDEOS_TAB
        ios_course_dashboard_page.load_videos_tab()
        assert ios_course_dashboard_page.get_videos_tab().text == global_contents.is_selected

    def test_load_contents_smoke(self, set_capabilities, setup_logging):
        """
        Verify that Videos subsection screen will show following contents,
            Header contents, Back icon, Videos as Title,
        Verify that user should be able to view these contents:
            videos download header,
            Videos download switch
        Verify that clicking any video Download icon will start downloading it,
            and change its Download icon to Downloaded
        """

        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)
        ios_videos_dashboard_page = IosVideosDashboard(set_capabilities, setup_logging)
        ios_course_subsection_page = IosCourseSubsection(set_capabilities, setup_logging)

        assert ios_course_dashboard_page.get_share_icon().text == strings.COURSE_DASHBOARD_SHARE_COURSE
        assert ios_course_dashboard_page.get_course_section_header()
        course_subsection_component = ios_course_dashboard_page.get_course_item_title().text
        assert ios_course_dashboard_page.get_course_item_title()
        assert ios_course_dashboard_page.get_course_item_download_icon()
        ios_course_dashboard_page.get_course_item_title().click()

        navigation_icon = ios_videos_dashboard_page.get_navigation_icon()
        assert navigation_icon.text == strings.COURSE_DASHBOARD_VIDEOS_TAB
        assert ios_videos_dashboard_page.get_subsection_title().text == course_subsection_component
        assert ios_course_dashboard_page.get_course_item_title()
        assert ios_course_subsection_page.get_course_item_download_icon()

        ios_course_subsection_page.get_course_item_download_icon().click()
        assert ios_course_subsection_page.wait_for_all_videos_to_download() == strings.VIDEO_ICON_DOWNLOADED_STATUS_IOS

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can logout from videos subsection screen
        """

        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        ios_course_dashboard_page.navigate_to_main_dashboard(set_capabilities)
        assert ios_main_dashboard_page.load_account_screen().text == strings.PROFILE_SCREEN_TITLE
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN
        assert ios_main_dashboard_page.load_ios_landing_page(
            set_capabilities, setup_logging).text == strings.NEW_LANDING_MESSAGE_IOS
        setup_logging.info(f'{global_contents.login_user_name} is successfully logged out')
        setup_logging.info('Ending Test Case')
