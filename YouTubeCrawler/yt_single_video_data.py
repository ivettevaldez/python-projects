#!/usr/bin/python
#
# Created by Silvia Valdez on 6/12/2016.
# Retrieves information about the specified video (id).
#
# Usage example from other script:
#   print yt_single_video_data.get_video_information(channel_id, video_id, client_secrets)
# Usage example from terminal:
#   python yt_single_video_data.py --video-id=VIDEO_ID --client-secrets="client_secrets.json"

import yt_authenticate_services
from config import *

import sys
import os
import unicodedata
from apiclient.errors import HttpError
from oauth2client.tools import argparser


def strip_accents(text):
  """
  Strip accents from input String.

  :param text: The input string.
  :type text: String.

  :returns: The processed String.
  :rtype: String.
  """
  try:
    text = unicode(text, 'utf-8')
  except NameError:   # Unicode is a default on Python 3
    pass
  except TypeError:
    pass
  text = unicodedata.normalize('NFD', text)
  text = text.encode('ascii', 'ignore')
  text = text.decode("utf-8")
  return str(text)


def clean_text(text):
  text = text.replace("\n", " ")
  text = text.replace("\r", " ")
  text = text.replace("\t", " ")
  text = text.replace("  ", "")
  text = text.replace("    ", "")
  text = text.replace("\"", "")
  text = text.replace("\\", "")
  text = text.replace("|", "")
  text = strip_accents(text)
  return str(text)


# Call the API's channels.list method to list the existing channel localizations.
def list_video_information(youtube, args):
  results = youtube.videos().list(
    part="snippet",
    id=args.video_id
  ).execute()

  snippet = results["items"][0]["snippet"]

  directory = "%sCandidate_%s/" % (FILES_DIR, args.channel_id)
  if not os.path.exists(directory):
      os.makedirs(directory)

  fileName = "%s%s" % (directory, VIDEOS_INFO_FILE)
  csvVideos = open(fileName, "a")
  line = args.video_id

  print "Data of the video with ID: %s" % args.video_id

  for attribute, value in snippet.iteritems():
    if attribute == "title" or attribute == "publishedAt" or attribute == "channelTitle":
      line = "%s%s%s" % (line, SEPARATOR, value)
      print "%-13s: %s" % (attribute, value)
    elif attribute == "description":
      line = "%s%s%s" % (line, SEPARATOR, clean_text(value))
      print "%-13s: %s" % (attribute, clean_text(value))

  print ""
  line = "%s%s" % (line, NEW_LINE)
  csvVideos.write(line.encode('utf-8'))
  csvVideos.close()

  return "Successfully obtained data of Video: %s" % args.video_id


def authenticate_services(args):
  (youtube, youtube_analytics) = yt_authenticate_services.get_authenticated_services(args)
  channel_id = yt_authenticate_services.get_channel_id(youtube)
  args.channel_id = channel_id

  try:
    list_video_information(youtube, args)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)


def get_video_information(video_id, client_secrets):
  args = argparser.parse_args()
  args.video_id = video_id
  args.client_secrets = client_secrets

  authenticate_services(args)


if __name__ == "__main__":
  argparser.add_argument("--video-id", help="Video ID")
  argparser.add_argument("--client-secrets", help="Client secrets")
  args = argparser.parse_args()

  authenticate_services(args)
