"""
    Edit Profile screen's Test Module
"""

from tests.android.pages import android_elements
from tests.android.pages.android_edit_profile import AndroidEditProfile
from tests.android.pages.android_login_smoke import AndroidLoginSmoke
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
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
            User should be able to see the following contents by tapping on edit button from profile screen
            Edit profile screen title
            Edit Profile image
            User Name
            Change photo button
            Profile label
            Full profile button
            Limited profile button
            Limited profile instructions
            Birth Year
            Location
            Primary Language
            About Me
        """

        global_contents = Globals(setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_profile_screen = AndroidProfile(set_capabilities, setup_logging)
        edit_profile_screen = AndroidEditProfile(set_capabilities, setup_logging)

        assert android_main_dashboard_page.load_account_screen() == global_contents.ACCOUNT_ACTIVITY_NAME
        android_profile_screen.get_edit_profile_screen().click()
        assert edit_profile_screen.get_by_class_from_elements(
            android_elements.all_textviews,
            global_contents.first_existence).text == strings.EDIT_PROFILE_SCREEN_TITLE
        assert edit_profile_screen.get_element_by_id(android_elements.edit_profile_screen_image)\
            .get_attribute('displayed') == 'true'
        assert strings.EDIT_PROFILE_USER_NAME in edit_profile_screen.get_element_by_id(
            android_elements.edit_profile_user_name).get_attribute('content-desc')

    def test_update_profile_location(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can update location
            Verify that user can update language
            Verify that user can update information
        """

        global_contents = Globals(setup_logging)
        edit_profile_screen = AndroidEditProfile(set_capabilities, setup_logging)
        android_profile_screen = AndroidProfile(set_capabilities, setup_logging)

        if global_contents.enable_workflows is False:
            profile_view = edit_profile_screen.get_by_class_from_elements(
                android_elements.all_textviews, global_contents.seventh_existence).get_attribute('enabled')
            if profile_view.get_attribute('enabled') == 'false':
                edit_profile_screen.get_element_by_id(android_elements.edit_profile_full_view).click()

            edit_profile_screen.get_by_class_from_elements(
                android_elements.all_textviews,
                global_contents.sixth_existence).click()

            user_new_location = edit_profile_screen.change_user_location().text
            edit_profile_screen.change_user_location().click()
            assert user_new_location in edit_profile_screen.get_by_class_from_elements(
                android_elements.all_textviews,
                global_contents.sixth_existence).text
            android_profile_screen.get_navigation_icon().click()
            assert user_new_location in android_profile_screen.get_user_profile_location().text

    def test_update_profile_language(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can update language
        """

        global_contents = Globals(setup_logging)
        edit_profile_screen = AndroidEditProfile(set_capabilities, setup_logging)
        android_profile_screen = AndroidProfile(set_capabilities, setup_logging)

        if global_contents.enable_workflows is False:
            android_profile_screen.get_edit_profile_screen().click()
            edit_profile_screen.get_by_class_from_elements(
                android_elements.all_textviews,
                global_contents.seventh_existence).click()

            edit_profile_screen.change_user_language()[1].click()
            assert edit_profile_screen.get_by_class_from_elements(
                android_elements.all_textviews,
                global_contents.seventh_existence).text == strings.EDIT_PROFILE_SELECT_LANGUAGE_TEXT
            edit_profile_screen.get_by_class_from_elements(
                android_elements.all_textviews,
                global_contents.seventh_existence).click()
            edit_profile_screen.change_user_language()[0].click()
            assert edit_profile_screen.get_by_class_from_elements(
                android_elements.all_textviews,
                global_contents.seventh_existence).text == strings.EDIT_PROFILE_UPDATE_LANGUAGE_TEXT

    def test_update_profile_information(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can update information
        """

        global_contents = Globals(setup_logging)
        edit_profile_screen = AndroidEditProfile(set_capabilities, setup_logging)

        if global_contents.enable_workflows is False:
            edit_profile_screen.get_by_class_from_elements(
                android_elements.all_textviews,
                global_contents.eight_existence).click()
            edit_profile_screen.change_user_info()
            assert edit_profile_screen.get_by_class_from_elements(
                android_elements.all_textviews,
                global_contents.eight_existence).text == strings.EDIT_PROFILE_NEW_INFO_TEXT

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can logout from course subsection screen
        """

        global_contents = Globals(setup_logging)
        android_profile_screen = AndroidProfile(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_profile_screen.get_navigation_icon().click()
        android_profile_screen.get_navigation_icon().click()

        assert android_main_dashboard_page.log_out() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
