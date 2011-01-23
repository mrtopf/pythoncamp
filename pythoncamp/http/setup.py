import sys
import os
import pkg_resources
import logbook
import datetime

from quantumcore.storages import AttributeMapper
from pythoncamp.framework.utils import get_static_urlparser

def setup(**kw):
    """initialize the setup"""
    settings = AttributeMapper()
    settings['staticapp'] = get_static_urlparser(pkg_resources.resource_filename(__name__, 'static'))
    
    settings['secret_key'] = "ci28228zs7s8c6c8976c89c7s6s8976cs87d6" #os.urandom(20)
    settings['log'] = logbook.Logger("pythoncamp")
    settings.update(kw)
    return settings

