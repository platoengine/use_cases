get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)

Plato_add_test_files("addDensity.py;analyzeApp.xml;amgx.json;CMakeLists.txt;cube.exo;density.exo;homog1.xml;homog2.xml;homog3.xml;homog4.xml;homog5.xml;homog6.xml;output.exo;strains.exo;strains.py")

set( COMMAND1 "python strains.py" )
set( COMMANDS "${COMMAND1}" )

add_test(
  NAME ${testDirName}
  COMMAND ${CMAKE_COMMAND}
  -DCOMMANDS=${COMMANDS}
  -P ${CMAKE_SOURCE_DIR}/cmake/run.cmake
)
