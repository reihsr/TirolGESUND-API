"""
Module for dealing with rest calls for the Garmin Sleep Summaries
"""

from config import db, configsProperty, basedir
from models import GarminDailySummarie
import time
import uuid
import json
import os