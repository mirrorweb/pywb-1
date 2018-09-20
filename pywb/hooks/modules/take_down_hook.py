from pywb.utils.wbexception import *


class PyWBHook:
    """
    Hooks MUST have a class name of PyWBHook, the hooks system searches inside a module for a
    class of the name PyWBHook.

    A hook should have a pre_hook and/or a post_hook function.
    """

    def __init__(self, *args, **kwargs):
        """
        A unique self.name must be defined so that modules can be
        set and used in the config.yaml file.

        :args: A tuple of args that may be passed to the hook, currently this doesn't happen though.
        :kwargs: A dictionary of key word args that may be passed to the hook, currently this doesn't happen though.
        """

        self.name = 'take_down_hook'


    def pre_hook(self, fn_name, *args, **kwargs):
        """
        Pre-hooks are run before a response is evaluated.

        :fn_name: The name of the function that was hooked.
        :args: A tuple of arguments that would be passed into the function hooked.
        :kwargs: A dictionary of key word arguments that would be passed into the function hooked.
        """

        if not fn_name == 'process_cdx':
            print('\tDummy pre-hook')


    def post_hook(self, fn_name, response, *args, **kwargs):
        """
        Pre-hooks are run after a response is evaluated.

        :fn_name: The name of the function that was hooked.
        :response: The response returned by the hooked function after applying args and kwargs.
        :args: A tuple of arguments that would be passed into the function hooked.
        :kwargs: A dictionary of key word arguments that would be passed into the function hooked.
        """

        if not fn_name == 'process_cdx':
            return response

        disallowed_url = 'http://www.uk-techmap.com/Portals/11/Skins/UK_Techmap/images/menu_bg_off.gif'
        print('\tExample post-hook: Disallowing: {}'.format(disallowed_url))

        return (res for res in response if res['url'] != disallowed_url)
