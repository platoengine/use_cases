get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)

set( testFiles "analyzeApp1.xml;analyzeApp2.xml;analyzeApp3.xml;amgx.json")
set( testFiles "${testFiles};analyzeInput1.xml;analyzeInput2.xml;analyzeInput3.xml")
set( testFiles "${testFiles};interface.xml;mpirun.source;platoApp.xml;platoMain.xml")

if( LOWRES )
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/bolted_bracket_lowres.exo ${CMAKE_CURRENT_BINARY_DIR}/bolted_bracket.exo COPYONLY)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/bolted_bracket_lowres.exo.4.0 ${CMAKE_CURRENT_BINARY_DIR}/bolted_bracket.exo.4.0 COPYONLY)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/bolted_bracket_lowres.exo.4.1 ${CMAKE_CURRENT_BINARY_DIR}/bolted_bracket.exo.4.1 COPYONLY)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/bolted_bracket_lowres.exo.4.2 ${CMAKE_CURRENT_BINARY_DIR}/bolted_bracket.exo.4.2 COPYONLY)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/bolted_bracket_lowres.exo.4.3 ${CMAKE_CURRENT_BINARY_DIR}/bolted_bracket.exo.4.3 COPYONLY)
else()
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/bolted_bracket.exo ${CMAKE_CURRENT_BINARY_DIR}/bolted_bracket.exo COPYONLY)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/bolted_bracket.exo.4.0 ${CMAKE_CURRENT_BINARY_DIR}/bolted_bracket.exo.4.0 COPYONLY)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/bolted_bracket.exo.4.1 ${CMAKE_CURRENT_BINARY_DIR}/bolted_bracket.exo.4.1 COPYONLY)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/bolted_bracket.exo.4.2 ${CMAKE_CURRENT_BINARY_DIR}/bolted_bracket.exo.4.2 COPYONLY)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/bolted_bracket.exo.4.3 ${CMAKE_CURRENT_BINARY_DIR}/bolted_bracket.exo.4.3 COPYONLY)
endif()


Plato_add_test_files( "${testFiles}" )

set( COMMAND1 "source mpirun.source" )
set( COMMANDS "${COMMAND1}" )

add_test(
  NAME ${testDirName}
  COMMAND ${CMAKE_COMMAND}
  -DCOMMANDS=${COMMANDS}
  -P ${CMAKE_SOURCE_DIR}/cmake/run.cmake
)
