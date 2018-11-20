import exodus
import math

mesh = exodus.ExodusDB()
mesh.read("cube.gen")

mesh.numNodeVars = 1
mesh.nodeVarNames = ["Rho_node"];
mesh.nodeVars = [[[0.0 for i in range(mesh.numNodes)]]];
mesh.varTimes = [0.0];

radius = 0.40;
for nodeIndex in range(mesh.numNodes):
  X = mesh.getCoordData(nodeIndex,"index")
  val = math.sqrt(X[0]*X[0]+X[1]*X[1]+X[2]*X[2]) - radius;
  if val < 0.0:
    val = 0.0
  else:
    val = 1.0
  mesh.nodeVars[0][0][nodeIndex] = val

mesh.write("density.gen")
