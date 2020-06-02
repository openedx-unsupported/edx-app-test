# coding=utf-8
"""
    Login Page Module
"""

from tests.common import strings
from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage
from tests.ios.pages.ios_new_landing import IosNewLanding
from tests.ios.pages.ios_whats_new import IosWhatsNew


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
        self.get_logo().click()
        return user_name

    def get_password_editfield(self):
        """
        Get Password

        Returns:
             webdriver element: Password Element
        """
        self.get_logo().click()
        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_password_editfield
        )

    def get_forgot_password_textview(self):
        """
        Get Forgot Password

        Returns:
             webdriver element: Forgot Password Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_forgot_password_textview
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

    def get_agreement_textview(self):
        """
        Get Agreement

        Returns:
             webdriver element: Agreement Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_agreement_textview
        )

    def get_eula_textview(self):
        """
        Get EULA

        Returns:
             webdriver element: EULA Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_eula_textview
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

    def get_privacy_textview(self):
        """
        Get Privacy

        Returns:
             webdriver element: Privacy Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_privacy_textview
        )

    def get_agreement_close_button(self):
        """
        Get Close

        Returns:
             webdriver element: Close Element
        """

        return self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_buttons
        )[self.global_contents.fourth_existence]

    def load_eula_screen(self):
        """
        Load EULA screen and then close it

        Returns:
             webdriver element: Login Button Element
        """

        self.get_eula_textview().click()
        self.global_contents.wait_for_element_visibility(
            self.driver,
            self.get_agreement_close_button()
        )
        self.get_agreement_close_button().click()

        return self.get_sign_in_button()

    def load_terms_screen(self):
        """
        Load Terms screen and then close it

        Returns:
             webdriver element: Login Button Element
        """

        self.get_terms_textview().click()
        self.global_contents.wait_for_element_visibility(
            self.driver,
            self.get_agreement_close_button()
        )
        self.get_agreement_close_button().click()

        return self.get_sign_in_button()

    def load_privacy_screen(self):
        """
        Load Privacy screen and then close it

        Returns:
             webdriver element: Login Button Element
        """

        self.get_privacy_textview().click()
        self.global_contents.wait_for_element_visibility(
            self.driver,
            self.get_agreement_close_button()
        )
        self.get_agreement_close_button().click()

        return self.get_sign_in_button()

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
        self.get_username_editfield().click()
        self.get_username_editfield().clear()
        self.get_username_editfield().send_keys(user_name)

        self.get_password_editfield().click()
        self.get_password_editfield().send_keys(password)
        self.get_logo().click()
        self.get_sign_in_button().click()

        output = self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.login_wrong_credential_alert_title
        )

        if output:
            self.global_contents.wait_and_get_element(
                self.driver,
                ios_elements.login_wrong_credential_alert_title
            )
            self.global_contents.wait_and_get_element(
                self.driver,
                ios_elements.login_wrong_credential_alert_msg
            )
            wrong_credentials_alert_ok = self.global_contents.wait_and_get_element(
                self.driver,
                ios_elements.login_reset_password_alert_ok_button
            )
            wrong_credentials_alert_ok.click()

            return False

        else:
            if is_first_time is True:
                textview_screen_title = IosWhatsNew(self.driver, self.log).get_title_textview()
                self.global_contents.is_first_time = False
            else:
                # textview_screen_title = IosWhatsNew(self.driver, self.log).get_close_button()
                # textview_screen_title.click()

                textview_screen_title = self.global_contents.wait_and_get_element(
                    self.driver,
                    ios_elements.main_dashboard_navigation_icon
                )
        return textview_screen_title

    def back_and_forth_new_landing(self):
        """
        From Login screen tapping back will load New Landing screen and tapping Login will
            load Login screen

        Returns:
             bool: Returns True if app is back on Login screen from New Landing screen
        """

        ios_new_landing = IosNewLanding(self.driver, self.log)

        if self.on_screen().text == strings.LOGIN:
            self.driver.back()
            if ios_new_landing.load_login_screen().text != strings.LOGIN:
                self.log.error('Problem - New Landing screen is not loaded')
                self.global_contents.flag = False
        else:
            self.log.info('Problem - Login screen is not loaded')
            self.global_contents.flag = False

        return self.global_contents.flag

    def back_and_forth_terms(self):
        """
        From Login screen tapping 'edX Terms of Service...' will load Terms & Conditions screen
            and tapping back will load Login screen

        Returns:
             bool: Returns True if app is back on Login screen from edX Terms of Service
        """

        if self.on_screen().text == strings.LOGIN:
            self.global_contents.flag = True
            self.get_terms_textview().click()

            self.global_contents.wait_and_get_element(
                self.driver,
                ios_elements.login_agreement_close).click()
            if self.on_screen().text == strings.LOGIN:
                self.global_contents.flag = True
            else:
                self.log.error('Problem - Terms screen is not loaded')
                self.global_contents.flag = False
        else:
            self.log.info('Problem - Login screen is not loaded')
            self.global_contents.flag = False

        return self.global_contents.flag

    def get_forgot_password_alert(self):
        """
        Load forgot Password alert

        Returns:
             webdriver element: alert element
        """

        self.get_forgot_password_textview().click()
        return self.driver.find_element_by_id(ios_elements.login_reset_password_alert_title)

    def get_forgot_password_alert_title(self):
        """
        Get alert's title element on Forgot Password Alert

        Returns:
             webdriver element: alert title element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_reset_password_alert_title
        )

    def get_forgot_password_alert_msg(self):
        """
        Get alert message element on Forgot Password Alert

        Returns:
             webdriver element: message element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_reset_password_alert_msg
        )

    def get_forgot_password_alert_ok_button(self):
        """
        Get OK button element on Forgot Password Alert

        Returns:
             webdriver element: OK element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_reset_password_alert_ok_button
        )

    def get_forgot_password_alert_cancel_button(self):
        """
        Get Cancel button element on Forgot Password Alert

        Returns:
             webdriver element: CANCEL element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.login_reset_password_alert_cancel_button
        )

    def close_forgot_password_alert(self):
        """
        Close forgot password alert

        Returns:
             bool: True if alert is closed, False if alert is not closed
        """

        self.get_forgot_password_alert_cancel_button().click()
        return self.global_contents.wait_for_element_invisibility(
            self.driver,
            ios_elements.login_reset_password_alert_cancel_button
        )
