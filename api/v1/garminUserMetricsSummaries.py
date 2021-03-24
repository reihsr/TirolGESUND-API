"""
Module for dealing with rest calls for the Garmin User Metrics Summaries
"""

from config import db, configsProperty, basedir
from models import GarminUserMetricsSummarie
import time
import uuid
import json
import os

def createGarminUserMetricsSummaries(garminUserMetricsSummaries):
    fileName = "garminUserMetricsSummaries_" + str(time.time()) + "_" + str(uuid.uuid4()) + ".json"
    filePath = os.path.join(configsProperty.get("FILE_STORAGE_PATH").data, fileName)
    with open(filePath, 'w') as outfile:
        json.dump(garminUserMetricsSummaries, outfile, indent=4)
    for garminUserMetricsSummarie in garminUserMetricsSummaries:
        createGarminUserMetricsSummarie(garminUserMetricsSummarie)
    return 200

def createGarminUserMetricsSummarie(garminUserMetricsSummarie):
    userMetrics = GarminUserMetricsSummarie.query.filter_by(summaryId=garminUserMetricsSummarie.get("summaryId")).first()
    if userMetrics == None:
        userMetrics = GarminUserMetricsSummarie()
        userMetrics.summaryId = garminUserMetricsSummarie.get("summaryId")
        db.session.add(userMetrics)
    userMetrics.userId = garminUserMetricsSummarie.get("userId")
    userMetrics.userAccessToken = garminUserMetricsSummarie.get("userAccessToken")
    userMetrics.calendarDate = garminUserMetricsSummarie.get("calendarDate")
    userMetrics.Vo2Max = garminUserMetricsSummarie.get("Vo2Max")
    userMetrics.fitnessAge = garminUserMetricsSummarie.get("fitnessAge")
    db.session.commit()
    return