import os

def get_or_update_source_data():

    files_in_current_dir = os.listdir()
    if "COVID-19" not in files_in_current_dir:
        print("Cloning down source data")
        os.system("git clone https://github.com/CSSEGISandData/COVID-19.git")
    else:
        print("Updating source data")
        os.system("cd COVID-19 && git pull origin master")