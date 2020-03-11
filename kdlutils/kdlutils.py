
# A small utility function when using sequential conv nets
# This function takes the input dimensions and a list of dictionary of sequential conv and maxpool layers
def getOutShape(input_dim,layersList):
    """
    params:
    input_dim : input dimension of the data to the sequential network. A tupple (in_channels,H_in,W_in)
    layersList : A list of dictionaries for each layer. Refer the example to know more.
    """
    in_ch, H_in, W_in = input_dim
    out_ch_prev = in_ch
    out_ch = in_ch

    for layer in layersList:
        for type_,params in layer.items():
            if type_=='conv':
                in_ch,out_ch,K,S,P,D = params
                if in_ch == out_ch_prev:
                    out_ch_prev = out_ch                          
                else:
                    print("dims did not match!")
                H_in = (H_in + 2*P - D*(K-1)-1)//S + 1
                W_in = (W_in + 2*P - D*(K-1)-1)//S + 1

            elif type_=='mp':
                K,S,P,D = params
                H_in = (H_in + 2*P - D*(K-1)-1)//S + 1
                W_in = (W_in + 2*P - D*(K-1)-1)//S + 1

            else:
                print("Wrong input layer type !")
    
    return H_in,W_in,out_ch

# input_dim = (1,600,800)
# layersList = [{'conv':(1,7,3,1,1,1)},{'mp':(2,2,0,1)},{'conv':(7,14,3,1,1,1)},{'mp':(2,2,0,1)},{'conv':(14,30,3,1,1,1)},{'mp':(2,2,0,1)}]

# print(getOutShape(input_dim,layersList)) 