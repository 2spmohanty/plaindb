__author__ = "Smruti Mohanty"

import json
import logging, sys
import argparse
from plaindb.core import customlogger, plainDB
from plaindb.render import HEADER, BODY, FOOTER

import webbrowser
import time

def get_args():
    """get_args function consolidates all the argumnets passed to the plaindb cli app.

    Returns:
        The parsed arguments.
    """
    parser = argparse.ArgumentParser(description="This is a complex db of the world that's so simple.")

    parser.add_argument("-n", "--name", nargs=1, required=False, dest='name', type=str,
                        help='Name of the Person.')
    parser.add_argument("-a", "--address", nargs=1, required=False, dest='address', type=str,
                        help='Address of the Person.')
    parser.add_argument("-p", "--phone", nargs=1, required=False, dest='phone', type=str,
                        help='Phone Number of the Person.')
    parser.add_argument("-f", "--file", nargs=1, required=True, dest='ftype', default="csv", type=str,
                        help='Core Database File Type. json/csv. Default is csv.')
    parser.add_argument("-v", "--value", nargs=1, required=False, dest='value', type=str,
                        help='New Value to be passed with -e/--edit option. ')
    parser.add_argument("-o", "--out", required=False, dest='out', action='store_true',
                        help='Display the result in a web page. Used with -q option. ')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-i", "--insert", required=False, dest='insert', action='store_true',
                       help='Insert Records to the DB.')
    group.add_argument("-q", "--query", required=False, dest='query', action='store_true',
                       help='Query Records of the Person.')
    group.add_argument("-u", "--update", required=False, dest='update', action='store_true',
                       help='Update the Record of the Person.')
    group.add_argument("-b", "--blow", required=False, dest='blow', action='store_true',
                       help='With power comes responsibility. This blows your database.')

    args = parser.parse_args()
    return args


def main():
    args = get_args()
    _logfile = "plaindb.log"
    logger = customlogger(logging.INFO, _logfile)
    logger.info("THREAD - plaindb - main - Initializing database file.")
    _filename = None
    if args.ftype:
        _ft = args.ftype[0]
        if "json" in _ft or "csv" in _ft:
            _filename = "plain-db-core." + args.ftype[0]
        else:
            logger.warning(
                "THREAD - plaindb - main - Could not understand file extension. Going ahead with default csv type.")
            _filename = "plain-db-core.csv"
        logger.info("THREAD - plaindb - main - The core db file is %s" % _filename)

    # Instantiate the DB
    logger.info("THREAD - plaindb - main - Initializing database Instance.")
    db = plainDB(_filename)

    # Insert Record WorkFlow
    _name = _address = _phone = _value = None
    if args.insert:
        if args.name:
            _name = args.name[0]
        if args.address:
            _address = args.address[0]
        if args.phone:
            _phone = args.phone[0]
        status, response = db.query(logger,"insert", name=_name, address=_address, phone=_phone)
        if status == 200:
            logger.info("THREAD - plaindb - main - %s" % response)
        else:
            logger.error("THREAD - plaindb - main - Error while inserting row. %s" % response)

    if args.query:
        if args.name:
            _name = args.name[0]
        if args.phone:
            _name = args.phone[0]
        if args.address:
            _address = args.address[0]
        status, response = db.query(logger,"select", name=_name, address=_address, phone=_phone)
        if status == 200:
            logger.info("THREAD - plaindb - main - %s" % response)
            if args.out:
                logger.info("THREAD - plaindb - Viewer - Output option selected. Rendering Web-page.")
                final_body = ""
                row = 1
                for item in response:
                    final_body = final_body + BODY.format(row_num=row, name=item["name"], address=item["address"],
                                                          phone=item["phone"])
                    row += 1
                web_content = HEADER + final_body + FOOTER
                with open("plaindb.html",'w') as f:
                    f.write(web_content)
                time.sleep(2)
                webbrowser.open("plaindb.html")

        else:
            logger.error("THREAD - plaindb - main - Error while selecting row. %s" % response)

    if args.update:
        if args.name:
            _name = args.name[0]
        if args.phone:
            _name = args.phone[0]
        if args.address:
            _address = args.address[0]
        if args.value:
            _value = args.value[0]
        status, response = db.query(logger,"update", name=_name, address=_address, phone=_phone, value=_value)
        if status == 200:
            logger.info("THREAD - plaindb - main - %s" % response)
        else:
            logger.error("THREAD - plaindb - main - Error while Updating row. %s" % response)


if __name__ == "__main__":
    main()
