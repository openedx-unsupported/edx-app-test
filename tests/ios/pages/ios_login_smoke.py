"""
    Course Dashboard Test Module
"""

from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_whats_new import IosWhatsNew
from tests.common import strings
from tests.common.globals import Globals


class IosLoginSmoke:
    """
    Login Smoke Test cases

    """

    def test_check_login_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully after successful login
        """

        global_contents = Globals(setup_logging)
        whats_new_page = IosWhatsNew(set_capabilities, setup_logging)

        setup_logging.info(f'Starting {IosLoginSmoke.__name__} Test Case')
        if login:
            setup_logging.info(f'{global_contents.login_user_name} is successfully logged in')

        if strings.IS_FIRST_TIME and global_contents.whats_new_enable:
            assert whats_new_page.exit_features().text == strings.BLANK_FIELD
            strings.IS_FIRST_TIME = False
        else:
            main_dashboard_page = IosMainDashboard(set_capabilities, setup_logging)
            assert main_dashboard_page.get_drawer_icon().text == strings.MAIN_DASHBOARD_NAVIGATION_MENU_NAME
        setup_logging.info(f'{global_contents.login_user_name} is successfully logged in')
