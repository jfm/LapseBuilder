from os import listdir

def get_source_file_list(source_folder):
    result_list = []
    full_list = listdir(source_folder)
    for listitem in full_list:
        if listitem.lower().endswith('.jpg'):
            result_list.append(listitem)

    return sorted(result_list)