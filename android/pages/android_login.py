"""
    Login Page Module
"""

from time import sleep

from android.pages.android_base_page import AndroidBasePage
from common import strings
from android.pages import android_elements


class AndroidLogin(AndroidBasePage):
    """
    Login screen
    """

    def on_screen(self):
        """
        Load Login screen

        Returns:
            str: Login Activity Name
        """

        self.log.info(self.driver.current_activity)
        return self.driver.current_activity

    def get_title_textview(self):
        """
        Get Screen Title

        Returns:
              webdriver element: Screen Title Element
        """

        all_textviews_on_screen = self.global_contents.get_all_views(self.driver, android_elements.all_textviews)
        textview_screen_title = all_textviews_on_screen[0]
        return self.global_contents.validate_element(
            textview_screen_title,
            textview_screen_title.text,
            strings.LOGIN_SCREEN_TITLE,
            strings.ERROR
        )

    def get_logo(self):
        """
        Get logo

        Returns:
              webdriver element: Logo Element
        """

        image_logo = self.driver.find_element_by_id(android_elements.login_edx_logo)
        return self.global_contents.validate_element(
            image_logo,
            image_logo.text,
            strings.BLANK_FIELD,
            strings.ERROR
        )

    def get_username_editfield(self):
        """
        Get Username

        Returns:
              webdriver element: Username Element
        """

        editfield_user_name = self.driver.find_element_by_id(android_elements.login_user_name_editfield)
        return self.global_contents.validate_element(
            editfield_user_name,
            editfield_user_name.text,
            strings.BLANK_FIELD,
            strings.ERROR_LABEL_NOT_MATCHING
        )

    def get_password_editfield(self):
        """
        Get Password

        Returns:
              webdriver element: Password Element
        """

        editfield_password = self.driver.find_element_by_id(android_elements.login_password_editfield)
        return self.global_contents.validate_element(
            editfield_password,
            editfield_password.text,
            strings.BLANK_FIELD,
            strings.ERROR_LABEL_NOT_MATCHING
        )

    def get_forget_password_textview(self):
        """
        Get Forget Password

        Returns:
              webdriver element: Forget Password Element
        """

        textview_forget_password = self.driver.find_element_by_id(android_elements.login_forget_password_textview)
        return self.global_contents.validate_element(
            textview_forget_password,
            textview_forget_password.text,
            strings.LOGIN_FORGET_PASSWORD,
            strings.ERROR
        )

    def get_sign_in_button(self):
        """
        Get Sing In

        Returns:
              webdriver element: Sing In Element
        """

        button_sing_in = self.driver.find_element_by_id(android_elements.login_singin_button)
        return self.global_contents.validate_element(
            button_sing_in, button_sing_in.text,
            strings.LOGIN,
            strings.ERROR_LABEL_NOT_MATCHING
        )

    def get_login_with_email_divider_textview(self):
        """
        Get Login with Email Divider

        Returns:
              webdriver element: Login with Email Divider Element
        """

        textview_login_with_email_divider = self.driver.find_element_by_id(
            android_elements.login_signin_divider_textview
        )
        return self.global_contents.validate_element(
            textview_login_with_email_divider,
            textview_login_with_email_divider.text,
            strings.LOGIN_ANDROID_WITH_EMAIL_DIVIDER,
            strings.ERROR
        )

    def get_facebook_textview(self):
        """
        Get Facebook

        Returns:
              webdriver element: Facebook Element
        """

        textview_facebook = self.driver.find_element_by_id(android_elements.login_facebook_textview)
        return self.global_contents.validate_element(
            textview_facebook,
            textview_facebook.text,
            strings.FACEBOOK_OPTION,
            strings.ERROR
        )

    def get_google_textview(self):
        """
        Get Google

        Returns:
              webdriver element: Google Element
        """

        textview_google = self.driver.find_element_by_id(android_elements.login_google_textview)
        return self.global_contents.validate_element(
            textview_google,
            textview_google.text,
            strings.GOOGLE_OPTION,
            strings.ERROR
        )

    def get_agree_textview(self):
        """
        Get Agree

        Returns:
              webdriver element: Agree Element
        """

        textview_agree = self.driver.find_element_by_id(android_elements.login_agree_textview)
        return self.global_contents.validate_element(
            textview_agree,
            textview_agree.text,
            strings.LOGIN_AGREE,
            strings.ERROR
        )

    def get_terms_textview(self):
        """
        Get Terms

        Returns:
              webdriver element: Terms Element
        """

        textview_terms = self.driver.find_element_by_id(android_elements.login_terms_textview)
        return self.global_contents.validate_element(
            textview_terms,
            textview_terms.text,
            strings.LOGIN_ANDROID_TERMS,
            strings.ERROR
        )

    def login(self, user_name, password):
        """
        Login

        Arguments:
            arg1(str): username
            arg2(str): password

        Returns:
            str: Whats New Activity Name
        """

        self.get_username_editfield().clear()

        self.get_username_editfield().send_keys(user_name)
        self.driver.hide_keyboard()

        self.get_password_editfield().send_keys(password)
        self.driver.hide_keyboard()

        self.get_sign_in_button().click()
        sleep(self.global_contents.maximum_timeout)

        self.log.info(self.driver.current_activity)
        return self.driver.current_activity
