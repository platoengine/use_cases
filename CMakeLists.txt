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

if(SEACAS)
  Plato_find_exe(SEACAS_EPU     epu      ${SEACAS_PATH}/bin)
  Plato_find_exe(SEACAS_EXODIFF exodiff  ${SEACAS_PATH}/bin)
  Plato_find_exe(SEACAS_DECOMP  decomp   ${SEACAS_PATH}/bin)
endif()

add_subdirectory(use_cases)
