---
id: learning.zephyr-docs.api-platform-topic-reference.page-3
title: 蓝牙 API（Bluetooth APIs）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_蓝牙 API（Bluetooth APIs）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙 API（Bluetooth APIs）

<a id="details"></a>

蓝牙应用程序编程接口（Bluetooth APIs）。蓝牙子系统核心 API（Bluetooth Subsystem Core APIs）提供使用和管理蓝牙通信所必需的功能，包括蓝牙协议栈初始化（Stack Initialization）、设备发现（Device Discovery）、连接管理（Connection Management）、数据传输（Data Transmission）、配置文件（Profiles）和服务（Services）。这些 API 同时支持经典蓝牙（Classic Bluetooth）和蓝牙低功耗（Bluetooth Low Energy，LE）操作。

<a id="header-groups"></a>
<a id="groups"></a>

## 3.1\_主题（Topics）

<a id="r_bt_5Fa2dp"></a>

相关声明：[高级音频分发配置文件（Advanced Audio Distribution Profile，A2DP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html)。

<a id="r_bt_5Fans"></a>

相关声明：[警报通知服务（Alert Notification Service，ANS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html)。

警报通知服务（Alert Notification Service，ANS）

<a id="r_bt_5Fassigned_5Fnumbers"></a>

相关声明：[分配编号（Assigned Numbers）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers.html)。

蓝牙分配编号（Bluetooth Assigned Numbers）、代码和标识符。

<a id="r_bt_5Fatt"></a>

相关声明：[属性协议（Attribute Protocol，ATT）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html)。

属性协议（Attribute Protocol，ATT）

<a id="r_bt_5Faics"></a>

相关声明：[音频输入控制服务（Audio Input Control Service，AICS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html)。

音频输入控制服务（Audio Input Control Service，AICS）

<a id="r_bt_5Fascs"></a>

相关声明：[音频流控制服务（Audio Stream Control Service，ASCS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html)。

音频流控制服务（Audio Stream Control Service，ASCS）

<a id="r_bt_5Favrcp"></a>

相关声明：[音频/视频远程控制配置文件（Audio Video Remote Control Profile，AVRCP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html)。

音频/视频远程控制配置文件（Audio Video Remote Control Profile，AVRCP）

<a id="r_bt_5Fbap_5Flc3_5Fpreset"></a>

相关声明：[基本音频配置文件（Basic Audio Profile，BAP）的 LC3 预设](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html)。

基本音频配置文件（Basic Audio Profile，BAP）的 LC3 预设

<a id="r_bt_5Fbip"></a>

相关声明：[基本成像配置文件（Basic Imaging Profile，BIP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html)。

基本成像配置文件（Basic Imaging Profile，BIP）

<a id="r_bt_5Fbas"></a>

相关声明：[电池服务（Battery Service，BAS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html)。

电池服务（Battery Service，BAS）

<a id="r_bluenrg_5Fhci_5Fdriver"></a>

相关声明：[BlueNRG HCI 驱动扩展 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bluenrg__hci__driver.html)。

BlueNRG HCI 驱动专用 API

<a id="r_bt_5Faudio"></a>

相关声明：[蓝牙音频（Bluetooth Audio）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html)。

蓝牙音频（Bluetooth Audio）

<a id="r_bt_5Fbap"></a>

相关声明：[蓝牙基本音频配置文件（Bluetooth Basic Audio Profile）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html)。

蓝牙基本音频配置文件（Bluetooth Basic Audio Profile，BAP）

<a id="r_bt_5Fccid"></a>

相关声明：[蓝牙内容控制标识符（Bluetooth Content Control Identifier）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccid.html)。

蓝牙内容控制标识符（Bluetooth Content Control Identifier，CCID）

<a id="r_bt_5Fctrl"></a>

相关声明：[蓝牙控制器（Bluetooth Controller）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ctrl.html)。

蓝牙控制器（Bluetooth Controller）

<a id="r_bt_5Fgmap"></a>

相关声明：[蓝牙游戏音频配置文件（Bluetooth Gaming Audio Profile）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html)。

蓝牙游戏音频配置文件（Bluetooth Gaming Audio Profile，GMAP）

<a id="r_bt_5Fhci_5Fapi"></a>

相关声明：[蓝牙主机控制器接口（Bluetooth HCI）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html)。

蓝牙主机控制器接口（Host Controller Interface，HCI）的相关接口。

<a id="r_bt_5Fhci_5Fpkt"></a>

相关声明：[蓝牙HCI数据包辅助接口（Packet Helpers）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html)。

蓝牙HCI数据包辅助接口（Packet Helpers）。

<a id="r_bt_5Fhid"></a>

相关声明：[蓝牙人机接口设备（Bluetooth HID）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid.html)。

