"""
    New Logistrtion Page Module
"""

from time import sleep
from common import strings
from ios.pages import ios_elements
from ios.pages.ios_base_page import IosBasePage


class IosWhatsNew(IosBasePage):
    """
    Whats New screen
    """

    def on_screen(self):
        """
        Load Whats New screen

        Returns:
            str: Whats New screen Title Name
        """

        textview_screen_title = self.driver.find_element_by_id(ios_elements.whats_new_title_textview)
        return textview_screen_title

    def get_title_textview(self):
        """
        Get Screen Title

        Returns:
            webdriver element: Screen Title Element
        """

        textview_screen_title = self.driver.find_element_by_id(ios_elements.whats_new_title_textview)
        return textview_screen_title

    def get_cross_icon(self):
        """
        Get Cross Icon

        Returns:
             webdriver element: Cross Icon Element
        """

        button_cross = self.driver.find_element_by_id(ios_elements.whats_new_close_button)
        return button_cross

    def get_main_image(self):
        """
        Get Main Image

        Returns:
             webdriver element:  Main Image Element
        """

        image_main_logo = self.driver.find_element_by_id(ios_elements.whats_new_main_image)
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

        all_textviews = self.driver.find_elements_by_class_name(
            ios_elements.all_textviews
        )
        textview_feature_title = all_textviews[1]
        return textview_feature_title

    def get_feature_details(self):
        """
        Get Feature Details

        Returns:
             webdriver element: Feature Details Element
        """

        all_textviews = self.driver.find_elements_by_class_name(ios_elements.all_textviews)
        textview_feature_details = all_textviews[2]
        return textview_feature_details

    def get_done_button(self):
        """
        Get Done

        Returns:
             webdriver element: Done Element
        """

        button_done = self.driver.find_element_by_id(ios_elements.whats_new_done_button)
        return button_done

    def exit_features(self):
        """
        Exit What New Screen/Features

        Returns:
            str: Main Dashboard screen Title
        """

        self.get_done_button().click()
        sleep(self.global_contents.medium_timeout)
        textview_screen_title = self.driver.find_element_by_id(ios_elements.main_dashboard_title_textview)
        return textview_screen_title
