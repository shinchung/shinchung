from re import S
from napalm import get_network_driver
import json
import yaml

driver = get_network_driver('ios')

with open('inventory.yml') as f:
    devices = yaml.load(f, Loader=yaml.SafeLoader)
    for device in devices:
        conn = d

# device = driver(**)