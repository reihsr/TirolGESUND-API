"""
Module for dealing with rest calls for the Garmin Daily Summaries
"""

from flask import make_response, abort
from config import db
from models import GarminDailySummarie

def createGarminDailySummaries(garminDailySummaries):
    print(garminDailySummaries)
    print(garminDailySummaries[0].get("timeOffsetHeartRateSamples"))
    return 200