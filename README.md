# use_cases
Collection of Plato Engine use cases

# set up
The use_cases repository uses CMake to allow multiple testing areas for, say,
different software builds.  To run the use_cases:

1.  Create a testing directory:

'mkdir -p builds/all
cd builds/all

2.  configure with CMake:

cmake -DPLATOMAIN=ON -DPLATOSTATICS=ON -DPLATO_PYTHON=ON -DANALYZE_PYTHON=ON -DANALYZE_MPMD=ON -DANALYZE=ON ../..

(see use_cases/cmake/defaults.cmake for the various options)

3.  run the tests

ctest


# additional configuration

To use a specific SEACAS installation, set SEACAS_PATH to point to it, i.e.,

cmake -DSEACAS_PATH=/path/to/seacas ...

If SEACAS_PATH is not provided, 'epu', 'exodiff', and 'decomp' must be in the current path at test time.
