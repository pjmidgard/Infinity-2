from time import time
cvf=0
import os
import binascii
self="'"

namez = input("for compression c or e for extract: ")
#@Author Jurijus pacalovas
class encypthion_class:

    def encypthion1(self):

                 
                
                self.name = "Author: Jurijus Pacalovas"

                print(self.name)

                if namez!="c" and namez!="e":
                    print("Your enter incorrect letter")
                
                if namez=="c":


                    
                   
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                   
                    
                        
                    namea=""
                    namem=""
                    namema="?"
                    
                    assxw=0
                    
                    nameas=name
                    nac=len(nameas)

                    long=len(name)
                   
                    name_cut=len(".bin")
                    
                    nameas=name+".bin"
                    name_bofore=len(nameas)
                    
                    
                    

                    	 
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                 
                    size_data3=""
                    size_data2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
                        
                
                        size_after2=len(data)
                        #print(size_after2)  
                        
                        if len(data)==0 or len(data)>2**40:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                            
                      
                         

                  
                        s=str(data)
                        
                        
                        lenf1=len(data)
                          
                    
                            
  
                            
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countraz==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    qqwslenf=len(size_data2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)

                                size_data11=""
                                size_data12=""
                                long21=len(size_data3)
                                limit1=0
                                size_data4="'"
                                
                                Times_of_times=0
                                
                                

                                
                                while limit1!=1:    
                                
                                    size_data4=size_data2
                                    long_B=len(size_data4)
                                    long=len(size_data4)
                                    Times_of_times+=1
                                    if Times_of_times==100:
                                        limit1
                                        
                                    
                                    
                                        
                                    
                                    info_hex=size_data4
                                    times10=0 
                                    limit=0
                                   
                                    
                                    while times10!=1:
                                        

                                        
                                        Caculus_oct3="1001"
                                        
                                    
                                    
                                        size_data3=info_hex

                                       
                                        
                                        long=len(size_data3)
                                        #print(long)
                                        
                                        if long<=32:
                                            limit=1
                                            smaller=1
                                            limit1=1
                                        #print(long)
                                       
                                       
                                        block=0
                                        
                                        blocks=32
                                        #print(blocks)
                                        
                                        Calculus=""
                                        Caculus_oct=0
                                        res=""
                                        res3=0
                                        res6=""
                                        file=0
                                        resf=0
                                        times_compress=0
                                       

                                        
        
                                        res_one_time=0
                                        
                                        while block<long:
                                            Calculus=size_data3[block:block+blocks]
                                            Calculus8=size_data3[block+blocks:block+blocks+3]
                                            block=block+blocks
                                            times_compress+=1
                                            
                                            if file==0:
                                                    
                                                long2=len(Calculus)
                                                #print(long2)
                                                block2=0
                                                blocks2=0
                                                Times=-4
                                                Times2=0
                                                res1=0
                                                res2=0
                                                res5=0
                                                limit_find=0
                                                
                                                while Times2!=28:
                                                    Times2+=4
                                                   
                                                    #print(Times2)
                                                    
            
                                                    if Calculus[:4]==Calculus[Times2:Times2+4] and res1==0 and long2==blocks:
                                                            Caculus_oct=format(Times//4,'03b')
                                                            
                                                            
                                                            Caculus_oct=Caculus_oct
                                                         
                                                            Caculus_oct2=format(Times2//4,'03b')
                                                           
                                                            #print(Caculus_oct)
                                                            #print(Caculus_oct2)
                                                            
                                                           
                                                            
                                                            res7=Calculus[:3]+Calculus[3:Times2]+Caculus_oct3+Calculus[Times2+4:]
                                                            res8=Calculus[:3]+Calculus[3:Times2]+Caculus_oct3[::-1]+Calculus[Times2+4:]
                                                            
                                                            #print(len(res7))   
                                                                
                                                        
                                                            res1=1
                                                            res2=0
                                                            
                                                            res5=1
                                                            
                                                            
                                                            if Calculus[Times2:Times2+4]==Caculus_oct3:
                                                                    
                                                                   res9=res7

                                                            elif Calculus[Times2:Times2+4]==Caculus_oct3[::-1]:
                                                            
                                                                  res9=res8
                                                                   
                                                            else:
                                                                res9=Calculus 
                                                                
                                                    
                                                if res5==1:              
                                                    res+=res9           
                                                else:
                                                    res+=Calculus                                          
                                                       #print("4")
                                                       
                                                       
                                                
                                                    
                                                resf+=1
                                                
                                            
                                            #print(block)                                        
                                            
                                        
         
                                                    
                                                    
                                                    
                                         
                   
                                        

                                            
                                        
                                        times10+=1
                                       
                                            
                                        info_hex=res 
                                        long_after_compression=len(info_hex)
                                        if long==long_after_compression:
                                            limit=1
                                            limit1=1

                                         
                              
                                        info_hex=res
                                            
                                        
                                        
                                        
                                                                       
                                    
                                    encypthion=info_hex
                                    
                                   
                                    
                                    #print(res3)
                                    #print(resf)
                                    #print(limit)
                                    
                                    size_data14=""
                                    
                                    
       
                                    
                                                                        
                                    size_data12=encypthion

                                    long21=len(size_data12)
                                    #print(long21)

                                    
                                    
                                    limit1=1
                                
                               
                                    
                                size_data11=size_data12
                                
                                
                                #print(size_data11)
                                  
                               
             
                                                                                
                                n = int(size_data11, 2)
                                
                                qqwslenf=len(size_data11)
                                qqwslenf=(qqwslenf/8)*2
                                qqwslenf=str(qqwslenf)
                                qqwslenf="%0"+qqwslenf+"x"
                             
                                jl=binascii.unhexlify(qqwslenf % n)
                                
                              
                                
                                import paq
                                jl= paq.compress(jl)
                             
                                
                               
                                
                                    
                                size_after=len(jl)

                                size_after=len(jl)
                                
                                   
                                qqqwz=qqqwz+1
                                szxzzza=""
                                szxzs=""
                            
                                assxw=assxw+1
                                if assxw==1:
                                    assx=10
                                    if assx==10:

                                        f2.write(jl)
                                        x2 = time()
                                        x3=x2-x
                                        return print(x3)

    def encypthion2(self):

                 
                 if namez=="e":
                    
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                   
                    namea=""
                    namem=""
                    namema="?"
                   
                 
                    assxw=0
                    nameas=name
                    nac=len(nameas)
                    name_cut=""
                    name_cut=len(".bin")
                    nameas=name
                    
                    name_long=len(nameas)
                    nameSS=name[name_long-name_cut:]
                    if nameSS!=".bin":
                        x3=0.0
                        return print(x3)
                        
                    nameas=name[:name_long-name_cut]
                    nac=len(nameas)
                    
                  
                    
                    long=len(nameas)

                    nac=len(nameas)
                   
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                 
                    size_data3=""
                    size_data2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        
                        data = binary_file.read()
                        import paq
                        data= paq.decompress(data)
                        

                        

                    
                        if len(data)==0:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                     	

                        s=str(data)
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1
                                            
                                   

                                    if countraz==1:
                                        size_data2=size_data
                            
                                    n = int(size_data2, 2)
                                
                                    qqwslenf=len(size_data2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    size_data=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(size_data)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            size_data="0"+size_data
                                            z=z+1

                                    size_data2=size_data

                                    lenf3=len(size_data2)
                                lenf2=len(size_data2)  
                                x4=1
                                if x4==1:

                                    Count_add_block=0

                                    

                                    size_data3=size_data2
                                    
                                size_data11=""
                                size_data12=""
                                long21=len(size_data3)
                                limit1=0
                                size_data4="'"
                                
                                Times_of_times=0
                                
                                

                                
                                while limit1!=1:    
                                
                                    size_data4=size_data2
                                    long_B=len(size_data4)
                                    long=len(size_data4)
                                    Times_of_times+=1
                                    if Times_of_times==100:
                                        limit1
                                        
                                    
                                    
                                        
                                    
                                    info_hex=size_data4
                                    times10=0 
                                    limit=0
                                   
                                    
                                    while times10!=1:
                                        

                                        
                                        Caculus_oct3="1001"
                                        
                                    
                                    
                                        size_data3=info_hex

                                       
                                        
                                        long=len(size_data3)
                                        #print(long)
                                        
                                        if long<=32:
                                            limit=1
                                            smaller=1
                                            limit1=1
                                        #print(long)
                                       
                                       
                                        block=0
                                        
                                        blocks=32
                                        #print(blocks)
                                        
                                        Calculus=""
                                        Caculus_oct=0
                                        res=""
                                        res3=0
                                        res6=""
                                        file=0
                                        resf=0
                                        times_compress=0
                                       

                                        
        
                                        res_one_time=0
                                        
                                        while block<long:
                                            Calculus=size_data3[block:block+blocks]
                                            Calculus8=size_data3[block+blocks:block+blocks+3]
                                            block=block+blocks
                                            times_compress+=1
                                            
                                            if file==0:
                                                    
                                                long2=len(Calculus)
                                                #print(long2)
                                                block2=0
                                                blocks2=0
                                                Times=-4
                                                Times2=0
                                                res1=0
                                                res2=0
                                                res5=0
                                                limit_find=0
                                                
                                                while Times2!=28:
                                                    Times2+=4
                                                   
                                                    #print(Times2)
                                                    
            
                                                    if Calculus[:4]==Calculus[Times2:Times2+4][::-1] and res1==0 and long2==blocks:
                                                            Caculus_oct=format(Times//4,'03b')
                                                            
                                                            
                                                            Caculus_oct=Caculus_oct
                                                         
                                                            Caculus_oct2=format(Times2//4,'03b')
                                                           
                                                            #print(Caculus_oct)
                                                            #print(Caculus_oct2)
                                                            
                                                           
                                                            
                                                            res7=Calculus[:3]+Calculus[3:Times2]+Caculus_oct3+Calculus[Times2+4:]
                                                            res8=Calculus[:3]+Calculus[3:Times2]+Caculus_oct3[::-1]+Calculus[Times2+4:]
                                                            
                                                                
                                                                
                                                        
                                                            res1=1
                                                            res2=0
                                                            
                                                            res5=1
                                                            
                                                            
                                                            if Calculus[Times2:Times2+4]==Caculus_oct3:
                                                                    
                                                                   res9=res7

                                                            elif Calculus[Times2:Times2+4]==Caculus_oct3[::-1]:
                                                            
                                                                  res9=res8
                                                                   
                                                            else:
                                                                res9=Calculus 
                                                                
                                                    
                                                if res5==1:              
                                                    res+=res9             
                                                               
                                                else:
                                                    res+=Calculus                                          
                                                       #print("4")
                                                       
                                                       
                                                
                                                    
                                                resf+=1
                                                
                                            
                                            #print(block)                                        
                                            
                                        
         
                                                    
                                                    
                                                    
                                         
                   
                                        

                                            
                                        
                                        times10+=1
                                       
                                            
                                        info_hex=res 
                                        long_after_compression=len(info_hex)
                                        if long==long_after_compression:
                                            limit=1
                                            limit1=1

                                         
                              
                                        info_hex=res
                                            
                                        
                                        
                                        
                                                                       
                                    
                                    encypthion=info_hex
                                    
                                   
                                    
                                    #print(res3)
                                    #print(resf)
                                    #print(limit)
                                    
                                    size_data14=""
                                    
                                    
       
                                    
                                                                        
                                    size_data12=encypthion

                                    long21=len(size_data12)

                                    
                                    
                                    limit1=1
                                
                               
                                    
                                size_data11=size_data12
                                
                                
                                #print(size_data11)
                                  
                               
             
                                                                                
                                n = int(size_data11, 2)
                                
                                qqwslenf=len(size_data11)
                                qqwslenf=(qqwslenf/8)*2
                                qqwslenf=str(qqwslenf)
                                qqwslenf="%0"+qqwslenf+"x"
                             
                                jl=binascii.unhexlify(qqwslenf % n)
                                
                              
                                
                                
                             
                                
                               
                                
                                    
                                size_after=len(jl)

                                size_after=len(jl)
                                
                                   
                                qqqwz=qqqwz+1
                                szxzzza=""
                                szxzs=""
                            
                                assxw=assxw+1
                                if assxw==1:
                                    assx=10
                                    if assx==10:

                                        f2.write(jl)
                                        x2 = time()
                                        x3=x2-x
                                        return print(x3)
                  
self=""                                
d=encypthion_class()
    
xw=d.encypthion1()
print(xw)

xw1=d.encypthion2()
print(xw1)