蓝牙人机接口设备（Bluetooth HID）

<a id="r_bt_5Fhid_5Fdevice"></a>

相关声明：[蓝牙 HID 设备（Device）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html)。

蓝牙 HID 设备（Device）

<a id="r_bt_5Fhid_5Fhost"></a>

相关声明：[蓝牙 HID 主机（Host）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html)。

蓝牙 HID 主机（Host）

<a id="r_bt_5Flc3"></a>

相关声明：[蓝牙 LC3 编解码器（Bluetooth LC3 codec）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__lc3.html)。

LC3

<a id="r_bt_5Fl2cap_5Fbr"></a>

相关声明：[用于基本速率/增强数据速率（BR/EDR）的蓝牙逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol，L2CAP）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html)。

用于基本速率/增强数据速率（BR/EDR）的蓝牙逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol，L2CAP）。

<a id="r_bt_5Fmesh"></a>

相关声明：[蓝牙网状网络（Bluetooth Mesh）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html)。

蓝牙网状网络（Bluetooth Mesh）

<a id="r_bt_5Fbyteorder"></a>

相关声明：[字节序（Byte Order）。](../byteorder_reference/P003_蓝牙字节序辅助接口.md)。

字节序（Byte Order）。

<a id="r_bt_5Fccp"></a>

相关声明：[呼叫控制配置文件（Call Control Profile，CCP）](P004_呼叫控制配置文件（Call Control Profile，CCP）.md)。

呼叫控制配置文件（Call Control Profile，CCP）

<a id="r_bt_5Fle_5Fcs"></a>

相关声明：[信道探测（Channel Sounding，CS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html)。

低功耗蓝牙信道探测（LE Channel Sounding，CS）

<a id="r_bt_5Fcap"></a>

相关声明：[通用音频配置文件（Common Audio Profile，CAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html)。

通用音频配置文件（Common Audio Profile，CAP）

<a id="r_bt_5Fconn"></a>

相关声明：[连接管理（Connection management）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html)。

连接管理（Connection management）

<a id="r_bt_5Fcsip"></a>

相关声明：[协调集标识配置文件（Coordinated Set Identification Profile，CSIP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html)。

协调集标识配置文件（Coordinated Set Identification Profile，CSIP）

<a id="r_bt_5Fcrypto"></a>

相关声明：[密码学（Cryptography）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html)。

密码学（Cryptography）

<a id="r_bt_5Fcts"></a>

相关声明：[当前时间服务（Current Time Service，CTS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html)。

当前时间服务（Current Time Service，CTS）

<a id="r_bt_5Fbuf"></a>

相关声明：[数据缓冲区（Data buffers）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html)。

数据缓冲区（Data buffers）

<a id="r_bt_5Faddr"></a>

相关声明：[设备地址（Device Address）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html)。

蓝牙设备地址（Bluetooth Device Address）的定义和工具。

<a id="r_bt_5Fets"></a>

相关声明：[经过时间服务（Elapsed Time Service，ETS）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html)。

<a id="r_bt_5Fead"></a>

相关声明：[加密广播数据（Encrypted Advertising Data，EAD）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html)。

加密广播数据（Encrypted Advertising Data，EAD）

<a id="r_bt_5Fgmap_5Flc3_5Fpreset"></a>

相关声明：[游戏音频配置文件（Gaming Audio Profile，GMAP）的 LC3 预设](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap__lc3__preset.html)。

游戏音频配置文件（Gaming Audio Profile，GMAP）的 LC3 预设

<a id="r_bt_5Fgap"></a>

相关声明：[通用访问配置文件（Generic Access Profile，GAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html)。

通用访问配置文件（Generic Access Profile，GAP）

<a id="r_bt_5Fgatt"></a>

相关声明：[通用属性配置文件（Generic Attribute Profile，GATT）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html)。

通用属性配置文件（Generic Attribute Profile，GATT）

<a id="r_bt_5Fgoep"></a>

相关声明：[通用对象交换规范（Generic Object Exchange Profile，GOEP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html)。

通用对象交换规范（Generic Object Exchange Profile，GOEP）

<a id="r_hci_5Fraw"></a>

