---
id: learning.zephyr-docs.api-socket-lora-topic-reference.page-3
title: 分配编号（Assigned Numbers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_分配编号（Assigned Numbers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙分配编号（Bluetooth Assigned Numbers）、代码和标识符。

<a id="details"></a>

蓝牙已分配编号、代码和标识符（Bluetooth Assigned Numbers, Codes and Identifiers）。起始版本（Since）：1.0。版本（Version）：1.0.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 3.1\_主题（Topics）

<a id="r_bt_5Fassigned_5Fnumbers_5Fmesh"></a>

相关声明：[蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md)。

蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）

<a id="r_bt_5Fassigned_5Fnumbers_5Fcore"></a>

相关声明：[核心规范分配编号（Core Specification Assigned Numbers）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html)。

核心规范分配编号（Core Specification Assigned Numbers）

<a id="r_bt_5Fassigned_5Fnumbers_5Faudio"></a>

相关声明：[通用音频分配编号（Generic Audio Assigned Numbers）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html)。

通用音频分配编号（Generic Audio Assigned Numbers）

<a id="header-member-group"></a>
<a id="member-group"></a>

## 3.2\_公司标识符（Company Identifiers，参见 Bluetooth Assigned Numbers）

<a id="r_ga6bbf21c05f24d2c2c710be9bcf05af5f"></a>

```c
#define BT_COMP_ID_LF 0x05f1
```

