
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

def upconv(Din,k,s,p,op=0):
    """
    Din : Input dimension
    k : kernel size
    s : stride
    p : padding
    op: output padding
    """
    Dout = (Din-1)*s - 2*p + (k-1) + op + 1
    print(Dout)

def conv(Din,k,s,p,op=0):
    """
    
    Din : Input dimension
    k : kernel size
    s : stride
    p : padding
    op: output padding
    """
    Dout = (Din+2*p - (k-1) - 1)//s + 1
    print(Dout)
