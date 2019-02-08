# CSP_Sudoku
Implementation, comparation and testing of CSP solver algorithms based on Backtracking. <br />

__Implementation__ of different inference strategies (__csp.py__) : 
1. Pure backtracking
2. Backtracking with forward checking (FC)
3. Maintaining arc consistency (MAC).

__Comparation__ of the strategies in terms of _time complexity_ and _number of backtracks_. <br />
__Testing__ on _Sudoku_ game instances.

The code in csp.py was taken from AIMA repository (https://github.com/aimacode/aima-python) with little modifications to simplify the algorithms and remove dependencies from other files (check comments for further info). 

All the work and results are explained in the PDF paper included in this repository. <br />
To reproduce the results of the paper you have to modify the parameters in __main.py__ according to the test you want to execute (more detailed information can be found in the comments of the code) and then run it from there. <br />


Python 3.6 or later is required to run the application.
