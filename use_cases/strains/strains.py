# problem setup
inputMeshName    = "density.gen"
inputTimeStep    = 0
inputFieldName   = "Rho_node"

appFileName = "analyzeApp.xml"
defaultInputFile = "homog1.xml"

cellOperationNames = [ \
  "Compute Displacement Solution 1", \
  "Compute Displacement Solution 2", \
  "Compute Displacement Solution 3", \
  "Compute Displacement Solution 4", \
  "Compute Displacement Solution 5", \
  "Compute Displacement Solution 6" ]

outputMeshName   = "output.exo"
analyzeElemDataNames = [ "strain@0", "strain@1", "strain@2", "strain@3", "strain@4", "strain@5" ]
outputElemDataNames  = [  "StrainXX",  "StrainYY",  "StrainZZ",  "StrainYZ",  "StrainXZ",  "StrainXY" ]
outputElemDataType = "ELEMENT_FIELD"
numElemTerms = len(analyzeElemDataNames)

analyzeNodeDataNames = [ "Solution X", "Solution Y", "Solution Z" ]
outputNodeDataNames  = [  "solution_x", "solution_y", "solution_z" ]
outputNodeDataType = "SCALAR_FIELD"
numNodeTerms = len(analyzeNodeDataNames)


# boilerplate that dynamically loads the mpi library required by Plato.Analyze
import ctypes
ctypes.CDLL("libmpi.so",mode=ctypes.RTLD_GLOBAL)


# load Plato module and create Analyze instance
import PlatoPython
analyze = PlatoPython.Analyze(defaultInputFile, appFileName, "homog")
analyze.initialize();

# load density field from mesh
import exodus
inMesh = exodus.ExodusDB()
inMesh.read(inputMeshName)
inputDensity = inMesh.getNodeData(inputTimeStep, inputFieldName)

# open exodus file for output and configure
outMesh = exodus.ExodusDB()
outMesh.read(inputMeshName)
outMesh.elemVarNames = outputElemDataNames;
outMesh.nodeVarNames = outputNodeDataNames;
numCellSolutions = len(cellOperationNames)
numElemBlocks = 1
outMesh.numElemVars = len(outputElemDataNames)
outMesh.numNodeVars = len(outputNodeDataNames)
outMesh.elemVars = [[[[] for k in range(numElemBlocks)] for j in outputElemDataNames] for i in range(numCellSolutions)]
outMesh.nodeVars = [[[] for i in outputNodeDataNames] for j in range(numCellSolutions)]
outMesh.varTimes = [float(i) for i in range(numCellSolutions)]


# import current design into Analyze instance
inputDataType = "SCALAR_FIELD"
analyze.importData("Topology", inputDataType, inputDensity)


# compute cell solution
for iCell in range(numCellSolutions):
  analyze.compute(cellOperationNames[iCell])

  # export output data from Analyze instance
  iBlock = 0
  for iTerm in range(numElemTerms):
    outMesh.elemVars[iCell][iTerm][iBlock] = analyze.exportData(analyzeElemDataNames[iTerm], outputElemDataType)
  for iTerm in range(numNodeTerms):
    outMesh.nodeVars[iCell][iTerm] = analyze.exportData(analyzeNodeDataNames[iTerm], outputNodeDataType)


# finalize mpi and kokkos.  Not essential, but you'll get warnings otherwise.
analyze.finalize()

# write output
outMesh.write(outputMeshName)
