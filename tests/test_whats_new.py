from pages.whats_new import WhatsNew
from testdata.input_data import InputData
from common.strings import Strings
from common.globals import Globals


class TestWhatsNew():
    """
    Whats New screen's Test Case
    """

    def test_start_whats_new_smoke(self, login):
        """
        Scenarios:
            Verify Whats New screen is loaded successfully
        """

        print('-- Starting ', TestWhatsNew.__name__, 'Test Case')
        if login:
            print(InputData.login_user_name, 'is successfully logged in')

    def test_validate_ui_elements(self, set_capabilities):
        """
        Scenarios:
                Verify following contents are visible on screen, 
                    "Screen Title", "Cross Icon", "Main Feature Image",  "Feature Title", "Feature Details"
                    "Done"
                Verify all screen contents have their default values
        """

        whats_new_page = WhatsNew(set_capabilities)

        textview_screen_title = whats_new_page.get_title_textview()
        assert textview_screen_title is not None
        if InputData.target_environment == Strings.IOS:
            assert textview_screen_title.text == Strings.WHATS_NEW_IOS_SCREEN_TITLE
        assert whats_new_page.get_cross_icon() is not None

        if InputData.target_environment == Strings.ANDROID:
            assert whats_new_page.get_main_image() is not None

        textview_feature_title = whats_new_page.get_feature_title_textview()
        assert textview_feature_title is not None
        if InputData.target_environment == Strings.IOS:
            assert textview_feature_title.text == Strings.WHATS_NEW_FEATURE_TITLE

        textview_feature_details = whats_new_page.get_feature_details()
        assert textview_feature_details is not None
        if InputData.target_environment == Strings.IOS:
            assert textview_feature_details.text == Strings.WHATS_NEW_FEATURE_DETAILS

        button_done = whats_new_page.get_done_button()
        assert button_done is not None
        if InputData.target_environment == Strings.IOS:
            assert button_done.text == Strings.WHATS_NEW_DONE

    def test_close_features_screen_smoke(self, set_capabilities):
        """
        Verifies that user can close New Feature screen and move to Main Dashboard screen
        """

        whats_new_page = WhatsNew(set_capabilities)
        if InputData.target_environment == Strings.ANDROID:
            assert whats_new_page.exit_features() == Globals.VIEW_MY_COURSES_ACTIVITY_NAME

        elif InputData.target_environment == Strings.IOS:
            assert whats_new_page.exit_features().text == Strings.MAIN_DASHBOARD_SCREEN_TITLE

        print('-- Ending ', TestWhatsNew.__name__, 'Test Case')