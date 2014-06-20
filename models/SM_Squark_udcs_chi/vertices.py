# This file was automatically created by FeynRules 1.6.16
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (November 20, 2012)
# Date: Mon 15 Jul 2013 12:10:55


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_12})

V_2 = Vertex(name = 'V_2',
             particles = [ P.g, P.g, P.g, P.g ],
             color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
             couplings = {(1,1):C.GC_18,(0,0):C.GC_18,(2,2):C.GC_18})

V_3 = Vertex(name = 'V_3',
             particles = [ P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_7})

V_4 = Vertex(name = 'V_4',
             particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVVV2 ],
             couplings = {(0,0):C.GC_11})

V_5 = Vertex(name = 'V_5',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_36})

V_6 = Vertex(name = 'V_6',
             particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVVV2 ],
             couplings = {(0,0):C.GC_22})

V_7 = Vertex(name = 'V_7',
             particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVVV5 ],
             couplings = {(0,0):C.GC_37})

V_8 = Vertex(name = 'V_8',
             particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVVV2 ],
             couplings = {(0,0):C.GC_23})

V_9 = Vertex(name = 'V_9',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_20})

V_10 = Vertex(name = 'V_10',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS1 ],
              couplings = {(0,0):C.GC_54})

V_11 = Vertex(name = 'V_11',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_21})

V_12 = Vertex(name = 'V_12',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_55})

V_13 = Vertex(name = 'V_13',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_53})

V_14 = Vertex(name = 'V_14',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_56})

V_15 = Vertex(name = 'V_15',
              particles = [ P.ghG, P.ghG__tilde__, P.g ],
              color = [ 'f(3,1,2)' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_12})

V_16 = Vertex(name = 'V_16',
              particles = [ P.a, P.scl__tilde__, P.scl ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_1})

V_17 = Vertex(name = 'V_17',
              particles = [ P.chi__tilde__, P.c, P.scl__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_19})

