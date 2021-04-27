"""
    Edit Profile screen's Test Module
"""

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.tests.android_login_smoke import AndroidLoginSmoke
from tests.android.pages.android_edit_profile import AndroidEditProfile
from tests.android.pages.android_profile import AndroidProfile
from tests.android.pages import android_elements
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
            By clicking change photo button user can see these following options:
                Take photo
                Choose photo
                Remove photo
        """

        global_contents = Globals(setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_profile_screen = AndroidProfile(set_capabilities, setup_logging)
        edit_profile_screen = AndroidEditProfile(set_capabilities, setup_logging)

        assert android_main_dashboard_page.load_profile_screen() == global_contents.PROFILE_ACTIVITY_NAME
        android_profile_screen.get_edit_profile_screen().click()
        assert edit_profile_screen.get_by_class_from_elements(android_elements.all_textviews, global_contents.first_existence).text \
            == strings.EDIT_PROFILE_SCREEN_TITLE
        assert edit_profile_screen.get_element_by_id(android_elements.edit_profile_screen_image)\
            .get_attribute('displayed') == 'true'
        assert strings.EDIT_PROFILE_USER_NAME in edit_profile_screen.get_element_by_id\
            (android_elements.edit_profile_user_name).get_attribute('content-desc')
        assert edit_profile_screen.get_element_by_id(android_elements.edit_profile_change_photo)\
            .get_attribute('content-desc') == strings.EDIT_PROFILE_CHANGE_PHOTO_TEXT
        assert edit_profile_screen.get_element_by_id(android_elements.edit_profile_label).text \
            == strings.EDIT_PROFILE_LABEL_TEXT
        assert edit_profile_screen.get_element_by_id(android_elements.edit_profile_full_view).text \
            == strings.EDIT_PROFILE_FULL_VIEW_TEXT
        assert edit_profile_screen.get_element_by_id(android_elements.edit_profile_limited_view).text \
            == strings.EDIT_PROFILE_LIMITED_VIEW_TEXT
        assert edit_profile_screen.get_element_by_id(android_elements.edit_profile_instructions).text \
            == strings.EDIT_PROFILE_INSTRUCTIONS_TEXT
        assert strings.EDIT_PROFILE_BIRTH_YEAR_TEXT in edit_profile_screen.get_by_class_from_elements\
            (android_elements.all_textviews, global_contents.sixth_existence).text
        assert strings.EDIT_PROFILE_LOCATION_TEXT in edit_profile_screen.get_by_class_from_elements\
            (android_elements.all_textviews, global_contents.seventh_existence).text
        assert strings.EDIT_PROFILE_LANGUAGE_TEXT in edit_profile_screen.get_by_class_from_elements\
            (android_elements.all_textviews, global_contents.eight_existence).text
        assert strings.EDIT_PROFILE_ABOUT_ME_TEXT in edit_profile_screen.get_by_class_from_elements\
            (android_elements.all_textviews, global_contents.ninth_existence).text

        edit_profile_screen.get_element_by_id(android_elements.edit_profile_change_photo).click()
        assert edit_profile_screen.get_by_id_from_elements(android_elements.edit_profile_change_photo_option, \
            global_contents.first_existence).text == strings.EDIT_PROFILE_TAKE_PHOTO_TEXT
        assert edit_profile_screen.get_by_id_from_elements(android_elements.edit_profile_change_photo_option, \
            global_contents.second_existence).text == strings.EDIT_PROFILE_CHOOSE_PHOTO_TEXT
        assert edit_profile_screen.get_by_id_from_elements(android_elements.edit_profile_change_photo_option, \
            global_contents.third_existence).text == strings.EDIT_PROFILE_REMOVE_PHOTO_TEXT
        set_capabilities.back()
        edit_profile_screen.get_by_class_from_elements(android_elements.all_textviews, \
            global_contents.sixth_existence).click()

    def test_change_birth_year_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that all options gets disabled when birth year is below 13 years
            Verify that all options gets enabled when birth year is below 13 years

        """

        global_contents = Globals(setup_logging)
        edit_profile_screen = AndroidEditProfile(set_capabilities, setup_logging)
        edit_profile_screen.change_birth_year_below_13()
        assert edit_profile_screen.get_by_class_from_elements(android_elements.all_textviews, \
            global_contents.seventh_existence).get_attribute('enabled') == 'false'
        assert edit_profile_screen.get_by_class_from_elements(android_elements.all_textviews, \
            global_contents.eight_existence).get_attribute('enabled') == 'false'
        assert edit_profile_screen.get_element_by_id(android_elements.edit_profile_change_photo)\
            .get_attribute('enabled') == 'false'
        assert edit_profile_screen.get_element_by_id(android_elements.edit_profile_full_view)\
            .get_attribute('enabled') == 'false'
        assert edit_profile_screen.get_element_by_id(android_elements.edit_profile_limited_view)\
            .get_attribute('enabled') == 'false'

        edit_profile_screen.get_by_class_from_elements(android_elements.all_textviews, \
            global_contents.sixth_existence).click()
        edit_profile_screen.change_birth_year_above_13()
        assert edit_profile_screen.get_element_by_id(android_elements.edit_profile_full_view)\
            .get_attribute('enabled') == 'true'
        assert edit_profile_screen.get_element_by_id(android_elements.edit_profile_limited_view)\
            .get_attribute('enabled') == 'true'
        assert edit_profile_screen.get_element_by_id(android_elements.edit_profile_change_photo)\
            .get_attribute('enabled') == 'true'

    def test_profile_views_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that all content should be anabled for full profile view
            Verify that these contents will be diabled for limited profile view
                location
                language
                about me

        """

        global_contents = Globals(setup_logging)
        edit_profile_screen = AndroidEditProfile(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_profile_screen = AndroidProfile(set_capabilities, setup_logging)

        edit_profile_screen.get_element_by_id(android_elements.edit_profile_full_view).click()
        assert edit_profile_screen.get_element_by_id(android_elements.edit_profile_full_view)\
            .get_attribute('checked') == 'true'
        assert edit_profile_screen.get_element_by_id(android_elements.edit_profile_limited_view)\
            .get_attribute('checked') == 'false'
        assert edit_profile_screen.get_by_class_from_elements(android_elements.all_textviews, \
            global_contents.seventh_existence).get_attribute('enabled') == 'true'
        assert edit_profile_screen.get_by_class_from_elements(android_elements.all_textviews, \
            global_contents.eight_existence).get_attribute('enabled') == 'true'
        assert edit_profile_screen.get_by_class_from_elements(android_elements.all_textviews, \
            global_contents.ninth_existence).get_attribute('enabled') == 'true'

        edit_profile_screen.get_element_by_id(android_elements.edit_profile_limited_view).click()
        assert edit_profile_screen.get_element_by_id(android_elements.edit_profile_limited_view)\
            .get_attribute('checked') == 'true'
        assert edit_profile_screen.get_element_by_id(android_elements.edit_profile_full_view)\
            .get_attribute('checked') == 'false'
        assert edit_profile_screen.get_by_class_from_elements(android_elements.all_textviews, \
            global_contents.seventh_existence).get_attribute('enabled')
        assert edit_profile_screen.get_by_class_from_elements(android_elements.all_textviews, \
            global_contents.eight_existence).get_attribute('enabled') == 'false'
        assert edit_profile_screen.get_by_class_from_elements(android_elements.all_textviews, \
            global_contents.ninth_existence).get_attribute('enabled') == 'false'
        android_profile_screen.get_navigation_icon().click()
        android_profile_screen.get_navigation_icon().click()

        assert android_main_dashboard_page.get_logout_account_option().text == strings.ACCOUNT_LOGOUT
        assert android_main_dashboard_page.log_out() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
