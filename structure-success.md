# Yat4tango:

Before:

2021-07-26T16:49:02.185140+0200 | DEBUG | AF788B70 | flyscan/core/server.1 | NEXUSCPP_ERROR. Unsupported HDF5 datatype. nexusData2h5Data

After:

{"@timestamp":"2021-08-02T14:11:38.042Z","host":{"name":"localhost.localdomain"},"log":{"offset":0,"file":{"path":"/vagrant/assembly/ds_RecordingManager/yat4tango/ds_FlyScanServer/flyscan.1/flyscan_core_server.1.20210802141654/flyscan_core_server.1.log.202108021416"}},"ecs":{"version":"1.10.0"},"level":"ERROR","beamline":"flyscan","agent":{"name":"localhost.localdomain","type":"filebeat","ephemeral_id":"a1ad8dcd-87a5-4f06-98ac-e753a145cb34","version":"7.14.0","hostname":"localhost.localdomain","id":"5f61175d-e407-49d3-b9a3-3efa77d25554"},"thread_id":"7DACBB70","timestamp_nanos":"2021-08-02T16:11:38.042822+0200","@version":"1","device":{"domain":"flyscan","name":"flyscan/core/server.1","family":"core","process":"ds_FlyScanServer","instance":"flyscan.1","member":"server.1"},"message":"NEXUSCPP_ERROR. Unsupported HDF5 datatype. nexusData2h5Data"}

# Spyc:

Before:

#Sat, 20 Mar 2021 09:38:59
shopen
#[INFO: spyc.printer]# Opening ALL authorized shutters.
#[INFO: spyc.printer]# Device is ready.
#[INFO: spyc.printer]# 
#[INFO: spyc.printer]# ------ Devices state ------
#[INFO: spyc.printer]# #0: tdl-i06-m/vi/tdl.1: OPEN
#[INFO: spyc.printer]# #1: i06-m-c06/ex/obx.1: OPEN
#[INFO: spyc.printer]#

After:

{"agent":{"name":"localhost.localdomain","type":"filebeat","ephemeral_id":"a1ad8dcd-87a5-4f06-98ac-e753a145cb34","version":"7.14.0","hostname":"localhost.localdomain","id":"5f61175d-e407-49d3-b9a3-3efa77d25554"},"@timestamp":"2021-03-09T10:23:07.000Z","host":{"name":"localhost.localdomain"},"spyc":{"level":"INFO","command":"microstep 0.01","message":"#[INFO: spyc.printer]# start positions:\n#[INFO: spyc.printer]# \tmicros: 0.3656 mm [Not specified, Not specified]\n#[INFO: spyc.printer]# \tmicrox: -0.3657 mm [Not specified, Not specified]\n#[INFO: spyc.core.Macro.MoveCmd]# micros: 0.3727 STANDBY microx: -0.3727 STANDBY"},"log":{"offset":69841,"flags":["multiline"],"file":{"path":"/vagrant/assembly/ds_RecordingManager/spyc/all_210309T102924.log"}},"ecs":{"version":"1.10.0"},"@version":"1","input":{"type":"log"},"tags":["spyc","beats_input_codec_plain_applied"]}

# Passerelle:

Before:

10 Nov 2019 14:00:18:657 [Eiger_ptycho3D_Nov2019_v2:ConfigSpiral.XDistanceToCenterCalculation] - calculating abs(x1-x2) where x1=-0.3465 x2=-0.341971241062 
	
After:

{"passerelle":{"actor":"Eiger_ptycho3D_Nov2019_v2","source":"ConfigSpiral.StringsAdder"},"agent":{"name":"localhost.localdomain","type":"filebeat","ephemeral_id":"a1ad8dcd-87a5-4f06-98ac-e753a145cb34","version":"7.14.0","hostname":"localhost.localdomain","id":"5f61175d-e407-49d3-b9a3-3efa77d25554"},"@timestamp":"2019-11-10T11:39:01.729Z","host":{"name":"localhost.localdomain"},"log":{"offset":329555,"file":{"path":"/vagrant/assembly/ds_RecordingManager/passerelle/execution-trace.log.4"}},"ecs":{"version":"1.10.0"},"@version":"1","input":{"type":"log"},"message":"calculating abs(x1-x2) where x1=-0.3465 x2=-0.341971241062 "]}


# Javagui:

Before:

