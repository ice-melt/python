from .chrome import chrome
from .firefox import firefox
from .mozilla import mozilla
from .opera import opera
from .safari import safari
import random

def getUserAgent(browser=''):
    browser = browser.lower()
    userAgent = {
        'chrome': chrome,
        'firefox': firefox,
        'mozilla': mozilla,
        'opera': opera,
        'safari': safari,
        'all': chrome + firefox + mozilla + opera + safari
    }
    #if browser == 'chrome' or browser == 'firefox' or browser == 'mozilla' or browser == 'opera' or browser == 'safari':
    if browser in userAgent:
        ua = random.choice(userAgent[browser])
    else:
        ua = random.choice(userAgent['all'])
    return ua

