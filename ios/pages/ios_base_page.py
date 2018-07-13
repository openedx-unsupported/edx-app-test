# coding=utf-8
"""
   Module covers iOS base page
"""

from common.globals import Globals


class IosBasePage(object):
    """
         Base page for all iOS Pages
    """

    def __init__(self, driver, setup_logging):
        self.driver = driver
        self.global_contents = Globals(setup_logging)
        self.log = setup_logging
        self.discovery_close_button = None
        self.textview_drawer_account_option = None
        self.account_options = None
        self.LOGOUT_OPTION = self.global_contents.fourth_existence
        self.discovery_cancel_button = None