15:42:58.728 ERROR AttributesValuesRefreshingThread(storage/configuration/technicaldata.1)(1s)-DataConnectionManagement.logError:452 - Device 'storage/configuration/technicaldata.1' seems to be down
Cannot Re-import storage/configuration/technicaldata.1 :
fr.esrf.TangoApi.CommunicationFailed: IDL:Tango/DevFailed:1.0
	at fr.esrf.TangoDs.Except.throw_communication_failed(Except.java:708)
	at fr.esrf.TangoDs.Except.throw_communication_failed(Except.java:646)
	
After:

{"javagui":{"tasknumber":"768","threadname":"Thread-1096-f.s.m.s.CurrentScanDataModel.updateNexusInfo","beamline":"Salsa","level":"WARN","message":"Attribute d03-1-c00/ex/scan.1/generatedNexusFileName has an empty value! (try nb 12)"},"agent":{"name":"localhost.localdomain","type":"filebeat","ephemeral_id":"a1ad8dcd-87a5-4f06-98ac-e753a145cb34","version":"7.14.0","hostname":"localhost.localdomain","id":"5f61175d-e407-49d3-b9a3-3efa77d25554"},"@timestamp":"2021-03-26T20:49:06.583Z","host":{"name":"localhost.localdomain"},"log":{"offset":14323,"file":{"path":"/vagrant/assembly/ds_RecordingManager/javagui/salsa-mars-PROBLEM-1820/Salsa-20210326T214703.log"}},"ecs":{"version":"1.10.0"},"@version":"1","input":{"type":"log"},"tags":["javagui","beats_input_codec_plain_applied"]}

# Javadevices:

Before:

INFO  2018-04-30 13:54:49,534 archiving/hdbarchivingwatcher/Watch-CIG-MON - main | f.s.t.s.w.HDBTDBArchivingWatcher.initDevice:1214 - start init


After:

{"javagui":{"tasknumber":"160","threadname":"main-fr.soleil.salsa.dao.impl.CommonsJDBC.doConnection","beamline":"Salsa","level":"INFO","message":"Connected to jdbc:mysql://srv1/salsa"},"agent":{"name":"localhost.localdomain","type":"filebeat","ephemeral_id":"a1ad8dcd-87a5-4f06-98ac-e753a145cb34","version":"7.14.0","hostname":"localhost.localdomain","id":"5f61175d-e407-49d3-b9a3-3efa77d25554"},"@timestamp":"2021-03-16T11:30:00.442Z","host":{"name":"localhost.localdomain"},"log":{"offset":0,"file":{"path":"/vagrant/assembly/ds_RecordingManager/javagui/salsa-mars-PROBLEM-1820/Salsa-20210316T122950.log"}},"ecs":{"version":"1.10.0"},"@version":"1","input":{"type":"log"},"tags":["javagui","beats_input_codec_plain_applied"]}

# Backtrace:
	
Before:

DServer: ds_CompactPCICrate/srv7
Started: 2021-05-07T15:10:30
Aborted: 2021-08-05T16:05:19
Host   : srv7.sirius.rcl
Reason : process aborted
Why    : n/a

Thread 1 (Thread 0xb64c1b70 (LWP 1031)):
Crashed thread
#0  0xb77ff420 in __kernel_vsyscall ()
No symbol table info available.
#1  0xb65527c1 in raise () from /lib/libc.so.6

After:
	
