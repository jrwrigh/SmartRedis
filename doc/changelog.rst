Changelog
=========

Development branch
------------------

To be released at some future point in time

Description

- Add pip-install target to Makefile to automate this process going forward

Detailed Notes

- New pip-install target in Makefile will be a dependency of the lib target going forward so that users don't have to manually pip install SmartRedis in the future (PR330_)

.. _PR330: https://github.com/CrayLabs/SmartRedis/pull/330

0.4.0
-----

Released on April 12, 2023

Description

This release provides a variety of features to improve usability and debugging
of the SmartRedis library, notably including Unix domain socket support, logging,
the ability to print a textual representation of a string or dataset, dataset
inspection, documentation updates, fixes to the multi-GPU support, and much more:

- Prepare 0.4.0 release
- Disable codecov CI tests
- Improved error message in to_string methods in C interface
- Streamlined PyBind interface layer
- Updated Python API documentation
- Streamlined C interface layer
- Improved performance of get, put, and copy dataset methods
- Fix a bug which prevented multi-GPU model set in some cases
- Streamline pipelined execution of tasks for backend database
- Enhance code coverage to include all 4 languages supported by SmartRedis
- Fix a bug which resulted in wrong key prefixing when retrieving aggregation lists in ensembles
- Correct assorted API documentation errors
- Improve documentation of exception handling in Redis server classes
- Improve error handling for setting of scripts and models
- Add support to inspect the dimensions of a tensor via get_tensor_dims()
- Split dataset prefixing control from use_tensor_ensemble_prefix() to use_dataset_ensemble_prefix()
- Update to the latest version of redis-plus-plus
- Update to the latest version of PyBind
- Change documentation theme to sphinx_book_theme and fix doc strings
- Add print capability for Client and DataSet
- Add support for inspection of tensors and metadata inside datasets
- Add support for user-directed logging for Python clients, using Client, Dataset, or LogContext logging methods
- Add support for user-directed logging for C and Fortran clients without a Client or Dataset context
- Additional error reporting for connections to and commands run against Redis databases
- Improved error reporting capabilities for Fortran clients
- Python error messages from SmartRedis contain more information
- Added logging functionality to the SmartRedis library
- A bug related to thread pool initialization was fixed.
- This version adds new functionality in the form of support for Unix Domain Sockets.
- Fortran client can now be optionally built with the rest of the library
- Initial support for dataset conversions, specifically Xarray.

Detailed Notes

- Update docs and version numbers in preparation for version 0.4.0. Clean up duplicate marking of numpy dependency (PR321_)
- Remove codecov thresholds to avoid commits being marked as 'failed' due to coverage variance (PR317_)
- Corrected the error message in to_string methods in C interface to not overwrite the returned error message and to name the function (PR320_)
- Streamlined PyBind interface layer to reduce repetitive boilerplate code (PR315_)
- Updated Python API summary table to include new methods (PR313_)
- Streamlined C interface layer to reduce repetitive boilerplate code (PR312_)
- Leveraged Redis pipelining to improve performance of get, put, and copy dataset methods (PR311_)
- Redis::set_model_multigpu() will now upload the correct model to all GPUs (PR310_)
- RedisCluster::_run_pipeline() will no longer unconditionally apply a retry wait before returning (PR309_)
- Expand code coverage to all four languages and make the CI/CD more efficent (PR308_)
- An internal flag was set incorrectly, it resulted in wrong key prefixing when accessing (retrieving or querying) lists created in ensembles (PR306_)
- Corrected a variety of Doxygen errors and omissions in the API documentation (PR305_)
- Added throw documentation for exception handling in redis.h, redisserver.h, rediscluster.h (PR301_)
- Added error handling for a rare edge condition when setting scripts and models (PR300_)
- Added support to inspect the dimensions of a tensor via new get_tensor_dims() method (PR299_)
- The use_tensor_ensemble_prefix() API method no longer controls whether datasets are prefixed. A new API method, use_dataset_ensemble_prefix() now manages this. (PR298_)
- Updated from redis-plus-plus v1.3.2 to v1.3.5 (PR296_)
- Updated from PyBind v2.6.2 to v2.10.3 (PR295_)
- Change documentation theme to sphinx_book_theme to match SmartSim documentation theme and fix Python API doc string errors (PR294_)
- Added print capability for Client and DataSet to give details diagnostic information for debugging (PR293_)
- Added support for retrieval of names and types of tensors and metadata inside datasets (PR291_)
- Added support for user-directed logging for Python clients via {Client, Dataset, LogContext}.{log_data, log_warning, log_error} methods (PR289_)
- Added support for user-directed logging without a Client or Dataset context to C and Fortran clients via _string() methods (PR288_)
- Added logging to capture transient errors that arise in the _run() and _connect() methods of the Redis and RedisCluster classes (PR287_)
- Tweak direct testing of Redis and RedisCluster classes (PR286_)
- Resolve a disparity in the construction of Python client and database classes (PR285_)
- Fortran clients can now access error text and source location (PR284_)
- Add exception location information from CPP code to Python exceptions (PR283_)
- Added client activity and manual logging for developer use (PR281_)
- Fix thread pool error (PR280_)
- Update library linking instructions and update Fortran tester build process (PR277_)
- Added `add_metadata_for_xarray` and `transform_to_xarray` methods in `DatasetConverter` class for initial support with Xarray (PR262_)
- Change Dockerfile to use Ubuntu 20.04 LTS image (PR276_)
- Implemented support for Unix Domain Sockets, including refactorization of server address code, test cases, and check-in tests. (PR252_)
- A new make target `make lib-with-fortran` now compiles the Fortran client and dataset into its own library which applications can link against (PR245_)

