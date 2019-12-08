# Usage: 
#     generate_image_list.py > assets.json

import sys
import json
import glob

assets = []

glob_pat = sys.argv[1] if len(sys.argv) > 1 else '*.jpg'
thumbs_dir = sys.argv[2] if len(sys.argv) > 2 else 'thumbs'

for f in sorted(glob.glob(glob_pat)):
    assets.append({'src': f, 'thumb': thumbs_dir + f})

print(json.dumps(assets, indent=1))
