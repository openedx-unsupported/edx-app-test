"""
    My Courses List Test Module
"""

from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages import ios_elements
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_login_smoke import IosLoginSmoke


class TestIosCourseDiscovery(IosLoginSmoke):
    """
    Discovery Test Case
    """

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify that from Main Dashboard tapping on Discovery tab will load Discovery
            contents in its tab
        Verify that Discovery tab will show following contents,
        Header contents,
            "Discovery" as screen Title,
            Account Icon
        Three tabs
            Courses, Programs, Degrees
        Search Courses option
        "Browse By Subject" Section below, Subject Background Image, Subject Name
        Verify that from discovery screen, courses and programs tab are loaded
        """

        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert ios_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB
        assert ios_main_dashboard_page.load_discovery_tab().text == strings.SELECTED_BY_DEFAULT

        title_element = global_contents.get_all_views_on_ios_screen(set_capabilities, ios_elements.all_textviews)[0]
        assert title_element.text == strings.MAIN_DASHBOARD_DISCOVERY_TAB

        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME

        course_discovery_tab = global_contents.get_all_views_on_ios_screen(set_capabilities,
                                                                           ios_elements.all_buttons)[4]
        assert course_discovery_tab.get_attribute('label') == strings.COURSES_DISCOVERY_COURSES_TAB
        course_discovery_tab.click()

        programs_discovery_tab = global_contents.get_all_views_on_ios_screen(set_capabilities,
                                                                             ios_elements.all_buttons)[5]
        assert programs_discovery_tab.get_attribute('label') == strings.COURSES_DISCOVERY_PROGRAMS_TAB
        programs_discovery_tab.click()

        degrees_discovery_tab = global_contents.get_all_views_on_ios_screen(set_capabilities,
                                                                            ios_elements.all_buttons)[6]
        assert degrees_discovery_tab.get_attribute('label') == strings.COURSES_DISCOVERY_DEGREES_TAB
        degrees_discovery_tab.click()
        course_discovery_tab.click()

        course_discovery_search_courses = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.course_discovery_search_courses)
        assert course_discovery_search_courses.get_attribute('label') == strings.COURSES_DISCOVERY_SEARCH_COURSE_IOS

        course_discovery_browse_by_subject = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.course_discovery_browse_by_subject)
        assert course_discovery_browse_by_subject.get_attribute('label') \
            == strings.COURSES_DISCOVERY_BROWSE_BY_SUBJECT_IOS

        assert ios_main_dashboard_page.load_discovery_tab().text == strings.SELECTED_BY_DEFAULT
        assert ios_main_dashboard_page.get_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert ios_main_dashboard_page.load_courses_tab().text == strings.SELECTED_BY_DEFAULT
        assert ios_main_dashboard_page.load_programs_tab().text == strings.SELECTED_BY_DEFAULT
        assert ios_main_dashboard_page.load_discovery_tab().text == strings.SELECTED_BY_DEFAULT
        assert ios_main_dashboard_page.load_account_screen().text == strings.PROFILE_SCREEN_TITLE
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN
        assert ios_main_dashboard_page.load_ios_landing_page(
            set_capabilities, setup_logging).text == strings.NEW_LANDING_MESSAGE_IOS
        setup_logging.info('{} is successfully logged out'.format(global_contents.login_user_name))
        setup_logging.info('-- Ending Test Case --')
