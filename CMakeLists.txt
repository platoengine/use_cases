############ Project setup #######################################
CMAKE_MINIMUM_REQUIRED(VERSION 3.0.0)
##################################################################

include( ${CMAKE_SOURCE_DIR}/cmake/tools.cmake )
Plato_no_src_build()

include( ${CMAKE_SOURCE_DIR}/cmake/defaults.cmake )



##################################################################
project(UseCases) 
##################################################################

enable_testing()

if(SEACAS_PATH)
  Plato_find_exe(SEACAS_EPU     epu      ${SEACAS_PATH}/bin)
  Plato_find_exe(SEACAS_EXODIFF exodiff  ${SEACAS_PATH}/bin)
  Plato_find_exe(SEACAS_DECOMP  decomp   ${SEACAS_PATH}/bin)
else()
  set( SEACAS_EPU     epu     )
  set( SEACAS_EXODIFF exodiff )
  set( SEACAS_DECOMP  decomp  )
endif()

add_subdirectory(use_cases)
