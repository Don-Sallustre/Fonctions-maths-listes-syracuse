def Syracuse(u) :
          if u%2==0 :
              u=u/2
          else :
              u=3*u+1
          return(u)

def Liste_Syracuse(u):
    L=[u]
    i=0
    while u!=1:
        L.append(Syracuse(u))
        u=Syracuse(u)
        i+=1
    return i

def temps_vol_sup100():
    u_n= 1
    i=0
    test=False
    while test==False:
        i=Liste_Syracuse(u_n)
        if i<100:
            u_n+=1
        else:
            test=True
    return u_n