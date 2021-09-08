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

    print('weights: ' )
    print( neuron_weights)
    print('biases: ' )
    print( neuron_bias)
    #zeroed output of given neuron
    neuron_output = 0
    print('outer loop' )
    print(neuron_output)
    #For each input and weight to the neuron`
    for n_input, weight in zip(inputs, neuron_weights):

        print('n_input ')
        print(n_input)
        print('weight ')
        print(weight)
        # Multiply this input by associated weight
        # and add to the neuron's output variable
        neuron_output += n_input * weight

        print('inner loop neuron output ')
        print( neuron_output)
    
    #add bias to neuron output
    neuron_output += neuron_bias
    print('neuron_output')
    print(neuron_output)
    #put neuron's result to the layer's output list
    layer_outputs.append(neuron_output)

print(layer_outputs)
    


