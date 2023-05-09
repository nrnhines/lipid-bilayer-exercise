from neuron import h, gui

s = h.Section()
s.L = s.diam = h.sqrt(100/h.PI) # 100um2 means 1nA = 1mA/cm2
ic = h.IClamp(s(.5))
ic.delay = 1
ic.dur = 2
ic.amp = 0.04

h.load_file("lipid.ses")

