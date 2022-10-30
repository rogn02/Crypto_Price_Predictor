from Modules import *
from LSTM_model import *
from GRU_model import *
def train_model(coin_name):
    if coin_name=="ETH":
        df=pd.read_csv("C:/Users/Rohan/Documents/PES/sem_5/MI/MI_Project/ND/Ethereum.csv")
    elif coin_name=="BNB":
        df=pd.read_csv("C:/Users/Rohan/Documents/PES/sem_5/MI/MI_Project/ND/Binance_Coin.csv")
    elif coin_name =="BTC":
        df=pd.read_csv("C:/Users/Rohan/Documents/PES/sem_5/MI/MI_Project/ND/Bitcoin.csv")
    elif coin_name =="USDT":
        df=pd.read_csv("C:/Users/Rohan/Documents/PES/sem_5/MI/MI_Project/ND/Tether.csv")
    price = df[['Price']]
    scaler = MinMaxScaler(feature_range=(-1, 1))
    price['Price'] = scaler.fit_transform(price['Price'].values.reshape(-1,1))
    #splitting the data into test and train data with numpy arrays
    def split_data(stock, lookback):
        data_raw = stock.to_numpy() # convert to numpy array
        data = []

        # create all possible sequences of length seq_len
        for index in range(len(data_raw) - lookback): 
            data.append(data_raw[index: index + lookback])

        data = np.array(data);
        #test_set_size = int(np.round(0.4*data.shape[0])); best
        tz=0.3
        test_set_size = int(np.round(tz*data.shape[0]));
        train_set_size = data.shape[0] - (test_set_size);
        print("Test size:",tz)
        x_train = data[:train_set_size,:-1,:]
        y_train = data[:train_set_size,-1,:]
        x_test = data[train_set_size:,:-1]
        y_test = data[train_set_size:,-1,:]
        return [x_train, y_train, x_test, y_test]
    lookback = 20 # choose sequence length 20 original
    print("Lookback:",lookback)
    x_train, y_train, x_test, y_test = split_data(price, lookback)
    #Converting to tensors
    x_train = torch.from_numpy(x_train).type(torch.Tensor)
    x_test = torch.from_numpy(x_test).type(torch.Tensor)
    y_train_gru = torch.from_numpy(y_train).type(torch.Tensor)
    y_test_gru = torch.from_numpy(y_test).type(torch.Tensor)
    y_train_lstm = torch.from_numpy(y_train).type(torch.Tensor)
    y_test_lstm = torch.from_numpy(y_test).type(torch.Tensor)

    print("hidden dims:",hidden_dim,"num layers:",num_layers,"num epochs:",num_epochs)
    print("\n")
    print("LSTM values:")
    LSTM_Model_train(x_train,y_train_lstm,x_test,scaler,y_test_lstm,coin_name)
    print("\n")
    print("GRU values:") 
    GRU_Model_train(x_train,y_train_gru,x_test,scaler,y_test_gru,coin_name)
