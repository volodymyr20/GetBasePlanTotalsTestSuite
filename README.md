Background: getbase.com provides different plan types and time periods combinations to choose from, depending on that the total sum will be calculated.

This is a test suite to check that the total sum is calculated correctly for different plan type & time period combinations - the main file is base_plan_total_tests2.py.

Pre-requisites - software:
1) Windows 7
2) Firefox 46
3) Python 2.7, assuming it's added to PATH variable, including the path to pip.exe
4) Jenkins
5) Git client (either CMD, or UI) + the project repository is cloned locally
6) Also see the dependencies below

Pre-requisites - web-site:
1) a user registered at getbase.com with the trial period expired (included)

Dependencies:
1) Run the following command from the local project repository root folder to install dependencies:
pip install -r prerequisites.txt

Ways to run it: 
1) Manually:
- either double click the main test suite file in Windows explorer
- or go to the path where the project repository is cloned locally and type its name
2) CI:
- create a free style job - an event which will fire it up is of your choice - manually, SI commit, schedule, etc.
- choose add execute Windows batch command as a build step
- specify: <path to python>\python.exe <path to local repository>\base_plan_total_tests2.py 
Note: please replace <...path...> with your actual paths

Disclaimer: This is rather an educational sample than a real life example, not a complete suite neither. Its purpose it to illustrate how Selenium+Python 
can be used for test automation of web sites, provide a base and examples how to create further test cases, and also demonstrate use of Page Object design pattern 
which makes maintenance a lot easier. 