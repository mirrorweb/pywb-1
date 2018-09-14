import importlib
from .modules import *


__all__ = ['HookManager']

_modules = dir()


class HookManager:
    __shared_state = {
        'module_names': [x for x in _modules if x.endswith('_hook')],
        'modules': [],
    }


    def __init__(self, config):
        self.__dict__ = self.__shared_state

        self.modules = [
            importlib.import_module(f'.{name}', 'pywb.hooks.modules').PyWBHook()
            for name in self.module_names
            if name in config.get('pre', []) or name in config.get('post', [])
        ]

