# coding=utf-8
"""
    Whats New Page Module
"""

from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosWhatsNew(IosBasePage):
    """
    Whats New screen
    """

    def get_title_textview(self):
        """
        Get Screen Title

        Returns:
            webdriver element: Screen Title Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.whats_new_title_textview
        )

    def get_close_button(self):
        """
        Get Close Icon

        Returns:
             webdriver element: Close Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.whats_new_close_button
        )

    def get_main_image(self):
        """
        Get Main Image

        Returns:
             webdriver element:  Main Image Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.whats_new_main_image
        )

    def get_feature_title_textview(self):
        """
        Get Feature Title

        Returns:
             webdriver element: Feature Title Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.whats_new_feature_title_textview
        )

    def get_feature_details(self):
        """
        Get Feature Details

        Returns:
             webdriver element: Feature Details Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.whats_new_feature_details_textview
        )

    def get_done_button(self):
        """
        Get Done

        Returns:
             webdriver element: Done Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.whats_new_done_button
        )

    def exit_features(self):
        """
        Exit What New Screen/Features

        Returns:
            webdriver element:: Main Dashboard screen Title element
        """

        self.get_close_button().click()

        return self.driver.find_element_by_id(ios_elements.main_dashboard_title_textview)

    def navigate_features(self):
        """
        Navigate between features
        """

        feature_main_image = self.get_main_image()
        screen_width = self.driver.get_window_size()["width"]
        screen_height = self.driver.get_window_size()["height"]
        element_x_position = feature_main_image.location['x']
        element_y_position = feature_main_image.location['y']

        self.log.info('screen width {} - screen height {} - element_x {} - element_y {} '.format(
            screen_width,
            screen_height,
            element_x_position,
            element_y_position
        ))

        horizontal_start_point = int(element_x_position + screen_width)
        vertical_start_point = int(element_x_position + screen_height / 2)
        horizontal_end_point = int(element_x_position + screen_width / 4)
        vertical_end_point = int(element_x_position + screen_height / 2)

        self.log.info('horizontal_start_point {} - vertical_start_point {} - horizontal_end_point {} - '
                      'vertical_end_point {} '.format(horizontal_start_point, horizontal_end_point,
                                                      vertical_start_point, vertical_end_point
                                                      ))

        self.driver.flick(horizontal_start_point, vertical_start_point, horizontal_end_point,
                          vertical_end_point)

        return self.get_close_button()