V_18 = Vertex(name = 'V_18',
              particles = [ P.c__tilde__, P.chi, P.scl ],
              color = [ 'Identity(1,3)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_19})

V_19 = Vertex(name = 'V_19',
              particles = [ P.a, P.a, P.scl__tilde__, P.scl ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_20 = Vertex(name = 'V_20',
              particles = [ P.a, P.scr__tilde__, P.scr ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_4})

V_21 = Vertex(name = 'V_21',
              particles = [ P.chi__tilde__, P.c, P.scr__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_19})

V_22 = Vertex(name = 'V_22',
              particles = [ P.c__tilde__, P.chi, P.scr ],
              color = [ 'Identity(1,3)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_19})

V_23 = Vertex(name = 'V_23',
              particles = [ P.a, P.a, P.scr__tilde__, P.scr ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_10})

V_24 = Vertex(name = 'V_24',
              particles = [ P.a, P.sdl__tilde__, P.sdl ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_1})

V_25 = Vertex(name = 'V_25',
              particles = [ P.chi__tilde__, P.d, P.sdl__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_19})

V_26 = Vertex(name = 'V_26',
              particles = [ P.d__tilde__, P.chi, P.sdl ],
              color = [ 'Identity(1,3)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_19})

V_27 = Vertex(name = 'V_27',
              particles = [ P.a, P.a, P.sdl__tilde__, P.sdl ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_28 = Vertex(name = 'V_28',
              particles = [ P.a, P.sdr__tilde__, P.sdr ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_3})

V_29 = Vertex(name = 'V_29',
              particles = [ P.chi__tilde__, P.d, P.sdr__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_19})

V_30 = Vertex(name = 'V_30',
              particles = [ P.d__tilde__, P.chi, P.sdr ],
              color = [ 'Identity(1,3)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_19})

V_31 = Vertex(name = 'V_31',
              particles = [ P.a, P.a, P.sdr__tilde__, P.sdr ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_32 = Vertex(name = 'V_32',
              particles = [ P.a, P.ssl__tilde__, P.ssl ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_1})

V_33 = Vertex(name = 'V_33',
              particles = [ P.chi__tilde__, P.s, P.ssl__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_19})

V_34 = Vertex(name = 'V_34',
              particles = [ P.s__tilde__, P.chi, P.ssl ],
              color = [ 'Identity(1,3)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_19})

V_35 = Vertex(name = 'V_35',
              particles = [ P.a, P.a, P.ssl__tilde__, P.ssl ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_36 = Vertex(name = 'V_36',
              particles = [ P.a, P.ssr__tilde__, P.ssr ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_3})

V_37 = Vertex(name = 'V_37',
              particles = [ P.chi__tilde__, P.s, P.ssr__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_19})

V_38 = Vertex(name = 'V_38',
              particles = [ P.s__tilde__, P.chi, P.ssr ],
              color = [ 'Identity(1,3)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_19})

V_39 = Vertex(name = 'V_39',
              particles = [ P.a, P.a, P.ssr__tilde__, P.ssr ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_9})

V_40 = Vertex(name = 'V_40',
              particles = [ P.a, P.sul__tilde__, P.sul ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_1})

V_41 = Vertex(name = 'V_41',
              particles = [ P.chi__tilde__, P.u, P.sul__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_19})

V_42 = Vertex(name = 'V_42',
              particles = [ P.u__tilde__, P.chi, P.sul ],
              color = [ 'Identity(1,3)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_19})

V_43 = Vertex(name = 'V_43',
              particles = [ P.a, P.a, P.sul__tilde__, P.sul ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_8})

V_44 = Vertex(name = 'V_44',
              particles = [ P.a, P.sur__tilde__, P.sur ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_4})

V_45 = Vertex(name = 'V_45',
              particles = [ P.chi__tilde__, P.u, P.sur__tilde__ ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.FFS1 ],
              couplings = {(0,0):C.GC_19})

V_46 = Vertex(name = 'V_46',
              particles = [ P.u__tilde__, P.chi, P.sur ],
              color = [ 'Identity(1,3)' ],
              lorentz = [ L.FFS2 ],
              couplings = {(0,0):C.GC_19})

V_47 = Vertex(name = 'V_47',
              particles = [ P.a, P.a, P.sur__tilde__, P.sur ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_10})

V_48 = Vertex(name = 'V_48',
              particles = [ P.g, P.sul__tilde__, P.sul ],
              color = [ 'T(1,3,2)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_13})

V_49 = Vertex(name = 'V_49',
              particles = [ P.a, P.g, P.sul__tilde__, P.sul ],
              color = [ 'T(2,4,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_15})

V_50 = Vertex(name = 'V_50',
              particles = [ P.g, P.g, P.sul__tilde__, P.sul ],
              color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_18,(1,0):C.GC_18})

V_51 = Vertex(name = 'V_51',
              particles = [ P.g, P.sdl__tilde__, P.sdl ],
              color = [ 'T(1,3,2)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_13})

V_52 = Vertex(name = 'V_52',
              particles = [ P.a, P.g, P.sdl__tilde__, P.sdl ],
              color = [ 'T(2,4,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_15})

V_53 = Vertex(name = 'V_53',
              particles = [ P.g, P.g, P.sdl__tilde__, P.sdl ],
              color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_18,(1,0):C.GC_18})

V_54 = Vertex(name = 'V_54',
              particles = [ P.g, P.sur__tilde__, P.sur ],
              color = [ 'T(1,3,2)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_13})

V_55 = Vertex(name = 'V_55',
              particles = [ P.a, P.g, P.sur__tilde__, P.sur ],
              color = [ 'T(2,4,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_17})

V_56 = Vertex(name = 'V_56',
              particles = [ P.g, P.g, P.sur__tilde__, P.sur ],
              color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_18,(1,0):C.GC_18})

V_57 = Vertex(name = 'V_57',
              particles = [ P.g, P.sdr__tilde__, P.sdr ],
              color = [ 'T(1,3,2)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_13})

V_58 = Vertex(name = 'V_58',
              particles = [ P.a, P.g, P.sdr__tilde__, P.sdr ],
              color = [ 'T(2,4,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_16})

V_59 = Vertex(name = 'V_59',
              particles = [ P.g, P.g, P.sdr__tilde__, P.sdr ],
              color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_18,(1,0):C.GC_18})

V_60 = Vertex(name = 'V_60',
              particles = [ P.g, P.scl__tilde__, P.scl ],
              color = [ 'T(1,3,2)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_13})

V_61 = Vertex(name = 'V_61',
              particles = [ P.a, P.g, P.scl__tilde__, P.scl ],
              color = [ 'T(2,4,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_15})

V_62 = Vertex(name = 'V_62',
              particles = [ P.g, P.g, P.scl__tilde__, P.scl ],
              color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_18,(1,0):C.GC_18})

V_63 = Vertex(name = 'V_63',
              particles = [ P.g, P.ssl__tilde__, P.ssl ],
              color = [ 'T(1,3,2)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_13})

V_64 = Vertex(name = 'V_64',
              particles = [ P.a, P.g, P.ssl__tilde__, P.ssl ],
              color = [ 'T(2,4,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_15})

V_65 = Vertex(name = 'V_65',
              particles = [ P.g, P.g, P.ssl__tilde__, P.ssl ],
              color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_18,(1,0):C.GC_18})

V_66 = Vertex(name = 'V_66',
              particles = [ P.g, P.scr__tilde__, P.scr ],
              color = [ 'T(1,3,2)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_13})

V_67 = Vertex(name = 'V_67',
              particles = [ P.a, P.g, P.scr__tilde__, P.scr ],
              color = [ 'T(2,4,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_17})

V_68 = Vertex(name = 'V_68',
              particles = [ P.g, P.g, P.scr__tilde__, P.scr ],
              color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_18,(1,0):C.GC_18})

V_69 = Vertex(name = 'V_69',
              particles = [ P.g, P.ssr__tilde__, P.ssr ],
              color = [ 'T(1,3,2)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_13})

V_70 = Vertex(name = 'V_70',
              particles = [ P.a, P.g, P.ssr__tilde__, P.ssr ],
              color = [ 'T(2,4,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_16})

V_71 = Vertex(name = 'V_71',
              particles = [ P.g, P.g, P.ssr__tilde__, P.ssr ],
              color = [ 'T(1,-1,3)*T(2,4,-1)', 'T(1,4,-1)*T(2,-1,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_18,(1,0):C.GC_18})

V_72 = Vertex(name = 'V_72',
              particles = [ P.Z, P.scl__tilde__, P.scl ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_39})

V_73 = Vertex(name = 'V_73',
              particles = [ P.a, P.Z, P.scl__tilde__, P.scl ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_43})

V_74 = Vertex(name = 'V_74',
              particles = [ P.Z, P.scr__tilde__, P.scr ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_42})

V_75 = Vertex(name = 'V_75',
              particles = [ P.a, P.Z, P.scr__tilde__, P.scr ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_45})

V_76 = Vertex(name = 'V_76',
              particles = [ P.Z, P.sdl__tilde__, P.sdl ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_39})

V_77 = Vertex(name = 'V_77',
              particles = [ P.a, P.Z, P.sdl__tilde__, P.sdl ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_43})

V_78 = Vertex(name = 'V_78',
              particles = [ P.Z, P.sdr__tilde__, P.sdr ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_40})

V_79 = Vertex(name = 'V_79',
              particles = [ P.a, P.Z, P.sdr__tilde__, P.sdr ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_44})

V_80 = Vertex(name = 'V_80',
              particles = [ P.Z, P.ssl__tilde__, P.ssl ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_39})

V_81 = Vertex(name = 'V_81',
              particles = [ P.a, P.Z, P.ssl__tilde__, P.ssl ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_43})

V_82 = Vertex(name = 'V_82',
              particles = [ P.Z, P.ssr__tilde__, P.ssr ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_40})

V_83 = Vertex(name = 'V_83',
              particles = [ P.a, P.Z, P.ssr__tilde__, P.ssr ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_44})

V_84 = Vertex(name = 'V_84',
              particles = [ P.Z, P.sul__tilde__, P.sul ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_39})

V_85 = Vertex(name = 'V_85',
              particles = [ P.a, P.Z, P.sul__tilde__, P.sul ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_43})

V_86 = Vertex(name = 'V_86',
              particles = [ P.Z, P.sur__tilde__, P.sur ],
              color = [ 'Identity(2,3)' ],
              lorentz = [ L.VSS1 ],
              couplings = {(0,0):C.GC_42})

V_87 = Vertex(name = 'V_87',
              particles = [ P.a, P.Z, P.sur__tilde__, P.sur ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_45})

V_88 = Vertex(name = 'V_88',
              particles = [ P.g, P.Z, P.sul__tilde__, P.sul ],
              color = [ 'T(1,4,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_46})

V_89 = Vertex(name = 'V_89',
              particles = [ P.g, P.Z, P.sdl__tilde__, P.sdl ],
              color = [ 'T(1,4,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_46})

V_90 = Vertex(name = 'V_90',
              particles = [ P.g, P.Z, P.sur__tilde__, P.sur ],
              color = [ 'T(1,4,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_48})

V_91 = Vertex(name = 'V_91',
              particles = [ P.g, P.Z, P.sdr__tilde__, P.sdr ],
              color = [ 'T(1,4,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_47})

V_92 = Vertex(name = 'V_92',
              particles = [ P.g, P.Z, P.scl__tilde__, P.scl ],
              color = [ 'T(1,4,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_46})

V_93 = Vertex(name = 'V_93',
              particles = [ P.g, P.Z, P.ssl__tilde__, P.ssl ],
              color = [ 'T(1,4,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_46})

V_94 = Vertex(name = 'V_94',
              particles = [ P.g, P.Z, P.scr__tilde__, P.scr ],
              color = [ 'T(1,4,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_48})

V_95 = Vertex(name = 'V_95',
              particles = [ P.g, P.Z, P.ssr__tilde__, P.ssr ],
              color = [ 'T(1,4,3)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_47})

V_96 = Vertex(name = 'V_96',
              particles = [ P.Z, P.Z, P.scl__tilde__, P.scl ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_49})

V_97 = Vertex(name = 'V_97',
              particles = [ P.Z, P.Z, P.scr__tilde__, P.scr ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_51})

V_98 = Vertex(name = 'V_98',
              particles = [ P.Z, P.Z, P.sdl__tilde__, P.sdl ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_49})

V_99 = Vertex(name = 'V_99',
              particles = [ P.Z, P.Z, P.sdr__tilde__, P.sdr ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_50})

V_100 = Vertex(name = 'V_100',
               particles = [ P.Z, P.Z, P.ssl__tilde__, P.ssl ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_49})

V_101 = Vertex(name = 'V_101',
               particles = [ P.Z, P.Z, P.ssr__tilde__, P.ssr ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_50})

V_102 = Vertex(name = 'V_102',
               particles = [ P.Z, P.Z, P.sul__tilde__, P.sul ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_49})

V_103 = Vertex(name = 'V_103',
               particles = [ P.Z, P.Z, P.sur__tilde__, P.sur ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.VVSS1 ],
               couplings = {(0,0):C.GC_51})

V_104 = Vertex(name = 'V_104',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_105 = Vertex(name = 'V_105',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_106 = Vertex(name = 'V_106',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2})

V_107 = Vertex(name = 'V_107',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_6})

V_108 = Vertex(name = 'V_108',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_6})

V_109 = Vertex(name = 'V_109',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_6})

V_110 = Vertex(name = 'V_110',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5})

V_111 = Vertex(name = 'V_111',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5})

V_112 = Vertex(name = 'V_112',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5})

V_113 = Vertex(name = 'V_113',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_14})

V_114 = Vertex(name = 'V_114',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_14})

V_115 = Vertex(name = 'V_115',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_14})

V_116 = Vertex(name = 'V_116',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_59})

V_117 = Vertex(name = 'V_117',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_62})

V_118 = Vertex(name = 'V_118',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_57})

V_119 = Vertex(name = 'V_119',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_34,(0,1):C.GC_38})

V_120 = Vertex(name = 'V_120',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_34,(0,1):C.GC_38})

V_121 = Vertex(name = 'V_121',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3 ],
               couplings = {(0,0):C.GC_34,(0,1):C.GC_38})

V_122 = Vertex(name = 'V_122',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_25})

V_123 = Vertex(name = 'V_123',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_28})

V_124 = Vertex(name = 'V_124',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_31})

V_125 = Vertex(name = 'V_125',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_26})

V_126 = Vertex(name = 'V_126',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_29})

V_127 = Vertex(name = 'V_127',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_32})

V_128 = Vertex(name = 'V_128',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_27})

V_129 = Vertex(name = 'V_129',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_30})

V_130 = Vertex(name = 'V_130',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_33})

V_131 = Vertex(name = 'V_131',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_66})

V_132 = Vertex(name = 'V_132',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_69})

V_133 = Vertex(name = 'V_133',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_72})

V_134 = Vertex(name = 'V_134',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_67})

V_135 = Vertex(name = 'V_135',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_70})

V_136 = Vertex(name = 'V_136',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_73})

V_137 = Vertex(name = 'V_137',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_68})

V_138 = Vertex(name = 'V_138',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_71})

V_139 = Vertex(name = 'V_139',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_74})

V_140 = Vertex(name = 'V_140',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_14})

V_141 = Vertex(name = 'V_141',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_14})

V_142 = Vertex(name = 'V_142',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_14})

V_143 = Vertex(name = 'V_143',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_60})

V_144 = Vertex(name = 'V_144',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_61})

V_145 = Vertex(name = 'V_145',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_64})

V_146 = Vertex(name = 'V_146',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_65})

V_147 = Vertex(name = 'V_147',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_58})

V_148 = Vertex(name = 'V_148',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_63})

V_149 = Vertex(name = 'V_149',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV4 ],
               couplings = {(0,0):C.GC_34,(0,1):C.GC_41})

V_150 = Vertex(name = 'V_150',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV4 ],
               couplings = {(0,0):C.GC_34,(0,1):C.GC_41})

V_151 = Vertex(name = 'V_151',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2, L.FFV4 ],
               couplings = {(0,0):C.GC_34,(0,1):C.GC_41})

V_152 = Vertex(name = 'V_152',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_24})

V_153 = Vertex(name = 'V_153',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_24})

V_154 = Vertex(name = 'V_154',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_24})

V_155 = Vertex(name = 'V_155',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_24})

V_156 = Vertex(name = 'V_156',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_24})

V_157 = Vertex(name = 'V_157',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_24})

V_158 = Vertex(name = 'V_158',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV5 ],
               couplings = {(0,0):C.GC_35,(0,1):C.GC_38})

V_159 = Vertex(name = 'V_159',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV5 ],
               couplings = {(0,0):C.GC_35,(0,1):C.GC_38})

V_160 = Vertex(name = 'V_160',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV5 ],
               couplings = {(0,0):C.GC_35,(0,1):C.GC_38})

V_161 = Vertex(name = 'V_161',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_52})

V_162 = Vertex(name = 'V_162',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_52})

V_163 = Vertex(name = 'V_163',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV2 ],
               couplings = {(0,0):C.GC_52})

