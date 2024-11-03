"""Making the code in our program"""

import os
from langchain_openai import ChatOpenAI
import requests

os.environ["LANGCHAIN_TRACING_V2"] = "true"


def get_products(word):
    link = 'https://data.unwrangle.com/api/getter/?platform=lowes_search&search='+word+'&api_key=8e2ed113c38dce504bd8557d66cb54719be94205'
    response = requests.get(link)
    return response.json([results])



