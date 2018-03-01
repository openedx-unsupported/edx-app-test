"""
    Whats New Test Module
"""

from android.pages.android_whats_new import AndroidWhatsNew
from common import strings
from common.globals import Globals



class TestAndroidWhatsNew:
    """
    Whats New screen's Test Case
    """

    def test_start_whats_new_smoke(self, login, setup_logging):
        """
        Scenarios:
            Verify Whats New screen is loaded successfully
        """

        log = setup_logging
        global_contents = Globals(log)
        log.info('-- Starting {} Test Case'.format(TestAndroidWhatsNew.__name__))
        if login:
            log.info('{} is successfully logged in'.format(global_contents.login_user_name))

    def test_validate_ui_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify following contents are visible on screen, 
                    "Screen Title", "Cross Icon", "Main Feature Image",
                     "Feature Title", "Feature Details", "Done"
                Verify all screen contents have their default values
        """

        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)

        assert android_whats_new_page.get_title_textview().text == strings.WHATS_NEW_ANDROID_SCREEN_TITLE
        assert android_whats_new_page.get_cross_icon()
        assert android_whats_new_page.get_main_image().text == strings.BLANK_FIELD
        assert android_whats_new_page.get_feature_title_textview().text == strings.WHATS_NEW_FEATURE_TITLE
        assert android_whats_new_page.get_feature_details().text == strings.WHATS_NEW_FEATURE_DETAILS
        assert android_whats_new_page.get_done_button().text == strings.WHATS_NEW_DONE

    def test_close_features_screen_smoke(self, set_capabilities, setup_logging):
        """
        Verifies that user can close New Feature screen and move to Main Dashboard screen
        """

        log = setup_logging
        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        assert android_whats_new_page.exit_features() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME

        log.info('-- Ending {} Test Case'.format(TestAndroidWhatsNew.__name__))
