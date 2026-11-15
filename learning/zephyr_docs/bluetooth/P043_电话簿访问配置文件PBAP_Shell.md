---
id: learning.zephyr-docs.bluetooth.page-43
title: 电话簿访问配置文件PBAP_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/classic/pbap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-classic-pbap-shell"></a>

# 第43章\_电话簿访问配置文件PBAP\_Shell

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/classic/pbap.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——使用前提：以下命令在启用了对应蓝牙功能的目标固件Zephyr Shell中执行，初始化与接入方式见[蓝牙Shell](P007_蓝牙Shell.md)。代码中的 `uart:~$` 是提示符，其后输出是原文预期结果；输入命令时不复制提示符和日志。若命令不可用或初始化失败，应先检查目标配置、控制器能力及当前版本帮助，再继续连接或传输步骤。本批仅翻译与核对文档，未连接设备或执行这些命令。

> 译注——术语：ACL 为异步面向连接链路（Asynchronous Connection-oriented Link）；SDP 为服务发现协议（Service Discovery Protocol）；OBEX 为对象交换协议（Object Exchange Protocol）；SLC 为服务级连接（Service Level Connection）。`telecom/pb` 等表示对端电话簿对象目录，与本地仓库位置无关。

本文说明如何运行经典蓝牙（Bluetooth Classic）的电话簿访问配置文件（Phonebook Access Profile，PBAP）功能。`pbap` 命令提供经典蓝牙 PBAP Shell 命令。

有两个子命令：`pbap pce` 和 `pbap pse`。

`pbap pce` 提供电话簿客户端设备（Phonebook Client Equipment，PCE）功能，`pbap pse` 提供电话簿服务端设备（Phonebook Server Equipment，PSE）功能。

<a id="commands"></a>

## 43.1 命令（Commands）

除了 `pbap pce sdp_reg`、`pbap pse rfcomm_register` 和 `pbap pse l2cap_register`，其余命令都只能在建立 ACL 连接后使用。

`pbap` 命令如下：

```text
uart:~$ pbap
pbap - Bluetooth pbap shell commands
Subcommands:
  alloc_buf                        : Alloc tx buffer
  release_buf                      : Free allocated tx buffer
  pce                              : Client sets
  pse                              : Server sets
  add_header_auth_challenge        : <password>
  add_header_auth_response         : <password>
  add_ap                           : add application param
```

`pbap pce` 命令如下：

```text
uart:~$ pbap pce
pce - Client sets
Subcommands:
  sdp_reg                          : [none]
  sdp_discover                     : [none]
  connect_rfcomm                   : <channel>
  disconnect_rfcomm                : [none]
  connect_l2cap                    : <channel>
  disconnect_l2cap                 : [none]
  connect                          : <mopl>
  disconnect                       : [none]
  pull_pb                          : <name> [srmp]
  pull_vcard_listing               : <name> [srmp]
  pull_vcard_entry                 : <name> [srmp]
  set_phone_book                   : <Flags> [name]
  abort                            : [none]
```

`pbap pse` 命令如下：

```text
uart:~$ pbap pse
pse - Server sets
Subcommands:
  rfcomm_register                  : [none]
  l2cap_register                   : [none]
  register                         : [none]
  connect_rsp                      : <mopl> <rsp: unauth,success,error> [rsp_code]
  disconnect_rsp                   : <rsp: success,error> [rsp_code]
  pull_phone_book_rsp              : <rsp: noerror, error> [rsp_code] [srmp]
  pull_vcard_listing_rsp           : <rsp: noerror, error> [rsp_code] [srmp]
  pull_vcard_entry_rsp             : <rsp: noerror, error> [rsp_code] [srmp]
  set_phone_book_rsp               : <rsp: success, error> [rsp_code]
  abort_rsp                        : <rsp: success, error> [rsp_code]
```

`pbap add_ap` 应用参数（Application Parameters）命令如下：

```text
uart:~$ pbap add_ap
add_ap - add application param
Subcommands:
  Order                            : <indexed/alphanumeric/phonetic>
  SearchValue                      : <text>
  SearchAttribute                  : <name/number/sound>
  MaxListCount                     : <0x0000-0xffff>
  ListStartOffset                  : <0x0000-0xffff>
  PropertySelector                 : <64 bits mask : bt_pbap_appl_param_property_mask>
  Format                           : <v2.1/v3.0>
  PhonebookSize                    : <0x0000-0xffff>
  NewMissedCalls                   : <0x00-0xff>
  PrimaryFolderVersion             : <16bytes>
  SecondaryFolderVersion           : <16bytes>
  vCardSelector                    : <64 bits mask : bt_pbap_appl_param_property_mask>
  DatabaseIdentifier               : <16bytes>
  vCardSelectorOperator            : <or/and>
  ResetNewMissedCalls              :
  PbapSupportedFeatures            : [supported features]
```

