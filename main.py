from data import DataSeq
from merge import Merge
from heap import Heap

import time
import argparse

parser=argparse.ArgumentParser(description="Sort Visulization")
parser.add_argument('-l','--length',type=int,default=64)
#intervalo para trocas (visualização)
parser.add_argument('-i','--interval',type=int,default=1)
parser.add_argument('-t','--sort-type',type=str,default='Bubble', 
                                    choices=["Bubble","Insertion","Merge","Selection","Radix", "Heap"])


args=parser.parse_args()

if __name__ == "__main__":
    MAXLENGTH= 10000
    Length=    args.length if args.length<MAXLENGTH else MAXLENGTH
    Interval=  args.interval
    SortType=  args.sort_type
  
    try:
        SortMethod=eval(SortType)
    except:
        print("Busca nao encontrada %s !"%SortType)
        exit()

    ds=DataSeq(Length, time_interval=Interval, sort_title=SortType)
    ds.Visualize()
    ds.StartTimer()
    SortMethod(ds)
    ds.StopTimer()

    #tempo da janela gráfica
    time.sleep(3)


