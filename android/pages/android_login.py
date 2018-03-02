"""
    Login Page Module
"""
from android.pages import android_elements
from android.pages.android_base_page import AndroidBasePage
from android.pages.android_new_logistration import AndroidNewLogistration
from common.globals import Globals


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

    def get_back_icon(self):
        """
        Get back icon

        Returns:
              webdriver element: back icon Element
        """

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.all_image_buttons)[0]

    def get_title_textview(self):
        """
        Get Screen Title

        Returns:
              webdriver element: Screen Title Element
        """

        return self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.all_textviews
        )[0]

    def get_logo(self):
        """
        Get logo

        Returns:
              webdriver element: Logo Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.login_edx_logo
        )

    def get_username_editfield(self):
        """
        Get Username

        Returns:
              webdriver element: Username Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.login_user_name_editfield
        )

    def get_password_editfield(self):
        """
        Get Password

        Returns:
              webdriver element: Password Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.login_password_editfield
        )

    def get_forgot_password_textview(self):
        """
        Get forgot Password

        Returns:
              webdriver element: forgot Password Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.login_forgot_password_textview
        )

    def get_sign_in_button(self):
        """
        Get Sing In

        Returns:
              webdriver element: Sing In Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.login_signin_button
        )

    def get_login_with_email_divider_textview(self):
        """
        Get Login with Email Divider

        Returns:
              webdriver element: Login with Email Divider Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.login_signin_divider_textview
        )

    def get_facebook_textview(self):
        """
        Get Facebook

        Returns:
              webdriver element: Facebook Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.login_facebook_textview
        )

    def get_google_textview(self):
        """
        Get Google

        Returns:
              webdriver element: Google Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.login_google_textview
        )

    def get_agree_textview(self):
        """
        Get Agree

        Returns:
              webdriver element: Agree Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.login_agree_textview
        )

    def get_terms_textview(self):
        """
        Get Terms & Conditions

        Returns:
              webdriver element: Terms & Conditions Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.login_terms_textview
        )

    def login(self, user_name, password):
        """
        Login with given username and password

        Arguments:
            user_name (str): username
            password (str): password

        Returns:
            str: Whats New Activity Name
        """

        self.get_username_editfield().clear()
        self.get_username_editfield().send_keys(user_name)
        self.driver.back()
        self.get_password_editfield().send_keys(password)
        self.driver.back()
        self.get_sign_in_button().click()

        out_put = self.global_contents.wait_for_element_visblility(
            self.driver,
            android_elements.login_wrong_credential_alert_title
        )

        if out_put:
            self.global_contents.wait_and_get_element(
                self.driver,
                android_elements.login_wrong_credential_alert_title
            )
            self.global_contents.wait_and_get_element(
                self.driver,
                android_elements.login_wrong_credential_alert_msg
            )
            wrong_credentials_alert_ok = self.global_contents.wait_and_get_element(
                self.driver,
                android_elements.login_reset_password_alert_ok_button
            )
            wrong_credentials_alert_ok.click()

            return False, None

        else:
            self.global_contents.wait_and_get_element(
                self.driver,
                android_elements.whats_new_title_textview
            )
            self.log.info(self.driver.current_activity)

            return self.driver.current_activity

    def back_and_forth_login(self):

        """
        Load login screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on Login screen from Login screen
        """

        android_new_logistration_page = AndroidNewLogistration(self.driver, self.log)
        status_flag = False

        if self.driver.current_activity == Globals.LOGIN_ACTIVITY_NAME:
            self.get_back_icon().click()

            if self.driver.current_activity == Globals.NEW_LOGISTRATION_ACTIVITY_NAME and \
                    android_new_logistration_page.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME:
                status_flag = True
            else:
                self.log.error('New Logistration screen is not loaded')
                status_flag = False
        else:
            self.log.error('Login screen is not loaded')
            status_flag = False

        return status_flag

    def back_and_forth_terms(self):

        """
        Load Terms & Conditions screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on Login screen from Terms & Conditions screen
        """
        status_flag = False
        if self.driver.current_activity == Globals.LOGIN_ACTIVITY_NAME:
            self.get_terms_textview().click()

            if self.driver.current_activity == Globals.TERMS_AND_CONDITIONS_ACTIVITY_NAME:
                self.driver.back()

                if self.driver.current_activity == Globals.LOGIN_ACTIVITY_NAME:
                    status_flag = True
            else:
                self.log.error('Terms and Condition screen is not loaded')
                status_flag = False
        else:
            self.log.error('Login screen is not loaded')
            status_flag = False

        return status_flag

    def get_forgot_password_alert(self):
        """
        Load forgot Password alert

        Returns:
             webdriver element: alert element
        """

        self.get_forgot_password_textview().click()
        return self.driver.find_element_by_id(android_elements.login_reset_password_alert)

    def get_forgot_password_alert_title(self):
        """
        Get alert's title element on Forgot Password Alert

        Returns:
             webdriver element: alert title element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.login_reset_password_alert_title
        )

    def get_forgot_password_alert_msg(self):
        """
        Get alert message element on Forgot Password Alert

        Returns:
             webdriver element: message element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.login_reset_password_alert_msg
        )

    def get_forgot_password_alert_ok_button(self):
        """
        Get OK button element on Forgot Password Alert

        Returns:
             webdriver element: OK element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.login_reset_password_alert_ok_button
        )

    def get_forgot_password_alert_cancel_button(self):
        """
        Get Cancel button element on Forgot Password Alert

        Returns:
             webdriver element: CANCEL element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.login_reset_password_alert_cancel_button
        )

    def close_forgot_password_alert(self):
        """
        Close forgot password alert

        Returns:
             bool: True if alert is closed, False if alert is not closed
        """

        self.get_forgot_password_alert_cancel_button().click()
        return self.global_contents.wait_for_element_invisblility(
            self.driver,
            android_elements.login_reset_password_alert_cancel_button
        )
