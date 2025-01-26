import csv
import urllib.request
import pandas as pd

class CSVDownloader:
    def __init__(self, base_url, contents, titles):
        self.base_url = base_url
        self.contents = contents
        self.titles = titles

    def download_all_files(self):
        for filename in self.contents:
            self.download_single_file(filename)

    def download_single_file(self, filename):
        url = self.build_url(filename)
        self.store_file(url, filename)

    def build_url(self, filename):
        return f"{self.base_url}{filename}"

    def store_file(self, url, filename):
        urllib.request.urlretrieve(url, filename)

if __name__ == "__main__":
     base_url = "https://www.mhlw.go.jp/content/"
     contents = [
          "pcr_positive_daily.csv",
          "pcr_tested_daily.csv",
          "cases_total.csv",
          "recovery_total.csv",
          "death_total.csv",
          "pcr_case_daily.csv"
     ]
     titles = [
     "陽性者数",
     "PCR検査実施人数",
     "入院治療等を要する者の数",
     "退院又は療養解除となった者の数",
     "死亡者数",
     "PCR検査の実施件数"
     ]

    downloader = CSVDownloader(base_url, contents, titles)
    downloader.download_files()
