#!/usr/bin/env python
"""
Module containing the functions to subset the data
according to a given country name
"""

import datetime
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def get_country_df(filename, country):
    # Load table
    wine = pd.read_csv(filename)

    # Use the country name to subset data
    subset_country_df = wine[wine["country"] == country].copy()

    return subset_country_df


def get_country(filename, country):
    """
    Get a subset of the data or a given country
    Args:
    -----
    filename: str
        Path to the filename containing the wine data
    country: str
        Country to be used to subset

    Returns:
    -----
    data_path: st
        Path to the created data set
    """

    # Subset the
    subset_country_df = get_country_df(filename, country)
    # Constructing the fname
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    fname = f"data/processed/{today}-winemag_{country}.csv"

    # Saving the csv
    subset_country_df.to_csv(fname)

    return (fname)


if __name__ == "__main__":
    filename = sys.argv[1]
    country = sys.argv[2]
    print(f"Subsetting: {filename}")
    print(f"Country searched: {country}")

    print(get_country(filename, country))


def get_mean_price(filename):
    """ function to get the mean price of the wines
    rounded to 4 decimals"""
    wine = pd.read_csv(filename)
    mean_price = wine["price"].mean()
    return round(mean_price, 4)  # note the rounding here
