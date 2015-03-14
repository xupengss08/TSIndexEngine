# package preprocess

"""

This is the first stage of our time-series indexing research, including:
    1) Read raw data for each equipment into memory (each equipment is a file
       of multi-lines of <timestamp, paravalue> pair.
    2) Slice raw data using certain timestamp interval.
    3) Align raw data into a paravalue list of the same timestamp interval.

"""
