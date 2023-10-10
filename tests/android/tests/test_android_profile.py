"""
    User Profile Test Module
"""

from tests.android.pages import android_elements
from tests.android.pages.android_login_smoke import AndroidLoginSmoke
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.android.pages.android_profile_options import AndroidProfileOptions
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
        profile_options_page = AndroidProfileOptions(set_capabilities, setup_logging)

        profile_tab = android_main_dashboard_page.get_all_tabs()[2]
        assert profile_tab.text == 'Profile'
        profile_tab.click()
        profile_tab = android_main_dashboard_page.get_all_tabs()[2].click()
        screen_title = profile_options_page.get_all_textviews()[0]
        assert screen_title.text == strings.PROFILE_OPTIONS_SCREEN_TITLE
        user_image = global_contents.get_element_by_id(set_capabilities, android_elements.profile_screen_user_image)
        assert user_image.get_attribute('displayed') == 'true'
        user_image.click()
        assert android_profile_screen.get_user_profile_image().get_attribute('displayed') == 'true'
        if android_profile_screen.get_user_profile_language():
            assert android_profile_screen.get_user_profile_language().get_attribute('displayed') == 'true'

        set_capabilities.back()
        assert android_main_dashboard_page.log_out() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME
