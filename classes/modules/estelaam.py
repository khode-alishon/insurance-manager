import pandas as pd
import json

para_file = r"src\para.xlsx"
bime_shode_file = r"src\bime_shode.xlsx"
bime_name_file = r"src\.bime_name.json"
with open(bime_name_file, "r", encoding="utf8") as f:
    bime_name = dict(json.load(f))
para_tarafe = bime_name.get("para_tarafe")
dandan_tarafe = bime_name.get("dandan_tarafe")
dandan_saghf_tajmiei = bime_name.get("dandan_saghf_tajmiei")
dandan_sagh_fard = bime_name.get("dandan_sagh_fard")
shomare_bime_name = bime_name.get("shomare_bime_name")
bime_name_name = bime_name.get("name")

df = pd.read_excel(para_file)



def get_saghf_dandan(type = "single" ,code_melli_asli = "0000000000", code_personeli_asli = "000000"):
        if code_melli_asli == "0000000000" and code_personeli_asli == "000000":
            print("error")
            return None

def get_saghf_orotez(type = "single" ,code_melli_asli = "0000000000", code_personeli_asli = "000000"):
        if code_melli_asli == "0000000000" and code_personeli_asli == "000000":
            print("error")
            return None

def get_saghf_eynak(type = "single" ,code_melli_asli = "0000000000", code_personeli_asli = "000000"):
        if code_melli_asli == "0000000000" and code_personeli_asli == "000000":
            print("error")
            return None

def get_havale(type = "single" ,code_melli_asli = "0000000000", code_personeli_asli = "000000"):
        if code_melli_asli == "0000000000" and code_personeli_asli == "000000":
            print("error")
            return None

def get_estefade(type = "single" ,code_melli_asli = "0000000000", code_personeli_asli = "000000"):
        if code_melli_asli == "0000000000" and code_personeli_asli == "000000":
            print("error")
            return None