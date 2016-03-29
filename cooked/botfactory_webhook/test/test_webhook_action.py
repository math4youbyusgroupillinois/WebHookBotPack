import time

from botfactory.test.utils import BotTestCase
from DivvyDb import DivvyDbObjects
from botfactory_webhook import plugin
from DivvyDb import DivvyCloudGatewayORM
from DivvyDb.DivvyDb import SharedSessionScope


class WebHookTest(BotTestCase):
    @SharedSessionScope(DivvyCloudGatewayORM.DivvyCloudGatewayORM)
    def get_fake_resource(self):
        db = DivvyCloudGatewayORM.DivvyCloudGatewayORM()
        instance_db_object = DivvyDbObjects.Instance("i-asdsdfas", 1, 1, 'running', 'blah', 'us-east-1', 'us-east-1a',
                                                     '2015-01-01T11:11:11.111Z', 'Linux')
        db.session.add(instance_db_object)
        return instance_db_object.get_resource()

    @SharedSessionScope(DivvyCloudGatewayORM.DivvyCloudGatewayORM)
    def test_webhook(self):
        self.settings = {
            "url": "http://localhost:3000"
        }

        plugin.call_webhook(self.fake_event, self.fake_bot, self.settings)

        # Because the URL call is threaded off, we want to give it a moment to do what it needs to do
        # Otherwise the application finishes prior to the URL call being made
        time.sleep(1)