<a id="pbap-pce-slc"></a>

## 43.2 PBAP 客户端设备的服务级连接（PBAP PCE SLC）

`pbap pce` 子命令提供经典蓝牙 PBAP 电话簿客户端设备（PCE）功能。

注册 PCE 的 SDP 服务记录：

```text
uart:~$ pbap pce sdp_reg
```

发现 PSE 的 SDP 服务记录：

```text
uart:~$ pbap pce sdp_discover
SDP PBAP data@0x2000d4a0 (len 54) hint 0 from remote XX:XX:XX:XX:XX:XX
PSE rfcomm channel param 0x0001
PSE l2cap psm param 0x0019
PSE feature param 0x00000019
```

通过 RFCOMM 连接 PSE：

```text
uart:~$ pbap pce connect_rfcomm 0x01
PBAP PCE rfcomm transport connected on 0x20005dd8
```

建立 OBEX 连接：

```text
uart:~$ pbap alloc_buf
uart:~$ pbap pce connect 300
pbap connect result Success, mopl 256
Connection ID: 0x00000001
Processing successful connection...
Connection established successfully (no auth required)
```

断开与 PSE 的连接：

```text
uart:~$ pbap pce disconnect
pbap disconnect result OK
PBAP PCE rfcomm transport disconnected
```

<a id="pbap-pse-slc"></a>

## 43.3 PBAP 服务端设备的服务级连接（PBAP PSE SLC）

`pbap pse` 子命令提供经典蓝牙 PBAP 电话簿服务端设备（PSE）功能。

注册 PSE 的 RFCOMM 服务端：

```text
uart:~$ pbap pse rfcomm_register
RFCOMM server (channel 01) is registered
```

注册 PSE 的 L2CAP 服务端：

```text
uart:~$ pbap pse l2cap_register
L2cap server (psm 01) is registered
```

注册 PSE：

```text
uart:~$ pbap pse register
```

接受 PCE 连接并作出响应：

```text
uart:~$ pbap alloc_buf
uart:~$ pbap pse connect_rsp 300 success
pbap connect version 1, mopl 256
Connection established with authentication
```

断开与 PCE 的连接：

```text
uart:~$ pbap alloc_buf
uart:~$ pbap pse disconnect_rsp success
pbap disconnect requested by pce
```

<a id="pull-phonebook"></a>

## 43.4 拉取电话簿（Pull Phonebook）

从 PSE 拉取完整电话簿：

**PCE 客户端一侧（PCE side）**

<a id="tab-0-UENFIHNpZGU="></a>
<a id="panel-0-UENFIHNpZGU="></a>

```text
uart:~$ pbap alloc_buf
uart:~$ pbap pce pull_pb "telecom/pb"
pbap pull phonebook result Continue
Application Parameters (length: 2):
  PhonebookSize: 0x0002 (2)

=========body=========
BEGIN:VCARD
VERSION:2.1
FN;CHARSET=UTF-8:descvs
N;CHARSET=UTF-8:descvs
END:VCARD
=========body=========

please send pull cmd again
uart:~$ pbap pce pull_pb "telecom/pb"
pbap pull phonebook result Success
Application Parameters (length: 2):
  PhonebookSize: 0x0002 (2)

=========body=========
BEGIN:VCARD
VERSION:2.1
FN;CHARSET=UTF-8:descvs
N;CHARSET=UTF-8:descvs
END:VCARD
=========body=========
```

**PSE 服务端一侧（PSE side）**

<a id="tab-0-UFNFIHNpZGU="></a>
<a id="panel-0-UFNFIHNpZGU="></a>

```text
uart:~$ pbap alloc_buf
pbap_pse get pull_phone_book request
name = telecom/pb
Application Parameters (length: 0):

uart:~$ pbap alloc_buf
uart:~$ pbap pse pull_phone_book_rsp noerror
Suspend after sending a single response and await the PCE request

uart:~$ pbap alloc_buf
uart:~$ pbap pse pull_phone_book_rsp noerror
Keep sending responses continuously until rsp_code is success
```

