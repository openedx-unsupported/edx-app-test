# coding=utf-8
"""
    Course Dashboard Test Module
"""

from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_course_subsection import AndroidCourseSubsection
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_account import AndroidAccunts
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidAccounts:
    """
    User Account screen's Test Case

    """

    def test_start_main_dashboard_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully after successful login
        """

        global_contents = Globals(setup_logging)
        setup_logging.info('-- Starting {} Test Case'.format(TestAndroidAccounts.__name__))
        if login:
            setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))

        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        android_whats_new_page.navigate_features()
        assert android_whats_new_page.navigate_features().text == strings.WHATS_NEW_DONE
        assert android_whats_new_page.exit_features() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that Account screen will show following contents:
                Back icon
                Specific "Account" as Title
                Profile
                Settings
                Submit_feedback
                Logout
        """

        global_contents = Globals(setup_logging)
        android_accounts_screen = AndroidAccunts(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        assert android_main_dashboard_page.load_account_screen() == global_contents.ACCOUNT_ACTIVITY_NAME

        assert android_accounts_screen.get_navigation_icon().get_attribute('content-desc') \
            == strings.ACCOUNT_SCREEN_NAVIGATION_ICON

        assert android_accounts_screen.get_profile_row().text == strings.PROFILE_SCREEN_TITLE

        assert android_accounts_screen.get_settings_row().text == strings.ACCOUNT_SETTINGS

        assert android_accounts_screen.get_submit_feedback_row().text == strings.ACCOUNT_SUBMIT_FEEDBACK

        assert android_accounts_screen.get_logout_row().text == strings.ACCOUNT_LOGOUT

    def test_load_contents_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify on tapping "Back icon" will load Main dashboard screen
            Verify on tapping "Profile" will load Profile
            Verify on tapping "Settings" will load Settings screen
            Verify on tapping "Logout" will logout user
        """

        global_contents = Globals(setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_accounts_screen = AndroidAccunts(set_capabilities, setup_logging)

        android_accounts_screen.get_navigation_icon().click()
        assert android_accounts_screen.on_screen() == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME

        assert android_main_dashboard_page.load_account_screen() == global_contents.ACCOUNT_ACTIVITY_NAME
        assert android_accounts_screen.load_profile_activity() == global_contents.PROFILE_ACTIVITY_NAME
        set_capabilities.back()
        assert android_accounts_screen.load_settings_activity() == global_contents.SETTINGS_ACTIVITY_NAME
        set_capabilities.back()
        assert android_main_dashboard_page.log_out() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
