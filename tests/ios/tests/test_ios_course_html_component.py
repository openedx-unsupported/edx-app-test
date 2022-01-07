"""
    Course HTMl component Test Module
"""


from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_my_courses_list import IosMyCoursesList
from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.ios.pages.ios_whats_new import IosWhatsNew
from tests.ios.pages.ios_course_subsection import IosCourseSubsection
from tests.ios.pages.ios_course_html_component import IosCourseHtmlComponent


class TestIosCourseHTMLComponent:
    """
    Course HTML component screen's Test Case

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
            Verify that Course Html Component screen will show following Header contents,
            Back icon
            Specific "<Topic name>" as Title
            Verify that user should be able to go back by clicking Back icon
            Verify that user should be able to view these:
            Topic name
            Verify that footer should have Previous and Next button in it
            Verify that user should be able to navigate between Previous and Next Button from footer
        """

        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)
        ios_my_courses_list = IosMyCoursesList(set_capabilities, setup_logging)
        ios_subsection = IosCourseSubsection(set_capabilities, setup_logging)
        ios_html_component = IosCourseHtmlComponent(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        assert strings.COURSE_NAME_IOS in ios_my_courses_list.load_course_details_screen().text

        assert ios_subsection.get_subsection_component_title()
        section_name = ios_subsection.get_subsection_component_title().text
        ios_subsection.get_subsection_component_title().click()
        assert ios_subsection.get_subsection_title()[0].text == section_name

        back_icon = ios_subsection.get_navigation_back_icon()[0]
        assert back_icon.get_attribute('visible') == 'true'
        back_icon.click()

        assert ios_course_dashboard_page.get_course_title().text in strings.COURSE_NAME_IOS
        subsection_component = ios_subsection.get_subsection_component()[0]
        subsection_component.click()
        assert ios_subsection.get_course_subsection_header_label()
        assert ios_subsection.get_subsection_html_topic_title()

        html_component = ios_subsection.get_subsection_component()[0]
        html_component.click()
        assert ios_subsection.get_subsection_title()[0].text == strings.COURSE_SUBSECTION_CONTENT_ROW_TEXT_IOS

        previous_navigation_button = ios_html_component.get_all_buttons()[1]
        next_navigation_button = ios_html_component.get_all_buttons()[2]
        assert previous_navigation_button.text == strings.COURSE_HTML_COMPONENT_PREV_BUTTON
        assert strings.COURSE_HTML_COMPONENT_NEXT_BUTTON in next_navigation_button.text

        next_navigation_button.click()
        assert strings.COURSE_HTML_COMPONENT_PREV_BUTTON in previous_navigation_button.text

        ios_html_component.get_all_buttons()[1].click()
        assert ios_subsection.get_subsection_title()[0].text == strings.COURSE_SUBSECTION_CONTENT_ROW_TEXT_IOS

        ios_course_dashboard_page.navigate_to_main_dashboard(set_capabilities)
        assert ios_main_dashboard_page.load_account_screen().text == strings.PROFILE_SCREEN_TITLE
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN
        assert ios_main_dashboard_page.load_ios_landing_page(
            set_capabilities, setup_logging).text == strings.NEW_LANDING_MESSAGE_IOS
        setup_logging.info('{} is successfully logged out'.format(global_contents.login_user_name))
        setup_logging.info(' Ending Test Case --')
