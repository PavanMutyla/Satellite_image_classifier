train_dir = 'path'
test_dir = 'path'
val_dir = 'path' # optional
data = 'path'
def split(data, train_dir, test_dir, val_dir):
    files = [i for i in os.listdir(data)]
    
    for file in files:
        folder = os.path.join(data, file)
        images = [i for i in os.listdir(folder) if i.endswith('.png')]
        n = len(images)
        train = int(n * 0.8)
        val = int(0.5 * (n - train))
        test = n - train - val
        
        random.seed(44)
        random.shuffle(images)

        # Label folders
        tr = os.path.join(train_dir, file)
        te = os.path.join(test_dir, file)
        va = os.path.join(val_dir, file)

        # Make folders
        os.makedirs(tr, exist_ok=True)
        os.makedirs(te, exist_ok=True)
        os.makedirs(va, exist_ok=True)

        # Save lists
        tr_images = images[:train]
        val_images = images[train:train+val]
        te_images = images[train+val:]

        # Save in folders
        for img in tr_images:
            s = os.path.join(folder, img)
            d = os.path.join(tr, img)
            shutil.copy(s, d)

        for img in te_images:
            so = os.path.join(folder, img)
            de = os.path.join(te, img)
            shutil.copy(so, de)

        for img in val_images:
            source = os.path.join(folder, img)
            dest = os.path.join(va, img)
            shutil.copy(source, dest)
