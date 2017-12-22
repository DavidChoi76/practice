import shutil

def SaveDecision(filename):
    f1 = open(Decision_filename_directory, 'r+')
    lines = f1.readlines()
    lines[9] = "simulStart              '%s'                   ! (01) simulation start time -- must be in single quotes \n" % startdate
    lines[10] = "simulFinsh             '%s'                   ! (02) simulation end time -- must be in single quotes \n" % enddate
    lines[12] = 'soilCatTbl                      %s            ! (03) soil-category dateset \n' % method3
    lines[13] = 'vegeParTbl                      %s            ! (04) vegetation category dataset \n' % method4
    lines[14] = 'soilStress                      %s            ! (05) choice of function for the soil moisture control on stomatal resistance \n' % method5
    lines[15] = 'stomResist                      %s            ! (06) choice of function for stomatal resistance \n' % method6
    lines[17] = 'num_method                      %s            ! (07) choice of numerical method \n' % method7
    lines[18] = 'fDerivMeth                      %s            ! (08) method used to calculate flux derivatives \n' % method8
    lines[19] = 'LAI_method                      %s            ! (09) method used to determine LAI and SAI \n' % method9
    lines[20] = 'f_Richards                      %s            ! (10) form of Richards equation \n' % method10
    lines[21] = 'groundwatr                      %s            ! (11) choice of groundwater parameterization \n' % method11
    lines[22] = 'hc_profile                      %s            ! (12) choice of hydraulic conductivity profile \n' % method12
    lines[23] = 'bcUpprTdyn                      %s            ! (13) type of upper boundary condition for thermodynamics \n' % method13
    lines[24] = 'bcLowrTdyn                      %s            ! (14) type of lower boundary condition for thermodynamics \n' % method14
    lines[25] = 'bcUpprSoiH                      %s            ! (15) type of upper boundary condition for soil hydrology \n' % method15
    lines[26] = 'bcLowrSoiH                      %s            ! (16) type of lower boundary condition for soil hydrology \n' % method16
    lines[27] = 'veg_traits                      %s            ! (17) choice of parameterization for vegetation roughness length and displacement height \n' % method17
    lines[28] = 'canopyEmis                      %s            ! (18) choice of parameterization for canopy emissivity \n' % method18
    lines[29] = 'snowIncept                      %s            ! (19) choice of parameterization for snow interception \n' % method19
    lines[30] = 'windPrfile                      %s            ! (20) choice of wind profile through the canopy \n' % method20
    lines[31] = 'astability                      %s            ! (21) choice of stability function \n' % method21
    lines[32] = 'canopySrad                      %s            ! (22) choice of canopy shortwave radiation method \n' % method22
    lines[33] = 'alb_method                      %s            ! (23) choice of albedo representation \n' % method23
    lines[34] = 'compaction                      %s            ! (24) choice of compaction routine \n' % method24
    lines[35] = 'snowLayers                      %s            ! (25) choice of method to combine and sub-divide snow layers \n' % method25
    lines[36] = 'thCondSnow                      %s            ! (26) choice of thermal conductivity representation for snow \n' % method26
    lines[37] = 'thCondSoil                      %s            ! (27) choice of thermal conductivity representation for soil \n' % method27
    lines[38] = 'spatial_gw                      %s            ! (28) choice of method for the spatial representation of groundwater \n' % method28
    lines[39] = 'subRouting                      %s            ! (29) choice of method for sub-grid routing \n' % method29

    f1 = open(Decision_filename_directory, 'a')
    DefaultDecision = Decision_filename_directory  # "Decisions_test.txt"
    AddDecision = filename  # "Decisions.txt"
    shutil.copy(DefaultDecision, AddDecision)

    for line in lines:
        data = line
        f1.write(data)
    f1.close

filename = raw_input("Rename your Decision file: ")
SaveDecision(filename)



