#!/usr/bin/python
#
# Created by Silvia Valdez on 30/11/2016.
# Retrieves analytics information about the channel.
#
# Usage example:
# python yt_channel_report.py --client-secrets="client_secrets.json"

import yt_authenticate_services
from config import *

import sys
import os
from apiclient.errors import HttpError
from oauth2client.tools import argparser


# Call the API's channels.list method to list the existing channel localizations.
def list_channel_statistics(youtube, channel_id):
  results = youtube.channels().list(
    part="statistics",
    id=channel_id
  ).execute()

  statistics = results["items"][0]["statistics"]

  directory = "%sCandidate_%s/" % (FILES_DIR, channel_id)
  if not os.path.exists(directory):
      os.makedirs(directory)

  fileName = "%s%s" % (directory, CHANNEL_HISTORY_FILE)
  csvChannel = open(fileName,"w")
  line = channel_id

  print "Analytics Data for Channel %s:" % channel_id

  for attribute, value in statistics.iteritems():
    line = "%s%s%s" % (line, SEPARATOR, value)
    print "%s: %s" % (attribute, value)

  csvChannel.write(line.encode('utf-8'))
  csvChannel.close()


if __name__ == "__main__":
  argparser.add_argument("--client-secrets", help="Client secrets")
  args = argparser.parse_args()

  (youtube, youtube_analytics) = yt_authenticate_services.get_authenticated_services(args)

  try:
    channel_id = yt_authenticate_services.get_channel_id(youtube)
    list_channel_statistics(youtube, channel_id)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
