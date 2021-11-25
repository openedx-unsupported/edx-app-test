"""
    Course Videos Dashboard Test Module
"""

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.tests.android_login_smoke import AndroidLoginSmoke
from tests.android.pages import android_elements
from tests.common import strings
from tests.common.globals import Globals
from tests.android.pages.android_video_dashboard import AndroidVideoDasboard


class TestAndroidVideosDashboard(AndroidLoginSmoke):
    """
    Course Videos Dashboard screen's Test Case

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

        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        assert android_main_dashboard_page.load_courses_tab()
        if android_my_courses_list_page.get_my_courses_list_row():
            android_my_courses_list_page.get_second_course().click()
        else:
            setup_logging.info('No course enrolled by this user.')

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
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        discussion_tab_element = android_course_dashboard_page.get_discussion_tab()
        if discussion_tab_element:
            discussion_tab_element.click()
            assert discussion_tab_element.get_attribute('selected') == 'true'

        dates_tab_element = android_course_dashboard_page.get_dates_tab()
        if dates_tab_element:
            dates_tab_element.click()
            assert dates_tab_element.get_attribute('selected') == 'true'

        resources_tab_element = android_course_dashboard_page.get_resources_tab()
        if resources_tab_element:
            resources_tab_element.click()
            assert resources_tab_element.get_attribute('selected') == 'true'

        course_tab_element = android_course_dashboard_page.get_course_tab()
        if course_tab_element:
            course_tab_element.click()
            assert course_tab_element.get_attribute('selected') == 'true'

        video_tab_element = android_course_dashboard_page.get_videos_tab()
        if video_tab_element:
            video_tab_element.click()
            assert video_tab_element.get_attribute('selected') == 'true'

        assert android_course_dashboard_page.get_navigation_icon().get_attribute('content-desc') \
            == strings.COURSE_DASHBOARD_NAVIGATION_ICON
        android_course_dashboard_page.get_navigation_icon().click()
        assert android_main_dashboard_page.on_screen() == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME
        android_my_courses_list_page.get_second_course().click()

    def test_video_tab_contents_smoke(self, set_capabilities, setup_logging):
        """
        Verify Video tab showing following content:
        Videos as title
        course share icon
        Video TV title
        Video TV sub-title
        Video icon
        Download to device toggle
        Verify download to device permission dialouge contents:
        Allow button
        Deny Button
        Permission message
        """

        global_contents = Globals(setup_logging)
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        android_course_dashboard_page.get_videos_tab().click()
        assert android_course_dashboard_page.get_all_text_views()[0].text \
            == strings.COURSE_DASHBOARD_VIDEOS_TAB
        assert android_course_dashboard_page.get_course_share_icon().get_attribute('content-desc') \
            == strings.COURSE_DASHBOARD_SHARE_COURSE_ANDROID

        assert global_contents.get_element_by_id(
            set_capabilities,
            android_elements.video_dashboard_tv_title).text == strings.VIDEO_DASHBOARD_TV_TITLE

        assert global_contents.get_element_by_id(
            set_capabilities,
            android_elements.video_dashboard_tv_subtitle).text == strings.VIDEO_DASHBOARD_TV_SUBTITLE

        assert global_contents.get_element_by_id(
            set_capabilities,
            android_elements.video_dahboard_video_icon)

        assert global_contents.get_element_by_id(
            set_capabilities,
            android_elements.video_dashboard_bulk_download_toggle)

        assert global_contents.get_element_by_id(
            set_capabilities,
            android_elements.video_dashboard_download_bar)
        assert android_course_dashboard_page.get_course_content_header().text

    def test_download_to_device_smoke(self, set_capabilities, setup_logging):
        """
        Verify the following senarios:
        check if download to device toggel off
        click on toggle
        if allow/deny permission popup appears
        check allow, deny and permission elements
        click on allow button
        check and click on progress wheel
        """

        global_contents = Globals(setup_logging)
        android_video_dashboard = AndroidVideoDasboard(set_capabilities, setup_logging)
        assert android_video_dashboard.check_videos_status(set_capabilities,
                                                           strings.VIDEO_ICON_ONLINE_STATUS)

        if global_contents.get_element_by_id(
                set_capabilities,
                android_elements.video_dashboard_bulk_download_toggle).text \
                == strings.VIDEO_DASHBOARD_DOWNLOAD_TOGGEL_OFF:

            global_contents.get_element_by_id(
                set_capabilities,
                android_elements.video_dashboard_bulk_download_toggle).click()

            if global_contents.get_by_class_from_elements(
                    set_capabilities,
                    android_elements.video_download_permission_buttons,
                    global_contents.first_existence):

                assert global_contents.get_by_class_from_elements(
                    set_capabilities, android_elements.video_download_permission_buttons,
                    global_contents.first_existence).text \
                        == strings.VIDEO_DOWNLOAD_PERMISSION_ALLOW_BUTTON

                assert global_contents.get_by_class_from_elements(
                    set_capabilities, android_elements.video_download_permission_message,
                    global_contents.first_existence)

                assert global_contents.get_by_class_from_elements(
                    set_capabilities, android_elements.video_download_permission_buttons,
                    global_contents.second_existence).text == strings.VIDEO_DOWNLOAD_PERMISSION_DENY_BUTTON

                global_contents.get_by_class_from_elements(
                    set_capabilities, android_elements.video_download_permission_buttons,
                    global_contents.first_existence).click()

        global_contents.wait_and_get_element(
            set_capabilities,
            android_elements.video_dahboard_video_icon
        )

        assert global_contents.get_element_by_id(
            set_capabilities,
            android_elements.video_dahboard_video_icon)

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
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_video_dashboard = AndroidVideoDasboard(set_capabilities, setup_logging)
        assert android_video_dashboard.wait_for_all_videos_to_download(set_capabilities) \
            == strings.VIDEO_DASHBOARD_ALL_VIDEOS_DOWNLOADED
        assert android_video_dashboard.check_videos_status(set_capabilities,
                                                           strings.VIDEO_ICON_DOWNLOADED_STATUS)
        assert android_video_dashboard.check_all_videos_numbers(set_capabilities)
        assert global_contents.get_element_by_id(
            set_capabilities,
            android_elements.video_dashboard_bulk_download_toggle).text \
            == strings.VIDEO_DASHBOARD_DOWNLOAD_TOGGEL_ON

        global_contents.get_element_by_id(
            set_capabilities,
            android_elements.video_dashboard_bulk_download_toggle).click()

        assert global_contents.get_element_by_id(
            set_capabilities,
            android_elements.video_dashboard_bulk_download_toggle).text \
            == strings.VIDEO_DASHBOARD_DOWNLOAD_TOGGEL_OFF

        assert android_video_dashboard.wait_for_all_videos_to_delete(set_capabilities) \
            == strings.VIDEO_DASHBOARD_TV_TITLE
        assert android_video_dashboard.check_videos_status(set_capabilities,
                                                           strings.VIDEO_ICON_ONLINE_STATUS)
        assert android_video_dashboard.check_all_videos_numbers(set_capabilities)
        set_capabilities.back()
        assert android_main_dashboard_page.get_logout_account_option().text == strings.PROFILE_OPTIONS_SIGNOUT_BUTTON
        assert android_main_dashboard_page.log_out() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info('-- Ending Test Case --')
