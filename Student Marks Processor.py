# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 12:39:26 2026

@author: mi
"""

marks = [78, 92, 67, 88, 96]

def process_marks(marks):
    updated = list(map(lambda m: min(m + 5, 100), marks))
    return updated

print(process_marks(marks))
