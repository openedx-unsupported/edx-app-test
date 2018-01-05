from time import sleep
from common.elements import Elements
from common.globals import Globals
from common.strings import Strings
from testdata.input_data import InputData


class Login:
    """
    Login screen
    """

    def __init__(self, driver):
        self.driver = driver
        self.global_contents = Globals()
        self.elements = Elements()

    def on_screen(self):
        """
        Load Login screen

        Returns:
            If Android - Login Activity Name
            If iOS - Login screen Title Name
        """

        if InputData.target_environment == Strings.ANDROID:
            print(self.driver.current_activity)
            return self.driver.current_activity

        elif InputData.target_environment == Strings.IOS:
            textview_screen_title = self.driver.find_element_by_id(self.elements.login_title_textview)

            return textview_screen_title

    def get_title_textview(self):
        """
        Get Screen Title

        Returns:
             Screen Title Element
        """

        if InputData.target_environment == Strings.ANDROID:
            all_textviews_on_screen = self.global_contents.get_all_text_views(self.driver)
            textview_screen_title = all_textviews_on_screen[0]
            return self.global_contents.validate_element(textview_screen_title, textview_screen_title.text,
                                                         Strings.LOGIN_SCREEN_TITLE, Strings.ERROR)
        elif InputData.target_environment == Strings.IOS:
            tv_screen_title = self.driver.find_element_by_id(self.elements.login_title_textview)
            return tv_screen_title

    def get_logo(self):
        """
        Get logo

        Returns:
             Logo Element
        """

        image_logo = self.driver.find_element_by_id(self.elements.login_edx_logo)
        return self.global_contents.validate_element(image_logo, image_logo.text, Strings.BLANK_FIELD, Strings.ERROR)

    def get_username_editfield(self):
        """
        Get Username

        Returns:
             Username Element
        """

        if InputData.target_environment == Strings.ANDROID:
            editfield_user_name = self.driver.find_element_by_id(self.elements.login_user_name_editfield)
            return self.global_contents.validate_element(editfield_user_name, editfield_user_name.text,
                                                         Strings.BLANK_FIELD, Strings.ERROR_LABEL_NOT_MATCHING)

        elif InputData.target_environment == Strings.IOS:
            editfield_user_name = self.driver.find_element_by_class_name(self.elements.login_user_name_editfield)
            return editfield_user_name

    def get_password_editfield(self):
        """
        Get Password

        Returns:
             Password Element
        """

        if InputData.target_environment == Strings.ANDROID:
            editfield_password = self.driver.find_element_by_id(self.elements.login_password_editfield)
            return self.global_contents.validate_element(editfield_password, editfield_password.text,
                                                         Strings.BLANK_FIELD, Strings.ERROR_LABEL_NOT_MATCHING)

        elif InputData.target_environment == Strings.IOS:
            editfield_password = self.driver.find_element_by_class_name(self.elements.login_password_editfield)
            return editfield_password

    def get_forget_password_textview(self):
        """
        Get Forget Password

        Returns:
             Forget Password Element
        """

        if InputData.target_environment == Strings.ANDROID:
            textview_forget_password = self.driver.find_element_by_id(self.elements.login_forget_password_textview)
            return self.global_contents.validate_element(textview_forget_password, textview_forget_password.text,
                                                         Strings.LOGIN_FORGET_PASSWORD, Strings.ERROR)

        elif InputData.target_environment == Strings.IOS:
            all_buttons = self.driver.find_elements_by_class_name(self.elements.all_buttons)
            textview_forget_password = all_buttons[1]
            return textview_forget_password

    def get_sign_in_button(self):
        """
        Get Sing In

        Returns:
             Sing In Element
        """

        if InputData.target_environment == Strings.ANDROID:
            button_sing_in = self.driver.find_element_by_id(self.elements.login_singin_button)
            return self.global_contents.validate_element(button_sing_in, button_sing_in.text, Strings.LOGIN,
                                                         Strings.ERROR_LABEL_NOT_MATCHING)

        elif InputData.target_environment == Strings.IOS:
            all_buttons = self.driver.find_elements_by_class_name(self.elements.all_buttons)
            button_sing_in = all_buttons[2]
            return button_sing_in

    def get_login_with_email_divider_textview(self):
        """
        Get Login with Email Divider

        Returns:
             Login with Email Divider Element
        """

        if InputData.target_environment == Strings.ANDROID:
            textview_login_with_email_divider = self.driver.find_element_by_id(self.elements.login_signin_divider_textview)
            return self.global_contents.validate_element(textview_login_with_email_divider,
                                                         textview_login_with_email_divider.text,
                                                         Strings.LOGIN_ANDROID_WITH_EMAIL_DIVIDER, Strings.ERROR)

        elif InputData.target_environment == Strings.IOS:
            textview_login_with_email_divider = self.driver.find_element_by_id(self.elements.login_signin_divider_textview)
            return textview_login_with_email_divider

    def get_facebook_textview(self):
        """
        Get Facebook

        Returns:
             Facebook Element
        """

        if InputData.target_environment == Strings.ANDROID:
            textview_facebook = self.driver.find_element_by_id(self.elements.login_facebook_textview)
            return self.global_contents.validate_element(textview_facebook, textview_facebook.text,
                                                         Strings.FACEBOOK_OPTION, Strings.ERROR)

        elif InputData.target_environment == Strings.IOS:
            all_buttons = self.driver.find_elements_by_class_name(self.elements.all_buttons)
            textview_facebook = all_buttons[4]
            return textview_facebook

    def get_google_textview(self):
        """
        Get Google

        Returns:
             Google Element
        """

        if InputData.target_environment == Strings.ANDROID:
            textview_google = self.driver.find_element_by_id(self.elements.login_google_textview)
            return self.global_contents.validate_element(textview_google, textview_google.text, Strings.GOOGLE_OPTION,
                                                         Strings.ERROR)

        elif InputData.target_environment == Strings.IOS:
            all_button = self.driver.find_elements_by_class_name(self.elements.all_buttons)
            textview_google = all_button[3]
            return textview_google

    def get_agree_textview(self):
        """
        Get Agree

        Returns:
             Agree Element
        """

        if InputData.target_environment == Strings.ANDROID:
            textview_agree = self.driver.find_element_by_id(self.elements.login_agree_textview)
            return self.global_contents.validate_element(textview_agree, textview_agree.text, Strings.LOGIN_AGREE,
                                                         Strings.ERROR)

        elif InputData.target_environment == Strings.IOS:
            textview_agree = self.driver.find_element_by_id(self.elements.login_agree_textview)
            return textview_agree

    def get_terms_textview(self):
        """
        Get Terms

        Returns:
             Terms Element
        """

        if InputData.target_environment == Strings.ANDROID:
            textview_terms = self.driver.find_element_by_id(self.elements.login_terms_textview)
            return self.global_contents.validate_element(textview_terms, textview_terms.text, Strings.
                                                         LOGIN_ANDROID_TERMS, Strings.ERROR)

        elif InputData.target_environment == Strings.IOS:
            textview_terms = self.driver.find_element_by_id(self.elements.login_terms_textview)
            return textview_terms

    def login(self, user_name, password):
        """
        Login

        Arguments:
            arg1(str): username
            arg2(str): password

        Returns:
            If Android - Whats New Activity Name
            If iOS - Whats New screen Title
        """

        self.get_username_editfield().send_keys(user_name)
        if InputData.target_environment == Strings.ANDROID:
            self.driver.hide_keyboard()
        self.get_password_editfield().send_keys(password)
        if InputData.target_environment == Strings.ANDROID:
            self.driver.hide_keyboard()
        self.get_sign_in_button().click()
        sleep(self.global_contents.max_timeout)

        if InputData.target_environment == Strings.ANDROID:
            print(self.driver.current_activity)
            return self.driver.current_activity

        elif InputData.target_environment == Strings.IOS:
            tv_screen_title = self.driver.find_element_by_id(self.elements.whats_new_title_textview)
            return tv_screen_title
