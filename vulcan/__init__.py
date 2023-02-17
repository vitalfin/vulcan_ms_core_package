"""Vulcan Microservice Core Library"""
import datetime
import os 

version = os.getenv("VERSION")
if version is None:
  version = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M")
__version__ = versio