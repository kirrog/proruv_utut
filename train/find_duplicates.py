import json
from collections import defaultdict
from pathlib import Path

from PIL import Image
from tqdm import tqdm

img_list = list(Path("../data/data_v2").glob("*.jpg"))
images_duplicates_dict = defaultdict(list)
for img_path in tqdm(img_list):
    img = Image.open(img_path)
    entropy = img.entropy()
    images_duplicates_dict[entropy].append(img_path)
    # img = img.resize((480, 600))
    # img.save(main_dir + image)
duplicates_entropies = list(map(lambda x: (x[0], [str(y) for y in x[1]], len(x[1])) ,filter(lambda x: len(x[1]) > 1, images_duplicates_dict.items())))
print(len(duplicates_entropies))
print(sum(map(lambda x: x[2], duplicates_entropies)))
with open("../data/data_v2_results.json", "w", encoding="UTF-8") as f:
    json.dump(duplicates_entropies, f, ensure_ascii=False)
