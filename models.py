from datetime import datetime
from config import db, ma
import sqlalchemy

class Participant(db.Model):
    __tablename__ = "participant"
    study_id = db.Column('study_id', db.String(100), primary_key=True)
    study = db.Column('study', db.String(100))
    oauth_token = db.Column(db.String(100))
    oauth_token_secret = db.Column(db.String(100))
    oauth_verifier = db.Column(db.String(100))
    authorization_redirect_url = db.Column(db.String(500))
    user_oauth_token = db.Column(db.String(100))
    user_oauth_token_secret = db.Column(db.String(100))
    create_date = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class ParticipantSchema(ma.Schema):
    class Meta:
        model = Participant
        sqla_session = db.session

class GarminDailySummarie(db.Model):
    __tablename__ = "daily_summarie"
    summaryId = db.Column('summary_id', db.String(100), primary_key=True)
    userId = db.Column('user_id', db.String(100))
    userAccessToken = db.Column('user_access_token', db.String(100))
    calendarDate = db.Column('calendar_date', db.String(100))
    startTimeInSeconds = db.Column('start_time_in_seconds', db.Integer)
    startTimeOffsetInSeconds = db.Column('start_time_offset_in_seconds', db.Integer)
    activityType = db.Column('activity_type', db.String(100))
    durationInSeconds = db.Column('duration_in_seconds', db.Integer)
    steps = db.Column('steps', db.Integer)
    distanceInMeters = db.Column('distance_in_meters', db.Float)
    activeTimeInSeconds = db.Column('active_time_in_seconds', db.Integer)
    activeKilocalories = db.Column('active_kilocalories', db.Integer)
    bmrKilocalories = db.Column('bmr_kilocalories', db.Integer)
    consumedCalories = db.Column('consumed_calories', db.Integer)
    moderateIntensityDurationInSeconds = db.Column('moderate_intensity_duration_in_seconds', db.Integer)
    vigorousIntensityDurationInSeconds = db.Column('vigorous_intensity_duration_in_seconds', db.Integer)
    floorsClimbed = db.Column('floors_climbed', db.Integer)
    minHeartRateInBeatsPerMinute = db.Column('min_heart_rate_in_beats_per_minute', db.Integer)
    averageHeartRateInBeatsPerMinute = db.Column('average_heart_rate_in_beats_per_minute', db.Integer)
    maxHeartRateInBeatsPerMinute = db.Column('max_heart_rate_in_beats_per_minute', db.Integer)
    restingHeartRateInBeatsPerMinute = db.Column('resting_heart_rate_in_beats_per_minute', db.Integer)
    timeOffsetHeartRateSamples = db.Column('time_offset_heart_rate_samples', sqlalchemy.dialects.postgresql.JSONB)
    averageStressLevel = db.Column('average_stress_level', db.Integer)
    maxStressLevel = db.Column('max_stress_level', db.Integer)
    stressDurationInSeconds = db.Column('stress_duration_in_seconds', db.Integer)
    restStressDurationInSeconds = db.Column('rest_stress_duration_in_seconds', db.Integer)
    activityStressDurationInSeconds = db.Column('activity_stress_duration_in_seconds', db.Integer)
    lowStressDurationInSeconds = db.Column('low_stress_duration_in_seconds', db.Integer)
    mediumStressDurationInSeconds = db.Column('medium_stress_duration_in_seconds', db.Integer)
    highStressDurationInSeconds = db.Column('high_stress_duration_in_seconds', db.Integer)
    stressQualifier = db.Column('stress_qualifier', db.String)
    stepsGoal = db.Column('steps_goal', db.Integer)
    netKilocaloriesGoal = db.Column('net_kilocalories_goal', db.Integer)
    intensityDurationGoalInSeconds = db.Column('intensity_duration_goal_in_seconds', db.Integer)
    floorsClimbedGoal = db.Column('floors_climbed_goal', db.Integer)

class GarminDailySummarieSchema(ma.Schema):
    class Meta:
        model = GarminDailySummarie
        sqla_session = db.session

class GarminSleepSummarie(db.Model):
    __tablename__ = "sleep_summarie"
    summaryId = db.Column('summary_id', db.String(100), primary_key=True)
    userId = db.Column('user_id', db.String(100))
    userAccessToken = db.Column('user_access_token', db.String(100))
    calendarDate = db.Column('calendar_date', db.String(100))
    startTimeInSeconds = db.Column('start_time_in_seconds', db.Integer)
    startTimeOffsetInSeconds = db.Column('start_time_offset_in_seconds', db.Integer)
    durationInSeconds = db.Column('duration_in_seconds', db.Integer)
    unmeasurableSleepInSeconds = db.Column('unmeasurable_sleep_in_seconds', db.Integer)
    deepSleepDurationInSeconds = db.Column('deep_sleep_duration_in_seconds', db.Integer)
    lightSleepDurationInSeconds = db.Column('light_sleep_duration_in_seconds', db.Integer)
    remSleepInSeconds = db.Column('rem_sleep_in_seconds', db.Integer)
    awakeDurationInSeconds = db.Column('awake_duration_in_seconds', db.Integer)
    sleepLevelsMap = db.Column('sleep_levels_map', sqlalchemy.dialects.postgresql.JSONB)
    validation = db.Column('validation', db.String)
    timeOffsetSleepRespiration = db.Column('time_offset_sleep_respiration', sqlalchemy.dialects.postgresql.JSONB)
    timeOffsetSleepSpo2 = db.Column('time_offset_sleep_spo2', sqlalchemy.dialects.postgresql.JSONB)

class GarminSleepSummarieSchema(ma.Schema):
    class Meta:
        model = GarminSleepSummarie
        sqla_session = db.session

class GarminStressSummarie(db.Model):
    __tablename__ = "stress_summarie"
    summaryId = db.Column('summary_id', db.String(100), primary_key=True)
    userId = db.Column('user_id', db.String(100))
    userAccessToken = db.Column('user_access_token', db.String(100))
    calendarDate = db.Column('calendar_date', db.String(100))
    startTimeInSeconds = db.Column('start_time_in_seconds', db.Integer)
    startTimeOffsetInSeconds = db.Column('start_time_offset_in_seconds', db.Integer)
    durationInSeconds = db.Column('duration_in_seconds', db.Integer)
    timeOffsetStressLevelValues = db.Column('time_offset_stress_level_values', sqlalchemy.dialects.postgresql.JSONB)
    timeOffsetBodyBatteryValues = db.Column('time_offset_body_battery_values', sqlalchemy.dialects.postgresql.JSONB)

class GarminStressSummarieSchema(ma.Schema):
    class Meta:
        model = GarminStressSummarie
        sqla_session = db.session

class GarminUserMetricsSummarie(db.Model):
    __tablename__ = "user_metrics_summarie"
    summaryId = db.Column('summary_id', db.String(100), primary_key=True)
    userId = db.Column('user_id', db.String(100))
    userAccessToken = db.Column('user_access_token', db.String(100))
    calendarDate = db.Column('calendar_date', db.String(100))
    Vo2Max = db.Column('vo2max', db.Float)
    fitnessAge = db.Column('fitness_age', db.Integer)

class GarminUserMetricsSummarieSchema(ma.Schema):
    class Meta:
        model = GarminUserMetricsSummarie
        sqla_session = db.session