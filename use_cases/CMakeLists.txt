IF( PLATOMAIN )
ENDIF()

IF( ANALYZE )
ENDIF()

IF( ALBANY )
  add_subdirectory(4bolt_opt_cutout)
ENDIF()

IF( ANALYZE_MPMD AND PLATOMAIN )
  add_subdirectory(barlat_stress)
  add_subdirectory(uq_multiperf)
ENDIF()

IF( ANALYZE_PYTHON AND PLATO_PYTHON )
  add_subdirectory(bolted_bracket_py)
  add_subdirectory(displacements)
  add_subdirectory(gradient)
  add_subdirectory(mitchell3D)
  add_subdirectory(strains)
  add_subdirectory(stress_pnorm)
ENDIF()

IF( ALBANY_MPMD )
ENDIF()