<a id="pull-vcard-listing"></a>

## 43.5 拉取 vCard 列表（Pull vCard Listing）

拉取电子名片（vCard）列表以发现联系人：

**PCE 客户端一侧（PCE side）**

<a id="tab-1-UENFIHNpZGU="></a>
<a id="panel-1-UENFIHNpZGU="></a>

```text
uart:~$ pbap alloc_buf
uart:~$ pbap add_ap MaxListCount 0x0005
uart:~$ pbap add_ap ListStartOffset 0x0000
uart:~$ pbap pce pull_vcard_listing "telecom/pb"
pbap pull vcard_listing result Continue
Application Parameters (length: 6):
  MaxListCount: 0x0005 (5)
  ListStartOffset: 0x0000 (0)

=========body=========
<?xml version="1.0"?><!DOCTYPE vcard-listing SYSTEM "vcard-listing.dtd">
<vCard-listing version="1.0"><card handle="1.vcf" name="qwe"/>
<card handle="2.vcf" name="qwe"/>
=========body=========

please send pull cmd again
uart:~$ pbap pce pull_vcard_listing "telecom/pb"
pbap pull vcard_listing result Success
=========body=========
<card handle="1.vcf" name="qwe"/><card handle="2.vcf" name="qwe"/>
/<vCard-listing>
=========body=========
```

**PSE 服务端一侧（PSE side）**

<a id="tab-1-UFNFIHNpZGU="></a>
<a id="panel-1-UFNFIHNpZGU="></a>

```text
uart:~$ pbap alloc_buf
pbap_pse get pull_vcard_listing request
name = telecom/pb
Application Parameters (length: 6):
  MaxListCount: 0x0005 (5)
  ListStartOffset: 0x0000 (0)

uart:~$ pbap alloc_buf
uart:~$ pbap pse pull_vcard_listing_rsp noerror
Suspend after sending a single response and await the PCE request

uart:~$ pbap alloc_buf
uart:~$ pbap pse pull_vcard_listing_rsp noerror
```

> 译注——原文 XML 拼写：上方原日志将结束标签写成 `/<vCard-listing>`，不符合 XML 结束标签语法；正确形式应为 `</vCard-listing>`。这里保留原日志，实际生成或解析电子名片列表时应使用合法 XML。

<a id="pull-vcard-entry"></a>

## 43.6 拉取 vCard 条目（Pull vCard Entry）

拉取指定 vCard 条目：

**PCE 客户端一侧（PCE side）**

<a id="tab-2-UENFIHNpZGU="></a>
<a id="panel-2-UENFIHNpZGU="></a>

```text
uart:~$ pbap alloc_buf
uart:~$ pbap add_ap Format v2.1
uart:~$ pbap pce pull_vcard_entry "telecom/pb/1.vcf"
pbap pull vcard_entry result Continue
Application Parameters (length: 1):
  Format: 0x00 (vCard 2.1)

=========body=========
BEGIN:VCARD
VERSION:2.1
FN:
N:
TEL;X-0:1155
=========body=========

uart:~$ pbap pce pull_vcard_entry "telecom/pb/1.vcf"
pbap pull vcard_entry result Success

=========body=========
X-IRMC-CALL-DATETIME;DIALED:20220913T110607
END:VCARD
=========body=========
```

**PSE 服务端一侧（PSE side）**

<a id="tab-2-UFNFIHNpZGU="></a>
<a id="panel-2-UFNFIHNpZGU="></a>

```text
uart:~$ pbap alloc_buf
pbap_pse get pull_vcard_entry request
name = telecom/pb/1.vcf
Application Parameters (length: 1):
  Format: 0x00 (vCard 2.1)

uart:~$ pbap alloc_buf
uart:~$ pbap pse pull_vcard_entry_rsp noerror
Suspend after sending a single response and await the PCE request

uart:~$ pbap alloc_buf
uart:~$ pbap pse pull_vcard_entry_rsp noerror
```

<a id="set-phone-book"></a>

## 43.7 设置电话簿（Set Phone Book）

更改当前电话簿目录：

**PCE 客户端一侧（PCE side）**

<a id="tab-3-UENFIHNpZGU="></a>
<a id="panel-3-UENFIHNpZGU="></a>

