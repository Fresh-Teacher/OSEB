import zipfile
import os

def zip_folder(folder_path, zip_path, password):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, folder_path))
        zip_file.setpassword(password.encode())

if __name__ == "__main__":
    folder_to_zip = "path/to/your/folder"
    output_zip_file = "locked_folder.zip"
    password = "12345"
    
    zip_folder(folder_to_zip, output_zip_file, password)
    print(f"Locked folder created at: {output_zip_file}")
