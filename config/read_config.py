import os
import configparser

cur_path = os.path.dirname(os.path.realpath(__file__))

config_path = os.path.join(cur_path, 'config.ini')

conf = configparser.ConfigParser()
conf.read(config_path)

brat_path = conf.get('config', 'brat_path')
ref_path = conf.get('config', 'crf_path')
brat_files = conf.items('brat_files')


