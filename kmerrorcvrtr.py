errorIDs = """
    #define KM_ID_OK    					0x0000 // OK
    #define KM_ID_BAD_CRC					0x0001 // ERROR_CRC
    #define KM_ID_TIME_OUT					0x0002 // ERROR_TIMEOUT
    #define KM_ID_BAD_DEVICE_ID				0x0003 // ERROR_INVALID_PARAMETER
    #define KM_ID_DEVICE_NOT_INSTALLED		0x0004 // ERROR_PRODUCT_UNINSTALLED
    #define KM_ID_LOCK_FAILED				0x0005 // ERROR_EXCL_SEM_ALREADY_OWNED
    #define KM_ID_NO_DATA					0x0006 // ERROR_INVALID_DATA
    #define KM_ID_BUFFER_TOO_SMALL			0x0007 // ERROR_INSUFFICIENT_BUFFER
    #define KM_ID_FAIL_SEND_MSG				0x0009
    #define KM_ID_FAIL_ACK_NAK				0x000A
    #define KM_ID_FAIL_ACCEPT				0x000B
    #define KM_ID_FAIL_PROTOCOL				0x000C
    #define KM_ID_FAIL_RESPOND				0x000D
    #define KM_ID_UNKNOWN_MESSAGE			0x000E
    #define KM_ID_MEM_LOCK					0x000F
    #define KM_ID_FAIL_CREATE_FILE			0x0010
    #define KM_ID_FAIL_OPEN_FILE			0x0011
    #define KM_ID_FAIL_FIND_FILE			0x0012 // ERROR_FILE_NOT_FOUND
    #define KM_ID_UNEXPECTED_EOF			0x0013
    #define KM_ID_NO_CONTEXT				0x0014
    #define KM_ID_MEM_ALLOC					0x0015
    #define KM_ID_INVALID_PRODUCT			0x0016
    #define KM_ID_SYSTEM					0x0017
    #define KM_ID_FAIL_FIND_NAME			0x0018
    #define KM_ID_INVALID_TYPE				0x0019
    #define KM_ID_NO_DEFAULT				0x001A
    #define KM_ID_NO_MAX_MIN				0x001B
    #define KM_ID_BAD_IRQ_NUMBER        	0x001C
    #define KM_ID_INVALID_FORMAT        	0x001D
    #define KM_ID_NOT_IMPLEMENTED       	0x001E
    #define KM_ID_FAIL_FIND_MSG				0x001F
    #define KM_ID_NOT_DEVICE				0x0020
    #define KM_ID_FAILED_OPEN_DEVICE		0x0021
    #define KM_ID_INVALID_VALUE				0x0022
    #define KM_ID_INVALID_DEVICE_CONTEXT	0x0023
    #define KM_ID_GROUP_MAX_EXCEEDED		0x0024
    #define KM_ID_AXIS_ALREADY_IN_GROUP		0x0025
    #define KM_ID_FAIL_FIND_DEVICE			0x0026
    #define KM_ID_DEVICE					0x0027
    #define KM_ID_FAIL_WRITE_FILE			0x0028
    #define KM_ID_FAIL_READ_FILE			0x0029
    #define KM_ID_CONFIG_ALREADY_EXISTS     0x002A
    #define KM_ID_DEVICE_ALREADY_EXISTS     0x002B
    #define KM_ID_WINDOWS_API				0x002C
    #define KM_ID_VARIABLE_NOT_FOUND		0x002D
    #define KM_ID_SERIAL_FRAMING			0x002E
    #define KM_ID_FAILED_CLOSE_DEVICE		0x002F
    #define KM_ID_FAIL_PRODUCT_DLL			0x0030
    #define KM_ID_NO_CONTROLLER				0x0031
    #define KM_ID_FAIL_RETRIEVE_SIZE        0x0032//#define KM_ID_TCP_ERROR_CONNECT_SINK	0x0032
    #define KM_ID_TCP_ERROR_CONNECT_SINK	0x0037
    #define KM_ID_TCP_NO_ALLOC_INTERFACE    0x0033
    #define KM_ID_TCP_INVALID_INTERFACE_POINTER  0x0034
    #define KM_ID_TCP_INVALID_SINK_INTERFACE     0x0035
    #define KM_ID_TCP_NOT_REGISTERED		0x0036
    #define KM_ID_TCP_IP_NOT_FOUND      	0x0038
    #define KM_ID_SYNTAX_ERROR				0x0100
    #define KM_ID_BAD						0xFFFF"""

