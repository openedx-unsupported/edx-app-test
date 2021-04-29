# coding=utf-8
"""
    Course Videos Dashboard Test Module
"""

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.tests.android_login_smoke import AndroidLoginSmoke
from tests.android.pages.android_videos_dashboard import AndroidVideosDashboard
from tests.common import strings
from tests.common.globals import Globals


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

        global_contents = Globals(setup_logging)
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        assert android_main_dashboard_page.load_courses_tab()
        if android_my_courses_list_page.get_my_courses_list_row():
            course_name = android_my_courses_list_page.get_first_course().text
            android_my_courses_list_page.get_first_course().click()
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
        android_video_dashboard = AndroidVideosDashboard(set_capabilities, setup_logging)

        # discussion_tab_element = android_course_dashboard_page.get_discussion_tab()
        # if discussion_tab_element:
        #     discussion_tab_element.click()
        #     assert discussion_tab_element.get_attribute('selected') == 'true'

        # dates_tab_element = android_course_dashboard_page.get_dates_tab()
        # if dates_tab_element:
        #     dates_tab_element.click()
        #     assert dates_tab_element.get_attribute('selected') == 'true'

        # resources_tab_element = android_course_dashboard_page.get_resources_tab()
        # if resources_tab_element:
        #     resources_tab_element.click()
        #     assert resources_tab_element.get_attribute('selected') == 'true'

        # course_tab_element = android_course_dashboard_page.get_course_tab()
        # if course_tab_element:
        #     course_tab_element.click()
        #     assert course_tab_element.get_attribute('selected') == 'true'

        # video_tab_element = android_course_dashboard_page.get_videos_tab()
        # if video_tab_element:
        #     video_tab_element.click()
        #     assert video_tab_element.get_attribute('selected') == 'true'
            
        # assert android_course_dashboard_page.get_navigation_icon().get_attribute('content-desc') \
        #     == strings.COURSE_DASHBOARD_NAVIGATION_ICON
        # android_course_dashboard_page.get_navigation_icon().click()
        # assert android_main_dashboard_page.on_screen() == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME
        # android_my_courses_list_page.load_course_details_screen()
        
        android_course_dashboard_page.get_videos_tab().click()
        assert android_course_dashboard_page.get_all_text_views()[0].text == 'Videos'
        assert android_course_dashboard_page.get_course_share_icon().get_attribute('content-desc') \
            == strings.COURSE_DASHBOARD_SHARE_COURSE

        # assert android_video_dashboard.get_video_dashboard_tv_title().text == strings.VIDEO_DASHBOARD_TV_TITLE
        # assert android_video_dashboard.get_video_dashboard_tv_subtitle()
        # assert android_video_dashboard.get_video_dahboard_video_icon()
        # assert android_video_dashboard.get_video_dashboard_bulk_download_toggle()
        # assert android_video_dashboard.get_video_dashboard_download_bar()
        # assert android_course_dashboard_page.get_course_content_header().text

        print('1111111111: ', android_course_dashboard_page.get_course_content_header().text)

        if android_video_dashboard.get_video_dashboard_bulk_download_toggle().text == strings.VIDEO_DASHBOARD_DOWNLOAD_TOGGEL_OFF:
            assert android_video_dashboard.get_video_dashboard_bulk_download_toggle().text == strings.VIDEO_DASHBOARD_DOWNLOAD_TOGGEL_OFF
            assert android_video_dashboard.get_video_dashboard_tv_subtitle().text == strings.VIDEO_DASHBOARD_TV_SUBTITLE    
            
            android_video_dashboard.get_video_dashboard_bulk_download_toggle().click()
            print('outside if:')
            if android_video_dashboard.get_video_download_permission_allow_button():
                print('inside if:')
                assert android_video_dashboard.get_video_download_permission_allow_button()
                assert android_video_dashboard.get_video_download_permission_deny_button().text == 'Deny'
                assert android_video_dashboard.get_video_download_permission_message()
                android_video_dashboard.get_video_download_permission_allow_button().click()

            # print('222222222: ', android_video_dashboard.get_video_dashboard_tv_subtitle().text)
        # toggel off
        # video_dashboard_tv_title.text == Download to device
        # number of videos.text
         
        # toggel on 
        # if allow button then video_download_permission_allow_button.click()
        # video_dashboard_tv_title.text == Downloading videos
        # org.edx.mobile:id/progress_wheel.displayed == true
        # number of videos hide
