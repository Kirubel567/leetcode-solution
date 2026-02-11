class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        #have two dictionaries, one that store all the files in a list as the content the key(content)
        #the second a dictionary taht stores the files as the key and the path as the value 
        #then iterate over the first dictionary and build the answer from the second mapp 
        
        same_files = defaultdict(list)
        path_holder = {}

        for path in paths: 
            splited = path.split(" ")
            for i in range(1, len(splited)):
                full_path = splited[0] + "/" + splited[i][:splited[i].find("(")]

                same_files[splited[i][splited[i].find("("):]].append(full_path)


        return [duplicate for duplicate in same_files.values() if len(duplicate) > 1]




    