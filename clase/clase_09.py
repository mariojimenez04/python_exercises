# import datetime as dt
# import locale
# # locale.setlocale(locale.LC_ALL, 'es_ES.utf8')

# # # print(datetime.date.today())

# # x = datetime.datetime(2018, 6, 1)

# # print(x.strftime("%B")) 

# def fecha(fecha):
#   mes_espaniol = dt.strptime(fecha, '%d %B %Y')
#   print(mes_espaniol.strftime('%B'))

# fecha('2024-08-03')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import os
import math