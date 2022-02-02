"""
    Course Resources Test Module
"""

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_login_smoke import AndroidLoginSmoke
from tests.common import strings
from tests.common.globals import Globals
from tests.android.pages import android_elements


class TestAndroidCourseResources(AndroidLoginSmoke):
    """
    Course Resources screen's Test Case

    """

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify that Course Resources tab will show following contents,
        Header contents,
            Back icon,
            Resources as Title, Share icon,
        Verify that user should be able to go back by clicking Back icon
        """

        global_contents = Globals(setup_logging)
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        assert android_main_dashboard_page.load_courses_tab()
        if android_my_courses_list_page.get_my_courses_list_row():
            android_my_courses_list_page.get_first_course().click()
        else:
            setup_logging.info('No course enrolled by this user.')

        resources_tab_element = android_course_dashboard_page.get_resources_tab()
        resources_tab_element.click()
        assert resources_tab_element.get_attribute('selected') == 'true'

        navigation_icon = android_course_dashboard_page.get_navigation_icon()
        assert navigation_icon.get_attribute('content-desc') == strings.COURSE_DASHBOARD_NAVIGATION_ICON
        android_course_dashboard_page.get_navigation_icon().click()
        assert android_main_dashboard_page.on_screen() == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME
        android_my_courses_list_page.load_course_details_screen()
        android_course_dashboard_page.get_resources_tab().click()
        assert resources_tab_element.get_attribute('selected') == 'true'
        share_icon = android_course_dashboard_page.get_course_share_icon()
        assert share_icon.get_attribute('content-desc') == strings.COURSE_DASHBOARD_SHARE_COURSE_ANDROID

        resources_tab_title = global_contents.get_by_class_from_elements(
            set_capabilities,
            android_elements.all_textviews,
            global_contents.first_existence)
        assert resources_tab_title.text == strings.COURSE_DASHBOARD_RESOURCES_TAB

    def test_handouts_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user should be able to view:
            Handouts as Row title
            Subtitle of the row,
            Handouts icon in row,
            Handouts can be clickable and it will navigate to handouts page
            Handouts as Title of the page
        """

        global_contents = Globals(setup_logging)
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)

        handouts_row_title = global_contents.get_by_id_from_elements(
            set_capabilities,
            android_elements.course_resources_row_title,
            global_contents.first_existence)
        assert handouts_row_title.text == strings.COURSE_DASHBOARD_HANDOUTS_TITLE

        handouts_row_subtitle = global_contents.get_by_id_from_elements(
            set_capabilities,
            android_elements.course_resources_row_subtitle,
            global_contents.first_existence)
        assert handouts_row_subtitle.text == strings.COURSE_DASHBOARD_HANDOUTS_ROW

        handouts_icon_element = global_contents.get_by_id_from_elements(
            set_capabilities,
            android_elements.course_resources_row_icon_type,
            global_contents.first_existence)
        assert handouts_icon_element.get_attribute('displayed') == 'true'

        handouts_row_title.click()
        handouts_page_title = global_contents.get_by_class_from_elements(
            set_capabilities,
            android_elements.all_textviews,
            global_contents.first_existence)
        assert handouts_page_title.text == strings.COURSE_DASHBOARD_HANDOUTS_TITLE

        android_course_dashboard_page.get_navigation_icon().click()

    def test_announcement_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user should be able to view:
            Announcements as Row title
            Subtitle of the row,
            Announcements icon in row,
            Announcements can be clickable and it will navigate to Announcements page
            Announcements as Title of page
        """
        global_contents = Globals(setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)

        announcement_row_title = global_contents.get_by_id_from_elements(
            set_capabilities,
            android_elements.course_resources_row_title,
            global_contents.second_existence)
        assert announcement_row_title.text == strings.COURSE_DASHBOARD_ANNOUNCEMENT_TITLE

        announcement_row_subtitle = global_contents.get_by_id_from_elements(
            set_capabilities,
            android_elements.course_resources_row_subtitle,
            global_contents.second_existence)
        assert announcement_row_subtitle.text == strings.COURSE_DASHBOARD_ANNOUNCEMENT_ROW

        announcement_icon_element = global_contents.get_by_id_from_elements(
            set_capabilities,
            android_elements.course_resources_row_icon_type,
            global_contents.second_existence)
        assert announcement_icon_element.get_attribute('displayed') == 'true'

        announcement_row_title.click()
        announcement_page_title = global_contents.get_by_class_from_elements(
            set_capabilities,
            android_elements.all_textviews,
            global_contents.first_existence)
        assert announcement_page_title.text == strings.COURSE_DASHBOARD_ANNOUNCEMENT_TITLE

        android_course_dashboard_page.get_navigation_icon().click()

        set_capabilities.back()
        assert android_main_dashboard_page.get_logout_account_option().text == strings.PROFILE_OPTIONS_SIGNOUT_BUTTON
        assert android_main_dashboard_page.log_out() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info('Ending Test Case --')
