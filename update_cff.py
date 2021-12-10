import fileinput
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("tag", help="Github tag.")
args = parser.parse_args()

for lines in fileinput.input('CITATION.cff', inplace=True):
    line = lines.split(':')
    key = line[0].strip()
    if key == 'version':
        print('{} : {}'.format(key, args.tag))
    else:
        print(lines.rstrip())
