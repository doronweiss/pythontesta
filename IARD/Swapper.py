data="""
        model.detection_confidence = DataStore.selectedCam.algoParams.detection_confidence;
        model.horizon_confidence = DataStore.selectedCam.algoParams.horizon_confidence;
        model.horizon_source = DataStore.selectedCam.algoParams.horizon_source;
        model.full_picture = DataStore.selectedCam.algoParams.full_picture;
        model.skylines_pixels = DataStore.selectedCam.algoParams.skylines_pixels;
        model.sealines_pixels = DataStore.selectedCam.algoParams.sealines_pixels;
        model.auto_tiles = DataStore.selectedCam.algoParams.auto_tiles;
        model.tiles_offset_x = DataStore.selectedCam.algoParams.tiles_offset_x;
        model.tiles_offset_y = DataStore.selectedCam.algoParams.tiles_offset_y;
        model.use_tracker = DataStore.selectedCam.algoParams.use_tracker;
        model.track2drop = DataStore.selectedCam.algoParams.track2drop;
        model.possible2drop = DataStore.selectedCam.algoParams.possible2drop;
        model.possible2track = DataStore.selectedCam.algoParams.possible2track;
        model.possible2track_history = DataStore.selectedCam.algoParams.possible2track_history;
        model.centroid_shift_x = DataStore.selectedCam.algoParams.centroid_shift_x;
        model.centroid_shift_y = DataStore.selectedCam.algoParams.centroid_shift_y;
        model.bb_width_ratio = DataStore.selectedCam.algoParams.bb_width_ratio;
        model.bb_height_ratio = DataStore.selectedCam.algoParams.bb_height_ratio;
"""

def getrelevant(alist):
    parts = list(map(str.strip, alist))
    parts = [x for x in parts if len(x) > 0]
    return parts

lines = [ln for ln in data.split('\n') if len(ln)>0]
print ("Len={0}".format(len(lines)))
for line in lines:
    line = line.replace(';','')
    parts = line.split('=')
    print ("{1} = {0};".format(parts[0].strip(), parts[1].strip()))
