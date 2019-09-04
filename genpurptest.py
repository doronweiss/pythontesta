data = ["Id  ", "HoleNum  ", "NozzleType  ", "x  ", "y  ", "ATPGroup  ", "InsertionDT  "]
data.extend(["InsertionForce  ", "InsertionForcePass  ", "P1SResult  ", "P2SResult  ", "P2Pass  "])
data.extend(["P2TestDT  ", "P4Result  ", "P4SResult  ", "P4Pass ", "P4TestDT  ", "Faulted  ", "ErrorReason  "])
data.extend(["IsLong  ", "actualX  ", "actualY  ", "TraySN  ", "TrayPosition  ", "forceFailsQty  "])
data.extend(["batchNum  ", "trayRerunNum  ", "M1P1Result  ", "M1P2Result  ", "M1NozzleAddressInTray  "])
data.extend(["insertionTemperature  ", "P3Result  ", "P3SResult  ", "P3Pass  ", "P3TestDT  "])
data.extend(["pressureFailsQty  ", "pressureFailsQty4  ", "pressureFailsQty3  ", "PlatesId  "])

for str in data:
    print ('<GridViewColumn Header="{0}" DisplayMemberBinding="{{Binding Path = {0} }}" />'.format(str.strip()))