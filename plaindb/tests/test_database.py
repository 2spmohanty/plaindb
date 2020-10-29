__author__ = "Smruti Mohanty"

import pytest
from ..plaindb.core import customlogger, plainDB
import logging

logger = customlogger(logging.INFO, "plaindb-unit-test.log")


def test_db_creation_csv():
    logger.info("THREAD - test_db_creation_csv - Create Database with csv as db file ")
    pytest.csvdb = plainDB("plaindb_test.csv")
    assert pytest.csvdb is not None, "Plain DB CSV version creation failed."


def test_db_creation_json():
    logger.info("THREAD - test_db_creation_json - Create Database with json as db file ")
    pytest.jsondb = plainDB("plaindb_test.json")
    assert pytest.jsondb is not None, "Plain DB JSON version creation failed."


insert_test_data = [("Smruti", "La La Land", "480253550", 200),
                    ("Jitu", "Zootopia", "480253551", 200),
                    ("Harry", "Hogwarts", "480253552", 200),
                    ("Hermione", "Gryffindor", "480253553", 200),
                    ("Hermione", "Gryffindor", "480253554", 200), ]


@pytest.mark.dependency(depends=["test_db_creation_csv"])
@pytest.mark.parametrize("name,address,phone,expected_status,", insert_test_data)
def test_db_insert_record_csv_db(name, address, phone, expected_status):
    logger.info("THREAD - test_db_insert_record_csv_db - Insert record to a plaindb csv version ")

    status, response = pytest.csvdb.query(logger, "insert", name=name, address=address, phone=phone)
    assert status == expected_status, "Plain CSV DB insert query failed.."


@pytest.mark.dependency(depends=["test_db_creation_json"])
@pytest.mark.parametrize("name,address,phone,expected_status,", insert_test_data)
def test_db_insert_record_json_db(name, address, phone, expected_status):
    logger.info("THREAD - test_db_insert_record_json_db - Insert record to a plaindb json version ")

    status, response = pytest.jsondb.query(logger, "insert", name=name, address=address, phone=phone)
    assert status == expected_status, "Plain JSON DB insert query failed.."


select_data = [("Smruti", 200),
               ("Harry", 200),
               ("Hermione", 200)]


@pytest.mark.dependency(depends=["test_db_insert_record_csv_db"])
@pytest.mark.parametrize("name,expected_status,", select_data)
def test_db_select_record_csv_db(name, expected_status):
    logger.info("THREAD - test_db_select_record_csv_db - Select record from a plaindb csv version ")
    status, response = pytest.csvdb.query(logger, "select", name=name)
    assert status == expected_status, "Plain csv DB select query failed.."


@pytest.mark.dependency(depends=["test_db_insert_record_json_db"])
@pytest.mark.parametrize("name,expected_status,", select_data)
def test_db_select_record_json_db(name, expected_status):
    logger.info("THREAD - test_db_select_record_csv_db - Select record from a plaindb json version ")
    status, response = pytest.jsondb.query(logger, "select", name=name)
    assert status == expected_status, "Plain csv DB select query failed.."


select_mixed_predicate = [("Smruti", "Hogwarts", 200),
                          ("Harry", "Zootopia", 200),
                          ("Hermione", "Gryffindor", 200)]


@pytest.mark.dependency(depends=["test_db_insert_record_csv_db"])
@pytest.mark.parametrize("name,address,expected_status,", select_mixed_predicate)
def test_db_select_record_csv_db_mixed_predicate(name, address, expected_status):
    logger.info("THREAD - test_db_select_record_csv_db - Select record from a plaindb csv version ")
    status, response = pytest.csvdb.query(logger, "select", name=name, address=address)
    assert status == expected_status, "Plain csv DB mixed predicate select query failed.."


@pytest.mark.dependency(depends=["test_db_insert_record_json_db"])
@pytest.mark.parametrize("name,address,expected_status,", select_mixed_predicate)
def test_db_select_record_json_db_mixed_predicate(name, address, expected_status):
    logger.info("THREAD - test_db_select_record_csv_db - Select record from a plaindb json version ")
    status, response = pytest.jsondb.query(logger, "select", name=name, address=address)
    assert status == expected_status, "Plain csv DB mixed predicate select query failed.."


alter_data = [("Smruti", "Mohanty", 200),
              ("Harry", "Potter", 200),
              ("Hermione", "Granger", 200)]


@pytest.mark.dependency(depends=["test_db_insert_record_csv_db"])
@pytest.mark.parametrize("name,value,expected_status,", alter_data)
def test_db_update_record_csv_db(name, value, expected_status):
    logger.info("THREAD - test_db_update_record_csv_db - Update record in a plaindb csv version ")
    status, response = pytest.csvdb.query(logger, "update", name=name, value=value)
    assert status == expected_status, "Plain csv DB Alter query failed.."

"""
@pytest.mark.dependency(depends=["test_db_insert_record_json_db"])
@pytest.mark.parametrize("name,value,expected_status,", alter_data)
def test_db_alter_record_json_db(name, value, expected_status):
    logger.info("THREAD - test_db_select_record_csv_db - Alter record in a plaindb json version ")
    status, response = pytest.jsondb.query(logger, "edit", name=name, value=value)
    assert status == expected_status, "Plain csv DB Alter query failed.."
"""
