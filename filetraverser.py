import os

def print_image_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.png'):  # Assuming we're only looking for PNG images
                print(os.path.join(root, file))

# Replace the path below with the path to your 'data' directory
data_directory_path = '/path/to/data'
print_image_files(data_directory_path)
