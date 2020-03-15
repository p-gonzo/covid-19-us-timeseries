import os

def get_or_update_source_data():

    files_in_current_dir = os.listdir()
    if "COVID-19" not in files_in_current_dir:
        print("Cloning down source data")
        os.system("git clone https://github.com/CSSEGISandData/COVID-19.git")
    else:
        print("Updating source data")
        os.system("cd COVID-19 && git pull origin master")


def logistic4(x, A, B, C, D):
    """4PL lgoistic equation."""
    return ((A-D)/(1.0+((x/C)**B))) + D

def residuals(p, y, x):
    """Deviations of data from fitted 4PL curve"""
    A,B,C,D = p
    err = y-logistic4(x, A, B, C, D)
    return err

def peval(x, p):
    """Evaluated value at x with current parameters."""
    A,B,C,D = p
    return logistic4(x, A, B, C, D)