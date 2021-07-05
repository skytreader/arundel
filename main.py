from bottle import route, run

class IndexIgnore(object):

    def __init__(self, ignorefilename=None):
        self.ignores = set()
        if ignorefilename:
            with open(ignorefilename) as ignorefile:
                for line in ignorefile:
                    self.ignores.add(self.__normalize_dirname(line))

    def __normalize_dirname(self, dirname):
        dir_stripped = dirname.strip()
        if dir_stripped[-1] == '/':
            return dir_stripped[:-1]
        
        return dir_stripped

    def should_ignore(self, dirname):
        return self.__normalize_dirname(dirname) in self.ignores
    
    def extend(self, ignorefilename):
        new_indexignore = IndexIgnore(ignorefilename)
        for item in self.ignores:
            new_indexignore.add(item)
        return new_indexignore

@route("/")
def root():
    return "Welcome to Arundel"

if __name__ == "__main__":
    run(host="0.0.0.0", port=8000)
