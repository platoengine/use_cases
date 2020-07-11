get_filename_component(testDirName ${CMAKE_CURRENT_SOURCE_DIR} NAME)

set( testFiles "analyzeApp.xml;amgx.json")
set( testFiles "${testFiles};analyzeInput.xml")
set( testFiles "${testFiles};interface.xml;mpirun.source;platoApp.xml;platoMain.xml")

if( LOWRES )
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/brick_reduced_lowres.exo ${CMAKE_CURRENT_BINARY_DIR}/brick_reduced.exo COPYONLY)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/brick_reduced_lowres.exo.4.0 ${CMAKE_CURRENT_BINARY_DIR}/brick_reduced.exo.4.0 COPYONLY)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/brick_reduced_lowres.exo.4.1 ${CMAKE_CURRENT_BINARY_DIR}/brick_reduced.exo.4.1 COPYONLY)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/brick_reduced_lowres.exo.4.2 ${CMAKE_CURRENT_BINARY_DIR}/brick_reduced.exo.4.2 COPYONLY)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/brick_reduced_lowres.exo.4.3 ${CMAKE_CURRENT_BINARY_DIR}/brick_reduced.exo.4.3 COPYONLY)
else()
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/brick_reduced.exo ${CMAKE_CURRENT_BINARY_DIR}/brick_reduced.exo COPYONLY)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/brick_reduced.exo.4.0 ${CMAKE_CURRENT_BINARY_DIR}/brick_reduced.exo.4.0 COPYONLY)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/brick_reduced.exo.4.1 ${CMAKE_CURRENT_BINARY_DIR}/brick_reduced.exo.4.1 COPYONLY)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/brick_reduced.exo.4.2 ${CMAKE_CURRENT_BINARY_DIR}/brick_reduced.exo.4.2 COPYONLY)
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/brick_reduced.exo.4.3 ${CMAKE_CURRENT_BINARY_DIR}/brick_reduced.exo.4.3 COPYONLY)
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
