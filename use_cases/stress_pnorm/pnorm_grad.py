# problem setup

analyzeElemDataNames = [ "stress@0", "stress@1", "stress@2", "stress@3", "stress@4", "stress@5" ]
outputElemDataNames  = [  "StressXX",  "StressYY",  "StressZZ",  "StressYZ",  "StressXZ",  "StressXY" ]
outputElemDataType = "ELEMENT_FIELD"
numElemTerms = len(analyzeElemDataNames)

analyzeNodeDataNames = [ "Solution X", "Solution Y", "Solution Z", "Objective Gradient", "Constraint Gradient" ]
outputNodeDataNames  = [  "solution_x", "solution_y", "solution_z", "pnorm_grad", "vol_grad" ]
outputNodeDataType = "SCALAR_FIELD"
numNodeTerms = len(analyzeNodeDataNames)


# boilerplate that dynamically loads the mpi library required by Plato.Analyze
import ctypes
ctypes.CDLL("libmpi.so",mode=ctypes.RTLD_GLOBAL)

# load Plato module and create Analyze instance
import Plato
analyze = Plato.Analyze("stress_pnorm.xml", "alexaApp.xml", "pnorm")
analyze.initialize();

# load density field from mesh
import exodus
inMesh = exodus.ExodusDB()
inMesh.read("cube.gen")
inputDensity = [0.5 for i in range(inMesh.numNodes)]

# open exodus file for output and configure
outMesh = exodus.ExodusDB()
outMesh.read("cube.gen")
outMesh.elemVarNames = outputElemDataNames;
outMesh.nodeVarNames = outputNodeDataNames;
numElemBlocks = 1
outMesh.numElemVars = len(outputElemDataNames)
outMesh.numNodeVars = len(outputNodeDataNames)
outMesh.elemVars = [[[[] for k in range(numElemBlocks)] for j in outputElemDataNames]]
outMesh.nodeVars = [[[] for i in outputNodeDataNames]]
outMesh.varTimes = [0.0]

# import current design into Analyze instance
inputDataType = "SCALAR_FIELD"
analyze.importData("Topology", inputDataType, inputDensity)

# compute gradient
analyze.compute("Compute Objective")
analyze.compute("Compute Constraint")

# export output data from Analyze instance
iTime = 0
iBlock = 0
for iTerm in range(numElemTerms):
  outMesh.elemVars[iTime][iTerm][iBlock] = analyze.exportData(analyzeElemDataNames[iTerm], outputElemDataType)
for iTerm in range(numNodeTerms):
  outMesh.nodeVars[iTime][iTerm] = analyze.exportData(analyzeNodeDataNames[iTerm], outputNodeDataType)

dfdp = outMesh.nodeVars[iTime][3]
dgdp = outMesh.nodeVars[iTime][4]
dfdg = [dfdp[i]/dgdp[i] for i in range(outMesh.numNodes)]

outMesh.numNodeVars += 1
outMesh.nodeVarNames.append("dfdg")
outMesh.nodeVars[iTime].append(dfdg)


# finalize mpi and kokkos.  Not essential, but you'll get warnings otherwise.
analyze.finalize()

# write output
outMesh.write("output.exo")
