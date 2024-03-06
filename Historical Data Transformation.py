import pandas as pd

# Read the input CSV file containing employee data into a DataFrame
input_csv_path = "C:/Users/Hrishikesh/Desktop/rohan/input.csv"
df = pd.read_csv(input_csv_path)

# Sort the DataFrame by employee code and relevant dates
df['Date_of_Joining'] = pd.to_datetime(df['Date of Joining'])
df['Date_of_Exit'] = pd.to_datetime(df['Date of Exit'])
df['Compensation_1_date'] = pd.to_datetime(df['Compensation 1 date'])
df['Compensation_2_date'] = pd.to_datetime(df['Compensation 2 date'])
df['Review_1_date'] = pd.to_datetime(df['Review 1 date'])
df['Review_2_date'] = pd.to_datetime(df['Review 2 date'])
df['Engagement_1_date'] = pd.to_datetime(df['Engagement 1 date'])
df['Engagement_2_date'] = pd.to_datetime(df['Engagement 2 date'])

df.sort_values(by=['Employee Code', 'Date of Joining'], inplace=True)

# Create an empty list to store the transformed data
historical_data = []

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Calculate effective and end dates
    next_index = index + 1
    if next_index < len(df):
        end_date = df.iloc[next_index]['Date_of_Joining'] - pd.Timedelta(days=1)
    else:
        end_date = pd.Timestamp(year=2100, month=1, day=1)

 # Create historical records for each period with consistent data
    historical_data.append({
        'Employee Code': row['Employee Code'],
        'Manager Employee Code': row['Manager Employee Code'],
        'Last Compensation': None,
        'Compensation': row['Compensation'],
        'Last Pay Raise Date': None,
        'Variable Pay': None,
        'Tenure in Org': None,
        'Performance Rating': None,
        'Engagement Score': None,
        'Effective Date': row['Date of Joining'],
        'End Date': end_date
    })

    # Check if there are changes in compensation or performance
    if pd.notna(row['Compensation 1 date']):
        # New compensation
        historical_data.append({
            'Employee Code': row['Employee Code'],
            'Manager Employee Code': row['Manager Employee Code'],
            'Last Compensation': row['Compensation'],
            'Compensation': row['Compensation 1'],
            'Last Pay Raise Date': row['Compensation 1 date'],
            'Variable Pay': None,
            'Tenure in Org': None,
            'Performance Rating': None,
            'Engagement Score': None,
            'Effective Date': row['Compensation 1 date'],
            'End Date': end_date
        })

    if pd.notna(row['Compensation 2 date']):
        # New compensation
        historical_data.append({
            'Employee Code': row['Employee Code'],
            'Manager Employee Code': row['Manager Employee Code'],
            'Last Compensation': row['Compensation 1'],
            'Compensation': row['Compensation 2'],
            'Last Pay Raise Date': row['Compensation 2 date'],
            'Variable Pay': None,
            'Tenure in Org': None,
            'Performance Rating': None,
            'Engagement Score': None,
            'Effective Date': row['Compensation 2 date'],
            'End Date': end_date
        })

    if pd.notna(row['Review 1 date']):
        # New performance review
        historical_data.append({
            'Employee Code': row['Employee Code'],
            'Manager Employee Code': row['Manager Employee Code'],
            'Last Compensation': None,
            'Compensation': None,
            'Last Pay Raise Date': None,
            'Variable Pay': None,
            'Tenure in Org': None,
            'Performance Rating': row['Review 1'],
            'Engagement Score': None,
            'Effective Date': row['Review 1 date'],
            'End Date': end_date
        })

    if pd.notna(row['Review 2 date']):
        # New performance review
        historical_data.append({
            'Employee Code': row['Employee Code'],
            'Manager Employee Code': row['Manager Employee Code'],
            'Last Compensation': None,
            'Compensation': None,
            'Last Pay Raise Date': None,
            'Variable Pay': None,
            'Tenure in Org': None,
            'Performance Rating': row['Review 2'],
            'Engagement Score': None,
            'Effective Date': row['Review 2 date'],
            'End Date': end_date
        })

    if pd.notna(row['Engagement 1 date']):
        # New engagement score
        historical_data.append({
            'Employee Code': row['Employee Code'],
            'Manager Employee Code': row['Manager Employee Code'],
            'Last Compensation': None,
            'Compensation': None,
            'Last Pay Raise Date': None,
            'Variable Pay': None,
            'Tenure in Org': None,
            'Performance Rating': None,
            'Engagement Score': row['Engagement 1'],
            'Effective Date': row['Engagement 1 date'],
            'End Date': end_date
        })

    if pd.notna(row['Engagement 2 date']):
        # New engagement score
        historical_data.append({
            'Employee Code': row['Employee Code'],
            'Manager Employee Code': row['Manager Employee Code'],
            'Last Compensation': None,
            'Compensation': None,
            'Last Pay Raise Date': None,
            'Variable Pay': None,
            'Tenure in Org': None,
            'Performance Rating': None,
            'Engagement Score': row['Engagement 2'],
            'Effective Date': row['Engagement 2 date'],
            'End Date': end_date
        })

# Convert the list of dictionaries to a DataFrame
historical_df = pd.DataFrame(historical_data)

# Write the DataFrame to a CSV file
output_csv_path = "C:/Users/Hrishikesh/Desktop/rohan/output.csv"
historical_df.to_csv(output_csv_path, index=False)  # index=False to exclude row indices

