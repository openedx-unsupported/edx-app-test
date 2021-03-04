"""
    User Profile Test Module
"""

from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_account import AndroidAccunts
from tests.android.pages.android_profile import AndroidProfile
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidProfile:
    """
    User Profile screen's Test Case

    """

    def test_start_main_dashboard_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully after successful login
        """

        global_contents = Globals(setup_logging)
        setup_logging.info('-- Starting {} Test Case'.format(TestAndroidProfile.__name__))
        if login:
            setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))

        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        android_whats_new_page.navigate_features()
        assert android_whats_new_page.navigate_features().text == strings.WHATS_NEW_DONE
        assert android_whats_new_page.exit_features() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that Profile screen will show following contents:
                Back icon
                "Profile" as Title
                Edit
                Profile Image
                User Name
            Verify that Profile screen will show following contents for limited profile:
                Age limit text
                Account settings Button
            Verify that Profile screen will show following contents for limited profile:
                location
                Laguage (if selected)
                User Bio
        """

        global_contents = Globals(setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_accounts_screen = AndroidAccunts(set_capabilities, setup_logging)
        android_profile_screen = AndroidProfile(set_capabilities, setup_logging)

        assert android_main_dashboard_page.load_account_screen() == global_contents.ACCOUNT_ACTIVITY_NAME
        assert android_accounts_screen.load_profile_activity() == global_contents.PROFILE_ACTIVITY_NAME

        android_profile_screen.get_navigation_icon().click()
        assert android_profile_screen.get_account_activity() == global_contents.ACCOUNT_ACTIVITY_NAME
        assert android_accounts_screen.load_profile_activity() == global_contents.PROFILE_ACTIVITY_NAME
        android_profile_screen.get_edit_profile_screen().click()
        android_profile_screen.get_navigation_icon().click()
        assert android_profile_screen.get_user_profile_image().get_attribute('displayed') == 'true'
        assert android_profile_screen.get_user_profile_name().get_attribute('displayed') == 'true'

        if android_profile_screen.get_limited_profile_view():
            assert android_profile_screen.get_profile_age_text_note().text == strings.PROFILE_AGE_LIMIT_TEXT
            assert android_profile_screen.get_profile_account_settings_button().text \
                == strings.PROFILE_ACCOUNT_SETTINGS_BUTTON
        else:
            assert android_profile_screen.get_user_profile_location().get_attribute('displayed') == 'true'

            if android_profile_screen.get_user_profile_language():
                assert android_profile_screen.get_user_profile_language().get_attribute('displayed') == 'true'

            assert android_profile_screen.get_user_profile_bio().get_attribute('displayed') == 'true'
