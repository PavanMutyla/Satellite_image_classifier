train_path = ''
test_path = ''
# transform
trans = transforms.Compose([transforms.Resize((224,224)), transforms.ToTensor()])
# imagefolder 
train_data = datsets.ImageFolder(train_path, transform = trans)
test_data = datasets.ImageFolder(test_path, transform = trans)
# dataloader
train_loader = DataLoader(train_data, batch_size  = 32, shuffle = True)
test_loader  = DataLoader(test_data, batch_size = 32, shuffle = False)

classes = train_data.classes

def accuracy(true, preds):
    correct = torch.eq(true, preds).sum().item()
    acc = (correct/len(preds)) * 100
    return acc

loss_func = nn.CrossEntropyLoss()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

ann = torchvision.models.resnet18(weights=w).to(device)
optimizer = torch.optim.SGD(params = ann.parameters(), lr = 0.01)

ann.fc = nn.Linear(512, len(classes))
