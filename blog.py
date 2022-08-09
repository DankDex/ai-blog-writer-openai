import os
import openai
import config


openai.api_key = config.OPENAI_API_KEY


def generateBlogTopics(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="create topics for " + prompt1,
      temperature=0.7,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0.4,
      presence_penalty=0
    )

    return response['choices'][0]['text']

def generateBlogSections(prompt1):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="create sections for " + prompt1,
      temperature=0.6,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0.4,
      presence_penalty=0
    )

    return response['choices'][0]['text']


def blogSectionExpander(prompt1, prompt2):
    response = openai.Completion.create(
      engine="davinci-instruct-beta-v3",
      prompt="Expand the topic " + prompt1 + " " + prompt2,
      temperature=0.7,
      max_tokens=200,
      top_p=1,
      frequency_penalty=0.4,
      presence_penalty=0
    )

    return response['choices'][0]['text']
