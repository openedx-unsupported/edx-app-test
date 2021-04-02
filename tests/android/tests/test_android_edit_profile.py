"""
    Edit Profile screen's Test Module
"""

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_account import AndroidAccunts
from tests.android.tests.android_login_smoke import AndroidLoginSmoke
from tests.android.pages.android_edit_profile import AndroidEditProfile
from tests.android.pages.android_profile import AndroidProfile
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidEditProfile(AndroidLoginSmoke):
    """
    User Edit Profile screen's Test Case

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
        android_profile_screen = AndroidProfile(set_capabilities, setup_logging)
        edit_profile_screen = AndroidEditProfile(set_capabilities, setup_logging)

        assert android_main_dashboard_page.load_profile_screen() == global_contents.PROFILE_ACTIVITY_NAME
        android_profile_screen.get_edit_profile_screen().click()
        assert edit_profile_screen.get_edit_profile_screen_title().text == strings.EDIT_PROFILE_SCREEN_TITLE
        assert edit_profile_screen.get_edit_profile_image().get_attribute('displayed') == 'true'
        assert strings.EDIT_PROFILE_USER_NAME in edit_profile_screen.get_edit_profile_user_name().get_attribute('content-desc')
        assert edit_profile_screen.get_edit_profile_change_photo().get_attribute('content-desc') == strings.EDIT_PROFILE_CHANGE_PHOTO_TEXT
        assert edit_profile_screen.get_edit_profile_label().text == strings.EDIT_PROFILE_LABEL_TEXT
        assert edit_profile_screen.get_edit_profile_full_view().text == strings.EDIT_PROFILE_FULL_VIEW_TEXT
        assert edit_profile_screen.get_edit_profile_limited_view().text == strings.EDIT_PROFILE_LIMITED_VIEW_TEXT
        assert edit_profile_screen.get_edit_profile_instructions().text == strings.EDIT_PROFILE_INSTRUCTIONS_TEXT
        assert strings.EDIT_PROFILE_BIRTH_YEAR_TEXT in edit_profile_screen.get_edit_profile_birth_year().text
        assert strings.EDIT_PROFILE_LOCATION_TEXT in edit_profile_screen.get_edit_profile_location().text
        assert strings.EDIT_PROFILE_LANGUAGE_TEXT in edit_profile_screen.get_edit_profile_language().text
        assert strings.EDIT_PROFILE_ABOUT_ME_TEXT in edit_profile_screen.get_edit_profile_about_me().text
