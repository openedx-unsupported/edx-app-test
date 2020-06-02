# coding=utf-8
"""
    Whats New Page Module
"""

from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


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

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.WHATS_NEW_ACTIVITY_NAME
        )

    def get_title_textview(self):
        """
        Get Screen Title

        Returns:
             webdriver element: Screen Title Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.whats_new_title_textview
        )

    def get_cross_icon(self):
        """
        Get Cross Icon

        Returns:
             webdriver element: Cross Icon Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.whats_new_close_button
        )

    def get_main_image(self):
        """
        Get Main Image

        Returns:
             webdriver element: Main Image Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.whats_new_main_image
        )

    def get_feature_title_textview(self):
        """
        Get Feature Title

        Returns:
             webdriver element: Feature Title Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.whats_new_feature_title_textview
        )

    def get_feature_details(self):
        """
        Get Feature Details

        Returns:
             webdriver element: Feature Details Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.whats_new_feature_details_textview
        )

    def get_done_button(self):
        """
        Get Done

        Returns:
             webdriver element: Done Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.whats_new_done_button
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.whats_new_done_button
        )

    def exit_features(self):
        """
        Exit What New Screen/Features

        Returns:
             str: Main Dashboard Activity Name
        """

        self.get_done_button().click()

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.MAIN_DASHBOARD_ACTIVITY_NAME
        )

    def navigate_features(self):
        """
        Navigate between features

        Returns:
             webdriver element: Done Element
        """

        feature_main_image = self.get_main_image()
        screen_width = self.driver.get_window_size()["width"]
        screen_height = self.driver.get_window_size()["height"]
        element_x_position = feature_main_image.location['x']
        element_y_position = feature_main_image.location['y']

        self.log.info('screen width {} - screen height {} - element_x {} - element_y {} '
                      .format(
                          screen_width,
                          screen_height,
                          element_x_position,
                          element_y_position
                      ))

        horizontal_start_point = int(screen_width - screen_width * 0.1)
        vertical_start_point = int(screen_height / 2)
        horizontal_end_point = 0
        vertical_end_point = int(screen_height / 2)

        self.log.info('horizontal_start_point {} - vertical_start_point {} - horizontal_end_point {}'
                      ' - vertical_end_point {} '.format(
                          horizontal_start_point,
                          horizontal_end_point,
                          vertical_start_point,
                          vertical_end_point
                      ))

        self.driver.swipe(horizontal_start_point, vertical_start_point, horizontal_end_point, vertical_end_point, 500)

        return self.get_done_button()
