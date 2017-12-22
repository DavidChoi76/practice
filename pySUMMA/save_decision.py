with open('summa_zDecisions_1dRichards2.txt', 'r') as infile:
    data = infile.read()
my_list = data.splitlines()


def savemethod(string):
    f = open("summa_zDecisions_1dRichards2.txt", "r")
    lines = f.readlines()
    lines[9] = "simulStart              '%s'                   ! (01) simulation start time -- must be in single quotes \n" % entry1.get()
    lines[10] = "simulFinsh             '%s'                   ! (02) simulation end time -- must be in single quotes \n" % entry2.get()
    lines[12] = 'soilCatTbl                      %s            ! (03) soil-category dateset \n' % combobox3.get()
    lines[13] = 'vegeParTbl                      %s            ! (04) vegetation category dataset \n' % combobox4.get()
    lines[14] = 'soilStress                      %s            ! (05) choice of function for the soil moisture control on stomatal resistance \n' % combobox5.get()
    lines[15] = 'stomResist                      %s            ! (06) choice of function for stomatal resistance \n' % combobox6.get()
    lines[17] = 'num_method                      %s            ! (07) choice of numerical method \n' % combobox7.get()
    lines[18] = 'fDerivMeth                      %s            ! (08) method used to calculate flux derivatives \n' % combobox8.get()
    lines[19] = 'LAI_method                      %s            ! (09) method used to determine LAI and SAI \n' % combobox9.get()
    lines[20] = 'f_Richards                      %s            ! (10) form of Richards equation \n' % combobox10.get()
    lines[21] = 'groundwatr                      %s            ! (11) choice of groundwater parameterization \n' % combobox11.get()
    lines[22] = 'hc_profile                      %s            ! (12) choice of hydraulic conductivity profile \n' % combobox12.get()
    lines[23] = 'bcUpprTdyn                      %s            ! (13) type of upper boundary condition for thermodynamics \n' % combobox13.get()
    lines[24] = 'bcLowrTdyn                      %s            ! (14) type of lower boundary condition for thermodynamics \n' % combobox14.get()
    lines[25] = 'bcUpprSoiH                      %s            ! (15) type of upper boundary condition for soil hydrology \n' % combobox15.get()
    lines[26] = 'bcLowrSoiH                      %s            ! (16) type of lower boundary condition for soil hydrology \n' % combobox16.get()
    lines[27] = 'veg_traits                      %s            ! (17) choice of parameterization for vegetation roughness length and displacement height \n' % combobox17.get()
    lines[28] = 'canopyEmis                      %s            ! (18) choice of parameterization for canopy emissivity \n' % combobox18.get()
    lines[29] = 'snowIncept                      %s            ! (19) choice of parameterization for snow interception \n' % combobox19.get()
    lines[30] = 'windPrfile                      %s            ! (20) choice of wind profile through the canopy \n' % combobox20.get()
    lines[31] = 'astability                      %s            ! (21) choice of stability function \n' % combobox21.get()
    lines[32] = 'canopySrad                      %s            ! (22) choice of canopy shortwave radiation method \n' % combobox22.get()
    lines[33] = 'alb_method                      %s            ! (23) choice of albedo representation \n' % combobox23.get()
    lines[34] = 'compaction                      %s            ! (24) choice of compaction routine \n' % combobox24.get()
    lines[35] = 'snowLayers                      %s            ! (25) choice of method to combine and sub-divide snow layers \n' % combobox25.get()
    lines[36] = 'thCondSnow                      %s            ! (26) choice of thermal conductivity representation for snow \n' % combobox26.get()
    lines[37] = 'thCondSoil                      %s            ! (27) choice of thermal conductivity representation for soil \n' % combobox27.get()
    lines[38] = 'spatial_gw                      %s            ! (28) choice of method for the spatial representation of groundwater \n' % combobox28.get()
    lines[39] = 'subRouting                      %s            ! (29) choice of method for sub-grid routing \n' % combobox29.get()

    f = open('SUMMA_zDecision_Test.txt', 'a')
    for line in lines:
        data = line
        f.write(data)
    f.close