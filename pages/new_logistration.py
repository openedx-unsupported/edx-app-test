from time import sleep
from common.elements import Elements
from common.globals import Globals
from common.strings import Strings
from testdata.input_data import InputData


class NewLogistration():
    """
    New Logistration screen
    """

    def __init__(self, driver):
        self.driver = driver
        self.global_contents = Globals()
        self.elements = Elements()

    def load_app(self):
        """
        Load New Logistration screen

        Args:

        Returns:
            If Android - New Logistration Activity Name
            If iOS - New Logistration screen Title Name
        """

        if InputData.target_environment == Strings.ANDROID:
            print(self.driver.current_activity)
            return self.driver.current_activity

        elif InputData.target_environment == Strings.IOS:
            button_discover_courses = self.driver.find_element_by_id(self.elements.new_logistration_discover_courses_button)
            return button_discover_courses

    def get_edx_logo(self):
        """
        Get edX logo

        Args:

        Returns:
            Logo element
        """
        if InputData.target_environment == Strings.ANDROID:
            image_edx_logo = self.driver.find_element_by_id(self.elements.new_logistration_logo)
            return self.global_contents.validate_element(image_edx_logo, image_edx_logo.text,
                                            Strings.BLANK_FIELD, Strings.ERROR_LABEL_NOT_MATCHING)
        elif InputData.target_environment == Strings.IOS:
            all_images = self.driver.find_elements_by_class_name(self.elements.new_logistration_logo)
            image_edx_logo = all_images[1]
            return image_edx_logo

    def get_discover_course_button(self):
        """
        Get Discover Button

        Args:

        Returns:
            Discover Button element
        """
        button_discover_courses = self.driver.find_element_by_id(self.elements.new_logistration_discover_courses_button)

        return self.global_contents.validate_element(button_discover_courses, button_discover_courses.text,
                                        Strings.NEW_LOGIS_DISCOVER_COURSES, Strings.ERROR_LABEL_NOT_MATCHING)
        
    def get_register_button(self):
        """
        Get Register Button

        Args:

        Returns:
            Register Button element
        """

        button_register = self.driver.find_element_by_id(self.elements.new_logistration_register_button)
        return self.global_contents.validate_element(button_register, button_register.text, Strings.NEW_LOGIS_REGISTER,
                                        Strings.ERROR_LABEL_NOT_MATCHING)

    def get_signin_button(self):
        """
        Get Login Button
        Args:

        Returns:
            Login Button element
        """

        button_login = self.driver.find_element_by_id(self.elements.new_logistration_sign_in_button)
        return self.global_contents.validate_element(button_login, button_login.text, Strings.NEW_LOGIS_LOGIN,
                                        Strings.ERROR_LABEL_NOT_MATCHING)

    def load_login_screen(self):
        """
        Load Login Screen

        Args:

        Returns:
             If Android - Login Activity Name
             If iOS - Login screen Title Name
        """

        self.get_signin_button().click()
        sleep(self.global_contents.med_timeout)

        if InputData.target_environment == Strings.ANDROID:
            print(self.driver.current_activity)
            return self.driver.current_activity

        elif InputData.target_environment == Strings.IOS:
            textview_screen_title = self.driver.find_element_by_id(self.elements.login_title_textview)
            return textview_screen_title

    def load_register_screen(self):
        """
        Load Register Screen

        Args:

        Returns:
             If Android - Register Activity Name
             If iOS - Register screen Title Name
        """

        self.get_register_button().click()
        sleep(self.global_contents.med_timeout)
        print(self.driver.current_activity)

        return self.driver.current_activity