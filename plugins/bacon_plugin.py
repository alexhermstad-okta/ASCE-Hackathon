from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
import requests

class BaconPlugin(WillPlugin):

    @respond_to("get results")
    def say_bonjour_will(self, message):
        import requests
        r = requests.post('http://10.20.197.218:8888/bacon', json={"sha": "aa347fc983f6cc578a2731b9nc4240e3b4a1e156"})
        self.reply(message, r)
