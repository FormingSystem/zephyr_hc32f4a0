---
id: learning.zephyr-docs.device-power-control-model-reference.page-93
title: tcpc_chip_info_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtcpc__chip__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第93章\_tcpc\_chip\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtcpc__chip__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Type-C端口控制器（TCPC）的芯片信息。

```c
#include <zephyr/drivers/usb_c/usbc_tcpc.h>
```

<a id="details"></a>

Type-C端口控制器（TCPC）的芯片信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 93.1\_数据成员（Data Fields）

<a id="r_ab48400ea4209d5443e5b7e0bfee6c4fc"></a>

```c
uint16_t vendor_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[vendor_id](#ab48400ea4209d5443e5b7e0bfee6c4fc)。

供应商 ID（Vendor ID）。

<a id="r_a14c11999ef548e41f4338f3e7208b7a9"></a>

```c
uint16_t product_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[product_id](#a14c11999ef548e41f4338f3e7208b7a9)。

产品 ID（Product ID）。

<a id="r_a9e76ee3bcc395dbb77d7a065f6181cd6"></a>

```c
uint16_t device_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[device_id](#a9e76ee3bcc395dbb77d7a065f6181cd6)。

设备 ID（Device ID）。

<a id="r_a7789339580e2774d18a8f4c78332f774"></a>

```c
uint64_t fw_version_number
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[fw_version_number](#a7789339580e2774d18a8f4c78332f774)。

固件版本号。

```c
union {
```

<a id="r_adb3fa181590ac13ffb5cf3af4294a10a"></a>

```c
uint8_t min_req_fw_version_string [8]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[min_req_fw_version_string](#a677a85ef27f0d5db969ce3232506d1bb)。

所需的最低固件版本字符串。

<a id="r_ae5ceb81e2fc71aebb618d488844055d6"></a>

```c
uint64_t min_req_fw_version_number
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[min_req_fw_version_number](#a8d66f33379493e1a0ed707b3715f863a)。

所需的最低固件版本号。

<a id="r_ab0964dfb0a6ea8d41373be2b4989f9b3"></a>

```c
};
```

所需的最低固件版本，以字符串或数字表示。

## 93.2\_详细说明（Detailed Documentation）

<a id="ab0964dfb0a6ea8d41373be2b4989f9b3"></a>

### `[union]`

```c
union { ... } tcpc_chip_info
```

所需的最低固件版本，以字符串或数字表示。

<a id="a9e76ee3bcc395dbb77d7a065f6181cd6"></a>

### `device_id`

```c
uint16_t tcpc_chip_info::device_id
```

设备 ID（Device ID）。

<a id="a7789339580e2774d18a8f4c78332f774"></a>

### `fw_version_number`

```c
uint64_t tcpc_chip_info::fw_version_number
```

固件版本号。

<a id="a8d66f33379493e1a0ed707b3715f863a"></a>

### `min_req_fw_version_number`

```c
uint64_t tcpc_chip_info::min_req_fw_version_number
```

所需的最低固件版本号。

<a id="a677a85ef27f0d5db969ce3232506d1bb"></a>

### `min_req_fw_version_string`

```c
uint8_t tcpc_chip_info::min_req_fw_version_string[8]
```

所需的最低固件版本字符串。

<a id="a14c11999ef548e41f4338f3e7208b7a9"></a>

### `product_id`

```c
uint16_t tcpc_chip_info::product_id
```

产品 ID（Product ID）。

<a id="ab48400ea4209d5443e5b7e0bfee6c4fc"></a>

### `vendor_id`

```c
uint16_t tcpc_chip_info::vendor_id
```

供应商 ID（Vendor ID）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/usb_c/usbc_tcpc.h`

## 93.3\_原页交叉引用（Cross References）

- [zephyr/drivers/usb_c/usbc_tcpc.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__tcpc_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [tcpc_chip_info](P093_tcpc_chip_info_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P092_svc_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P094_tcpc_driver_api_结构体.md)
