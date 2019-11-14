import importlib.util
import inspect
import os


def build_test():
    packages = ["core", "infra", "mail", "resource", "shop", "socialnetwork"]
    with open("_temp.py", "w+") as temp_file:
        temp_file.truncate()
        temp_file.write("import unittest\n")
        for package in packages:
            for root, dirs, files in os.walk(f"./../{package}"):
                if "unittest" in root or 'functionaltest' in root:
                    for file in files:
                        if file.endswith("test.py"):
                            file_absolute_path = os.path.abspath(root + "\\" + file)
                            module = file[:-3]
                            spec = importlib.util.spec_from_file_location(module, file_absolute_path)
                            _module = spec.loader.load_module()
                            for class_name, class_type in inspect.getmembers(_module, inspect.isclass):
                                if class_type.__module__ == module:
                                    _from = root[5:].replace('\\', '.') + "." + module
                                    temp_file.write(f"from {_from} import {class_name}\n")

        temp_file.write("\n\nclass full_test(unittest.TestCase):\n\tunittest.main()")


if __name__ == '__main__':
    build_test()
