---
id: learning.zephyr-docs.usb.api-187
title: DFU设备类头文件接口
kind: reference
status: maintained
domains: [zephyr, usb, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usbd__dfu_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- Copyright (c) 2024 Nordic Semiconductor ASA -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第187章\_DFU设备类头文件接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usbd__dfu_8h.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 187.1\_阅读说明与来源

译注：本组补齐设备固件升级（Device Firmware Upgrade，DFU）的头文件参考、协议状态和功能描述符，分别标明旧版设备栈与新版设备栈。镜像定义宏及回调说明见[设备固件升级 API](P062_USB设备固件升级API.md)和[镜像结构](P063_USB固件升级镜像结构.md)；本页不会仅凭描述符字段推定目标板已具备升级能力。

USB 设备固件升级（Device Firmware Upgrade，DFU）公共头文件。

```c
#include <stdint.h>
```

USB 设备固件升级（Device Firmware Upgrade，DFU）公共头文件。

本头文件提供注册 DFU 镜像（Image）的 API。

## 187.2\_数据结构（Data Structures）

<a id="r_usb_5Fdfu_5Fdescriptor"></a>

```c
struct usb_dfu_descriptor
```



相关声明：[usb_dfu_descriptor](P185_DFU功能描述符.md)。

<a id="r_usbd_5Fdfu_5Fimage"></a>

```c
struct usbd_dfu_image
```



相关声明：[usbd_dfu_image](P063_USB固件升级镜像结构.md)。

## 187.3\_宏定义（Macros）

<a id="r_a518e936748d79f70576e082604203ae7"></a>

```c
#define USB_DFU_SUBCLASS 0x01
```



相关声明：[USB_DFU_SUBCLASS](P187_DFU设备类头文件接口.md#a518e936748d79f70576e082604203ae7)。

<a id="r_a0f6bc7bb8b073e9a19a6a77524dde1a1"></a>

```c
#define USB_DFU_PROTOCOL_RUNTIME 0x01
```



相关声明：[USB_DFU_PROTOCOL_RUNTIME](P187_DFU设备类头文件接口.md#a0f6bc7bb8b073e9a19a6a77524dde1a1)。

<a id="r_a501a899e415cb37503f446cc54cb64ed"></a>

```c
#define USB_DFU_PROTOCOL_DFU 0x02
```



相关声明：[USB_DFU_PROTOCOL_DFU](P187_DFU设备类头文件接口.md#a501a899e415cb37503f446cc54cb64ed)。

<a id="r_a083ab5fb2b7ea064ba0caeeba9ecba73"></a>

```c
#define USB_DFU_REQ_DETACH 0x00
```



相关声明：[USB_DFU_REQ_DETACH](P187_DFU设备类头文件接口.md#a083ab5fb2b7ea064ba0caeeba9ecba73)。

<a id="r_a54e31f9cb963e35caaf8049a8116ab52"></a>

```c
#define USB_DFU_REQ_DNLOAD 0x01
```



相关声明：[USB_DFU_REQ_DNLOAD](P187_DFU设备类头文件接口.md#a54e31f9cb963e35caaf8049a8116ab52)。

<a id="r_ac3118cca70abbc4e08a6cb58ce439f71"></a>

```c
#define USB_DFU_REQ_UPLOAD 0x02
```



相关声明：[USB_DFU_REQ_UPLOAD](P187_DFU设备类头文件接口.md#ac3118cca70abbc4e08a6cb58ce439f71)。

<a id="r_afebeea3c212557b2c17dbf8549b42681"></a>

```c
#define USB_DFU_REQ_GETSTATUS 0x03
```



相关声明：[USB_DFU_REQ_GETSTATUS](P187_DFU设备类头文件接口.md#afebeea3c212557b2c17dbf8549b42681)。

<a id="r_a1fb983580f4fc40ceec78b7bb7398126"></a>

```c
#define USB_DFU_REQ_CLRSTATUS 0x04
```



相关声明：[USB_DFU_REQ_CLRSTATUS](P187_DFU设备类头文件接口.md#a1fb983580f4fc40ceec78b7bb7398126)。

<a id="r_aca55ad0b7ee615c5414aa518c94af345"></a>

```c
#define USB_DFU_REQ_GETSTATE 0x05
```



相关声明：[USB_DFU_REQ_GETSTATE](P187_DFU设备类头文件接口.md#aca55ad0b7ee615c5414aa518c94af345)。

<a id="r_a9e54b63df02eac63afd493b4ec8ba8dd"></a>

```c
#define USB_DFU_REQ_ABORT 0x06
```



相关声明：[USB_DFU_REQ_ABORT](P187_DFU设备类头文件接口.md#a9e54b63df02eac63afd493b4ec8ba8dd)。

<a id="r_ae5b7a3271bc417852f829a9d913a0e43"></a>

```c
#define USB_DESC_DFU_FUNCTIONAL 0x21
```



相关声明：[USB_DESC_DFU_FUNCTIONAL](P187_DFU设备类头文件接口.md#ae5b7a3271bc417852f829a9d913a0e43)。

<a id="r_a005e5b7fc18c066ee61ae393a2ba09c7"></a>

```c
#define USB_DFU_ATTR_WILL_DETACH BIT(3)
```



相关声明：[USB_DFU_ATTR_WILL_DETACH](P187_DFU设备类头文件接口.md#a005e5b7fc18c066ee61ae393a2ba09c7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a645a02847a4ff2b47ce93be8c90168eb"></a>

```c
#define USB_DFU_ATTR_MANIFESTATION_TOLERANT BIT(2)
```



相关声明：[USB_DFU_ATTR_MANIFESTATION_TOLERANT](P187_DFU设备类头文件接口.md#a645a02847a4ff2b47ce93be8c90168eb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a40264d92194b790a6b285c1aefa0cc3c"></a>

```c
#define USB_DFU_ATTR_CAN_UPLOAD BIT(1)
```



相关声明：[USB_DFU_ATTR_CAN_UPLOAD](P187_DFU设备类头文件接口.md#a40264d92194b790a6b285c1aefa0cc3c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a22c5740401995633128679a460d4a2ef"></a>

```c
#define USB_DFU_ATTR_CAN_DNLOAD BIT(0)
```



相关声明：[USB_DFU_ATTR_CAN_DNLOAD](P187_DFU设备类头文件接口.md#a22c5740401995633128679a460d4a2ef)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_aa3f88d63fbd9542614b6057da9c133e5"></a>

```c
#define USB_DFU_VERSION 0x0110
```



相关声明：[USB_DFU_VERSION](P187_DFU设备类头文件接口.md#aa3f88d63fbd9542614b6057da9c133e5)。

<a id="r_ga24229d3b70d2e61bb1658c35f0be5070"></a>

```c
#define USBD_DFU_DEFINE_IMG(id, iname, ipriv, iread, iwrite, inext)
```

定义 USB DFU 镜像。

相关声明：[USBD_DFU_DEFINE_IMG](P062_USB设备固件升级API.md#ga24229d3b70d2e61bb1658c35f0be5070)。

## 187.4\_枚举（Enumerations）

<a id="r_a3c39293bedc430e245f3f0919cb36e62"></a>

```c
enum usb_dfu_status {
    ERR_OK = 0x00,
    ERR_TARGET = 0x01,
    ERR_FILE = 0x02,
    ERR_WRITE = 0x03,
    ERR_ERASE = 0x04,
    ERR_CHECK_ERASED = 0x05,
    ERR_PROG = 0x06,
    ERR_VERIFY = 0x07,
    ERR_ADDRESS = 0x08,
    ERR_NOTDONE = 0x09,
    ERR_FIRMWARE = 0x0A,
    ERR_VENDOR = 0x0B,
    ERR_USBR = 0x0C,
    ERR_POR = 0x0D,
    ERR_UNKNOWN = 0x0E,
    ERR_STALLEDPKT = 0x0F
}
```



相关声明：[usb_dfu_status](P187_DFU设备类头文件接口.md#a3c39293bedc430e245f3f0919cb36e62)、[ERR_OK](P187_DFU设备类头文件接口.md#a3c39293bedc430e245f3f0919cb36e62aa26c163b80b1f6786ca81dadc14b00fb)、[ERR_TARGET](P187_DFU设备类头文件接口.md#a3c39293bedc430e245f3f0919cb36e62a86a37904a04f8a7ddc9831e85d826a5a)、[ERR_FILE](P187_DFU设备类头文件接口.md#a3c39293bedc430e245f3f0919cb36e62a1a945da4703d6f5953ea81519dcaaaad)、[ERR_WRITE](P187_DFU设备类头文件接口.md#a3c39293bedc430e245f3f0919cb36e62a7b2c2fd2edcf9479181e72ee6ef6fffc)、[ERR_ERASE](P187_DFU设备类头文件接口.md#a3c39293bedc430e245f3f0919cb36e62a7f528dddca00563b477800a95163a347)、[ERR_CHECK_ERASED](P187_DFU设备类头文件接口.md#a3c39293bedc430e245f3f0919cb36e62aaaefe7b6fd4399eb00ed391833956103)、[ERR_PROG](P187_DFU设备类头文件接口.md#a3c39293bedc430e245f3f0919cb36e62a97067bf5865840561ec9eba092838e9a)、[ERR_VERIFY](P187_DFU设备类头文件接口.md#a3c39293bedc430e245f3f0919cb36e62a7b3dcb9b918d6e5af83b68d4fb767274)、[ERR_ADDRESS](P187_DFU设备类头文件接口.md#a3c39293bedc430e245f3f0919cb36e62a8c7d94233447f239b74aeea63cb8e09d)、[ERR_NOTDONE](P187_DFU设备类头文件接口.md#a3c39293bedc430e245f3f0919cb36e62a1d02e2949a0d4e292140efe5742c79a6)、[ERR_FIRMWARE](P187_DFU设备类头文件接口.md#a3c39293bedc430e245f3f0919cb36e62a4f5e97d0bc125828f2c779c11426367c)、[ERR_VENDOR](P187_DFU设备类头文件接口.md#a3c39293bedc430e245f3f0919cb36e62a98b47a7a9e4e6f1442d76fa668a6ff49)、[ERR_USBR](P187_DFU设备类头文件接口.md#a3c39293bedc430e245f3f0919cb36e62add41639f9db3a8cc4c0183c039c2b6ed)、[ERR_POR](P187_DFU设备类头文件接口.md#a3c39293bedc430e245f3f0919cb36e62a6532abde77d62a3154cb1ee22a5bce0b)、[ERR_UNKNOWN](P187_DFU设备类头文件接口.md#a3c39293bedc430e245f3f0919cb36e62a5c708decdcbd7d8c9fddd8d9e75828a1)、[ERR_STALLEDPKT](P187_DFU设备类头文件接口.md#a3c39293bedc430e245f3f0919cb36e62a614b66b2b507a2c6343462f94582cecb)。

<a id="r_a9096f7fb11c9d84692bc677d8218d01e"></a>

```c
enum usb_dfu_state {
    APP_IDLE = 0,
    APP_DETACH = 1,
    DFU_IDLE = 2,
    DFU_DNLOAD_SYNC = 3,
    DFU_DNBUSY = 4,
    DFU_DNLOAD_IDLE = 5,
    DFU_MANIFEST_SYNC = 6,
    DFU_MANIFEST = 7,
    DFU_MANIFEST_WAIT_RST = 8,
    DFU_UPLOAD_IDLE = 9,
    DFU_ERROR = 10,
    DFU_STATE_MAX = 11
}
```



相关声明：[usb_dfu_state](P187_DFU设备类头文件接口.md#a9096f7fb11c9d84692bc677d8218d01e)、[APP_IDLE](P187_DFU设备类头文件接口.md#a9096f7fb11c9d84692bc677d8218d01eab7ba8c8ed2c179fec88a9b6aafc663f0)、[APP_DETACH](P187_DFU设备类头文件接口.md#a9096f7fb11c9d84692bc677d8218d01ea1b6cb3fe0a26dce8a6fce9f179aa23ef)、[DFU_IDLE](P187_DFU设备类头文件接口.md#a9096f7fb11c9d84692bc677d8218d01ea6750bb1bc3aa5e183a24e5f1eebbc134)、[DFU_DNLOAD_SYNC](P187_DFU设备类头文件接口.md#a9096f7fb11c9d84692bc677d8218d01eac112f5ac931419fca913cc4791c768cc)、[DFU_DNBUSY](P187_DFU设备类头文件接口.md#a9096f7fb11c9d84692bc677d8218d01ea6c7e0d5ef61f350a4719b0d637dae263)、[DFU_DNLOAD_IDLE](P187_DFU设备类头文件接口.md#a9096f7fb11c9d84692bc677d8218d01eaf6596caed39e4fc9a86c86fc48fb04ea)、[DFU_MANIFEST_SYNC](P187_DFU设备类头文件接口.md#a9096f7fb11c9d84692bc677d8218d01eadf68d3fd97017e0caba53637e530fc1d)、[DFU_MANIFEST](P187_DFU设备类头文件接口.md#a9096f7fb11c9d84692bc677d8218d01ea7b90825d89b39d39d150336fe251982c)、[DFU_MANIFEST_WAIT_RST](P187_DFU设备类头文件接口.md#a9096f7fb11c9d84692bc677d8218d01ea5c827ad80eccc0249ee7ada76f36a8ac)、[DFU_UPLOAD_IDLE](P187_DFU设备类头文件接口.md#a9096f7fb11c9d84692bc677d8218d01eaf56d835eb6704702c3ddf5134402f82a)、[DFU_ERROR](P187_DFU设备类头文件接口.md#a9096f7fb11c9d84692bc677d8218d01eafc200a88839dcdee3b90417f52b35657)、[DFU_STATE_MAX](P187_DFU设备类头文件接口.md#a9096f7fb11c9d84692bc677d8218d01ea24195d3c70ed2d81039d3a0e306b3c94)。

## 187.5\_详细说明（Detailed Documentation）

<a id="ae5b7a3271bc417852f829a9d913a0e43"></a>

### 187.5.1\_`USB_DESC_DFU_FUNCTIONAL`

```c
#define USB_DESC_DFU_FUNCTIONAL 0x21
```

<a id="a22c5740401995633128679a460d4a2ef"></a>

### 187.5.2\_`USB_DFU_ATTR_CAN_DNLOAD`

```c
#define USB_DFU_ATTR_CAN_DNLOAD BIT(0)
```

<a id="a40264d92194b790a6b285c1aefa0cc3c"></a>

### 187.5.3\_`USB_DFU_ATTR_CAN_UPLOAD`

```c
#define USB_DFU_ATTR_CAN_UPLOAD BIT(1)
```

<a id="a645a02847a4ff2b47ce93be8c90168eb"></a>

### 187.5.4\_`USB_DFU_ATTR_MANIFESTATION_TOLERANT`

```c
#define USB_DFU_ATTR_MANIFESTATION_TOLERANT BIT(2)
```

<a id="a005e5b7fc18c066ee61ae393a2ba09c7"></a>

### 187.5.5\_`USB_DFU_ATTR_WILL_DETACH`

```c
#define USB_DFU_ATTR_WILL_DETACH BIT(3)
```

<a id="a501a899e415cb37503f446cc54cb64ed"></a>

### 187.5.6\_`USB_DFU_PROTOCOL_DFU`

```c
#define USB_DFU_PROTOCOL_DFU 0x02
```

<a id="a0f6bc7bb8b073e9a19a6a77524dde1a1"></a>

### 187.5.7\_`USB_DFU_PROTOCOL_RUNTIME`

```c
#define USB_DFU_PROTOCOL_RUNTIME 0x01
```

<a id="a9e54b63df02eac63afd493b4ec8ba8dd"></a>

### 187.5.8\_`USB_DFU_REQ_ABORT`

```c
#define USB_DFU_REQ_ABORT 0x06
```

<a id="a1fb983580f4fc40ceec78b7bb7398126"></a>

### 187.5.9\_`USB_DFU_REQ_CLRSTATUS`

```c
#define USB_DFU_REQ_CLRSTATUS 0x04
```

<a id="a083ab5fb2b7ea064ba0caeeba9ecba73"></a>

### 187.5.10\_`USB_DFU_REQ_DETACH`

```c
#define USB_DFU_REQ_DETACH 0x00
```

<a id="a54e31f9cb963e35caaf8049a8116ab52"></a>

### 187.5.11\_`USB_DFU_REQ_DNLOAD`

```c
#define USB_DFU_REQ_DNLOAD 0x01
```

<a id="aca55ad0b7ee615c5414aa518c94af345"></a>

### 187.5.12\_`USB_DFU_REQ_GETSTATE`

```c
#define USB_DFU_REQ_GETSTATE 0x05
```

<a id="afebeea3c212557b2c17dbf8549b42681"></a>

### 187.5.13\_`USB_DFU_REQ_GETSTATUS`

```c
#define USB_DFU_REQ_GETSTATUS 0x03
```

<a id="ac3118cca70abbc4e08a6cb58ce439f71"></a>

### 187.5.14\_`USB_DFU_REQ_UPLOAD`

```c
#define USB_DFU_REQ_UPLOAD 0x02
```

<a id="a518e936748d79f70576e082604203ae7"></a>

### 187.5.15\_`USB_DFU_SUBCLASS`

```c
#define USB_DFU_SUBCLASS 0x01
```

<a id="aa3f88d63fbd9542614b6057da9c133e5"></a>

### 187.5.16\_`USB_DFU_VERSION`

```c
#define USB_DFU_VERSION 0x0110
```

<a id="a9096f7fb11c9d84692bc677d8218d01e"></a>

### 187.5.17\_`usb_dfu_state`

```c
enum usb_dfu_state
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `APP_IDLE` |  |
| `APP_DETACH` |  |
| `DFU_IDLE` |  |
| `DFU_DNLOAD_SYNC` |  |
| `DFU_DNBUSY` |  |
| `DFU_DNLOAD_IDLE` |  |
| `DFU_MANIFEST_SYNC` |  |
| `DFU_MANIFEST` |  |
| `DFU_MANIFEST_WAIT_RST` |  |
| `DFU_UPLOAD_IDLE` |  |
| `DFU_ERROR` |  |
| `DFU_STATE_MAX` |  |

> 译注（源码核对）：DFU_STATE_MAX = 11 是当前实现用于检查状态表长度的上界。dfu_state_string() 只接受小于该值的状态；不能将这个表长标记当成额外的协议状态。

<a id="a3c39293bedc430e245f3f0919cb36e62"></a>

### 187.5.18\_`usb_dfu_status`

```c
enum usb_dfu_status
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `ERR_OK` |  |
| `ERR_TARGET` |  |
| `ERR_FILE` |  |
| `ERR_WRITE` |  |
| `ERR_ERASE` |  |
| `ERR_CHECK_ERASED` |  |
| `ERR_PROG` |  |
| `ERR_VERIFY` |  |
| `ERR_ADDRESS` |  |
| `ERR_NOTDONE` |  |
| `ERR_FIRMWARE` |  |
| `ERR_VENDOR` |  |
| `ERR_USBR` |  |
| `ERR_POR` |  |
| `ERR_UNKNOWN` |  |
| `ERR_STALLEDPKT` |  |

> 译注（源码核对）：本版标识符为 ERR_USBR = 0x0C，旧版对应名称为 errUSB；这里保留上游拼写和数值，不自行改名。它们是 DFU 协议状态码，不是 Zephyr 的负 errno 返回值。

## 187.6\_源码跟踪与使用边界

译注依据保存的[旧版 DFU 头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usb_dfu.h)、[新版 DFU 头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/usb/class/usbd_dfu.h)、[新版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device_next/class/usbd_dfu.c)及[旧版实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/usb/device/class/dfu/usb_dfu.c)，摘要见[来源记录](../SOURCES.md)。仓库内[旧版头文件](../../../include/zephyr/usb/class/usb_dfu.h)、[新版头文件](../../../include/zephyr/usb/class/usbd_dfu.h)、[新版实现](../../../subsys/usb/device_next/class/usbd_dfu.c)与[旧版实现](../../../subsys/usb/device/class/dfu/usb_dfu.c)用于相对路径跟踪，版本可能与官网不同。

本批未构建固件、执行镜像下载、擦写 Flash 或验证重启后的镜像。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-define-members"></a>
<a id="define-members"></a>
<a id="header-enum-members"></a>
<a id="enum-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a9096f7fb11c9d84692bc677d8218d01eab7ba8c8ed2c179fec88a9b6aafc663f0"></a>
<a id="a9096f7fb11c9d84692bc677d8218d01ea1b6cb3fe0a26dce8a6fce9f179aa23ef"></a>
<a id="a9096f7fb11c9d84692bc677d8218d01ea6750bb1bc3aa5e183a24e5f1eebbc134"></a>
<a id="a9096f7fb11c9d84692bc677d8218d01eac112f5ac931419fca913cc4791c768cc"></a>
<a id="a9096f7fb11c9d84692bc677d8218d01ea6c7e0d5ef61f350a4719b0d637dae263"></a>
<a id="a9096f7fb11c9d84692bc677d8218d01eaf6596caed39e4fc9a86c86fc48fb04ea"></a>
<a id="a9096f7fb11c9d84692bc677d8218d01eadf68d3fd97017e0caba53637e530fc1d"></a>
<a id="a9096f7fb11c9d84692bc677d8218d01ea7b90825d89b39d39d150336fe251982c"></a>
<a id="a9096f7fb11c9d84692bc677d8218d01ea5c827ad80eccc0249ee7ada76f36a8ac"></a>
<a id="a9096f7fb11c9d84692bc677d8218d01eaf56d835eb6704702c3ddf5134402f82a"></a>
<a id="a9096f7fb11c9d84692bc677d8218d01eafc200a88839dcdee3b90417f52b35657"></a>
<a id="a9096f7fb11c9d84692bc677d8218d01ea24195d3c70ed2d81039d3a0e306b3c94"></a>
<a id="a3c39293bedc430e245f3f0919cb36e62aa26c163b80b1f6786ca81dadc14b00fb"></a>
<a id="a3c39293bedc430e245f3f0919cb36e62a86a37904a04f8a7ddc9831e85d826a5a"></a>
<a id="a3c39293bedc430e245f3f0919cb36e62a1a945da4703d6f5953ea81519dcaaaad"></a>
<a id="a3c39293bedc430e245f3f0919cb36e62a7b2c2fd2edcf9479181e72ee6ef6fffc"></a>
<a id="a3c39293bedc430e245f3f0919cb36e62a7f528dddca00563b477800a95163a347"></a>
<a id="a3c39293bedc430e245f3f0919cb36e62aaaefe7b6fd4399eb00ed391833956103"></a>
<a id="a3c39293bedc430e245f3f0919cb36e62a97067bf5865840561ec9eba092838e9a"></a>
<a id="a3c39293bedc430e245f3f0919cb36e62a7b3dcb9b918d6e5af83b68d4fb767274"></a>
<a id="a3c39293bedc430e245f3f0919cb36e62a8c7d94233447f239b74aeea63cb8e09d"></a>
<a id="a3c39293bedc430e245f3f0919cb36e62a1d02e2949a0d4e292140efe5742c79a6"></a>
<a id="a3c39293bedc430e245f3f0919cb36e62a4f5e97d0bc125828f2c779c11426367c"></a>
<a id="a3c39293bedc430e245f3f0919cb36e62a98b47a7a9e4e6f1442d76fa668a6ff49"></a>
<a id="a3c39293bedc430e245f3f0919cb36e62add41639f9db3a8cc4c0183c039c2b6ed"></a>
<a id="a3c39293bedc430e245f3f0919cb36e62a6532abde77d62a3154cb1ee22a5bce0b"></a>
<a id="a3c39293bedc430e245f3f0919cb36e62a5c708decdcbd7d8c9fddd8d9e75828a1"></a>
<a id="a3c39293bedc430e245f3f0919cb36e62a614b66b2b507a2c6343462f94582cecb"></a>

[上一章](P186_DFU公共头文件源码.md) · [返回大纲](大纲.md) · [下一章](P188_DFU设备类头文件源码.md)
