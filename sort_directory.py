import os
import shutil
import argparse

ap = argparse.ArgumentParser()

ap.add_argument('-D','--dir', required=False, help='Directory to sort')

args = vars(ap.parse_args())
if args['dir'] == None:
    DIR = os.getcwd()
elif os.path.exists(args['dir']):
    DIR = args['dir']
for file in os.listdir(DIR):
    if not os.path.isdir(os.path.join(DIR, file)):
        name, ext = os.path.splitext(file)
        ext = ext[::-1][:-1][::-1]
        if os.path.exists(os.path.join(DIR, ext.upper())):
            shutil.move(os.path.join(DIR, file), os.path.join(DIR, ext.upper(), file))
        else:
            os.mkdir(os.path.join(DIR, ext.upper()))
            shutil.move(os.path.join(DIR, file), os.path.join(DIR, ext.upper(), file))