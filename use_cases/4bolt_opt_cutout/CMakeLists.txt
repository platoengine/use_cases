get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)
Plato_add_test_files("body.cogent;load0.cogent;mitchell_sf.xml;mitchell.xml;mount0.cogent;mount1.cogent;mount2.cogent;mount3.cogent")

set( COMMAND1 "${ALBANY_BINARY} mitchell_sf.xml" )
set( COMMANDS "${COMMAND1}" )

add_test(
  NAME ${testDirName}
  COMMAND ${CMAKE_COMMAND}
  -DCOMMANDS=${COMMANDS}
  -P ${CMAKE_SOURCE_DIR}/cmake/run.cmake
)
