"""
   Module covers Android & iOS screens' global contents
"""
from time import sleep
from common.elements import Elements
from common.strings import Strings

class Globals:
    """
    Contains all global level contents, accessible in Pages & Tests
    """
    #Android Activities Names
    AUT_PACKAGE_NAME = 'org.edx.mobile'
    LAUNCH_ACTIVITY_NAME1 = '.view.LaunchActivity'
    SPLASH_ACTIVITY_NAME = '.view.SplashActivity'
    NEW_LOGISTRATION_ACTIVITY_NAME = '.view.DiscoveryLaunchActivity'
    LOGIN_ACTIVITY_NAME = '.view.LoginActivity'
    WHATS_NEW_ACTIVITY_NAME = '.whatsnew.WhatsNewActivity'
    VIEW_MY_COURSES_ACTIVITY_NAME = '.view.MyCoursesListActivity'
    REGISTER_ACTIVITY_NAME = '.view.RegisterActivity'
    DISCOVERY_ACTIVITY_NAME = '.view.WebViewFindCoursesActivity'

    def __init__(self):
        self.medium_timeout = 5
        self.maximum_timeout = 8
        self.minimum_timeout = 2
        self.flag = True
        #CAPABILITIES
        self.appium_remort_url = 'http://localhost:4723/wd/hub'
        self.ios_platform = Strings.IOS
        self.ios_platform_version = '10.3'
        self.ios_device_name = 'iPhone Simulator'
        self.and_platform = Strings.ANDROID
        self.and_platform_version = '8.0'
        self.and_device_name = 'Nexus 6P'
        self.app_package_name = 'org.edx.mobile'

    def validate_element(self, target_element, element_value, expected_value, error_msg):
        """
        Get element on screen and validate its visible value/label

        Arguments:
            target_element, element_value, expected_value, error_msg

        Return:
            Element
        """
        optimise_error = error_msg, 'Target - ', element_value, 'expected - ', expected_value
        if target_element is not None:
            if element_value == expected_value:
                print('Found - ', target_element, ' - ', target_element.tag_name, ' - ', element_value)
                return target_element
            else:
                print(Strings.ERROR_LABEL_NOT_MATCHING, target_element, ' - ', target_element.tag_name,
                      ' - ', element_value, ' - ', expected_value)
                return None
        else:
            print(Strings.ERROR_UTF_ELEMENT, ' - ', optimise_error, target_element, ' - ', target_element.tag_name)
            return None

    def get_all_text_views(self, driver):
        """
        Get list of Static Text Views on screen

        Argument:
            driver

        Return:
            List of Static Text Views
        """

        all_text_view = driver.find_elements_by_class_name(Elements.all_textviews)
        if all_text_view is not None:
            if len(all_text_view) > 0:
                print('Total ', len(all_text_view), 'Text Views found on screen')
                return all_text_view
            else:
                print('0 Text Views on screen')
        else:
            return None

    def get_all_edit_fields(self, driver):
        """
        Get list of Edit Text Fields on screen

        Argument:
            driver

        Return:
            List of Edit Text Fields
        """

        all_editfields = driver.find_elements_by_id(Elements.all_editfields)
        if all_editfields is not None:

                if len(all_editfields) > 0:
                    print('Total ', len(all_editfields), 'Edit Fields found on screen')
                    return all_editfields
                else:
                    print('0 Edit Fields on screen')
        else:
            return None

    def get_all_image_views(self, driver):
        """
        Get list of Images Views on screen

        Argument:
            driver

        Return:
            List of Images Views
        """

        all_imgages = driver.find_elements_by_class_name(Elements.all_images)
        if all_imgages is not None:

                if len(all_imgages) > 0:
                    print('Total ', len(all_imgages), 'Image Views found on screen')
                    return all_imgages
                else:
                    print('0 Image Views on screen')
        else:
            return None

    def get_all_image_buttons(self, driver):
        """
        Get list of Images Buttons on screen

        Argument:
            driver

        Return:
            List of Images Buttons
        """

        all_image_buttons = driver.find_elements_by_class_name(Elements.all_image_buttons)
        if all_image_buttons is not None:

                if len(all_image_buttons) > 0:
                    print('Total ', len(all_image_buttons), 'Image Buttons found on screen')
                    return all_image_buttons
                else:
                    print('0 Image Buttons on screen')
        else:
            return None

    def scroll_screen(self, driver, from_element, to_element):
        """
        Scroll from one element to other element on screen

        Arguments:
            from_element, to_element
        """
        sleep(self.minimum_timeout)
        print('Scrolling screen.')
        driver.scroll(from_element, to_element)
        sleep(self.minimum_timeout)

    def print_all_static_textviews_on_screen(self, driver):
        """
        Print list of Static Text views on console

        Argument:
            driver
        """

        all_textviews = driver.find_self.el_by_class_name(Elements.all_textviews)
        print('total ', len(all_textviews))
        for a in all_textviews:
            print('Tagname - ', a.tag_name, 'Label =', a.text, 'all = ', a)
