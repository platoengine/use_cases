# problem setup
inputMeshName    = "density.exo"
inputTimeStep    = 0
inputFieldName   = "Rho_node"

appFileName = "analyzeApp.xml"
defaultInputFile = "homog1.xml"

cellOperationNames = [ \
  "Compute Effective Energy 1", \
  "Compute Effective Energy 2", \
  "Compute Effective Energy 3", \
  "Compute Effective Energy 4", \
  "Compute Effective Energy 5", \
  "Compute Effective Energy 6" ]

outputMeshName   = "output.exo"
analyzeDataNames = [ "Objective Gradient" ]
outputDataNames  = [ "Objective_Gradient" ]
outputDataType = "SCALAR_FIELD"
numTerms = len(analyzeDataNames)


# boilerplate that dynamically loads the mpi library required by Plato.Analyze
import ctypes
ctypes.CDLL("libmpi.so",mode=ctypes.RTLD_GLOBAL)


# load Plato module and create Analyze instance
import PlatoPython
analyze = PlatoPython.Analyze(defaultInputFile, appFileName, "homog1")
analyze.initialize();

# load density field from mesh
import exodus
inMesh = exodus.ExodusDB()
inMesh.read(inputMeshName)
inputDensity = inMesh.getNodeData(inputTimeStep, inputFieldName)

# open exodus file for output and configure
outMesh = exodus.ExodusDB()
outMesh.read(inputMeshName)
outMesh.nodeVarNames = outputDataNames;
numCellSolutions = len(cellOperationNames)
numTimes = numCellSolutions+1
outMesh.numNodeVars = len(outputDataNames)
outMesh.nodeVars = [[[] for i in outputDataNames] for j in range(numTimes)]
outMesh.varTimes = [float(i) for i in range(numTimes)]


# import current design into Analyze instance
inputDataType = "SCALAR_FIELD"
analyze.importData("Topology", inputDataType, inputDensity)


# compute cell solutions
for iCell in range(numCellSolutions):
  analyze.compute(cellOperationNames[iCell])

  # export output data from Analyze instance
  for iTerm in range(numTerms):
    outMesh.nodeVars[iCell][iTerm] = analyze.exportData(analyzeDataNames[iTerm], outputDataType)


# compute multi-objective
assumedStrain = [0.0,0.0,0.0,1.0,1.0,1.0]
numNodes = len(outMesh.nodeVars[0][0])
objIndex = 0
outMesh.nodeVars[numCellSolutions][objIndex] = [0.0 for iNode in range(numNodes)]
for iNode in range(numNodes):
  for iTime in range(numCellSolutions):
    outMesh.nodeVars[numCellSolutions][objIndex][iNode] += assumedStrain[iTime]*outMesh.nodeVars[iTime][objIndex][iNode]

# finalize mpi and kokkos.  Not essential, but you'll get warnings otherwise.
analyze.finalize()

# write output
outMesh.write(outputMeshName)
