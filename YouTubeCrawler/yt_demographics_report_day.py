#!/usr/bin/python

# Created by Silvia Valdez on 5/12/2016.
# Retrieves demographic information about the genders of the channel viewers in the specified date.
#
# Usage example:
# python yt_demographics_report_day.py --client-secrets="client_secrets.json"

import yt_authenticate_services
from config import *

import sys
import os
from apiclient.errors import HttpError
from oauth2client.tools import argparser


def run_demographics_report(youtube_analytics, channel_id, options):
  # Call the Analytics API to retrieve a report. For a list of available reports, see:
  # https://developers.google.com/youtube/analytics/v1/channel_reports
  analytics_query_response = youtube_analytics.reports().query(
    ids="channel==%s" % channel_id,
    metrics=options.metrics,
    dimensions=options.dimensions,
    start_date=options.start_date,
    end_date=options.end_date
  ).execute()

  directory = "%sCandidate_%s/" % (FILES_DIR, channel_id)

  if not os.path.exists(directory):
      print "An error occurred! Directory not exists"
      sys.exit()

  fileName = "%s%s" % (directory, CHANNEL_HISTORY_FILE)
  csvChannel = open(fileName,"a")

  print "Demographics Data for Channel %s:" % channel_id

  for column_header in analytics_query_response.get("columnHeaders", []):
    print "%-13s" % column_header["name"],
  print

  counter = 0
  line = ""
  for row in analytics_query_response.get("rows", []):
    for value in row:
      counter += 1
      if counter % 2 == 0:
        line = "%s%s%s" % (line, SEPARATOR, value)
      print "%-13s" % value,
    print

  csvChannel.write(line.encode('utf-8'))
  csvChannel.close()


if __name__ == "__main__":
  argparser.add_argument("--metrics", help="Report metrics", default="viewerPercentage")
  argparser.add_argument("--dimensions", help="Report dimensions", default="gender")
  argparser.add_argument("--start-date", help="Start date, in YYYY-MM-DD format", default=start_date)
  argparser.add_argument("--end-date", help="End date, in YYYY-MM-DD format", default=end_date)
  argparser.add_argument("--client-secrets", help="Client secrets")

  args = argparser.parse_args()
  (youtube, youtube_analytics) = yt_authenticate_services.get_authenticated_services(args)

  try:
    channel_id = yt_authenticate_services.get_channel_id(youtube)
    run_demographics_report(youtube_analytics, channel_id, args)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
