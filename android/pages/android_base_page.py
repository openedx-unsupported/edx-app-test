# coding=utf-8
"""
   Module covers Android base page
"""

from common.globals import Globals


class AndroidBasePage(object):
    """
     Base page for all Android Pages
    """

    def __init__(self, driver, setup_logging):
        self.driver = driver
        self.global_contents = Globals(setup_logging)
        self.log = setup_logging
        self.textview_drawer_account_option = None
        self.global_contents.flag = False
        self.account_logout_option = None
        self.target_activity = None
