"""
Module for dealing with rest calls for the Garmin Sleep Summaries
"""

from config import db, configsProperty, basedir
from models import GarminSleepSummarie
import time
import uuid
import json
import os

def createGarminSleepSummaries(garminSleepSummaries):
    fileName = "garminSleepSummaries_" + str(time.time()) + "_" + str(uuid.uuid4()) + ".json"
    filePath = os.path.join(configsProperty.get("FILE_STORAGE_PATH").data, fileName)
    with open(filePath, 'w') as outfile:
        json.dump(garminSleepSummaries, outfile, indent=4)
    for garminSleepSummarie in garminSleepSummaries.get("sleeps"):
        createGarminSleepSummarie(garminSleepSummarie)
    return 200

def createGarminSleepSummarie(garminSleepSummarie):
    sleep = GarminSleepSummarie.query.filter_by(summaryId=garminSleepSummarie.get("summaryId")).first()
    if sleep == None:
        sleep = GarminSleepSummarie()
        sleep.summaryId = garminSleepSummarie.get("summaryId")
        db.session.add(sleep)
    sleep.userId = garminSleepSummarie.get("userId")
    sleep.userAccessToken = garminSleepSummarie.get("userAccessToken")
    sleep.calendarDate = garminSleepSummarie.get("calendarDate")
    sleep.startTimeInSeconds = garminSleepSummarie.get("startTimeInSeconds")
    sleep.startTimeOffsetInSeconds = garminSleepSummarie.get("startTimeOffsetInSeconds")
    sleep.durationInSeconds = garminSleepSummarie.get("durationInSeconds")
    sleep.unmeasurableSleepInSeconds = garminSleepSummarie.get("unmeasurableSleepInSeconds")
    sleep.deepSleepDurationInSeconds = garminSleepSummarie.get("deepSleepDurationInSeconds")
    sleep.lightSleepDurationInSeconds = garminSleepSummarie.get("lightSleepDurationInSeconds")
    sleep.remSleepInSeconds = garminSleepSummarie.get("remSleepInSeconds")
    sleep.awakeDurationInSeconds = garminSleepSummarie.get("awakeDurationInSeconds")
    sleep.sleepLevelsMap = garminSleepSummarie.get("sleepLevelsMap")
    sleep.validation = garminSleepSummarie.get("validation")
    sleep.timeOffsetSleepRespiration = garminSleepSummarie.get("timeOffsetSleepRespiration")
    sleep.timeOffsetSleepSpo2 = garminSleepSummarie.get("timeOffsetSleepSpo2")
    db.session.commit()
    return