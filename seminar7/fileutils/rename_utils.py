import os

def rename_files(directory, desired_name, num_digits, source_extension, target_extension, name_range=None):
    if not os.path.exists(directory):
        print(f"Директории '{directory}' не существует.")
        return

    files = [f for f in os.listdir(directory) if f.endswith(source_extension)]

    if not files:
        print(f"Файлов с расширением '{source_extension}' не найдено.")
        return

    for i, filename in enumerate(files, start=1):
        if name_range:
            original_name = filename[name_range[0]:name_range[1]]
        else:
            original_name = filename[:filename.rfind(source_extension)]

        new_filename = f"{desired_name}_{i:0{num_digits}d}.{target_extension}"

        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)

        os.rename(old_path, new_path)

        print(f"Переименован: {filename} -> {new_filename}")
