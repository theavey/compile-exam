#!/usr/bin/python

########################################################################
#                                                                      #
# This script was written by Thomas Heavey in 2017.                    #
#        theavey@bu.edu     thomasjheavey@gmail.com                    #
#                                                                      #
# Copyright 2017 Thomas J. Heavey IV                                   #
#                                                                      #
# Licensed under the Apache License, Version 2.0 (the "License");      #
# you may not use this file except in compliance with the License.     #
# You may obtain a copy of the License at                              #
#                                                                      #
#    http://www.apache.org/licenses/LICENSE-2.0                        #
#                                                                      #
# Unless required by applicable law or agreed to in writing, software  #
# distributed under the License is distributed on an "AS IS" BASIS,    #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or      #
# implied.                                                             #
# See the License for the specific language governing permissions and  #
# limitations under the License.                                       #
#                                                                      #
########################################################################

from argparse import ArgumentParser
import re
from shutil import copyfile

parser = ArgumentParser()
parser.add_argument('filename')
parser.add_argument('-f', '--forward', action='store_true')

args = parser.parse_args()
copyfile(args.filename, args.filename+'.bak')

basename = re.match(r".+(?=\.tex)", args.filename).group(0)

# with open(args.filename, 'rw') as in_file, \
#      open(basename+'-solutions.tex', 'w') as out_file:
#     for line in in_file:
#         if r'\printanswers' in line:
#             in_file.write('\printanswers\n')
#         else:
#             continue

if args.forward:
    contents = []
    with open(args.filename, 'r') as in_file:
        for line in in_file:
            if r'\printanswers' in line:
                contents.append('\printanswers\n')
            else:
                contents.append(line)
    with open(args.filename, 'w') as out_file:
        for line in contents:
            out_file.write(line)
else:
    contents = []
    with open(args.filename, 'r') as in_file:
        for line in in_file:
            if r'\printanswers' in line:
                contents.append('%\printanswers\n')
            else:
                contents.append(line)
    with open(args.filename, 'w') as out_file:
        for line in contents:
            out_file.write(line)

