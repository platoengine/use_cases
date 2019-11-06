get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)
Plato_add_test_files("analyzeApp.xml;analyzeInput.xml;amgx.json;bolted_bracket.exo;bolted_bracket.jou;interface.xml;platoApp.xml;platoMain.xml;mpirun.source")

set( COMMAND1 "source mpirun.source" )
set( COMMANDS "${COMMAND1}" )

add_test(
  NAME ${testDirName}
  COMMAND ${CMAKE_COMMAND}
  -DCOMMANDS=${COMMANDS}
  -P ${CMAKE_SOURCE_DIR}/cmake/run.cmake
)
