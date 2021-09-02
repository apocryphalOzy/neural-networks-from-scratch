# Output = input * weight + bias
inputs = [1, 2, 3, 2.5]

weights = [[.2, .8, -.5, 1],
         [.5, -.91, .26, -.5],
         [-.26, -.27, .17, .87]]
biases = [2, 3, .5]

#output of current layer
layer_outputs = []
# For each neuron
for neuron_weights, neuron_bias in zip(weights, biases): #destructuring
    #zeroed output of given neuron
    neuron_output = 0
    #For each input and weight to the neuron`
    for n_input, weight in zip(inputs, neuron_weights):
        # Multiply this input by associated weight
        # and add to the neuron's output variable
        neuron_output += n_input * weight
    
    #add bias to neuron output
    neuron_output += neuron_bias
    #put neuron's result to the layer's output list
    layer_outputs.append(neuron_output)

print(layer_outputs)
    