相关声明：[HCI 原始通道（RAW channel）](https://docs.zephyrproject.org/latest/doxygen/html/group__hci__raw.html)。

HCI 原始通道（RAW channel）

<a id="r_bt_5Fhfp"></a>

相关声明：[免提配置文件（Hands Free Profile，HFP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html)。

免提配置文件（Hands Free Profile，HFP）

<a id="r_bt_5Fhfp_5Fag"></a>

相关声明：[免提配置文件——音频网关（Hands Free Profile - Audio Gateway，HFP-AG）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html)。

免提配置文件——音频网关（Hands Free Profile - Audio Gateway，HFP-AG）

<a id="r_bt_5Fhas"></a>

相关声明：[助听接入服务（Hearing Access Service，HAS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html)。

助听接入服务（Hearing Access Service，HAS）

<a id="r_bt_5Fhrs"></a>

相关声明：[心率服务（Heart Rate Service，HRS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hrs.html)。

心率服务（Heart Rate Service，HRS）

<a id="r_bt_5Fias"></a>

相关声明：[即时警报服务（Immediate Alert Service，IAS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html)。

即时警报服务（Immediate Alert Service，IAS）

<a id="r_bt_5Fobex"></a>

相关声明：[IrDA 对象交换协议（Object Exchange Protocol，OBEX）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html)。

IrDA 对象交换协议（Object Exchange Protocol，OBEX）

<a id="r_bt_5Fiso"></a>

相关声明：[等时通道（Isochronous channels，ISO）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html)。

等时通道（Isochronous channels，ISO）

<a id="r_bt_5Fl2cap"></a>

相关声明：[逻辑链路控制与适配协议（L2CAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html)。

逻辑链路控制与适配协议（L2CAP）

<a id="r_bt_5Fmcc"></a>

相关声明：[媒体控制客户端（Media Control Client，MCC）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html)。

蓝牙媒体控制客户端（Media Control Client，MCC）接口。

<a id="r_bt_5Fmcs"></a>

相关声明：[媒体控制服务（Media Control Service，MCS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html)。

媒体控制服务（Media Control Service，MCS）

<a id="r_bt_5Fmedia_5Fproxy"></a>

相关声明：[媒体代理（Media Proxy）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html)。

媒体代理模块。

<a id="r_bt_5Fmap"></a>

相关声明：[消息访问配置文件（Message Access Profile，MAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html)。

消息访问配置文件（Message Access Profile，MAP）

<a id="r_bt_5Fmicp"></a>

相关声明：[麦克风控制配置文件（Microphone Control Profile，MICP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html)。

麦克风控制配置文件（Microphone Control Profile，MICP）

<a id="r_bt_5Fots"></a>

相关声明：[对象传输服务（Object Transfer Service，OTS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html)。

对象传输服务（Object Transfer Service，OTS）

<a id="r_bt_5Fpbap"></a>

相关声明：[电话簿访问配置文件（Phone Book Access Profile，PBAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html)。

电话簿访问配置文件（Phone Book Access Profile，PBAP）

<a id="r_bt_5Fpbp"></a>

相关声明：[公共广播配置文件（Public Broadcast Profile，PBP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html)。

公共广播配置文件（Public Broadcast Profile，PBP）

<a id="r_bt_5Fpacs"></a>

相关声明：[已发布音频能力服务（Published Audio Capabilities Service，PACS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html)。

已发布音频能力服务（Published Audio Capabilities Service，PACS）

<a id="r_bt_5Frfcomm"></a>

相关声明：[RFCOMM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html)。

RFCOMM

<a id="r_bt_5Fsdp"></a>

相关声明：[服务发现协议（Service Discovery Protocol，SDP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html)。

<a id="r_bt_5Ftbs"></a>

相关声明：[电话承载服务（Telephone Bearer Service，TBS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html)。

电话承载服务（Telephone Bearer Service，TBS）

<a id="r_bt_5Ftmap"></a>

相关声明：[电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html)。

电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）

<a id="r_bt_5Fuuid"></a>

相关声明：[通用唯一标识符（UUIDs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html)。

通用唯一标识符（UUIDs）

<a id="r_bt_5Fvcp"></a>

相关声明：[音量控制配置文件（Volume Control Profile，VCP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html)。

音量控制配置文件（Volume Control Profile，VCP）

<a id="r_bt_5Fvocs"></a>

相关声明：[音量偏移控制服务（Volume Offset Control Service，VOCS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html)。

音量偏移控制服务（Volume Offset Control Service，VOCS）


## 3.2\_原页交叉引用（Cross References）

- [高级音频分发配置文件（Advanced Audio Distribution Profile，A2DP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__a2dp.html)
- [警报通知服务（Alert Notification Service，ANS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ans.html)
- [分配编号（Assigned Numbers）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers.html)
- [属性协议（Attribute Protocol，ATT）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html)
- [音频输入控制服务（Audio Input Control Service，AICS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html)
- [音频流控制服务（Audio Stream Control Service，ASCS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ascs.html)
- [音频/视频远程控制配置文件（Audio Video Remote Control Profile，AVRCP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__avrcp.html)
- [基本音频配置文件（Basic Audio Profile，BAP）的 LC3 预设](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap__lc3__preset.html)
- [基本成像配置文件（Basic Imaging Profile，BIP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bip.html)
- [电池服务（Battery Service，BAS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bas.html)
- [BlueNRG HCI 驱动扩展 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bluenrg__hci__driver.html)
- [蓝牙音频（Bluetooth Audio）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__audio.html)
- [蓝牙基本音频配置文件（Bluetooth Basic Audio Profile）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__bap.html)
- [蓝牙内容控制标识符（Bluetooth Content Control Identifier）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ccid.html)
- [蓝牙控制器（Bluetooth Controller）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ctrl.html)
- [蓝牙游戏音频配置文件（Bluetooth Gaming Audio Profile）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap.html)
- [蓝牙主机控制器接口（Bluetooth HCI）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__api.html)
- [蓝牙HCI数据包辅助接口（Packet Helpers）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hci__pkt.html)
- [蓝牙人机接口设备（Bluetooth HID）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid.html)
- [蓝牙 HID 设备（Device）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__device.html)
- [蓝牙 HID 主机（Host）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hid__host.html)
- [蓝牙 LC3 编解码器（Bluetooth LC3 codec）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__lc3.html)
- [用于基本速率/增强数据速率（BR/EDR）的蓝牙逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol，L2CAP）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap__br.html)
- [蓝牙网状网络（Bluetooth Mesh）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html)
- [字节序（Byte Order）。](../byteorder_reference/P003_蓝牙字节序辅助接口.md)
- [呼叫控制配置文件（Call Control Profile，CCP）](P004_呼叫控制配置文件（Call Control Profile，CCP）.md)
- [信道探测（Channel Sounding，CS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html)
- [通用音频配置文件（Common Audio Profile，CAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cap.html)
- [连接管理（Connection management）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__conn.html)
- [协调集标识配置文件（Coordinated Set Identification Profile，CSIP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__csip.html)
- [密码学（Cryptography）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__crypto.html)
- [当前时间服务（Current Time Service，CTS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__cts.html)
- [数据缓冲区（Data buffers）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html)
- [设备地址（Device Address）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__addr.html)
- [经过时间服务（Elapsed Time Service，ETS）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ets.html)
- [加密广播数据（Encrypted Advertising Data，EAD）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ead.html)
- [游戏音频配置文件（Gaming Audio Profile，GMAP）的 LC3 预设](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gmap__lc3__preset.html)
- [通用访问配置文件（Generic Access Profile，GAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gap.html)
- [通用属性配置文件（Generic Attribute Profile，GATT）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__gatt.html)
- [通用对象交换规范（Generic Object Exchange Profile，GOEP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__goep.html)
- [HCI 原始通道（RAW channel）](https://docs.zephyrproject.org/latest/doxygen/html/group__hci__raw.html)
- [免提配置文件（Hands Free Profile，HFP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp.html)
- [免提配置文件——音频网关（Hands Free Profile - Audio Gateway，HFP-AG）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hfp__ag.html)
- [助听接入服务（Hearing Access Service，HAS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__has.html)
- [心率服务（Heart Rate Service，HRS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__hrs.html)
- [即时警报服务（Immediate Alert Service，IAS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ias.html)
- [IrDA 对象交换协议（Object Exchange Protocol，OBEX）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__obex.html)
- [等时通道（Isochronous channels，ISO）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__iso.html)
- [逻辑链路控制与适配协议（L2CAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__l2cap.html)
- [媒体控制客户端（Media Control Client，MCC）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcc.html)
- [媒体控制服务（Media Control Service，MCS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mcs.html)
- [媒体代理（Media Proxy）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__media__proxy.html)
- [消息访问配置文件（Message Access Profile，MAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__map.html)
- [麦克风控制配置文件（Microphone Control Profile，MICP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html)
- [对象传输服务（Object Transfer Service，OTS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html)
- [电话簿访问配置文件（Phone Book Access Profile，PBAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbap.html)
- [公共广播配置文件（Public Broadcast Profile，PBP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pbp.html)
- [已发布音频能力服务（Published Audio Capabilities Service，PACS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__pacs.html)
- [RFCOMM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__rfcomm.html)
- [服务发现协议（Service Discovery Protocol，SDP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__sdp.html)
- [电话承载服务（Telephone Bearer Service，TBS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tbs.html)
- [电话与媒体音频配置文件（Telephone and Media Audio Profile，TMAP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__tmap.html)
- [通用唯一标识符（UUIDs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__uuid.html)
- [音量控制配置文件（Volume Control Profile，VCP）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vcp.html)
- [音量偏移控制服务（Volume Offset Control Service，VOCS）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__vocs.html)

<a id="header-details"></a>

---

[上一章](P002_Aesc Silicon 时钟域标识符（Clock domain identifiers）.md) · [返回大纲](大纲.md) · [下一章](P004_呼叫控制配置文件（Call Control Profile，CCP）.md)
