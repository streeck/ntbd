#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

import sys
import json


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyCxvjimd-OTimRESiRNECly50py7eOFn7g"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    part="id,snippet",
    maxResults=options.max_results,
    order="viewCount",
    q=options.search,
    channelId=options.channel_id
  ).execute()

  videos = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s" % (search_result["id"]["videoId"]))

  return videos


def youtube_video(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

  video_response = youtube.videos().list(
    part="snippet,statistics",
    id=options.video_id
  ).execute()

  for video_result in video_response.get("items", []):
    print "ID: {}".format(video_result["id"])
    print "Channel ID: {}".format(video_result["snippet"]["channelId"])
    print u"Title: {}".format(video_result["snippet"]["title"]).encode('utf-8')
    print "Publish Date: {}".format(video_result["snippet"]["publishedAt"][:10])
    print "Views: {:,}".format(int(video_result["statistics"]["viewCount"]))
    print "Likes: {:,}".format(int(video_result["statistics"]["likeCount"]))
    print "Dislikes: {:,}".format(int(video_result["statistics"]["dislikeCount"]))
    print "Category: {}".format(video_result["snippet"]["categoryId"])
    print "\n------------------------------------------------\n"

    return {'id': '{}'.format(video_result["id"]),
            'channelId': '{}'.format(video_result["snippet"]["channelId"]),
            'title': u'{}'.format(video_result["snippet"]["title"]).encode('utf-8'),
            'date': video_result["snippet"]["publishedAt"][:10],
            'category': video_result["snippet"]["categoryId"],
            'stats': {'views': int(video_result["statistics"]["viewCount"]),
                      'likes': int(video_result["statistics"]["likeCount"]),
                      'dislikes': int(video_result["statistics"]["dislikeCount"])}}


def jsonGenerator(options):
  videoList = youtube_search(options)

  jsonFile = {'videos': []}

  for video in videoList:
    options.video_id = video
    jsonFile["videos"].append(youtube_video(options))

  with open('synthetic-data.json', 'w') as output:
    json.dump(jsonFile, output)

  print "Data extraction completed!"


if __name__ == "__main__":
  argparser.add_argument("--video-id", help="Video ID")
  argparser.add_argument("--max-results", help="Max results", default=25)
  argparser.add_argument("--search", help="Search terms")
  argparser.add_argument("--channel-id", help="Channel ID")
  args = argparser.parse_args()

  if args.video_id:
    try:
      youtube_video(args)
    except HttpError, e:
      print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
  else:
    try:
      jsonGenerator(args)
    except HttpError, e:
      print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
