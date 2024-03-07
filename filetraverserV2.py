# So what we need to do is go into the directory and just train things straight

#First we need to 

import os
import cv2
import glob

def print_image_files(directory):
    sendTrain = True
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.png'): 
                file_path = os.path.join(root, file)

                relative_path = (os.path.dirname(root))

                train_dir = os.path.join(relative_path, 'train')
                test_dir = os.path.join(relative_path, 'test')

                if not os.path.exists(train_dir):
                    os.makedirs(train_dir)
                
                if not os.path.exists(test_dir):
                    os.makedirs(test_dir)
                

                #In here we will need to cut the photos up - when cutting the photos into chunks we will need to send some chunks to train and some to not train

def go_through():
    print("hi")
    for experiment in glob.glob("/home/ajbam/Documents/data/*"):
        print(experiment)
        experimentString = experiment + "/*"
        for category in glob.glob(experimentString):
            print(category)
            categoryString = category + "/*"
            for image in glob.glob(categoryString):
                print(image)
                #Now from here I can call cut and just have it store all of the data to an array


go_through()
#data_directory_path = '/home/ajbam/Documents/data'
#print_image_files(data_directory_path)


def save_chunks(image, chunk_size, output_folder):
    global chunk_n
    height, width, _ = image.shape
    num_rows = height // chunk_size
    num_cols = width // chunk_size

    for row in range(num_rows):
        for col in range(num_cols):
            y_start = row * chunk_size
            y_end = y_start + chunk_size
            x_start = col * chunk_size
            x_end = x_start + chunk_size

            sub_image = image[y_start:y_end, x_start:x_end]

            # see if sub_image is invalid or contains and white pixels
            check_wp = cv2.cvtColor(sub_image, cv2.COLOR_BGR2GRAY)
            if 255 in check_wp or not (check_wp.shape[0] == chunk_size and check_wp.shape[1] == chunk_size):
                continue

            chunk_n += 1            
            filename = f"{chunk_n}.png"
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, sub_image)

def main():
    pass

if __name__ == "__main__":
    main()
