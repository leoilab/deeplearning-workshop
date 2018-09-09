import json
from pathlib import Path
import tqdm

descriptions = Path('data/isic/descriptions/')
images_path = Path('data/isic/images/')
images_out_train = Path('data/isic/train')
images_out_valid = Path('data/isic/valid')

for file in tqdm.tqdm(descriptions.iterdir()):
    description = json.loads(file.read_text())
    image_file = images_path / (file.stem + '.jpg')
    if 'meta' not in description:
        continue
    if 'clinical' not in description['meta']:
        continue
    if 'benign_malignant' not in description['meta']['clinical']:
        continue
    if description['meta']['clinical']['benign_malignant'] not in ['benign', 'malignant']:
        continue

    # Split data equally to validation and training.
    if int(description['_id'], 16) % 2 > 0:
        images_out = images_out_valid
    else:
        images_out = images_out_train

    out_dir = images_out / description['meta']['clinical']['benign_malignant']
    out_dir.mkdir(exist_ok=True, parents=True)

    if image_file.is_file():
        image_symlink = out_dir / (file.stem + '.jpg')
        image_symlink.symlink_to(image_file.absolute())
