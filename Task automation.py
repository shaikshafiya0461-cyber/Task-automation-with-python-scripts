import os
import shutil

def organize_jpg_files():
    source_dir = "./source_folder"
    target_dir = "./jpg_folder"

    # Create directories if they do not exist
    if not os.path.exists(source_dir):
        os.makedirs(source_dir)
        print(f"Created dummy source directory: {source_dir}")
        print("Please place some .jpg files inside it and run again.")
        return

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    files = os.listdir(source_dir)
    moved_count = 0

    for file in files:
        if file.lower().endswith(".jpg"):
            source_path = os.path.join(source_dir, file)
            target_path = os.path.join(target_dir, file)
            shutil.move(source_path, target_path)
            print(f"Moved: {file}")
            moved_count += 1

    print(f"\nAutomation complete. Total .jpg files moved: {moved_count}")

if __name__ == "__main__":
    organize_jpg_files()