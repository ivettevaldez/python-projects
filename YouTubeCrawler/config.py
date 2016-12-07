#!/usr/bin/python
#
# Created by Silvia Valdez on 5/12/2016.
# Configuration file with constants and variables which are neccesary for the other scripts.

from datetime import datetime, timedelta

FILES_DIR = "/Users/Silvia/Repos/Hnb16Elecciones2017/Source/Python/Crawler_Youtube/Files/"
CHANNEL_HISTORY_FILE = "CHANNEL_HISTORY.csv"
VIDEOS_HISTORY_FILE = "VIDEOS_HISTORY.csv"
VIDEOS_INFO_FILE = "VIDEOS_INFO.csv"

SEPARATOR = "|"
NEW_LINE = "\n"

MAX_RESULTS = 200
TIME_UNITY = 60

START_DAYS_AGO = 2
END_DAYS_AGO = 1

now = datetime.now()
start_date = (now - timedelta(days=START_DAYS_AGO)).strftime("%Y-%m-%d")
end_date = (now - timedelta(days=END_DAYS_AGO)).strftime("%Y-%m-%d")
