get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)
Plato_add_test_files("analyzeApp.xml;amgx.json;CMakeLists.txt;defines.xml;interface.xml;mitchell_tri_assoc.txt;mitchell_tri.gen;mitchell_tri.jou;analyzeInput.xml;mpirun.source;platoApp.xml;platoMain.xml")

file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/bolted_bracket.osh DESTINATION ${CMAKE_CURRENT_BINARY_DIR})

set( COMMAND1 "source mpirun.source" )
set( COMMANDS "${COMMAND1}" )

add_test(
  NAME ${testDirName}
  COMMAND ${CMAKE_COMMAND}
  -DCOMMANDS=${COMMANDS}
  -P ${CMAKE_SOURCE_DIR}/cmake/run.cmake
)
