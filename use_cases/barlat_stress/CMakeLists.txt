get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)
Plato_add_test_files("analyzeApp1.xml;analyzeApp2.xml;analyzeApp3.xml;amgx.json;bolted_bracket.exo;bolted_bracket.exo.4.0;bolted_bracket.exo.4.1;bolted_bracket.exo.4.2;bolted_bracket.exo.4.3;CMakeLists.txt;interface.xml;mpirun.source;platoApp.xml;platoMain.xml;analyzeInput1.xml;analyzeInput2.xml;analyzeInput3.xml")

set( COMMAND1 "source mpirun.source" )
set( COMMANDS "${COMMAND1}" )

add_test(
  NAME ${testDirName}
  COMMAND ${CMAKE_COMMAND}
  -DCOMMANDS=${COMMANDS}
  -P ${CMAKE_SOURCE_DIR}/cmake/run.cmake
)
