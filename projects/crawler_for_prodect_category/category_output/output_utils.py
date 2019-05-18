#!/usr/bin/python3
import time
from assets.log import log

Logger = log('crawler.log', level='debug').logger


def get_filename(filename, suffix):
    timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    return '%s_%s.%s' % (filename, timestamp, suffix)
