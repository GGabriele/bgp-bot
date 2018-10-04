import os
import yaml

from bgp_bot.helpers.napalm_helper import execute, open_session

BASE_PATH = os.path.dirname(__file__)
CONFIG = os.path.join(os.path.dirname(__file__), "../sample.yml")
DEVICE = "eos1"


class TestBot:
    """Wraps tests."""

    @classmethod
    def setup_class(cls):
        try:
            with open(CONFIG, "r") as f:
                cls.config = yaml.load(f.read())
        except IOError:
            print("Config file not found: ", CONFIG)

    def test_open_session(self):
        """Test open_session helper function."""
        device = open_session(DEVICE, self.config)
        assert device.is_alive()["is_alive"]

    def test_execute(self):
        """Test execute helper function."""
        facts = execute(DEVICE, self.config, "get_facts")
        assert facts.keys() == ["os_version",
                                "uptime",
                                "interface_list",
                                "vendor",
                                "serial_number",
                                "model",
                                "hostname",
                                "fqdn"]

#    def test_commit_config(self):
#        """Test commit_config helper function."""
#        pass
