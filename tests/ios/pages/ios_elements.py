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
main_dashboard_navigation_icon = 'EnrolledTabBarViewController:menu-button'
main_dashboard_profile_icon = 'EnrolledTabBarViewController:profile-button'
main_dashboard_courses_tab = 'Courses'
main_dashboard_discovery_tab = 'Discovery'
profile_close_button = 'UserProfileViewController:close-button'
account_view_close_button = 'AccountViewController:close-button'

# MY COURSES LIST SCREEN
my_courses_list = 'courses-table-view'  # XCUIElementTypeTable
my_courses_list_course_row = 'CourseCardCell:course-card-view'
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
account_signout = 'SignOutVersionCell:signout-button'

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
select_country = 'Afghanistan'

# DISCOVERY SCREEN
discovery_close_button = 'Cancel'   # need id for this field
discover_courses_title_textview = 'Discover'   # need id for this field

# NEW LANDING SCREEN
new_landing_logo = 'StartUpViewController:logo-image-view'
new_landing_welcome_message = 'StartUpViewController:message-label'
new_landing_search_courses_editfield = 'StartUpViewController:search-textfield'
new_landing_log_in_button = 'StartUpViewController:sign-in-button'
new_landing_register_button = 'StartUpViewController:register-button'


# COURSE DASHBOARD SCREEN
course_dahsboard_share_icon = 'CourseDashboardViewController:course-share-item'
course_dashboard_course_image = 'CourseCardView:cover-image'
course_dashboard_course_title = 'CourseCardView:title-label'
course_dashboard_course_date = 'CourseCardView:date-label'
course_dashboard_course_section_header = 'CourseOutlineHeaderCell:header-label'
course_dashboard_course_item_title = 'CourseOutlineItemView:title-label'
course_dashboard_course_item_download = 'CourseSectionTableViewCell:download-view'
course_dashboard_courses_tab = 'CourseDashboardViewController:tabbar-item-Course'
course_dashboard_videos_tab = 'CourseDashboardViewController:tabbar-item-Videos'
course_dashboard_discussion_tab = 'CourseDashboardViewController:tabbar-item-Discussion'
course_dashboard_dates_tab = 'CourseDashboardViewController:tabbar-item-Dates'
course_dashboard_resources_tab = 'CourseDashboardViewController:tabbar-item-Resources'
course_dashboard_resources_list_title = 'AdditionalTableViewCell:title-label'
course_dashboard_resources_list_name = 'AdditionalTableViewCell:detail-label'
course_dashboard_resume_row = 'CourseOutlineHeaderView:view-button'

# COURSE SUBSECTION SCREEN
course_subsection_download_icon = 'CourseVideoTableViewCell:download-view'
course_subsection_html_cell = 'CourseHTMLTableViewCell:view'
course_subsection_video_cell = 'CourseVideoTableViewCell:view'

# COURSE VIDEOS DASHBOARD
video_dashboard_download_switch = 'CourseVideosHeader:toggle-switch'
video_dashboard_download_header = 'CourseVideosHeader:show-downloads-button'

# COURSE_DISCUSSIONS_DASHBOARD
discussions_dashboard_search_post = 'XCUIElementTypeSearchField'
discussions_topic_title_cell = 'DiscussionTopicCell:title-label'

# COURSE VIDEO SUBSECTION SCREEN
video_subsection_navigation_icon = 'Videos'

# PROFILE SCREEN
personal_information_profile_cell = 'PersonalInformationCell:chevron-image-view'
profile_screen_edit_profile_button = 'UserProfileViewController:edit-button'
profile_screen_username_label = 'UserProfileView:username-label'
profile_screen_language_label = 'UserProfileView:language-label'
profile_screen_country_label = 'UserProfileView:country-label'
profile_screen_bio_text = 'UserProfileView:bio-text-view'
profile_screen_limited_view_message = 'UserProfileView:message-label'
profile_screen_edit_profile_back_icon = 'UserProfileEditViewController:back-item'

