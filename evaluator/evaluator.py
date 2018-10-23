from __future__ import print_function
import argparse
import h5py
import os
import sys
import cv2

from metrics import prepare_folders, computeCUS, computeBHI

parser = argparse.ArgumentParser("Evaluator for OST")
parser.add_argument('-a', '--automatic_summarization', type=str, required=True)
parser.add_argument('-u', '--users_summarization', type=str, required=True)
parser.add_argument('-v', '--original_video', type=str, required=True)
parser.add_argument('-e', '--epsilon', default=0.4, type=float)
parser.add_argument('-d', '--distance', default=120, type=int)
parser.add_argument('-m', '--method', type=str, required=True, default='bhi', choices=['cus', 'bhi'])
parser.add_argument('--user_summary_path',
                    type=str, help="User summary path in the h5 file (ex video_11/user_summary)")
parser.add_argument('--automatic_summary_path',
                    type=str, help="Automatic summary path in the h5 file (ex video_11/machine_summary)")

args = parser.parse_args()


'''useFolders
Loads the summarizations from folders.
'''
def useFolders():
    cap = cv2.VideoCapture(args.original_video)
    videoLength = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if args.method == 'cus':
        f1, kappa = computeCUS(
            args.epsilon,
            videoLength,
            args.users_summarization,
            args.automatic_summarization
        )
    else:
        f1, kappa = computeBHI(
            args.epsilon,
            videoLength,
            args.distance,
            args.users_summarization,
            args.automatic_summarization
        )

    return f1, kappa


'''useH5
Loads the summarizations from H5 files.
'''
def useH5():
    if args.automatic_summary_path is None or args.user_summary_path is None:
        sys.exit("Error: Summaries paths in H5 files were not specified.")

    uFile = h5py.File(args.users_summarization, 'r')
    aFile = h5py.File(args.automatic_summarization, 'r')

    # Access user summaries table in H5
    user_summaries = uFile
    for tableName in args.user_summary_path.split('/'):
        user_summaries = user_summaries[tableName]

    # Access automatic summaries table in H5
    automatic_summary = aFile
    for tableName in args.automatic_summary_path.split('/'):
        automatic_summary = automatic_summary[tableName]
    automatic_summary = automatic_summary[:]

    prepare_folders(user_summaries, automatic_summary, args.original_video)

    cap = cv2.VideoCapture(args.original_video)
    videoLength = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if args.method == 'cus':
        f1, kappa = computeCUS(
            args.epsilon,
            videoLength
        )
    else:
        f1, kappa = computeBHI(
            args.epsilon,
            videoLength,
            args.distance
        )

    return f1, kappa


if __name__ == '__main__':
    print('Evaluating summarization...')
    print('Method:', args.method)
    print('Epsilon', args.epsilon)
    if args.method == 'bhi':
        print('Distance', args.distance)

    if os.path.isdir(args.users_summarization) and os.path.isdir(args.automatic_summarization):
        f1, kappa = useFolders()
    else:
        f1, kappa = useH5()

    print('Average F1:', round(f1, 2))
    print('Average Kappa:', round(kappa, 2))
