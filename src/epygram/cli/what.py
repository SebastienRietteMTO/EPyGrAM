#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) Météo France (2014-)
# This software is governed by the CeCILL-C license under French law.
# http://www.cecill.info

import sys
import argparse

import epygram
from epygram import epylog
from .args_catalog import (add_arg_to_parser,
                           files_management, fields_management,
                           runtime_options, output_options)


def main():
    epygram.init_env()
    args = get_args()
    if args.verbose:
        epylog.setLevel('INFO')
    else:
        epylog.setLevel('WARNING')
    what(args.filename,
         details=args.details,
         sortfields=args.sortfields,
         stdoutput=args.stdout,
         mode=args.mode)


def what(filename,
         details=None,
         sortfields=None,
         stdoutput=False,
         mode='fid_list'):
    """
    Get info about resource.

    :param filename: name of the file to be processed.
    :param details: if not None, gives some more details about the fields.
    :param sortfields: sort fields. Cf. formats what() method for further details.
    :param stdoutput: if True, output is redirected to stdout.
    :param mode: for GRIB only, among ('one+list', 'fid_list', 'what', 'ls', 'mars'), \n
          - 'one+list' = gives the validity/geometry of the first field in
            GRIB, plus the list of fid.
          - 'fid_list' = gives only the fid of each field in GRIB.
          - 'what' = gives the values of the keys from each GRIB message that
            are used to generate an **epygram** field from the message (slower).
          - 'ls' = gives the values of the 'ls' keys from each GRIB message.
          - 'mars' = gives the values of the 'mars' keys from each GRIB message.
    """
    resource = epygram.formats.resource(filename, openmode='r')
    if resource.format not in ('GRIB', 'FA', 'DDHLFA', 'LFA', 'LFI', 'TIFFMF'):
        epylog.warning(" ".join(["tool NOT TESTED with format",
                                 resource.format, "!"]))
    if stdoutput:
        out = sys.stdout
    else:
        out = open(resource.container.abspath + '.info', 'w')
    resource.what(out,
                  details=details,
                  sortfields=sortfields,
                  mode=mode)


def get_args():

    parser = argparse.ArgumentParser(description="An EPyGrAM tool for asking what's inside a resource.",
                                     epilog='End of help for: %(prog)s (EPyGrAM-' + epygram.__version__ + ')')
    add_arg_to_parser(parser, files_management['principal_file'])
    add_arg_to_parser(parser, output_options['get_field_details'])
    add_arg_to_parser(parser, fields_management['GRIB_what_mode'])
    add_arg_to_parser(parser, fields_management['GRIB_sort'])
    add_arg_to_parser(parser, fields_management['sort_fields'])
    add_arg_to_parser(parser, output_options['stdout'])
    add_arg_to_parser(parser, runtime_options['verbose'])
    return parser.parse_args()

