import pandas as pd

# Load the Title AKAs dataset
title_akas_path = 'data/title.akas.tsv'
title_akas_data = pd.read_csv(title_akas_path, sep='\t', dtype=str)

# Load the Title Basics dataset
title_basics_path = 'data/title.basics.tsv'
title_basics_data = pd.read_csv(title_basics_path, sep='\t', dtype=str)

# Count the number of unique values in 'titleId' from the Title AKAs dataset
unique_title_ids = title_akas_data['titleId'].nunique()

# Count the number of records in the Title Basics file
title_basics_records = title_basics_data.shape[0]

# Calculate the difference
titles_without_alternative = title_basics_records - unique_title_ids

# Print the results
print(f"Number of unique values in 'titleId': {unique_title_ids}")
print(f"Number of records in Title Basics: {title_basics_records}")
print(f"There are {titles_without_alternative} titles which do not have an alternative title.")

# If the two numbers are the same, it means that every title has at least one alternate title, 
# and the participation in the ERD would be total. If the numbers are different, the difference indicates
# the number of titles that do not have an alternate title, reflecting partial participation in the relationship.