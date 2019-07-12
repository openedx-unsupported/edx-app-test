# coding=utf-8

"""
    edX App Test Module
"""

from tests.common import strings
from tests.common.globals import Globals
from tests.android.pages.android_new_landing import AndroidNewLanding
from tests.android.pages.android_login import AndroidLogin
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.android.pages.android_course_discovery import AndroidCourseDiscovery
from tests.android.pages.android_register import AndroidRegister

class TestAndroidedXApp(object):
    """
    New Landing screen's Test Case
    """

    def test_start_new_landing_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify New Landing screen is loaded successfully
        """

        setup_logging.info('-- Starting New Landing Test Case --')
        global_contents = Globals(setup_logging)
        android_new_landing = AndroidNewLanding(set_capabilities, setup_logging)

        assert android_new_landing.on_screen() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME

    def test_new_landing_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Verify following contents are visible on screen,
            "edX logo", "Message" text-field, "Search Courses" edit-field, "Register" button, "Sign In" button
        Verify all contents have their default values
        """

        android_new_landing = AndroidNewLanding(set_capabilities, setup_logging)
        
        assert android_new_landing.get_edx_logo().text == strings.BLANK_FIELD
        android_new_landing.get_welcome_message()
        # assert android_new_landing.get_welcome_message().text == strings.NEW_LANDING_MESSAGE_ANDROID
        assert android_new_landing.get_search_course_icon().text == strings.NEW_LANDING_SEARCH_COURSES
        assert android_new_landing.get_search_course_editfield().text == strings.NEW_LANDING_SEARCH_COURSES
        assert android_new_landing.get_signin_button().text == strings.NEW_LANDING_LOG_IN
        assert android_new_landing.get_register_button().text == strings.NEW_LANDING_CREATE_YOUR_ACCOUNT

    def test_new_landing_search_courses_smoke(self, set_capabilities, setup_logging):
        """
        Verifies that user can search courses, and back to New Landing screen
        """

        global_contents = Globals(setup_logging)
        android_new_landing = AndroidNewLanding(set_capabilities, setup_logging)

        search_courses_screen = android_new_landing.search_courses(global_contents.new_landing_search_courses)
        assert search_courses_screen == global_contents.WITHOUT_LOGIN_DISCOVERY_ACTIVITY_NAME
        set_capabilities.back()
        assert android_new_landing.on_screen() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME

    def test_new_landing_back_and_forth_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify tapping "Login" will load "Sign In" screen
                Verify tapping back/cross icon from 'Sign In' screen navigate user
                    back to 'New Landing' screen
                Verify tapping "Create your Account" loads "Register" screen
                Verify tapping back/cross icon from "Register" screen
                    navigate user back to 'New Landing' screen
        """

        android_new_landing = AndroidNewLanding(set_capabilities, setup_logging)

        assert android_new_landing.back_and_forth_login()
        assert android_new_landing.back_and_forth_register()

        setup_logging.info('-- Ending New landing Test Case --')

    def test_start_login_smoke(self, set_capabilities, setup_logging):
        """
        Scenario:
            Verify Login screen is loaded successfully
        """

        setup_logging.info('-- Starting Login Test Case --')

        android_new_landing_page = AndroidNewLanding(set_capabilities, setup_logging)
        android_login_page = AndroidLogin(set_capabilities, setup_logging)

        assert android_new_landing_page.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME
        assert android_login_page.on_screen() == Globals.LOGIN_ACTIVITY_NAME

        setup_logging.info('Login screen successfully loaded')

    def test_login_ui_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify following contents are visible on screen 
            "Back icon", "Sign In" Title, "User name or e-mail address" label, User Name edit-field
            Password edit-field, "Forgot your password?" option, "Sign In" button,
            "Or sing in with" label, "Facebook" button, "Google" button,
            "By signing in to this app, you agree to the" label,
            "edX Terms of Service and Honor Code" option
        Verify all screen contents have their default values
        """

        android_login_page = AndroidLogin(set_capabilities, setup_logging)

        assert android_login_page.get_title_textview().text == strings.LOGIN
        assert android_login_page.get_username_editfield().text == strings.LOGIN_USER_NAME_WATER_MARK_ANDROID
        assert android_login_page.get_password_editfield().text == strings.LOGIN_PASSWORD_WATER_MARK
        assert android_login_page.get_forgot_password_textview().text == strings.LOGIN_FORGOT_PASSWORD
        assert android_login_page.get_sign_in_button().text == strings.LOGIN
        login_with_email_divider = android_login_page.get_login_with_email_divider_textview().text
        assert login_with_email_divider == strings.LOGIN_ANDROID_WITH_EMAIL_DIVIDER
        assert android_login_page.get_facebook_textview().text == strings.FACEBOOK_OPTION
        assert android_login_page.get_google_textview().text == strings.GOOGLE_OPTION
        assert android_login_page.get_agreement_textview().text == strings.LOGIN_ANDROID_AGREEMENT

    def test_login_back_and_forth_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify tapping back icon from 'Sign In' screen navigate user
                    back to 'New Landing' screen.
                Verify that user is able to load EULA screen and get back to Login Screen
                Verify that user is able to load Terms screen and get back to Login Screen
                Verify that user is able to load Privacy screen and get back to Login Screen
        """

        android_login_page = AndroidLogin(set_capabilities, setup_logging)

        assert android_login_page.back_and_forth_login()
        
    def test_login_forgot_password_alert(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify tapping 'Forgot your password?' will  load 'Reset Password' alert
                Verify following contents are visible on 'Reset Password' alert, 
                Alert Title, Alert Message, Email edit field, Cancel & OK buttons
                Verify tapping 'Cancel' will close 'Reset Password' alert
        """

        android_login_page = AndroidLogin(set_capabilities, setup_logging)
        android_login_page.get_forgot_password_alert()

        assert android_login_page.get_forgot_password_alert_title().text == strings.LOGIN_RESET_PASSWORD_ALERT_TITLE
        android_login_page.get_forgot_password_alert_msg()
        # assert android_login_page.get_forgot_password_alert_msg().text == strings.LOGIN_RESET_PASSWORD_ALERT_MSG_ANDROID
        assert android_login_page.get_forgot_password_alert_ok_button().text == strings.LOGIN_RESET_PASSWORD_ALERT_OK
        forgot_password_alert_cancel_button = android_login_page.get_forgot_password_alert_cancel_button().text
        assert forgot_password_alert_cancel_button == strings.LOGIN_RESET_PASSWORD_ALERT_CANCEL_ANDROID
        assert android_login_page.close_forgot_password_alert()

    def test_login_smoke(self, set_capabilities, setup_logging):
        """
        Verifies that user can login with valid Username and Password
        """

        global_contents = Globals(setup_logging)
        android_login_page = AndroidLogin(set_capabilities, setup_logging)
        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        assert android_login_page.login(
            global_contents.login_wrong_user_name,
            global_contents.login_wrong_password) is False

        assert android_login_page.login(
            global_contents.login_user_name,
            global_contents.login_password,
            global_contents.is_first_time
        ) == Globals.WHATS_NEW_ACTIVITY_NAME
        setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))        
        

        setup_logging.info('-- Ending Login Test Case --')    

    def test_start_whats_new_smoke(self, setup_logging, set_capabilities):
        """
        Scenarios:
            Verify Whats New screen is loaded successfully
        """
        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        setup_logging.info('-- Starting Whats New Test Case')

        assert android_whats_new_page.on_screen() == Globals.WHATS_NEW_ACTIVITY_NAME

    def test_whats_new_validate_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify following contents are visible on screen 
                    "Screen Title", "Cross Icon", "Main Feature Image",
                     "Feature Title", "Feature Details", "Done"
                Verify all screen contents have their default values
        """

        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)

        assert android_whats_new_page.get_title_textview()
        assert android_whats_new_page.get_cross_icon()
        assert android_whats_new_page.get_main_image().text == strings.BLANK_FIELD
        assert android_whats_new_page.get_feature_title_textview()
        assert android_whats_new_page.get_feature_details()

    def test_whats_new_navigate_features_smoke(self, set_capabilities, setup_logging):
        """
        Verifies that user can navigate between features
        """

        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        
        android_whats_new_page.navigate_features()
        assert android_whats_new_page.navigate_features().text == strings.WHATS_NEW_DONE
        assert android_whats_new_page.exit_features() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME

    def test_start_main_dashboard_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully
        """

        setup_logging.info('-- Starting Main Dashboard Test Case --')
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert android_main_dashboard_page.on_screen() == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME

    def test_main_dashboard_ui_elements(self, set_capabilities, setup_logging):
        """
         Scenarios:
                Verify following contents are visible on screen, 
                    Logged in user's avatar, Screen Title, Account Icon
                    Courses Tab, Discovery Tab
                Verify that Courses tab will be selected by default
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        assert android_main_dashboard_page.get_profile_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_title_textview().text == strings.MAIN_DASHBOARD_SCREEN_TITLE
        assert android_main_dashboard_page.get_menu_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert android_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB

    def test_main_dashboard_load_contents_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify on tapping Courses will load Courses contents in its tab
                Verify on tapping Discovery will load Discovery contents in its tab
                Verify tapping user's avatar will load User Profile screen
                Verify tapping back/cancel icon from User Profile screen should get back to Main Dashboard screen
                Verify tapping Account Icon will load Account Screen
                Verify tapping back/cancel icon from Account Screen should get back to Main Dashboard screen
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert android_main_dashboard_page.get_programs_tab().text == strings.MAIN_DASHBOARD_PROGRAMS_TAB
        assert android_main_dashboard_page.load_programs_tab()
        assert android_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB
        assert android_main_dashboard_page.load_discovery_tab()
        assert android_main_dashboard_page.get_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert android_main_dashboard_page.load_courses_tab()
        assert android_main_dashboard_page.load_profile_screen() == global_contents.PROFILE_ACTIVITY_NAME
        set_capabilities.back()

        assert android_main_dashboard_page.load_account_screen() == global_contents.ACCOUNT_ACTIVITY_NAME
        set_capabilities.back()

    def test_main_dashboard_logout_smoke(self, set_capabilities, setup_logging):
        """
        Scenario:
                Verify that user can log out successfully, and back on Login screen
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert android_main_dashboard_page.load_account_screen() == global_contents.ACCOUNT_ACTIVITY_NAME
        assert android_main_dashboard_page.log_out() == global_contents.NEW_LOGISTRATION_ACTIVITY_NAME
        setup_logging.info('{} is successfully logged out'.format(global_contents.login_user_name))

    def test_main_dashboard_landscape_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Landscape support is added for Main Dashboard screen with following cases,
                Change device orientation to Landscape mode
                Verify following contents are visible on screen, 
                    Logged in user's avatar, Screen Title, Account Icon
                    Courses Tab, Discovery Tab
                Verify that Courses tab will be selected by default
                Verify on tapping Courses will load Courses contents in its tab
                Verify on tapping Discovery will load Discovery contents in its tab
                Verify tapping user's avatar will load User Profile screen
                Verify tapping back/cancel icon from User Profile screen should get back to Main Dashboard screen
                Verify tapping Account Icon will load Account Screen
                Verify tapping back/cancel icon from Account Screen should get back to Main Dashboard screen
                Verify that user can log out successfully, and back on Login screen
        """

        global_contents = Globals(setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_new_landing_page = AndroidNewLanding(set_capabilities, setup_logging)
        android_login_page = AndroidLogin(set_capabilities, setup_logging)

        assert android_new_landing_page.on_screen() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME
        assert android_new_landing_page.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME
        login_output = android_login_page.login(
            global_contents.login_user_name,
            global_contents.login_password, False)
        setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))
        assert login_output == Globals.MAIN_DASHBOARD_ACTIVITY_NAME

        global_contents.turn_orientation(set_capabilities, global_contents.LANDSCAPE_ORIENTATION)

        assert android_main_dashboard_page.get_profile_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_title_textview().text == strings.MAIN_DASHBOARD_SCREEN_TITLE
        assert android_main_dashboard_page.get_menu_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert android_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB
        assert android_main_dashboard_page.get_programs_tab().text == strings.MAIN_DASHBOARD_PROGRAMS_TAB
        assert android_main_dashboard_page.load_discovery_tab()
        assert android_main_dashboard_page.load_programs_tab()
        assert android_main_dashboard_page.load_courses_tab()
        assert android_main_dashboard_page.load_profile_screen() == global_contents.PROFILE_ACTIVITY_NAME
        set_capabilities.back()
        assert android_main_dashboard_page.load_account_screen() == global_contents.ACCOUNT_ACTIVITY_NAME
        set_capabilities.back()
        global_contents.turn_orientation(set_capabilities, global_contents.PORTRAIT_ORIENTATION)

        setup_logging.info('-- Ending Main Dashboard Test Case --')

    def test_start_my_courses_list_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that from Main Dashboard tapping Courses tab will load My Courses
                list(of specific logged in user) in its tab
        """

        setup_logging.info('-- Starting My Courses List Test Case --')
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        
        assert android_main_dashboard_page.get_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert android_main_dashboard_page.load_courses_tab()

    def test_my_courses_list_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that from Main Dashboard  tapping Courses tab will load My Courses
                contents(of specific logged in user) in its tab
            Verify that Courses tab/screen will show following header contents,
            Header Contents
                Profile icon
                "Courses" title
                Account Icon
            Courses Tab
            Discovery Tab
            Verify that My Courses(enrolled) List with followings in each course,
                Course image
                Course Name
                Course Start/End date
            "Looking for a new challenge?" label
            "Find a Course" button

        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert android_main_dashboard_page.get_profile_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_title_textview().text == strings.MAIN_DASHBOARD_SCREEN_TITLE
        assert android_main_dashboard_page.get_menu_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert android_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB

        if android_my_courses_list_page.get_my_courses_list():
            assert android_my_courses_list_page.get_my_courses_list_row()
            android_my_courses_list_page.get_contents_from_list()
            global_contents.swipe_screen(set_capabilities)
        else:
            setup_logging.info('No course enrolled by this user.')

        find_courses_message = android_my_courses_list_page.get_find_courses_message().text
        assert find_courses_message == strings.MY_COURSES_LIST_FIND_COURSES_MESSAGE
        find_courses_button = android_my_courses_list_page.get_find_course_button().text
        assert find_courses_button == strings.MY_COURSES_LIST_FIND_COURSES_BUTTON_ANDROID

    def test_my_courses_list_load_course_details_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that tapping any course should load specific Course Dashboard screen
            Verity that from Course Dashboard tapping back should load My Courses List screen
            Verify that user should be able to scroll courses
            Verify on tapping "Find a Course" button will load Discovery screen
            Verity that from Course Dashboard tapping back should load My Courses List screen

        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        if android_my_courses_list_page.get_my_courses_list_row():
            course_dashboard_screen = android_my_courses_list_page.load_course_details_screen()
            assert course_dashboard_screen == global_contents.COURSE_DASHBOARD_ACTIVITY_NAME
            set_capabilities.back()
            assert android_main_dashboard_page.on_screen() == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME
            global_contents.swipe_screen(set_capabilities)

        else: 
            setup_logging.info('No course enrolled by this user.')

        course_discovery_screen = android_my_courses_list_page.load_discovery_screen()
        assert course_discovery_screen == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME
        assert android_main_dashboard_page.get_discovery_tab().is_selected()
        android_main_dashboard_page.load_courses_tab()
        assert android_main_dashboard_page.get_courses_tab().is_selected()

    def test_my_courses_list_landscape_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Change device orientation to Landscape mode
            Verify that from Main Dashboard tapping Courses tab will load My Courses
            list(of specific logged in user) in its tab
            Verify that from Main Dashboard  tapping Courses tab will load My Courses
            contents(of specific logged in user) in its tab
            Verify that Courses tab/screen will show following header contents,
            Header Contents
                Profile icon
                "Courses" title
                Account Icon
                Courses Tab
                Discovery Tab
            Verify that My Courses(enrolled) List with followings in each course,
                Course image
                Course Name
                Course Start/End date
            "Looking for a new challenge?" label
            "Find a Course" button
            Verify that tapping any course should load specific Course Dashboard screen
            Verity that from Course Dashboard tapping back should load My Courses List screen
            Verify that user should be able to scroll courses
            Verify on tapping "Find a Course" button will load Discovery screen
            Verity that from Course Dashboard tapping back should load My Courses List screen
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        global_contents.turn_orientation(set_capabilities, global_contents.LANDSCAPE_ORIENTATION)

        assert android_main_dashboard_page.get_profile_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_title_textview().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert android_main_dashboard_page.get_menu_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_courses_tab().text == strings.MAIN_DASHBOARD_COURSES_TAB
        assert android_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB

        if android_my_courses_list_page.get_my_courses_list():
            assert android_my_courses_list_page.get_my_courses_list_row()
            android_my_courses_list_page.get_contents_from_list()
            course_dashboard_screen = android_my_courses_list_page.load_course_details_screen()
            assert course_dashboard_screen == global_contents.COURSE_DASHBOARD_ACTIVITY_NAME
            set_capabilities.back()
            assert android_main_dashboard_page.on_screen() == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME
            global_contents.swipe_screen(set_capabilities)

        else:
            setup_logging.info('No course enrolled by this user.')

        find_courses_message = android_my_courses_list_page.get_find_courses_message().text
        assert find_courses_message == strings.MY_COURSES_LIST_FIND_COURSES_MESSAGE
        find_courses_button = android_my_courses_list_page.get_find_course_button().text
        assert find_courses_button == strings.MY_COURSES_LIST_FIND_COURSES_BUTTON_ANDROID

        course_discovery_screen = android_my_courses_list_page.load_discovery_screen()
        assert course_discovery_screen == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME
        assert android_main_dashboard_page.get_discovery_tab().is_selected()
        global_contents.turn_orientation(set_capabilities, global_contents.PORTRAIT_ORIENTATION)
    
        setup_logging.info('-- Ending My Courses Test Case --')

    def test_course_discovery_screen(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that from Main Dashboard tapping on Discovery tab will load Discovery
            contents in its tab
        """

        setup_logging.info('-- Starting Course Disovery Test Case --')
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
    
        assert android_main_dashboard_page.get_discovery_tab().text == strings.MAIN_DASHBOARD_DISCOVERY_TAB
        assert android_main_dashboard_page.load_discovery_tab()

    def test_course_discovery_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify that Discovery tab will show following contents,
        Header contents,
            Profile icon, "Discovery" as screen Title,
            Discovery edit-field in place title(Android Only), Account Icon
        Three tabs
            Courses, Programs, Degrees
        "Browse By Subject" Section below, Subject Background Image, Subject Name
        "Viewing <total number of available results"
        Filter courses option
        """

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        android_course_discovery_page = AndroidCourseDiscovery(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert android_main_dashboard_page.get_profile_icon().text == strings.BLANK_FIELD
        assert android_main_dashboard_page.get_title_textview().text == strings.COURSES_DISCOVERY_SCREEN_TITLE
        assert android_course_discovery_page.get_search_icon().text == strings.BLANK_FIELD
        search_editfield = android_course_discovery_page.load_search_editfield().text
        assert search_editfield == strings.COURSES_DISCOVERY_SEARCH_EDIT_FIELD
        assert android_main_dashboard_page.get_menu_icon().text == strings.BLANK_FIELD
        browse_by_subject_heading = android_course_discovery_page.get_browse_by_subject_heading().text
        assert browse_by_subject_heading == strings.COURSES_DISCOVERY_BROWSE_BY_SUBJECT_LABEL
        assert android_course_discovery_page.get_subject_name().text == strings.COURSES_DISCOVERY_SUBJECT_NAME
        assert android_course_discovery_page.get_subject_image().text == strings.BLANK_FIELD
        
        # Log out 
        assert android_main_dashboard_page.load_account_screen() == global_contents.ACCOUNT_ACTIVITY_NAME
        assert android_main_dashboard_page.log_out() == global_contents.DISCOVERY_LAUNCH_ACTIVITY_NAME
        setup_logging.info('{} is successfully logged out'.format(global_contents.login_user_name)) 
        setup_logging.info('-- Ending Course Disovery Test Case --')   
    
    def test_start_register_smoke(self, set_capabilities, setup_logging):
        """
        Scenario:
            Verify Register screen is loaded successfully
        """

        setup_logging.info('-- Starting Register Test Case --')

        android_new_landing_page = AndroidNewLanding(set_capabilities, setup_logging)
        android_register_page = AndroidRegister(set_capabilities, setup_logging)

        android_new_landing_page.load_register_screen()
        assert android_register_page.on_screen() == Globals.REGISTER_ACTIVITY_NAME

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:

        Verify following contents are visible on screen,
            "Register with" label, "Facebook" button
            "Google" button, "or register with email" label, Email edit-field,
            "This is what you will use to login" label below, Full Name edit-field,
            "The name will be used on any certificates that you earn" label below,
            Public User Name edit-field,
            "The name that will identify you in your courses. It cannot be changed later." label below,
            Password edit-field, "Your password must contain at least 8 characters, including 1 letter & 1 number.",
            "Country or Region of Residence" spinner,
            "The country or region where you live." label below, "Show optional fields" option below,
            "Create my account" button,
            "By creating an account you agree to the "edX Terms of Service and Honor Code" option
        Verify all contents/elements have default value
        Verify that user should be able to scroll screen to see all contents
        """

        android_register_page = AndroidRegister(set_capabilities, setup_logging)

        assert android_register_page.get_register_divider_textview().text == strings.REGISTER_SCREEN_REGISTER_WITH
        assert android_register_page.get_facebook_textview().text == strings.FACEBOOK_OPTION
        assert android_register_page.get_google_textview().text == strings.GOOGLE_OPTION

        email_divider = android_register_page.get_register_with_email_divider_textview()
        assert email_divider.text == strings.REGISTER_SCREEN_REGISTER_WITH
        assert android_register_page.get_email_editfield().text == strings.REGISTER_EMAIL_LABEL
        assert android_register_page.get_email_instructions_textview().text == strings.REGISTER_EMAIL_INSTRUCTIONS
        assert android_register_page.get_full_name_editfield().text == strings.REGISTER_FULL_NAME_LABEL

        full_name_instructions = android_register_page.get_full_name_instructions_textview()
        assert full_name_instructions.text == strings.REGISTER_FULL_NAME_INSTRUCTIONS
        assert android_register_page.get_user_name_editfield().text == strings.REGISTER_USER_NAME_LABEL

        user_name_instructions = android_register_page.get_user_name_instructions_textview()
        assert user_name_instructions.text == strings.REGISTER_USER_NAME_INSTRUCTIONS
        assert android_register_page.get_password_editfield().text == strings.REGISTER_PASSWORD_LABEL

        password_instructions = android_register_page.get_password_instructions_textview()
        assert password_instructions.text == strings.REGISTER_PASSWORD_INSTRUCTIONS
        assert android_register_page.get_country_spinner().text == strings.BLANK_FIELD

        country_spinner_instructions = android_register_page.get_country_spinner_instructions_textview()
        assert country_spinner_instructions.text == strings.REGISTER_COUNTRY_INSTRUCTIONS

        show_optional_fields = android_register_page.get_show_optional_fields_textview()
        assert show_optional_fields.text == strings.REGISTER_SHOW_OPTIONAL_FIELDS_OPTION
        assert android_register_page.get_create_my_account_textview().text == strings.REGISTER_CREATE_MY_ACCOUNT
        assert android_register_page.get_agreement_textview().text == strings.REGISTER_AGREEMENT_ANDROID

    def test_show_hide_optional_fields_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:

        Verify that tapping "Show optional fields" will turn to "Hide optional fields" and load following optional
        contents below,
            "Gender" spinner, "Year of birth" spinner, "Highest level of education completed" spinner,
            "Tell us why you're interested in edX" label with edit-field below,
        Verify that tapping "Hide optional fields" will turn to "Show optional fields" and all optional
            contents will be hidden
        Verify all optional contents/elements have default values
        """

        android_register_page = AndroidRegister(set_capabilities, setup_logging)

        assert android_register_page.show_hide_optional_fields().text == strings.REGISTER_HIDE_OPTIONAL_FIELDS_OPTION

        assert android_register_page.get_gender_spinner().text == strings.BLANK_FIELD
        assert android_register_page.get_year_of_birth_spinner().text == strings.BLANK_FIELD
        assert android_register_page.get_eduction_spinner().text == strings.BLANK_FIELD
        assert android_register_page.get_why_interested_editfield()

        assert android_register_page.show_hide_optional_fields().text == strings.REGISTER_SHOW_OPTIONAL_FIELDS_OPTION

    def test_back_and_forth_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify tapping "Back" icon will load New Logistration/New Landing screen
                    back to 'New Logistration' screen.
                Verify tapping "edX Terms of Service and Honor Code" loads "End User License Agreement" screen
                Verify tapping back icon from "End User License Agreement" screen
                    navigate user back to 'Register' screen.
                Verify that user is able to load EULA screen and get back to Register Screen
                Verify that user is able to load Terms screen and get back to Register Screen
                Verify that user is able to load Privacy screen and get back to Register Screen
        """

        android_register_page = AndroidRegister(set_capabilities, setup_logging)

        assert android_register_page.back_and_forth_register()
        # android_register_page.load_eula_screen()
        # android_register_page.load_terms_screen()
        # android_register_page.load_privacy_screen()

    def test_required_and_optional_fields_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:

        Verify that following input types are required,
            Email editfield, Full Name editfield, Public, User Name, editfield, Password editfield,
            "Country or Region of Residence" spinner
        Verify that following input types are optional,
            "Gender" spinner, "Year of birth" spinner, "Highest level of education completed" spinner,
            "Tell us why you're interested in edX" label with edit - field below
        """

        android_register_page = AndroidRegister(set_capabilities, setup_logging)
        assert android_register_page.validate_required_optional_fields()
        assert android_register_page.get_email_validation_textview().text == strings.REGISTER_EMAIL_BLANK_ERROR
        assert android_register_page.get_full_name_validation_textview().text == strings.REGISTER_FULL_NAME_BLANK_ERROR
        assert android_register_page.get_username_validation_textview().text == strings.REGISTER_USER_NAME_BLANK_ERROR
        assert android_register_page.get_password_validation_textview().text == strings.REGISTER_PASSWORD_BLANK_ERROR
        assert android_register_page.get_country_validation_textview().text == strings.REGISTER_COUNTRY_BLANK_ERROR

    def test_register_smoke(self, set_capabilities, setup_logging):
        """
        Verify that tapping "Create your account" button after filling all required input(valid) types,
            will validate all inputs and load "Whats new feature screen" with specific user logged in
        Verify that user should be able to log out and re-login with new created account credentials
        """

        android_register_page = AndroidRegister(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        user_name = global_contents.generate_random_credentials(4)
        email = user_name + '@example.com'
        first_name = global_contents.generate_random_credentials(4)
        last_name = global_contents.generate_random_credentials(4)
        full_name = (first_name + ' ' + last_name)
        password = global_contents.generate_random_credentials(8)
        setup_logging.info('Email - {},  Username - {}, Full Name - {}, Password -{}'.format(
            email,
            user_name,
            full_name,
            password
        ))

        register_output = android_register_page.register(email,
                                                         full_name,
                                                         user_name,
                                                         password,
                                                         global_contents.country
                                                         )

        global_contents.wait_for_android_activity_to_load(
            set_capabilities,
            global_contents.REGISTER_ACTIVITY_NAME
        )

        assert register_output == Globals.MAIN_DASHBOARD_ACTIVITY_NAME

        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)
        assert android_main_dashboard_page.load_account_screen() == global_contents.ACCOUNT_ACTIVITY_NAME
        assert android_main_dashboard_page.get_logout_account_option().text == strings.ACCOUNT_LOGOUT
        assert android_main_dashboard_page.log_out() == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME

        android_new_landing_page = AndroidNewLanding(set_capabilities, setup_logging)
        assert android_new_landing_page.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME

        android_login_page = AndroidLogin(set_capabilities, setup_logging)

        login_output = android_login_page.login(
            user_name,
            password,
            False)

        assert login_output == Globals.MAIN_DASHBOARD_ACTIVITY_NAME
        setup_logging.info('{} is successfully logged in'.format(user_name))

        setup_logging.info('-- Ending Register Test Case --')
