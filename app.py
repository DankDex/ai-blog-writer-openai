from flask import Flask, render_template, request
import config
import blog
from blog_api import blogConnect 

import sys

import random
from time import sleep

import requests
from googleapiclient.discovery import build

from oauth2client import client
from googleapiclient import sample_tools

Key = "AIzaSyBsMu6-T6herV7oXWTmE5t_w_VNtRZYskE"
BlogId = "3974082107657293362"


def main(argv):

    print("Starting....")

    # Authenticate and construct service.
    service, flags = sample_tools.init(
    argv, 'blogger', 'v3', __doc__, __file__,
    scope='https://www.googleapis.com/auth/blogger')

    while(True):

        try:

            users = service.users()

            # Retrieve this user's profile information
            thisuser = users.get(userId="self").execute()
            print("This user's display name is: %s" % thisuser["displayName"])

            blogs = service.blogs()

            posts = service.posts()
            
            prompt_file = open("prompts.txt","r")
            prompt_list = prompt_file.readlines()


            print("\n\nLIST:\n")

            for index in range(0,len(prompt_list)):
                prompt_list[index] = prompt_list[index].replace('\n','')
                print(prompt_list[index]+", ")

            print("\n\n")

            prompt = prompt_list[random.randint(0, len(prompt_list)-1)]

            fullText = ""

            blogT = blog.generateBlogTopics(prompt)
            blogTopicIdeas = blogT.split('\n')

            if(blogTopicIdeas[2][0].isdigit()):
                blogTopicIdeas[2] = blogTopicIdeas[2][2:]

            fullText += "<h1><b>" + blogTopicIdeas[2] + "</b></h1><br><br><br>";

            blogT = blog.generateBlogSections(blogTopicIdeas[2])
            blogSectionIdeas = blogT.split('\n')

            for section in range(2, len(blogSectionIdeas)-1):
                if(blogSectionIdeas[section].replace(" ", "") != ""):
                    if(blogSectionIdeas[section][0].isdigit()):
                        blogSectionIdeas[section] = blogSectionIdeas[section][2:]
                    fullText += "<h4><b>" + blogSectionIdeas[section] + "</b></h4>" + "<p>" + blog.blogSectionExpander(blogTopicIdeas[2],blogSectionIdeas[section]) + "<p><br><br>"

            fullText = fullText.replace('\n', '<br>')

            body = {
                "kind": "blogger#post",
                "title": blogTopicIdeas[2],
                "content":fullText
            }

            posts.insert(blogId=BlogId, body=body, isDraft=False).execute()

            print("Blog Post made with title: " + blogTopicIdeas[2])
        
        except client.AccessTokenRefreshError:
            print(
                "The credentials have been revoked or expired, please re-run"
                "the application to re-authorize"
            )

        sleep(60*15)

    print("Closing...")


if __name__ == '__main__':
    main(sys.argv)

