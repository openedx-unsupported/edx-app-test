"""
    User Profile Test Module
"""

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.android.tests.android_login_smoke import AndroidLoginSmoke
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidProfile(AndroidLoginSmoke):
    """
    User Profile screen's Test Case

    """

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
            Verify that Profile screen will show following contents for Full profile:
                location
                Language (if selected)
                User Bio
        """

        global_contents = Globals(setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_profile_screen = AndroidProfile(set_capabilities, setup_logging)

        assert android_main_dashboard_page.load_account_screen() == global_contents.ACCOUNT_ACTIVITY_NAME
        android_profile_screen.get_edit_profile_screen().click()

        android_profile_screen.get_navigation_icon().click()
        android_profile_screen.get_edit_profile_screen().click()
        android_profile_screen.get_navigation_icon().click()
        assert android_profile_screen.get_user_profile_image().get_attribute('displayed') == 'true'
        assert android_profile_screen.get_user_profile_name().get_attribute('displayed') == 'true'

        if android_profile_screen.get_limited_profile_view():
            if android_profile_screen.get_profile_account_settings_button():
                assert android_profile_screen.get_profile_age_text_note().text == strings.PROFILE_AGE_LIMIT_TEXT
                assert android_profile_screen.get_profile_account_settings_button().text \
                    == strings.PROFILE_ACCOUNT_SETTINGS_BUTTON
        else:
            assert android_profile_screen.get_user_profile_location().get_attribute('displayed') == 'true'

            if android_profile_screen.get_user_profile_language():
                assert android_profile_screen.get_user_profile_language().get_attribute('displayed') == 'true'

            assert android_profile_screen.get_user_profile_bio().get_attribute('displayed') == 'true'

        set_capabilities.back()
        assert android_main_dashboard_page.log_out() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME
