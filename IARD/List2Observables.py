data="""
  double detection_confidence
  double horizon_confidence
  string horizon_source
  bool full_picture
  int skylines_pixels
  int sealines_pixels
  bool auto_tiles
  int tiles_offset_x
  int tiles_offset_y
  bool use_tracker
  int track2drop
  int possible2drop
  int possible2track
  int possible2track_history
  double centroid_shift_x
  double centroid_shift_y
  double bb_width_ratio
  double bb_height_ratio

"""

def getrelevant(alist):
    parts = list(map(str.strip, alist))
    parts = [x for x in parts if len(x) > 0]
    return parts

lines = [ln for ln in data.split('\n') if len(ln)>0]
print ("Len={0}".format(len(lines)))
for line in lines:
    parts = line.split(' ')
    parts = getrelevant(parts)  # list(map(str.strip, parts))
    theType = parts[0]
    theName = parts[1]
    print ("private {0} _{1} = default;".format(theType, theName))
    print ("public {0} {1} {{".format(theType, theName.capitalize()))
    print ("  get => _{0} ;".format( theName))
    print ("  set => SetProperty(ref _{0}, value);".format(theName))
    print ("}}")
