from subprocess import call


class CallPy(object):

    def __init__(self, path):
        self.path = path

    def call_python_file(self):
        call(["python3", "{}".format(self.path)])
    
    def call_streamlit_file(self):
        call(["streamlit run", "{}".format(self.path)])



if __name__ == "__main__":
    CallPy(path="webscrap.py").call_python_file()
    # CallPy(path="app.py").call_streamlit_file()