import pandas as pd
import numpy as np

url ='https://www.fdic.gov/bank/individual/failed/banklist.html'
res2=pd.read_html(url)
print(res2)
print("+"*50)
print(res2[0]["Bank Name"])



