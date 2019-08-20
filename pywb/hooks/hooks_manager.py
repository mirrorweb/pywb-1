import importlib
from .modules import *


__all__ = ['HookManager']

"""
Apparently calling dir() from inside a class only gets the
attributes of that class and not anything imported in the
top level module.
"""

_modules = dir()


class HookManager:
    """
    This HookManager class is used to dynamically load the hooks,
    please ensure that hook files are inside 'modules' and have a name ending
    with '_hook'.

    It uses the Borg model to ensure that all instances of a HookManager share
    the same state.
    """

    __shared_state = {
        'module_names': [x for x in _modules if x.endswith('_hook')],
        'modules': [],
    }


    def __init__(self, config):
        """
        :config: The config dictionary.
        """

        self.__dict__ = self.__shared_state

        self.modules = [
            importlib.import_module(f'.{name}', 'pywb.hooks.modules').PyWBHook()
            for name in self.module_names
            if name in config.get('pre', []) or name in config.get('post', [])
        ]

