from os import listdir

def get_names_files():
    from os.path import isfile, join
    names = [f for f in listdir('./src') if isfile(join('./src', f))]
    return names
