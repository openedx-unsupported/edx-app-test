"""
    Login Page Module
"""

from ios.pages import ios_elements
from ios.pages.ios_base_page import IosBasePage
from ios.pages.ios_whats_new import IosWhatsNew


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

        return self.get_sign_in_button()

    def get_close_button(self):
        """
        Get Close Button

        Returns:
             webdriver element: Close Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_close_button
        )

    def get_title_textview(self):
        """
        Get Screen Title

        Returns:
            webdriver element: Screen Title Element
        """

        return self.driver.find_element_by_id(ios_elements.login_title_textview)

    def get_logo(self):
        """
        Get edX logo

        Returns:
             webdriver element: Logo Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_edx_logo
        )

    def get_username_editfield(self):
        """
        Get Username

        Returns:
             webdriver element: Username Element
        """
        user_name = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_user_name_editfield
        )
        user_name.clear()
        return user_name

    def get_password_editfield(self):
        """
        Get Password

        Returns:
             webdriver element: Password Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_password_editfield
        )

    def get_forget_password_textview(self):
        """
        Get Forget Password

        Returns:
             webdriver element: Forget Password Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_forget_password_textview
        )

    def get_sign_in_button(self):
        """
        Get Sing In

        Returns:
             webdriver element: Sing In Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_signin_button
        )

    def get_login_with_email_divider_textview(self):
        """
        Get Login with Email Divider

        Returns:
             webdriver element: Login with Email Divider Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_signin_divider_textview
        )

    def get_facebook_textview(self):
        """
        Get Facebook

        Returns:
             webdriver element: Facebook Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_facebook_textview
        )

    def get_google_textview(self):
        """
        Get Google

        Returns:
             webdriver element: Google Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_google_textview
        )

    def get_agree_textview(self):
        """
        Get Agree

        Returns:
             webdriver element: Agree Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_agree_textview
        )

    def get_terms_textview(self):
        """
        Get Terms

        Returns:
             webdriver element: Terms Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_terms_textview
        )

    def login(self, user_name, password, is_first_time=True):
        """
        Login

        Arguments:
            user_name (str): username
            password (str): password
            is_first_time (bool): True or False

        Returns:
            str: Whats New screen Title
        """

        self.get_username_editfield().clear()
        self.get_username_editfield().send_keys(user_name)

        self.get_password_editfield().send_keys(password)
        self.get_sign_in_button().click()

        if is_first_time:
            textview_screen_title = IosWhatsNew(self.driver, self.log).get_title_textview()
            self.global_contents.is_first_time = False
        else:
            textview_screen_title = self.global_contents.wait_and_get_element(
                self.driver,
                ios_elements.main_dashboard_navigation_icon
            )
        return textview_screen_title
