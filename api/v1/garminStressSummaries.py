"""
Module for dealing with rest calls for the Garmin Stress Summaries
"""

from config import db, configsProperty, basedir
from models import GarminStressSummarie
import time
import uuid
import json
import os

def createGarminStressSummaries(garminStressSummaries):
    fileName = "garminStressSummaries_" + str(time.time()) + "_" + str(uuid.uuid4()) + ".json"
    filePath = os.path.join(configsProperty.get("FILE_STORAGE_PATH").data, fileName)
    with open(filePath, 'w') as outfile:
        json.dump(garminStressSummaries, outfile, indent=4)
    for garminStressSummarie in garminStressSummaries:
        createGarminStressSummarie(garminStressSummarie)
    return 200

def createGarminStressSummarie(garminStressSummarie):
    stress = GarminStressSummarie.query.filter_by(summaryId=garminStressSummarie.get("summaryId")).first()
    if stress == None:
        stress = GarminStressSummarie()
        stress.summaryId = garminStressSummarie.get("summaryId")
        db.session.add(stress)
    stress.calendarDate = garminStressSummarie.get("calendarDate")
    stress.startTimeInSeconds = garminStressSummarie.get("startTimeInSeconds")
    stress.startTimeOffsetInSeconds = garminStressSummarie.get("startTimeOffsetInSeconds")
    stress.durationInSeconds = garminStressSummarie.get("durationInSeconds")
    stress.timeOffsetStressLevelValues = garminStressSummarie.get("timeOffsetStressLevelValues")
    stress.timeOffsetBodyBatteryValues = garminStressSummarie.get("timeOffsetBodyBatteryValues")
    db.session.commit()
    return