{"log":{"offset":0,"file":{"path":"/vagrant/assembly/ds_RecordingManager/dumps/dumps.log"},"flags":["multiline"]},"tags":["logdumps","beats_input_codec_plain_applied"],"agent":{"name":"localhost.localdomain","ephemeral_id":"19a695ea-acbe-4bda-ba77-fe6a4450e9f3","version":"7.14.0","hostname":"localhost.localdomain","type":"filebeat","id":"5f61175d-e407-49d3-b9a3-3efa77d25554"},"input":{"type":"log"},"host":{"name":"localhost.localdomain"},"logdumps":{"message":"\nThread 1 (Thread 0xb64c1b70 (LWP 1031)):\nCrashed thread\n#0  0xb77ff420 in __kernel_vsyscall ()\nNo symbol table info available.","Started":"Started","host":"Host   : srv7.sirius.rcl","server":"DServer: ds_CompactPCICrate/srv7","Aborted":"Aborted","reason":"Reason : process aborted","why":"Why    : n/a","abortdate":"2021-08-05T16:05:19"},"@version":"1","ecs":{"version":"1.10.0"},"@timestamp":"2021-08-05T16:05:19.000Z",:[{"device”:{”instance”:”DServer: ds_CompactPCICrate/srv7”}}, {“process”:{”start”:”2021-05-07T15:10:30”, “end”: “2021-08-05T16:05:19”}}, {”host”:{”hostname”   : “srv7.sirius.rcl”}}
{“error":{”code":”Reason : process aborted”, “message”:”Why :n/a”, “stack-trace”:”Thread 1 (Thread 0xb64c1b70 (LWP 1031)):\nCrashed thread\n#0  0xb77ff420 in __kernel_vsyscall”}}

# Cppdevices:
	
Before:

<log4j:event logger="flyscan/core/data-merger.1" timestamp="1616322327325" level="INFO" thread="2557475696">
<log4j:message><![CDATA[Processing buffer file /nfs/srv5/spool1/flyscan_in/falcon1x_001251.nxs...]]></log4j:message>
<log4j:NDC><![CDATA[]]></log4j:NDC>
</log4j:event>

After:

{"ndc":{},"thread":"3892","event":{},"@timestamp":"2021-01-07T16:17:08.991Z","host":{"name":"localhost.localdomain"},"log":{"offset":0,"flags":["multiline"],"file":{"path":"/vagrant/assembly/ds_RecordingManager/cppdevices/cpplogs-20210327-06h46/i06-m-c00_ca_bai.1587-pci.1h-sai.3.log"}},"ecs":{"version":"1.10.0"},"input":{"type":"log"},"tags":["cppdevices","beats_input_codec_plain_applied"],"level":"INFO","agent":{"name":"localhost.localdomain","type":"filebeat","ephemeral_id":"a1ad8dcd-87a5-4f06-98ac-e753a145cb34","version":"7.14.0","hostname":"localhost.localdomain","id":"5f61175d-e407-49d3-b9a3-3efa77d25554"},"@version":"1","device":{"domain":"i06-m-c00","name":"i06-m-c00/ca/bai.1587-pci.1h-sai.3","family":"ca","member":"bai.1587-pci.1h-sai.3"},"message":"AIController::AIController() create device I06-M-C00/CA/BAI.1587-PCI.1H-SAI.3"}

# Cooxdaemon:
	
Before:

17/01/19 14:40:41.961 - [INFO] :Service Database - Replication - Url blacklist updated: []

After:

{"agent":{"name":"localhost.localdomain","type":"filebeat","ephemeral_id":"a1ad8dcd-87a5-4f06-98ac-e753a145cb34","version":"7.14.0","hostname":"localhost.localdomain","id":"5f61175d-e407-49d3-b9a3-3efa77d25554"},"@timestamp":"2019-01-17T14:40:41.961Z","host":{"name":"localhost.localdomain"},"cooxdaemon":{"timestamp":"8/27/19 15:42:24.832","level":"INFO","message":"Service Database - Replication - Url blacklist updated: []"},"log":{"offset":2736,"file":{"path":"/vagrant/assembly/ds_RecordingManager/coox/mars/CooxDaemon/replication0.log"}},"ecs":{"version":"1.10.0"},"@version":"1","input":{"type":"log"},"tags":["cooxdaemon","beats_input_codec_plain_applied"]}

# Cooxviewer:

Before:

5/11/21 17:22:54.265 - [INFO] : Connection error: StringButton With:d03-1-cx0/dt/diode.fly_insert/insert

After:

{"agent":{"name":"localhost.localdomain","type":"filebeat","ephemeral_id":"a1ad8dcd-87a5-4f06-98ac-e753a145cb34","version":"7.14.0","hostname":"localhost.localdomain","id":"5f61175d-e407-49d3-b9a3-3efa77d25554"},"@timestamp":"2021-11-05T17:22:54.265Z","host":{"name":"localhost.localdomain"},"log":{"offset":5236,"file":{"path":"/vagrant/assembly/ds_RecordingManager/coox/mars/CooxViewer/Soleil_CooxViewer.2020-12-26_09.log"}},"ecs":{"version":"1.10.0"},"@version":"1","input":{"type":"log"},"tags":["cooxviewer","beats_input_codec_plain_applied"],"cooxviewer":{"threadnumber":"140","threadname":"DataSourceReconnectionManager ConnectionThread-DataConnectionManagement.log","level":"INFO","message":"Connection error: StringButton With:d03-1-cx0/dt/diode.fly_insert/insert"}}
