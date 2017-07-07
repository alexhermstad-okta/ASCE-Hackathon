from will.plugin import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template, require_settings
import requests

class BaconPlugin(WillPlugin):
    @respond_to("get results from (?P<sha>.*)")
    def say_bonjour_will(self, message, sha):
        r = requests.post('http://10.20.197.218:8888/bacon', verify=False, json = {
        "sha": sha
        })

        self.reply(message, str(r.text))

