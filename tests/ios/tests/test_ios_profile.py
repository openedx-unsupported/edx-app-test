"""
    Profile screen Test Module
"""
from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_whats_new import IosWhatsNew
from tests.ios.pages.ios_profile import IosProfile


class TestIosProfile:
    """
    Profile screen's Test Case
    """

    def test_start_main_dashboard_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully
        """

        global_contents = Globals(setup_logging)

        setup_logging.info('-- Starting Test Case')
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
            Verify that Profile screen will show following contents:
                Back icon
                "Profile" as Title
                Edit
                Profile Image
                User Name
            Verify that Profile screen will show following contents for limited profile:
                Limited profile message
            Verify that Profile screen will show following contents for Full profile:
                location
                Language (if selected)
                User Bio
        """

        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        ios_profile_page = IosProfile(set_capabilities, setup_logging)

        assert ios_main_dashboard_page.get_drawer_icon().text == strings. MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        ios_main_dashboard_page.get_drawer_icon().click()
        ios_profile_page.get_personal_information_profile_cell().click()
        assert ios_profile_page.get_subsection_title().text == strings.PROFILE_SCREEN_TITLE
        assert ios_profile_page.get_navigation_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        assert ios_profile_page.get_profile_screen_edit_profile_button().text == strings.IOS_PROFILE_SCREEN_EDIT_PROFILE_BUTTON_TEXT
        assert ios_profile_page.get_profile_screen_username_label().get_attribute('visible') == 'true'

        ios_profile_page.get_profile_screen_edit_profile_button().click()
        assert ios_profile_page.get_subsection_title().get_attribute('value') == strings.EDIT_PROFILE_SCREEN_TITLE
        ios_profile_page.get_edit_profile_back_icon().click()

        if ios_profile_page.get_profile_screen_limited_view_message():
            assert ios_profile_page.get_profile_screen_limited_view_message().text == strings.IOS_PROFILE_SCREEN_LIMITED_VIEW_MESSAGE
        else:
            assert ios_profile_page.get_profile_screen_country_label().get_attribute('visible') == 'true'
            assert ios_profile_page.get_profile_screen_bio_text().get_attribute('visible') == 'true'

            if ios_profile_page.get_profile_screen_language_label():
                assert ios_profile_page.get_profile_screen_language_label().get_attribute('visible') == 'true'

        ios_profile_page.get_back_icon().click()
        assert ios_main_dashboard_page.account_signout().text == strings.ACCOUNT_SIGNOUT
        ios_main_dashboard_page.account_signout().click()
        setup_logging.info(' Ending Test Case --')
