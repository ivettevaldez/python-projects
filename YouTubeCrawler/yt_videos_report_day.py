#!/usr/bin/python
#
# Created by Silvia Valdez on 30/11/2016.
# Retrieves analytics information about the activity of videos in the specified date.
#
# Usage example:
# python yt_videos_report_day.py --client-secrets="client_secrets.json"

import yt_authenticate_services
import yt_single_video_data
from config import *

import sys
import os
import datetime
from apiclient.errors import HttpError
from oauth2client.tools import argparser


def run_analytics_report(youtube_analytics, channel_id, options):
  # Call the Analytics API to retrieve a report. For a list of available reports, see:
  # https://developers.google.com/youtube/analytics/v1/channel_reports
  analytics_query_response = youtube_analytics.reports().query(
    ids="channel==%s" % channel_id,
    metrics=options.metrics,
    dimensions=options.dimensions,
    start_date=options.start_date,
    end_date=options.end_date,
    max_results=options.max_results,
    sort=options.sort
  ).execute()

  directory = "%sCandidate_%s/" % (FILES_DIR, channel_id)

  if not os.path.exists(directory):
      print "An error occurred! Directory not exists"
      sys.exit()

  # Declaration of the files which are being used
  fileChannel = "%s%s" % (directory, CHANNEL_HISTORY_FILE)
  csvChannel = open(fileChannel,"a")

  fileVideos = "%s%s" % (directory, VIDEOS_HISTORY_FILE)
  csvVideos = open(fileVideos,"w")

  fileVideosDetails = "%s%s" % (directory, VIDEOS_INFO_FILE)

  # Remove videos details file if already exists.
  if os.path.isfile(fileVideosDetails):
    os.remove(fileVideosDetails)

  print "Analytics Data for Videos of Channel %s:" % channel_id

  counter = 0
  videos = 0
  averageViewDuration = 0   # In seconds

  for row in analytics_query_response.get("rows", []):
    videoLine = ""
    print ""

    for value in row:
      counter += 1

      if counter == 1 and counter < 5:
        yt_single_video_data.get_video_information(value, options.client_secrets)

      if counter == 7:  # averageViewDuration column position
        averageViewDuration += int(value)
        videos += 1
        counter = 0

      videoLine = "%s%s%s" % (videoLine, value, SEPARATOR)
      print "%-13s" % value,
    print

    for column_header in analytics_query_response.get("columnHeaders", []):
      print "%-13s" % column_header["name"],
    print

    # Add the current timestamp and a new line
    now = datetime.datetime.now()
    parts = str(now).split('.')
    now = parts[0]
    videoLine = "%s%s%s" % (videoLine, now, NEW_LINE)

    csvVideos.write(videoLine.encode('utf-8'))
    print ""

  # Calculate the average view duration time of all the videos
  if videos != 0:
    seconds = averageViewDuration / videos
    m, s = divmod(seconds, TIME_UNITY)
    h, m = divmod(m, TIME_UNITY)
    print "\nAverage view duration: %02d:%02d min\n" % (m, s)
  else:
    print "\n---> WARNING: Analytics data for the selected date is not available yet."
    sys.exit()

  channelLine = "%s%s%s%s%s" % (SEPARATOR, seconds, SEPARATOR, now, NEW_LINE)
  csvChannel.write(channelLine.encode('utf-8'))

  csvChannel.close()
  csvVideos.close()


if __name__ == "__main__":
  argparser.add_argument("--metrics", default="views,comments,likes,dislikes,shares,averageViewDuration",
    help="Report metrics")
  argparser.add_argument("--dimensions", help="Report dimensions", default="video")
  argparser.add_argument("--start-date", help="Start date, in YYYY-MM-DD format", default=start_date)
  argparser.add_argument("--end-date", help="End date, in YYYY-MM-DD format", default=end_date)
  argparser.add_argument("--max-results", help="Max results", default=MAX_RESULTS)
  argparser.add_argument("--sort", help="Sort order", default="-views")
  argparser.add_argument("--client-secrets", help="Client secrets")

  args = argparser.parse_args()
  (youtube, youtube_analytics) = yt_authenticate_services.get_authenticated_services(args)

  try:
    channel_id = yt_authenticate_services.get_channel_id(youtube)
    run_analytics_report(youtube_analytics, channel_id, args)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
