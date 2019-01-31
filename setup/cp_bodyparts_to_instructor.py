#!/usr/bin/env python

from pathlib import Path
import shutil
from uuid import uuid1

home_path = Path('/home/ubuntu/')

project_base = home_path / 'source/deeplearning-workshop'
instructor_folder = home_path / 'instructor_notebook/bodyparts_data/'

bodyparts = [
    'abdomen', 'ankle', 'buttocks', 'elbow', 'face', 'foot', 'groin',
    'hand', 'knee', 'lower_arm', 'lower_back', 'lower_leg', 'neck',
    'shoulder', 'thorax', 'upper_arm', 'upper_back', 'upper_leg', 'wrist',
]


def copy_bodypart_folders(team_path):
    for body_part in bodyparts:
        body_part_folder = (team_path / 'bodyparts_data' / body_part)
        for file in body_part_folder.iterdir():
            if file.is_file():
                # Add some random uuid to output to make sure filenames do not clash
                if 'ilabbers' in file.name:
                    continue

                shutil.copy(file, instructor_folder / body_part / (str(uuid1()) + file.name))


def main():
    team_folder_base = home_path / 'dis_jan_2019_notebooks'
    teams = range(14)

    for t in teams:
        team_path = team_folder_base / ("team_%i" % (t + 1))
        copy_bodypart_folders(team_path)


if __name__ == '__main__':
    main()
