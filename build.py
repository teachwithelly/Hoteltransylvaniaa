from pathlib import Path
import shutil
p=Path('/mnt/data/ht_work');a=p/'assets'
for i,f in enumerate(sorted(Path('/mnt/data').glob('image(20261103-2246*.png'))): shutil.copy(f,a/f'room{i+1}.png')
# actual chronological sort
