from bottle import request, route, run
from elasticsearch import Elasticsearch

es_indexer = Elasticsearch(["elasticsearch:9200", "elasticsearch:9300"])
INDEX_NAME = "codex-arundel"


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

@route("/_index", method="POST")
def index():
    filename = request.forms["filename"]
    body = request.body.read()
    document = {
        "filename": filename,
        "body": str(body)
    }

    es_indexer.index(index=INDEX_NAME, id=1, body=document)
    return "OK"

@route("/")
def root():
    return "Welcome to Arundel"

if __name__ == "__main__":
    run(host="0.0.0.0", port=8000)
