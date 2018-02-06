"""
    New Logistrtion Page Module
"""

from time import sleep

from android.pages.android_base_page import AndroidBasePage
from common.globals import Globals
from common import strings
from android.pages import android_elements


class AndroidWhatsNew(AndroidBasePage):
    """
    Whats New screen
    """

    def on_screen(self):
        """
        Load Whats New screen

        Returns:
            str: Whats New Activity Name
        """

        self.log.info(self.driver.current_activity)
        return self.driver.current_activity

    def get_title_textview(self):
        """
        Get Screen Title

        Returns:
             webdriver element: Screen Title Element
        """

        textview_screen_title = self.driver.find_element_by_id(android_elements.whats_new_title_textview)
        return self.global_contents.validate_element(
            textview_screen_title,
            textview_screen_title.text,
            strings.WHATS_NEW_ANDROID_SCREEN_TITLE,
            strings.ERROR
        )

    def get_cross_icon(self):
        """
        Get Cross Icon

        Returns:
             webdriver element: Cross Icon Element
        """

        button_cross = self.driver.find_element_by_id(android_elements.whats_new_close_button)
        return self.global_contents.validate_element(
            button_cross,
            button_cross.text,
            strings.WHATS_NEW_CROSS,
            strings.ERROR
        )

    def get_main_image(self):
        """
        Get Main Image

        Returns:
             webdriver element: Main Image Element
        """

        image_main_logo = self.driver.find_element_by_id(android_elements.whats_new_main_image)
        return self.global_contents.validate_element(
            image_main_logo,
            image_main_logo.text,
            strings.BLANK_FIELD,
            strings.ERROR
        )

    def get_feature_title_textview(self):
        """
        Get Feature Title

        Returns:
             webdriver element: Feature Title Element
        """

        textview_feature_title = self.driver.find_element_by_id(android_elements.whats_new_feature_title_textview)
        return self.global_contents.validate_element(
            textview_feature_title,
            textview_feature_title.text,
            strings.WHATS_NEW_FEATURE_TITLE,
            strings.ERROR
        )

    def get_feature_details(self):
        """
        Get Feature Details

        Returns:
             webdriver element: Feature Details Element
        """

        textview_feature_details = self.driver.find_element_by_id(android_elements.whats_new_feature_details_textview)
        return self.global_contents.validate_element(
            textview_feature_details,
            textview_feature_details.text,
            strings.WHATS_NEW_FEATURE_DETAILS,
            strings.ERROR_LABEL_NOT_MATCHING
        )

    def get_done_button(self):
        """
        Get Done

        Returns:
             webdriver element: Done Element
        """

        button_done = self.driver.find_element_by_id(android_elements.whats_new_done_button)
        return self.global_contents.validate_element(
            button_done,
            button_done.text,
            strings.WHATS_NEW_DONE,
            strings.ERROR
        )

    def exit_features(self):
        """
        Exit What New Screen/Features

        Returns:
             str: Main Dashboard Activity Name
        """

        self.get_done_button().click()
        sleep(self.global_contents.medium_timeout)
        self.log.info(self.driver.current_activity)
        return self.driver.current_activity
