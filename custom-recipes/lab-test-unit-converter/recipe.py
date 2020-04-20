# Code for custom code recipe converter (imported from a Python recipe)

# To finish creating your custom recipe from your original PySpark recipe, you need to:
#  - Declare the input and output roles in recipe.json
#  - Replace the dataset names by roles access in your code
#  - Declare, if any, the params of your custom recipe in recipe.json
#  - Replace the hardcoded params values by acccess to the configuration map

# See sample code below for how to do that.
# The code of your original recipe is included afterwards for convenience.
# Please also see the "recipe.json" file for more information.

# import the classes for accessing DSS objects from the recipe
import dataiku
# Import the helpers for custom recipes
from dataiku.customrecipe import *

# Inputs and outputs are defined by roles. In the recipe's I/O tab, the user can associate one
# or more dataset to each input and output role.
# Roles need to be defined in recipe.json, in the inputRoles and outputRoles fields.

# To  retrieve the datasets of an input role named 'lab_test_datasets' as an array of dataset names:
#lab_test_dataset_name = get_input_names_for_role('lab_tests_dataset')
# The dataset objects themselves can then be created like this:
#lab_test_dataset = dataiku.Dataset(lab_test_dataset_name)

# For outputs, the process is the same:
#successful_conversion_output_name = get_output_names_for_role('successful_conversion_output')
#successful_conversion_dataset = dataiku.Dataset(successful_conversion_output_name)
#unsuccessful_conversion_output_name = get_output_names_for_role('unsuccessful_conversion_output')
#unsuccessful_conversion_dataset = dataiku.Dataset(unsuccessful_conversion_output_name)



# The configuration consists of the parameters set up by the user in the recipe Settings tab.

# Parameters must be added to the recipe.json file so that DSS can prompt the user for values in
# the Settings tab of the recipe. The field "params" holds a list of all the params for wich the
# user will be prompted for values.

# The configuration is simply a map of parameters, and retrieving the value of one of them is simply:
#my_variable = get_recipe_config()['parameter_name']

# For optional parameters, you should provide a default value in case the parameter is not present:
#my_variable = get_recipe_config().get('parameter_name', None)

# Note about typing:
# The configuration of the recipe is passed through a JSON object
# As such, INT parameters of the recipe are received in the get_recipe_config() dict as a Python float.
# If you absolutely require a Python int, use int(get_recipe_config()["my_int_param"])


#############################
# Your original recipe
#############################

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np

# Read recipe inputs
prp_cln_labs_pq = dataiku.Dataset("prp_cln_labs_pq")
prp_cln_labs_pq_df = prp_cln_labs_pq.get_dataframe()

# Define dataframe
df = prp_cln_labs_pq_df

# Get the columns that we will use as variables
lab_name_column_name =
lab_value_column_name =
lab_unit_to_column_name =
lab_unit_from_column_name =

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
prp_cln_labs_standardization_and_conversion_pq = dataiku.Dataset("prp_cln_labs_standardization_and_conversion_pq")
prp_cln_labs_standardization_and_conversion_pq.write_with_schema(prp_cln_labs_standardization_and_conversion_pq_df)