USAGE

System Requirements:
1. Python 3
!!! Install Dependencies FIRST
2. Install NLTK http://www.nltk.org/install.html
3. Insall NLTK libraries:
	launch python
	import nltk
	nltk.download('punkt')
	nltk.download('averaged_perceptron_tagger')
4. Install newspaper “pip3 install newspaper3k”
4. Install Watson Developer Cloud "pip3 install --upgrade watson_developer_cloud"

Dependencies "sudo pipenv install xxx"
1. requests
2. pysolr
3. argparse
4. pyOpenSSL
5. python-dateutil
6. responses

Sub-Dependencies:
pip
pipenv

python3 compile.py -> currently generates four csv files to load


#Reference Filter:
#python reference-filt.py <article title> <MMddYYYY>
#python reference-filt.py "North Korea decides to invest in Bitcoin" "11222017"
#
#Politic Filter:
#python politic-filt.py <democraft reference> <republican reference> <text file>
#python politic-filt.py "Democrat Platform.txt" "Republican Platform.txt" "input.txt"
#
#Emotion Filter:
#python emotion-filt.py <text file>
#python emotion-filt.py "input.txt"

