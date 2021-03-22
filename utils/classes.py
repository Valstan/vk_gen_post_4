import json
import os


class ReadWriteFile:

    def __init__(self, patch, name, file):
        self.patch = patch
        self.name = name
        self.file = file

    def read_file(self):
        with open(os.path.join(self.patch, self.name), 'r', encoding='utf-8') as f:
            self.file = json.load(f)
            return self.file

    def write_file(self):
        with open(os.path.join(self.patch, self.name), 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.file, indent=2, ensure_ascii=False))

