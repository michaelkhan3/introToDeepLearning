from numpy import exp, array, random, dot

class NeuralNetwork():
	"""docstring for NeuralNetwork"""
	def __init__(self):
		random.seed(1)

		self.synaptic_weights = 2 * random.random((3,1)) -1

	def __sigmoid(self, x):
		return 1/(1 + exp(-x))

	#gradient of the sigmoid curve		
	def __sigmoid_derivative(self, x):
		return x * (1-x)


	def train(self, training_set_inputs, training_set_outputs, number_of_traning_iterations):
		for iterations in xrange(number_of_traning_iterations):
			#pass the training set through our neural network
			output =  self.think(training_set_inputs)

			#calculate error
			error = training_set_outputs - output

			#multiply the error by the input ad again by the gradient of the sigmoid curve
			adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

			#adjust the weights
			self.synaptic_weights += adjustment


	def think(self, inputs):
		return self.__sigmoid(dot(inputs, self.synaptic_weights))





if __name__ == '__main__':

	#initialise a single neuron neural network
	neural_network = NeuralNetwork()

	print 'random starting synaptic weights:'
	print neural_network.synaptic_weights

	#training set
	training_set_inputs = array([[0,0,1], [1,1,1], [1,0,1], [0,1,1]])
	training_set_outputs = array([[0,1,1,0]]).T

	#training the neural network using a training set.
	#Do it 10,000 times and make small adjustments each time
	neural_network.train(training_set_inputs, training_set_outputs, 10000)

	print 'New synaptic weights after training: '
	print neural_network.synaptic_weights

	#Test the neural network with a new situation 
	print 'Considering new situation [1,0,0] -> ?: '
	print neural_network.think(array([1,0,0]))