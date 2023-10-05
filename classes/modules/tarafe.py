import pandas as pd

def get_tarafe(search_argument = "None"):

    result = []
    return_result = []
    df = pd.read_excel(r"src\tarafe.xlsx")
    
    columns = df.columns
    index_CM = columns.get_loc("MelliCode")
    index_SC = columns.get_loc("System Code")
    index_Name = columns.get_loc("Name")
    index_Prince = columns.get_loc("Price")
    index_Note = columns.get_loc("Note")
    index_Motekhases = columns.get_loc("Motekhases")


    try:
        int(search_argument)

    except:
        #SEARCH BY STR
        for row in df["Name"]:
            if row.__contains__(search_argument):
                result.append(pd.Index(df["Name"]).get_loc(row))


    else:
        #SEARCH BY INT
        if len(search_argument) < 3:
            print("Kamtar")
            return_result = [["Name", "Price", "Motekhases", "Note"] ,["None", "None", "None", "None"]]
            return return_result
        else:
            if len(search_argument) == 3 or len(search_argument) == 4:
                for row in df["System Code"]:
                    if str(row).__contains__(search_argument):
                        result.append(pd.Index(df["System Code"]).get_loc(row))
            else:
                for row in df["MelliCode"]:
                    if str(row).__contains__(search_argument):
                        result.append(pd.Index(df["MelliCode"]).get_loc(row))


    def get(search_index,what):
        return str(df[what].values[search_index])

    return_result.append(["Name", "Price", "Motekhases", "Note"])

    for index in list(result):
        price = f"{get(index, 'Price')}"

        return_result.append([get(index,"Name"), price , get(index, "Motekhases"), get(index,"Note")])


    return return_result
