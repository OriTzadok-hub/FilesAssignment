import datetime


class Target:
    def __init__(self, starting_path, search_criteria):
        self.search_criteria = search_criteria
        self.starting_path = starting_path

    #this functions adds all the file's information to a dictionary and then adds the dictionary to the shared array
    def add_to_list(self, obj, return_list):
        dic = {'<FolderPath>': obj, '<FileName>': obj.name, '<CreationDate>': self.convert_date(obj.stat().st_ctime),
               '<ModifiedDate>': self.convert_date(obj.stat().st_mtime),
               '<DateAccessed>': self.convert_date(obj.stat().st_atime)}

        return_list.append(dic)

    def convert_date(self, timestamp):
        d = datetime.datetime.utcfromtimestamp(timestamp)
        formated_date = d.strftime('%d %b %Y')
        return formated_date


class TargetDiv(Target):
    def find_target(self, return_list):
        for p in self.starting_path.rglob(self.search_criteria):
            if p.is_dir():
                self.add_to_list(p, return_list)


class TargetFile(Target):
    def find_target(self, return_list):
        for p in self.starting_path.rglob(self.search_criteria):
            if p.is_file():
                self.add_to_list(p, return_list)
