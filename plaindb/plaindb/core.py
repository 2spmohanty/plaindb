__author__ = "Smruti Mohanty"

import logging
import csv
import json
import os
import re
import shutil


class SingletonMetaClass(type):
    def __init__(cls, name, bases, dict):
        super(SingletonMetaClass, cls).__init__(name, bases, dict)
        original_new = cls.__new__

        def my_new(cls, *args, **kwds):
            if cls.instance == None:
                cls.instance = original_new(cls, *args, **kwds)
            return cls.instance

        cls.instance = None
        cls.__new__ = staticmethod(my_new)


class plainDB():
    """
    plainDB is  classy blueprint for the plain db.
    Currently this supports 2 version.
    A csv (default) or a json based database file is created.

    """
    __metaclass__ = SingletonMetaClass  # Make Sure we have a Single DB instance.

    def __init__(self, filename: str):
        """
        The constructor for plainDB.

        :param filename: The Core DB file. (It is a csv/ JSON file)

        """

        self._filename = filename
        file_exists = os.path.isfile(self._filename)
        if "csv" in self._filename and not file_exists:
            fieldnames = ['name', 'address', 'phone']
            with open(self._filename, mode='w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
        if "json" in self._filename and not file_exists:
            with open(self._filename, mode='w', encoding='utf-8') as jsonfile:
                json.dump([], jsonfile, indent=4)

    def query(self, logger, querytype, **parameters):
        """
        query function initiate DML function on the table.

        :param self: The instance of the object.
        :param logger: A logger object.
        :param querytype: select/insert/update.
        :param parameters: name/phone/address

        :returns : A status code and a response.

        """

        if querytype == "insert":
            name = parameters.get("name", None)
            address = parameters.get("address", None)
            phone = parameters.get("phone", None)
            if not name:
                return 400, "plaindb :: Error: 0001 name cannot be null for Insert"
            logger.info(
                "THREAD - plaindb::Insert - Inserting Rows Name %s Address %s Phone %s" % (name, address, phone))
            if "csv" in self._filename:
                fieldnames = ['name', 'address', 'phone']
                with open(self._filename, mode='a') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow({'name': name, 'address': address, 'phone': phone})
            if "json" in self._filename:
                data = None
                with open(self._filename) as json_file_read:
                    data = json.load(json_file_read)
                data.append(parameters)
                with open(self._filename, 'w') as json_file_write:
                    json.dump(data, json_file_write, indent=4)

            return 200, "plaindb :: Success: 1 row inserted"

        if querytype == "select":
            name = parameters.get("name", None)
            address = parameters.get("address", None)
            phone = parameters.get("phone", None)
            query_param = []
            if name:
                name_x = re.compile(name)
                query_param.append(name_x)
            if address:
                ad_x = re.compile(address)
                query_param.append(ad_x)
            if phone:
                p_x = re.compile(address)
                query_param.append(p_x)
            output = []
            if not query_param:
                logger.info("THREAD - plaindb::Select - Selecting all rows as no predicate given.")
                if "json" in self._filename:
                    rows = None
                    with open(self._filename) as json_file_read:
                        rows = json.load(json_file_read)
                        for row in rows:
                            output.append(row)
                if "csv" in self._filename:
                    rows = None
                    with open(self._filename, mode='r') as csv_file:
                        csv_reader = csv.DictReader(csv_file)
                        for row in csv_reader:
                            output.append(row)
                return 200, output

            logger.info(
                "THREAD - plaindb::Select - Select Rows Name %s Address %s Phone %s" % (name, address, phone))

            if "json" in self._filename:
                rows = None
                with open(self._filename) as json_file_read:
                    rows = json.load(json_file_read)

                for row in rows:
                    matched = []
                    for matcher in query_param:
                        for key, value in row.items():
                            if matcher.match(value):
                                matched.append(True)
                    if any(matched):
                        output.append(row)

            if "csv" in self._filename:
                rows = None
                with open(self._filename, mode='r') as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    for row in csv_reader:
                        matched = []
                        for matcher in query_param:
                            for key, value in row.items():
                                if matcher.match(value):
                                    matched.append(True)
                        if any(matched):
                            output.append(row)

            if output:
                return 200, output
            else:
                return 200, "plaindb :: 0003 NO ROWS RETURNED."

        if querytype == "update":
            response, rows = self.query(logger, "select", **parameters)
            _cache = rows
            alt_num = len(rows)
            value = parameters.get("value", None)
            name = parameters.get("name", None)
            address = parameters.get("address", None)
            phone = parameters.get("phone", None)
            edit_param = []
            if name:
                edit_param.append("name")
            if address:
                edit_param.append("address")
            if phone:
                edit_param.append("address")
            if len(edit_param) > 1:
                logger.error("THREAD - plaindb::Update - At a time only one column can be altered. ")
                return 400, "plaindb :: Error 0003 At a time only one column can be updated."
            if "csv" in self._filename:
                fieldnames = ['name', 'address', 'phone']
                tmpfile = "tmp.csv"
                with open(tmpfile, mode='w') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()

                with open(self._filename, mode='r') as csv_read, open(tmpfile, "a") as csv_write:
                    csv_reader = csv.DictReader(csv_read)
                    csv_writer = csv.DictWriter(csv_write, fieldnames=fieldnames)
                    for read_row in csv_reader:
                        written_unmatch = False
                        written_inner = False
                        for row in rows:
                            if read_row[edit_param[0]] == row[edit_param[0]] and row in _cache and not written_inner:
                                written_unmatch = True
                                written_inner = True
                                logger.info("THREAD - plaindb::Update - Update row %s " % row)
                                row[edit_param[0]] = value
                                csv_writer.writerow(row)
                                _cache.remove(row)
                        if not written_unmatch:
                            written_unmatch = True
                            csv_writer.writerow(read_row)
                logger.info("THREAD - plaindb::Update - Updated %s row." % alt_num)
                shutil.move(tmpfile, self._filename)
                return 200, "plaindb :: Update: Success: %s row updated" % alt_num


    def blow(self, logger):
        """
        blow Destroys the database instance.

        :param logger:  A logger object.

        """
        logger.warning("THREAD - blow - Not Implemented")



def customlogger(log_level=None, log_file=None):
    """
    customlogger Generates a custom Logging mechanism at INFO or DEBUG level.
    The Error logs are marked as ERROR.
    In case the user misses the log file name, it generates a default file by name VM_Restore_dmYHMS.log

    :param log_level:
    :param log_file:
    :return: A Custom logger to console and a file.
    """
    fh = None
    FORMAT = "%(asctime)s %(levelname)s %(message)s"
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)
    # Reset the logger.handlers if it already exists.
    if logger.handlers:
        logger.handlers = []
    formatter = logging.Formatter(FORMAT)
    if log_file:
        fh = logging.FileHandler(log_file)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
