class Target:
    def __init__(self, starting_path, search_criteria):
        self.search_criteria = search_criteria
        self.starting_path = starting_path

    def get_criteria(self):
        return self.search_criteria

    def add_to_list(self, obj, return_list):
        dic = {'path': obj, 'name': obj.name, 'cdate': obj.stat().st_ctime,
               'mdate': obj.stat().st_mtime,
               'adate': obj.stat().st_atime}

        return_list.append(dic)


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
