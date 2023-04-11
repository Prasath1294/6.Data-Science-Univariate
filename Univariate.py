class Univariate():
    def quanQual(dataset):
        Quan=[]
        Qual=[]
        for i in dataset.columns:
            if (dataset[i].dtype=='O'):
                Qual.append(i)
            else:
                Quan.append(i)
        return Quan,Qual