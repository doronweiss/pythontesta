"""
// returns the id of a new KMAPI object
extern "C" KMAPI_EXPORT KMApi* KMNewKMAPI();
// free kmpai object
extern "C" KMAPI_EXPORT void MCFreeKMApi( KMApi* pKmapi );

extern "C" KMAPI_EXPORT void MCTest(int a, int b );

extern "C" KMAPI_EXPORT void SetCallback(KMApi* pKmapi, MCCallback * pCallback);
extern "C" KMAPI_EXPORT KMResponse Connect(KMApi* pKmapi, LPCSTR ip, int port);
extern "C" KMAPI_EXPORT KMResponse ExecCommand(KMApi* pKmapi, LPCSTR command, LPSTR response, int rspLength);
extern "C" KMAPI_EXPORT KMResponse SendCommand(KMApi* pKmapi, LPCSTR command);

extern "C" KMAPI_EXPORT KMResponse DownloadFile( KMApi* pKmapi, LPCSTR sFilePath, LPCSTR sFileName );
extern "C" KMAPI_EXPORT KMResponse UploadFile( KMApi* pKmapi, LPCSTR Filename );
extern "C" KMAPI_EXPORT KMResponse GetMCLastError( KMApi* pKmapi,/* out*/ int& errorCode,/* out*/  LPSTR sErrorMessage,/* out*/  int msgLength );

extern "C" KMAPI_EXPORT void SetTimeout( KMApi* pKmapi, KMTimeout type, DWORD timeout );
extern "C" KMAPI_EXPORT KMResponse DetectDevices( KMApi* pKmapi, DWORD Timout );
extern "C" KMAPI_EXPORT MCDevice * GetDeviceList( KMApi* pKmapi);
extern "C" KMAPI_EXPORT KMResponse Authenticate( KMApi* pKmapi, const char * password );
"""

import sys
import ctypes as ct

# from ctypes import *
resp = ct.create_string_buffer(1024)
cmd = ct.create_string_buffer(b"?ver")
l = ct.cdll.LoadLibrary('c:/Workspaces/Python/test1/KMApi.dll')
if l is None:
    sys.exit()
dev = l.KMNewKMAPI()
res = l.Connect (dev, ct.create_string_buffer(b"10.4.20.103"), 4001)
res = l.ExecCommand(dev, cmd, resp, 1024)
print("Response: " + repr(resp.value))
cmd = ct.create_string_buffer(b"?sys.information")
res = l.ExecCommand(dev, cmd, resp, 1024)
print("Response: " + repr(resp.value))
l.MCFreeKMApi(dev)
