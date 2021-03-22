# coding=utf-8
"""
    Account screen's Test Module
"""

from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_account import AndroidAccunts
from tests.android.tests.android_login_smoke import AndroidLoginSmoke
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidAccounts(AndroidLoginSmoke):
    """
    User Account screen's Test Case

    """

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that Account screen will show following contents:
                Back icon
                Specific "Account" as Title
                Profile
                Settings
                Submit_feedback
                Logout
        """

        global_contents = Globals(setup_logging)
        android_accounts_screen = AndroidAccunts(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        assert android_main_dashboard_page.load_account_screen() == global_contents.ACCOUNT_ACTIVITY_NAME

        assert android_accounts_screen.get_navigation_icon().get_attribute('content-desc') \
            == strings.ACCOUNT_SCREEN_NAVIGATION_ICON

        assert android_accounts_screen.get_profile_row().text == strings.PROFILE_SCREEN_TITLE

        assert android_accounts_screen.get_settings_row().text == strings.ACCOUNT_SETTINGS

        assert android_accounts_screen.get_submit_feedback_row().text == strings.ACCOUNT_SUBMIT_FEEDBACK

        assert android_accounts_screen.get_logout_row().text == strings.ACCOUNT_LOGOUT

    def test_load_contents_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify on tapping "Back icon" will load Main dashboard screen
            Verify on tapping "Profile" will load Profile
            Verify on tapping "Settings" will load Settings screen
            Verify on tapping "Logout" will logout user
        """

        global_contents = Globals(setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_accounts_screen = AndroidAccunts(set_capabilities, setup_logging)

        android_accounts_screen.get_navigation_icon().click()
        assert android_accounts_screen.on_screen() == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME

        assert android_main_dashboard_page.load_account_screen() == global_contents.ACCOUNT_ACTIVITY_NAME
        assert android_accounts_screen.load_profile_activity() == global_contents.PROFILE_ACTIVITY_NAME
        set_capabilities.back()
        assert android_accounts_screen.load_settings_activity() == global_contents.SETTINGS_ACTIVITY_NAME
        set_capabilities.back()
        assert android_main_dashboard_page.log_out() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
