from .chrome import chrome
from .firefox import firefox
from .mozilla import mozilla
from .opera import opera
from .safari import safari
import random


def get_user_agent(browser=''):
    browser = browser.lower()
    user_agent = {
        'chrome': chrome,
        'firefox': firefox,
        'mozilla': mozilla,
        'opera': opera,
        'safari': safari,
        'all': chrome + firefox + mozilla + opera + safari
    }

    if browser in user_agent:
        ua = random.choice(user_agent[browser])
    else:
        ua = random.choice(user_agent['all'])
    return ua

