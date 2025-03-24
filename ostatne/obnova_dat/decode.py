import zipfile

zip_path = 'data.zip'
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    for info in zip_ref.infolist():
        print(info.filename, info.file_size)

