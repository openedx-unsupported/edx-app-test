"""
   Module covers iOS screens' elements
"""
all_editfields = 'XCUIElementTypeTextField'
all_buttons = 'XCUIElementTypeButton'
all_textviews = 'XCUIElementTypeStaticText'

# NEW LOGISTRATION SCREEN
new_logistration_logo = 'StartUpViewController:logo-image-view'
new_logistration_discover_courses_button = 'StartUpViewController:discover-button'
new_logistration_sign_in_button = 'StartUpViewController:sign-in-button'
new_logistration_register_button = 'StartUpViewController:register-button'
new_logistration_explore_button = 'StartUpViewController:explore-button'
old_logistration__signup_button = 'Sign up and start learning'

# LOGIN SCREEN
login_title_textview = 'Sign In'
login_close_button = 'LoginViewController:close-bar-button-item'
login_edx_logo = 'LoginViewController:logo-image-view'
login_user_name_editfield = 'LoginViewController:email-text-field'
login_password_editfield = 'LoginViewController:password-text-field'
login_forget_password_textview = 'LoginViewController:trouble-logging-button'
login_signin_button = 'LoginViewController:login-button'
login_signin_divider_textview = 'LoginViewController:sign-in-label'
login_facebook_textview = 'ExternalAuthOptionsView:facebook-button'
login_google_textview = 'ExternalAuthOptionsView:google-button'
login_agree_textview = 'LoginViewController:redirect-label'
login_terms_textview = 'LoginViewController:open-eula-button'

# WHATS NEW SCREEN
whats_new_title_textview = 'WhatsNewViewController:header-label'
whats_new_close_button = 'WhatsNewViewController:close-button'
whats_new_main_image = 'WhatsNewContentController:screen-image-view'
whats_new_feature_title_textview = 'WhatsNewContentController:title-label'
whats_new_feature_details_textview = 'WhatsNewContentController:message-label'
whats_new_done_button ='WhatsNewViewController:done-button'

# MY DASHBOARD SCREEN
main_dashboard_title_textview = 'Courses'
# <XCUIElementTypeButton type="XCUIElementTypeButton" name="navigation-bar-button"
#  label="Navigation Menu" enabled="true" visible="true" x="5" y="26" width="38"
# height="30"/>
main_dashboard_navigation_icon = 'XCUIElementTypeButton'
main_dashboard_drawer_account_textview = 'ACCOUNT'

# MY ACCOUNT SCREEN
account_logout_option = 'Logout'

# REGISTER SCREEN
register_title_textview = 'Register'
register_with_textview = 'RegistrationViewController:register-with-label'
register_close_button = 'RegistrationViewController:close-button'
register_create_my_account_button = 'RegistrationViewController:register-button'

# DISCOVERY SCREEN
discovery_close_button = 'Cancel'
discover_courses_title_textview = 'Discover'
