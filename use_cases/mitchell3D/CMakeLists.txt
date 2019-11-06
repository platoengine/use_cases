get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)

Plato_add_test_files("analyzeApp.xml;amgx.json;CMakeLists.txt;mitchell_tet_assoc.txt;mitchell_tet.gen;mitchell_tet.jou;analyzeInput.xml;opt.py;output.exo;;platoApp.xml;platoMain.xml")

file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/mitchell_tet.osh DESTINATION ${CMAKE_CURRENT_BINARY_DIR})

set( COMMAND1 "python opt.py" )
set( COMMANDS "${COMMAND1}" )

add_test(
  NAME ${testDirName}
  COMMAND ${CMAKE_COMMAND}
  -DCOMMANDS=${COMMANDS}
  -P ${CMAKE_SOURCE_DIR}/cmake/run.cmake
)
