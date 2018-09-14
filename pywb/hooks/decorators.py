from pywb.apps.wbrequestresponse import WbResponse
from pywb.hooks.hooks_manager import HookManager
from pywb.utils.loaders import load_yaml_config
from pywb.utils.wbexception import *


__all__ = ['hooked']


def hooked(disable_pre=False, disable_view=False, disable_post=False):
    def outer_wrapper(fn):
        def inner_wrapper(*args, **kwargs):
            try:
                # Just bail out if the view is disabled.
                if disable_view:
                    raise NotFoundException()

                config = load_yaml_config('./config.yaml').get('hooks', {})
                hook_manager = HookManager(config)

                if not disable_pre and config:
                    print('Running pre hooks:')
                    for hook in hook_manager.modules:
                        if hook.name in config.get('pre', []) and hasattr(hook, 'pre_hook'):
                            hook.pre_hook()

                response = fn(*args, **kwargs)

                if not disable_post and config:
                    print('Running post hooks:')
                    for hook in hook_manager.modules:
                        if hook.name in config.get('post', []) and hasattr(hook, 'post_hook'):
                            hook.post_hook(response)

                return response

            # Ensure all exceptions that CAN be thrown by hooks are handled here.
            except LiveResourceException as e:
                return WbResponse.text_response('Bad Live Resource', status='400 Bad Live Resource')

            except BadRequestException as e:
                return WbResponse.text_response('Bad Request', status='400 Bad Request')

            except AccessException as e:
                return WbResponse.text_response('Access Denied', status='403 Access Denied')

            except NotFoundException as e:
                return WbResponse.text_response('Not Found', status='404 Not Found')

            except LegallyUnavailableException as e:
                return WbResponse.text_response('Legally Unavailable', status='451 Unavailable For Legal Reasons')

        return inner_wrapper
    return outer_wrapper
