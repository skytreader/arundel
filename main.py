from bottle import route, run

@route("/")
def root():
    return "Welcome to Arundel"

if __name__ == "__main__":
    run(host="0.0.0.0", port=8000)
