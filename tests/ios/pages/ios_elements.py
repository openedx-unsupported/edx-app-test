# coding=utf-8
"""
   Module covers iOS screens' elements
"""
all_editfields = 'XCUIElementTypeTextField'
all_buttons = 'XCUIElementTypeButton'
all_textviews = 'XCUIElementTypeStaticText'
all_pickwheels = 'XCUIElementTypePickerWheel'
all_otherviews = 'XCUIElementTypeOther'

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
login_forgot_password_textview = 'LoginViewController:trouble-logging-button'
login_signin_button = 'LoginViewController:login-button'
login_signin_divider_textview = 'LoginViewController:sign-in-label'
login_facebook_textview = 'ExternalAuthOptionsView:facebook-button'
login_google_textview = 'ExternalAuthOptionsView:google-button'
login_agree_textview = 'LoginViewController:redirect-label'
login_agreement_textview = 'LoginViewController:agreement-text-view'
login_eula_textview = 'edX End User License Agreement'
login_terms_textview = 'edX Terms of Service and Honor Code'
login_privacy_textview = 'Privacy Policy'
login_agreement_close = 'OEXUserLicenseAgreementViewController:close-button'
# Accessing elements on visible contents until following ticket is processed
# [LEARNER-5086 iOS - Login Screen - Forgot Password Alert - unique ids are not assigned]
login_reset_password_alert_title = 'Reset Password'
login_reset_password_alert_msg = ('Enter the e-mail address for your account, and we\'ll send you '
                                  'instructions to reset your password.')
login_reset_password_alert_email_editfield = 'XCUIElementTypeTextField'
login_reset_password_alert_ok_button = 'OK'
login_reset_password_alert_cancel_button = 'Cancel'
# TERMS & CONDITIONS
login_terms_close_button = 'Close'
login_wrong_credential_alert_title = 'Sign-in Error'
login_wrong_credential_alert_msg = ('Please make sure that your username or e-mail address'
                                    ' and password are correct and try again.')
login_wrong_credential_alert_ok_button = 'OK'

# WHATS NEW SCREEN
whats_new_title_textview = 'WhatsNewViewController:header-label'
whats_new_close_button = 'WhatsNewViewController:close-button'
whats_new_main_image = 'WhatsNewContentController:screen-image-view'
whats_new_feature_title_textview = 'WhatsNewContentController:title-label'
whats_new_feature_details_textview = 'WhatsNewContentController:message-label'
whats_new_done_button = 'WhatsNewViewController:done-button'

# MY DASHBOARD SCREEN
main_dashboard_title_textview = 'Courses'
main_dashboard_navigation_icon = 'EnrolledTabBarViewController:account-button'
main_dashboard_profile_icon = 'Profile'  # Typo from dev side
main_dashboard_courses_tab = 'Courses'
main_dashboard_discovery_tab = 'Discovery'
profile_close_button = 'Close'

# MY COURSES LIST SCREEN
my_courses_list = 'courses-table-view'  # XCUIElementTypeTable
my_courses_list_course_row = 'XCUIElementTypeCell'
my_courses_list_course_image = ''
my_courses_list_course_name = 'XCUIElementTypeStaticText'
my_courses_list_course_details = 'XCUIElementTypeStaticText'
my_courses_list_find_courses_message = 'Looking for a new challenge?'
my_courses_list_find_course_button = 'FIND A COURSE'

# MY COURSE DETAILS SCREEN
course_details_last_accessed_textview = 'Last Accessed'

# COURSE DISCOVERY SCREEN
course_discovery_textview = 'PopularSubjectsViewController:title-label'

# MY ACCOUNT SCREEN
account_options = 'AccountViewController:title-label'

