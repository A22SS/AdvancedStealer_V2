import os
import shutil

class FileOperations:
    @staticmethod
    def copy(source, destination):
        if os.path.isfile(source):
            shutil.copy2(source, destination)
            return os.path.isfile(destination)
        else:
            print(f"Le fichier {source} n'a pas été trouvé.")
            return False

    @staticmethod
    def move(source, destination):
        shutil.move(source, destination)
        return os.path.isfile(destination)

    @staticmethod
    def create(path, content=''):
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        with open(path, 'w') as f:
            f.write(content)
        return os.path.isfile(path)

    @staticmethod
    def delete(path):
        if os.path.isfile(path):
            os.remove(path)
            return not os.path.isfile(path)
        else:
            print(f"Le fichier {path} n'a pas été trouvé.")
            return False

    @staticmethod
    def list_files(directory):
        return [os.path.join(directory, fname) for fname in os.listdir(directory)]

file_ops = FileOperations()