# PROFILE OPTIONS SCREEN
profile_options_close_button = 'ProfileOptionsViewController:close-button'
profile_options_wifi_switch = 'VideoSettingCell:wifi-switch'
profile_options_video_settings_option_label = 'VideoSettingCell:option-label'
profile_options_videos_setting_cell = 'ProfileOptionsViewController:video-setting-cell'
profile_options_video_settings_description_label = 'VideoSettingCell:video-setting-description-label'
profile_options_video_quality_description_label = 'VideoSettingCell:video-quality-description-label'
profile_options_video_quality_subtitle_label = 'VideoSettingCell:video-quality-subtitle-label'
profile_options_wifi_cell = 'ProfileOptionsViewController:wifi-cell'
profile_options_personal_information_option_label = 'PersonalInformationCell:option-label'
profile_options_personal_information_email_label = 'PersonalInformationCell:email-label'
profile_options_personal_information_username_label = 'PersonalInformationCell:username-label'
profile_options_personal_information_profile_view = 'PersonalInformationCell:profile-view'
profile_options_personal_information_image_view = 'PersonalInformationCell:chevron-image-view'
profile_options_help_cell = 'ProfileOptionsViewController:help-cell'
profile_options_help_cell_feedback_label = 'HelpCell:feedback-label'
profile_options_help_cell_subtitle_label = 'HelpCell:feedback-subtitle-label'
profile_options_help_cell_support_label = 'HelpCell:support-label'
profile_options_help_cell_support_subtitle_label = 'HelpCell:support-subtitle-label'
profile_options_help_cell_option_label = 'HelpCell:option-label'
profile_options_email_feedback_button = 'HelpCell:email-feedback-button'
profile_options_view_faq_button = 'HelpCell:view-faq-button'
profile_options_signout_version_cell = 'ProfileOptionsViewController:signout-version-cell'
profile_options_signout_button = 'SignOutVersionCell:signout-button'
profile_options_signout_version_label = 'SignOutVersionCell:version-label'
profile_options_delete_account_cell = 'ProfileOptionsViewController:delete-account-cell'
profile_options_delete_button = 'DeleteAccountCell:signout-button'
profile_options_delete_account_info_label = 'DeleteAccountCell:info-label'
delete_account_page_title = 'Delete your account'
cellular_download_popup_allow_button = 'allow'
cellular_download_popup_dont_allow_button = 'Don\'t allow'
video_quality_popup_back_icon = 'Profile'

# EDIT PROFILE SCREEN
edit_profile_screen_image = 'ProfileBanner:short-profile-image-view'
edit_profile_user_name = 'ProfileBanner:username-label'
edit_profile_change_photo = 'ProfileBanner:change-button'
edit_profile_subtitle_label = 'SegmentCell:title-label'
edit_profile_label = 'org.edx.mobile:id/label'
edit_profile_full_view = 'Full Profile'
edit_profile_limited_view = 'Limited Profile'
edit_profile_instructions = 'SegmentCell:description-label'
edit_profile_change_photo_option = 'org.edx.mobile:id/title'
edit_profile_change_location = 'Location:'
edit_profile_change_language = 'Spoken language:'
edit_profile_about_me = 'About me:'
profile_screen_back_icon = 'UserProfileEditViewController:back-item'
edit_profile_screen_back_icon = 'Edit profile'
edit_profile_choose_photo_option = 'Choose a photo'
edit_profile_remove_photo_option = 'Remove'
edit_profile_cancel_photo_option = 'Cancel'
edit_profile_location_title = 'Location'
edit_profile_language_title = 'Spoken language'
edit_profile_about_me_text = 'JSONFormBuilderTextEditorViewController:text-view'

# COURSE DISCOVERY
course_discovery_search_courses = 'Search courses'
course_discovery_browse_by_subject = 'PopularSubjectsViewController:title-label'
