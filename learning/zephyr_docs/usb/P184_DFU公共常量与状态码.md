---
id: learning.zephyr-docs.usb.api-184
title: DFU公共常量与状态码
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb__dfu_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2015,2016 Intel Corporation. -->
<!-- Copyright (c) 2017 PHYTEC Messtechnik GmbH -->
<!-- SPDX-License-Identifier: Apache-2.0 AND BSD-3-Clause -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第184章\_DFU公共常量与状态码

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usb__dfu_8h.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 184.1\_阅读说明与来源

译注：本组补齐设备固件升级（Device Firmware Upgrade，DFU）的头文件参考、协议状态和功能描述符，分别标明旧版设备栈与新版设备栈。镜像定义宏及回调说明见[设备固件升级 API](P062_USB设备固件升级API.md)和[镜像结构](P063_USB固件升级镜像结构.md)；本页不会仅凭描述符字段推定目标板已具备升级能力。

USB 设备固件升级（Device Firmware Upgrade，DFU）公共头文件。

```c
#include <zephyr/sys/clock.h>
```

USB 设备固件升级（Device Firmware Upgrade，DFU）公共头文件。

已弃用（Deprecated）：此 API 已弃用。

相关声明：[Deprecated](https://docs.zephyrproject.org/latest/doxygen/html/deprecated.html#_deprecated000105)。

本头文件遵循《设备固件升级设备类规范》（Device Class Specification for Device Firmware Upgrade）1.1 版。

## 184.2\_数据结构（Data Structures）

<a id="r_dfu_5Fruntime_5Fdescriptor"></a>

```c
struct dfu_runtime_descriptor
```

运行时功能描述符（Run-Time Functional Descriptor）。

相关声明：[dfu_runtime_descriptor](P189_旧版DFU运行时描述符.md)。

## 184.3\_宏定义（Macros）

<a id="r_a86d100d1016e44b1a57d72f87394f49b"></a>

```c
#define DFU_SUBCLASS 0x01 __DEPRECATED_MACRO
```

DFU 类的子类（Subclass）。

相关声明：[DFU_SUBCLASS](P184_DFU公共常量与状态码.md#a86d100d1016e44b1a57d72f87394f49b)。

<a id="r_a6da8cdd5028653f5008ae62371d68049"></a>

```c
#define DFU_RT_PROTOCOL 0x01 __DEPRECATED_MACRO
```

DFU 类的运行时协议（Runtime Protocol）。

相关声明：[DFU_RT_PROTOCOL](P184_DFU公共常量与状态码.md#a6da8cdd5028653f5008ae62371d68049)。

<a id="r_ad44791964357de89e8f051a0eeff7b6c"></a>

```c
#define DFU_MODE_PROTOCOL 0x02 __DEPRECATED_MACRO
```

DFU 类的 DFU 模式协议（DFU Mode Protocol）。

相关声明：[DFU_MODE_PROTOCOL](P184_DFU公共常量与状态码.md#ad44791964357de89e8f051a0eeff7b6c)。

<a id="r_a1dbfcd9de4badc68f1a79720113dfa3d"></a>

```c
#define DFU_DETACH 0x00 __DEPRECATED_MACRO
```

DFU 类专用请求（Class Specific Requests）。

相关声明：[DFU_DETACH](P184_DFU公共常量与状态码.md#a1dbfcd9de4badc68f1a79720113dfa3d)。

<a id="r_aaf8b2bc0fa447ec925a47cee00916e4a"></a>

```c
#define DFU_DNLOAD 0x01 __DEPRECATED_MACRO
```



相关声明：[DFU_DNLOAD](P184_DFU公共常量与状态码.md#aaf8b2bc0fa447ec925a47cee00916e4a)。

<a id="r_a9ec42539a3b1d7a1fcb47383e5ae73b7"></a>

```c
#define DFU_UPLOAD 0x02 __DEPRECATED_MACRO
```



相关声明：[DFU_UPLOAD](P184_DFU公共常量与状态码.md#a9ec42539a3b1d7a1fcb47383e5ae73b7)。

<a id="r_af45d9250c3e5dfb12a217bc08828cc06"></a>

```c
#define DFU_GETSTATUS 0x03 __DEPRECATED_MACRO
```



相关声明：[DFU_GETSTATUS](P184_DFU公共常量与状态码.md#af45d9250c3e5dfb12a217bc08828cc06)。

<a id="r_aff6ab40ddfc07a8e873aa4c8dde99fc8"></a>

```c
#define DFU_CLRSTATUS 0x04 __DEPRECATED_MACRO
```



相关声明：[DFU_CLRSTATUS](P184_DFU公共常量与状态码.md#aff6ab40ddfc07a8e873aa4c8dde99fc8)。

<a id="r_a41912ad6c650bf2df2b730f3d6d07849"></a>

```c
#define DFU_GETSTATE 0x05 __DEPRECATED_MACRO
```



相关声明：[DFU_GETSTATE](P184_DFU公共常量与状态码.md#a41912ad6c650bf2df2b730f3d6d07849)。

<a id="r_a9f0bb6811ae976a2cd8a7b42c19a8390"></a>

```c
#define DFU_ABORT 0x06 __DEPRECATED_MACRO
```



相关声明：[DFU_ABORT](P184_DFU公共常量与状态码.md#a9f0bb6811ae976a2cd8a7b42c19a8390)。

<a id="r_a2d6a59039cf1e8f97ba0443e7d20fd1c"></a>

```c
#define DFU_FUNC_DESC 0x21 __DEPRECATED_MACRO
```

DFU 功能描述符类型（Functional Descriptor Type）。

相关声明：[DFU_FUNC_DESC](P184_DFU公共常量与状态码.md#a2d6a59039cf1e8f97ba0443e7d20fd1c)。

<a id="r_a8f41515182d31b45f06523deb89a0b6d"></a>

```c
#define DFU_ATTR_WILL_DETACH 0x08 __DEPRECATED_MACRO
```

DFU 功能描述符的属性（Attributes）。

相关声明：[DFU_ATTR_WILL_DETACH](P184_DFU公共常量与状态码.md#a8f41515182d31b45f06523deb89a0b6d)。

<a id="r_a9426f19a5d9970da8b7479e6f341e26c"></a>

```c
#define DFU_ATTR_MANIFESTATION_TOLERANT 0x04 __DEPRECATED_MACRO
```



相关声明：[DFU_ATTR_MANIFESTATION_TOLERANT](P184_DFU公共常量与状态码.md#a9426f19a5d9970da8b7479e6f341e26c)。

<a id="r_a0fe01b636c7e5224a7cbd0ddcd3ac3e7"></a>

```c
#define DFU_ATTR_CAN_UPLOAD 0x02 __DEPRECATED_MACRO
```



相关声明：[DFU_ATTR_CAN_UPLOAD](P184_DFU公共常量与状态码.md#a0fe01b636c7e5224a7cbd0ddcd3ac3e7)。

<a id="r_a07cbf2381d03bafb4d844cd00fd95079"></a>

```c
#define DFU_ATTR_CAN_DNLOAD 0x01 __DEPRECATED_MACRO
```



相关声明：[DFU_ATTR_CAN_DNLOAD](P184_DFU公共常量与状态码.md#a07cbf2381d03bafb4d844cd00fd95079)。

<a id="r_a7f333dc5f69079381f912b9b3ab9d202"></a>

```c
#define DFU_VERSION 0x0110 __DEPRECATED_MACRO
```

DFU 规范版本（Specification Release）。

相关声明：[DFU_VERSION](P184_DFU公共常量与状态码.md#a7f333dc5f69079381f912b9b3ab9d202)。

## 184.4\_枚举（Enumerations）

<a id="r_abcf2757cf1c6281a06a8a6f25ff2aa31"></a>

```c
enum dfu_status {
    statusOK,
    errTARGET,
    errFILE,
    errWRITE,
    errERASE,
    errCHECK_ERASED,
    errPROG,
    errVERIFY,
    errADDRESS,
    errNOTDONE,
    errFIRMWARE,
    errVENDOR,
    errUSB,
    errPOR,
    errUNKNOWN,
    errSTALLEDPKT
}
```

DFU_GETSTATUS 响应中的 bStatus 值。

相关声明：[dfu_status](P184_DFU公共常量与状态码.md#abcf2757cf1c6281a06a8a6f25ff2aa31)、[statusOK](P184_DFU公共常量与状态码.md#abcf2757cf1c6281a06a8a6f25ff2aa31acf11a7eb0a529adca2b399a6b81c8d19)、[errTARGET](P184_DFU公共常量与状态码.md#abcf2757cf1c6281a06a8a6f25ff2aa31a4f6d9b9397bdaf8c52b1a3b21814795d)、[errFILE](P184_DFU公共常量与状态码.md#abcf2757cf1c6281a06a8a6f25ff2aa31a56c7583a5956d85dc99cf250f8c7771e)、[errWRITE](P184_DFU公共常量与状态码.md#abcf2757cf1c6281a06a8a6f25ff2aa31a62181eec68b16d43c1aee03174f9bba1)、[errERASE](P184_DFU公共常量与状态码.md#abcf2757cf1c6281a06a8a6f25ff2aa31a5816bb25bcc32867630963dba649cc54)、[errCHECK_ERASED](P184_DFU公共常量与状态码.md#abcf2757cf1c6281a06a8a6f25ff2aa31a65c1f54049798ea81c7d1719f166a1be)、[errPROG](P184_DFU公共常量与状态码.md#abcf2757cf1c6281a06a8a6f25ff2aa31aacb4bde78f2c57c18dc2dc3d5249f2c8)、[errVERIFY](P184_DFU公共常量与状态码.md#abcf2757cf1c6281a06a8a6f25ff2aa31a251a276fd7bfe2744888dc97fe956aff)、[errADDRESS](P184_DFU公共常量与状态码.md#abcf2757cf1c6281a06a8a6f25ff2aa31a7465c34dd18ad03c8cbe13e3d395c902)、[errNOTDONE](P184_DFU公共常量与状态码.md#abcf2757cf1c6281a06a8a6f25ff2aa31af30286bf44938bdea942a7f3c513d998)、[errFIRMWARE](P184_DFU公共常量与状态码.md#abcf2757cf1c6281a06a8a6f25ff2aa31a770d6396237b7deac15001165ef9c9bb)、[errVENDOR](P184_DFU公共常量与状态码.md#abcf2757cf1c6281a06a8a6f25ff2aa31a08770dc5628ca360ef8a5ecfdf3d2210)、[errUSB](P184_DFU公共常量与状态码.md#abcf2757cf1c6281a06a8a6f25ff2aa31a7006bd30ea4310800fa059ddc8d30947)、[errPOR](P184_DFU公共常量与状态码.md#abcf2757cf1c6281a06a8a6f25ff2aa31a992b1de144265596023b92aa21094ecb)、[errUNKNOWN](P184_DFU公共常量与状态码.md#abcf2757cf1c6281a06a8a6f25ff2aa31aa69cd762eb2bcefece21d4601c51f471)、[errSTALLEDPKT](P184_DFU公共常量与状态码.md#abcf2757cf1c6281a06a8a6f25ff2aa31a0123f1a634c8d384393557aedecb0788)。

<a id="r_a3f025bde53c777c5e0493ef54bbeb143"></a>

```c
enum dfu_state {
    appIDLE,
    appDETACH,
    dfuIDLE,
    dfuDNLOAD_SYNC,
    dfuDNBUSY,
    dfuDNLOAD_IDLE,
    dfuMANIFEST_SYNC,
    dfuMANIFEST,
    dfuMANIFEST_WAIT_RST,
    dfuUPLOAD_IDLE,
    dfuERROR
}
```

DFU_GETSTATUS 响应中的 bState 值。

相关声明：[dfu_state](P184_DFU公共常量与状态码.md#a3f025bde53c777c5e0493ef54bbeb143)、[appIDLE](P184_DFU公共常量与状态码.md#a3f025bde53c777c5e0493ef54bbeb143aadb4993cd9183666f3ef9fd82a4519fa)、[appDETACH](P184_DFU公共常量与状态码.md#a3f025bde53c777c5e0493ef54bbeb143a71f82402de0db9a8f3263f045f87bcc1)、[dfuIDLE](P184_DFU公共常量与状态码.md#a3f025bde53c777c5e0493ef54bbeb143a64a13d4b1b2cc0b0a40069d8c28fe74c)、[dfuDNLOAD_SYNC](P184_DFU公共常量与状态码.md#a3f025bde53c777c5e0493ef54bbeb143ad5eb9bbb1f4eb27a0ac7e60c0bf5341f)、[dfuDNBUSY](P184_DFU公共常量与状态码.md#a3f025bde53c777c5e0493ef54bbeb143afd398c862995dfe599a9f182fa1e902e)、[dfuDNLOAD_IDLE](P184_DFU公共常量与状态码.md#a3f025bde53c777c5e0493ef54bbeb143a68f32e308ff090838040f69ddcab8fff)、[dfuMANIFEST_SYNC](P184_DFU公共常量与状态码.md#a3f025bde53c777c5e0493ef54bbeb143a002e3cc408cf56d51c6cd2b0d90f1b7c)、[dfuMANIFEST](P184_DFU公共常量与状态码.md#a3f025bde53c777c5e0493ef54bbeb143aaffa9156a82ef21608e730325d8bb2c6)、[dfuMANIFEST_WAIT_RST](P184_DFU公共常量与状态码.md#a3f025bde53c777c5e0493ef54bbeb143aa6e5b30fd65a5485046759f438be29d8)、[dfuUPLOAD_IDLE](P184_DFU公共常量与状态码.md#a3f025bde53c777c5e0493ef54bbeb143a541f6e1c465d547c1265ba6bde6c59c2)、[dfuERROR](P184_DFU公共常量与状态码.md#a3f025bde53c777c5e0493ef54bbeb143a15ff004b2336c3e5b88e3edd276b32fd)。

## 184.5\_函数（Functions）

<a id="r_a892959f521c403e4ec295c252e75e5dc"></a>

```c
void wait_for_usb_dfu (k_timeout_t delay)
```



相关声明：[wait_for_usb_dfu](P184_DFU公共常量与状态码.md#a892959f521c403e4ec295c252e75e5dc)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

## 184.6\_详细说明（Detailed Documentation）

<a id="a9f0bb6811ae976a2cd8a7b42c19a8390"></a>

### 184.6.1\_`DFU_ABORT`

```c
#define DFU_ABORT 0x06 __DEPRECATED_MACRO
```

<a id="a07cbf2381d03bafb4d844cd00fd95079"></a>

### 184.6.2\_`DFU_ATTR_CAN_DNLOAD`

```c
#define DFU_ATTR_CAN_DNLOAD 0x01 __DEPRECATED_MACRO
```

<a id="a0fe01b636c7e5224a7cbd0ddcd3ac3e7"></a>

### 184.6.3\_`DFU_ATTR_CAN_UPLOAD`

```c
#define DFU_ATTR_CAN_UPLOAD 0x02 __DEPRECATED_MACRO
```

<a id="a9426f19a5d9970da8b7479e6f341e26c"></a>

### 184.6.4\_`DFU_ATTR_MANIFESTATION_TOLERANT`

```c
#define DFU_ATTR_MANIFESTATION_TOLERANT 0x04 __DEPRECATED_MACRO
```

<a id="a8f41515182d31b45f06523deb89a0b6d"></a>

### 184.6.5\_`DFU_ATTR_WILL_DETACH`

```c
#define DFU_ATTR_WILL_DETACH 0x08 __DEPRECATED_MACRO
```

DFU 功能描述符的属性（Attributes）。

<a id="aff6ab40ddfc07a8e873aa4c8dde99fc8"></a>

### 184.6.6\_`DFU_CLRSTATUS`

```c
#define DFU_CLRSTATUS 0x04 __DEPRECATED_MACRO
```

<a id="a1dbfcd9de4badc68f1a79720113dfa3d"></a>

### 184.6.7\_`DFU_DETACH`

```c
#define DFU_DETACH 0x00 __DEPRECATED_MACRO
```

DFU 类专用请求（Class Specific Requests）。

<a id="aaf8b2bc0fa447ec925a47cee00916e4a"></a>

### 184.6.8\_`DFU_DNLOAD`

```c
#define DFU_DNLOAD 0x01 __DEPRECATED_MACRO
```

<a id="a2d6a59039cf1e8f97ba0443e7d20fd1c"></a>

### 184.6.9\_`DFU_FUNC_DESC`

```c
#define DFU_FUNC_DESC 0x21 __DEPRECATED_MACRO
```

DFU 功能描述符类型（Functional Descriptor Type）。

<a id="a41912ad6c650bf2df2b730f3d6d07849"></a>

### 184.6.10\_`DFU_GETSTATE`

```c
#define DFU_GETSTATE 0x05 __DEPRECATED_MACRO
```

<a id="af45d9250c3e5dfb12a217bc08828cc06"></a>

### 184.6.11\_`DFU_GETSTATUS`

```c
#define DFU_GETSTATUS 0x03 __DEPRECATED_MACRO
```

<a id="ad44791964357de89e8f051a0eeff7b6c"></a>

### 184.6.12\_`DFU_MODE_PROTOCOL`

```c
#define DFU_MODE_PROTOCOL 0x02 __DEPRECATED_MACRO
```

DFU 类的 DFU 模式协议（DFU Mode Protocol）。

<a id="a6da8cdd5028653f5008ae62371d68049"></a>

### 184.6.13\_`DFU_RT_PROTOCOL`

```c
#define DFU_RT_PROTOCOL 0x01 __DEPRECATED_MACRO
```

DFU 类的运行时协议（Runtime Protocol）。

<a id="a86d100d1016e44b1a57d72f87394f49b"></a>

### 184.6.14\_`DFU_SUBCLASS`

```c
#define DFU_SUBCLASS 0x01 __DEPRECATED_MACRO
```

DFU 类的子类（Subclass）。

<a id="a9ec42539a3b1d7a1fcb47383e5ae73b7"></a>

### 184.6.15\_`DFU_UPLOAD`

```c
#define DFU_UPLOAD 0x02 __DEPRECATED_MACRO
```

<a id="a7f333dc5f69079381f912b9b3ab9d202"></a>

### 184.6.16\_`DFU_VERSION`

```c
#define DFU_VERSION 0x0110 __DEPRECATED_MACRO
```

DFU 规范版本（Specification Release）。

<a id="a3f025bde53c777c5e0493ef54bbeb143"></a>

### 184.6.17\_`dfu_state`

```c
enum dfu_state
```

DFU_GETSTATUS 响应中的 bState 值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `appIDLE` |  |
| `appDETACH` |  |
| `dfuIDLE` |  |
| `dfuDNLOAD_SYNC` |  |
| `dfuDNBUSY` |  |
| `dfuDNLOAD_IDLE` |  |
| `dfuMANIFEST_SYNC` |  |
| `dfuMANIFEST` |  |
| `dfuMANIFEST_WAIT_RST` |  |
| `dfuUPLOAD_IDLE` |  |
| `dfuERROR` |  |

> 译注（源码核对）：这是旧版设备栈的状态枚举（State Enumeration）；`dfu_status` 则是 DFU_GETSTATUS 返回的状态码／错误码（Status Code），二者不是同一组数值。原始枚举顺序与名称保留，新版对应 usb_dfu_state 和 usb_dfu_status。

<a id="abcf2757cf1c6281a06a8a6f25ff2aa31"></a>

### 184.6.18\_`dfu_status`

```c
enum dfu_status
```

DFU_GETSTATUS 响应中的 bStatus 值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `statusOK` |  |
| `errTARGET` |  |
| `errFILE` |  |
| `errWRITE` |  |
| `errERASE` |  |
| `errCHECK_ERASED` |  |
| `errPROG` |  |
| `errVERIFY` |  |
| `errADDRESS` |  |
| `errNOTDONE` |  |
| `errFIRMWARE` |  |
| `errVENDOR` |  |
| `errUSB` |  |
| `errPOR` |  |
| `errUNKNOWN` |  |
| `errSTALLEDPKT` |  |

<a id="a892959f521c403e4ec295c252e75e5dc"></a>

### 184.6.19\_`wait_for_usb_dfu()`

```c
void wait_for_usb_dfu ( k_timeout_t delay)
```

> 译注（源码核对）：原始头文件将此函数声明为 `__deprecated void wait_for_usb_dfu(k_timeout_t delay)`，本 Doxygen 详情没有展开显示 __deprecated。当前实现先在 delay 给定的时间窗口内等待 DFU 开始；一旦开始，改用 k_poll(..., K_FOREVER) 等待完成信号。因此 delay 不是整个升级流程的总超时。函数返回 void，日志也不能代替镜像启动验证。

## 184.7\_源码跟踪与使用边界

译注依据保存的[旧版 DFU 头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usb_dfu.h)、[新版 DFU 头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_dfu.h)、[新版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_dfu.c)及[旧版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/class/dfu/usb_dfu.c)，摘要见[来源记录](../SOURCES.md)。仓库内[旧版头文件](../../../include/zephyr/usb/class/usb_dfu.h)、[新版头文件](../../../include/zephyr/usb/class/usbd_dfu.h)、[新版实现](../../../subsys/usb/device_next/class/usbd_dfu.c)与[旧版实现](../../../subsys/usb/device/class/dfu/usb_dfu.c)用于相对路径跟踪，版本可能与官网不同。

> 译注：本页属于已弃用的旧版 DFU 接口，保留用于阅读和迁移对照；新实现从[新版 DFU API](P062_USB设备固件升级API.md)阅读。

本批未构建固件、执行镜像下载、擦写 Flash 或验证重启后的镜像。

## 184.8\_原始版权与许可

以下保留所依据头文件的原始许可声明。

```c
/* SPDX-License-Identifier: BSD-3-Clause */

/***************************************************************************
 *
 * Copyright (c) 2015,2016 Intel Corporation.
 * Copyright (c) 2017 PHYTEC Messtechnik GmbH
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 *
 * * Redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer.
 * * Redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in
 * the documentation and/or other materials provided with the
 * distribution.
 * * Neither the name of Intel Corporation nor the names of its
 * contributors may be used to endorse or promote products derived
 * from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
 * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
 * OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 * SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
 * LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 * THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 ***************************************************************************/
```

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a3f025bde53c777c5e0493ef54bbeb143aadb4993cd9183666f3ef9fd82a4519fa"></a>
<a id="a3f025bde53c777c5e0493ef54bbeb143a71f82402de0db9a8f3263f045f87bcc1"></a>
<a id="a3f025bde53c777c5e0493ef54bbeb143a64a13d4b1b2cc0b0a40069d8c28fe74c"></a>
<a id="a3f025bde53c777c5e0493ef54bbeb143ad5eb9bbb1f4eb27a0ac7e60c0bf5341f"></a>
<a id="a3f025bde53c777c5e0493ef54bbeb143afd398c862995dfe599a9f182fa1e902e"></a>
<a id="a3f025bde53c777c5e0493ef54bbeb143a68f32e308ff090838040f69ddcab8fff"></a>
<a id="a3f025bde53c777c5e0493ef54bbeb143a002e3cc408cf56d51c6cd2b0d90f1b7c"></a>
<a id="a3f025bde53c777c5e0493ef54bbeb143aaffa9156a82ef21608e730325d8bb2c6"></a>
<a id="a3f025bde53c777c5e0493ef54bbeb143aa6e5b30fd65a5485046759f438be29d8"></a>
<a id="a3f025bde53c777c5e0493ef54bbeb143a541f6e1c465d547c1265ba6bde6c59c2"></a>
<a id="a3f025bde53c777c5e0493ef54bbeb143a15ff004b2336c3e5b88e3edd276b32fd"></a>
<a id="abcf2757cf1c6281a06a8a6f25ff2aa31acf11a7eb0a529adca2b399a6b81c8d19"></a>
<a id="abcf2757cf1c6281a06a8a6f25ff2aa31a4f6d9b9397bdaf8c52b1a3b21814795d"></a>
<a id="abcf2757cf1c6281a06a8a6f25ff2aa31a56c7583a5956d85dc99cf250f8c7771e"></a>
<a id="abcf2757cf1c6281a06a8a6f25ff2aa31a62181eec68b16d43c1aee03174f9bba1"></a>
<a id="abcf2757cf1c6281a06a8a6f25ff2aa31a5816bb25bcc32867630963dba649cc54"></a>
<a id="abcf2757cf1c6281a06a8a6f25ff2aa31a65c1f54049798ea81c7d1719f166a1be"></a>
<a id="abcf2757cf1c6281a06a8a6f25ff2aa31aacb4bde78f2c57c18dc2dc3d5249f2c8"></a>
<a id="abcf2757cf1c6281a06a8a6f25ff2aa31a251a276fd7bfe2744888dc97fe956aff"></a>
<a id="abcf2757cf1c6281a06a8a6f25ff2aa31a7465c34dd18ad03c8cbe13e3d395c902"></a>
<a id="abcf2757cf1c6281a06a8a6f25ff2aa31af30286bf44938bdea942a7f3c513d998"></a>
<a id="abcf2757cf1c6281a06a8a6f25ff2aa31a770d6396237b7deac15001165ef9c9bb"></a>
<a id="abcf2757cf1c6281a06a8a6f25ff2aa31a08770dc5628ca360ef8a5ecfdf3d2210"></a>
<a id="abcf2757cf1c6281a06a8a6f25ff2aa31a7006bd30ea4310800fa059ddc8d30947"></a>
<a id="abcf2757cf1c6281a06a8a6f25ff2aa31a992b1de144265596023b92aa21094ecb"></a>
<a id="abcf2757cf1c6281a06a8a6f25ff2aa31aa69cd762eb2bcefece21d4601c51f471"></a>
<a id="abcf2757cf1c6281a06a8a6f25ff2aa31a0123f1a634c8d384393557aedecb0788"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P183_CDC公共头文件源码.md) · [返回大纲](大纲.md) · [下一章](P185_DFU功能描述符.md)
