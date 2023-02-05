# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 21:20:33 2023

@author: IdrisIbrahimERTEN
"""

from academic_search_engine import academic_search_engine

result = academic_search_engine()


"""
Dergi Park ve Google Akademik sonuçlarını döndürür.
"""
result.sayfa("big data", 1)

"""
Science Direct sonuçlarını döndürür.

"""
user_input = "big data"
email = "scince direct hesabınızın mail adresi"
password = "science direct hesabınızın şifresi"
result.sciencedirect(user_input, email, password)