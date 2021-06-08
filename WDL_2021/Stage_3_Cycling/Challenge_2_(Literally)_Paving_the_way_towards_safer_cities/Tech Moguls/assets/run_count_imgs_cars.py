# Credits: https://towardsdatascience.com/count-number-of-cars-in-less-than-10-lines-of-code-using-python-40208b173554

# Imports
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

# CVLib Imports
import cvlib as cv
from cvlib.object_detection import draw_bbox


# Data Directories
# Data Dir
data_dir = "../data"

# Results Dir
results_dir = "../results/car_counts"
if os.path.isdir(results_dir) == False:
    os.makedirs(results_dir)

# Images Dir
images_dir = "Competition/images"

# Complete Path
complete_path = os.path.join(data_dir, images_dir)


# Count all the images
images_fnames = [i for i in os.listdir(complete_path) if not i.startswith('.')]
print(f"Number of Images: {len(images_fnames)}")

# Create a numpy array to append image names and car counts
car_counts = np.zeros(shape=(len(images_fnames), 2), dtype=object)


# Go through all the images and count the cars
for idx, img_fname in enumerate(images_fnames):
    
    # Print stuff
    print(f"Image {idx+1}/{len(images_fnames)}")


    # Read image
    im = cv2.imread(os.path.join(complete_path, img_fname))


    # Count cars
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)


    # Saving the image
    cv2.imwrite(os.path.join(results_dir, img_fname), output_image)
    
    
    # Show
    count = int(label.count('car'))
    print(f"Image Name: {img_fname} | Count: {count}")
    # plt.imshow(output_image)
    # plt.show()
    # print('Number of cars in the image is '+ str(label.count('car')))


    # Append to the array
    # Column 0 - Image Filename
    car_counts[idx, 0] = img_fname
    
    # Column 1 - Car Count
    car_counts[idx, 1] = count

    # Save numpy
    np.save(file="car_count_results.npy", arr=car_counts, allow_pickle=True)



# Save final numpy
np.save(file="car_count_results.npy", arr=car_counts, allow_pickle=True)
print("Finished.")