errorCodes = """
    #define KM_ERR_OK 						MAKE_ERR(PROD_API,KM_ID_OK)
    #define KM_ERR_BAD 						MAKE_ERR(PROD_API,KM_ID_BAD)
    #define KM_ERR_BAD_CRC              	MAKE_ERR(PROD_API,KM_ID_BAD_CRC)
    #define KM_ERR_TIME_OUT					MAKE_ERR(PROD_API,KM_ID_TIME_OUT)
    #define KM_ERR_BAD_DEVICE_ID			MAKE_ERR(PROD_API,KM_ID_BAD_DEVICE_ID)
    #define KM_ERR_DEVICE_NOT_INSTALLED 	MAKE_ERR(PROD_API,KM_ID_DEVICE_NOT_INSTALLED)
    #define KM_ERR_LOCK_FAILED				MAKE_ERR(PROD_API,KM_ID_LOCK_FAILED)
    #define KM_ERR_NO_DATA					MAKE_ERR(PROD_API,KM_ID_NO_DATA)
    #define KM_ERR_BUFFER_TOO_SMALL			MAKE_ERR(PROD_API,KM_ID_BUFFER_TOO_SMALL)
    #define KM_ERR_FAIL_SEND_MSG			MAKE_ERR(PROD_API,KM_ID_FAIL_SEND_MSG)
    #define KM_ERR_FAIL_ACK_NAK				MAKE_ERR(PROD_API,KM_ID_FAIL_ACK_NAK)
    #define KM_ERR_FAIL_ACCEPT				MAKE_ERR(PROD_API,KM_ID_FAIL_ACCEPT)
    #define KM_ERR_FAIL_PROTOCOL			MAKE_ERR(PROD_API,KM_ID_FAIL_PROTOCOL)
    #define KM_ERR_FAIL_RESPOND				MAKE_ERR(PROD_API,KM_ID_FAIL_RESPOND)
    #define KM_ERR_UNKNOWN_MESSAGE			MAKE_ERR(PROD_API,KM_ID_UNKNOWN_MESSAGE)
    #define KM_ERR_MEM_LOCK					MAKE_ERR(PROD_API,KM_ID_MEM_LOCK)
    #define KM_ERR_FAIL_CREATE_FILE			MAKE_ERR(PROD_API,KM_ID_FAIL_CREATE_FILE)
    #define KM_ERR_FAIL_OPEN_FILE			MAKE_ERR(PROD_API,KM_ID_FAIL_OPEN_FILE)
    #define KM_ERR_FAIL_FIND_FILE			MAKE_ERR(PROD_API,KM_ID_FAIL_FIND_FILE)
    #define KM_ERR_UNEXPECTED_EOF			MAKE_ERR(PROD_API,KM_ID_UNEXPECTED_EOF)
    #define KM_ERR_NO_CONTEXT				MAKE_ERR(PROD_API,KM_ID_NO_CONTEXT)
    #define KM_ERR_MEM_ALLOC				MAKE_ERR(PROD_API,KM_ID_MEM_ALLOC)
    #define KM_ERR_INVALID_PRODUCT			MAKE_ERR(PROD_API,KM_ID_INVALID_PRODUCT)
    #define KM_ERR_SYSTEM					MAKE_ERR(PROD_API,KM_ID_SYSTEM)
    #define KM_ERR_FAIL_FIND_NAME			MAKE_ERR(PROD_API,KM_ID_FAIL_FIND_NAME)
    #define KM_ERR_INVALID_TYPE				MAKE_ERR(PROD_API,KM_ID_INVALID_TYPE)
    #define KM_ERR_NO_DEFAULT				MAKE_ERR(PROD_API,KM_ID_NO_DEFAULT)
    #define KM_ERR_NO_MAX_MIN				MAKE_ERR(PROD_API,KM_ID_NO_MAX_MIN)
    #define KM_ERR_BAD_IRQ_NUMBER			MAKE_ERR(PROD_API,KM_ID_BAD_IRQ_NUMBER)
    #define KM_ERR_INVALID_FORMAT			MAKE_ERR(PROD_API,KM_ID_INVALID_FORMAT)
    #define KM_ERR_NOT_IMPLEMENTED			MAKE_ERR(PROD_API,KM_ID_NOT_IMPLEMENTED)
    #define KM_ERR_FAIL_FIND_MSG			MAKE_ERR(PROD_API,KM_ID_FAIL_FIND_MSG)
    #define KM_ERR_NOT_DEVICE				MAKE_ERR(PROD_API,KM_ID_NOT_DEVICE)
    #define KM_ERR_FAILED_OPEN_DEVICE		MAKE_ERR(PROD_API,KM_ID_FAILED_OPEN_DEVICE)
    #define KM_ERR_INVALID_VALUE			MAKE_ERR(PROD_API,KM_ID_INVALID_VALUE)
    #define KM_ERR_INVALID_DEVICE_CONTEXT	MAKE_ERR(PROD_API,KM_ID_INVALID_DEVICE_CONTEXT)
    #define KM_ERR_GROUP_MAX_EXCEEDED		MAKE_ERR(PROD_API,KM_ID_GROUP_MAX_EXCEEDED)
    #define KM_ERR_AXIS_ALREADY_IN_GROUP	MAKE_ERR(PROD_API,KM_ID_AXIS_ALREADY_IN_GROUP)
    #define KM_ERR_FAIL_FIND_DEVICE			MAKE_ERR(PROD_API,KM_ID_FAIL_FIND_DEVICE)
    #define KM_ERR_FAIL_WRITE_FILE			MAKE_ERR(PROD_API,KM_ID_FAIL_WRITE_FILE)
    #define KM_ERR_FAIL_READ_FILE			MAKE_ERR(PROD_API,KM_ID_FAIL_READ_FILE)
    #define KM_ERR_CONFIG_ALREADY_EXISTS	MAKE_ERR(PROD_API,KM_ID_CONFIG_ALREADY_EXISTS)
    #define KM_ERR_DEVICE_ALREADY_EXISTS	MAKE_ERR(PROD_API,KM_ID_DEVICE_ALREADY_EXISTS)
    #define KM_ERR_WINDOWS_API				MAKE_ERR(PROD_API,KM_ID_WINDOWS_API)
    #define KM_ERR_VARIABLE_NOT_FOUND		MAKE_ERR(PROD_API,KM_ID_VARIABLE_NOT_FOUND)
    #define KM_ERR_SERIAL_FRAMING			MAKE_ERR(PROD_API,KM_ID_SERIAL_FRAMING)
    #define KM_ERR_FAILED_CLOSE_DEVICE		MAKE_ERR(PROD_API,KM_ID_FAILED_CLOSE_DEVICE)
    #define KM_ERR_FAIL_PRODUCT_DLL			MAKE_ERR(PROD_API,KM_ID_FAIL_PRODUCT_DLL)
    #define KM_ERR_NO_CONTROLLER			MAKE_ERR(PROD_API,KM_ID_NO_CONTROLLER)
    #define KM_ERR_CONNECT_SINK				MAKE_ERR(PROD_API,KM_ID_TCP_ERROR_CONNECT_SINK)
    #define KM_ERR_IP_NOT_FOUND				MAKE_ERR(PROD_API,KM_ID_TCP_IP_NOT_FOUND)
    #define KM_ERR_NO_ALLOC_INTERFACE		MAKE_ERR(PROD_API,KM_ID_TCP_NO_ALLOC_INTERFACE)
    #define KM_ERR_INVALID_INTERFACE		MAKE_ERR(PROD_API,KM_ID_TCP_INVALID_INTERFACE_POINTER)
    #define	KM_ERR_INVALID_SINK_INTERFACE   MAKE_ERR(PROD_API,KM_ID_TCP_INVALID_SINK_INTERFACE)
    #define KM_ERR_TCP_NOT_REGISTERED	    MAKE_ERR(PROD_API,KM_ID_TCP_NOT_REGISTERED)
    #define KM_ERR_SYNTAX_ERROR				MAKE_ERR(PROD_API,KM_ID_SYNTAX_ERROR)"""

