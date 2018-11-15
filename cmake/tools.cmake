###############################################################################
## Plato_find_exe( 
##    VAR_NAME     == Return variable containing filepath to executable.
##    EXE_NAME     == Filename of executable.
##   [SEARCH_PATH] == Directories below this path are searched.
## )
###############################################################################
function( Plato_find_exe VAR_NAME EXE_NAME SEARCH_PATH )

  message(STATUS " ")
  message(STATUS "Finding ${EXE_NAME} executable")

  message("-- searching in " ${SEARCH_PATH})
  find_program( ${VAR_NAME}_SEARCH_RESULT ${EXE_NAME}
                HINTS ${SEARCH_PATH}
                NO_DEFAULT_PATH )

  if( ${VAR_NAME}_SEARCH_RESULT MATCHES "NOTFOUND" )
    message(FATAL_ERROR "!! ${EXE_NAME} executable not found !!")
  endif( ${VAR_NAME}_SEARCH_RESULT MATCHES "NOTFOUND" )

  set( ${VAR_NAME} ${${VAR_NAME}_SEARCH_RESULT} PARENT_SCOPE )
  message(STATUS "${EXE_NAME} executable found")
  message(STATUS "Using:  ${${VAR_NAME}_SEARCH_RESULT}")
  message(STATUS " ")

endfunction(Plato_find_exe)
###############################################################################


###############################################################################
function( Plato_no_src_build )

if("${CMAKE_SOURCE_DIR}" STREQUAL "${CMAKE_BINARY_DIR}")
  message(STATUS " ")
  message(STATUS "In-source builds are not allowed.")
  message(STATUS "Please remove CMakeCache.txt and the CMakeFiles/ directory and then build out-of-source.")
  message(STATUS "(That is, create a build directory below the source directory and build from there.)" )
  message(STATUS " ")
  message(FATAL_ERROR " ")
endif()

endfunction( Plato_no_src_build )
###############################################################################


###############################################################################
## Plato_add_test_files( 
##    FILE_LIST    == Return variable containing filepath to executable.
## )
###############################################################################

function( Plato_add_test_files FILE_LIST )
  
  foreach( testFile ${FILE_LIST} )
  
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${testFile} 
                   ${CMAKE_CURRENT_BINARY_DIR}/${testFile} COPYONLY)
    
  endforeach(testFile)
    
endfunction(Plato_add_test_files)
