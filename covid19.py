import csv
import urllib.request
import pandas as pd


base_url = "https://www.mhlw.go.jp/content/"
contents = ["pcr_positive_daily.csv", "pcr_tested_daily.csv", "cases_total.csv", "recovery_total.csv", "death_total.csv", "pcr_case_daily.csv"]
titles = ["陽性者数","PCR検査実施人数","入院治療等を要する者の数","退院又は療養解除となった者の数","死亡者数","PCR検査の実施件数"]

for i in range(len(contents)):
     url = base_url + contents[i]
     urllib.request.urlretrieve(url, contents[i])
     # print(url)