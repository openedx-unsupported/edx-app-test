"""
    Register Page Module
"""
from android.pages import android_elements
from android.pages.android_base_page import AndroidBasePage
from android.pages.android_new_landing import AndroidNewLanding
from common.globals import Globals


class AndroidRegister(AndroidBasePage):
    """
    Register screen
    """

    def on_screen(self):
        """
        Load Register screen

        Returns:
            str: Register Activity Name
        """

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.REGISTER_ACTIVITY_NAME
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

    def get_register_divider_textview(self):
        """
        Get Register With Divider

        Returns:
              webdriver element: Register With Divider Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_divider_textview
        )

    def get_facebook_textview(self):
        """
        Get Facebook

        Returns:
              webdriver element: Facebook Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_facebook_textview
        )

    def get_google_textview(self):
        """
        Get Google

        Returns:
              webdriver element: Google Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_google_textview
        )

    def get_register_with_email_divider_textview(self):
        """
        Get Register With Email Divider

        Returns:
              webdriver element: Register With Email Divider Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_with_email_divider_textview
        )

    def get_email_editfield(self):
        """
        Get Email

        Returns:
              webdriver element: Email Element
        """
        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.register_all_editfields)[self.global_contents.first_existence]

    def get_email_instructions_textview(self):
        """
        Get Email Instructions

        Returns:
              webdriver element: Email Instructions Element
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.register_input_instruction_all_textviews)[self.global_contents.first_existence]

    def get_full_name_editfield(self):
        """
        Get Full Name

        Returns:
              webdriver element: Full Name Element
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.register_all_editfields)[self.global_contents.second_existence]

    def get_full_name_instructions_textview(self):
        """
        Get Full Name Instructions

        Returns:
              webdriver element: Full Name Instructions Element
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.register_input_instruction_all_textviews)[self.global_contents.second_existence]

    def get_user_name_editfield(self):
        """
        Get User Name

        Returns:
              webdriver element: User Name Element
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.register_all_editfields)[self.global_contents.third_existence]

    def get_user_name_instructions_textview(self):
        """
        Get User Name Instructions

        Returns:
              webdriver element: User Name Instructions Element
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.register_input_instruction_all_textviews)[self.global_contents.third_existence]

    def get_password_editfield(self):
        """
        Get Password

        Returns:
              webdriver element: Password Element
        """
        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.register_all_editfields)[self.global_contents.fourth_existence]

    def get_password_instructions_textview(self):
        """
        Get Password Instructions

        Returns:
              webdriver element: Password Instructions Element
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.register_input_instruction_all_textviews)[self.global_contents.fourth_existence]

    def get_country_spinner(self):
        """
        Get Country Spinner

        Returns:
              webdriver element: Country Spinner Element
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.register_all_spinners)[self.global_contents.first_existence]

    def get_country_spinner_instructions_textview(self):
        """
        Get Country Spinner Instructions

        Returns:
              webdriver element: Country Spinner Instructions Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_country_instructions_textview
        )

    def get_show_optional_fields_textview(self):
        """
        Get Show Option Fields

        Returns:
              webdriver element: Show Option Fields Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_show_optional_fields_textview
        )

    def get_gender_spinner(self):
        """
        Get Gender Spinner

        Returns:
              webdriver element: Gender Spinner Element
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.register_all_spinners)[self.global_contents.second_existence]

    def get_year_of_birth_spinner(self):
        """
        Get Year Of Birth Spinner

        Returns:
              webdriver element: Year Of Birth Spinner Element
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.register_all_spinners)[self.global_contents.third_existence]

    def get_eduction_spinner(self):
        """
        Get Education Spinner

        Returns:
              webdriver element: Education Spinner Element
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.register_all_spinners)[self.global_contents.fourth_existence]

    def get_why_interested_editfield(self):
        """
        Get Why Interested editfield

        Returns:
              webdriver element: Why Interested editfield Element
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.register_all_editfields)[self.global_contents.first_existence]

    def get_create_my_account_textview(self):
        """
        Get Create My Account Textview

        Returns:
              webdriver element: Create My Account Element
        """

        self.global_contents.scroll_from_element(self.driver, self.get_password_editfield())

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_create_my_account_textview
        )

    def get_agreement_textview(self):
        """
        Get Agree Textview

        Returns:
              webdriver element: Agree Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_agreement_textview
        )

    def load_eula_screen(self):
        """
        Load EULA screen and get back to Login Screen

        Returns:
             bool: Returns True if app is back on Login screen from EULA
        """
        self.global_contents.scroll_from_element(self.driver, self.get_password_editfield())

        self.global_contents.get_element_coordinates(self.driver, android_elements.register_agreement_textview)

        target_x_position = self.global_contents.element_x_position + int(
            self.global_contents.element_width / 2) + 200

        target_y_position = self.global_contents.element_y_position + int(self.global_contents.element_height / 4)

        return self.navigate_eula(target_x_position, target_y_position)

    def load_terms_screen(self):
        """
        Load Terms screen and get back to Login Screen

        Returns:
             bool: Returns True if app is back on Login screen from Terms
        """

        self.global_contents.get_element_coordinates(self.driver, android_elements.register_agreement_textview)

        target_x_position = self.global_contents.element_x_position + int(self.global_contents.element_width / 2)
        target_y_position = self.global_contents.element_y_position + int(self.global_contents.element_height / 2)

        return self.navigate_eula(target_x_position, target_y_position)

    def load_privacy_screen(self):
        """
        Load Privacy screen and get back to Login Screen

        Returns:
             bool: Returns True if app is back on Login screen from Privacy
        """

        self.global_contents.get_element_coordinates(self.driver, android_elements.register_agreement_textview)

        target_x_position = self.global_contents.element_x_position + int(
            self.global_contents.element_width / 2) + 100
        target_y_position = self.global_contents.element_y_position + int(
            self.global_contents.element_height / 2) + 38

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
            if self.driver.current_activity == Globals.REGISTER_ACTIVITY_NAME:
                self.log.info('Register screen is successfully loaded')
            else:
                self.log.error('Register screen is not loaded')
                self.global_contents.flag = False
        else:
            self.log.error('EULA screen is not loaded')
            self.global_contents.flag = False

        return self.global_contents.flag

    def show_hide_optional_fields(self):
        """
        Show optional fields

        Returns:
              Webdriver element: Show/Hide Element
        """

        show_hide_optional_fields = self.get_show_optional_fields_textview()
        show_hide_optional_fields.click()

        self.global_contents.scroll_from_element(self.driver, show_hide_optional_fields)

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_show_optional_fields_textview
        )

    def back_and_forth_register(self):
        """
        Load register screen and get back to previous screen

        Returns:
             bool: Returns True if app is back on Register screen
        """

        android_new_landing_page = AndroidNewLanding(self.driver, self.log)

        if self.driver.current_activity == Globals.REGISTER_ACTIVITY_NAME:
            self.driver.back()

            if (self.driver.current_activity == Globals.DISCOVERY_LAUNCH_ACTIVITY_NAME and
                    android_new_landing_page.load_register_screen() == Globals.REGISTER_ACTIVITY_NAME):
                self.log.info('Register screen is successfully loaded')
            else:
                self.log.error('New Landing screen is not loaded')
                self.global_contents.flag = False
        else:
            self.log.error('Register screen is not loaded')
            self.global_contents.flag = False

        return self.global_contents.flag

    def register(self, email, full_name, user_name, password, country):
        """
        Register with given credentials

        Arguments:
            email (str): email
            full_name (str): full name
            user_name (str): username
            password (str): password
            country (str): country

        Returns:
            str: Whats New Activity Name
        """

        self.get_email_editfield().send_keys(email)
        self.driver.hide_keyboard()

        self.get_full_name_editfield().send_keys(full_name)
        self.driver.hide_keyboard()

        self.get_user_name_editfield().send_keys(user_name)
        self.driver.hide_keyboard()

        self.get_password_editfield().send_keys(password)
        self.driver.hide_keyboard()

        self.select_country(country)

        self.get_create_my_account_textview().click()

        return self.global_contents.wait_for_android_activity_to_load(
            self.driver,
            self.global_contents.WHATS_NEW_ACTIVITY_NAME
        )

    def select_country(self, value):
        """
        Navigate and select specific country in spinner

        Arguments:
            value (str): country value
        """

        self.get_country_spinner().click()

        fetched_countries = []
        total_expected_countries = 300
        countries_per_page = 10
        x = 0
        self.global_contents.flag = True

        for scroll in range(int(total_expected_countries/countries_per_page)):
            countries_list_values = self.get_all_textviews_in_listview()
            self.log.info('countries list - {}'.format(len(countries_list_values)))

            for country in countries_list_values:
                self.log.info('{} - {} - {} - {}'.format(
                    x,
                    country,
                    country.tag_name,
                    country.text
                ))
                fetched_countries.append(country.text)
                x += 1
                if country.text == value:
                    self.log.info('matching {} - country found, clicking - {}'.format(
                        value,
                        country.text))

                    country.click()
                    self.global_contents.flag = False
                    break

            if self.global_contents.flag:
                self.log.info('scrolling - {}'.format(scroll))
                self.global_contents.scroll_screen(self.driver, countries_list_values[10], countries_list_values[1])
            else:
                break

        self.log.info(fetched_countries)

        selected_values = self.get_selected_textview_in_spinner(self.get_country_spinner())
        self.log.info('New selected spinner value - {}'.format(
            selected_values[self.global_contents.first_existence].text))

    def get_all_textviews_in_listview(self):
        """
        Get all texts in list view

         Returns:
            list: list of text views
        """

        countries_list_container = self.driver.find_elements_by_class_name(android_elements.all_listviews)

        countries_list_values = countries_list_container[
            self.global_contents.fourth_existence].find_elements_by_class_name(android_elements.all_textviews)
        countries = len(countries_list_values)
        if countries > 0:
            self.log.info('Total - {} text views found in list view'.format(
                len(countries_list_values)
            ))
            return countries_list_values
        else:
            self.log.info('0 text views found in list view')
            return None

    def get_selected_textview_in_spinner(self, spinner):
        """
        Get selected value in spinner

         Returns:
            text: selected value
        """

        texts = spinner.find_elements_by_class_name(android_elements.all_textviews)
        if texts is not None:

            country = len(texts)
            if country > 0:
                self.log.info('Total {} text views found in spinner'.format(len(texts)))
                return texts
            else:
                self.log.info('0 text views found in spinner')

        else:
            return None

    def validate_required_optional_fields(self):
        """
        validate required fields

        Returns:
             bool: Returns True if Registration Error is visible
        """

        self.global_contents.scroll_from_element(self.driver, self.get_password_editfield())
        self.get_create_my_account_textview().click()

        output = self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.register_error_alert_title_textview
        )

        if output:
            self.global_contents.wait_and_get_element(
                self.driver,
                android_elements.register_error_alert_title_textview
            )
            self.global_contents.wait_and_get_element(
                self.driver,
                android_elements.register_error_alert_textview
            )
            wrong_credentials_alert_ok = self.global_contents.wait_and_get_element(
                self.driver,
                android_elements.register_error_alert_button
            )
            wrong_credentials_alert_ok.click()

            return True

        else:
            return False

    def get_email_validation_textview(self):
        """
        Get Email validation Textview

        Returns:
              Webdriver element: Email validation Element
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.register_validate_editfield_error_textview
            )[self.global_contents.first_existence]

    def get_full_name_validation_textview(self):
        """
        Get Full Name validation Textview

        Returns:
              Webdriver element: Full Name validation Element
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.register_validate_editfield_error_textview)[self.global_contents.second_existence]

    def get_username_validation_textview(self):
        """
        Get Username validation Textview

        Returns:
              Webdriver element: Username validation Element
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.register_validate_editfield_error_textview)[self.global_contents.third_existence]

    def get_password_validation_textview(self):
        """
        Get Password validation Textview

        Returns:
              Webdriver element: Password validation Element
        """

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.register_validate_editfield_error_textview)[self.global_contents.fourth_existence]

    def get_country_validation_textview(self):
        """
        Get Country validation Textview

        Returns:
              Webdriver element: Country validation Element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_validate_spinner_error_textview
        )
