get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)

Plato_add_test_files("alexaApp.xml;amgx.json;bolted_bracket_assoc.txt;bolted_bracket.gen;bolted_bracket.jou;bolted_bracket.xml;opt.py;platoApp.xml;platoMain.xml")

file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/bolted_bracket.osh DESTINATION ${CMAKE_CURRENT_BINARY_DIR})


set( COMMAND1 "python opt.py" )
set( COMMANDS "${COMMAND1}" )

add_test(
  NAME ${testDirName}
  COMMAND ${CMAKE_COMMAND}
  -DCOMMANDS=${COMMANDS}
  -P ${CMAKE_SOURCE_DIR}/cmake/run.cmake
)
