import os
import shutil

def build():
    try:
        shutil.rmtree('build')
    except:
        pass
    try:
        shutil.rmtree('dist')
    except:
        pass
    try:
        shutil.rmtree('GolfGTI.egg-info')
    except:
        pass
    
    os.system('python setup.py check')
    os.system('python setup.py sdist')
    os.system('python setup.py bdist_wheel')

if __name__ == '__main__':
    build()