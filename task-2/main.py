#!/usr/bin/env python

import csv
import timeit
from BTrees.OOBTree import OOBTree

# Loading data from CSV
FILE_NAME = "generated_items_data.csv"

def load_data(file_name):
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        data = [
            {
                "ID": int(row["ID"]),
                "Name": row["Name"],
                "Category": row["Category"],
                "Price": float(row["Price"])
            }
            for row in reader
        ]
    return data

# Adding products to OOBTree
def add_item_to_tree(tree, item):
    tree[item["ID"]] = item

# Adding products to dict
def add_item_to_dict(dictionary, item):
    dictionary[item["ID"]] = item

# Range query for OOBTree
def range_query_tree(tree, min_price, max_price):
    return [item for _, item in tree.items() if min_price <= item["Price"] <= max_price]

# Range query for dict
def range_query_dict(dictionary, min_price, max_price):
    return [item for item in dictionary.values() if min_price <= item["Price"] <= max_price]

# Main function
def main():
    # Loading data
    data = load_data(FILE_NAME)

    # Initialization of structures
    tree = OOBTree()
    dictionary = {}

    # Adding data to structures
    for item in data:
        add_item_to_tree(tree, item)
        add_item_to_dict(dictionary, item)

    # Defining a price range for queries
    min_price, max_price = 10.0, 100.0

    # Performance measurement for OOBTree
    tree_time = timeit.timeit(lambda: range_query_tree(tree, min_price, max_price), number=1000)

    # Performance measurement for dict
    dict_time = timeit.timeit(lambda: range_query_dict(dictionary, min_price, max_price), number=1000)

    # Display of results
    print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
    print(f"Total range_query time for Dict: {dict_time:.6f} seconds")

if __name__ == "__main__":
    main()
