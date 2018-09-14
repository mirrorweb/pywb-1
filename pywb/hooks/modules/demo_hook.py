from pywb.utils.wbexception import *


class PyWBHook:
    """
    PyWBHook modules that are called when a resource is being requested.
    These classes MUST be called PyWBHook and they may contain either a pre_hook
    function or a post_hook function or both. These functions are used to determine
    the behaviour to perform before a response is made and after.

    Additionally the class must define a name attribute which can be used in the
    config file to enable/disable the module.
    """
    def __init__(self):
        self.name = 'demo_hook'


    def pre_hook(self):
        """
        Function used to perform pre-hook functionality upon a request.
        """
        print('\tDemo pre-hook')


    """
    def pre_hook(self):
        print('\tDemo pre-hook with 404 exception')
        raise NotFoundException()
    """


    def post_hook(self, response):
        """
        Function used to perform post-hook functionality upon a request.
        """
        print('\tDemo post-hook')


    """
    def pre_hook(self):
        print('\tDemo pre-hook with 451 exception')
        # raise LegallyUnavailableException()
    """

