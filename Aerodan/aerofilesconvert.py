data="""
Cl_body_tab.mat
Cl_dp_inc_tab.mat
Cl_dr_inc_tab.mat
Cl_dy_inc_tab.mat
Cm_body_tab.mat
Cm_dp_inc_tab.mat
Cm_dr_inc_tab.mat
Cm_dy_inc_tab.mat
Cn_body_tab.mat
Cn_dp_inc_tab.mat
Cn_dr_inc_tab.mat
Cn_dy_inc_tab.mat
Cxfore_body_tab.mat
Cxfore_dp_inc_tab.mat
Cxfore_dr_inc_tab.mat
Cxfore_dy_inc_tab.mat
Cxoff_body_tab.mat
Cxoff_dp_inc_tab.mat
Cxoff_dr_inc_tab.mat
Cxoff_dy_inc_tab.mat
Cy_body_tab.mat
Cy_dp_inc_tab.mat
Cy_dr_inc_tab.mat
Cy_dy_inc_tab.mat
Cz_body_tab.mat
Cz_dp_inc_tab.mat
Cz_dr_inc_tab.mat
Cz_dy_inc_tab.mat
"""

def getrelevant(alist):
    parts = list(map(str.strip, alist))
    parts = [x for x in parts if len(x) > 0]
    return parts
print ("clear all")
lines = [ln for ln in data.split('\n') if len(ln)>0]
for line in lines:
    parts=line.split('.')
    varname = parts[0].strip()
    print ("load('{0}');".format(line.strip()))
    print ("writematrix({0},['{0}' '.txt'],'Delimiter','space');".format(varname))
    print ("clear {0};".format(varname))