相关声明：[BT_COMP_ID_LF](#ga6bbf21c05f24d2c2c710be9bcf05af5f)。

Linux 基金会（The Linux Foundation）。

## 3.3\_已定义的基本速率设备类别值（Defined BR Class of Device (CoD) values）

<a id="r_gaa8793a9bc39bf833124c8c961e441a43"></a>

```c
#define BT_COD(major_service, major_device, minor_device)
```

相关声明：[BT_COD](#gaa8793a9bc39bf833124c8c961e441a43)。

<a id="r_gaf2c925e431eec42930101a72b00a7283"></a>

```c
#define BT_COD_VALID(cod)
```

相关声明：[BT_COD_VALID](#gaf2c925e431eec42930101a72b00a7283)。

<a id="r_gab598bdad77874748f74187aa32049ea6"></a>

```c
#define BT_COD_MAJOR_SERVICE_CLASSES(cod)
```

相关声明：[BT_COD_MAJOR_SERVICE_CLASSES](#gab598bdad77874748f74187aa32049ea6)。

<a id="r_ga129895b48ad9071017a2e97335ec6d2b"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS(cod)
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS](#ga129895b48ad9071017a2e97335ec6d2b)。

<a id="r_gadcf892b98d0924ea8a78d4b8b588bddb"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS(cod)
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS](#gadcf892b98d0924ea8a78d4b8b588bddb)。

## 3.4\_主服务类别（Major Service Classes）

<a id="r_ga01883ae9792f486644dc96dd0559c72d"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_LIMITED_DISCOVER BIT(13)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_LIMITED_DISCOVER](#ga01883ae9792f486644dc96dd0559c72d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

有限可发现模式服务类别（Limited Discoverable Mode service class）。

<a id="r_ga031275c4187717b7556c4f0a7e16126a"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_LE_AUDIO BIT(14)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_LE_AUDIO](#ga031275c4187717b7556c4f0a7e16126a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

低功耗音频服务类别（LE Audio service class）。

<a id="r_ga18cbe8ede63ed6c3396aabf01c97c672"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_RESERVED BIT(15)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_RESERVED](#ga18cbe8ede63ed6c3396aabf01c97c672)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

保留服务类别（Reserved service class）。

<a id="r_ga9fa4505b17dc53c22c9ac3fde9743e29"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_POSITIONING BIT(16)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_POSITIONING](#ga9fa4505b17dc53c22c9ac3fde9743e29)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

定位服务类别（Positioning service class）。

<a id="r_ga262412d5459d96d7f64a3d13db4906d2"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_NETWORKING BIT(17)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_NETWORKING](#ga262412d5459d96d7f64a3d13db4906d2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

联网服务类别（Networking service class）。

<a id="r_ga6f959f962a9054102b4bbfe5b7248dd5"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_RENDERING BIT(18)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_RENDERING](#ga6f959f962a9054102b4bbfe5b7248dd5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

呈现服务类别（Rendering service class）。

<a id="r_ga35cd970ddcba07d98e9e42863ee155f9"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_CAPTURING BIT(19)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_CAPTURING](#ga35cd970ddcba07d98e9e42863ee155f9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

采集服务类别（Capturing service class）。

<a id="r_ga17cf278f25d45040991ef2d60dafb456"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_OBJECT_TRANSFER BIT(20)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_OBJECT_TRANSFER](#ga17cf278f25d45040991ef2d60dafb456)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

对象传输服务类别（Object Transfer service class）。

<a id="r_ga2c70ab983a099e74a89aaaff02c086d0"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_AUDIO BIT(21)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_AUDIO](#ga2c70ab983a099e74a89aaaff02c086d0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

音频服务类别（Audio service class）。

<a id="r_ga2bca689e747d06869b3e86dbe7e10253"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_TELEPHONY BIT(22)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_TELEPHONY](#ga2bca689e747d06869b3e86dbe7e10253)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

电话服务类别（Telephony service class）。

<a id="r_gafb44e9944c2f84d45d448975c1ab0300"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_INFORMATION BIT(23)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_INFORMATION](#gafb44e9944c2f84d45d448975c1ab0300)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

信息服务类别（Information service class）。

## 3.5\_主设备类别（Major Device Class）

<a id="r_ga9e57c7be37bc489c6ec4e35bf26e5718"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_MISCELLANEOUS 0x00
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_MISCELLANEOUS](#ga9e57c7be37bc489c6ec4e35bf26e5718)。

杂项主设备类别（Miscellaneous major device class）。

<a id="r_ga41f24363507a81975e1a1de8068bcd86"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_COMPUTER 0x01
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_COMPUTER](#ga41f24363507a81975e1a1de8068bcd86)。

计算机主设备类别（Computer major device class）。

<a id="r_gaf4e20997428ae008b48f1eee3f150633"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_PHONE 0x02
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_PHONE](#gaf4e20997428ae008b48f1eee3f150633)。

电话主设备类别（Phone major device class）。

<a id="r_ga341edcc0340d6d2d5ba3c76beeab1c93"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_LAN_NETWORK 0x03
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_LAN_NETWORK](#ga341edcc0340d6d2d5ba3c76beeab1c93)。

局域网／网络接入点主设备类别（LAN/Network Access Point major device class）。

<a id="r_ga88281290c9641477d5e19b321f489e85"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_AUDIO_VIDEO 0x04
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_AUDIO_VIDEO](#ga88281290c9641477d5e19b321f489e85)。

音频／视频主设备类别（Audio/Video major device class）。

<a id="r_ga71cb552a1ba251492456a3862a70321b"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_PERIPHERAL 0x05
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_PERIPHERAL](#ga71cb552a1ba251492456a3862a70321b)。

外设主设备类别（Peripheral major device class）。

<a id="r_gabd6b43f20dba80d46238567f8026a405"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_IMAGING 0x06
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_IMAGING](#gabd6b43f20dba80d46238567f8026a405)。

成像主设备类别（Imaging major device class）。

<a id="r_ga832d46c3654018a272f167e8d2f028c2"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_WEARABLE 0x07
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_WEARABLE](#ga832d46c3654018a272f167e8d2f028c2)。

可穿戴主设备类别（Wearable major device class）。

<a id="r_ga6af01f93fadb4ded2c0e7d74acdfa9a2"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_TOY 0x08
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_TOY](#ga6af01f93fadb4ded2c0e7d74acdfa9a2)。

玩具主设备类别（Toy major device class）。

<a id="r_ga7493589ba4918239c7714b12f4044c48"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_HEALTH 0x09
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_HEALTH](#ga7493589ba4918239c7714b12f4044c48)。

健康主设备类别（Health major device class）。

<a id="r_ga81690fb90860176fc17fed8625fed486"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_UNCATEGORIZED 0x1F
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_UNCATEGORIZED](#ga81690fb90860176fc17fed8625fed486)。

未分类的主设备类别（Uncategorized major device class）。

## 3.6\_次设备类别：计算机主类别（Minor Device Class - Computer Major Class）

<a id="r_ga47d7e27a9da20b27c0483ab50db3590d"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_UNCATEGORIZED 0x00
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_COMPUTER_UNCATEGORIZED](#ga47d7e27a9da20b27c0483ab50db3590d)。

未分类的计算机次设备类别（Uncategorized computer minor device class）。

<a id="r_gae1a285e3787132a97edf7adb53963880"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_DESKTOP_WORKSTATION 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_COMPUTER_DESKTOP_WORKSTATION](#gae1a285e3787132a97edf7adb53963880)。

台式工作站计算机次设备类别（Desktop workstation computer minor device class）。

<a id="r_ga6d009b3670bfa0de1ed30c2ec87f8918"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_SERVER 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_COMPUTER_SERVER](#ga6d009b3670bfa0de1ed30c2ec87f8918)。

服务器级计算机次设备类别（Server-class computer minor device class）。

<a id="r_ga60f70b01f651baab797b79ee5c7b94aa"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_LAPTOP 0x03
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_COMPUTER_LAPTOP](#ga60f70b01f651baab797b79ee5c7b94aa)。

笔记本计算机次设备类别（Laptop computer minor device class）。

<a id="r_gad8af957eeafefca10f2538b2e09c7bd3"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_HANDHELD_PC_PDA 0x04
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_COMPUTER_HANDHELD_PC_PDA](#gad8af957eeafefca10f2538b2e09c7bd3)。

手持 PC／个人数字助理计算机次设备类别（Handheld PC/PDA computer minor device class）。

<a id="r_gab5eb08bfa138cbfd55ffa2774a38fd9f"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_PALM_SIZED_PC_PDA 0x05
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_COMPUTER_PALM_SIZED_PC_PDA](#gab5eb08bfa138cbfd55ffa2774a38fd9f)。

掌上 PC／个人数字助理计算机次设备类别（Palm-sized PC/PDA computer minor device class）。

<a id="r_gaec2dc76edfa8a7edc6ce990be1658e54"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_WEARABLE_COMPUTER 0x06
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_COMPUTER_WEARABLE_COMPUTER](#gaec2dc76edfa8a7edc6ce990be1658e54)。

可穿戴计算机次设备类别（Wearable computer minor device class）。

<a id="r_ga0a98088245313a02c7dfbfdb39784632"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_TABLET 0x07
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_COMPUTER_TABLET](#ga0a98088245313a02c7dfbfdb39784632)。

平板计算机次设备类别（Tablet computer minor device class）。

## 3.7\_次设备类别：电话主类别（Minor Device Class - Phone Major Class）

<a id="r_ga86dd6474cad2c148c4bf2273707f3bca"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_UNCATEGORIZED 0x00
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PHONE_UNCATEGORIZED](#ga86dd6474cad2c148c4bf2273707f3bca)。

未分类的电话次设备类别（Uncategorized phone minor device class）。

<a id="r_gaf3796e468def379157c2cf02a356b578"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_CELLULAR 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PHONE_CELLULAR](#gaf3796e468def379157c2cf02a356b578)。

蜂窝电话次设备类别（Cellular phone minor device class）。

<a id="r_gacce21d82143f430ff2bac1608b42b7e1"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_CORDLESS 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PHONE_CORDLESS](#gacce21d82143f430ff2bac1608b42b7e1)。

无绳电话次设备类别（Cordless phone minor device class）。

<a id="r_gad74d69e9ec7a82b128df0a6ad33bfc65"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_SMARTPHONE 0x03
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PHONE_SMARTPHONE](#gad74d69e9ec7a82b128df0a6ad33bfc65)。

智能手机次设备类别（Smartphone minor device class）。

<a id="r_ga708f325406d16fbcb96f0a311ad6f12f"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_WIRED_MODEM 0x04
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PHONE_WIRED_MODEM](#ga708f325406d16fbcb96f0a311ad6f12f)。

有线调制解调器或语音网关电话次设备类别（Wired modem or voice gateway phone minor device class）。

<a id="r_gad711cb8a9d53d428f4aef9da0605c27e"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_COMMON_ISDN_ACCESS 0x05
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PHONE_COMMON_ISDN_ACCESS](#gad711cb8a9d53d428f4aef9da0605c27e)。

通用综合业务数字网接入电话次设备类别（Common ISDN access phone minor device class）。

## 3.8\_次设备类别：局域网／网络主类别：服务利用率（Minor Device Class - LAN/Network Major Class - Service Utilization）

<a id="r_gacf4f30af8af17254d8557c2102e82930"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_FULLY_AVAILABLE 0x00
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_FULLY_AVAILABLE](#gacf4f30af8af17254d8557c2102e82930)。

局域网服务利用率：完全可用（LAN service utilization: fully available）。

<a id="r_gaa48c789f29f33b7f129bbd593ab336fe"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_1_17_UTILIZED 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_1_17_UTILIZED](#gaa48c789f29f33b7f129bbd593ab336fe)。

局域网服务利用率：已使用 1–17%（LAN service utilization: 1-17% utilized）。

<a id="r_gab19bf6c95fbe0d3aa4923323b67c2f0c"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_17_33_UTILIZED 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_17_33_UTILIZED](#gab19bf6c95fbe0d3aa4923323b67c2f0c)。

局域网服务利用率：已使用 17–33%（LAN service utilization: 17-33% utilized）。

<a id="r_ga17e2dd35fb4fd37f45757515a03df565"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_33_50_UTILIZED 0x03
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_33_50_UTILIZED](#ga17e2dd35fb4fd37f45757515a03df565)。

局域网服务利用率：已使用 33–50%（LAN service utilization: 33-50% utilized）。

<a id="r_gaecb741bfc498bacfbd4c9059b3551e2f"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_50_67_UTILIZED 0x04
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_50_67_UTILIZED](#gaecb741bfc498bacfbd4c9059b3551e2f)。

局域网服务利用率：已使用 50–67%（LAN service utilization: 50-67% utilized）。

<a id="r_gaf296fcfd14235a0762a4565ff265e6be"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_67_83_UTILIZED 0x05
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_67_83_UTILIZED](#gaf296fcfd14235a0762a4565ff265e6be)。

局域网服务利用率：已使用 67–83%（LAN service utilization: 67-83% utilized）。

<a id="r_ga7a740756ba4dbc8770f4cdf5af2d1fa5"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_83_99_UTILIZED 0x06
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_83_99_UTILIZED](#ga7a740756ba4dbc8770f4cdf5af2d1fa5)。

局域网服务利用率：已使用 83–99%（LAN service utilization: 83-99% utilized）。

<a id="r_gafb3f26abffdd158cfd117aefa06a31bb"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_NO_SERVICE_AVAILABLE 0x07
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_NO_SERVICE_AVAILABLE](#gafb3f26abffdd158cfd117aefa06a31bb)。

局域网服务利用率：无可用服务（LAN service utilization: no service available）。

## 3.9\_次设备类别：局域网／网络主类别：设备类型（Minor Device Class - LAN/Network Major Class - Device Type）

<a id="r_gab4af4c15266ce0f24f2f61d0578f346a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_DEVICE_TYPE_UNCATEGORIZED 0x00
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_DEVICE_TYPE_UNCATEGORIZED](#gab4af4c15266ce0f24f2f61d0578f346a)。

未分类的局域网／网络设备类型（Uncategorized LAN/network device type）。

<a id="r_ga245357d925ffde5ce1d7d038bd661097"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_UNCATEGORIZED 0x00
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_UNCATEGORIZED](#ga245357d925ffde5ce1d7d038bd661097)。

次设备类别：音频／视频主类别（Minor Device Class - Audio/Video Major Class）。

<a id="r_gaa79054d26b530834da97412ffc6a6d76"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_WEARABLE_HEADSET 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_WEARABLE_HEADSET](#gaa79054d26b530834da97412ffc6a6d76)。

可穿戴耳麦音频／视频次设备类别（Wearable headset audio/video minor device class）。

<a id="r_gaea20dcaaf0dcf2914b1ede0e657ad233"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HANDSFREE 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HANDSFREE](#gaea20dcaaf0dcf2914b1ede0e657ad233)。

免提音频／视频次设备类别（Handsfree audio/video minor device class）。

<a id="r_ga6c71bd324c442918d05b2ba176549f78"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_MICROPHONE 0x04
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_MICROPHONE](#ga6c71bd324c442918d05b2ba176549f78)。

麦克风音频／视频次设备类别（Microphone audio/video minor device class）。

<a id="r_ga419c36342136f5ea827d2889ed666d4c"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_LOUDSPEAKER 0x05
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_LOUDSPEAKER](#ga419c36342136f5ea827d2889ed666d4c)。

扬声器音频／视频次设备类别（Loudspeaker audio/video minor device class）。

<a id="r_ga6adf41d4cadabdca21bb1191ae0951f5"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HEADPHONES 0x06
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HEADPHONES](#ga6adf41d4cadabdca21bb1191ae0951f5)。

耳机音频／视频次设备类别（Headphones audio/video minor device class）。

<a id="r_gac50804ea808e6e83686ad973d187bf9d"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_PORTABLE_AUDIO 0x07
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_PORTABLE_AUDIO](#gac50804ea808e6e83686ad973d187bf9d)。

便携音频设备的音频／视频次设备类别（Portable audio audio/video minor device class）。

<a id="r_ga8f60c01b2da107da93e8b873b03be337"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_CAR_AUDIO 0x08
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_CAR_AUDIO](#ga8f60c01b2da107da93e8b873b03be337)。

汽车音响的音频／视频次设备类别（Car audio audio/video minor device class）。

<a id="r_ga3a7182ce71c7ae49330475c0093e7665"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_SETTOP_BOX 0x09
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_SETTOP_BOX](#ga3a7182ce71c7ae49330475c0093e7665)。

机顶盒音频／视频次设备类别（Set-top box audio/video minor device class）。

<a id="r_ga7ec413fa38b2e0ddcdb0cacfb9565d2a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HIFI_AUDIO 0x0A
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HIFI_AUDIO](#ga7ec413fa38b2e0ddcdb0cacfb9565d2a)。

高保真音响的音频／视频次设备类别（HiFi audio audio/video minor device class）。

<a id="r_gafa6100bcc07e04e7177b34336a523c6a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VCR 0x0B
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VCR](#gafa6100bcc07e04e7177b34336a523c6a)。

录像机音频／视频次设备类别（VCR audio/video minor device class）。

<a id="r_ga4ee160425ba1d2fa7f7ab9f360eb51ea"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_CAMERA 0x0C
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_CAMERA](#ga4ee160425ba1d2fa7f7ab9f360eb51ea)。

视频摄像机音频／视频次设备类别（Video camera audio/video minor device class）。

<a id="r_ga9cb9ddf5ac2d9e132b1504bb35fba5e7"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_CAMCORDER 0x0D
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_CAMCORDER](#ga9cb9ddf5ac2d9e132b1504bb35fba5e7)。

便携式摄录机音频／视频次设备类别（Camcorder audio/video minor device class）。

<a id="r_ga7bb6a3801475a076153529859d607254"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_MONITOR 0x0E
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_MONITOR](#ga7bb6a3801475a076153529859d607254)。

视频监视器音频／视频次设备类别（Video monitor audio/video minor device class）。

<a id="r_ga5a20841438980c2fcf408974782c9f6e"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_DISPLAY_LOUDSPEAKER 0x0F
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_DISPLAY_LOUDSPEAKER](#ga5a20841438980c2fcf408974782c9f6e)。

视频显示器与扬声器音频／视频次设备类别（Video display and loudspeaker audio/video minor device class）。

<a id="r_ga07f3ddf991a1de0ef1a5e4bc80f87ae9"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_CONFERENCING 0x10
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_CONFERENCING](#ga07f3ddf991a1de0ef1a5e4bc80f87ae9)。

视频会议音频／视频次设备类别（Video conferencing audio/video minor device class）。

<a id="r_ga67798be9a45da9d23993851dc47b8015"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_GAMING_TOY 0x12
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_GAMING_TOY](#ga67798be9a45da9d23993851dc47b8015)。

游戏玩具音频／视频次设备类别（Gaming toy audio/video minor device class）。

## 3.10\_次设备类别：外设主类别：输入设备类型（Minor Device Class - Peripheral Major Class - Input Device Type）

<a id="r_ga4b48d9b5ef8fdddd11f1cb528e826d79"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_NO_KEYBOARD_NO_POINTING 0x00
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_NO_KEYBOARD_NO_POINTING](#ga4b48d9b5ef8fdddd11f1cb528e826d79)。

外设输入：无键盘，无指点设备（Peripheral input: no keyboard, no pointing device）。

<a id="r_gab648e64338834e0f986415603a7ee01a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_KEYBOARD 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_KEYBOARD](#gab648e64338834e0f986415603a7ee01a)。

外设输入：键盘（Peripheral input: keyboard）。

<a id="r_ga71c43b86fa8d01d45d11bea0bb56ee63"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_POINTING_DEVICE 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_POINTING_DEVICE](#ga71c43b86fa8d01d45d11bea0bb56ee63)。

外设输入：指点设备（Peripheral input: pointing device）。

<a id="r_ga4c26cacb0efe86dd586cacb48f7f9798"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_COMBO_KEYBOARD_POINTING 0x03
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_COMBO_KEYBOARD_POINTING](#ga4c26cacb0efe86dd586cacb48f7f9798)。

外设输入：键盘与指点设备组合（Peripheral input: combo keyboard and pointing device）。

## 3.11\_次设备类别：外设主类别：设备类型（Minor Device Class - Peripheral Major Class - Device Type）

<a id="r_gadd57844cdd2d6ff59ea8371b64c0786a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_UNCATEGORIZED 0x00
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_UNCATEGORIZED](#gadd57844cdd2d6ff59ea8371b64c0786a)。

未分类的外设设备类型（Uncategorized peripheral device type）。

<a id="r_gae7ceeea12447c03b901704165f815d2a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_JOYSTICK 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_JOYSTICK](#gae7ceeea12447c03b901704165f815d2a)。

操纵杆外设设备类型（Joystick peripheral device type）。

<a id="r_gaae4e0e78d28b915f7be42640aab41802"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_GAMEPAD 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_GAMEPAD](#gaae4e0e78d28b915f7be42640aab41802)。

游戏手柄外设设备类型（Gamepad peripheral device type）。

<a id="r_ga55dc4b9ce33c7254ade2b32124bd5a52"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_REMOTE_CONTROL 0x03
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_REMOTE_CONTROL](#ga55dc4b9ce33c7254ade2b32124bd5a52)。

遥控器外设设备类型（Remote control peripheral device type）。

<a id="r_ga6115e1fc2619c95bcf7a50e657347c8b"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_SENSING_DEVICE 0x04
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_SENSING_DEVICE](#ga6115e1fc2619c95bcf7a50e657347c8b)。

传感设备外设类型（Sensing device peripheral device type）。

<a id="r_ga8b21b9c98bb8ec187bb7be661c875048"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_DIGITIZER_TABLET 0x05
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_DIGITIZER_TABLET](#ga8b21b9c98bb8ec187bb7be661c875048)。

数字化绘图板外设设备类型（Digitizer tablet peripheral device type）。

<a id="r_ga8b23f0432923353c1425244780c2cd4a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_CARD_READER 0x06
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_CARD_READER](#ga8b23f0432923353c1425244780c2cd4a)。

读卡器外设设备类型（Card reader peripheral device type）。

<a id="r_ga7a8bec17a83efabcf83a3a0848fbd286"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_DIGITAL_PEN 0x07
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_DIGITAL_PEN](#ga7a8bec17a83efabcf83a3a0848fbd286)。

数字笔外设设备类型（Digital pen peripheral device type）。

<a id="r_ga3cff5d97f27e3725217f332dbd1e15ef"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_HANDHELD_SCANNER 0x08
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_HANDHELD_SCANNER](#ga3cff5d97f27e3725217f332dbd1e15ef)。

手持扫描仪外设设备类型（Handheld scanner peripheral device type）。

<a id="r_ga2e603791c7467731fcd8e5ef521405fc"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_HANDHELD_GESTURAL_INPUT 0x09
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_HANDHELD_GESTURAL_INPUT](#ga2e603791c7467731fcd8e5ef521405fc)。

手持手势输入外设设备类型（Handheld gestural input peripheral device type）。

## 3.12\_次设备类别：成像主类别（Minor Device Class - Imaging Major Class）。

<a id="r_gaeb931c305948fa843853f9f418c71d45"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_DISPLAY 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_IMAGING_DISPLAY](#gaeb931c305948fa843853f9f418c71d45)。

次设备类别：成像主类别（Minor Device Class - Imaging Major Class）。

<a id="r_ga238b06f556138d4bab338ff1375a1021"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_CAMERA 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_IMAGING_CAMERA](#ga238b06f556138d4bab338ff1375a1021)。

成像相机设备（Imaging camera device）。

<a id="r_ga6eb468819358a83906f40f2f64c344ae"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_SCANNER 0x04
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_IMAGING_SCANNER](#ga6eb468819358a83906f40f2f64c344ae)。

成像扫描仪设备（Imaging scanner device）。

<a id="r_gaf6a4be11446739a2aede1adf4d4fda77"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_PRINTER 0x08
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_IMAGING_PRINTER](#gaf6a4be11446739a2aede1adf4d4fda77)。

成像打印机设备（Imaging printer device）。

<a id="r_ga5010b99a3111775447ac89f169d824af"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_UNCATEGORIZED 0x00
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_IMAGING_UNCATEGORIZED](#ga5010b99a3111775447ac89f169d824af)。

次设备类别：成像主类别中的未分类设备（Minor Device Class - Imaging Major Class Uncategorized）。

## 3.13\_次设备类别：可穿戴主类别（Minor Device Class - Wearable Major Class）

<a id="r_gae879842e986be1f78b1a6afdd06f267e"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_HEADSET 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_WEARABLE_HEADSET](#gae879842e986be1f78b1a6afdd06f267e)。

可穿戴耳麦设备（Wearable headset device）。

<a id="r_ga2c68dc5a8fe4252bc2c743f05f9d4e96"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_PAGER 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_WEARABLE_PAGER](#ga2c68dc5a8fe4252bc2c743f05f9d4e96)。

可穿戴寻呼机设备（Wearable pager device）。

<a id="r_ga9a7d4d0b3645f38a9888beb2ec994fe1"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_JACKET 0x03
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_WEARABLE_JACKET](#ga9a7d4d0b3645f38a9888beb2ec994fe1)。

可穿戴夹克设备（Wearable jacket device）。

<a id="r_ga091efe28aab4b90f3552d56704b2a886"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_HELMET 0x04
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_WEARABLE_HELMET](#ga091efe28aab4b90f3552d56704b2a886)。

可穿戴头盔设备（Wearable helmet device）。

<a id="r_gaea4e865414b40d9b370951a328dc0c36"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_GLASSES 0x05
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_WEARABLE_GLASSES](#gaea4e865414b40d9b370951a328dc0c36)。

可穿戴眼镜设备（Wearable glasses device）。

## 3.14\_次设备类别：玩具主类别（Minor Device Class - Toy Major Class）

<a id="r_gaf527b4a6353fc0e110033f1661342a80"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_TOY_ROBOT 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_TOY_ROBOT](#gaf527b4a6353fc0e110033f1661342a80)。

玩具机器人设备（Toy robot device）。

<a id="r_ga236dedbc75b174d221173080e734227e"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_TOY_VEHICLE 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_TOY_VEHICLE](#ga236dedbc75b174d221173080e734227e)。

玩具车辆设备（Toy vehicle device）。

<a id="r_gaf22179ae786663d350c7dfa9a25671b0"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_TOY_DOLL 0x03
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_TOY_DOLL](#gaf22179ae786663d350c7dfa9a25671b0)。

玩具娃娃设备（Toy doll device）。

<a id="r_gae51ab020f0a58a7468e79b33cf5888d2"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_TOY_CONTROLLER 0x04
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_TOY_CONTROLLER](#gae51ab020f0a58a7468e79b33cf5888d2)。

玩具控制器设备（Toy controller device）。

<a id="r_ga4305ed742e35f7d21d97d6ca8a228776"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_TOY_GAME 0x05
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_TOY_GAME](#ga4305ed742e35f7d21d97d6ca8a228776)。

玩具游戏设备（Toy game device）。

## 3.15\_次设备类别：健康主类别（Minor Device Class - Health Major Class）

<a id="r_ga98a4f1577322dd14790bda9ce8b28661"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_UNDEFINED 0x00
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_UNDEFINED](#ga98a4f1577322dd14790bda9ce8b28661)。

未定义的健康设备（Undefined health device）。

<a id="r_gadc1ba5de00271e2663dc52770acbf1f1"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_BLOOD_PRESSURE_MONITOR 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_BLOOD_PRESSURE_MONITOR](#gadc1ba5de00271e2663dc52770acbf1f1)。

血压监测健康设备（Blood pressure monitor health device）。

<a id="r_ga60998708af979e1c02d8a0d6373500c8"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_THERMOMETER 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_THERMOMETER](#ga60998708af979e1c02d8a0d6373500c8)。

温度计健康设备（Thermometer health device）。

<a id="r_ga8c6cb016bdd1a5f50258c671f7528f8e"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_WEIGHING_SCALE 0x03
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_WEIGHING_SCALE](#ga8c6cb016bdd1a5f50258c671f7528f8e)。

体重秤健康设备（Weighing scale health device）。

<a id="r_ga5c9e6a84ff76bfc8c12750e9b133861a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_GLUCOSE_METER 0x04
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_GLUCOSE_METER](#ga5c9e6a84ff76bfc8c12750e9b133861a)。

血糖仪健康设备（Glucose meter health device）。

<a id="r_gabe9f5e78c7321d8a2ff1752fe41d124d"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_PULSE_OXIMETER 0x05
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_PULSE_OXIMETER](#gabe9f5e78c7321d8a2ff1752fe41d124d)。

脉搏血氧仪健康设备（Pulse oximeter health device）。

<a id="r_ga94863d500f1a576eb3d818209196d12e"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_HEART_PULSE_MONITOR 0x06
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_HEART_PULSE_MONITOR](#ga94863d500f1a576eb3d818209196d12e)。

心率／脉搏监测健康设备（Heart/pulse monitor health device）。

<a id="r_gad6577d566fd17b126611583b4379ad01"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_HEALTH_DATA_DISPLAY 0x07
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_HEALTH_DATA_DISPLAY](#gad6577d566fd17b126611583b4379ad01)。

健康数据展示设备（Health data display device）。

<a id="r_ga6e50e1316332ba4e5da2fd81c6e65ef7"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_STEP_COUNTER 0x08
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_STEP_COUNTER](#ga6e50e1316332ba4e5da2fd81c6e65ef7)。

计步器健康设备（Step counter health device）。

<a id="r_gad34ed19a24a0b2a300b8e31c5a7ce798"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_BODY_COMPOSITION_ANALYZER 0x09
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_BODY_COMPOSITION_ANALYZER](#gad34ed19a24a0b2a300b8e31c5a7ce798)。

身体成分分析仪健康设备（Body composition analyzer health device）。

<a id="r_ga746b3b863fb6250cd990099b014f063f"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_PEAK_FLOW_MONITOR 0x0A
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_PEAK_FLOW_MONITOR](#ga746b3b863fb6250cd990099b014f063f)。

峰值流量监测健康设备（Peak flow monitor health device）。

<a id="r_ga4b376213b25611ff4bcf8cb7c7483a3a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_MEDICATION_MONITOR 0x0B
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_MEDICATION_MONITOR](#ga4b376213b25611ff4bcf8cb7c7483a3a)。

用药监测健康设备（Medication monitor health device）。

<a id="r_gaabd014dab3f24d38b8aabda2ae7e5ff4"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_KNEE_PROSTHESIS 0x0C
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_KNEE_PROSTHESIS](#gaabd014dab3f24d38b8aabda2ae7e5ff4)。

膝关节假体健康设备（Knee prosthesis health device）。

<a id="r_ga25315720692627e093a25df80d5b487d"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_ANKLE_PROSTHESIS 0x0D
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_ANKLE_PROSTHESIS](#ga25315720692627e093a25df80d5b487d)。

踝关节假体健康设备（Ankle prosthesis health device）。

<a id="r_ga308d6b8f3ed8cefccbca002ede932218"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_GENERIC_HEALTH_MANAGER 0x0E
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_GENERIC_HEALTH_MANAGER](#ga308d6b8f3ed8cefccbca002ede932218)。

通用健康管理器设备（Generic health manager device）。

<a id="r_ga5fd6e3a6703d961259bd563ca6379c9a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_PERSONAL_MOBILITY_DEVICE 0x0F
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_PERSONAL_MOBILITY_DEVICE](#ga5fd6e3a6703d961259bd563ca6379c9a)。

个人移动辅助健康设备（Personal mobility health device）。

## 3.16\_详细说明（Detailed Documentation）

<a id="gaa8793a9bc39bf833124c8c961e441a43"></a>

### `BT_COD`

```c
#define BT_COD ( major_service, major_device, minor_device )
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

展开值（Value）：

```c
(((uint32_t)major_service << 13) | ((uint32_t)major_device << 8) |                         \
 ((uint32_t)minor_device << 2))
```

<a id="ga129895b48ad9071017a2e97335ec6d2b"></a>

### `BT_COD_MAJOR_DEVICE_CLASS`

```c
#define BT_COD_MAJOR_DEVICE_CLASS ( cod)
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

展开值（Value）：

```c
((((uint32_t)cod[1]) & 0x1FUL))
```

<a id="ga88281290c9641477d5e19b321f489e85"></a>

### `BT_COD_MAJOR_DEVICE_CLASS_AUDIO_VIDEO`

```c
#define BT_COD_MAJOR_DEVICE_CLASS_AUDIO_VIDEO 0x04
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

音频／视频主设备类别（Audio/Video major device class）。

<a id="ga41f24363507a81975e1a1de8068bcd86"></a>

### `BT_COD_MAJOR_DEVICE_CLASS_COMPUTER`

```c
#define BT_COD_MAJOR_DEVICE_CLASS_COMPUTER 0x01
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

计算机主设备类别（Computer major device class）。

<a id="ga7493589ba4918239c7714b12f4044c48"></a>

### `BT_COD_MAJOR_DEVICE_CLASS_HEALTH`

```c
#define BT_COD_MAJOR_DEVICE_CLASS_HEALTH 0x09
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

健康主设备类别（Health major device class）。

<a id="gabd6b43f20dba80d46238567f8026a405"></a>

### `BT_COD_MAJOR_DEVICE_CLASS_IMAGING`

```c
#define BT_COD_MAJOR_DEVICE_CLASS_IMAGING 0x06
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

成像主设备类别（Imaging major device class）。

<a id="ga341edcc0340d6d2d5ba3c76beeab1c93"></a>

### `BT_COD_MAJOR_DEVICE_CLASS_LAN_NETWORK`

```c
#define BT_COD_MAJOR_DEVICE_CLASS_LAN_NETWORK 0x03
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

局域网／网络接入点主设备类别（LAN/Network Access Point major device class）。

<a id="ga9e57c7be37bc489c6ec4e35bf26e5718"></a>

### `BT_COD_MAJOR_DEVICE_CLASS_MISCELLANEOUS`

```c
#define BT_COD_MAJOR_DEVICE_CLASS_MISCELLANEOUS 0x00
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

杂项主设备类别（Miscellaneous major device class）。

<a id="ga71cb552a1ba251492456a3862a70321b"></a>

### `BT_COD_MAJOR_DEVICE_CLASS_PERIPHERAL`

```c
#define BT_COD_MAJOR_DEVICE_CLASS_PERIPHERAL 0x05
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

外设主设备类别（Peripheral major device class）。

<a id="gaf4e20997428ae008b48f1eee3f150633"></a>

### `BT_COD_MAJOR_DEVICE_CLASS_PHONE`

```c
#define BT_COD_MAJOR_DEVICE_CLASS_PHONE 0x02
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

电话主设备类别（Phone major device class）。

<a id="ga6af01f93fadb4ded2c0e7d74acdfa9a2"></a>

### `BT_COD_MAJOR_DEVICE_CLASS_TOY`

```c
#define BT_COD_MAJOR_DEVICE_CLASS_TOY 0x08
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

玩具主设备类别（Toy major device class）。

<a id="ga81690fb90860176fc17fed8625fed486"></a>

### `BT_COD_MAJOR_DEVICE_CLASS_UNCATEGORIZED`

```c
#define BT_COD_MAJOR_DEVICE_CLASS_UNCATEGORIZED 0x1F
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

未分类的主设备类别（Uncategorized major device class）。

<a id="ga832d46c3654018a272f167e8d2f028c2"></a>

### `BT_COD_MAJOR_DEVICE_CLASS_WEARABLE`

```c
#define BT_COD_MAJOR_DEVICE_CLASS_WEARABLE 0x07
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

可穿戴主设备类别（Wearable major device class）。

<a id="gab598bdad77874748f74187aa32049ea6"></a>

### `BT_COD_MAJOR_SERVICE_CLASSES`

```c
#define BT_COD_MAJOR_SERVICE_CLASSES ( cod)
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

展开值（Value）：

```c
((((uint32_t)cod[2] & 0xFF) >> 5) | (((uint32_t)cod[1] & 0xD0) >> 5))
```

<a id="ga2c70ab983a099e74a89aaaff02c086d0"></a>

### `BT_COD_MAJOR_SVC_CLASS_AUDIO`

```c
#define BT_COD_MAJOR_SVC_CLASS_AUDIO BIT(21)
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

音频服务类别（Audio service class）。

<a id="ga35cd970ddcba07d98e9e42863ee155f9"></a>

### `BT_COD_MAJOR_SVC_CLASS_CAPTURING`

```c
#define BT_COD_MAJOR_SVC_CLASS_CAPTURING BIT(19)
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

采集服务类别（Capturing service class）。

<a id="gafb44e9944c2f84d45d448975c1ab0300"></a>

### `BT_COD_MAJOR_SVC_CLASS_INFORMATION`

```c
#define BT_COD_MAJOR_SVC_CLASS_INFORMATION BIT(23)
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

信息服务类别（Information service class）。

<a id="ga031275c4187717b7556c4f0a7e16126a"></a>

### `BT_COD_MAJOR_SVC_CLASS_LE_AUDIO`

```c
#define BT_COD_MAJOR_SVC_CLASS_LE_AUDIO BIT(14)
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

低功耗音频服务类别（LE Audio service class）。

<a id="ga01883ae9792f486644dc96dd0559c72d"></a>

### `BT_COD_MAJOR_SVC_CLASS_LIMITED_DISCOVER`

```c
#define BT_COD_MAJOR_SVC_CLASS_LIMITED_DISCOVER BIT(13)
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

有限可发现模式服务类别（Limited Discoverable Mode service class）。

<a id="ga262412d5459d96d7f64a3d13db4906d2"></a>

### `BT_COD_MAJOR_SVC_CLASS_NETWORKING`

```c
#define BT_COD_MAJOR_SVC_CLASS_NETWORKING BIT(17)
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

联网服务类别（Networking service class）。

<a id="ga17cf278f25d45040991ef2d60dafb456"></a>

### `BT_COD_MAJOR_SVC_CLASS_OBJECT_TRANSFER`

```c
#define BT_COD_MAJOR_SVC_CLASS_OBJECT_TRANSFER BIT(20)
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

对象传输服务类别（Object Transfer service class）。

<a id="ga9fa4505b17dc53c22c9ac3fde9743e29"></a>

### `BT_COD_MAJOR_SVC_CLASS_POSITIONING`

```c
#define BT_COD_MAJOR_SVC_CLASS_POSITIONING BIT(16)
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

定位服务类别（Positioning service class）。

<a id="ga6f959f962a9054102b4bbfe5b7248dd5"></a>

### `BT_COD_MAJOR_SVC_CLASS_RENDERING`

```c
#define BT_COD_MAJOR_SVC_CLASS_RENDERING BIT(18)
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

呈现服务类别（Rendering service class）。

<a id="ga18cbe8ede63ed6c3396aabf01c97c672"></a>

### `BT_COD_MAJOR_SVC_CLASS_RESERVED`

```c
#define BT_COD_MAJOR_SVC_CLASS_RESERVED BIT(15)
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

保留服务类别（Reserved service class）。

<a id="ga2bca689e747d06869b3e86dbe7e10253"></a>

### `BT_COD_MAJOR_SVC_CLASS_TELEPHONY`

```c
#define BT_COD_MAJOR_SVC_CLASS_TELEPHONY BIT(22)
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

电话服务类别（Telephony service class）。

<a id="gadcf892b98d0924ea8a78d4b8b588bddb"></a>

### `BT_COD_MINOR_DEVICE_CLASS`

```c
#define BT_COD_MINOR_DEVICE_CLASS ( cod)
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

展开值（Value）：

```c
(((((uint32_t)cod[0]) & 0xFF) >> 2))
```

<a id="ga9cb9ddf5ac2d9e132b1504bb35fba5e7"></a>

### `BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_CAMCORDER`

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_CAMCORDER 0x0D
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

便携式摄录机音频／视频次设备类别（Camcorder audio/video minor device class）。

<a id="ga8f60c01b2da107da93e8b873b03be337"></a>

### `BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_CAR_AUDIO`

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_CAR_AUDIO 0x08
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

汽车音响的音频／视频次设备类别（Car audio audio/video minor device class）。

<a id="ga67798be9a45da9d23993851dc47b8015"></a>

### `BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_GAMING_TOY`

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_GAMING_TOY 0x12
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

游戏玩具音频／视频次设备类别（Gaming toy audio/video minor device class）。

<a id="gaea20dcaaf0dcf2914b1ede0e657ad233"></a>

### `BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HANDSFREE`

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HANDSFREE 0x02
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

免提音频／视频次设备类别（Handsfree audio/video minor device class）。

<a id="ga6adf41d4cadabdca21bb1191ae0951f5"></a>

### `BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HEADPHONES`

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HEADPHONES 0x06
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

耳机音频／视频次设备类别（Headphones audio/video minor device class）。

<a id="ga7ec413fa38b2e0ddcdb0cacfb9565d2a"></a>

### `BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HIFI_AUDIO`

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HIFI_AUDIO 0x0A
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

高保真音响的音频／视频次设备类别（HiFi audio audio/video minor device class）。

<a id="ga419c36342136f5ea827d2889ed666d4c"></a>

### `BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_LOUDSPEAKER`

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_LOUDSPEAKER 0x05
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

扬声器音频／视频次设备类别（Loudspeaker audio/video minor device class）。

<a id="ga6c71bd324c442918d05b2ba176549f78"></a>

### `BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_MICROPHONE`

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_MICROPHONE 0x04
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

麦克风音频／视频次设备类别（Microphone audio/video minor device class）。

<a id="gac50804ea808e6e83686ad973d187bf9d"></a>

### `BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_PORTABLE_AUDIO`

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_PORTABLE_AUDIO 0x07
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

便携音频设备的音频／视频次设备类别（Portable audio audio/video minor device class）。

<a id="ga3a7182ce71c7ae49330475c0093e7665"></a>

### `BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_SETTOP_BOX`

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_SETTOP_BOX 0x09
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

机顶盒音频／视频次设备类别（Set-top box audio/video minor device class）。

<a id="ga245357d925ffde5ce1d7d038bd661097"></a>

### `BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_UNCATEGORIZED`

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_UNCATEGORIZED 0x00
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

次设备类别：音频／视频主类别（Minor Device Class - Audio/Video Major Class）。

未分类的音频／视频次设备类别（Uncategorized audio/video minor device class）。

<a id="gafa6100bcc07e04e7177b34336a523c6a"></a>

### `BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VCR`

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VCR 0x0B
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

录像机音频／视频次设备类别（VCR audio/video minor device class）。

<a id="ga4ee160425ba1d2fa7f7ab9f360eb51ea"></a>

### `BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_CAMERA`

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_CAMERA 0x0C
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

视频摄像机音频／视频次设备类别（Video camera audio/video minor device class）。

<a id="ga07f3ddf991a1de0ef1a5e4bc80f87ae9"></a>

### `BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_CONFERENCING`

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_CONFERENCING 0x10
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

视频会议音频／视频次设备类别（Video conferencing audio/video minor device class）。

<a id="ga5a20841438980c2fcf408974782c9f6e"></a>

### `BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_DISPLAY_LOUDSPEAKER`

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_DISPLAY_LOUDSPEAKER 0x0F
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

视频显示器与扬声器音频／视频次设备类别（Video display and loudspeaker audio/video minor device class）。

<a id="ga7bb6a3801475a076153529859d607254"></a>

### `BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_MONITOR`

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_MONITOR 0x0E
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

视频监视器音频／视频次设备类别（Video monitor audio/video minor device class）。

<a id="gaa79054d26b530834da97412ffc6a6d76"></a>

### `BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_WEARABLE_HEADSET`

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_WEARABLE_HEADSET 0x01
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

可穿戴耳麦音频／视频次设备类别（Wearable headset audio/video minor device class）。

<a id="gae1a285e3787132a97edf7adb53963880"></a>

### `BT_COD_MINOR_DEVICE_CLASS_COMPUTER_DESKTOP_WORKSTATION`

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_DESKTOP_WORKSTATION 0x01
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

台式工作站计算机次设备类别（Desktop workstation computer minor device class）。

<a id="gad8af957eeafefca10f2538b2e09c7bd3"></a>

### `BT_COD_MINOR_DEVICE_CLASS_COMPUTER_HANDHELD_PC_PDA`

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_HANDHELD_PC_PDA 0x04
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

手持 PC／个人数字助理计算机次设备类别（Handheld PC/PDA computer minor device class）。

<a id="ga60f70b01f651baab797b79ee5c7b94aa"></a>

### `BT_COD_MINOR_DEVICE_CLASS_COMPUTER_LAPTOP`

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_LAPTOP 0x03
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

笔记本计算机次设备类别（Laptop computer minor device class）。

<a id="gab5eb08bfa138cbfd55ffa2774a38fd9f"></a>

### `BT_COD_MINOR_DEVICE_CLASS_COMPUTER_PALM_SIZED_PC_PDA`

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_PALM_SIZED_PC_PDA 0x05
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

掌上 PC／个人数字助理计算机次设备类别（Palm-sized PC/PDA computer minor device class）。

<a id="ga6d009b3670bfa0de1ed30c2ec87f8918"></a>

### `BT_COD_MINOR_DEVICE_CLASS_COMPUTER_SERVER`

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_SERVER 0x02
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

服务器级计算机次设备类别（Server-class computer minor device class）。

<a id="ga0a98088245313a02c7dfbfdb39784632"></a>

### `BT_COD_MINOR_DEVICE_CLASS_COMPUTER_TABLET`

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_TABLET 0x07
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

平板计算机次设备类别（Tablet computer minor device class）。

<a id="ga47d7e27a9da20b27c0483ab50db3590d"></a>

### `BT_COD_MINOR_DEVICE_CLASS_COMPUTER_UNCATEGORIZED`

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_UNCATEGORIZED 0x00
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

未分类的计算机次设备类别（Uncategorized computer minor device class）。

<a id="gaec2dc76edfa8a7edc6ce990be1658e54"></a>

### `BT_COD_MINOR_DEVICE_CLASS_COMPUTER_WEARABLE_COMPUTER`

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_WEARABLE_COMPUTER 0x06
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

可穿戴计算机次设备类别（Wearable computer minor device class）。

<a id="ga25315720692627e093a25df80d5b487d"></a>

### `BT_COD_MINOR_DEVICE_CLASS_HEALTH_ANKLE_PROSTHESIS`

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_ANKLE_PROSTHESIS 0x0D
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

踝关节假体健康设备（Ankle prosthesis health device）。

<a id="gadc1ba5de00271e2663dc52770acbf1f1"></a>

### `BT_COD_MINOR_DEVICE_CLASS_HEALTH_BLOOD_PRESSURE_MONITOR`

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_BLOOD_PRESSURE_MONITOR 0x01
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

血压监测健康设备（Blood pressure monitor health device）。

<a id="gad34ed19a24a0b2a300b8e31c5a7ce798"></a>

### `BT_COD_MINOR_DEVICE_CLASS_HEALTH_BODY_COMPOSITION_ANALYZER`

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_BODY_COMPOSITION_ANALYZER 0x09
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

身体成分分析仪健康设备（Body composition analyzer health device）。

<a id="ga308d6b8f3ed8cefccbca002ede932218"></a>

### `BT_COD_MINOR_DEVICE_CLASS_HEALTH_GENERIC_HEALTH_MANAGER`

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_GENERIC_HEALTH_MANAGER 0x0E
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用健康管理器设备（Generic health manager device）。

<a id="ga5c9e6a84ff76bfc8c12750e9b133861a"></a>

### `BT_COD_MINOR_DEVICE_CLASS_HEALTH_GLUCOSE_METER`

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_GLUCOSE_METER 0x04
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

血糖仪健康设备（Glucose meter health device）。

<a id="gad6577d566fd17b126611583b4379ad01"></a>

### `BT_COD_MINOR_DEVICE_CLASS_HEALTH_HEALTH_DATA_DISPLAY`

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_HEALTH_DATA_DISPLAY 0x07
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

健康数据展示设备（Health data display device）。

<a id="ga94863d500f1a576eb3d818209196d12e"></a>

### `BT_COD_MINOR_DEVICE_CLASS_HEALTH_HEART_PULSE_MONITOR`

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_HEART_PULSE_MONITOR 0x06
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

心率／脉搏监测健康设备（Heart/pulse monitor health device）。

<a id="gaabd014dab3f24d38b8aabda2ae7e5ff4"></a>

### `BT_COD_MINOR_DEVICE_CLASS_HEALTH_KNEE_PROSTHESIS`

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_KNEE_PROSTHESIS 0x0C
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

膝关节假体健康设备（Knee prosthesis health device）。

<a id="ga4b376213b25611ff4bcf8cb7c7483a3a"></a>

### `BT_COD_MINOR_DEVICE_CLASS_HEALTH_MEDICATION_MONITOR`

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_MEDICATION_MONITOR 0x0B
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

用药监测健康设备（Medication monitor health device）。

<a id="ga746b3b863fb6250cd990099b014f063f"></a>

### `BT_COD_MINOR_DEVICE_CLASS_HEALTH_PEAK_FLOW_MONITOR`

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_PEAK_FLOW_MONITOR 0x0A
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

峰值流量监测健康设备（Peak flow monitor health device）。

<a id="ga5fd6e3a6703d961259bd563ca6379c9a"></a>

### `BT_COD_MINOR_DEVICE_CLASS_HEALTH_PERSONAL_MOBILITY_DEVICE`

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_PERSONAL_MOBILITY_DEVICE 0x0F
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

个人移动辅助健康设备（Personal mobility health device）。

<a id="gabe9f5e78c7321d8a2ff1752fe41d124d"></a>

### `BT_COD_MINOR_DEVICE_CLASS_HEALTH_PULSE_OXIMETER`

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_PULSE_OXIMETER 0x05
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

脉搏血氧仪健康设备（Pulse oximeter health device）。

<a id="ga6e50e1316332ba4e5da2fd81c6e65ef7"></a>

### `BT_COD_MINOR_DEVICE_CLASS_HEALTH_STEP_COUNTER`

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_STEP_COUNTER 0x08
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

计步器健康设备（Step counter health device）。

<a id="ga60998708af979e1c02d8a0d6373500c8"></a>

### `BT_COD_MINOR_DEVICE_CLASS_HEALTH_THERMOMETER`

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_THERMOMETER 0x02
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

温度计健康设备（Thermometer health device）。

<a id="ga98a4f1577322dd14790bda9ce8b28661"></a>

### `BT_COD_MINOR_DEVICE_CLASS_HEALTH_UNDEFINED`

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_UNDEFINED 0x00
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

未定义的健康设备（Undefined health device）。

<a id="ga8c6cb016bdd1a5f50258c671f7528f8e"></a>

### `BT_COD_MINOR_DEVICE_CLASS_HEALTH_WEIGHING_SCALE`

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_WEIGHING_SCALE 0x03
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

体重秤健康设备（Weighing scale health device）。

<a id="ga238b06f556138d4bab338ff1375a1021"></a>

### `BT_COD_MINOR_DEVICE_CLASS_IMAGING_CAMERA`

```c
#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_CAMERA 0x02
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

成像相机设备（Imaging camera device）。

<a id="gaeb931c305948fa843853f9f418c71d45"></a>

### `BT_COD_MINOR_DEVICE_CLASS_IMAGING_DISPLAY`

```c
#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_DISPLAY 0x01
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

次设备类别：成像主类别（Minor Device Class - Imaging Major Class）。

<a id="gaf6a4be11446739a2aede1adf4d4fda77"></a>

### `BT_COD_MINOR_DEVICE_CLASS_IMAGING_PRINTER`

```c
#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_PRINTER 0x08
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

成像打印机设备（Imaging printer device）。

<a id="ga6eb468819358a83906f40f2f64c344ae"></a>

### `BT_COD_MINOR_DEVICE_CLASS_IMAGING_SCANNER`

```c
#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_SCANNER 0x04
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

成像扫描仪设备（Imaging scanner device）。

<a id="ga5010b99a3111775447ac89f169d824af"></a>

### `BT_COD_MINOR_DEVICE_CLASS_IMAGING_UNCATEGORIZED`

```c
#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_UNCATEGORIZED 0x00
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

次设备类别：成像主类别中的未分类设备（Minor Device Class - Imaging Major Class Uncategorized）。

<a id="gab4af4c15266ce0f24f2f61d0578f346a"></a>

### `BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_DEVICE_TYPE_UNCATEGORIZED`

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_DEVICE_TYPE_UNCATEGORIZED 0x00
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

未分类的局域网／网络设备类型（Uncategorized LAN/network device type）。

<a id="gab19bf6c95fbe0d3aa4923323b67c2f0c"></a>

### `BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_17_33_UTILIZED`

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_17_33_UTILIZED 0x02
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

局域网服务利用率：已使用 17–33%（LAN service utilization: 17-33% utilized）。

<a id="gaa48c789f29f33b7f129bbd593ab336fe"></a>

### `BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_1_17_UTILIZED`

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_1_17_UTILIZED 0x01
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

局域网服务利用率：已使用 1–17%（LAN service utilization: 1-17% utilized）。

<a id="ga17e2dd35fb4fd37f45757515a03df565"></a>

### `BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_33_50_UTILIZED`

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_33_50_UTILIZED 0x03
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

局域网服务利用率：已使用 33–50%（LAN service utilization: 33-50% utilized）。

<a id="gaecb741bfc498bacfbd4c9059b3551e2f"></a>

### `BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_50_67_UTILIZED`

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_50_67_UTILIZED 0x04
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

局域网服务利用率：已使用 50–67%（LAN service utilization: 50-67% utilized）。

<a id="gaf296fcfd14235a0762a4565ff265e6be"></a>

### `BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_67_83_UTILIZED`

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_67_83_UTILIZED 0x05
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

局域网服务利用率：已使用 67–83%（LAN service utilization: 67-83% utilized）。

<a id="ga7a740756ba4dbc8770f4cdf5af2d1fa5"></a>

### `BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_83_99_UTILIZED`

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_83_99_UTILIZED 0x06
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

局域网服务利用率：已使用 83–99%（LAN service utilization: 83-99% utilized）。

<a id="gacf4f30af8af17254d8557c2102e82930"></a>

### `BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_FULLY_AVAILABLE`

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_FULLY_AVAILABLE 0x00
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

局域网服务利用率：完全可用（LAN service utilization: fully available）。

<a id="gafb3f26abffdd158cfd117aefa06a31bb"></a>

### `BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_NO_SERVICE_AVAILABLE`

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_NO_SERVICE_AVAILABLE 0x07
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

局域网服务利用率：无可用服务（LAN service utilization: no service available）。

<a id="ga8b23f0432923353c1425244780c2cd4a"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_CARD_READER`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_CARD_READER 0x06
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

读卡器外设设备类型（Card reader peripheral device type）。

<a id="ga7a8bec17a83efabcf83a3a0848fbd286"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_DIGITAL_PEN`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_DIGITAL_PEN 0x07
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

数字笔外设设备类型（Digital pen peripheral device type）。

<a id="ga8b21b9c98bb8ec187bb7be661c875048"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_DIGITIZER_TABLET`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_DIGITIZER_TABLET 0x05
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

数字化绘图板外设设备类型（Digitizer tablet peripheral device type）。

<a id="gaae4e0e78d28b915f7be42640aab41802"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_GAMEPAD`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_GAMEPAD 0x02
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

游戏手柄外设设备类型（Gamepad peripheral device type）。

<a id="ga2e603791c7467731fcd8e5ef521405fc"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_HANDHELD_GESTURAL_INPUT`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_HANDHELD_GESTURAL_INPUT 0x09
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

手持手势输入外设设备类型（Handheld gestural input peripheral device type）。

<a id="ga3cff5d97f27e3725217f332dbd1e15ef"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_HANDHELD_SCANNER`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_HANDHELD_SCANNER 0x08
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

手持扫描仪外设设备类型（Handheld scanner peripheral device type）。

<a id="gae7ceeea12447c03b901704165f815d2a"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_JOYSTICK`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_JOYSTICK 0x01
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

操纵杆外设设备类型（Joystick peripheral device type）。

<a id="ga55dc4b9ce33c7254ade2b32124bd5a52"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_REMOTE_CONTROL`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_REMOTE_CONTROL 0x03
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

遥控器外设设备类型（Remote control peripheral device type）。

<a id="ga6115e1fc2619c95bcf7a50e657347c8b"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_SENSING_DEVICE`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_SENSING_DEVICE 0x04
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

传感设备外设类型（Sensing device peripheral device type）。

<a id="gadd57844cdd2d6ff59ea8371b64c0786a"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_UNCATEGORIZED`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_UNCATEGORIZED 0x00
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

未分类的外设设备类型（Uncategorized peripheral device type）。

<a id="ga4c26cacb0efe86dd586cacb48f7f9798"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_COMBO_KEYBOARD_POINTING`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_COMBO_KEYBOARD_POINTING 0x03
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

外设输入：键盘与指点设备组合（Peripheral input: combo keyboard and pointing device）。

<a id="gab648e64338834e0f986415603a7ee01a"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_KEYBOARD`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_KEYBOARD 0x01
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

外设输入：键盘（Peripheral input: keyboard）。

<a id="ga4b48d9b5ef8fdddd11f1cb528e826d79"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_NO_KEYBOARD_NO_POINTING`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_NO_KEYBOARD_NO_POINTING 0x00
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

外设输入：无键盘，无指点设备（Peripheral input: no keyboard, no pointing device）。

<a id="ga71c43b86fa8d01d45d11bea0bb56ee63"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_POINTING_DEVICE`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_POINTING_DEVICE 0x02
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

外设输入：指点设备（Peripheral input: pointing device）。

<a id="gaf3796e468def379157c2cf02a356b578"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PHONE_CELLULAR`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_CELLULAR 0x01
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

蜂窝电话次设备类别（Cellular phone minor device class）。

<a id="gad711cb8a9d53d428f4aef9da0605c27e"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PHONE_COMMON_ISDN_ACCESS`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_COMMON_ISDN_ACCESS 0x05
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用综合业务数字网接入电话次设备类别（Common ISDN access phone minor device class）。

<a id="gacce21d82143f430ff2bac1608b42b7e1"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PHONE_CORDLESS`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_CORDLESS 0x02
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

无绳电话次设备类别（Cordless phone minor device class）。

<a id="gad74d69e9ec7a82b128df0a6ad33bfc65"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PHONE_SMARTPHONE`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_SMARTPHONE 0x03
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

智能手机次设备类别（Smartphone minor device class）。

<a id="ga86dd6474cad2c148c4bf2273707f3bca"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PHONE_UNCATEGORIZED`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_UNCATEGORIZED 0x00
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

未分类的电话次设备类别（Uncategorized phone minor device class）。

<a id="ga708f325406d16fbcb96f0a311ad6f12f"></a>

### `BT_COD_MINOR_DEVICE_CLASS_PHONE_WIRED_MODEM`

```c
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_WIRED_MODEM 0x04
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

有线调制解调器或语音网关电话次设备类别（Wired modem or voice gateway phone minor device class）。

<a id="gae51ab020f0a58a7468e79b33cf5888d2"></a>

### `BT_COD_MINOR_DEVICE_CLASS_TOY_CONTROLLER`

```c
#define BT_COD_MINOR_DEVICE_CLASS_TOY_CONTROLLER 0x04
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

玩具控制器设备（Toy controller device）。

<a id="gaf22179ae786663d350c7dfa9a25671b0"></a>

### `BT_COD_MINOR_DEVICE_CLASS_TOY_DOLL`

```c
#define BT_COD_MINOR_DEVICE_CLASS_TOY_DOLL 0x03
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

玩具娃娃设备（Toy doll device）。

<a id="ga4305ed742e35f7d21d97d6ca8a228776"></a>

### `BT_COD_MINOR_DEVICE_CLASS_TOY_GAME`

```c
#define BT_COD_MINOR_DEVICE_CLASS_TOY_GAME 0x05
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

玩具游戏设备（Toy game device）。

<a id="gaf527b4a6353fc0e110033f1661342a80"></a>

### `BT_COD_MINOR_DEVICE_CLASS_TOY_ROBOT`

```c
#define BT_COD_MINOR_DEVICE_CLASS_TOY_ROBOT 0x01
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

玩具机器人设备（Toy robot device）。

<a id="ga236dedbc75b174d221173080e734227e"></a>

### `BT_COD_MINOR_DEVICE_CLASS_TOY_VEHICLE`

```c
#define BT_COD_MINOR_DEVICE_CLASS_TOY_VEHICLE 0x02
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

玩具车辆设备（Toy vehicle device）。

<a id="gaea4e865414b40d9b370951a328dc0c36"></a>

### `BT_COD_MINOR_DEVICE_CLASS_WEARABLE_GLASSES`

```c
#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_GLASSES 0x05
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

可穿戴眼镜设备（Wearable glasses device）。

<a id="gae879842e986be1f78b1a6afdd06f267e"></a>

### `BT_COD_MINOR_DEVICE_CLASS_WEARABLE_HEADSET`

```c
#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_HEADSET 0x01
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

可穿戴耳麦设备（Wearable headset device）。

<a id="ga091efe28aab4b90f3552d56704b2a886"></a>

### `BT_COD_MINOR_DEVICE_CLASS_WEARABLE_HELMET`

```c
#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_HELMET 0x04
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

可穿戴头盔设备（Wearable helmet device）。

<a id="ga9a7d4d0b3645f38a9888beb2ec994fe1"></a>

### `BT_COD_MINOR_DEVICE_CLASS_WEARABLE_JACKET`

```c
#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_JACKET 0x03
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

可穿戴夹克设备（Wearable jacket device）。

<a id="ga2c68dc5a8fe4252bc2c743f05f9d4e96"></a>

### `BT_COD_MINOR_DEVICE_CLASS_WEARABLE_PAGER`

```c
#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_PAGER 0x02
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

可穿戴寻呼机设备（Wearable pager device）。

<a id="gaf2c925e431eec42930101a72b00a7283"></a>

### `BT_COD_VALID`

```c
#define BT_COD_VALID ( cod)
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

展开值（Value）：

```c
((0 == (cod[0] & (BIT(0) | BIT(1)))) ? true : false)
```

<a id="ga6bbf21c05f24d2c2c710be9bcf05af5f"></a>

### `BT_COMP_ID_LF`

```c
#define BT_COMP_ID_LF 0x05f1
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

Linux 基金会（The Linux Foundation）。


## 3.17\_原页交叉引用（Cross References）

- [蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md)
- [核心规范分配编号（Core Specification Assigned Numbers）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html)
- [通用音频分配编号（Generic Audio Assigned Numbers）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__audio.html)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [zephyr/bluetooth/assigned_numbers.h](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="agroup__sys-util_html_ga3a8ea58898cb58fc96013383d39f482c"></a>
<a id="astdbool_8h_html_a41f9c5fb8b08eb5dc3edce4dcb37fee7"></a>

---

[上一章](P002_高级音频分发配置文件（Advanced Audio Distribution Profile，A2DP）.md) · [返回大纲](大纲.md) · [下一章](P004_蓝牙基本音频配置文件（Bluetooth Basic Audio Profile）.md)
