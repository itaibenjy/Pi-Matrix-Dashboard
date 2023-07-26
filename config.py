# config.py
import yaml

class Config:
    with open('config.yml', 'r') as f:
        data = yaml.safe_load(f)

