"""
    Whats New Test Module
"""

from common import strings

from common.globals import Globals
from ios.pages.ios_whats_new import IosWhatsNew


class TestIosWhatsNew:
    """
    Whats New screen's Test Case
    """

    def test_start_whats_new_smoke(self, login, setup_logging, set_capabilities):
        """
        Scenarios:
            Verify Whats New screen is loaded successfully
        """

        log = setup_logging
        global_contents = Globals(log)
        log.info('-- Starting {} Test Case'.format(TestIosWhatsNew.__name__))
        if login:
            log.info('{} is successfully logged in'.format(global_contents.login_user_name))
        textview_screen_title = IosWhatsNew(set_capabilities, setup_logging).on_screen()
        assert textview_screen_title.text == strings.WHATS_NEW_IOS_SCREEN_TITLE

    def test_validate_ui_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify following contents are visible on screen, 
                    "Screen Title", "Cross Icon", "Main Feature Image",
                     "Feature Title", "Feature Details", "Done"
                Verify all screen contents have their default values
        """

        ios_whats_new_page = IosWhatsNew(set_capabilities, setup_logging)

        assert ios_whats_new_page.get_title_textview().text == strings.WHATS_NEW_IOS_SCREEN_TITLE
        assert ios_whats_new_page.get_close_button().text == strings.WHATS_NEW_CLOSE
        assert ios_whats_new_page.get_main_image()
        assert ios_whats_new_page.get_feature_title_textview().text == strings.WHATS_NEW_FEATURE_TITLE
        assert ios_whats_new_page.get_feature_details().text == strings.WHATS_NEW_FEATURE_DETAILS
        assert ios_whats_new_page.get_done_button().text == strings.WHATS_NEW_DONE

    def test_close_features_screen_smoke(self, set_capabilities, setup_logging):
        """
        Verifies that user can close New Feature screen and move to Main Dashboard screen
        """

        log = setup_logging
        ios_whats_new_page = IosWhatsNew(set_capabilities, setup_logging)

        assert ios_whats_new_page.exit_features().text == strings.MAIN_DASHBOARD_SCREEN_TITLE
        log.info('-- Ending {} Test Case'.format(TestIosWhatsNew.__name__))
