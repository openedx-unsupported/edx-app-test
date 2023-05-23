"""
    Course Dashboard Test Module
"""


from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.ios.pages.ios_videos_dashboard import IosVideosDashboard
from tests.ios.pages.ios_login_smoke import IosLoginSmoke
from tests.ios.pages import ios_elements


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

        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        if ios_course_dashboard_page.get_my_courses_list_row():
            course_name = ios_course_dashboard_page.get_my_courses_list_row().text
            assert ios_course_dashboard_page.load_course_details_screen().text
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

        assert ios_course_dashboard_page.get_share_icon().text == strings.COURSE_DASHBOARD_SHARE_COURSE
        assert ios_course_dashboard_page.get_course_section_header()
        assert ios_course_dashboard_page.get_course_item_title()
        assert ios_course_dashboard_page.get_course_item_download_icon()

        assert ios_videos_dashboard_page.get_video_download_switch()
        ios_videos_dashboard_page.get_video_download_switch().click()
        ios_course_dashboard_page.load_courses_tab()
        ios_course_dashboard_page.load_videos_tab()
        assert ios_videos_dashboard_page.get_video_download_switch().get_attribute('label')

    def test_video_download_smoke(self, set_capabilities, setup_logging):
        """
        Verify the following senarios:
        check all videos are downloading
        wait for all videos to download
        check all videos are downloaded
        turn off toggel and check all video are deleted
        check videos numbers with icons
        """

        global_contents = Globals(setup_logging)
        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)
        ios_video_dashboard = IosVideosDashboard(set_capabilities, setup_logging)
        assert ios_video_dashboard.wait_for_all_videos_to_download(set_capabilities) \
            == strings.VIDEO_DASHBOARD_ALL_VIDEOS_DOWNLOADED_IOS
        assert ios_video_dashboard.check_videos_status(set_capabilities,
                                                       strings.VIDEO_ICON_DOWNLOADED_STATUS_IOS)
        assert ios_video_dashboard.check_all_videos_numbers(set_capabilities)
        assert global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.video_dashboard_download_switch).get_attribute('value') \
            == strings.VIDEO_DASHBOARD_DOWNLOAD_TOGGEL_ON_IOS

        global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.video_dashboard_download_switch).click()

        assert global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.video_dashboard_download_switch).get_attribute('value') \
            == strings.VIDEO_DASHBOARD_DOWNLOAD_TOGGEL_OFF_IOS

        ios_course_dashboard_page.load_courses_tab()
        ios_course_dashboard_page.load_videos_tab()

        assert ios_video_dashboard.check_videos_status(set_capabilities,
                                                       strings.VIDEO_ICON_DOWNLOADED_STATUS_IOS)
        assert ios_video_dashboard.check_all_videos_numbers(set_capabilities)

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can logout from videos dashboard screen
        """

        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)
        set_capabilities.back()
        assert ios_main_dashboard_page.load_account_screen().text == strings.PROFILE_SCREEN_TITLE
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN
        assert ios_main_dashboard_page.load_ios_landing_page(
            set_capabilities, setup_logging).text == strings.NEW_LANDING_MESSAGE_IOS
        setup_logging.info(f'{global_contents.login_user_name} is successfully logged out')
        setup_logging.info('-- Ending Test Case --')