.. _PR321: https://github.com/CrayLabs/SmartRedis/pull/321
.. _PR317: https://github.com/CrayLabs/SmartRedis/pull/317
.. _PR320: https://github.com/CrayLabs/SmartRedis/pull/320
.. _PR315: https://github.com/CrayLabs/SmartRedis/pull/315
.. _PR313: https://github.com/CrayLabs/SmartRedis/pull/313
.. _PR312: https://github.com/CrayLabs/SmartRedis/pull/312
.. _PR311: https://github.com/CrayLabs/SmartRedis/pull/311
.. _PR310: https://github.com/CrayLabs/SmartRedis/pull/310
.. _PR309: https://github.com/CrayLabs/SmartRedis/pull/309
.. _PR308: https://github.com/CrayLabs/SmartRedis/pull/308
.. _PR306: https://github.com/CrayLabs/SmartRedis/pull/306
.. _PR305: https://github.com/CrayLabs/SmartRedis/pull/305
.. _PR301: https://github.com/CrayLabs/SmartRedis/pull/301
.. _PR300: https://github.com/CrayLabs/SmartRedis/pull/300
.. _PR299: https://github.com/CrayLabs/SmartRedis/pull/299
.. _PR298: https://github.com/CrayLabs/SmartRedis/pull/298
.. _PR296: https://github.com/CrayLabs/SmartRedis/pull/296
.. _PR295: https://github.com/CrayLabs/SmartRedis/pull/295
.. _PR294: https://github.com/CrayLabs/SmartRedis/pull/294
.. _PR293: https://github.com/CrayLabs/SmartRedis/pull/293
.. _PR291: https://github.com/CrayLabs/SmartRedis/pull/291
.. _PR289: https://github.com/CrayLabs/SmartRedis/pull/289
.. _PR288: https://github.com/CrayLabs/SmartRedis/pull/288
.. _PR287: https://github.com/CrayLabs/SmartRedis/pull/287
.. _PR286: https://github.com/CrayLabs/SmartRedis/pull/286
.. _PR285: https://github.com/CrayLabs/SmartRedis/pull/285
.. _PR284: https://github.com/CrayLabs/SmartRedis/pull/284
.. _PR283: https://github.com/CrayLabs/SmartRedis/pull/283
.. _PR281: https://github.com/CrayLabs/SmartRedis/pull/281
.. _PR280: https://github.com/CrayLabs/SmartRedis/pull/280
.. _PR277: https://github.com/CrayLabs/SmartRedis/pull/277
.. _PR262: https://github.com/CrayLabs/SmartRedis/pull/262
.. _PR276: https://github.com/CrayLabs/SmartRedis/pull/276
.. _PR252: https://github.com/CrayLabs/SmartRedis/pull/252
.. _PR245: https://github.com/CrayLabs/SmartRedis/pull/245

