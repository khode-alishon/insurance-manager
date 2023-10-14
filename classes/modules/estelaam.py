import pandas as pd
import json


bime_shode_file = r"src\bime_shode.xlsx"
bime_name_file = r"src\.all_bime_name_ha.json"
with open(bime_name_file, "r", encoding="utf8") as f:
    bime_name_ha = dict(json.load(f))


df = pd.read_excel(bime_shode_file)

bime_shode_bime_name = str(list(df["شماره بیمه نامه"])[1])


def farsi(what):
        return str(what).replace("ي", "ی").replace("ك", "ک")

def get_saghf_dandan():
        if bime_shode_bime_name not in list(bime_name_ha.keys()):
            return "Error, Bime name not defined"
        else:
            saghf_tajmiei_dandan = dict(bime_name_ha.get(bime_shode_bime_name)).get("dandan_saghf_tajmiei")
            index_dandan = []
            ind = 0
            for item in list(df["بیماری"]):
                 if "دندانپزشکی" in farsi(item):
                       index_dandan.append(ind)
                 ind = ind + 1
            print(index_dandan)

def get_saghf_orotez():
        if bime_shode_bime_name not in list(bime_name_ha.keys()):
            return "Error, Bime name not defined"
        else:
            saghf_orotez = dict(bime_name_ha.get(bime_shode_bime_name)).get("orotez_saghf")
            print(saghf_orotez)

def get_saghf_eynak():
        if bime_shode_bime_name not in list(bime_name_ha.keys()):
            return "Error, Bime name not defined"
        else:
            saghf_eynak = dict(bime_name_ha.get(bime_shode_bime_name)).get("saghf_eynak")
            print(saghf_eynak)

def get_havale():
        if bime_shode_bime_name not in list(bime_name_ha.keys()):
            return "Error, Bime name not defined"

def get_estefade():
        if bime_shode_bime_name not in list(bime_name_ha.keys()):
            return "Error, Bime name not defined"

get_saghf_dandan()