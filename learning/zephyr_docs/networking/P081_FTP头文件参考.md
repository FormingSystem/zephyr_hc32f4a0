---
id: learning.zephyr-docs.networking.api-81
title: FTP头文件参考
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ftp__client_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第81章\_FTP头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ftp__client_8h.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 81.1\_阅读说明与来源

译注：先读[FTP客户端库](P075_FTP客户端库.md)和[客户端示例](P076_FTP客户端示例.md)，再按接口查询本组参考。

本组：[完整API参考](P080_FTP完整API参考.md) · [头文件参考](P081_FTP头文件参考.md) · [头文件源码](P082_FTP头文件源码.md)。

FTP客户端库（FTP Client Library）。

```c
#include <zephyr/kernel.h>
```

```c
#include <zephyr/types.h>
```

```c
#include <zephyr/net/net_ip.h>
```

FTP客户端库（FTP Client Library）。提供部分选定的FTP客户端功能。

## 81.2\_数据结构（Data Structures）

<a id="r_ftp_5Fclient"></a>

```c
struct ftp_client
```

FTP客户端上下文（Client Context）。

相关声明：[ftp_client](P083_FTP客户端上下文.md)。

## 81.3\_类型定义（Typedefs）

<a id="r_ga5d2fbddcb382dc2c4b082b32cb28ef82"></a>

```c
typedef void(* ftp_client_callback_t) (const uint8_t *msg, uint16_t len)
```

FTP异步回调函数（Asynchronous Callback Function）。

