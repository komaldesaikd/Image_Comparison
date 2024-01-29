# Image_Comparison
This task contains test script for open and image and compare with another image

# Prerequisite
Following libraries should be installed to run the test script.</br>
1. PIL </br>
2. pytest </br>
3. pytest-html </br>
4. pytest-depends </br>
5. logging </br></br>

# Execution

The test script should be run using following pytest command. </br>
**pytest -v -s --html=<current_location>\Results\report_testcompare.html .\test_Image_Compare.py** </br>

# Results

After execution, test run results will be generated under **Results** folder. </br>
It contains following files: </br>
1. IMAGE_DIFFERENCE.png file: This file contains image comparison difference. </br>
2. Test_Chaos_Image_Task.log file: This file contains logs for test script. </br>
3. report_testcompare.html file: This file contains error html report along with all testases with PASS/FAIL results. </br>
