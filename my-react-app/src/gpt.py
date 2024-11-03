"""Integrating the AI"""

import getpass
import os
import requests
from langchain_openai import ChatOpenAI
# import pandas as pd

# os.environ[openai_api_key] = getpass.getpass()

llm = ChatOpenAI(model="gpt-4o-mini")

lowes_word = str()
project_descript = str()
cost_list = list()
total_cost_list = list()
total_cost = 0
material_list = list()
quantity_list = list()

def get_products(word): # gets product from Lowe's API based on word search
    """Returns first product in results of searching for <word> in Lowe's API"""
    global lowes_word
    link = 'https://data.unwrangle.com/api/getter/?platform=lowes_search&search='+word+'&api_key=8e2ed113c38dce504bd8557d66cb54719be94205'
    response = requests.get(link)
    lowes_word = word
    return response.json()["Results"][0]

def get_project_materials(project_description): #asks GPT for materials for project input
    """Returns list of all materials needed for <project description> based on GPT's response"""
    global project_descript
    link = 'https://data.unwrangle.com/api/getter/?platform=lowes_search&search='+lowes_word+'&api_key=8e2ed113c38dce504bd8557d66cb54719be94205'
    response = llm.generate(f"List the materials needed to build a {project_description} using products from {link} and place each item on a new line.")
    project_descript = project_description #make this global because it will be used on other places
    return response.split("\n")

def get_project_quantity(project_description): #asks GPT for materials for project input
    """Returns list of quantities of each material needed for <project description> based on GPT's response"""
    link = 'https://data.unwrangle.com/api/getter/?platform=lowes_search&search='+lowes_word+'&api_key=8e2ed113c38dce504bd8557d66cb54719be94205'
    response = llm.generate(f"List the quantity of each material needed to build a {project_description} using products from {link} and place each item on a new line.")
    return response.split("\n")

def get_product_costs(): #materials comes from the gpt function, input material list??
    """Updates each item's cost and builds a list for all of them"""
    global total_cost
    for idx in range(0, len(material_list)):
        product = get_products(material_list[idx]) #assign product var to matching Lowe's product based on material
        product_cost = product['price'] #find price
        quantity = int(quantity_list[idx])
        cost_list.append(product_cost)
        total_cost_list.append(product_cost * quantity)
        total_cost += (product_cost * quantity)
    return total_cost

def display_table(): #table with material, quantity, cost, total cost
    print("Project Materials and Costs")
    data = { "Material": material_list, "Quantity": quantity_list, "Cost per Item": cost_list, "Total Cost per Item": total_cost_list}
    # df = pd.DataFrame(data)
    # print(df)
    print(get_product_costs())

quantity_list = get_project_quantity(project_descript)
material_list = get_project_materials(project_descript)