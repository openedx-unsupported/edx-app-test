"""
    Main Profile Options Test Module
"""
from tests.android.pages import android_elements
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.tests.android_login_smoke import AndroidLoginSmoke
from tests.android.pages.android_profile_options import AndroidProfileOptions
from tests.common.globals import Globals
from tests.common import strings


class TestAndroidProfileOptions(AndroidLoginSmoke):
    """
    Profile Option screen's Test Case
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

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        profile_options_page = AndroidProfileOptions(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert android_main_dashboard_page.get_menu_icon().get_attribute('content-desc') \
            == strings.PROFILE_SCREEN_TITLE
        android_main_dashboard_page.get_menu_icon().click()

        navigation_icon = profile_options_page.get_all_image_buttons()[0]
        assert navigation_icon.get_attribute('content-desc') == strings.PROFILE_OPTIONS_SCREEN_NAVIGATION_ICON
        navigation_icon.click()
        android_main_dashboard_page.get_menu_icon().click()
        screen_title = profile_options_page.get_all_textviews()[0]
        assert screen_title.text == strings.PROFILE_OPTIONS_SCREEN_TITLE

        video_settings_option_label = profile_options_page.get_all_textviews()[1]
        assert video_settings_option_label.text == strings.PROFILE_OPTIONS_VIDEO_SETTINGS_OPTION_LABEL

        wifi_only_download_label = profile_options_page.get_all_textviews()[2]
        assert wifi_only_download_label.text == strings.PROFILE_OPTIONS_VIDEO_SETTINGS_DESCRIPTION_LABEL

        wifi_switch = global_contents.get_element_by_id(set_capabilities, android_elements.profile_options_wifi_switch)
        assert wifi_switch.text == strings.PROFILE_OPTIONS_WIFI_TOGGLE_ON_ANDROID

        download_content_subtitle = profile_options_page.get_all_textviews()[3]
        assert download_content_subtitle.text == strings.SETTINS_SCREEN_DOWNLOAD_CONTENT_TEXT_ANDROID

        video_download_quality_description = profile_options_page.get_all_textviews()[4]
        assert video_download_quality_description.text == strings.PROFILE_OPTIONS_VIDEO_QUALITY_DESCRIPTION_LABEL

        video_quality_subtitle_label = global_contents.get_element_by_id(
            set_capabilities, android_elements.profile_options_video_quality_subtitle_label)
        assert video_quality_subtitle_label.text == strings.VIDEO_DOWNLOAD_AUTO_QUALITY

    def test_validate_personal_information_cell_elements(self, set_capabilities, setup_logging):
        """
        Verify that personal information cell will show following contents:
        Personal information label
        Email
        Username
        Profile image
        """

        global_contents = Globals(setup_logging)
        profile_options_page = AndroidProfileOptions(set_capabilities, setup_logging)

        personal_information_label = profile_options_page.get_all_textviews()[6]
        assert personal_information_label.text == strings.PROFILE_OPTIONS_PERSONAL_INFORMATION_LABEL

        personal_information_email_label = global_contents.get_element_by_id(
            set_capabilities, android_elements.profile_options_personal_information_email_label)
        assert personal_information_email_label.get_attribute('displayed') == 'true'

        personal_information_username_label = global_contents.get_element_by_id(
            set_capabilities, android_elements.profile_options_personal_information_username_label)
        assert personal_information_username_label.get_attribute('displayed') == 'true'

        personal_information_profile_view = global_contents.get_element_by_id(
            set_capabilities, android_elements.profile_options_personal_information_profile_view)
        assert personal_information_profile_view.get_attribute('displayed') == 'true'

        personal_information_profile_view = global_contents.get_element_by_id(
            set_capabilities, android_elements.profile_options_personal_information_image_view)
        assert personal_information_profile_view.get_attribute('displayed') == 'true'

    def test_validate_help_cell_elements(self, set_capabilities, setup_logging):
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
        profile_options_page = AndroidProfileOptions(set_capabilities, setup_logging)

        help_cell = global_contents.get_element_by_id(set_capabilities, android_elements.profile_options_help_cell)
        assert help_cell.text == strings.PROFILE_OPTIONS_HELP_CELL_TITLE

        submit_feedback_label = profile_options_page.get_all_textviews()[10]
        assert submit_feedback_label.text == strings.PROFILE_OPTIONS_FEEDBACK_LABEL

        support_subtitle = global_contents.get_element_by_id(
            set_capabilities, android_elements.profile_options_support_subtitle_label)
        assert support_subtitle.text == strings.PROFILE_OPTIONS_SUPPORT_SUBTITLE_LABEL

        email_feedback_button = global_contents.get_element_by_id(
            set_capabilities, android_elements.profile_options_email_feedback_button)
        assert email_feedback_button.text == strings.PROFILE_OPTIONS_EMAIL_FEEDBACK_BUTTON

        get_support_label = profile_options_page.get_all_textviews()[12]
        assert get_support_label.text == strings.PROFILE_OPTIONS_SUPPORT_LABEL

        get_support_description = global_contents.get_element_by_id(
            set_capabilities, android_elements.profile_options_support_description_label)
        assert get_support_description.text == strings.PROFILE_OPTIONS_FEEDBACK_SUBTITLE_LABEL

        view_faq_button = global_contents.get_element_by_id(
            set_capabilities, android_elements.profile_options_view_faq_button)
        assert view_faq_button.text == strings.PROFILE_OPTIONS_FAQ_BUTTON_ANDROID

        global_contents.scroll_from_element(set_capabilities, view_faq_button)

    def test_validate_signout_and_delete_cell_elements(self, set_capabilities, setup_logging):
        """
        Verify that Profile Options screen will show following contents:
            Sign out button
            App version
            Delete account button
            Delete account description
        """

        global_contents = Globals(setup_logging)
        profile_options_page = AndroidProfileOptions(set_capabilities, setup_logging)

        sign_out_button = global_contents.get_element_by_id(
            set_capabilities, android_elements.profile_options_signout_button)
        assert sign_out_button.text == strings.PROFILE_OPTIONS_SIGNOUT_BUTTON

        app_version = global_contents.get_element_by_id(set_capabilities, android_elements.profile_options_app_version)
        assert app_version.text == strings.PROFILE_OPTIONS_SIGNOUT_VERSION

        delete_account_button = global_contents.get_element_by_id(
            set_capabilities, android_elements.profile_options_delete_account_button)
        assert delete_account_button.text == strings.PROFILE_OPTIONS_DELETE_ACCOUNT_BUTTON

        delete_account_instructions = profile_options_page.get_all_textviews()[10]
        assert delete_account_instructions.text == strings.PROFILE_OPTIONS_DELETE_INFO_LABEL

        delete_account_button.click()
        assert profile_options_page.get_all_textviews()[0].text == strings.DELETE_ACCOUNT_PAGE_TITLE
        set_capabilities.back()

        personal_information_email_label = global_contents.get_element_by_id(
            set_capabilities, android_elements.profile_options_personal_information_email_label)

        global_contents.scroll_screen(set_capabilities, personal_information_email_label, delete_account_button)

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

        wifi_switch = global_contents.get_element_by_id(set_capabilities, android_elements.profile_options_wifi_switch)
        assert wifi_switch.text == strings.PROFILE_OPTIONS_WIFI_TOGGLE_ON_ANDROID
        wifi_switch.click()

        assert global_contents.wait_for_element_visibility(
            set_capabilities,
            android_elements.settings_screen_allow_cellular_download_dialog
        ).get_attribute('displayed') == 'true'

        title = global_contents.get_element_by_id(
            set_capabilities, android_elements.settings_screen_dialog_title)
        assert title.text == strings.SETTINGS_SCREEN_DIALOG_TITLE
        message = global_contents.get_element_by_id(
            set_capabilities, android_elements.settings_screen_dialog_message)
        assert message.text == strings.SETTINGS_SCREEN_DIALOG_MESSAGE
        dont_allow_button = global_contents.get_element_by_id(
            set_capabilities, android_elements.settings_screen_dialog_dont_allow_button)
        assert dont_allow_button.text == strings.SETTINGS_SCREEN_DIALOG_DONT_ALLOW_BUTTON
        allow_button = global_contents.get_element_by_id(
            set_capabilities, android_elements.settings_screen_dialog_allow_button)
        assert allow_button.text == strings.SETTINGS_SCREEN_DIALOG_ALLOW_BUTTON

        dont_allow_button.click()
        wifi_switch = global_contents.get_element_by_id(set_capabilities, android_elements.profile_options_wifi_switch)
        assert wifi_switch.text == strings.PROFILE_OPTIONS_WIFI_TOGGLE_ON_ANDROID
        wifi_switch.click()
        allow_button = global_contents.get_element_by_id(
            set_capabilities, android_elements.settings_screen_dialog_allow_button)
        allow_button.click()
        wifi_switch = global_contents.get_element_by_id(set_capabilities, android_elements.profile_options_wifi_switch)
        assert wifi_switch.text == strings.PROFILE_OPTIONS_WIFI_TOGGLE_OFF_ANDROID

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
        profile_options_page = AndroidProfileOptions(set_capabilities, setup_logging)

        video_quality_subtitle_label = global_contents.get_element_by_id(
            set_capabilities, android_elements.profile_options_video_quality_subtitle_label)
        assert video_quality_subtitle_label.text == strings.VIDEO_DOWNLOAD_AUTO_QUALITY
        video_quality_subtitle_label.click()

        video_quality_popup_title = global_contents.get_element_by_id(
            set_capabilities, android_elements.video_quality_popup_title)
        assert video_quality_popup_title.text == strings.VIDEO_DOWNLOAD_QUALITY_POPUP_TITLE

        video_quality_popup_description = global_contents.get_element_by_id(
            set_capabilities, android_elements.video_quality_popup_message)
        assert video_quality_popup_description.text == strings.VIDEO_DOWNLOAD_QUALITY_POPUP_DESCRIPTION

        video_auto_quality = profile_options_page.get_all_video_qualitie_titles()[0]
        assert video_auto_quality.text == strings.VIDEO_DOWNLOAD_AUTO_QUALITY

        video_360p_quality = profile_options_page.get_all_video_qualitie_titles()[1]
        assert video_360p_quality.text == strings.VIDEO_DOWNLOAD_360p_QUALITY
        video_360p_quality.click()
        assert video_quality_subtitle_label.text == strings.VIDEO_DOWNLOAD_360p_QUALITY

        video_quality_subtitle_label.click()
        video_540p_quality = profile_options_page.get_all_video_qualitie_titles()[2]
        assert video_540p_quality.text == strings.VIDEO_DOWNLOAD_540p_QUALITY
        video_540p_quality.click()
        assert video_quality_subtitle_label.text == strings.VIDEO_DOWNLOAD_540p_QUALITY

        video_quality_subtitle_label.click()
        video_720p_quality = profile_options_page.get_all_video_qualitie_titles()[3]
        assert video_720p_quality.text == strings.VIDEO_DOWNLOAD_720p_QUALITY
        video_720p_quality.click()
        assert video_quality_subtitle_label.text == strings.VIDEO_DOWNLOAD_720p_QUALITY

        video_quality_subtitle_label.click()
        cancel_button = global_contents.get_element_by_id(
            set_capabilities, android_elements.video_quality_cancel_button)
        cancel_button.click()
        assert video_quality_subtitle_label.text == strings.VIDEO_DOWNLOAD_720p_QUALITY

        sign_out_button = global_contents.get_element_by_id(
            set_capabilities, android_elements.profile_options_signout_button)
        sign_out_button.click()
        assert global_contents.wait_for_android_activity_to_load(
            set_capabilities,
            global_contents.NEW_LOGISTRATION_ACTIVITY_NAME) == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info(' Ending Test Case --')
