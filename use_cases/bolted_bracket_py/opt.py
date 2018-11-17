import nlopt
import exodus
import Plato
import PlatoServices
import ctypes
from numpy import *

# boilerplate that dynamically loads the mpi library required by Plato.Analyze
ctypes.CDLL("libmpi.so",mode=ctypes.RTLD_GLOBAL)

# create global Analyze instance
appFileName = "alexaApp.xml"
defaultInputFile = "bolted_bracket.xml"
analyze = Plato.Analyze(defaultInputFile, appFileName, "bolted bracket")
analyze.initialize();

# create global PlatoServices instance
services = PlatoServices.Services("platoMain.xml", "platoApp.xml", "services")
services.initialize();

# initialize control
targetFraction = 0.5
inputMeshName    = "bolted_bracket.gen"
inMesh = exodus.ExodusDB()
inMesh.read(inputMeshName)
numOptDofs = inMesh.numNodes
xinit = [targetFraction for i in range(numOptDofs)]

# compute reference volume
x = [1.0 for i in range(numOptDofs)]
analyze.importData("Topology", "SCALAR_FIELD", x)
analyze.compute("Compute Constraint Value")
refValue = analyze.exportData("Constraint Value", "SCALAR")


#define objective
def f(x, grad):

  services.importData("Field", "SCALAR_FIELD", x.tolist())
  services.compute("FilterControl")
  x_filtered = services.exportData("Filtered Field", "SCALAR_FIELD")
    
  # import current design into Analyze instance
  analyze.importData("Topology", "SCALAR_FIELD", x_filtered)

  if grad.size > 0:

    value = 0.0
    for i in range(grad.size):
      grad[i] = 0.0

    # compute cell solutions
    analyze.compute("Compute Objective")
  
    # export output data from Analyze instance
    cellGrad  = analyze.exportData("Objective Gradient", "SCALAR_FIELD")
    value = analyze.exportData("Objective Value", "SCALAR")
  
    services.importData("Field", "SCALAR_FIELD", cellGrad)
    services.compute("FilterGradient")
    filtered_grad = services.exportData("Filtered Field", "SCALAR_FIELD")
    for iVal in range(len(filtered_grad)):
        grad[iVal] = filtered_grad[iVal]
    
    print " objective value: ", value
    return value

  else:

    value = 0.0

    # compute cell solutions
    analyze.compute("Compute Objective Value")
  
    # export output data from Analyze instance
    value = analyze.exportData("Objective Value", "SCALAR")
  
    print " objective value: ", value
    return value




#define constraint
def g(x, grad):

  services.importData("Field", "SCALAR_FIELD", x.tolist())
  services.compute("FilterControl")
  x_filtered = services.exportData("Filtered Field", "SCALAR_FIELD")
    
  # import current design into Analyze instance
  analyze.importData("Topology", "SCALAR_FIELD", x_filtered)

  if grad.size > 0:

    analyze.compute("Compute Constraint")
    grad[:] = analyze.exportData("Constraint Gradient", "SCALAR_FIELD")
    value = analyze.exportData("Constraint Value", "SCALAR")

    val = value/refValue - targetFraction
    print " constraint value: ", val
    return val

  else:
  
    analyze.compute("Compute Constraint Value")
    value = analyze.exportData("Constraint Value", "SCALAR")
    
    val = value/refValue - targetFraction
    print " constraint value: ", val
    return val




# create nlopt instance
opt = nlopt.opt(nlopt.LD_MMA, numOptDofs)

opt.set_min_objective(f)
opt.add_inequality_constraint(g, 1e-6)
opt.set_lower_bounds(0.0)
opt.set_upper_bounds(1.0)
opt.set_xtol_rel(1e-6)
opt.set_maxeval(40)

xopt = opt.optimize(xinit)
minf = opt.last_optimum_value()

print "optimum at: ", minf
fauxgrad = array([])
print "eval f() at min point: ", f(xopt,fauxgrad)
print "eval g() at min point: ", g(xopt,fauxgrad)

solx = analyze.exportData("Solution X", "SCALAR_FIELD")
soly = analyze.exportData("Solution Y", "SCALAR_FIELD")
solz = analyze.exportData("Solution Z", "SCALAR_FIELD")

services.importData("Field", "SCALAR_FIELD", xopt.tolist())
services.compute("FilterControl")
x_filtered = services.exportData("Filtered Field", "SCALAR_FIELD")
    
# open exodus file for output and configure
outMesh = exodus.ExodusDB()
outMesh.read(inputMeshName)
numTimes = 1
outMesh.nodeVarNames = ["topology","solution_x","solution_y","solution_z"]
outMesh.numNodeVars = len(outMesh.nodeVarNames)
outMesh.nodeVars = [[x_filtered,solx,soly,solz]]
outMesh.varTimes = [1.0]

# write output
outputMeshName   = "output.exo"
outMesh.write(outputMeshName)


# finalize mpi and kokkos.  Not essential, but you'll get warnings otherwise.
analyze.finalize()