```text
uart:~$ pbap alloc_buf
uart:~$ pbap pce set_phone_book 0x02 "telecom"
PBAP set phonebook result OK

uart:~$ pbap alloc_buf
uart:~$ pbap pce set_phone_book 0x02 "pb"
PBAP set phonebook result OK

uart:~$ pbap alloc_buf
uart:~$ pbap pce set_phone_book 0x02
PBAP set phonebook result OK
```

**PSE 服务端一侧（PSE side）**

<a id="tab-3-UFNFIHNpZGU="></a>
<a id="panel-3-UFNFIHNpZGU="></a>

```text
uart:~$ pbap alloc_buf
pbap_pse get set_phone_book request
set phonebook to children telecom folder

uart:~$ pbap alloc_buf
uart:~$ pbap pse set_phone_book_rsp success

uart:~$ pbap alloc_buf
pbap_pse get set_phone_book request
set phonebook to children pb folder

uart:~$ pbap alloc_buf
uart:~$ pbap pse set_phone_book_rsp success

uart:~$ pbap alloc_buf
pbap_pse get set_phone_book request
set phonebook to parent folder

uart:~$ pbap alloc_buf
uart:~$ pbap pse set_phone_book_rsp success
```

<a id="abort-operation"></a>

## 43.8 中止操作（Abort Operation）

中止正在进行的操作：

**PCE 客户端一侧（PCE side）**

<a id="tab-4-UENFIHNpZGU="></a>
<a id="panel-4-UENFIHNpZGU="></a>

```text
uart:~$ pbap pce abort
abort success.
```

**PSE 服务端一侧（PSE side）**

<a id="tab-4-UFNFIHNpZGU="></a>
<a id="panel-4-UFNFIHNpZGU="></a>

```text
uart:~$ pbap alloc_buf
pbap_pse get receive abort req

uart:~$ pbap pse abort_rsp success
```

<a id="authentication"></a>

## 43.9 身份认证（Authentication）

PBAP 可以使用 OBEX 身份认证（authentication）保护连接。认证过程采用质询—响应（challenge-response）机制。

PCE 发起认证质询的示例：

**PCE 客户端一侧（PCE side）**

<a id="tab-5-UENFIHNpZGU="></a>
<a id="panel-5-UENFIHNpZGU="></a>

```text
uart:~$ pbap alloc_buf
uart:~$ pbap add_header_auth_challenge "password123"
uart:~$ pbap pce connect 255
pbap connect result Unauthorized, mopl 255
PSE requires authentication
Action required:
  1. Allocate new tx_buf (pbap alloc_buf)
  2. Add auth_response header (pbap add_header_auth_response <password>)
  3. Add original auth_challenge header (pbap add_header_auth_challenge <password>)
  4. Re-send connect request (pbap pce connect <mopl>)

uart:~$ pbap alloc_buf
uart:~$ pbap add_header_auth_response "password123"
uart:~$ pbap add_header_auth_challenge "password123"
uart:~$ pbap pce connect 255
pbap connect result Success, mopl 255
Connection ID: 0x00000001
Authentication verified successfully
Connection established with authentication
```

**PSE 服务端一侧（PSE side）**

<a id="tab-5-UFNFIHNpZGU="></a>
<a id="panel-5-UFNFIHNpZGU="></a>

```text
uart:~$ pbap alloc_buf
uart:~$ pbap pse register

uart:~$ pbap alloc_buf
pbap connect version 1, mopl 255
PCE authentication required - add auth_response to connect_rsp tx_buf

uart:~$ pbap alloc_buf
uart:~$ pbap add_header_auth_challenge "password123"
uart:~$ pbap pse connect_rsp 255 unauth

uart:~$ pbap alloc_buf
pbap connect version 1, mopl 255
auth success
Connection established with authentication

uart:~$ pbap alloc_buf
uart:~$ pbap pse connect_rsp 255 success
```


对应官方文档源码：[doc/services/connectivity/bluetooth/shell/classic/pbap.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/classic/pbap.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/connectivity/bluetooth/shell/classic/pbap.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：消息访问配置文件MAP_Shell](P042_消息访问配置文件MAP_Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：串口配置文件SPP_Shell](P044_串口配置文件SPP_Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P042_消息访问配置文件MAP_Shell.md) · [返回大纲](大纲.md) · [下一章](P044_串口配置文件SPP_Shell.md)

</details>

<!-- reading-navigation:end -->
