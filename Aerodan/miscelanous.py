data="""
Cl_dp_inc_tab
Cl_dr_inc_tab
Cl_dy_inc_tab
Cm_dp_inc_tab
Cm_dr_inc_tab
Cm_dy_inc_tab
Cn_dp_inc_tab
Cn_dr_inc_tab
Cn_dy_inc_tab
Cxfore_dp_inc_tab
Cxfore_dr_inc_tab
Cxfore_dy_inc_tab
Cxoff_dp_inc_tab
Cxoff_dr_inc_tab
Cxoff_dy_inc_tab
Cy_dp_inc_tab
Cy_dr_inc_tab
Cy_dy_inc_tab
Cz_dp_inc_tab
Cz_dr_inc_tab
Cz_dy_inc_tab
"""

lines = [ln for ln in data.split('\n') if len(ln)>0]
print ("Len={0}".format(len(lines)))
for line in lines:
    line = line.strip()
    print ("if (!LoadIncData({0}, \"aerodata/{0}.txt\"))".format(line))
    print ("return false;")
