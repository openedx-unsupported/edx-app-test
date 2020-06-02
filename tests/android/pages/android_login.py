# coding=utf-8
"""
    Login Page Module
"""
from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage
from tests.android.pages.android_new_landing import AndroidNewLanding
from tests.common.globals import Globals


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

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.LOGIN_ACTIVITY_NAME
        )

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

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.login_user_name_editfield
        )

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

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.login_forgot_password_textview
        )

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

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.login_signin_button
        )

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

    def get_agreement_textview(self):
        """
        Get Agree

        Returns:
              webdriver element: Agreement Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.login_agreement_textview
        )

    def load_eula_screen(self):
        """
        Load EULA screen and get back to Login Screen

        Returns:
             bool: Returns True if app is back on Login screen from EULA
        """

        self.global_contents.get_element_coordinates(self.driver, android_elements.login_agreement_textview)

        target_x_position = self.global_contents.element_x_position + int(self.global_contents.element_width / 2) + 200
        target_y_position = self.global_contents.element_y_position + int(self.global_contents.element_height / 4)

        return self.navigate_eula(target_x_position, target_y_position)

    def load_terms_screen(self):
        """
        Load Terms screen and get back to Login Screen

        Returns:
             bool: Returns True if app is back on Login screen from Terms
        """

        self.global_contents.get_element_coordinates(self.driver, android_elements.login_agreement_textview)

        target_x_position = self.global_contents.element_x_position + int(self.global_contents.element_width / 2)
        target_y_position = self.global_contents.element_y_position + int(self.global_contents.element_height / 2)

        return self.navigate_eula(target_x_position, target_y_position)

    def load_privacy_screen(self):
        """
        Load Privacy screen and get back to Login Screen

        Returns:
             bool: Returns True if app is back on Login screen from Privacy
        """

        self.global_contents.get_element_coordinates(self.driver, android_elements.login_agreement_textview)

        target_x_position = self.global_contents.element_x_position + int(self.global_contents.element_width / 2) + 100
        target_y_position = self.global_contents.element_y_position + int(self.global_contents.element_height / 2) + 38

        return self.navigate_eula(target_x_position, target_y_position)

    def navigate_eula(self, target_x_position, target_y_position):
        """
        Tap on specific given coordinates on screen and navigate back

        Returns:
             bool: Returns True or False based on the conditions applied
        """

        self.log.info('Going to tap on x-position {} - y-position {}'.format(
            target_x_position,
            target_y_position
        ))

        self.driver.tap([(target_x_position, target_y_position)])

        self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.EULA_ACTIVITY_NAME)

        if self.driver.current_activity == Globals.EULA_ACTIVITY_NAME:
            self.get_back_icon().click()
            if self.driver.current_activity == Globals.LOGIN_ACTIVITY_NAME:
                self.global_contents.flag = True
            else:
                self.log.error('Login screen is not loaded')
                self.global_contents.flag = False
        else:
            self.log.error('EULA screen is not loaded')
            self.global_contents.flag = False

        return self.global_contents.flag

    def login(self, user_name, password, is_first_time=True):
        """
        Login with given username and password

        Arguments:
            user_name (str): username
            password (str): password
            is_first_time (bool): true/false

        Returns:
            str: Whats New Activity Name
        """

        self.get_username_editfield().clear()
        self.get_username_editfield().click()
        self.get_username_editfield().send_keys(user_name)
        # self.driver.back()
        self.get_password_editfield().click()
        self.get_password_editfield().send_keys(password)
        # self.driver.back()
        self.get_sign_in_button().click()

        output = self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.login_wrong_credential_alert_title
        )

        if output:
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

            return False

        else:
            if is_first_time:
                self.target_activity = self.global_contents.wait_for_android_activity_to_load(
                    self.driver,
                    self.global_contents.WHATS_NEW_ACTIVITY_NAME
                )
            else:
                self.target_activity = self.global_contents.wait_for_android_activity_to_load(
                    self.driver,
                    self.global_contents.MAIN_DASHBOARD_ACTIVITY_NAME
                )

            return self.target_activity

    def back_and_forth_login(self):

        """
        Load login screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on Login screen from Login screen
        """

        android_new_landing_page = AndroidNewLanding(self.driver, self.log)

        if self.driver.current_activity == Globals.LOGIN_ACTIVITY_NAME:
            self.get_back_icon().click()

            if (self.driver.current_activity == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME and
                    android_new_landing_page.load_login_screen() == Globals.LOGIN_ACTIVITY_NAME):
                self.global_contents.flag = True
            else:
                self.log.error('New Landing screen is not loaded')
                self.global_contents.flag = False
        else:
            self.log.error('Login screen is not loaded')
            self.global_contents.flag = False

        return self.global_contents.flag

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
        return self.global_contents.wait_for_element_invisibility(
            self.driver,
            android_elements.login_reset_password_alert_cancel_button
        )