相关声明：[ftp_client_callback_t](P080_FTP完整API参考.md#ga5d2fbddcb382dc2c4b082b32cb28ef82)。

## 81.4\_枚举（Enumerations）

<a id="r_ga1fd1b76dd9faa02fdb72440c94851c9f"></a>

```c
enum ftp_reply_code { FTP_CODE_110_RESTART_MARKER_REPLAY = 110 , FTP_CODE_120_SERVICE_READY_IN_NNN_MINUTES = 120 , FTP_CODE_125_DATA_CONN_ALREADY_OPEN = 125 , FTP_CODE_150_FILE_STATUS_OK = 150 , FTP_CODE_200_OK = 200 , FTP_CODE_202_NOT_IMPLEMENTED = 202 , FTP_CODE_211_SYSTEM_STATUS = 211 , FTP_CODE_212_DIR_STATUS = 212 , FTP_CODE_213_FILE_STATUS = 213 , FTP_CODE_214_HELP_MSG = 214 , FTP_CODE_215_NAME_SYSTEM_TYPE = 215 , FTP_CODE_220_SERVICE_READY = 220 , FTP_CODE_221_SERVICE_CLOSING_CONN = 221 , FTP_CODE_225_DATA_CONN_OPEN = 225 , FTP_CODE_226_CLOSING_DATA_CONN_SUCCESS = 226 , FTP_CODE_227_ENTERING_PASSIVE_MODE = 227 , FTP_CODE_228_ENTERING_LONG_PASSIVE_MODE = 228 , FTP_CODE_229_ENTERING_EXT_PASSIVE_MODE = 229 , FTP_CODE_230_USER_LOGGED_IN = 230 , FTP_CODE_231_USER_LOGGED_OUT = 231 , FTP_CODE_233_LOGOUT_COMMAND_NOTED = 233 , FTP_CODE_234_SECURITY_ACCEPTED = 234 , FTP_CODE_250_FILE_ACTION_COMPLETED = 250 , FTP_CODE_257_PATHNAME_CREATED = 257 , FTP_CODE_331_USERNAME_OK_NEED_PASSWORD = 331 , FTP_CODE_332_NEED_ACCOUNT = 332 , FTP_CODE_350_FILE_ACTION_PENDING = 350 , FTP_CODE_421_SERVICE_UNAVAILABLE = 421 , FTP_CODE_425_CANNOT_OPEN_DATA_CONN = 425 , FTP_CODE_426_CONN_CLOSED = 426 , FTP_CODE_430_INVALID_USERNAME_OR_PASSWORD = 430 , FTP_CODE_434_HOST_UNAVAILABLE = 434 , FTP_CODE_450_FILE_ACTION_NOT_TAKEN = 450 , FTP_CODE_451_ACTION_ABORTED = 451 , FTP_CODE_452_ACTION_NOT_TAKEN = 452 , FTP_CODE_500_GENERAL_ERROR = 500 , FTP_CODE_501_SYNTAX_ERROR = 501 , FTP_CODE_502_COMMAND_NOT_COMPLETED = 502 , FTP_CODE_503_BAD_SEQUENCE_OF_COMMANDS = 503 , FTP_CODE_504_COMMAND_NOT_IMPLEMENTED = 504 , FTP_CODE_530_NOT_LOGGED_IN = 530 , FTP_CODE_532_NEED_ACCOUNT = 532 , FTP_CODE_534_CANNOT_CONNECT_SSL_REQUIRED = 534 , FTP_CODE_550_FILE_UNAVAILABLE = 550 , FTP_CODE_551_PAGE_TYPE_UNKNOWN = 551 , FTP_CODE_552_FILE_EXCEEDED_STORAGE_LOCATION = 552 , FTP_CODE_553_FILE_NAME_NOT_ALLOWED = 553 , FTP_CODE_631_INTEGRITY_PROTECTED_REPLY = 631 , FTP_CODE_632_INT_AND_CONF_PROTECTED_REPLY = 632 , FTP_CODE_633_CONFIDENTIALITY_PROTECTED_REPLY = 633 , FTP_CODE_900_UNKNOWN_ERROR = 900 , FTP_CODE_901_DISCONNECTED_BY_REMOTE = 901 , FTP_CODE_902_CONNECTION_ABORTED = 902 , FTP_CODE_903_SOCKET_POLL_ERROR = 903 , FTP_CODE_904_UNEXPECTED_POLL_EVENT = 904 , FTP_CODE_905_NETWORK_DOWN = 905 , FTP_CODE_909_UNEXPECTED_ERROR = 909 , FTP_CODE_910_DATA_TRANSFER_TIMEOUT = 910 , FTP_CODE_10054_CONNECTION_RESET_BY_PEER = 10054 , FTP_CODE_10060_CANNOT_CONNECT = 10060 , FTP_CODE_10061_CONNECTION_REFUSED = 10061 , FTP_CODE_10066_DIRECTORY_NOT_EMPTY = 10066 , FTP_CODE_10068_TOO_MANY_USERS = 10068 }
```

FTP服务器应答码（Server Reply Code）列表，参见[RFC 959文件传输协议](https://datatracker.ietf.org/doc/html/rfc959)。

相关声明：[ftp_reply_code](P080_FTP完整API参考.md#ga1fd1b76dd9faa02fdb72440c94851c9f)、[FTP_CODE_110_RESTART_MARKER_REPLAY](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa8d01634d86ff6225ccd632474c3ba24e)、[FTP_CODE_120_SERVICE_READY_IN_NNN_MINUTES](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa19a33a1e0797be0043bd601b14d8f26e)、[FTP_CODE_125_DATA_CONN_ALREADY_OPEN](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa73ea1be785d44a4295ed6a75d5f6dfb5)、[FTP_CODE_150_FILE_STATUS_OK](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fab529849ab3807fedf4d1f8e5a4ef0f8e)、[FTP_CODE_200_OK](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa6861e5ca7f670c4535c068222564dca1)、[FTP_CODE_202_NOT_IMPLEMENTED](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa923d41feabbfabbf07d2af4b53c4f7e2)、[FTP_CODE_211_SYSTEM_STATUS](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa61a8a385cf84bac33d4c5a8674698ab8)、[FTP_CODE_212_DIR_STATUS](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa3413c670d2c6d7acf4db6ba32a1e65c8)、[FTP_CODE_213_FILE_STATUS](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa64748b689db68fa0cb339dd05a9c7d5f)、[FTP_CODE_214_HELP_MSG](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa0c463837a30fc056dda3fd6861e08b8e)、[FTP_CODE_215_NAME_SYSTEM_TYPE](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9facb4dbe7ad6b21b3035c9dfaa4c6bd606)、[FTP_CODE_220_SERVICE_READY](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa50a6fe48a902b0ef77ca1edae9f3b621)、[FTP_CODE_221_SERVICE_CLOSING_CONN](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fadba5c377a8a199036028342f23ff4efd)、[FTP_CODE_225_DATA_CONN_OPEN](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa1d161d26f45fb34f92a3d90eb085ac43)、[FTP_CODE_226_CLOSING_DATA_CONN_SUCCESS](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa67c57b5668c76e059122b5cef1f5aa7c)、[FTP_CODE_227_ENTERING_PASSIVE_MODE](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa262af9766c244af4c48c2138d6ca69ee)、[FTP_CODE_228_ENTERING_LONG_PASSIVE_MODE](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa21038c2632abf047794844f8ad4745b3)、[FTP_CODE_229_ENTERING_EXT_PASSIVE_MODE](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa3812aa7f26553556d43e9de2e7334fb8)、[FTP_CODE_230_USER_LOGGED_IN](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa30af249b9321a12f3afecd91d7a4c878)、[FTP_CODE_231_USER_LOGGED_OUT](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa4b2b8ebe26117024353db6839e965611)、[FTP_CODE_233_LOGOUT_COMMAND_NOTED](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa41addb3c6db5be11eff8b31bd95af73c)、[FTP_CODE_234_SECURITY_ACCEPTED](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa20be33d647b863ba7cf1a911ad5e890d)、[FTP_CODE_250_FILE_ACTION_COMPLETED](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa4ce31dbbe2e3aa1829b33e26835198d6)、[FTP_CODE_257_PATHNAME_CREATED](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fad3170f0654f4125bb2283a5647111989)、[FTP_CODE_331_USERNAME_OK_NEED_PASSWORD](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa1dd9d9d393289ec8c3b1637063124498)、[FTP_CODE_332_NEED_ACCOUNT](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa362887c01cef49c24f857cb44b50745f)、[FTP_CODE_350_FILE_ACTION_PENDING](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa023293f5c686359a71ab467f34596452)、[FTP_CODE_421_SERVICE_UNAVAILABLE](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fae71d394182c338b54cb54fb43601efdc)、[FTP_CODE_425_CANNOT_OPEN_DATA_CONN](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa24b50796bd736f92fd5cd699ffda309b)、[FTP_CODE_426_CONN_CLOSED](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa4b5ebacbf400d5cfa5becdb652bde3a1)、[FTP_CODE_430_INVALID_USERNAME_OR_PASSWORD](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9faa8ba47771c6ecc429e3f0249b2991853)、[FTP_CODE_434_HOST_UNAVAILABLE](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fad775cb9ff8cc9e276b2da42a2411f7db)、[FTP_CODE_450_FILE_ACTION_NOT_TAKEN](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fadc7cded100e930866d3d4688654261c9)、[FTP_CODE_451_ACTION_ABORTED](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa01b4a58ab89cce0c7601fa12fe5c54f5)、[FTP_CODE_452_ACTION_NOT_TAKEN](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa8e91f38038fb2845ed2cf1bb11633e06)、[FTP_CODE_500_GENERAL_ERROR](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa2c51597ca89a0c956da2dfde9c9ff189)、[FTP_CODE_501_SYNTAX_ERROR](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fab746dd2a6dbb241c7708876b068a0b3a)、[FTP_CODE_502_COMMAND_NOT_COMPLETED](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa57e289509dca21af5fa78a61fc787085)、[FTP_CODE_503_BAD_SEQUENCE_OF_COMMANDS](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa9021858f8f1fb75455808cbe2858fe6d)、[FTP_CODE_504_COMMAND_NOT_IMPLEMENTED](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa2ecbe59151d8857b2069ef129ffb7124)、[FTP_CODE_530_NOT_LOGGED_IN](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fad62ed521671902a07306f8693f57ad12)、[FTP_CODE_532_NEED_ACCOUNT](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa6f0da4302c0c47b9950a9638824b9071)、[FTP_CODE_534_CANNOT_CONNECT_SSL_REQUIRED](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa5f6630cabd8f3164f9529514a2228a4b)、[FTP_CODE_550_FILE_UNAVAILABLE](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa5e9d356354c7ba6f71aaf662e500d921)、[FTP_CODE_551_PAGE_TYPE_UNKNOWN](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa5c343ab624f0c93014d45b563caab935)、[FTP_CODE_552_FILE_EXCEEDED_STORAGE_LOCATION](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fad1e65f88caad7e6410bd042405edebd2)、[FTP_CODE_553_FILE_NAME_NOT_ALLOWED](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa2b30ed8b504cd9c3934a7380ca9305dd)、[FTP_CODE_631_INTEGRITY_PROTECTED_REPLY](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9faf0d941ddc9c7cbbd331967bc89f56936)、[FTP_CODE_632_INT_AND_CONF_PROTECTED_REPLY](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fafe9ff46b8d55d6e49387182cbbc020f3)、[FTP_CODE_633_CONFIDENTIALITY_PROTECTED_REPLY](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa2b00435a0c116dfdde586e9ba5ecee64)、[FTP_CODE_900_UNKNOWN_ERROR](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa4a098c006025387894a44e98710ccfd4)、[FTP_CODE_901_DISCONNECTED_BY_REMOTE](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fad57f89f9c561f2a11537d87943bbcb0f)、[FTP_CODE_902_CONNECTION_ABORTED](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9faa20686c639dd8ad6b8c34d3bcf81aa08)、[FTP_CODE_903_SOCKET_POLL_ERROR](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa80e8cd999e1444210404fd6777297050)、[FTP_CODE_904_UNEXPECTED_POLL_EVENT](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9facff17031b4639ddc19969ea0fd46cb37)、[FTP_CODE_905_NETWORK_DOWN](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa63f4ed70304926d9401d07df5b947fac)、[FTP_CODE_909_UNEXPECTED_ERROR](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9faf90ecdd5446eff36c6eee2bf217c47e3)、[FTP_CODE_910_DATA_TRANSFER_TIMEOUT](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa02735b72822fed42af9addaa19da4afc)、[FTP_CODE_10054_CONNECTION_RESET_BY_PEER](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa0f31db3b37502fa7fe35d9b4c3614bc8)、[FTP_CODE_10060_CANNOT_CONNECT](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9faa3cf4061361db61705d267161d8e2299)、[FTP_CODE_10061_CONNECTION_REFUSED](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9facb625cec2d6adf0acf4cabf1566a36b6)、[FTP_CODE_10066_DIRECTORY_NOT_EMPTY](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9fa1972ccdb2117b1fce8b07c6ce01c63f5)、[FTP_CODE_10068_TOO_MANY_USERS](P080_FTP完整API参考.md#gga1fd1b76dd9faa02fdb72440c94851c9faeb89d65f6cd5a982dfae8cca5e4caa4b)。

<a id="r_gad2e0517bed675c54f69e457815935da5"></a>

```c
enum ftp_transfer_type { FTP_TYPE_ASCII , FTP_TYPE_BINARY }
```

FTP传输模式（Transfer Mode）。

相关声明：[ftp_transfer_type](P080_FTP完整API参考.md#gad2e0517bed675c54f69e457815935da5)、[FTP_TYPE_ASCII](P080_FTP完整API参考.md#ggad2e0517bed675c54f69e457815935da5ab3a051eff6a65236e97811716b2ae9ff)、[FTP_TYPE_BINARY](P080_FTP完整API参考.md#ggad2e0517bed675c54f69e457815935da5a3a21938d02227ad37c1fcad3cda67039)。

<a id="r_gaf9f99979b6178b195574135e30146b51"></a>

```c
enum ftp_put_type { FTP_PUT_NORMAL , FTP_PUT_UNIQUE , FTP_PUT_APPEND }
```

FTP文件写入模式（File Write Mode）。

相关声明：[ftp_put_type](P080_FTP完整API参考.md#gaf9f99979b6178b195574135e30146b51)、[FTP_PUT_NORMAL](P080_FTP完整API参考.md#ggaf9f99979b6178b195574135e30146b51a1daa8fd6fb897bb0b6bedcd95b257d53)、[FTP_PUT_UNIQUE](P080_FTP完整API参考.md#ggaf9f99979b6178b195574135e30146b51a86668e9c2d6905f8f270f353a015fc7d)、[FTP_PUT_APPEND](P080_FTP完整API参考.md#ggaf9f99979b6178b195574135e30146b51a64c12215f266804fd8d64112ca11d56e)。

## 81.5\_函数（Functions）

<a id="r_gadda7bc4206bc8a6b22be619b1ea0ecd8"></a>

```c
int ftp_init (struct ftp_client *client, ftp_client_callback_t ctrl_callback, ftp_client_callback_t data_callback)
```

初始化FTP客户端上下文。

相关声明：[ftp_init](P080_FTP完整API参考.md#gadda7bc4206bc8a6b22be619b1ea0ecd8)、[ftp_client](P083_FTP客户端上下文.md)、[ftp_client_callback_t](P080_FTP完整API参考.md#ga5d2fbddcb382dc2c4b082b32cb28ef82)。

<a id="r_gabaa6663c007b7e8c3d508b31d28d71ee"></a>

```c
int ftp_uninit (struct ftp_client *client)
```

反初始化FTP客户端上下文（Uninitialize）。

相关声明：[ftp_uninit](P080_FTP完整API参考.md#gabaa6663c007b7e8c3d508b31d28d71ee)、[ftp_client](P083_FTP客户端上下文.md)。

<a id="r_ga133d01a5122050e71b9164b631347345"></a>

```c
int ftp_open (struct ftp_client *client, const char *hostname, uint16_t port, int sec_tag)
```

打开FTP连接。

相关声明：[ftp_open](P080_FTP完整API参考.md#ga133d01a5122050e71b9164b631347345)、[ftp_client](P083_FTP客户端上下文.md)。

<a id="r_gaaa49d1b2dc6c033285c36a745a7a988c"></a>

```c
int ftp_login (struct ftp_client *client, const char *username, const char *password)
```

登录FTP服务器。

相关声明：[ftp_login](P080_FTP完整API参考.md#gaaa49d1b2dc6c033285c36a745a7a988c)、[ftp_client](P083_FTP客户端上下文.md)。

<a id="r_ga1021a2168ba8e0955637807fdef4d692"></a>

```c
int ftp_close (struct ftp_client *client)
```

关闭FTP连接。

相关声明：[ftp_close](P080_FTP完整API参考.md#ga1021a2168ba8e0955637807fdef4d692)、[ftp_client](P083_FTP客户端上下文.md)。

<a id="r_ga9c35334bbe9e0c7d86de7fea470e3742"></a>

```c
int ftp_status (struct ftp_client *client)
```

获取FTP服务器和连接状态；同时返回服务器系统类型（System Type）。

相关声明：[ftp_status](P080_FTP完整API参考.md#ga9c35334bbe9e0c7d86de7fea470e3742)、[ftp_client](P083_FTP客户端上下文.md)。

<a id="r_ga7e44297d4ffa3dda684e8fe09a2f30d1"></a>

```c
int ftp_type (struct ftp_client *client, enum ftp_transfer_type type)
```

设置FTP传输类型（Transfer Type）。

相关声明：[ftp_type](P080_FTP完整API参考.md#ga7e44297d4ffa3dda684e8fe09a2f30d1)、[ftp_client](P083_FTP客户端上下文.md)、[ftp_transfer_type](P080_FTP完整API参考.md#gad2e0517bed675c54f69e457815935da5)。

<a id="r_gaabd04bf684f643ce5e313c474f0bf33c"></a>

```c
int ftp_pwd (struct ftp_client *client)
```

输出工作目录。

相关声明：[ftp_pwd](P080_FTP完整API参考.md#gaabd04bf684f643ce5e313c474f0bf33c)、[ftp_client](P083_FTP客户端上下文.md)。

<a id="r_ga454863be9cb65d02ac59580f468ab355"></a>

```c
int ftp_list (struct ftp_client *client, const char *options, const char *target)
```

列出目录或文件的信息。

相关声明：[ftp_list](P080_FTP完整API参考.md#ga454863be9cb65d02ac59580f468ab355)、[ftp_client](P083_FTP客户端上下文.md)。

<a id="r_ga488cc79e627f7974bb097a9ac54aaaf9"></a>

```c
int ftp_cwd (struct ftp_client *client, const char *folder)
```

切换工作目录（Working Directory）。

相关声明：[ftp_cwd](P080_FTP完整API参考.md#ga488cc79e627f7974bb097a9ac54aaaf9)、[ftp_client](P083_FTP客户端上下文.md)。

<a id="r_gac057b5a49b9788cae46b49d5a7e2a355"></a>

```c
int ftp_mkd (struct ftp_client *client, const char *folder)
```

创建目录。

相关声明：[ftp_mkd](P080_FTP完整API参考.md#gac057b5a49b9788cae46b49d5a7e2a355)、[ftp_client](P083_FTP客户端上下文.md)。

<a id="r_gacc35656664b3efeee20ec89c0e50e093"></a>

```c
int ftp_rmd (struct ftp_client *client, const char *folder)
```

删除目录。

相关声明：[ftp_rmd](P080_FTP完整API参考.md#gacc35656664b3efeee20ec89c0e50e093)、[ftp_client](P083_FTP客户端上下文.md)。

<a id="r_gad7aec38daf5f8595905293a9e52b217a"></a>

```c
int ftp_rename (struct ftp_client *client, const char *old_name, const char *new_name)
```

重命名文件。

相关声明：[ftp_rename](P080_FTP完整API参考.md#gad7aec38daf5f8595905293a9e52b217a)、[ftp_client](P083_FTP客户端上下文.md)。

<a id="r_ga132a310c8f7854623f203f7cddb53b76"></a>

```c
int ftp_delete (struct ftp_client *client, const char *file)
```

删除文件。

相关声明：[ftp_delete](P080_FTP完整API参考.md#ga132a310c8f7854623f203f7cddb53b76)、[ftp_client](P083_FTP客户端上下文.md)。

<a id="r_gab254efce8f6874498e577a05c5a05f28"></a>

```c
int ftp_get (struct ftp_client *client, const char *file)
```

获取文件。

相关声明：[ftp_get](P080_FTP完整API参考.md#gab254efce8f6874498e577a05c5a05f28)、[ftp_client](P083_FTP客户端上下文.md)。

<a id="r_ga6b7e18f2c7197825a0c8e7ea8128e628"></a>

```c
int ftp_put (struct ftp_client *client, const char *file, const uint8_t *data, uint16_t length, int type)
```

将数据写入文件；如果文件不存在，则创建文件。

相关声明：[ftp_put](P080_FTP完整API参考.md#ga6b7e18f2c7197825a0c8e7ea8128e628)、[ftp_client](P083_FTP客户端上下文.md)。

<a id="r_ga7e821b21f05c5366eac8fef730b7df5f"></a>

```c
int ftp_keepalive (struct ftp_client *client)
```

与服务器交换保活命令（Keep-alive Commands）。

相关声明：[ftp_keepalive](P080_FTP完整API参考.md#ga7e821b21f05c5366eac8fef730b7df5f)、[ftp_client](P083_FTP客户端上下文.md)。

## 81.6\_相关头文件与源码

此页声明来自`<zephyr/net/ftp_client.h>`。本仓库的[对应头文件](../../../include/zephyr/net/ftp_client.h)可用于源码跟踪；本仓库版本可能与官网`latest`不同。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-typedef-members"></a>
<a id="typedef-members"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>

[上一章](P080_FTP完整API参考.md) · [返回大纲](大纲.md) · [下一章](P082_FTP头文件源码.md)
