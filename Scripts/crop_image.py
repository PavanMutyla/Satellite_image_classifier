'''
processes annotated images, extracts labeled regions of intrest and save's them accordingly
'''
img_path = 'path'
ann = 'annotations path'
output = 'dest folder'
labels = [] # list of desired classes
def process(image_folder=img_path, annotation_folder=ann, output_folder=output, labels=labels):
    
    image_files = [file for file in os.listdir(image_folder) if file.lower().endswith(('.png'))]
     
    print(len(image_files))
    for image_file in image_files:
        
        image_path = os.path.join(image_folder, image_file)
        annotation_path = os.path.join(annotation_folder, image_file.replace('.png', '.txt')) 
        completed.append(image_file)
        print(image_path)
        
        if not os.path.exists(annotation_path):
            continue

       
        img_data = cv2.imread(image_path)

       
        with open(annotation_path, 'r') as f:
            data = f.readlines()

        

        for i in data:
            val = i.strip().split()
            x1, y1, x2, y2, x3, y3, x4, y4 = map(int, map(float, val[:8]))
            label = val[8]

            if label in labels:
                
                
                crop = img_data[min(y1, y2, y3, y4):max(y1, y2, y3, y4), min(x1, x2, x3, x4):max(x1, x2, x3, x4)]
                if crop is None:
                    print(f"Failed to crop region for label {label} in image {img_path}")
                    continue

               
                folder = os.path.join(output_folder, label)
                os.makedirs(folder, exist_ok=True)

                
                output_path = os.path.join(folder, f"{label}_{len(os.listdir(folder)) + 1}.png")
                cv2.imwrite(output_path, crop)
