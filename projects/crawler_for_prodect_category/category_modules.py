#!/usr/bin/python3
import requests
import codecs
from modules import useragent
from modules import log
import json
from urllib.parse import urljoin, unquote
from lxml import etree
import pickle
import traceback
from tkinter import *
from tkinter import ttk
import tkinter.filedialog as filedialog
import queue
import threading


Logger = log.Logger('crawler.log', level='debug').logger
