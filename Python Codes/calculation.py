from final_code2 import final_vr1
from final_code2 import final_vs1
from final_code2 import final_vz1
from final_code2 import final_vr2
from final_code2 import final_vs2
from final_code2 import final_vz2
from final_code2 import ref_res
from final_code2 import ref_res2
from Tkinter import *




print "voltage across ref-- %f" %final_vr1
print "voltage across unknown-- %f" %final_vz1
print "voltage across source-- %f" %final_vs1
print "voltage across ref for other frequency-- %f" %final_vr2
print "voltage across unknown for other frequency-- %f" %final_vz2
print "voltage across source for other frequency-- %f" %final_vs2
print ref_res
print ref_res2 # 0 for 10k ohm  1 for 1megaohm 2 for 100 ohm


if abs(final_vz1-final_vz2) <=0.1 and abs(final_vr1-final_vr2)<=0.1:
    print "Its a resistor"
    var=0
    if ref_res==0:
        ans_r=(final_vz1/final_vr1)*10000
        print ans_r
    elif ref_res==1:
        ans_r=(final_vz1/final_vr1)*1000000
        print ans_r
    elif ref_res==2:
        ans_r=(final_vz1/final_vr1)*100
        print ans_r
    elif ref_res==3:
        ans_r=(final_vz1/final_vr1)*100000
        print ans_r
    elif ref_res==4:
        ans_r=(final_vz1/final_vr1)*1000
        print ans_r

elif (final_vz1)>(final_vz2):
    var=1
    print "impedance for frequency of 10000hz"
    if ref_res==0:
        ans_l=(final_vz1/final_vr1)*10000
        print ans_l
    elif ref_res==1:
        ans_l=(final_vz1/final_vr1)*1000000
        print ans_l
    elif ref_res==2:
        ans_l=(final_vz1/final_vr1)*100
        print ans_l
    elif ref_res==3:
        ans_l=(final_vz1/final_vr1)*100000
        print ans_l
    elif ref_res==4:
        ans_l=(final_vz1/final_vr1)*1000
        print ans_l
    print "impedance for frequency of 5000hz"
    if ref_res2==0:
        ans_L=(final_vz2/final_vr2)*10000
        print ans_L
    elif ref_res2==1:
        ans_L=(final_vz2/final_vr2)*1000000
        print ans_L
    elif ref_res2==2:
        ans_L=(final_vz2/final_vr2)*100
        print ans_L
    elif ref_res2==3:
        ans_L=(final_vz2/final_vr2)*100000
        print ans_L
    elif ref_res2==4:
        ans_L=(final_vz2/final_vr2)*1000
        print ans_L
    ind=(ans_L/(5000.0*6.28))*1000
    print "it has a inductance of %f mH" %ind

elif (final_vz1)<(final_vz2):
    var=2
    print "impedance for frequency of 10000hz"
    if ref_res==0:
        ans_c=(final_vz1/final_vr1)*10000
        print ans_c
    elif ref_res==1:
        ans_c=(final_vz1/final_vr1)*1000000
        print ans_c
    elif ref_res==2:
        ans_c=(final_vz1/final_vr1)*100
        print ans_c
    elif ref_res==3:
        ans_c=(final_vz1/final_vr1)*100000
        print ans_c
    elif ref_res==4:
        ans_c=(final_vz1/final_vr1)*1000
        print ans_c
    print "impedance for frequency of 5000hz"
    if ref_res2==0:
        ans_C=(final_vz2/final_vr2)*10000
        print ans_C
    elif ref_res2==1:
        ans_C=(final_vz2/final_vr2)*1000000
        print ans_C
    elif ref_res2==2:
        ans_C=(final_vz2/final_vr2)*100
        print ans_C
    elif ref_res2==3:
        ans_C=(final_vz2/final_vr2)*100000
        print ans_C
    elif ref_res2==4:
        ans_C=(final_vz2/final_vr2)*1000
        print ans_C
    cap=(1/(ans_C*5000.0*6.28))*1000000000
    print "it has a capacitance of %f nF" %cap

if var==0:
    root = Tk()
    value="resistance of "+str(ans_r)+" ohms"
    s="hey"
    var1 = StringVar()
    var2=StringVar()
    #photo=PhotoImage(file="resistor.jpg")
    label = Label( root, textvariable=var1, bd=6,height=10,width=50,fg="red", font=10,background="black" )
    l = Label( root, textvariable=var2, bd=6,height=10,width=50,fg="red", font=10,background="black" )
    var1.set(value)
    var2.set(s)
    label.pack()
    l.pack()
    root.mainloop()
if var==1:
    root = Tk()
    value="inductance of "+str(ind)+" mH"
    value_1="impedance at 5000 hz is "+str(ans_L)
    value_2="impedance at 10000 hz is "+str(ans_l)
    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    #photo=PhotoImage(file="resistor.jpg")
    label1 = Label( root, textvariable=var1, bd=6,height=10,width=50,fg="red",font=10,background="black" )
    label2 = Label( root, textvariable=var2, bd=6,height=10,width=50,fg="red",font=10,background="black" )
    label3 = Label( root, textvariable=var3, bd=6,height=10,width=50,fg="red",font=10,background="black" )
    var1.set(value)
    var2.set(value_1)
    var3.set(value_2)
    label1.pack()
    label2.pack()
    label3.pack()
    root.mainloop()
if var==2:
    root = Tk()
    value="capacitance of "+str(cap)+" nF"
    value_1="impedance at 5000 hz is "+str(ans_C)
    value_2="impedance at 10000 hz is "+str(ans_c)
    var1 = StringVar()
    var2 = StringVar()
    var3 = StringVar()
    #photo=PhotoImage(file="resistor.jpg")
    label1 = Label( root, textvariable=var1, bd=6,height=10,width=50,fg="red",font=10,background="black" )
    label2 = Label( root, textvariable=var2, bd=6,height=10,width=50,fg="red",font=10,background="black" )
    label3 = Label( root, textvariable=var3, bd=6,height=10,width=50,fg="red",font=10,background="black" )
    var1.set(value)
    var2.set(value_1)
    var3.set(value_2)
    label1.pack()
    label2.pack()
    label3.pack()
    root.mainloop()