# REGISTER SCREEN
register_title_textview = 'Register'
register_with_textview = 'RegistrationViewController:register-with-label'
register_close_button = 'RegistrationViewController:close-button'
register_create_my_account_button = 'register'    # need id for this field
register_agreement_textview = 'RegistrationViewController:agreement-text-view'
register_divider_textview = 'RegistrationViewController:register-with-label'
register_google_textview = 'ExternalAuthOptionsView:google-button'
register_facebook_textview = 'ExternalAuthOptionsView:facebook-button'
register_with_email_divider_textview = 'RegistrationViewController:register-with-email-label'
register_email_label = 'RegistrationFormFieldView:email-text-input-label'
register_email_textfield = 'field-email'
register_email_instructions = 'RegistrationFormFieldView:email-instructions-label'
register_email_error = 'RegistrationFormFieldView:email-error-label'
register_full_name_label = 'RegistrationFormFieldView:name-text-input-label'
register_full_name_textfield = 'RegistrationFormFieldView:name-text-input-field'
register_full_name_instructions = 'RegistrationFormFieldView:name-instructions-label'
register_full_name_error = 'RegistrationFormFieldView:name-error-label'
register_user_name_label = 'RegistrationFormFieldView:username-text-input-label'
register_user_name_textfield = 'RegistrationFormFieldView:username-text-input-field'
register_user_name_instructions = 'RegistrationFormFieldView:username-instructions-label'
register_user_name_error = 'RegistrationFormFieldView:username-error-label'
register_password_label = 'RegistrationFormFieldView:password-text-input-label'
register_password_textfield = 'RegistrationFormFieldView:password-text-input-field'
register_password_instructions = 'RegistrationFormFieldView:password-instructions-label'
register_password_error = 'RegistrationFormFieldView:password-error-label'
register_country_label = 'RegistrationFormFieldView:country-text-input-label'
register_country_dropdown = 'field-country'  # 'RegistrationFieldSelectView:text-input-field'
register_country_instructions = 'RegistrationFormFieldView:country-instructions-label'
register_country_error = 'RegistrationFormFieldView:country-error-label'
register_show_optional_fields_textview = 'Show optional fields'  # need id for this field
register_hide_optional_fields_textview = 'Hide optional fields'  # need id for this field
register_gender_label = 'RegistrationFormFieldView:gender-text-input-label'
register_gender_dropdown = 'RegistrationFieldSelectView:text-input-field'
register_year_of_birth_label = 'RegistrationFormFieldView:year_of_birth-text-input-label'
register_year_of_birth__dropdown = 'RegistrationFieldSelectView:text-input-field'
register_education_label = 'RegistrationFormFieldView:level_of_education-text-input-label'
register_education_dropdown = 'RegistrationFieldSelectView:text-input-field'
register_goal_label = 'RegistrationFormFieldView:goals-text-input-label'
register_goal_textarea = 'RegistrationFormFieldView:goals-text-input-area'
register_all_dropdowns = 'RegistrationFieldSelectView:text-input-field'
register_eula_textview = 'edX End User License Agreement'   # need id for this field
register_terms_textview = 'edX Terms of Service and Honor Code'   # need id for this field
register_privacy_textview = 'Privacy Policy'   # need id for this field
register_agreement_close_button = 'OEXUserLicenseAgreementViewController:close-button'   # need id for this field
register_error_alert_title_textview = 'Registration Error'   # need id for this field
register_error_alert_textview = 'Update the highlighted fields and try again'   # need id for this field
register_error_alert_button = 'OK'    # need id for this field
register_country_list_picker = 'picker-field-country'  # XCUIElementTypePicker >
register_terms_button = 'Close'

# DISCOVERY SCREEN
discovery_close_button = 'Cancel'   # need id for this field
discover_courses_title_textview = 'Discover'   # need id for this field

# NEW LANDING SCREEN
new_landing_logo = 'StartUpViewController:logo-image-view'
new_landing_welcome_message = 'StartUpViewController:message-label'
new_landing_search_courses_editfield = 'StartUpViewController:search-textfield'
new_landing_log_in_button = 'StartUpViewController:sign-in-button'
new_landing_register_button = 'StartUpViewController:register-button'
