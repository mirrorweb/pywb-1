from pywb.hooks.hooks_manager import HookManager
from pywb.utils.loaders import load_yaml_config


__all__ = ['hooked']


def hooked(disable_pre=False, disable_post=False):
    """
    :disable_pre: Disables the pre-hooks on this function.
    :disable_post: Disables the post-hooks on this function.
    """

    def outer_wrapper(fn):
        """
        :fn: The function to be decorated.
        """

        def inner_wrapper(*args, **kwargs):
            """
            :args: The args that will be applied to fn.
            :kwargs: The kwargs that will be applied to fn.
            """

            config = load_yaml_config('./config.yaml').get('hooks', {})
            hook_manager = HookManager(config)

            if not disable_pre and config:
                for hook in hook_manager.modules:
                    if hook.name in config.get('pre', []) and hasattr(hook, 'pre_hook'):
                        hook.pre_hook(fn.__name__, *args, **kwargs)

            response = fn(*args, **kwargs)

            if not disable_post and config:
                for hook in hook_manager.modules:
                    if hook.name in config.get('post', []) and hasattr(hook, 'post_hook'):
                        # Make sure we modify the response else post hooks will have no effect.
                        response = hook.post_hook(fn.__name__, response, *args, **kwargs)

            return response
        return inner_wrapper
    return outer_wrapper

