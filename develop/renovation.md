## 24 August 2017

- Installing a mechanism to isolate the requirements of a python project 

`pip install pipreqs`

- This one doesn't work as of yet.

- Perhaps I should move to maintaining a proper conda env for this.


- `cookiecutter` is gonna be my template generator overall and I shall move to `conda` for my environment management and `bazel` for build systems. 

- `pip install cookiecutter`

- Moving the project to this template `cookiecutter https://github.com/drivendata/cookiecutter-data-science`

## 25 August 2017



- Installing the required libs 
``` 
pip install tweepy
conda install -c anaconda jupyter pandas matplotlib numpy bokeh nltk 


```

- I've chunked the jupyter notebooks scripts into separate python files to generate a requirements file

```
eklavya@neanderthal:~/Desktop/ProjectEklavya/Eklavya/DTU_7th_Sem_Project/develop/DTU_7th_Sem_Project$ pipreqs . --force
cat ../INFO: Successfully saved requirements file in ./requirements.txt
eklavya@neanderthal:~/Desktop/ProjectEklavya/Eklavya/DTU_7th_Sem_Project/develop/DTU_7th_Sem_Project$ cat ../re
renovation.md     requirements.txt  
eklavya@neanderthal:~/Desktop/ProjectEklavya/Eklavya/DTU_7th_Sem_Project/develop/DTU_7th_Sem_Project$ cat ../requirements.txt 
pip==9.0.1
click==6.7
requests==2.14.2
requests_oauthlib==0.8.0
pymongo==3.5.1
Django==1.11.4
python-dotenv==0.6.5
mock==2.0.0
nose==1.3.7
setuptools==36.2.7
simplejson==3.11.1
six==1.10.0
unittest2==1.1.0
vcr==0.0.9

```

