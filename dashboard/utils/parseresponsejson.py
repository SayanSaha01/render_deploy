import pandas as pd

from functools import lru_cache

from .datafetch import fetch_data_fromdb

VILLAGE_NAMES = ["Aastha", "Sehore"]
TABLE_NAMES = ["respondent_prof","gen_ho_info","fam_info","mig_status","govt_schemes","water_source",
"source_of_energy","land_holding_info","agri_inputs","agri_products","livestock_nos","major_problems"]

DATA = {"a":1}

#dict of dict of tables
@lru_cache()
def get_data(village_name):
    data = fetch_data_fromdb(village_name) # ["Aastha", "Sehore", "string"]
    DATA = {table:pd.DataFrame(data['data'][table])for table in TABLE_NAMES}
    return DATA


# pprint.pprint(DATA) 