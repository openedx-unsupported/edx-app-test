"""
    Profile Options Page Module
"""

from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidProfileOptions(AndroidBasePage):
    """
    Profile Options screen
    """

    def get_all_textviews(self):
        """
        Wait for all textview on screen
        Returns:
            webdriver element: Subsection title element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.all_textviews
        )

        all_textviews_on_screen = self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.all_textviews
        )

        return all_textviews_on_screen

    def get_all_image_buttons(self):
        """
        Wait for all textview on screen
        Returns:
            webdriver element: Subsection title element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.all_image_buttons
        )

        all_image_buttons_on_screen = self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.all_image_buttons
        )

        return all_image_buttons_on_screen

    def get_all_video_qualitie_titles(self):
        """
        Wait for all video quality popup
        Returns:
            webdriver element: all title elements
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.video_quality_all_titles
        )

        video_quality_all_titles = self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.video_quality_all_titles
        )

        return video_quality_all_titles
