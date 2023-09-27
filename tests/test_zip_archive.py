import os
from zipfile import ZipFile, ZIP_DEFLATED
from .conftest import tmp_path, resources_path

path_zip = (os.path.join(tmp_path, 'new.zip'))


def is_exist_zip(name, namelist):
    for item in namelist:
        if item == name:
            return True
    return False


def test_create_zip():
    source = os.listdir(resources_path)

    with ZipFile(path_zip, 'w', ZIP_DEFLATED) as archive:
        for file in source:
            add_file = os.path.join(resources_path, file)
            archive.write(add_file, arcname=file)

    with ZipFile(path_zip) as archive:

        files_list = archive.namelist()
        counter = 0
        for name in source:
            if is_exist_zip(name, files_list):
                counter += 1

        assert counter == len(source)
        assert os.path.exists(path_zip)
        assert len(source) == len(archive.infolist())

