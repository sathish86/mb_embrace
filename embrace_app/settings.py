# project settings loader
import os
import importlib
APP_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# You can key the configurations off of anything - I use project path.
configs = {
    '/home/sathish/Projects/workspace/data_embrace/embrace_app': 'local_settings',
    'E:\\Workspace\\data_embrace\\embrace_app': 'settings_test',
    '/opt/test/data_embrace/embrace_app': 'settings_test',
    '/opt/prod/data_embrace/embrace_app': 'settings_prod',
}

# Import the configuration settings file
if configs.get(APP_PATH, None):
    config_module = __import__('conf.%s' % configs[APP_PATH], globals(), locals(), 'data_embrace')

    # Load the config settings properties into the local scope.
    for setting in dir(config_module):
        if setting == setting.upper():
            locals()[setting] = getattr(config_module, setting)


SETTING_ENVIRONMENT_VARIABLE = 'MB_SETTINGS_MODULE'
# Import settings module and copy settings (all caps settings only)

# Import the configuration settings file
if os.environ.get(SETTING_ENVIRONMENT_VARIABLE, None):
    module_name = os.environ[SETTING_ENVIRONMENT_VARIABLE]
    mod = __import__('%s' % module_name, globals(), locals())

    for setting in dir(mod):
        if setting.isupper():
            locals()[setting] = getattr(mod, setting)
