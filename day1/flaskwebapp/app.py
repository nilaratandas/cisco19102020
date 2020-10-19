from  flask  import  Flask
myapp=Flask(__name__)


@myapp.route('/')
def   hello():
    return "welcome to python Flask with Docker"


if  __name__ ==   "__main__" :
    myapp.run(host='0.0.0.0',port=5000,debug=True)
