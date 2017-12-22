def SetSoilCategoryDatasetFunction(method3):
    #method3 = raw_input("Select STAS or STAS-RUC or ROSETTA : ")
    if method3 == "STAS" or method3 == "STAS-RUC" or method3 == "ROSETTA":
        print("Input is correct !!")
    else:
        print("Check your input !! ")
    return method3

# (03) soil-category dateset
method3 = raw_input("Select STAS or STAS-RUC or ROSETTA : ")
SetSoilCategoryDatasetFunction(method3)

def SetVegetationCategoryDatasetFunction(method):
    method4 = input("Select USGS or MODIFIED_IGBP_MODIS_NOAH : ")
    return method4



def SetSoilMoistureControlFunction(method):
    method5 = input("Select NoahType or CLM_Type or ROSETTA : ")
    return method5

def SetStomatalResistanceFunction(method):
    method6 = input("Select BallBerry or Jarvis : ")
    return method6

def SetNumericalMethodFunction(method):
    method7 = input("Select itertive or non_iter or itersurf : ")
    return method7

def SetFluxDerivativesFunction(method):
    method8 = input("Select numericl or analytic : ")
    return method8

def SetLAIandSAIFunction(method):
    method9 = input("Select monTable or specified : ")
    if (method9 != 'monTable') or (method9 != 'specified') :
        print ("Check your input !! ")
    if (method9 == 'specified') :
        print ("LAI and SAI method option ['specified'] is no longer supported !! ")
    return method9

def SetRichardsEquationFunction(method):
    method10 = input("Select moisture or mixdform : ")
    return method10

def SetGroundwaterRarameterizationFunction(method):
    method11 = input("Select qTopmodl or bigBuckt or noXplict : ")
    if (method11 != 'qTopmodl') or (method11 != 'bigBuckt') or (method11 != 'noXplict'):
        print ("Check your input !! ")
    if (method11 == 'bigBuckt') :
        print ("If you select 'bigBuckt', you have select 'singleBasin' at (28) choice of method for the spatial representation of groundwater !! ")
    return method11

def SetHydraulicConductivityProfileFunction(method):
    method12 = input("Select constant or pow_prof : ")
    return method12

def SetUpperBoundaryConditionsForThermodynamicsFunction(method):
    method13 = input("Select presTemp or nrg_flux : ")
    return method13

def SetLowerBoundaryConditionsForThermodynamicsFunction(method):
    method14 = input("Select presTemp or zeroFlux : ")
    return method14

def SetUpperBoundaryConditionsForSoilHydrologyFunction(method):
    method15 = input("Select presHead or liq_flux : ")
    return method15

def SetLowerBoundaryConditionsForSoilHydrologyFunction(method):
    method16 = input("Select drainage or presHead or bottmPsi or zeroFlux : ")
    return method16

def SetParameterizationForVegetationFunction(method):
    method17 = input("Select Raupach_BLM1994 or CM_QJRMS1998 or vegTypeTable : ")
    return method17

def SetParameterizationForCanopyEmissivityFunction(method):
    method18 = input("Select simplExp or difTrans : ")
    return method18

def SetParameterizationForSnowInterceptionFunction(method):
    method19 = input("Select stickySnow or lightSnow : ")
    return method19

def SetWindProfileFunction(method):
    method20 = input("Select exponential or logBelowCanopy : ")
    return method20

def SetStabilityFunction(method):
    method21 = input("Select standard or louisinv or mahrtexp : ")
    return method21

def SetCanopyShortwaveRadiationMethodFunction(method):
    method22 = input("Select noah_mp or CLM_2stream or UEB_2stream or NL_scatter or BeersLaw : ")
    return method22

def SetAlbedoRepresentationFunction(method):
    method23 = input("Select conDecay or varDecay : ")
    return method23

def SetCompactionRoutineFunction(method):
    method24 = input("Select consettl or anderson : ")
    return method24

def SetSnowLayersFunction(method):
    method25 = input("Select CLM_2010 or jrdn1991 : ")
    return method25

def SetThermalConductivityRepresentationForSnowFunction(method):
    method26 = input("Select tyen1965 or melr1977 or jrdn1991 or smnv2000 : ")
    return method26

def SetThermalConductivityRepresentationForSoilFunction(method):
    method27 = input("Select funcSoilWet or mixConstit or hanssonVZJ : ")
    return method27

def SetSpatialRepresentationOfGroundwaterFunction(method):
    method28 = input("Select localColumn or singleBasin : ")
    return method28

def SetSubGridRoutingFunction(method):
    method29 = input("Select timeDlay or qInstant : ")
    return method29