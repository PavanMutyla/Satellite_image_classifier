epochs = 4
torch.manual_seed(42)
# ann -> the model (ResNet)
for epoch in tqdm(range(epochs)):
    tr_loss, tr_acc = 0, 0
    test_loss, test_acc = 0, 0
    ann.to(device)
    ann.train()

    for batch, (X, y) in enumerate(train_loader):
        X, y = X.to(device), y.to(device)

        preds = ann(X)
        tr_acc += accuracy(y, preds.argmax(dim=1))
        loss = loss_func(preds, y)
        tr_loss += loss.item()

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    tr_loss /= len(train_loader)
    tr_acc /= len(train_loader)

    ann.eval()
    with torch.inference_mode():
        for X, y in test_loader:
            X = X.to(device)
            y = y.to(device)

            test_preds = ann(X)

            test_loss += loss_func(test_preds, y).item()
            test_acc += accuracy(y, test_preds.argmax(dim=1))

        test_loss /= len(test_loader)
        test_acc /= len(test_loader)

    print(f" train_loss: {tr_loss:.3f}, train_acc: {tr_acc:.3f}, test_loss: {test_loss:.3f}, test_acc: {test_acc:.3f}")
