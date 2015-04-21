# -*- coding: UTF-8 -*-
# Author: daniel roca roca486@gmail.com
# PAC 2 IAA - UOC 2015

import fileProcessing as fp
import numpy as np

# --- Activitat 1  --- #
rawData = fp.readFileData()
normalised = fp.dataNormalization(rawData)
print("The number of components needed for the 95% variance acceptance is: ", 
	fp.pcaComponentsCalc(normalised))



