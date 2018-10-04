import subprocess
import pytest
import os
import json


BASE_PATH = os.path.dirname(__file__)
CONFIG = os.path.join(os.path.dirname(__file__), "../../sample.yml")
DEVICES = ["eos1", "eos2"]
AS_MAP = {"eos1": 65001, "eos2": 65002}


def execute(command):
    """Execute a CLI command."""
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    return process.communicate()


class TestCliBot:
    """Wraps CLI tests."""

    @pytest.mark.parametrize('device', DEVICES)
    def test_show_neighbors_empty(self, device):
        """Test to ensure devices have no neighbors."""
        command_line = [
            "bgp-bot",
            "--config", CONFIG,
            "show",
            device,
            "--neighbors"
        ]
        print execute(command_line)
        output = json.loads(execute(command_line)[0])
        assert not output

    @pytest.mark.parametrize('device', DEVICES)
    def test_show_bgp_config_empty(self, device):
        """Test to ensure devices have no bgp config."""
        command_line = [
            "bgp-bot",
            "--config", CONFIG,
            "show",
            device,
            "--bgp-config"
        ]
        print execute(command_line)
        output = json.loads(execute(command_line)[0])
        assert not output

    @pytest.mark.parametrize('device', DEVICES)
    def test_deploy_bgp_config(self, device):
        """Test deploy bgp config."""
        command_line = [
            "bgp-bot",
            "--config", CONFIG,
            "deploy",
            device
        ]
        execute(command_line)
        command_line = [
            "bgp-bot",
            "show",
            device,
            "--bgp-config"
        ]
        print execute(command_line)
        output = json.loads(execute(command_line)[0])
        assert output["_"]["local_as"] == AS_MAP[device]

#    @pytest.mark.parametrize('device', DEVICES)
#    def test_show_neighbors(self, device):
#        """Test neighbors are correctly set."""
