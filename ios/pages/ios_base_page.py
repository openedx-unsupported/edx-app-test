from common.globals import Globals


class IosBasePage(object):

    def __init__(self, driver, setup_logging):
        self.driver = driver
        self.global_contents = Globals(setup_logging)
        self.log = setup_logging
