# -*- coding: utf-8 -*-
import femm
# Parameters
I= 1 # current
femm.openfemm()
femm.newdocument(0) # 0 for magnetostatic problem
femm.mi_probdef(0,"millimeters","axi", 1e-8) # frequency,units,type,precision
# Draw the geometry
femm.mi_drawline(5,50,6,50)
femm.mi_drawline(6,50,6,-50)
femm.mi_drawline(6,-50,5,-50)
femm.mi_drawline(5,-50,5,50)
# Add block labels
femm.mi_addblocklabel(5.5,46) # label for winding
femm.mi_addblocklabel(25,60)  # label for air
# Add materials
femm.mi_getmaterial("Air")
femm.mi_getmaterial("1mm")
# Add coil properties
femm.mi_addcircprop("Coil", I, 1) # 1 is for series circuit (coil)
# Associate properties to  block labels
# Winding
femm.mi_selectlabel(5.5,46)
femm.mi_setblockprop("1mm",0,0,"Coil",0,0,100) # 100 turns
femm.mi_clearselected();
# Air
femm.mi_selectlabel(25,60)
femm.mi_setblockprop("Air",0,0,"",0,0,1)
femm.mi_clearselected();
# Create boundary conditions using default parameters
femm.mi_makeABC()
# zoom and save
femm.mi_zoomnatural()
femm.mi_saveas("inductor.fem");
# Analyze and load solution
femm.mi_analyze()
femm.mi_loadsolution()
# Hide flux lines (contour) and show density plot of B
femm.mo_hidecontourplot()
femm.mo_showdensityplot(1, 0, 1.25e-3, 0, "bmag")
# Inductance calculation
Coil_props = femm.mo_getcircuitproperties("Coil") # current, voltage, flux
L= Coil_props[2]/I
print("Inductance (uH)= ", L*1e6)

    