0.3.1
-----

Released on June 24, 2022

Description

Version 0.3.1 adds new functionality in the form of DataSet aggregation lists for pipelined retrieval of data, convenient support for multiple GPUs, and the ability to delete scripts and models from the backend database. It also introduces multithreaded execution for certain tasks that span multiple shards of a clustered database, and it incorporates a variety of internal improvements that will enhance the library going forward.

Detailed Notes

- Implemented DataSet aggregation lists in all client languages, for pipelined retrieval of data across clustered and non-clustered backend databases. (PR258_) (PR257_) (PR256_) (PR248_) New commands are:

  - append_to_list()
  - delete_list()
  - copy_list()
  - rename_list()
  - get_list_length()
  - poll_list_length()
  - poll_list_length_gte()
  - poll_list_length_lte()
  - get_datasets_from_list()
  - get_dataset_list_range()
  - use_list_ensemble_prefix()

- Implemented multithreaded execution for parallel dataset list retrieval on clustered databases. The number of threads devoted for this purpose is controlled by the new environment variable SR_THERAD_COUNT. The value defaults to 4, but may be any positive integer or special value zero, which will cause the SmartRedis runtime to allocate one thread for each available hardware context. (PR251_) (PR246_)

- Augmented support for GPUs by implementing multi-GPU convenience functions for all client languages. (PR254_) (PR250_) (PR244_) New commands are:

  - set_model_from_file_multigpu()
  - set_model_multigpu()
  - set_script_from_file_multigpu()
  - set_script_multigpu()
  - run_model_multigpu()
  - run_script_multigpu()
  - delete_model_multigpu()
  - delete_script_multigpu()

- Added API calls for all clients to delete models and scripts from the backend database. (PR240_) New commands are:

  - delete_script()
  - delete_model()

- Updated the use of backend RedisAI API calls to discontinue use of deprecated methods for model selection (AI.MODELSET) and execution (AI.MODELRUN) in favor of current methods AI.MODELSTORE and AI.MODELEXECUTE, respectively. (PR234_)

- SmartRedis will no longer call the C runtime method srand() to ensure that it does not interfere with random number generation in client code. It now uses a separate instance of the C++ random number generator. (PR233_)

- Updated the way that the Fortran enum_kind type defined in the fortran_c_interop module is defined in order to better comply with Fortran standard and not interfere with GCC 6.3.0. (PR231_)

- Corrected the spelling of the word "command" in a few error message strings. (PR221_)

- SmartRedis now requires a CMake version 3.13 or later in order to utilize the add_link_options CMake command. (PR217_)

- Updated and improved the documentation of the SmartRedis library. In particular, a new SmartRedis Integration Guide provides an introduction to using the SmartRedis library and integrating it with existing software. (PR261_) (PR260_) (PR259_) (SSPR214_)

- Added clustered Redis testing to automated GitHub check-in testing. (PR239_)

- Updated the SmartRedis internal API for building commands for the backend database. (PR223_) This change should not be visible to clients.

- The SmartRedis example code is now validated through the automated GitHub checkin process. This will help ensure that the examples do not fall out of date. (PR220_)

- Added missing copyright statements to CMakeLists.txt and the SmartRedis examples. (PR219_)

- Updated the C++ test coverage to ensure that all test files are properly executed when running "make test". (PR218_)

- Fixed an internal naming conflict between a local variable and a class member variable in the DataSet class. (PR215_)  This should not be visible to clients.

- Updated the internal documentation of methods in SmartRedis C++ classes with the override keyword to improve compliance with the latest C++ standards. (PR214_) This change should not be visible to clients.

- Renamed variables internally to more cleanly differentiate between names that are given to clients for tensors, models, scripts, datasets, etc., and the keys that are used when storing them in the backend database. (PR213_) This change should not be visible to clients.

.. _SSPR214: https://github.com/CrayLabs/SmartSim/pull/214
.. _PR261: https://github.com/CrayLabs/SmartRedis/pull/261
.. _PR260: https://github.com/CrayLabs/SmartRedis/pull/260
.. _PR259: https://github.com/CrayLabs/SmartRedis/pull/259
.. _PR258: https://github.com/CrayLabs/SmartRedis/pull/258
.. _PR257: https://github.com/CrayLabs/SmartRedis/pull/257
.. _PR256: https://github.com/CrayLabs/SmartRedis/pull/256
.. _PR254: https://github.com/CrayLabs/SmartRedis/pull/254
.. _PR251: https://github.com/CrayLabs/SmartRedis/pull/251
.. _PR250: https://github.com/CrayLabs/SmartRedis/pull/250
.. _PR248: https://github.com/CrayLabs/SmartRedis/pull/248
.. _PR246: https://github.com/CrayLabs/SmartRedis/pull/246
.. _PR244: https://github.com/CrayLabs/SmartRedis/pull/244
.. _PR240: https://github.com/CrayLabs/SmartRedis/pull/240
.. _PR239: https://github.com/CrayLabs/SmartRedis/pull/239
.. _PR234: https://github.com/CrayLabs/SmartRedis/pull/234
.. _PR233: https://github.com/CrayLabs/SmartRedis/pull/233
.. _PR231: https://github.com/CrayLabs/SmartRedis/pull/231
.. _PR223: https://github.com/CrayLabs/SmartRedis/pull/223
.. _PR221: https://github.com/CrayLabs/SmartRedis/pull/221
.. _PR220: https://github.com/CrayLabs/SmartRedis/pull/220
.. _PR219: https://github.com/CrayLabs/SmartRedis/pull/219
.. _PR218: https://github.com/CrayLabs/SmartRedis/pull/218
.. _PR217: https://github.com/CrayLabs/SmartRedis/pull/217
.. _PR215: https://github.com/CrayLabs/SmartRedis/pull/215
.. _PR214: https://github.com/CrayLabs/SmartRedis/pull/214
.. _PR213: https://github.com/CrayLabs/SmartRedis/pull/213

0.3.0
-----

Released on Febuary 11, 2022

Description

- Improve error handling across all SmartRedis clients (PR159_) (PR191_) (PR199_) (PR205_) (PR206_)

  - Includes changes to C and Fortran function prototypes that are not backwards compatible
  - Includes changes to error class names and enum type names that are not backwards compatible

- Add ``poll_dataset`` functionality to all SmartRedis clients (PR184_)

  - Due to other breaking changes made in this release, applications using methods other than ``poll_dataset`` to check for the existence of a dataset should now use ``poll_dataset``

- Add environment variables to control client connection and command timeout behavior (PR194_)
- Add AI.INFO command to retrieve statistics on scripts and models via Python and C++ clients (PR197_)
- Create a Dockerfile for SmartRedis (PR180_)
- Update ``redis-plus-plus`` version to 1.3.2 (PR162_)
- Internal client performance and API improvements (PR138_) (PR141_) (PR163_) (PR203_)
- Expose Redis ``FLUSHDB``, ``CONFIG GET``, ``CONFIG SET``, and ``SAVE`` commands to the Python client (PR139_) (PR160_)
- Extend inverse CRC16 prefixing to all hash slots (PR161_)
- Improve backend dataset representation to enable performance optimization (PR195_)
- Simplify SmartRedis build proccess (PR189_)
- Fix zero-length array transfer in Fortran ``convert_char_array_to_c`` (PR170_)
- Add continuous integration for all SmartRedis tests (PR165_) (PR173_) (PR177_)
- Update SmartRedis docstrings (PR200_) (PR207_)
- Update SmartRedis documentation and examples (PR202_) (PR208_) (PR210_)

