from time import sleep
from common.elements import Elements
from common.globals import Globals
from common.strings import Strings
from testdata.input_data import InputData


class WhatsNew:
    """
    Whats New screen
    """

    def __init__(self, driver):
        self.driver = driver
        self.global_content = Globals()
        self.elements = Elements()

    def on_screen(self):
        """
        Load Whats New screen

        Returns:
            If Android - Whats New Activity Name
            If iOS - Whats New screen Title Name
        """

        if InputData.target_environment == Strings.ANDROID:
            print(self.driver.current_activity)
            return self.driver.current_activity

        elif InputData.target_environment == Strings.IOS:
            textview_screen_title = self.driver.find_element_by_id(self.elements.whats_new_title_textview)
            return textview_screen_title

    def get_title_textview(self):
        """
        Get Screen Title

        Returns:
             Screen Title Element
        """

        if InputData.target_environment == Strings.ANDROID:
            textview_screen_title = self.driver.find_element_by_id(self.elements.whats_new_title_textview)
            return self.global_content.validate_element(textview_screen_title, textview_screen_title.text,
                                                        Strings.WHATS_NEW_ANDROID_SCREEN_TITLE,
                                                        Strings.ERROR)

        elif InputData.target_environment == Strings.IOS:
            textview_screen_title = self.driver.find_element_by_id(self.elements.whats_new_title_textview)
            return textview_screen_title

    def get_cross_icon(self):
        """
        Get Cross Icon

        Returns:
             Cross Icon Element
        """

        if InputData.target_environment == Strings.ANDROID:
            button_cross = self.driver.find_element_by_id(self.elements.whats_new_close_button)
            return self.global_content.validate_element(button_cross, button_cross.text, Strings.WHATS_NEW_CROSS,
                                                        Strings.ERROR)

        elif InputData.target_environment == Strings.IOS:
            button_cross = self.driver.find_element_by_class_name(self.elements.whats_new_close_button)
            return button_cross

    def get_main_image(self):
        """
        Get Main Image

        Returns:
             Main Image Element
        """

        image_main_logo = self.driver.find_element_by_id(self.elements.whats_new_main_image)
        return self.global_content.validate_element(image_main_logo, image_main_logo.text, Strings.BLANK_FIELD,
                                                    Strings.ERROR)

    def get_feature_title_textview(self):
        """
        Get Feature Title

        Returns:
             Feature Title Element
        """

        if InputData.target_environment == Strings.ANDROID:
            textview_feature_title = self.driver.find_element_by_id(self.elements.whats_new_feature_title_textview)
            return self.global_content.validate_element(textview_feature_title, textview_feature_title.text,
                                                        Strings.WHATS_NEW_FEATURE_TITLE, Strings.ERROR)
        elif InputData.target_environment == Strings.IOS:
            all_textviews = self.driver.find_elements_by_class_name(self.elements.all_textviews)
            textview_feature_title = all_textviews[1]
            return textview_feature_title

    def get_feature_details(self):
        """
        Get Feature Details

        Returns:
             Feature Details Element
        """

        if InputData.target_environment == Strings.ANDROID:
            textview_feature_details = self.driver.find_element_by_id(self.elements.whats_new_feature_details_textview)
            return self.global_content.validate_element(textview_feature_details, textview_feature_details.text,
                                                        Strings.WHATS_NEW_FEATURE_DETAILS,
                                                        Strings.ERROR_LABEL_NOT_MATCHING)

        elif InputData.target_environment == Strings.IOS:
            all_textviews = self.driver.find_elements_by_class_name(self.elements.all_textviews)
            textview_feature_details = all_textviews[2]
            return textview_feature_details

    def get_done_button(self):
        """
        Get Done

        Returns:
             Done Element
        """

        if InputData.target_environment == Strings.ANDROID:
            button_done = self.driver.find_element_by_id(self.elements.whats_new_done_button)
            return self.global_content.validate_element(button_done, button_done.text, Strings.WHATS_NEW_DONE,
                                                        Strings.ERROR)

        elif InputData.target_environment == Strings.IOS:
            button_done = self.driver.find_element_by_id(self.elements.whats_new_done_button)
            return button_done

    def exit_features(self):
        """
        Exit What New Screen/Features

        Args:

        Returns:
             If Android - Main Dashboard Activity Name
            If iOS - Main Dashboard screen Title
        """

        self.get_done_button().click()
        sleep(self.global_content.med_timeout)

        if InputData.target_environment == Strings.ANDROID:
            print(self.driver.current_activity)
            return self.driver.current_activity

        elif InputData.target_environment == Strings.IOS:
            textview_screen_title = self.driver.find_element_by_id(self.elements.main_dashboard_title_textview)
            return textview_screen_title
