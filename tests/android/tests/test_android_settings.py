"""
    Settings Screen Test Module
"""

from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_account import AndroidAccunts
from tests.android.pages.android_settings import AndroidSettings
from tests.android.tests.android_login_smoke import AndroidLoginSmoke
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidSettings(AndroidLoginSmoke):
    """
    User Settings screen's Test Case

    """

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
        accounts_screen = AndroidAccunts(set_capabilities, setup_logging)
        main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        settings_page = AndroidSettings(set_capabilities, setup_logging)
        assert main_dashboard_page.load_account_screen() == global_contents.ACCOUNT_ACTIVITY_NAME

        assert accounts_screen.get_settings_row().text == strings.ACCOUNT_SETTINGS
        assert accounts_screen.load_settings_activity() == global_contents.SETTINGS_ACTIVITY_NAME
        assert settings_page.get_navigation_icon().get_attribute('content-desc') \
            == strings.SETTINGS_SCREEN_NAVIGATION_ICON
        assert settings_page.on_screen() == global_contents.SETTINGS_ACTIVITY_NAME

        assert settings_page.get_settings_text().text == strings.SETTINGS_SCREEN_WIFI_SETTINGS_TEXT
        assert settings_page.get_download_content_text().text == strings.SETTINS_SCREEN_DOWNLOAD_CONTENT_TEXT
        assert settings_page.get_settings_wifi_toggle().text == strings.SETTINGS_SCREEN_WIFI_ON_TOGGLE

    def test_dialog_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Clicking toggle should show Dialog of "Allow cellular download"
            Verify that Dialog should have Following contents:
                Dialog title
                Dialog message
                Allow button
                Dont Allow button
            Verify that Clicking Dont Allow button should show Toggle ON
            Verify that Clicking Allow button should show Toggle OFF
        """

        global_contents = Globals(setup_logging)
        settings_page = AndroidSettings(set_capabilities, setup_logging)
        main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        assert settings_page.get_allow_cellular_download_dialog().get_attribute('displayed') == 'true'
        assert settings_page.get_dialog_title().text == strings.SETTINGS_SCREEN_DIALOG_TITLE
        assert settings_page.get_dialog_message().text == strings.SETTINGS_SCREEN_DIALOG_MESSAGE
        assert settings_page.get_dialog_dont_allow_button().text == \
            strings.SETTINGS_SCREEN_DIALOG_DONT_ALLOW_BUTTON
        assert settings_page.get_dialog_allow_button().text == strings.SETTINGS_SCREEN_DIALOG_ALLOW_BUTTON
        assert settings_page.check_dont_allow_button().text == strings.SETTINGS_SCREEN_WIFI_ON_TOGGLE
        assert settings_page.check_allow_button().text == strings.SETTINGS_SCREEN_WIFI_OFF_TOGGLE
        set_capabilities.back()
        assert main_dashboard_page.log_out() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
