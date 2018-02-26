"""
    Whats New Test Module
"""

from input_data import InputData
from common.globals import Globals
from android.pages.android_whats_new import AndroidWhatsNew

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
        log.info('-- Starting {} Test Case'.format(TestAndroidWhatsNew.__name__))
        if login:
            log.info('{} is successfully logged in'.format(InputData.login_user_name))

    def test_validate_ui_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify following contents are visible on screen, 
                    "Screen Title", "Cross Icon", "Main Feature Image",
                     "Feature Title", "Feature Details", "Done"
                Verify all screen contents have their default values
        """

        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)

        assert android_whats_new_page.get_title_textview()

        assert android_whats_new_page.get_cross_icon()

        assert android_whats_new_page.get_main_image()

        assert android_whats_new_page.get_feature_title_textview()

        assert android_whats_new_page.get_feature_details()

        assert android_whats_new_page.get_done_button()

    def test_close_features_screen_smoke(self, set_capabilities, setup_logging):
        """
        Verifies that user can close New Feature screen and move to Main Dashboard screen
        """

        log = setup_logging
        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        assert android_whats_new_page.exit_features() == Globals.VIEW_MY_COURSES_ACTIVITY_NAME

        log.info('-- Ending {} Test Case'.format(TestAndroidWhatsNew.__name__))
