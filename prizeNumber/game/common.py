import requests
import re
from lxml import etree
import datetime
import sys
from utils import configureRead


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/52.0.2743.116 Safari/537.36'}
UTC_FORMAT = '%Y-%m-%d %H:%M:%S'
date_format = '%Y-%m-%d'
