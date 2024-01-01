import pandas
import tensorflow as tf

### BEG DATA INTAKE
# read data file and confirm data shape
dataframe = pandas.read_csv('https://raw.githubusercontent.com/bryankolaczkowski/ALS3200C/main/phenopred.data.csv')
print(dataframe.shape)

# split into training and validation subsets, and confirm shape
train_dataframe = dataframe.sample(frac=0.8, random_state=402201)
valid_dataframe = dataframe.drop(train_dataframe.index)
print(train_dataframe.shape, valid_dataframe.shape, dataframe.shape)

# extract explanatory variables, convert to numpy and confirm shapes
snp_ids = [ x for x in dataframe.columns if x.find('SNP') == 0 ]
train_x = train_dataframe[snp_ids].to_numpy()
valid_x = valid_dataframe[snp_ids].to_numpy()
print(train_x.shape, valid_x.shape)

# extract response variables, convert to numpy and confirm shapes
train_y = train_dataframe['LS'].to_numpy()
valid_y = valid_dataframe['LS'].to_numpy()
print(train_y.shape, valid_y.shape)

# package into tensorflow.Dataset objects and batch
train_data = tf.data.Dataset.from_tensor_slices((train_x,train_y)).batch(10)
valid_data = tf.data.Dataset.from_tensor_slices((valid_x,valid_y)).batch(36)
### END DATA INTAKE

### BEG NEURAL NETWORK TRAIN-VALIDATE
## build and compile linear neural-network model
model = tf.keras.models.Sequential()
### BEG BUILD AND COMPILE MODEL
model.add(tf.keras.layers.InputLayer(input_shape=[17165]))
model.add(tf.keras.layers.Dropout(rate=0.7))
model.add(tf.keras.layers.Dense(1))
model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
              loss=tf.keras.losses.MeanAbsoluteError(),
              metrics=[tf.keras.metrics.MeanSquaredError()])

### END BUILD AND COMPILE MODEL
model.summary()

## fit and validate neural-network model
model.fit(train_data, epochs=500, validation_data=valid_data)
### END NEURAL NETWORK TRAIN-VALIDATE

### PLOT RESULTS FOR VISUALIZATION
## predict training and validation responses for plotting
train_y_hat = model.predict(train_x)
valid_y_hat = model.predict(valid_x)

## plot true-vs-predicted responses
import matplotlib.pyplot as plt
plt.plot([10,60],[10,60])
plt.scatter(train_y, train_y_hat, marker='o')
plt.scatter(valid_y, valid_y_hat, marker='+')
