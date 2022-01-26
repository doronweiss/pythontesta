import re

data = """string state
int firstFeederPercent
int firstFeederCartridgeReplacementNeeded
string firstFeederMaterial
bool firstCartridgeReplacmentRequired
int secondFeederPercent
int secondFeederCartridgeReplacementNeeded
string secondFeederMaterial
bool secondCartridgeReplacmentRequired
int thirdFeederPercent
int thirdFeederCartridgeReplacementNeeded
string thirdFeederMaterial
bool thirdCartridgeReplacmentRequired
int firstOvenUpper
int firstOvenLower
int secondOvenUpper
int secondOvenLower
int thirdOvenUpper
int thirdOvenLower
bool firstDrawerReadyBurgerWaiting
int firstDrawerTimeToReadyBurger
bool secondDrawerReadyBurgerWaiting
int secondDrawerTimeToReadyBurger
bool thirdDrawerReadyBurgerWaiting
int thirdDrawerTimeToReadyBurger
bool cleaningRequired
bool productionRequired
string _id
bool cartridgeReplacmentRequired
string serialNumber"""

if __name__ == "__main__":
    rx = "SW\.+[0-9]+"
    lines = data.split('\n')
    for line in lines:
        parts = [ln for ln in line.split(' ') if len(ln) > 0]
        varType = parts[0]
        varName = parts[1]
        print('if ({0} != prevMD.{0}){{  // {0}'.format(varName))
        print('prevMD.{0} = {0};'.format(varName))
        if varType=='int' or varType=='bool':
            print('((IDictionary<string, object>)obj2Send).Add("{0}", {0});'.format(varName))
        elif varType=='string':
            print('((IDictionary<string, object>)obj2Send).Add("{0}", "{0}");'.format(varName))
        elif varType=='bool':
            print('((IDictionary<string, object>)obj2Send).Add("{0}", "{0}");'.format(varName))
        print('}')
