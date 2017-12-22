#!/bin/bash

# Used to run the test cases for SUMMA

# There are two classes of test cases:
#  1) Test cases based on synthetic/lab data; and
#  2) Test cases based on field data.

# The commands assume that you are in the directory {localInstallation}/settings/
# and that the control files are in {localInstallation}/settings/

# Set the SUMMA executable (e.g. /usr/local/bin/summa.exe or wherever you have installed SUMMA)
SUMMA_EXE=/home/hydro/summa/summa-master/bin/summa.exe

if  [ -z ${SUMMA_EXE} ]
    then
        echo "Must define the SUMMA executable SUMMA_EXE in $0"
        exit 1
fi

# *************************************************************************************************
# * PART 1: TEST CASES BASED ON SYNTHETIC OR LAB DATA

${SUMMA_EXE} -p never -s _1dRichards          -m settings/wrrPaperTestCases/figure09/summa_fileManager_1dRichards.txt

${SUMMA_EXE} -p never -s _1dRichards          -m settings/wrrPaperTestCases/figure09/summa_fileManager_1dRichards1.txt

${SUMMA_EXE} -p never -s _1dRichards          -m settings/wrrPaperTestCases/figure09/summa_fileManager_1dRichards2.txt

# End of test cases based on field data
# *************************************************************************************************
