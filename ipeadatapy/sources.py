import pandas as pd
from .api_call import api_call

def sources():
    api = "http://ipeadata2-homologa.ipea.gov.br/api/v1/Fontes"
    return api_call(api).rename(index=str, columns={"FNTID": "ID", "FNTSIGLA": "SIGLA"})['SIGLA']
