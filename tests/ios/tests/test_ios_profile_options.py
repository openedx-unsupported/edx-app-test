"""
    Profile screen Test Module
"""
from tests.common import strings
from tests.common.globals import Globals
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_profile_options import IosProfileOptions
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages import ios_elements
from tests.ios.pages.ios_login_smoke import IosLoginSmoke


class TestIosProfileOptions(IosLoginSmoke):
    """
    Profile Options screen's Test Case
    """

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

        assert ios_profile_options_page.get_all_textviews()[0].text == strings.PROFILE_SCREEN_TITLE

        profile_options_close_button = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_close_button)
        assert profile_options_close_button.text == strings.CLOSE_BUTTON_TEXT

        profile_options_close_button.click()
        ios_main_dashboard_page.get_drawer_icon().click()

        wifi_switch = global_contents.get_element_by_id(set_capabilities, ios_elements.profile_options_wifi_switch)
        assert wifi_switch.text

        video_settings_option_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_video_settings_option_label)
        assert video_settings_option_label.text == strings.PROFILE_OPTIONS_VIDEO_SETTINGS_OPTION_LABEL_LOWER

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

    def test_allow_cellular_download_smoke(self, set_capabilities, setup_logging):
        """
        Verify that wifi switch is turned ON by default
        Verify that turning the switch ON again will open Allow cellular download popup
        Verify that cellular download popup show these elements
            "Allow Cellular Download" as Title
            "Allow cellular download Description
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

        cellular_download_popup_title = ios_profile_options_page.get_all_textviews()[1]
        assert cellular_download_popup_title.text == strings.CELLULAR_DOWNLOAD_POPUP_TITLE_IOS

        cellular_download_popup_message = ios_profile_options_page.get_all_textviews()[2]
        assert cellular_download_popup_message.text == strings.CELLULAR_DOWNLOAD_POPUP_MESSAGE_IOS

        cellular_popup_allow_button = ios_profile_options_page.get_all_buttons()[6]
        cellular_popup_dont_allow_button = ios_profile_options_page.get_all_buttons()[5]
        assert cellular_popup_allow_button.text == strings.CELLULAR_DOWNLOAD_POPUP_ALLOW_BUTTON
        assert cellular_popup_dont_allow_button.text == strings.CELLULAR_DOWNLOAD_POPUP_DONT_ALLOW_BUTTON

        cellular_popup_dont_allow_button.click()
        assert wifi_switch.text == strings.PROFILE_OPTIONS_WIFI_TOGGLE_ON
        wifi_switch.click()
        allow_button = ios_profile_options_page.get_all_buttons()[5]
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
        """

        global_contents = Globals(setup_logging)
        ios_profile_options_page = IosProfileOptions(set_capabilities, setup_logging)

        video_quality_subtitle_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_video_quality_subtitle_label)
        video_quality_subtitle_label.click()
        video_quality_popup_back_icon = global_contents.get_element_by_id(
            set_capabilities, ios_elements.video_quality_popup_back_icon)
        assert video_quality_popup_back_icon.text == strings.VIDEO_DOWNLOAD_QUALITY_POPUP_BACK_ICON

        video_quality_popup_title = ios_profile_options_page.get_all_textviews()[0]
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
        assert personal_information_option_label.text == strings.PROFILE_OPTIONS_PERSONAL_INFORMATION_LABEL_LOWER

        personal_information_email_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_personal_information_email_label)
        assert personal_information_email_label.get_attribute('visible') == 'true'

        personal_information_username_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_personal_information_username_label)
        assert personal_information_username_label.get_attribute('visible') == 'true'

        personal_information_profile_view = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_personal_information_profile_view)
        assert personal_information_profile_view.get_attribute('visible') == 'true'

    def test_validate_privacy_information_cell_elements(self, set_capabilities, setup_logging):
        """
        Verify that privacy information cell will show following contents:
            Privacy Policy
            Cookie Policy
            Do Not Sell My Personal Information
        """

        global_contents = Globals(setup_logging)

        privacy_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_privacy_cell_label)
        assert privacy_label.text == strings.PROFILE_OPTIONS_PRIVACY_CELL_LABEL

        privacy_policy = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_privacy_policy_label)
        assert privacy_policy.text == strings.PROFILE_OPTIONS_PRIVACY_POLICY_LABEL
        privacy_policy.click()
        back_icon = global_contents.get_element_by_id(
            set_capabilities, ios_elements.video_quality_popup_back_icon)
        assert back_icon.text == strings.PROFILE_OPTIONS_SCREEN_TITLE
        back_icon.click()

        cookie_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_cookie_policy_label)
        assert cookie_label.text == strings.PROFILE_OPTIONS_COOKIE_POLICY_LABEL
        cookie_label.click()
        back_icon.click()

        do_not_sell_info_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_do_not_sell_info_label)
        assert do_not_sell_info_label.text == strings.PROFILE_OPTIONS_DO_NOT_SELL_INFO_LABEL
        do_not_sell_info_label.click()
        back_icon.click()

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
            set_capabilities, ios_elements.profile_options_help_cell_support_subtitle_label)
        assert help_cell_subtitle_label.text == strings.PROFILE_OPTIONS_FEEDBACK_SUBTITLE_LABEL

        help_cell_support_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_help_cell_support_label)
        assert help_cell_support_label.text == strings.PROFILE_OPTIONS_SUPPORT_LABEL

        help_cell_support_subtitle_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_help_cell_subtitle_label)
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

        help_cell_feedback_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_help_cell_feedback_label)
        global_contents.scroll_from_element(set_capabilities, help_cell_feedback_label)

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
        delete_account_button = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_delete_button)
        assert delete_account_button.text == strings.PROFILE_OPTIONS_DELETE_ACCOUNT_BUTTON

        account_info_label = global_contents.get_element_by_id(
            set_capabilities, ios_elements.profile_options_delete_account_info_label)
        assert account_info_label.text == strings.PROFILE_OPTIONS_DELETE_INFO_LABEL

        delete_account_button.click()
        assert ios_profile_options_page.get_all_textviews()[0].text == strings.DELETE_ACCOUNT_PAGE_TITLE
        set_capabilities.back()

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that user can logout from profile options screen successfully
        """

        global_contents = Globals(setup_logging)
        ios_login_page = IosLogin(set_capabilities, setup_logging)

        global_contents.get_element_by_id(set_capabilities, ios_elements.profile_options_signout_button).click()
        assert ios_login_page.get_logo()
        ios_main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
        assert ios_main_dashboard_page.load_ios_landing_page(
            set_capabilities, setup_logging).text == strings.NEW_LANDING_MESSAGE_IOS
        setup_logging.info(' Ending Test Case --')
