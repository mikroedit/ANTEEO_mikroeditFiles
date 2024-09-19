from orderData import Data
from orderDef import orderFunctions

orderFunctions.sendLinkVideo(Data)

file_size = orderFunctions.checkImage(Data)
if file_size < 2 * 1024 * 1024:
    orderFunctions.sendImageBaseLinker(Data)
else:
    orderFunctions.sendImageGoogleDrive(Data)