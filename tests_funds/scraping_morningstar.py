#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import required modules 
from lxml import html 
import requests 
from bs4 import BeautifulSoup
import pandas as pd

# SearchBox
# //*[@id="quoteSearch"]

fund = {}



def extract_xpath(tree, xpath_obj):
    try:
        foo_str = tree.xpath(xpath_obj)[0].text
        print(foo_str)
    except:
        print('error')
    return foo_str

def get_fund_info(fund_web_url = 'https://www.morningstar.it/it/funds/snapshot/snapshot.aspx?id=F0GBR04P4X'):
    # Generale    
    # https://www.morningstar.it/it/funds/snapshot/snapshot.aspx?id=F0GBR04P4X
    
    fund['url'] = fund_web_url
    # Request the page 
    page = requests.get(fund_web_url)
    tree = html.fromstring(page.content) 
    isin_xpath = '//*[@id="overviewQuickstatsDiv"]/table/tr[6]/td[3]'
    fund['isin'] = extract_xpath(tree, isin_xpath)
    fund['url'] = fund_web_url

    # Rating e rischio
    # https://www.morningstar.it/it/funds/snapshot/snapshot.aspx?id=F0GBR04P4X&tab=2
    fund_web_url_tab_risk = fund_web_url + '&tab=2'

    # Request the page 
    page = requests.get(fund_web_url_tab_risk)
    tree = html.fromstring(page.content) 
    
    # Misure di Volatilità (3 anni) 
    meas_name = '//*[@id="ratingRiskDiv"]/table/tr[1]/td[1]'
    fund['meas_name'] = extract_xpath(tree, meas_name)
    # - Deviazione Std. 
    std_dev = '//*[@id="ratingRiskLeftDiv"]/table/tr[2]/td[2]'
    fund['std_dev'] = extract_xpath(tree, std_dev)
    # - Rendimento Medio
    avg = '//*[@id="ratingRiskLeftDiv"]/table/tr[3]/td[2]'
    fund['avg'] = extract_xpath(tree, avg)
    # - Indice di Sharpe //*[@id="ratingRiskRightDiv"]/table/tbody/tr[2]/td[2]
    sharpe_ratio = '//*[@id="ratingRiskRightDiv"]/table/tr[2]/td[2]'
    fund['sharpe_ratio'] = extract_xpath(tree, sharpe_ratio)
    # Indicatori Modern Portfolio Theory (MPT - 3 anni)
    # - MPT Index 
    mpt_index_name = '//div[@id="ratingMptStatsDiv"]/table/tr[3]/td[2]'
    fund['mpt_index_name'] = extract_xpath(tree, mpt_index_name)
    # - Beta //*[@id="ratingMptStatsDiv"]/table/tbody/tr[4]/td[2]
    mpt_index_beta = '//*[@id="ratingMptStatsDiv"]/table/tr[4]/td[2]'
    fund['mpt_index_beta'] = extract_xpath(tree, mpt_index_beta)
    #   - Alfa //*[@id="ratingMptStatsDiv"]/table/tbody/tr[5]/td[2]
    mpt_index_alpha = '//*[@id="ratingMptStatsDiv"]/table/tr[5]/td[2]'
    fund['mpt_index_alpha'] = extract_xpath(tree, mpt_index_alpha)
    # - Best Fit Index //*[@id="ratingMptStatsDiv"]/table/tbody/tr[3]/td[3]
    bestfit_index_name = '//*[@id="ratingMptStatsDiv"]/table/tr[3]/td[3]'
    fund['bestfit_index_name'] = extract_xpath(tree, bestfit_index_name)
    #   - Beta //*[@id="ratingMptStatsDiv"]/table/tbody/tr[4]/td[3]
    bestfit_index_beta = '//*[@id="ratingMptStatsDiv"]/table/tr[4]/td[3]'
    fund['bestfit_index_beta'] = extract_xpath(tree, bestfit_index_beta)
    #   - Alfa //*[@id="ratingMptStatsDiv"]/table/tbody/tr[5]/td[3]
    bestfit_index_alfa = '//*[@id="ratingMptStatsDiv"]/table/tr[5]/td[3]'
    fund['bestfit_index_alfa'] = extract_xpath(tree, bestfit_index_alfa)

    return fund


if __name__ == "__main__":
    df = pd.DataFrame()
    
    get_fund_info(fund_web_url)
    df = df.from_dict(fund, orient='index')
    df.to_excel('./foo.xlsx')

