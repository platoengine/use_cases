get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)
Plato_add_test_files("4bolt.cogent;albanyApp1.xml;albanyApp2.xml;background.gen;background.jou;CMakeLists.txt;interface.xml;mpirun.source;nodal_oc1.xml;nodal_oc2.xml;platoApp.xml;platomain.xml")

set( COMMAND1 "decomp -p 4 background.gen" )
set( COMMAND2 "decomp -p 8 background.gen" )
set( COMMAND3 "source mpirun.source" )
set( COMMANDS "${COMMAND1};${COMMAND2};${COMMAND3}" )

add_test(
  NAME ${testDirName}
  COMMAND ${CMAKE_COMMAND}
  -DCOMMANDS=${COMMANDS}
  -P ${CMAKE_SOURCE_DIR}/cmake/run.cmake
)
