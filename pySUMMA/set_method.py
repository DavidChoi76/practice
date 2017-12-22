# (03) soil-category dateset
def SetSoilCategoryDatasetFunction(method3):
    if (method3 == "STAS") or (method3 == "STAS-RUC") or (method3 == "ROSETTA"):
        print("Input is correct !!")
    else:
        print("Check your input !! ")
    return method3

# (03) soil-category dateset
method3 = raw_input("Select STAS or STAS-RUC or ROSETTA : ")
SetSoilCategoryDatasetFunction(method3)


# (09) method used to determine LAI and SAI
def SetLAIandSAIFunction(method9):
    if (method9 == "monTable") or (method9 == "specified"):
        print("Input is correct !!")
    else:
        print("Check your input !! ")

    if (method9 == 'specified') :
        print ("LAI and SAI method option ['specified'] is no longer supported !! Change your method to 'monTable")
    return method9

# (09) method used to determine LAI and SAI
method9 = raw_input("Select monTable or specified : ")
SetLAIandSAIFunction(method9)


# (11) choice of groundwater parameterization
def SetGroundwaterRarameterizationFunction(method11):
    if (method11 == 'qTopmodl') or (method11 == 'bigBuckt') or (method11 == 'noXplict'):
        print("Input is correct !!")
    else:
        print("Check your input !! ")

    if (method11 == 'bigBuckt') :
        print ("If you select 'bigBuckt', you have select 'singleBasin' at (28) choice of method for the spatial representation of groundwater !! ")
    return method11

# (11) choice of groundwater parameterization
method11 = raw_input("Select qTopmodl or bigBuckt or noXplict : ")
SetGroundwaterRarameterizationFunction(method11)


# (04) vegetation category dataset
def SetVegetationCategoryDatasetFunction(method4):
    if (method3 == "USGS") or (method3 == "MODIFIED_IGBP_MODIS_NOAH"):
        print("Input is correct !!")
    else:
        print("Check your input !! ")
    return method4

# (04) vegetation category dataset
method4 = raw_input("Select USGS or MODIFIED_IGBP_MODIS_NOAH : ")
SetVegetationCategoryDatasetFunction(method4)


# (05) choice of function for the soil moisture control on stomatal resistance
def SetSoilMoistureControlFunction(method):
    method5 = input("Select NoahType or CLM_Type or ROSETTA : ")
    return method5

# (06) choice of function for stomatal resistance
def SetStomatalResistanceFunction(method):
    method6 = input("Select BallBerry or Jarvis : ")
    return method6

# (07) choice of numerical method
def SetNumericalMethodFunction(method):
    method7 = input("Select itertive or non_iter or itersurf : ")
    return method7

# (08) method used to calculate flux derivatives
def SetFluxDerivativesFunction(method):
    method8 = input("Select numericl or analytic : ")
    return method8

# (10) form of Richards' equation
def SetRichardsEquationFunction(method):
    method10 = input("Select moisture or mixdform : ")
    return method10

# (12) choice of hydraulic conductivity profile
def SetHydraulicConductivityProfileFunction(method):
    method12 = input("Select constant or pow_prof : ")
    return method12

# (13) choice of upper boundary conditions for thermodynamics
def SetUpperBoundaryConditionsForThermodynamicsFunction(method):
    method13 = input("Select presTemp or nrg_flux : ")
    return method13

# (14) choice of lower boundary conditions for thermodynamics
def SetLowerBoundaryConditionsForThermodynamicsFunction(method):
    method14 = input("Select presTemp or zeroFlux : ")
    return method14

# (15) choice of upper boundary conditions for soil hydrology
def SetUpperBoundaryConditionsForSoilHydrologyFunction(method):
    method15 = input("Select presHead or liq_flux : ")
    return method15

# (16) choice of lower boundary conditions for soil hydrology
def SetLowerBoundaryConditionsForSoilHydrologyFunction(method):
    method16 = input("Select drainage or presHead or bottmPsi or zeroFlux : ")
    return method16

# (17) choice of parameterization for vegetation roughness length and displacement height
def SetParameterizationForVegetationFunction(method):
    method17 = input("Select Raupach_BLM1994 or CM_QJRMS1998 or vegTypeTable : ")
    return method17

# (18) choice of parameterization for canopy emissivity
def SetParameterizationForCanopyEmissivityFunction(method):
    method18 = input("Select simplExp or difTrans : ")
    return method18

# (19) choice of parameterization for snow interception
def SetParameterizationForSnowInterceptionFunction(method):
    method19 = input("Select stickySnow or lightSnow : ")
    return method19

# (20) choice of wind profile
def SetWindProfileFunction(method):
    method20 = input("Select exponential or logBelowCanopy : ")
    return method20

# (21) choice of stability function
def SetStabilityFunction(method):
    method21 = input("Select standard or louisinv or mahrtexp : ")
    return method21

# (22) choice of canopy shortwave radiation method
def SetCanopyShortwaveRadiationMethodFunction(method):
    method22 = input("Select noah_mp or CLM_2stream or UEB_2stream or NL_scatter or BeersLaw : ")
    return method22

# (23) choice of albedo representation
def SetAlbedoRepresentationFunction(method):
    method23 = input("Select conDecay or varDecay : ")
    return method23

# (24) choice of compaction routine
def SetCompactionRoutineFunction(method):
    method24 = input("Select consettl or anderson : ")
    return method24

# (25) choice of method to combine and sub-divide snow layers
def SetSnowLayersFunction(method):
    method25 = input("Select CLM_2010 or jrdn1991 : ")
    return method25

# (26) choice of thermal conductivity representation for snow
def SetThermalConductivityRepresentationForSnowFunction(method):
    method26 = input("Select tyen1965 or melr1977 or jrdn1991 or smnv2000 : ")
    return method26

# (27) choice of thermal conductivity representation for soil
def SetThermalConductivityRepresentationForSoilFunction(method):
    method27 = input("Select funcSoilWet or mixConstit or hanssonVZJ : ")
    return method27

# (28) choice of method for the spatial representation of groundwater
def SetSpatialRepresentationOfGroundwaterFunction(method):
    method28 = input("Select localColumn or singleBasin : ")
    return method28

# (29) choice of method for sub-grid routing
def SetSubGridRoutingFunction(method):
    method29 = input("Select timeDlay or qInstant : ")
    return method29