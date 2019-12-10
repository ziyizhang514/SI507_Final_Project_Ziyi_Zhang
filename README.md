# Project Title

SI507 Final Project


## Data Source

1. Wikipedia
  'https://en.wikipedia.org/wiki/List_of_state_and_territorial_universities_in_the_United_States'

2. Wikipedia
  483 pages of universities like 'https://en.wikipedia.org/wiki/Alabama_A%26M_University'

3. Foursquare
  Information of any venues needed when Running

4. 2019 QS World Unversiy Rankings
  CSV of 1000 records downloaded from topuniversities.com


## Information about create cache files/database

Please unzip the cache_file.zip and move inside files into the same route of py file

In py file, write code 'createbdall()', then the database will be dropped and rebuilt


## Project Structure

1. The project gets data from wikipedia and a specific csv and saved raw results in cache files
2. Use function 'createbdall' to call all related functions needed for building the database
3. Use serial functions begin with 'db_' to process data for later presentation
4. Use Flask names 'app' to give visual output to user


## User Guide (After running the py file)

1. Find cafes near specific university:
  e.g. input in explorer: "127.0.0.1:5000/nearbycafe/University of Michigan"
  * several options provided

2. Get list of universities in United States ordered by its name or year of establishment:
  e.g. input in explorer: '127.0.0.1:5000/universitylist/name'
  * 2 options provided

3. Get list of regions and their numbers of universities in QS Rankings ordered by average score of local universities:
  e.g. input in explorer: '127.0.0.1:5000/score'
  * only 1 option provided

4. Get list of America universities ordered by its rank in 2019 or 2018:
  e.g. input in explorer: '127.0.0.1:5000/universityrankings/2019 rank'
  * 2 options provided

5. Get official website of specific university and get a link hich can redirect you to the site:
  e.g. input in explorer: '127.0.0.1:5000/website/University of Michigan'
  * several options provided

6. Get map of the university and its nearby venues:
  e.g. input in explorer: '127.0.0.1:5000/map/University of Michigan'
  * several options provided


## Author

* Ziyi Zhang
