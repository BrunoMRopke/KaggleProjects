#!/usr/bin/env python
# coding: utf-8

# In[112]:


import os
import pandas as pd
import sqlite3
import math


# In[113]:


location = 'C:/Users/bruno/Desktop/Portifolio/Database_Inventory/Inventory.xlsx'


# In[114]:


# Lets prepare pandas to store the xlsx file.
df_inv = pd.read_excel(location,sheet_name='Inv List')

df_sku = pd.read_excel(location,sheet_name='SKU List')
df_sku.set_index('SKU_ID', inplace=True)


# In[115]:





# In[116]:


df_sku


# In[117]:


# The table SKU List in Inventory.xlsx doesnt look functional to create relationships with other tables. 
# Lets unpivot Unit,Box,Case and Pallet columns and create our on list/dataframe.

# New SKU Dataframe
SKU_List = pd.DataFrame()



# In[118]:


def create_unique_sku(df):
    """
    Creates a new DataFrame with individual rows for each type of SKU ('SKU - Unit', 'SKU - Box', 'SKU - Case', 'SKU - Pallet') 
    from the original DataFrame. For each new row, it includes the 'Product Name', 'Status', 'Brand', 'Units per Box', 
    and 'Boxes per Case' from the original DataFrame.
    
    Parameters:
    - df (DataFrame): The source DataFrame containing product information and different types of SKUs.
    
    Returns:
    - DataFrame: A new DataFrame where each row represents a unique SKU along with associated product information.
    """
    # Prepare a list to store new data for the resulting DataFrame
    new_data = []
    
    # Iterate over each row in the original DataFrame to create individual rows for each SKU type
    for i, row in df.iterrows():
        # For each type of SKU, create a new row
        for sku_type in ['SKU - Unit', 'SKU - Box', 'SKU - Case', 'SKU - Pallet']:
            new_row = {
                'SKU': row[sku_type],
                'Product Name': row['Product Name'],
                'Status': row['Status'],
                'Brand': row['Brand'],
                'Units per Box': row['Units per Box'],
                'Boxes per Case': row['Boxes per Case']
            }
            new_data.append(new_row)
    
    # Create a new DataFrame from the list of new data
    new_df = pd.DataFrame(new_data)
    
    return new_df

# Example usage:
# Assuming df_sku is your source DataFrame with the necessary columns.
new_df = create_unique_sku(df_sku)


# In[119]:


new_df


# In[120]:


new_df.to_excel('C:/Users/bruno/Desktop/Portifolio/Database_Inventory/SKU List.xlsx', index=False, engine='openpyxl')


# In[ ]:




