# plainDB
# Its overly plain and simple.

Sphinx docs are in `doc` folder


###### Usage 
```
python plaindb/app.py -h
usage: app.py [-h] [-n NAME] [-a ADDRESS] [-p PHONE] -f FTYPE [-v VALUE] [-o] (-i | -q | -u | -b)

This is a complex db of the world that's so simple.

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Name of the Person.
  -a ADDRESS, --address ADDRESS
                        Address of the Person.
  -p PHONE, --phone PHONE
                        Phone Number of the Person.
  -f FTYPE, --file FTYPE
                        Core Database File Type. json/csv. Default is csv.
  -v VALUE, --value VALUE
                        New Value to be passed with -e/--edit option.
  -o, --out             Display the result in a web page. Used with -q option.
  -i, --insert          Insert Records to the DB.
  -q, --query           Query Records of the Person.
  -u, --update          Update the Record of the Person.
  -b, --blow            With power comes responsibility. This blows your database.

```

###### Run Tests #
```
$ pytest tests/ -v

platform win32 -- Python 3.8.1, pytest-5.4.1, py-1.8.1, pluggy-0.13.1 -- c:\users\smrut\appdata\local\programs\python\python38-32\python.exe
cachedir: .pytest_cache
rootdir: D:\Quinticon_Projects\Python\AnimalLogic\plaindb, inifile: pytest.ini
collected 28 items

tests/test_custom_logger.py::test_Logging_Function PASSED                                                                                                                                                   [  3%]
tests/test_database.py::test_db_creation_csv PASSED                                                                                                                                                         [  7%]
tests/test_database.py::test_db_creation_json PASSED                                                                                                                                                        [ 10%]
tests/test_database.py::test_db_insert_record_csv_db[Smruti-La La Land-480253550-200] PASSED                                                                                                                [ 14%]
tests/test_database.py::test_db_insert_record_csv_db[Jitu-Zootopia-480253551-200] PASSED                                                                                                                    [ 17%]
tests/test_database.py::test_db_insert_record_csv_db[Harry-Hogwarts-480253552-200] PASSED                                                                                                                   [ 21%]
tests/test_database.py::test_db_insert_record_csv_db[Hermione-Gryffindor-480253553-200] PASSED                                                                                                              [ 25%]
tests/test_database.py::test_db_insert_record_csv_db[Hermione-Gryffindor-480253554-200] PASSED                                                                                                              [ 28%]
tests/test_database.py::test_db_insert_record_json_db[Smruti-La La Land-480253550-200] PASSED                                                                                                               [ 32%]
tests/test_database.py::test_db_insert_record_json_db[Jitu-Zootopia-480253551-200] PASSED                                                                                                                   [ 35%]
tests/test_database.py::test_db_insert_record_json_db[Harry-Hogwarts-480253552-200] PASSED                                                                                                                  [ 39%]
tests/test_database.py::test_db_insert_record_json_db[Hermione-Gryffindor-480253553-200] PASSED                                                                                                             [ 42%]
tests/test_database.py::test_db_insert_record_json_db[Hermione-Gryffindor-480253554-200] PASSED                                                                                                             [ 46%]
tests/test_database.py::test_db_select_record_csv_db[Smruti-200] PASSED                                                                                                                                     [ 50%]
tests/test_database.py::test_db_select_record_csv_db[Harry-200] PASSED                                                                                                                                      [ 53%]
tests/test_database.py::test_db_select_record_csv_db[Hermione-200] PASSED                                                                                                                                   [ 57%]
tests/test_database.py::test_db_select_record_json_db[Smruti-200] PASSED                                                                                                                                    [ 60%]
tests/test_database.py::test_db_select_record_json_db[Harry-200] PASSED                                                                                                                                     [ 64%]
tests/test_database.py::test_db_select_record_json_db[Hermione-200] PASSED                                                                                                                                  [ 67%]
tests/test_database.py::test_db_select_record_csv_db_mixed_predicate[Smruti-Hogwarts-200] PASSED                                                                                                            [ 71%]
tests/test_database.py::test_db_select_record_csv_db_mixed_predicate[Harry-Zootopia-200] PASSED                                                                                                             [ 75%]
tests/test_database.py::test_db_select_record_csv_db_mixed_predicate[Hermione-Gryffindor-200] PASSED                                                                                                        [ 78%]
tests/test_database.py::test_db_select_record_json_db_mixed_predicate[Smruti-Hogwarts-200] PASSED                                                                                                           [ 82%]
tests/test_database.py::test_db_select_record_json_db_mixed_predicate[Harry-Zootopia-200] PASSED                                                                                                            [ 85%]
tests/test_database.py::test_db_select_record_json_db_mixed_predicate[Hermione-Gryffindor-200] PASSED                                                                                                       [ 89%]
tests/test_database.py::test_db_update_record_csv_db[Smruti-Mohanty-200] PASSED                                                                                                                             [ 92%]
tests/test_database.py::test_db_update_record_csv_db[Harry-Potter-200] PASSED                                                                                                                               [ 96%]
tests/test_database.py::test_db_update_record_csv_db[Hermione-Granger-200] PASSED                                                                                                                           [100%]

=============================================================================================== 28 passed in 0.36s ===============================================================================================

```

###### Run TOX #

```
$tox

  clean: commands succeeded
  py38: commands succeeded
  docs: commands succeeded
  lint: commands succeeded
  coverage: commands succeeded
  report: commands succeeded
  congratulations :)

```