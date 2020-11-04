#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module: magic_numbers.py

Description:
    simple script to create magic numbers from gu511 student ids

Usage:
    <usage>

"""

import argparse
import hashlib
import logging
import logging.config
import os
import yaml

import numpy as np


# ----------------------------- #
#   Module Constants            #
# ----------------------------- #

HERE = os.path.dirname(os.path.realpath(__file__))
LOGGER = logging.getLogger('magic_numbers')
LOGCONF = os.path.join(HERE, 'logging.yaml')
with open(LOGCONF, 'rb') as f:
    logging.config.dictConfig(yaml.load(f, Loader=yaml.FullLoader))
LOGGER.setLevel(logging.INFO)


# ----------------------------- #
#   Main routine                #
# ----------------------------- #

def calc_magic_number(guid):
    """given a user's georgetown id, calculate a completely meaningless number

    args:
        guid (str): georgetown user id

    returns:
        None

    raises:
        None

    """
    h = hashlib.md5(guid.encode())
    seed = int(h.hexdigest(), 16) % (2 ** 32)
    LOGGER.info(seed)
    np.random.seed(seed)
    rands = np.random.random(20)
    LOGGER.info(rands)
    return rands.mean()


# ----------------------------- #
#   Command line                #
# ----------------------------- #

def parse_args():
    """parse command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--guid", help="your georgetown id", required=True)
    args = parser.parse_args()
    LOGGER.info("arguments set to {}".format(vars(args)))
    return args


if __name__ == '__main__':
    args = parse_args()
    print(calc_magic_number(args.guid))



"""
command:python magic_numbers.py -g lysd9

result:
2020-10-13 22:56:11,926 INFO     [magic_numbers.parse_args:74] arguments set to {'guid': 'lysd9'}
2020-10-13 22:56:11,927 INFO     [magic_numbers.calc_magic_number:58] 863627482
2020-10-13 22:56:11,927 INFO     [magic_numbers.calc_magic_number:61] [0.38478646 0.58393849 0.04171458 0.59311085 0.86511265 0.91084178
 0.05976166 0.62256386 0.22371605 0.64904188 0.81766045 0.52924444
 0.75484959 0.90881735 0.06509912 0.54363916 0.67000531 0.27912985
 0.53320985 0.19492979]
0.5115586586866703

"""

