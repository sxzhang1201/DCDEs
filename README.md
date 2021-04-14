# DCDEs
Attempt to sort ERNs data dictionaries into domain lists with variables in common



## Explanation of Scripts (Temporary)
#### Store Data Dictionary 
The raw Excel document is stored at the directory `Data/Raw_data` 
with the name containing the creation date.

#### Generate Test Data
Run `run_data_preparation.py`, and you will subset the raw Excel document 
(you can specify which data dictionary to test in `config.py`) 
by choosing certain column and any number of rows 
(NB: Ideally these two parameters should be put in `config` but that is future work).

Currently we choose the column "Name of the Data Element" and the first 100 rows 
in the phase of script development.

The subset data will be generated and stored in the directory `Data` as `*.pickle` file.

#### Preprocess (To Be Done)
Run `run_preprocessing.py`, and you will:

- convert tabular text to a list of plain text and lowercase them;
- break plain texts into a list tokens
- remove stopwords
- stem tokens (if necessary)

#### Analyze
Run ...., and you will get term frequency histogram.  

 

