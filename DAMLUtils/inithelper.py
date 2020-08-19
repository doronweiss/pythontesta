for i in range(10):
    print ('let pdate = CitizenData {{firstName = "f{0}", lastName="l{0}", address="some address {0}"}}'.format(i))
    print ('x <- submit superuser do')
    print('    createCmd Citizen with')
    print('        id = 566000{0}'.format(i))
    print('        persData = pdate')
    print('        internalAffairsOffice = internalAffairsOffice')
    print('        observers = [wellfareOffice, healthOffice, hlsOffice, borderCtrl]')
