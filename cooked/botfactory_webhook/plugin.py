
from DivvyUtils.field_definition import StringField, MultiSelectionField, FieldOptions, BooleanField
from DivvyUtils.flask_helpers import JsonResponse

from botfactory.registry import BotFactoryAction, ActionRegistry
from DivvyInterfaceMessages import ResourceConverters
import thread
import urllib2
from DivvyDb.DivvyDb import SharedSessionScope
from DivvyDb.DivvyCloudGatewayORM import DivvyCloudGatewayORM
import simplejson as json


from DivvyPlugins.plugin_metadata import PluginMetadata


class metadata(PluginMetadata):
    """
    Information about this plugin
    """
    version = '1.0'
    last_updated_date = '2016-03-18'
    author = 'Divvy Cloud Corp.'
    nickname = 'WebHook Bot Action'
    default_language_description = 'Webhook action for BotFactory.'
    support_email = 'support@divvycloud.com'
    support_url = 'http://support.divvycloud.com'
    main_url = 'http://www.divvycloud.com'
    category = 'Actions'
    managed = False
    divvy_api_version = "16.01"



@SharedSessionScope(DivvyCloudGatewayORM)
def call_webhook(event, current_bot, settings):
    """
    Call URL with event information.
    The URL call is threaded off to prevent blocking.
    :param event:
    :param current_bot:
    :param settings:
    :return:
    """

    event_json = json.dumps(event)
    url = settings['url']
    thread.start_new_thread(urllib2.urlopen,(url,),{"data": event_json})



ACTIONS = [
    BotFactoryAction(
        uid='divvy.action.webhook',
        name='WebHook',
        description='Make Rest Call',
        author='DivvyCloud Inc.',
        supported_resources=[],
        settings_config=[
            StringField(
                name='url',
                display_name='URL',
                description="Call URL with JSON representation of resource",
                options=FieldOptions.REQUIRED
            ),
        ],
        function=call_webhook
    )
]

def load():
    ActionRegistry().registry.register(ACTIONS)


def unload():
    ActionRegistry().registry.unregister(ACTIONS)
