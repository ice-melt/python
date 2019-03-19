#!/usr/bin/python3
import time
from modules import log

Logger = log.Logger('crawler.log', level='debug').logger

def get_filename(filename, suffix):
    timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    return '%s_%s.%s' % (filename, timestamp, suffix)
