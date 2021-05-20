import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from Preprocessing.remove_charaters import remove_characters
from Preprocessing.remove_stopwords import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

DATA_DICTIONARY = "Data/Raw data/DCDE_Candidates_Template May.xls"

# Load data dictionary
xls = pd.ExcelFile(DATA_DICTIONARY)

# Subset the Excel by selecting relevant columns
df = pd.read_excel(xls, "Data Dictionary (stewards)")[["Name of the ERN",
                                                       "Name of the grouping item",
                                                       "Name of the Data Element",
                                                       "Explanatory description",
                                                       "Data type or list of permitted values",
                                                       "Example value",
                                                       "Comments"]]

# Remove rows with NA in both "Name of the Data Element" and "Explanatory description" columns
df = df.dropna(subset=["Name of the Data Element", "Explanatory description"])

# # Add content of  "Explanatory description" to "Name of the Data Element"
indices = df[df["Name of the Data Element"].isnull()].index
df.loc[indices, "Name of the Data Element"] = df.loc[indices, "Explanatory description"]

# Get ERN List
ern_list = list(set(list(df["Name of the ERN"])))

ern_dic = []
ps = PorterStemmer()
lem = WordNetLemmatizer()

for ern_name in ern_list:
    print(ern_name)
    text = " ".join(df[df["Name of the ERN"] == ern_name]["Name of the Data Element"].tolist())
    print(text)
    # Remove special characters
    text = remove_characters(text)

    # tokenize
    tokens = word_tokenize(text)

    # stemming
    tokens2 = [lem.lemmatize(token) for token in tokens]

    text = " ".join(tokens2)

    ern_dic.append(text)

vec = CountVectorizer(min_df=2, lowercase=True, stop_words=stopwords, binary=True)

X = vec.fit_transform(ern_dic)

df_term = pd.DataFrame(X.toarray(), columns=vec.get_feature_names())

df_term.to_csv("df_term_binary.csv")









