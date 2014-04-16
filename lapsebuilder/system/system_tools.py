from os import listdir


class FileTools():

    def __init__(self):
        pass

    @staticmethod
    def get_source_file_list(source_folder):
        result_list = []
        full_list = listdir(source_folder)
        for listitem in full_list:
            if listitem.lower().endswith('.jpg'):
                result_list.append(source_folder + '/' + listitem)
                
        return sorted(result_list)