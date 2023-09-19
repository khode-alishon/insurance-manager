import json

settings_path = r"src\settings.json"

defaults = {
    "main_bg" : "ble",
}

def change(what, to_what):
    with open(settings_path, "r+") as file:
        global settings
        settings = dict(json.load(file))
        
        if settings.get(what) == None:
            raise TypeError
        else:
            settings[what] = to_what

    with open(settings_path, "w") as file:
        
        json.dump(settings, file, indent=4)

def force_set(what, to_what):
    with open(settings_path, "r+") as file:
        global settings
        settings = dict(json.load(file))
        settings[what] = to_what

    with open(settings_path, "w") as file:
        
        json.dump(settings, file, indent=4)

def to_default():
    with open(settings_path, "r") as settings_file:
        
        settings = dict(json.load(settings_file))

        for k, v in defaults.items():
            if settings.get(k) == None:
                pass
            else:
                settings[k] = v 

    with open(settings_path, "w") as settings_file:
        json.dump(settings, settings_file, indent=4)

def get(what):
    
    with open(settings_path, "r") as settings_file:
        settings = dict(json.load(settings_file))
        return settings.get(what)

to_default()