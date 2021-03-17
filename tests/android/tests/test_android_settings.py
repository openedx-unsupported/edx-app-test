# coding=utf-8
"""
    Settings Screen Test Module
"""

from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_account import AndroidAccunts
from tests.android.pages.android_settings import AndroidSettings
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidSettings:
    """
    User Settings screen's Test Case

    """

    def test_start_main_dashboard_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully after successful login
        """

        global_contents = Globals(setup_logging)
        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        setup_logging.info('-- Starting {} Test Case'.format(TestAndroidSettings.__name__))

        if login and android_whats_new_page.on_screen():
            android_whats_new_page.navigate_features()
            assert android_whats_new_page.navigate_features().text == strings.WHATS_NEW_DONE
            assert android_whats_new_page.exit_features() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME
        else:
            android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
            assert android_main_dashboard_page.on_screen() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME
        setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that Settings screen will show following contents:
                Settings screen should show these Header contents:
                Back icon
                "Setting" heading
                Setting Screen should show the following toggle options
                Wi-Fi only download
                On/OFF toggle
        """

        global_contents = Globals(setup_logging)
        android_accounts_screen = AndroidAccunts(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_settings_page = AndroidSettings(set_capabilities, setup_logging)
        assert android_main_dashboard_page.load_account_screen() == global_contents.ACCOUNT_ACTIVITY_NAME

        assert android_accounts_screen.get_settings_row().text == strings.ACCOUNT_SETTINGS
        assert android_accounts_screen.load_settings_activity() == global_contents.SETTINGS_ACTIVITY_NAME
        assert android_settings_page.get_navigation_icon().get_attribute('content-desc') \
            == strings.SETTINGS_SCREEN_NAVIGATION_ICON
        assert android_settings_page.on_screen() == global_contents.SETTINGS_ACTIVITY_NAME

        assert android_settings_page.get_settings_text().text == strings.SETTINGS_SCREEN_WIFI_SETTINGS_TEXT
        assert android_settings_page.get_download_content_text().text == strings.SETTINS_SCREEN_DOWNLOAD_CONTENT_TEXT
        assert android_settings_page.get_settings_wifi_toggel().text == strings.SETTINGS_SCREEN_WIFI_ON_TOGGEL

    def test_dialog_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Clicking toggle should show Dialog of "Allow cellular download"
            Verify that Dialog should have Following contents:
                Dialog title
                Dialog message
                Allow button
                Dont Allow button
            Verify that Clicking Dont Allow button should show Toggel ON
            Verify that Clicking Allow button should show Toggel OFF
        """

        global_contents = Globals(setup_logging)
        android_settings_page = AndroidSettings(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        assert android_settings_page.get_allow_cellular_download_dialog().get_attribute('displayed') == 'true'
        assert android_settings_page.get_dialog_title().text == strings.SETTINGS_SCREEN_DIALOG_TITLE
        assert android_settings_page.get_dialog_message().text == strings.SETTINGS_SCREEN_DIALOG_MESSAGE
        assert android_settings_page.get_dialog_dont_allow_button().text == \
            strings.SETTINGS_SCREEN_DIALOG_DONT_ALLOW_BUTTON
        assert android_settings_page.get_dialog_allow_button().text == strings.SETTINGS_SCREEN_DIALOG_ALLOW_BUTTON
        assert android_settings_page.check_dont_allow_button().text == strings.SETTINGS_SCREEN_WIFI_ON_TOGGEL
        assert android_settings_page.check_allow_button().text == strings.SETTINGS_SCREEN_WIFI_OFF_TOGGEL
        set_capabilities.back()
        assert android_main_dashboard_page.log_out() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
