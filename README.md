Baseball counting program (python3)
-----------------------------------------------.

--------Description and Architecture :

This program downloads files of Major League Baseball data, parses it and returns a list of triples of teams for which at least 50 players have played for all three teams.

The files are :

-Baseball.py 
-Main.py
-parameters.cfg
-requirements.txt
-Readme.md
-Test.py
-Simulated_data_2000_2000.csv
-Complexity.pdf

* Baseball class handles the program

* Main runs the program with the parameters given

* requirements contains the library pandas

* parameters.cfg contains the parameters : starting year for the study (default=1871), the last year (default=2014), and the Threshold of players in each triplet (default= 50)

* Test of the program is made with unittest

* Simulated_data_2000_2000.csv is created manually and contains 12 lines corresponding to football data (famous players with their corresponding teams)
The Test file needs it.

* Complexity.pdf provides a Spatial and Time complexity analysis.


---------Run the program:

-Install dependancies : 'pip install -r requirements.txt'
-Set parameters in parameters.cfg 
-Run 'python3 Main.py'

