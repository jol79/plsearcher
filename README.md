# plsearcher
The idea is to put the keyword that you are searching through the csv dataset and get the visualization on the google map (it can be the places where you've been before and noted to the csv as route points etc.)

# structure: ![alt text](http://url/to/img.png)
Requirements for csv file (cols names):
  Phone_num | Time | Connections | Location
  ![reqs](https://bit.ly/3aDJmCl)
  
Required packages:
  1) python version 3.7 and less
  2) python -m pip install --upgrade pip wheel setuptools
  3) python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew pandas selenium numpy==1.19.3 pillow webdriver_manager

Required software:
  1) Google-Chrome
  
  
 Let’s see the example with test file that you have for testing purposes:
    •	File -> test_dataset.csv
    •	Keyword -> 334251234
  ![alt text](https://bit.ly/3nJPyMN)
  As result the chrome in test software mode will be opened and you’ll see something like this (for single address common google maps tab will be opened (without any       authentication but next example will show you the multiple points situation where email credentials that program asked you on the beginning to provide will be used))
  ![alt text](https://bit.ly/34ItQBq)
  Multiple point example:
    • Keyword -> 123452424
  ![alt text](https://bit.ly/2WK3KcP)
  ![alt text](https://bit.ly/3mSJm3D)
