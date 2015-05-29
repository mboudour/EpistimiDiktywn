from pylab import *
def cororBarD(ss):
    #cdict = {'red': ((0.0, 0.0, 0.0),
                     #(0.5, 0.25, 0.25),
                     #(1.0, 0.75, 1.0)),
             #'green': ((0.0, 0.0, 0.0),
                       #(0.5, 0.25, 0.25),
                       #(1.0, 0.75, 1.0)),
             #'blue': ((0.0, 0.0, 0.0),
                       #(0.5, 0.0, 0.25),
                       #(1.0, 1., 1.0))}
    cdict = {'red':  [(0.0,  1.0, 1.0),
                    
                   (0.33, 1.0, 1.0),
                   (0.52, 0.0, 0.0),
                   (1.0,  0.0, 0.0)],

         'blue': [(0.0,  1.0, 1.0),
                   (0.25, 0.0, 0.0),
                  (0.33, 0.0, 0.0),
                   (0.50, 1.0, 1.0),
                   (0.66, 1.0, 1.0),
                   (0.75, 0.0,0.0),
                   (1.0,  0.0, 0.0)],

         'green':  [(0.0,  1.0, 1.0),
                   (0.15, 0.0, 0.0),
                   (0.66, 0.0, 0.0),
                   (1.0,  1.0, 1.0)]}
    #cdict = {'red':  [(0.0,  0.0, 0.0),
                    
                   #(0.33, 1.0, 1.0),
                   #(0.45, 1.0, 1.0),
                   #(1.0,  0.0, 0.0)],

         #'green': [(0.0,  0.0, 0.0),
                   #(0.33, 0.0, 0.0),
                   ##(0.5, 1.0, 1.0),
                   #(0.66, 1.0, 1.0),
                   #(0.81, 1.0,1.0),
                   #(1.0,  0.0, 0.0)],

         #'blue':  [(0.0,  0.0, 0.0),
                   
                   #(0.66, 0.0, 0.0),
                   #(1.0,  1.0, 1.0)]}
    #cdict = {'red':   [(0.0,  0.0, 0.0),
                   #(0.5,  1.0, 1.0),
                   #(1.0,  1.0, 1.0)],

         #'green': [(0.0,  0.0, 0.0),
                   #(0.25, 0.0, 0.0),
                   #(0.75, 1.0, 1.0),
                   #(1.0,  1.0, 1.0)],

         #'blue':  [(0.0,  0.0, 0.0),
                   #(0.5,  0.0, 0.0),
                   #(1.0,  1.0, 1.0)]}
    my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap',cdict,ss)
    return my_cmap
def cororBar():
    #cdict = {'red': ((0.0, 0.0, 0.0),
                     #(0.5, 0.25, 0.25),
                     #(1.0, 0.75, 1.0)),
             #'green': ((0.0, 0.0, 0.0),
                       #(0.5, 0.25, 0.25),
                       #(1.0, 0.75, 1.0)),
             #'blue': ((0.0, 0.0, 0.0),
                       #(0.5, 0.0, 0.25),
                       #(1.0, 1., 1.0))}
    cdict = {'red':  [(0.0,  1.0, 1.0),
                    
                   (0.33, 1.0, 1.0),
                   (0.52, 0.0, 0.0),
                   (1.0,  0.0, 0.0)],

         'blue': [(0.0,  1.0, 1.0),
                   (0.25, 0.0, 0.0),
                  (0.33, 0.0, 0.0),
                   (0.50, 1.0, 1.0),
                   (0.66, 1.0, 1.0),
                   (0.75, 0.0,0.0),
                   (1.0,  0.0, 0.0)],

         'green':  [(0.0,  1.0, 1.0),
                   (0.15, 0.0, 0.0),
                   (0.66, 0.0, 0.0),
                   (1.0,  1.0, 1.0)]}
    
    #cdict = {'red':   [(0.0,  0.0, 0.0),
                   #(0.5,  1.0, 1.0),
                   #(1.0,  1.0, 1.0)],

         #'green': [(0.0,  0.0, 0.0),
                   #(0.25, 0.0, 0.0),
                   #(0.75, 1.0, 1.0),
                   #(1.0,  1.0, 1.0)],

         #'blue':  [(0.0,  0.0, 0.0),
                   #(0.5,  0.0, 0.0),
                   #(1.0,  1.0, 1.0)]}
    my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap',cdict,512)
    return my_cmap
#my_cmap=colorbar()
def drawScat(at_matx,mcmap,y=None,li=[]):
    #print rand(10,10)
    if y!=None:
        ylim(y,0)

    pcolor(at_matx,cmap=mcmap)
    if len(li)>0:
        colorbar(ticks=li)
    else:
        colorbar()
    #show()
def drawScatInOut(at_matx,mcmap,y=None,li=[],mi=[],mo=[]):
    #print rand(10,10)
    
    if y!=None:
        ylim(y,0)
    if len(mi)>0 and len(mo)>0:
        pcolor(at_matx,cmap=mcmap)
        axis([mi[0],mi[1],mo[0],mo[1]])
        xlabel('In-Degree')
        ylabel('Out-Degree')
    else:
        pcolor(at_matx,cmap=mcmap)
        xlabel('In-Degree')
        ylabel('Out-Degree')
    if len(li)>0:
        colorbar(ticks=li)
    else:
        colorbar()
    #ylabel('fraction of Nodes')
    
    #show()

def drawScattes():
    #print rand(10,10)
    pcolor(rand(10,10),cmap=cororBar())
    colorbar()
    #show()

#drawScattes()
