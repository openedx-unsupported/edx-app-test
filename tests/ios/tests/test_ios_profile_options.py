"""
    Profile screen Test Module
"""
from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_whats_new import IosWhatsNew
from tests.ios.pages.ios_profile_options import IosProfileOptions
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages import ios_elements


class TestIosProfileOptions:
    """
    Profile Options screen's Test Case
    """

    def test_start_profile_options_smoke(self, login, set_capabilities, setup_logging):
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

    def test_validate_video_settings_cell_elements(self, set_capabilities, setup_logging):
        """
        Verify that video settings cell will show following contents:
            Close icon
            "Profile" as Title
            Video Settings label
            Wifi only download
            Wifi switch
            Video download quality label
            Video quality description
        """

        global_contents = Globals(setup_logging)
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        ios_profile_options_page = IosProfileOptions(set_capabilities, setup_logging)

        assert ios_main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        ios_main_dashboard_page.get_drawer_icon().click()

        assert ios_profile_options_page.get_all_textviews()[1].text == strings.PROFILE_SCREEN_TITLE

        profile_options_close_button = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_close_button)
        assert profile_options_close_button.text == strings.CLOSE_BUTTON_TEXT

        profile_options_close_button.click()
        ios_main_dashboard_page.get_drawer_icon().click()

        wifi_switch = global_contents.get_element_by_id(set_capabilities, ios_elements.profile_options_wifi_switch)
        assert wifi_switch.text

        video_settings_option_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_video_settings_option_label)
        assert video_settings_option_label.text == strings.PROFILE_OPTIONS_VIDEO_SETTINGS_OPTION_LABEL

        videos_setting_cell = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_videos_setting_cell)
        assert videos_setting_cell.get_attribute('visible') == 'true'

        video_settings_description_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_video_settings_description_label)
        assert video_settings_description_label.text == strings.PROFILE_OPTIONS_VIDEO_SETTINGS_DESCRIPTION_LABEL

        video_quality_description_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_video_quality_description_label)
        assert video_quality_description_label.text == strings.PROFILE_OPTIONS_VIDEO_QUALITY_DESCRIPTION_LABEL

        video_quality_subtitle_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_video_quality_subtitle_label)
        assert video_quality_subtitle_label.text == strings.VIDEO_DOWNLOAD_AUTO_QUALITY

        wifi_cell = global_contents.get_element_by_id(set_capabilities, ios_elements.profile_options_wifi_cell)
        assert wifi_cell.get_attribute('visible') == 'true'

    def test_validate_personal_information_cell_elements(self, set_capabilities, setup_logging):
        """
        Verify that personal information cell will show following contents:
        Personal information label
        Email
        Username
        Profile image
        """

        global_contents = Globals(setup_logging)

        personal_information_option_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_personal_information_option_label)
        assert personal_information_option_label.text == strings.PROFILE_OPTIONS_PERSONAL_INFORMATION_LABEL

        personal_information_email_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_personal_information_email_label)
        assert personal_information_email_label.get_attribute('visible') == 'true'

        personal_information_username_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_personal_information_username_label)
        assert personal_information_username_label.get_attribute('visible') == 'true'

        personal_information_profile_view = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_personal_information_profile_view)
        assert personal_information_profile_view.get_attribute('visible') == 'true'

    def test_validate_video_help_cell_elements(self, set_capabilities, setup_logging):
        """
        Verify that help cell will show following contents:
            Help cell
            Submit feedback title
            Submit feedback description
            Email support team button
            Get support cell title
            Get support description
            View FAQ button
        """

        global_contents = Globals(setup_logging)
        help_cell = global_contents.get_element_by_id(set_capabilities, ios_elements.profile_options_help_cell)
        assert help_cell.get_attribute('visible') == 'true'

        help_cell_feedback_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_help_cell_feedback_label)
        assert help_cell_feedback_label.text == strings.PROFILE_OPTIONS_FEEDBACK_LABEL

        help_cell_subtitle_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_help_cell_subtitle_label)
        assert help_cell_subtitle_label.text == strings.PROFILE_OPTIONS_FEEDBACK_SUBTITLE_LABEL

        help_cell_support_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_help_cell_support_label)
        assert help_cell_support_label.text == strings.PROFILE_OPTIONS_SUPPORT_LABEL

        help_cell_support_subtitle_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_help_cell_support_subtitle_label)
        assert help_cell_support_subtitle_label.text == strings.PROFILE_OPTIONS_SUPPORT_SUBTITLE_LABEL

        help_cell_option_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_help_cell_option_label)
        assert help_cell_option_label.get_attribute('visible') == 'true'

        email_feedback_button = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_email_feedback_button)
        assert email_feedback_button.text == strings.PROFILE_OPTIONS_EMAIL_FEEDBACK_BUTTON

        view_faq_button = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_view_faq_button)
        assert view_faq_button.text == strings.PROFILE_OPTIONS_FAQ_BUTTON

    def test_validate_signout_and_delete_cell_elements(self, set_capabilities, setup_logging):
        """
        Verify that Profile Options screen will show following contents:
            Sign out button
            App version
            Delete account button
            Delete account description
        """

        global_contents = Globals(setup_logging)
        ios_profile_options_page = IosProfileOptions(set_capabilities, setup_logging)

        delete_account_button = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_delete_button)
        global_contents.scroll_from_element(set_capabilities, delete_account_button)

        signout_version_cell = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_signout_version_cell)
        assert signout_version_cell.get_attribute('visible') == 'true'

        signout_button = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_signout_button)
        assert signout_button.text == strings.PROFILE_OPTIONS_SIGNOUT_BUTTON

        signout_version_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_signout_version_label)
        assert signout_version_label.text == strings.PROFILE_OPTIONS_SIGNOUT_VERSION

        delete_account_cell = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_delete_account_cell)
        assert delete_account_cell.get_attribute('visible') == 'true'
        assert delete_account_button.text == strings.PROFILE_OPTIONS_DELETE_ACCOUNT_BUTTON

        account_info_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_delete_account_info_label)
        assert account_info_label.text == strings.PROFILE_OPTIONS_DELETE_INFO_LABEL

        delete_account_button.click()
        assert ios_profile_options_page.get_all_textviews()[0].text == strings.DELETE_ACCOUNT_PAGE_TITLE
        set_capabilities.back()

        video_settings_description_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_video_settings_description_label)
        global_contents.scroll_from_element(set_capabilities, video_settings_description_label)

    def test_allow_cellular_download_smoke(self, set_capabilities, setup_logging):
        """
        Verify that wifi switch is turned ON by default
        Verify that turning the switch ON again will open Allow cellular download popup
        Verify that cellular download popup show these elements
        "Allow Cellular Download" as Title
        Allow cellular download Description
        Don't allow button
        Allow button
        Verify that clicking allow button will turn the wifi switch ON
        Verify that clicking Don't allow button will turn the wifi switch OFF
        """

        global_contents = Globals(setup_logging)
        ios_profile_options_page = IosProfileOptions(set_capabilities, setup_logging)

        wifi_switch = global_contents.get_element_by_id(set_capabilities, ios_elements.profile_options_wifi_switch)
        assert wifi_switch.text == strings.PROFILE_OPTIONS_WIFI_TOGGLE_ON

        wifi_switch.click()
        assert wifi_switch.text == strings.PROFILE_OPTIONS_WIFI_TOGGLE_OFF
        wifi_switch.click()

        cellular_download_popup_title = ios_profile_options_page.get_all_textviews()[2]
        assert cellular_download_popup_title.text == strings.CELLULAR_DOWNLOAD_POPUP_TITLE_IOS

        cellular_download_popup_message = ios_profile_options_page.get_all_textviews()[3]
        assert cellular_download_popup_message.text == strings.CELLULAR_DOWNLOAD_POPUP_MESSAGE_IOS

        cellular_popup_allow_button = ios_profile_options_page.get_all_buttons()[6]
        cellular_popup_dont_allow_button = ios_profile_options_page.get_all_buttons()[5]
        assert cellular_popup_allow_button.text == strings.CELLULAR_DOWNLOAD_POPUP_ALLOW_BUTTON
        assert cellular_popup_dont_allow_button.text == strings.CELLULAR_DOWNLOAD_POPUP_DONT_ALLOW_BUTTON

        cellular_popup_dont_allow_button.click()
        assert wifi_switch.text == strings.PROFILE_OPTIONS_WIFI_TOGGLE_OFF
        wifi_switch.click()
        allow_button = ios_profile_options_page.get_all_buttons()[6]
        allow_button.click()
        assert wifi_switch.text == strings.PROFILE_OPTIONS_WIFI_TOGGLE_ON

    def test_vide_download_quality_smoke(self, set_capabilities, setup_logging):
        """
        Verify that clicking video quality cell will open Video quality popup
        Verify that video quality popup show following elements
        "Video download quality" as title
        Back icon, Close icon
        Auto Recommended, 360p (smallest file size), 540p, 720p (Best quality)
        Verify that clicking all the qualities will select that quality and
        show it in Profile options screen
        Verify that user can logout from profile options screen successfully
        """

        global_contents = Globals(setup_logging)
        ios_profile_options_page = IosProfileOptions(set_capabilities, setup_logging)
        ios_login_page = IosLogin(set_capabilities, setup_logging)

        video_quality_subtitle_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_video_quality_subtitle_label)
        video_quality_subtitle_label.click()
        video_quality_popup_back_icon = global_contents.get_element_by_id(
            set_capabilities, ios_elements.video_quality_popup_back_icon)
        assert video_quality_popup_back_icon.text == strings.VIDEO_DOWNLOAD_QUALITY_POPUP_BACK_ICON

        video_quality_popup_title = ios_profile_options_page.get_all_textviews()[1]
        assert video_quality_popup_title.text == strings.VIDEO_DOWNLOAD_QUALITY_POPUP_TITLE

        video_quality_popup_description = ios_profile_options_page.get_all_textviews()[2]
        assert video_quality_popup_description.text == strings.VIDEO_DOWNLOAD_QUALITY_POPUP_DESCRIPTION

        video_auto_quality = ios_profile_options_page.get_all_textviews()[3]
        assert video_auto_quality.text == strings.VIDEO_DOWNLOAD_AUTO_QUALITY
        video_auto_quality.click()
        video_quality_popup_back_icon = global_contents.get_element_by_id(
            set_capabilities, ios_elements.video_quality_popup_back_icon)

        video_quality_popup_back_icon.click()
        video_quality_subtitle_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_video_quality_subtitle_label)
        assert video_quality_subtitle_label.text == strings.VIDEO_DOWNLOAD_AUTO_QUALITY

        video_quality_subtitle_label.click()
        video_360p_quality = ios_profile_options_page.get_all_textviews()[4]
        assert video_360p_quality.text == strings.VIDEO_DOWNLOAD_360p_QUALITY
        video_360p_quality.click()
        video_quality_popup_back_icon.click()
        assert video_quality_subtitle_label.text == strings.VIDEO_DOWNLOAD_360p_QUALITY

        video_quality_subtitle_label.click()
        video_540p_quality = ios_profile_options_page.get_all_textviews()[5]
        assert video_540p_quality.text == strings.VIDEO_DOWNLOAD_540p_QUALITY
        video_540p_quality.click()
        video_quality_popup_back_icon.click()
        assert video_quality_subtitle_label.text == strings.VIDEO_DOWNLOAD_540p_QUALITY

        video_quality_subtitle_label.click()
        video_720_quality = ios_profile_options_page.get_all_textviews()[6]
        assert video_720_quality.text == strings.VIDEO_DOWNLOAD_720p_QUALITY
        video_720_quality.click()
        video_quality_popup_back_icon.click()
        assert video_quality_subtitle_label.text == strings.VIDEO_DOWNLOAD_720p_QUALITY

        global_contents.get_element_by_id(set_capabilities, ios_elements.profile_options_signout_button).click()
        assert ios_login_page.get_logo()
        setup_logging.info(' Ending Test Case --')
