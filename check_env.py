"""
Script to check if the required packages for the workshop are installed 

Author: Bargava Subramanian

"""

import sys

# requirements
has = dict(
    gensim='0.12.4',
    IPython='5.0.0',
    lda='1.0.4',
    matplotlib='1.5.1',   
    numpy='1.11.0',
    pandas='0.19',
    requests='2.11.1',
    scipy='0.17.0',
    seaborn='0.7',
    sklearn='0.18',
    spacy='1.2.0',
    tweepy='3.5.0'
)



returns = 0

# check installed packages
for module in has:
    try:
        _module = module.split('-')[-1]
        __module__ = __import__(_module, globals(), locals(), [], 0)
        exec(f'{_module} = __module__')
    except ImportError:
        print(f"{module}:: {sys.exc_info()[1]}")
        #run.pop(module, None)
        returns += 1


# check required versions
from distutils.version import LooseVersion as V
for module,version in has.items():
    try:
        _module = module.split('-')[-1]
        assert V(eval(_module).__version__) >= V(version)
    except (NameError, AttributeError):
        pass # failed import
    except AssertionError:
        print(f"{module}:: Version >= {version} is required")
        returns += 1

#Check for image
try:
    from PIL import Image
except:
    print("Image not found. Please install pillow package or Image package")

#check for wordcloud
try:
    import wordcloud
except:
    print("wordcloud package not found")


# final report
if not returns:
    print('-'*50)
    print('OK.  All required items installed.')

sys.exit(returns)



