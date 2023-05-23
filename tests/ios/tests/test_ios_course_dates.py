"""
    Course Dates Test Module
"""


from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_my_courses_list import IosMyCoursesList
from tests.ios.pages.ios_course_dashboard import IosCourseDashboard
from tests.ios.pages.ios_course_resources import IosCourseResources
from tests.ios.pages.ios_login_smoke import IosLoginSmoke
from tests.ios.pages import ios_elements


class TestIosCourseDates(IosLoginSmoke):
    """
    Course Dates screen's Test Case

    """

    def test_validate_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that Course Dates screen will show following contents,
            Header contents,
                Back icon,
                "Important Dates" as Title Date
                Share icon to share specific date
                Information about specific dates,
            Verify that user should be able to view these contents:
                Dates banner title,
                Dates banner information
                Dates start date
                Dates start title
            Verify all screen contents have their default values
        """

        global_contents = Globals(setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        ios_course_dashboard_page = IosCourseDashboard(set_capabilities, setup_logging)
        ios_my_courses_list = IosMyCoursesList(set_capabilities, setup_logging)
        ios_course_resources_page = IosCourseResources(set_capabilities, setup_logging)

        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        if ios_my_courses_list.get_my_courses_list_row():
            course_name = ios_my_courses_list.get_my_course_for_dates().text
            assert ios_my_courses_list.load_course_details_for_dates_screen().text in course_name

        assert ios_course_dashboard_page.get_dates_tab().text == strings.COURSE_DASHBOARD_DATES_TAB
        ios_course_dashboard_page.load_dates_tab()

        assert ios_course_dashboard_page.get_share_icon().text == strings.COURSE_DASHBOARD_SHARE_COURSE
        assert ios_course_resources_page.get_subsection_title()[0].text == strings.DATES_HEADER_TITLE
        assert ios_course_resources_page.get_navigation_back_icon()[0].text == 'Courses'
        assert ios_course_dashboard_page.get_share_icon().text == strings.COURSE_DASHBOARD_SHARE_COURSE
        banner_title = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.dates_banner_title)
        assert banner_title.text == strings.DATES_COURSE_BANNER_TITLE

        banner_info = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.dates_banner_info)
        assert banner_info.text == strings.DATES_COURSE_BANNER_INFO_IOS

        all_text = global_contents.get_all_views_on_ios_screen(
            set_capabilities,
            ios_elements.all_textview_type
        )

        assert all_text[1].text == strings.DATES_COURSE_STARTS_TITLE

    def test_calendar_sync_toggle_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that Calendar sync toggle is working properly
            Verify that on switching on the toggle a pop up appears
                (edx whould like to access your calendar) with "Don't Allow" & "OK" button
            Verify that tapping on "Don't Allow" will close the pop-up and the toggle will be switched Off
        """

        global_contents = Globals(setup_logging)

        sync_calendar_title = global_contents.get_all_views_on_ios_screen(
            set_capabilities,
            ios_elements.all_textviews
        )[4]
        assert sync_calendar_title.text == strings.DATES_CALENDAR_SYNC_TITLE

        sync_calendar_message = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.dates_calendar_sync_message)
        assert sync_calendar_message.text == strings.DATES_CALENDAR_SYNC_INFO

        sync_calendar_toggle = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.dates_calendar_sync_toggle)
        assert sync_calendar_toggle.text == strings.TOGGLE_OFF_IOS
        sync_calendar_toggle.click()

        dont_allow_button = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.calendar_permission_popup_dont_allow_button)
        assert dont_allow_button.text == strings.DONT_ALLOW_IOS

        ok_button = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.calendar_permission_popup_allow_button)
        assert ok_button.text == strings.OK_BUTTON

        calendar_permission_title = global_contents.get_all_views_on_ios_screen(
            set_capabilities,
            ios_elements.all_textviews
        )[0]
        assert calendar_permission_title.text == strings.DATES_CALENDAR_POPUP_TITLE

        calendar_permission_message = global_contents.get_all_views_on_ios_screen(
            set_capabilities,
            ios_elements.all_textviews
        )[1]
        assert calendar_permission_message.text == strings.DATES_CALENDAR_POPUP_MESSAGE
        ok_button.click()

    def test_calendar_permission_alert_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that Settings pop-up appears after tapping "Don't Allow" button and switching the toggle back On
            Verify that user is able to get permission for calendar after tapping open settings button
            Verify that tapping on OK button from access your calendar pop-up an other pop-up appears
        """

        global_contents = Globals(setup_logging)

        cancel_button = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.calendar_add_permission_cancel_button)
        assert cancel_button.text == strings.CANCEL_BUTTON

        calendar_permission_title = global_contents.get_all_views_on_ios_screen(
            set_capabilities,
            ios_elements.all_textviews
        )[0]
        assert calendar_permission_title.text == strings.ADD_CALENDAR_ALERT_TITLE_IOS

        add_button = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.calendar_add_permission_add_button)
        assert add_button.text == strings.ADD_BUTTON
        add_button.click()

        done_button = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.calendar_add_permission_done_button)
        assert done_button.text == strings.DONE_BUTTON
        view_events_popup_title = global_contents.get_all_views_on_ios_screen(
            set_capabilities,
            ios_elements.all_textviews
        )[0]
        assert view_events_popup_title.text == strings.CALENDAR_EVENTS_ALERT_TITLE_IOS
        view_events_button = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.calendar_add_permission_view_events_button)
        assert view_events_button.text == strings.CALENDAR_EVENTS_ALERT_VIEW_BUTTON_IOS
        done_button.click()
        sync_calendar_toggle = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.dates_calendar_sync_toggle)
        assert sync_calendar_toggle.text == strings.TOGGLE_ON_IOS

    def test_calendar_remove_events_alert_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that a pop-up appears with (Cancel & Remove) button after switching off the toggle
            "Your course calendar has been removed" toast appears after switching off the toggle and
                tapping on remove button
        """

        global_contents = Globals(setup_logging)

        sync_calendar_toggle = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.dates_calendar_sync_toggle)
        assert sync_calendar_toggle.text == strings.TOGGLE_ON_IOS
        sync_calendar_toggle.click()

        cancel_button = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.calendar_add_permission_cancel_button)
        assert cancel_button.text == strings.CANCEL_BUTTON

        remove_button = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.calendar_remove_permission_remove_button)
        assert remove_button.text == strings.REMOVE_BUTTON_IOS

        remove_events_popup_title = global_contents.get_all_views_on_ios_screen(
            set_capabilities,
            ios_elements.all_textviews
        )[0]
        assert remove_events_popup_title.text == strings.REMOVE_CALENDAR_EVENTS_TITLE_IOS

        remove_events_popup_info = global_contents.get_all_views_on_ios_screen(
            set_capabilities,
            ios_elements.all_textviews
        )[1]
        assert remove_events_popup_info.text == strings.REMOVE_CALENDAR_EVENTS_MESSAGE_IOS

        remove_button.click()
        sync_calendar_toggle = global_contents.get_element_by_id(
            set_capabilities,
            ios_elements.dates_calendar_sync_toggle)
        assert sync_calendar_toggle.text == strings.TOGGLE_OFF_IOS

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can logout from course dashboard screen
        """

        global_contents = Globals(setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        set_capabilities.back()
        assert ios_main_dashboard_page.load_account_screen().text == strings.PROFILE_SCREEN_TITLE
        assert ios_main_dashboard_page.log_out().text == strings.LOGIN
        assert ios_main_dashboard_page.load_ios_landing_page(
            set_capabilities, setup_logging).text == strings.NEW_LANDING_MESSAGE_IOS

        setup_logging.info(f'{global_contents.login_user_name} is successfully logged out')
        setup_logging.info('-- Ending Test Case --')
