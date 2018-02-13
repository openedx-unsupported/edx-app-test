"""
    Login Page Module
"""

from time import sleep
from ios.pages import ios_elements
from ios.pages.ios_base_page import IosBasePage


class IosLogin(IosBasePage):
    """
    Login screen
    """

    def on_screen(self):
        """
        Load Login screen

        Returns:
            str: Login screen Title Name
        """

        textview_screen_title = self.driver.find_element_by_id(ios_elements.login_title_textview)
        return textview_screen_title

    def get_title_textview(self):
        """
        Get Screen Title

        Returns:
            webdriver element: Screen Title Element
        """

        textview_screen_title = self.driver.find_element_by_id(ios_elements.login_title_textview)
        return textview_screen_title

    def get_logo(self):
        """
        Get logo

        Returns:
             webdriver element: Logo Element
        """

        image_logo = self.driver.find_element_by_id(ios_elements.login_edx_logo)
        return image_logo

    def get_username_editfield(self):
        """
        Get Username

        Returns:
             webdriver element: Username Element
        """

        editfield_user_name = self.driver.find_element_by_class_name(ios_elements.login_user_name_editfield)
        editfield_user_name.clear()
        return editfield_user_name

    def get_password_editfield(self):
        """
        Get Password

        Returns:
             webdriver element: Password Element
        """

        editfield_password = self.driver.find_element_by_class_name(ios_elements.login_password_editfield)
        return editfield_password

    def get_forget_password_textview(self):
        """
        Get Forget Password

        Returns:
             webdriver element: Forget Password Element
        """

        all_buttons = self.driver.find_elements_by_class_name(ios_elements.all_buttons)
        textview_forget_password = all_buttons[1]
        return textview_forget_password

    def get_sign_in_button(self):
        """
        Get Sing In

        Returns:
             webdriver element: Sing In Element
        """

        all_buttons = self.driver.find_elements_by_class_name(ios_elements.all_buttons)
        button_sing_in = all_buttons[2]
        return button_sing_in

    def get_login_with_email_divider_textview(self):
        """
        Get Login with Email Divider

        Returns:
             webdriver element: Login with Email Divider Element
        """

        textview_login_with_email_divider = self.driver.find_element_by_id(ios_elements.login_signin_divider_textview)
        return textview_login_with_email_divider

    def get_facebook_textview(self):
        """
        Get Facebook

        Returns:
             webdriver element: Facebook Element
        """

        all_buttons = self.driver.find_elements_by_class_name(ios_elements.all_buttons)
        textview_facebook = all_buttons[4]
        return textview_facebook

    def get_google_textview(self):
        """
        Get Google

        Returns:
             webdriver element: Google Element
        """

        all_button = self.driver.find_elements_by_class_name(ios_elements.all_buttons)
        textview_google = all_button[3]
        return textview_google

    def get_agree_textview(self):
        """
        Get Agree

        Returns:
             webdriver element: Agree Element
        """

        textview_agree = self.driver.find_element_by_id(ios_elements.login_agree_textview)
        return textview_agree

    def get_terms_textview(self):
        """
        Get Terms

        Returns:
             webdriver element: Terms Element
        """

        textview_terms = self.driver.find_element_by_id(ios_elements.login_terms_textview)
        return textview_terms

    def login(self, user_name, password):
        """
        Login

        Arguments:
            arg1(str): user_name
            arg2(str): password

        Returns:
            str: Whats New screen Title
        """

        self.get_username_editfield().clear()
        self.get_username_editfield().send_keys(user_name)

        self.get_password_editfield().send_keys(password)
        self.get_sign_in_button().click()
        sleep(self.global_contents.maximum_timeout)

        if self.global_contents.is_first_time:
            self.textview_screen_title = self.driver.find_element_by_id(ios_elements.whats_new_title_textview)
            self.global_contents.IsFirstTime = False
        else:
            self.textview_screen_title = self.driver.find_element_by_id(ios_elements.main_dashboard_title_textview)

        return self.textview_screen_title
