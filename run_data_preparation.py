import pandas as pd
import config

# Load data dictionary
xls = pd.ExcelFile(config.DATA_DICTIONARY)

# Subset the Excel by selecting relevant columns
df = pd.read_excel(xls, "Data Dictionary (stewards)")[["Name of the ERN",
                                                       "Name of the grouping item",
                                                       "Name of the Data Element",
                                                       "Explanatory description",
                                                       "Data type or list of permitted values",
                                                       "Example value",
                                                       "Comments"]]

# Subset raw data by choosing the first 100 rows and one column "Name of the Data Element"
df_test = df[["Name of the Data Element"]][0:100]

print(df_test)

# Store data as a pickle file (in order to avoid re-run this script for each test)
df_test.to_pickle("Data/my_test_df.pickle")


