from os import walk
from pathlib import Path


class DirectoryFile:
    def __init__(self, directory: str):
        self.directory = directory

    def get_file(self):
        outputs = []
        for path, directories, files in walk(self.directory):
            for file in files:
                if file.endswith('.txt'):
                    outputs.append(f'{path}/{file}')

        return outputs

    def text_from_file(self):
        texts = []
        for file in self.get_file():
            with open(f'{file}') as output:
                text = "\n".join(text.strip() for text in output.readlines())
                texts.append(text)

        combined_texts = "\n".join(texts)
        return combined_texts

    def append_text_to_file(self, text, file_name):
        samples = self.get_file()
        for sample in samples:
            sample_path = Path(sample)
            if sample_path.name == file_name:
                with open(sample_path, 'a') as output:
                    output.write(f'{text}\n')
                return None
        return f'File {file_name} does not exist.'
