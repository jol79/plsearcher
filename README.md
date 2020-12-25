# plsearcher
The idea is to put the keyword that you are searching through the csv dataset and get the visualization on the google map (it can be the places where you've been before and noted to the csv as route points etc.)

Requirements for csv file (cols names):
  Phone_num | Time | Connections | Location
  ![HomeInterface](https://user-images.githubusercontent.com/41474876/103136845-8a26bf80-46cc-11eb-957e-2b51476acd04.png)
  ![Reqs](https://user-images.githubusercontent.com/41474876/103136939-4f715700-46cd-11eb-939a-433e5835a974.png)
  
Required packages:
  1) python version 3.7 and less
  2) python -m pip install --upgrade pip wheel setuptools
  3) python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew pandas selenium numpy==1.19.3 pillow webdriver_manager

Required software:
  1) Google-Chrome
  
  
 Let’s see the example with test file that you have for testing purposes:
    •	File -> test_dataset.csv
    •	Keyword -> 334251234
  ![ExampleHomePage](https://user-images.githubusercontent.com/41474876/103136961-6fa11600-46cd-11eb-9d29-54ffc4413e15.png)
  As result the chrome in test software mode will be opened and you’ll see something like this (for single address common google maps tab will be opened (without any       authentication but next example will show you the multiple points situation where email credentials that program asked you on the beginning to provide will be used))
  ![ExampleGoogleMapSinglePoint](https://user-images.githubusercontent.com/41474876/103136969-792a7e00-46cd-11eb-9e46-cf3474a7ada8.png)
  Multiple point example:
    • Keyword -> 123452424
  ![ExampleGooglePointsList](https://user-images.githubusercontent.com/41474876/103136978-8a738a80-46cd-11eb-9114-59c3bead689f.png)
  ![ExampleGoogleMapMultiplePoints](https://user-images.githubusercontent.com/41474876/103136981-92332f00-46cd-11eb-81dc-670dedb087ec.png)
