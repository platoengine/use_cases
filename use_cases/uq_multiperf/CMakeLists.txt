get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)
Plato_add_test_files("analyzeApp.xml;amgx.json;CMakeLists.txt;defines.xml;interface.xml;mitchell_tri.exo;mitchell_tri.jou;analyzeInput.xml;mpirun.source;platoApp.xml;platoMain.xml")

set( COMMAND1 "source mpirun.source" )
set( COMMANDS "${COMMAND1}" )

add_test(
  NAME ${testDirName}
  COMMAND ${CMAKE_COMMAND}
  -DCOMMANDS=${COMMANDS}
  -P ${CMAKE_SOURCE_DIR}/cmake/run.cmake
)
