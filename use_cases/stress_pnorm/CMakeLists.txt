get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)

Plato_add_test_files("analyzeApp.xml;amgx.json;CMakeLists.txt;cube.exo;output.exo;pnorm_grad.py;analyzeInput.xml")

set( COMMAND1 "python pnorm_grad.py" )
set( COMMANDS "${COMMAND1}" )

add_test(
  NAME ${testDirName}
  COMMAND ${CMAKE_COMMAND}
  -DCOMMANDS=${COMMANDS}
  -P ${CMAKE_SOURCE_DIR}/cmake/run.cmake
)