.. _PR138: https://github.com/CrayLabs/SmartRedis/pull/138
.. _PR139: https://github.com/CrayLabs/SmartRedis/pull/139
.. _PR141: https://github.com/CrayLabs/SmartRedis/pull/141
.. _PR159: https://github.com/CrayLabs/SmartRedis/pull/159
.. _PR160: https://github.com/CrayLabs/SmartRedis/pull/160
.. _PR161: https://github.com/CrayLabs/SmartRedis/pull/161
.. _PR162: https://github.com/CrayLabs/SmartRedis/pull/162
.. _PR163: https://github.com/CrayLabs/SmartRedis/pull/163
.. _PR165: https://github.com/CrayLabs/SmartRedis/pull/165
.. _PR170: https://github.com/CrayLabs/SmartRedis/pull/170
.. _PR173: https://github.com/CrayLabs/SmartRedis/pull/173
.. _PR177: https://github.com/CrayLabs/SmartRedis/pull/177
.. _PR180: https://github.com/CrayLabs/SmartRedis/pull/180
.. _PR183: https://github.com/CrayLabs/SmartRedis/pull/183
.. _PR184: https://github.com/CrayLabs/SmartRedis/pull/184
.. _PR189: https://github.com/CrayLabs/SmartRedis/pull/189
.. _PR191: https://github.com/CrayLabs/SmartRedis/pull/191
.. _PR194: https://github.com/CrayLabs/SmartRedis/pull/194
.. _PR195: https://github.com/CrayLabs/SmartRedis/pull/195
.. _PR197: https://github.com/CrayLabs/SmartRedis/pull/197
.. _PR198: https://github.com/CrayLabs/SmartRedis/pull/198
.. _PR199: https://github.com/CrayLabs/SmartRedis/pull/199
.. _PR200: https://github.com/CrayLabs/SmartRedis/pull/200
.. _PR202: https://github.com/CrayLabs/SmartRedis/pull/202
.. _PR203: https://github.com/CrayLabs/SmartRedis/pull/203
.. _PR205: https://github.com/CrayLabs/SmartRedis/pull/205
.. _PR206: https://github.com/CrayLabs/SmartRedis/pull/206
.. _PR207: https://github.com/CrayLabs/SmartRedis/pull/207
.. _PR208: https://github.com/CrayLabs/SmartRedis/pull/208
.. _PR210: https://github.com/CrayLabs/SmartRedis/pull/210

0.2.0
-----

Released on August, 5, 2021

Description

- Improved tensor memory management in the Python client (PR70_)
- Improved metadata serialization and removed protobuf dependency (PR61_)
- Added unit testing infrastructure for the C++ client (PR96_)
- Improve command execution fault handling (PR65_) (PR97_) (PR105_)
- Bug fixes (PR52_) (PR72_) (PR76_) (PR84_)
- Added copy, rename, and delete tensor and DataSet commands in the Python client (PR66_)
- Upgrade to RedisAI 1.2.3 (PR101_)
- Fortran and C interface improvements (PR93_) (PR94_) (PR95_) (PR99_)
- Add Redis INFO command execution to the Python client (PR83_)
- Add Redis CLUSTER INFO command execution to the Python client (PR105_)

.. _PR52: https://github.com/CrayLabs/SmartRedis/pull/52
.. _PR61: https://github.com/CrayLabs/SmartRedis/pull/61
.. _PR65: https://github.com/CrayLabs/SmartRedis/pull/65
.. _PR66: https://github.com/CrayLabs/SmartRedis/pull/66
.. _PR70: https://github.com/CrayLabs/SmartRedis/pull/70
.. _PR72: https://github.com/CrayLabs/SmartRedis/pull/72
.. _PR76: https://github.com/CrayLabs/SmartRedis/pull/76
.. _PR83: https://github.com/CrayLabs/SmartRedis/pull/83
.. _PR84: https://github.com/CrayLabs/SmartRedis/pull/84
.. _PR93: https://github.com/CrayLabs/SmartRedis/pull/93
.. _PR94: https://github.com/CrayLabs/SmartRedis/pull/94
.. _PR95: https://github.com/CrayLabs/SmartRedis/pull/95
.. _PR96: https://github.com/CrayLabs/SmartRedis/pull/96
.. _PR97: https://github.com/CrayLabs/SmartRedis/pull/97
.. _PR99: https://github.com/CrayLabs/SmartRedis/pull/99
.. _PR101: https://github.com/CrayLabs/SmartRedis/pull/101
.. _PR105: https://github.com/CrayLabs/SmartRedis/pull/105

0.1.1
-----

Released on May 5, 2021

Description

- Compiled client library build and install update to remove environment variables (PR47_)
-  Pip install for Python client (PR45_)

.. _PR47: https://github.com/CrayLabs/SmartRedis/pull/47
.. _PR45: https://github.com/CrayLabs/SmartRedis/pull/45

0.1.0
-----

Released on April 1, 2021

Description

- Initial 0.1.0 release of SmartRedis
