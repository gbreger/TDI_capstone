#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
from unidecode import unidecode

def standardize_string(string):
    """
    Standardize strings by converting diacritics and East Asian characters as well as removing parentheses (and their inclused
    content), retaining only alphanumeric characters.
    
    Parameters
    ----------
    string : str
        The string to be standardized.
    
    Returns
    -------
    str
        The standardized string in lowercase and stripped of preceding/following whitespace.
    """

    # if string is not a str, return an empty string
    if not isinstance(string, str):
        return ''
   
    # convert everything to unicode, addressing diacritics as well as chinese characters
    string = unidecode(string)
    
    # remove any non-alphanumeric character or non-space as well as parenthesis (and their enclosed content)
    regex = r'\([^)]*\)|[^a-zA-Z0-9\s]'
    string = re.sub(regex, '', string)
    
    # standardize spacing to retain a single space between words
    string = re.sub(r'\s+', ' ', string)
    
    # change to lowercase and strips whitespaces
    return string.lower().strip()


# In[2]:


def pseudo_list_parser(item, dtype=int, ignore_space=True):
    """
    Parse a string that appears as a list into a list of elements of a specified data type.
    It assumes elements are separated by a comma.
    These kind of strings are a common outcome of reading lists from csv files into a dataframe.
    
    Parameters
    ----------
    item : str
        The string to be parsed.
    dtype : data type, default int
        The data type that would comprise the elements of the parsed list.
    ignore_space : bool, default True
        Whether to remove spaces (appearing most often after a comma in a list string) from the string before parsing.
    
    Returns
    -------
    list or object
        Returns the parsed string as a list of elements of the specified data type.
        If the first argument passed to the function is not a string (e.g. NaN),
        returns the item without performing any operations.
    """

    if isinstance(item, str):
        if ignore_space:
            item = item.replace(' ', '')
        return [dtype(x) for x in item.replace('[','').replace(']', '').split(',')]
    
    return item


# In[ ]:




