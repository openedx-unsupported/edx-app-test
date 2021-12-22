"""
    Profile screen Test Module
"""
from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages import ios_elements
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_whats_new import IosWhatsNew
from tests.ios.pages.ios_profile import IosProfile
from tests.ios.pages.ios_edit_profile import IosEditProfile


class TestIosEditProfile:
    """
    Edit Profile screen's Test Case
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

        if global_contents.is_first_time:
            ios_whats_new_page = IosWhatsNew(set_capabilities, setup_logging)
            assert ios_whats_new_page.exit_features().text == strings.BLANK_FIELD
        else:
            ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
            assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            User should be able to see the following contents by tapping on edit button from profile screen
            Edit profile screen title
            Edit Profile image
            User Name
            Change photo button
        """

        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        ios_profile_page = IosProfile(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert ios_main_dashboard_page.get_drawer_icon().text == strings. MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        ios_main_dashboard_page.get_drawer_icon().click()
        ios_profile_page.get_personal_information_profile_cell().click()
        assert ios_profile_page.get_subsection_title().text == strings.PROFILE_SCREEN_TITLE
        assert ios_profile_page.get_navigation_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        assert ios_profile_page.get_profile_screen_edit_profile_button().get_attribute('label') == \
            strings.IOS_PROFILE_SCREEN_EDIT_PROFILE_BUTTON_TEXT
        assert ios_profile_page.get_profile_screen_username_label().get_attribute('visible') == 'true'

        ios_profile_page.get_profile_screen_edit_profile_button().click()
        title_element = ios_profile_page.get_subsection_title()
        assert title_element.get_attribute('value') == strings.EDIT_PROFILE_SCREEN_TITLE

        edit_profile_screen_image = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_screen_image)
        assert edit_profile_screen_image.get_attribute('enabled') == 'true'

        edit_profile_user_name = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_user_name)
        assert edit_profile_user_name.get_attribute('visible') == 'true'

        edit_profile_change_photo = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_change_photo)
        assert edit_profile_change_photo.get_attribute('visible') == 'true'

    def test_profile_views_ui_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            User should be able to see the following contents on edit profile screen
            Profile label
            Full profile button
            Limited profile button
            Limited profile instructions
            By clicking change photo button user can see these following options:
                Take photo
                Choose photo
                Remove photo
        """

        global_contents = Globals(setup_logging)
        ios_profile_page = IosProfile(set_capabilities, setup_logging)

        edit_profile_change_photo = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_change_photo)
        edit_profile_change_photo.click()
        edit_profile_choose_photo_option = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_choose_photo_option)
        assert edit_profile_choose_photo_option.text == strings.EDIT_PROFILE_CHOOSE_PHOTO_TEXT

        edit_profile_remove_photo_option = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_remove_photo_option)
        assert edit_profile_remove_photo_option.text == strings.EDIT_PROFILE_REMOVE_PHOTO_TEXT_IOS

        edit_profile_cancel_photo_option = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_cancel_photo_option)
        assert edit_profile_cancel_photo_option.text == strings.EDIT_PROFILE_CANCEL_PHOTO_POPUP
        edit_profile_cancel_photo_option.click()
        title_element = ios_profile_page.get_subsection_title()
        assert title_element.get_attribute('value') == strings.EDIT_PROFILE_SCREEN_TITLE

        edit_profile_subtitle_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_subtitle_label)
        assert edit_profile_subtitle_label.text == strings.EDIT_PROFILE_LABEL_TEXT

        edit_profile_full_view = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_full_view)
        assert edit_profile_full_view.get_attribute('label') == strings.EDIT_PROFILE_FULL_VIEW_TEXT

        edit_profile_limited_view = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_limited_view)
        assert edit_profile_limited_view.get_attribute('label') == strings.EDIT_PROFILE_LIMITED_VIEW_TEXT

        edit_profile_instructions = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_instructions)
        assert edit_profile_instructions.text == strings.EDIT_PROFILE_INSTRUCTIONS_TEXT

    def test_profile_views_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that all content should be enabled for full profile view
            Verify that these contents will be disabled for limited profile view
                location
                language
                about me

        """
        ios_profile_page = IosProfile(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        edit_profile_full_view = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_full_view)
        edit_profile_full_view.click()
        edit_profile_change_location = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_change_location)
        assert edit_profile_change_location.text == strings.EDIT_PROFILE_LOCATION_TEXT
        edit_profile_change_location.click()
        assert ios_profile_page.get_subsection_title().text == strings.EDIT_PROFILE_LOCATION_TITLE
        ios_profile_page.get_edit_profile_back_icon().click()

        edit_profile_change_language = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_change_language)
        assert edit_profile_change_language.text == strings.EDIT_PROFILE_LANGUAGE_TEXT
        edit_profile_change_language.click()
        assert ios_profile_page.get_subsection_title().text == strings.EDIT_PROFILE_LANGUAGE_TITLE
        ios_profile_page.get_edit_profile_back_icon().click()

        edit_profile_about_me = global_contents.get_element_by_id(set_capabilities, ios_elements.edit_profile_about_me)
        assert edit_profile_about_me.text == strings.EDIT_PROFILE_ABOUT_ME_TEXT
        edit_profile_about_me.click()
        assert ios_profile_page.get_subsection_title().text == strings.EDIT_PROFILE_ABOUT_ME_TITLE
        ios_profile_page.get_edit_profile_back_icon().click()

        edit_profile_limited_view = global_contents.get_element_by_id(set_capabilities,
                                                                      ios_elements.edit_profile_limited_view)
        edit_profile_limited_view.click()

        edit_profile_change_location = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_change_location)
        edit_profile_change_location.click()
        assert ios_profile_page.get_subsection_title().get_attribute('value') == strings.EDIT_PROFILE_SCREEN_TITLE

        edit_profile_change_language = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_change_language)
        edit_profile_change_language.click()
        assert ios_profile_page.get_subsection_title().get_attribute('value') == strings.EDIT_PROFILE_SCREEN_TITLE

    def test_update_profile_location(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can update location
            Verify that user can update language
            Verify that user can update information
        """

        ios_profile_page = IosProfile(set_capabilities, setup_logging)
        ios_edit_profile_page = IosEditProfile(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        edit_profile_full_view = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_full_view)
        edit_profile_full_view.click()
        edit_profile_change_location = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_change_location)
        edit_profile_change_location.click()

        new_location = ios_edit_profile_page.update_location_and_language(strings.EDIT_PROFILE_ALGERIA_LOCATION)
        ios_profile_page.get_edit_profile_back_icon().click()
        assert ios_edit_profile_page.get_location_on_edit_profile().get_attribute('value') == new_location

        edit_profile_change_location = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_change_location)
        edit_profile_change_location.click()
        old_location = ios_edit_profile_page.update_location_and_language(strings.EDIT_PROFILE_ALBANIA_LOCATION)
        ios_profile_page.get_edit_profile_back_icon().click()
        assert ios_edit_profile_page.get_location_on_edit_profile().get_attribute('value') == old_location

    def test_update_profile_language(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can update language
        """

        ios_profile_page = IosProfile(set_capabilities, setup_logging)
        ios_edit_profile_page = IosEditProfile(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        edit_profile_change_language = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_change_language)
        edit_profile_change_language.click()
        esperanto_language = ios_edit_profile_page.update_location_and_language(
            strings.EDIT_PROFILE_USER_ESPERANTO_LANGUAGE)
        ios_profile_page.get_edit_profile_back_icon().click()
        assert ios_edit_profile_page.check_language_on_edit_profile().get_attribute('value') == esperanto_language

        edit_profile_change_language = global_contents.get_element_by_id(
            set_capabilities, ios_elements.edit_profile_change_language)
        edit_profile_change_language.click()
        english_language = ios_edit_profile_page.update_location_and_language(
            strings.EDIT_PROFILE_USER_ENGLISH_LANGUAGE)
        ios_profile_page.get_edit_profile_back_icon().click()
        assert ios_edit_profile_page.check_language_on_edit_profile().get_attribute('value') == english_language

    def test_update_profile_information(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can update information
        """

        ios_profile_page = IosProfile(set_capabilities, setup_logging)
        ios_edit_profile_page = IosEditProfile(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        edit_profile_about_me = global_contents.get_element_by_id(set_capabilities, ios_elements.edit_profile_about_me)
        edit_profile_about_me.click()
        ios_edit_profile_page.change_user_info()
        ios_profile_page.get_edit_profile_back_icon().click()
        about_me_info = ios_edit_profile_page.check_information_on_edit_profile()
        assert about_me_info.get_attribute('value') in strings.EDIT_PROFILE_NEW_INFO_TEXT
