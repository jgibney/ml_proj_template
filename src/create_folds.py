import pandas as pd
from sklearn import model selection

if __name__ == "__main__":
    df = pd.read.csv("input/train.csv")
    df['kfold']= -1

    df = df.sample(frac=1).reset_index(drop=True)

    kf = model_selection.StratifiedKFold(n_splitss=5, shuffle=False, random_state=42)

    for fold, (train_idx, val_idx) in enumerage(kf.split(X=df, df.target.values)):
        print(len(train_idx), len(val_idx)
        df.loc[val_idx, 'kfold'] = fold
    
    df.to_csv("input/train_folds.csv", index=False)
