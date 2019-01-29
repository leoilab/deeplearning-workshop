from pathlib import Path
import shutil

home_path = Path('/home/ubuntu/')

project_base = home_path / 'source/deeplearning-workshop'
team_folder_file_paths = [
    project_base / 'Exercise 1 - Cats and dogs.ipynb',
    project_base / 'Exercise 2 - Bodyparts.ipynb',
    home_path / 'instructor_notebook' / 'bodypart_predictor.h5'
]


def set_folder_content(team_path):
    for p in team_folder_file_paths:
        (team_path / p.name).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(str(p), str(team_path / p.name))


bodyparts = [
    'abdomen', 'ankle', 'buttocks', 'elbow', 'face', 'foot', 'groin',
    'hand', 'knee', 'lower_arm', 'lower_back', 'lower_leg', 'neck',
    'shoulder', 'thorax', 'upper_arm', 'upper_back', 'upper_leg', 'wrist',
]


def create_bodypart_folders(team_path):
    for bp in bodyparts:
        (team_path / 'bodyparts_data' / bp).mkdir(parents=True, exist_ok=True)

    hand_src = project_base / 'bodyparts_data' / 'hand' / 'fingers.jpg'
    shutil.copy(hand_src, team_path / 'bodyparts_data' / 'hand' / hand_src.name)


def main():
    team_folder_base = home_path / 'dis_jan_2019_notebooks'
    teams = range(14)
    for t in teams:
        team_path = team_folder_base / ("team_%i" % (t + 1))
        set_folder_content(team_path)
        create_bodypart_folders(team_path)


if __name__ == '__main__':
    main()
