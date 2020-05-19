#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:23:22 2020

@author: saylorstarks
"""

import openpyxl

book = openpyxl.load_workbook('jbhunt.xlsx')
sheet = book['Sheet1']

sheet.delete_rows(30, 20)

book.save('jbhunt_new.xlsx')