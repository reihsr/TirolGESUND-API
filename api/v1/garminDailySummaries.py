"""
Module for dealing with rest calls for the Garmin Daily Summaries
"""

from config import db, configsProperty, basedir
from models import GarminDailySummarie
import time
import uuid
import json
import os

def createGarminDailySummaries(garminDailySummaries):
    fileName = "garminDailySummaries_" + str(time.time()) + "_" + str(uuid.uuid4()) + ".json"
    filePath = os.path.join(configsProperty.get("FILE_STORAGE_PATH").data, fileName)
    with open(filePath, 'w') as outfile:
        json.dump(garminDailySummaries, outfile, indent=4)
    for garminDailySummarie in garminDailySummaries:
        createGarminDailySummarie(garminDailySummarie)
    return 200

def createGarminDailySummarie(garminDailySummarie):
    summary = GarminDailySummarie.query.filter_by(summaryId=garminDailySummarie.get("summaryId")).first()
    if summary == None:
        summary = GarminDailySummarie()
        summary.summaryId = garminDailySummarie.get("summaryId")
        db.session.add(summary)
    summary.userId = garminDailySummarie.get("userId")
    summary.userAccessToken = garminDailySummarie.get("userAccessToken")
    summary.calendarDate = garminDailySummarie.get("calendarDate")
    summary.startTimeInSeconds = garminDailySummarie.get("startTimeInSeconds")
    summary.startTimeOffsetInSeconds = garminDailySummarie.get("startTimeOffsetInSeconds")
    summary.activityType = garminDailySummarie.get("activityType")
    summary.durationInSeconds = garminDailySummarie.get("durationInSeconds")
    summary.steps = garminDailySummarie.get("steps")
    summary.distanceInMeters = garminDailySummarie.get("distanceInMeters")
    summary.activeTimeInSeconds = garminDailySummarie.get("activeTimeInSeconds")
    summary.activeKilocalories = garminDailySummarie.get("activeKilocalories")
    summary.bmrKilocalories = garminDailySummarie.get("bmrKilocalories")
    summary.consumedCalories = garminDailySummarie.get("consumedCalories")
    summary.moderateIntensityDurationInSeconds = garminDailySummarie.get("moderateIntensityDurationInSeconds")
    summary.vigorousIntensityDurationInSeconds = garminDailySummarie.get("vigorousIntensityDurationInSeconds")
    summary.floorsClimbed = garminDailySummarie.get("floorsClimbed")
    summary.minHeartRateInBeatsPerMinute = garminDailySummarie.get("minHeartRateInBeatsPerMinute")
    summary.averageHeartRateInBeatsPerMinute = garminDailySummarie.get("averageHeartRateInBeatsPerMinute")
    summary.maxHeartRateInBeatsPerMinute = garminDailySummarie.get("maxHeartRateInBeatsPerMinute")
    summary.restingHeartRateInBeatsPerMinute = garminDailySummarie.get("restingHeartRateInBeatsPerMinute")
    summary.timeOffsetHeartRateSamples = garminDailySummarie.get("timeOffsetHeartRateSamples")
    summary.averageStressLevel = garminDailySummarie.get("averageStressLevel")
    summary.maxStressLevel = garminDailySummarie.get("maxStressLevel")
    summary.stressDurationInSeconds = garminDailySummarie.get("stressDurationInSeconds")
    summary.restStressDurationInSeconds = garminDailySummarie.get("restStressDurationInSeconds")
    summary.activityStressDurationInSeconds = garminDailySummarie.get("activityStressDurationInSeconds")
    summary.lowStressDurationInSeconds = garminDailySummarie.get("lowStressDurationInSeconds")
    summary.mediumStressDurationInSeconds = garminDailySummarie.get("mediumStressDurationInSeconds")
    summary.highStressDurationInSeconds = garminDailySummarie.get("highStressDurationInSeconds")
    summary.stressQualifier = garminDailySummarie.get("stressQualifier")
    summary.stepsGoal = garminDailySummarie.get("stepsGoal")
    summary.netKilocaloriesGoal = garminDailySummarie.get("netKilocaloriesGoal")
    summary.intensityDurationGoalInSeconds = garminDailySummarie.get("intensityDurationGoalInSeconds")
    summary.floorsClimbedGoal = garminDailySummarie.get("floorsClimbedGoal")
    db.session.commit()
    return