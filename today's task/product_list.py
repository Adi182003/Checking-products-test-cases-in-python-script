import pandas as pd

# Load the Excel file
workbook = pd.ExcelFile("Data For Test.xlsx")
transactions = workbook.parse("Transaction")
item_info = workbook.parse("Item_Info")

# Merge both sheets on 'Material No'
data = pd.merge(transactions, item_info, on="Material No")

# Group by Product Head and Material No, sum the quantity
grouped = data.groupby(["Product Head", "Material No"], as_index=False)["Qty"].sum()

# Sort by quantity in descending order and get top 5 products
top_5_products = grouped.sort_values(by="Qty", ascending=False).head(5)

# Print the final table
print("\nTop 5 Products by Quantity:\n")
print(top_5_products.to_markdown(index=False))
