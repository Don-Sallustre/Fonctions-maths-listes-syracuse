def Syracuse(u) :
          if u%2==0 :
              u=u/2
          else :
              u=3*u+1
          return(u)

def Liste_Syracuse(u):
    L=[u]
    while u!=1:
        L.append(Syracuse(u))
        u=Syracuse(u)
    return L


def temps_vol_altitude(u_0):
    u_n_add_1=u_0+1
    i=0
    liste=Liste_Syracuse(u_0)
    while u_n_add_1>u_0:
        u_n_add_1=liste[i]
        i+=1
    return i