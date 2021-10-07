"""
    Course Resources Test Module
"""


from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_my_courses_list import IosMyCoursesList
from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.ios.pages.ios_whats_new import IosWhatsNew
from tests.ios.pages.ios_course_resources import IosCourseResources


class TestIosCourseResources:
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
            Verify that Course Resources tab will show following contents,
            Header contents,
                Back icon,
                Resources as Title, Share icon,
            Verify that user should be able to go back by clicking Back icon
        """

        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)
        ios_my_courses_list = IosMyCoursesList(set_capabilities, setup_logging)
        ios_course_resources_page = IosCourseResources(set_capabilities, setup_logging)

        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        if ios_my_courses_list.get_my_courses_list_row():
            course_name = ios_my_courses_list.get_my_courses_list_row().text
            assert ios_my_courses_list.load_course_details_screen().text in course_name

        assert ios_course_dashboard_page.get_resources_tab().text == strings.COURSE_DASHBOARD_RESOURCES_TAB
        ios_course_dashboard_page.load_resources_tab()

        assert ios_course_dashboard_page.get_share_icon().text == strings.COURSE_DASHBOARD_SHARE_COURSE
        assert ios_course_resources_page.get_subsection_title()[0].text == strings.COURSE_DASHBOARD_RESOURCES_TAB
        assert ios_course_resources_page.get_navigation_back_icon()[0].text == 'Courses'

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

        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)
        ios_course_resources_page = IosCourseResources(set_capabilities, setup_logging)

        assert ios_course_dashboard_page.get_handouts_row_title().text == strings.COURSE_DASHBOARD_HANDOUTS_TITLE
        assert ios_course_dashboard_page.get_handouts_row_name().text == strings.COURSE_DASHBOARD_HANDOUTS_ROW

        ios_course_dashboard_page.load_handouts_row()
        assert ios_course_resources_page.get_subsection_title()[0].text == strings.COURSE_DASHBOARD_HANDOUTS_TITLE

        assert ios_course_resources_page.get_navigation_back_icon()[0].text
        set_capabilities.back()
        set_capabilities.back()

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
        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)
        ios_course_resources_page = IosCourseResources(set_capabilities, setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)

        announcement_title = ios_course_dashboard_page.get_announcements_row_title()
        assert announcement_title.text == strings.COURSE_DASHBOARD_ANNOUNCEMENT_TITLE
        assert ios_course_dashboard_page.get_announcements_row_name().text == strings.COURSE_DASHBOARD_ANNOUNCEMENT_ROW

        ios_course_dashboard_page.load_announcement_row()
        assert ios_course_resources_page.get_subsection_title()[0].text == strings.COURSE_DASHBOARD_ANNOUNCEMENT_TITLE
        assert ios_course_resources_page.get_navigation_back_icon()[0].text
        set_capabilities.back()
        set_capabilities.back()
        assert ios_course_dashboard_page.get_resources_tab().text == global_contents.is_selected

        ios_course_dashboard_page.navigate_to_main_dashboard(set_capabilities)
        ios_main_dashboard_page.get_drawer_icon().click()
        assert ios_main_dashboard_page.account_signout().text == strings.ACCOUNT_SIGNOUT
        ios_main_dashboard_page.account_signout().click()
        setup_logging.info('-- Ending Test Case --')
