get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)
Plato_add_test_files("alexaApp1.xml;alexaApp2.xml;alexaApp3.xml;amgx.json;bolted_bracket_assoc1.txt;bolted_bracket_assoc2.txt;bolted_bracket_assoc3.txt;bolted_bracket.gen;bolted_bracket.gen.4.0;bolted_bracket.gen.4.1;bolted_bracket.gen.4.2;bolted_bracket.gen.4.3;CMakeLists.txt;interface.xml;mpirun.source;platoApp.xml;platoMain.xml;soap1.xml;soap2.xml;soap3.xml")

file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/bolted_bracket.osh DESTINATION ${CMAKE_CURRENT_BINARY_DIR})

set( COMMAND1 "source mpirun.source" )
set( COMMANDS "${COMMAND1}" )

add_test(
  NAME ${testDirName}
  COMMAND ${CMAKE_COMMAND}
  -DCOMMANDS=${COMMANDS}
  -P ${CMAKE_SOURCE_DIR}/cmake/run.cmake
)
