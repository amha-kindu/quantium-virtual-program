import pandas as pd


merged_df = pd.DataFrame()
# Read all three files into a single dataframe
for i in range(3):
    df = pd.read_csv('data\daily_sales_data_'+str(i)+'.csv')
    print(merged_df.empty)
    merged_df = df if merged_df.empty else merged_df.merge(df, how='outer')

#Change string data type of column 'price'
merged_df['price'] = merged_df['price'].apply(lambda a: float(a[1:]))

#Calculating the total sales of each product
merged_df['sales'] = merged_df['price']*merged_df['quantity']

#Pick the data of the pink morsel product
merged_df = merged_df[merged_df['product']=='pink morsel']

#Selecting sales, date and region columns
merged_df = merged_df.loc[:, ['sales', 'date', 'region']]

#Exporting to *.csv file
merged_df.to_csv('data\daily_sales_data.csv')