# dictionary
errIdsDict = {}
# build error codes
def buildErrorCode():
    lines = errorIDs.split('\n')
    for line in lines:
        if (len(line) == 0):
            continue
        idx = line.find("//")
        if (idx > 0):
            line = line[0:idx]
        line = line.replace("#define ", "").replace('\t', ' ').strip()
        parts = [x for x in line.split(' ') if x]
        #print("Parts: {0}/{1}".format(parts[0], parts[1]))
        errIdsDict[parts[0].strip()] = int(parts[1].strip(), 0)
    # for k, v in errIdsDict:
    #     print("Key={0}, Value={1}".format(k, v))

def makeConsts():
    # parse the KM errors
    lines = errorCodes.split('\n')
    for line in lines:
        origline=line
        if (len(line) == 0):
            continue
        idx = line.find("//")
        if (idx > 0):
            line = line[0:idx]
        line = line.replace("#define ", "").replace('MAKE_ERR(PROD_API,',''). replace('\t', ' ').strip().strip(')')
        parts = [x for x in line.split(' ') if x]
        try:
            print ("public const uint {0} = {1};".format(parts[0], errIdsDict[parts[1]]))
        except:
            print ("FORMAT error in line: {0}".format(origline))
            return

if __name__ == "__main__":
    buildErrorCode()
    makeConsts()