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
analyzeDataNames = [ "Solution X", "Solution Y", "Solution Z"]
outputDataNames  = [ "Solution_X", "Solution_Y", "Solution_Z"]
outputDataType = "SCALAR_FIELD"
numTerms = len(analyzeDataNames)


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
outMesh.nodeVarNames = outputDataNames;
numCellSolutions = len(cellOperationNames)
outMesh.numNodeVars = len(outputDataNames)
outMesh.nodeVars = [[[] for i in outputDataNames] for j in range(numCellSolutions)]
outMesh.varTimes = [float(i) for i in range(numCellSolutions)]


# import current design into Analyze instance
inputDataType = "SCALAR_FIELD"
analyze.importData("Topology", inputDataType, inputDensity)


# compute cell solution
for iCell in range(numCellSolutions):
  analyze.compute(cellOperationNames[iCell])

  # export output data from Analyze instance
  for iTerm in range(numTerms):
    outMesh.nodeVars[iCell][iTerm] = analyze.exportData(analyzeDataNames[iTerm], outputDataType)


# finalize mpi and kokkos.  Not essential, but you'll get warnings otherwise.
analyze.finalize()

# write output
outMesh.write(outputMeshName)
