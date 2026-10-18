---
id: learning.zephyr-docs.device-power-control-model-reference.page-101
title: usbc_vbus_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structusbc__vbus__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第101章\_usbc\_vbus\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structusbc__vbus__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：USB-C VBUS驱动操作。

```c
#include <zephyr/drivers/usb_c/usbc_vbus.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：USB-C VBUS 驱动操作。这是每个 USB-C VBUS 驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 101.1\_数据成员（Data Fields）

<a id="r_adce9dc1f3065a029b53ee954d734cfac"></a>

```c
bool(* check_level )(const struct device *dev, enum tc_vbus_level level)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[check_level](#adce9dc1f3065a029b53ee954d734cfac)、[device](../device_reference/P002_设备对象结构.md)、[tc_vbus_level](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga015455a6c5620dfc96cfb713bbb72161)。

`REQ`：检查 VBUS 是否处于指定电平。

<a id="r_a373b4435b3e4a1a88a78a15d24bdcbab"></a>

```c
int(* measure )(const struct device *dev, int *vbus_meas)
```

相关声明：[measure](#a373b4435b3e4a1a88a78a15d24bdcbab)、[device](../device_reference/P002_设备对象结构.md)。

`REQ`：读取并返回以 mV 为单位的 VBUS 测量值。

<a id="r_a164ae753995e293460fc408edebe21df"></a>

```c
int(* discharge )(const struct device *dev, bool enable)
```

相关声明：[discharge](#a164ae753995e293460fc408edebe21df)、[device](../device_reference/P002_设备对象结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enable](#a5a7e6383279dc17c01d478a063efcac0)。

`REQ`：控制用于对 VBUS 放电的引脚。

<a id="r_a5a7e6383279dc17c01d478a063efcac0"></a>

```c
int(* enable )(const struct device *dev, bool enable)
```

相关声明：[enable](#a5a7e6383279dc17c01d478a063efcac0)、[device](../device_reference/P002_设备对象结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

`REQ`：控制用于启用 VBUS 测量的引脚。

## 101.2\_详细说明（Detailed Documentation）

<a id="adce9dc1f3065a029b53ee954d734cfac"></a>

### `check_level`

```c
bool(* usbc_vbus_driver_api::check_level) (const struct device *dev, enum tc_vbus_level level)
```

`REQ`：检查 VBUS 是否处于指定电平。

<a id="a164ae753995e293460fc408edebe21df"></a>

### `discharge`

```c
int(* usbc_vbus_driver_api::discharge) (const struct device *dev, bool enable)
```

`REQ`：控制用于对 VBUS 放电的引脚。

<a id="a5a7e6383279dc17c01d478a063efcac0"></a>

### `enable`

```c
int(* usbc_vbus_driver_api::enable) (const struct device *dev, bool enable)
```

`REQ`：控制用于启用 VBUS 测量的引脚。

<a id="a373b4435b3e4a1a88a78a15d24bdcbab"></a>

### `measure`

```c
int(* usbc_vbus_driver_api::measure) (const struct device *dev, int *vbus_meas)
```

`REQ`：读取并返回以 mV 为单位的 VBUS 测量值。

本数据类型文档由以下文件生成：

- `zephyr/drivers/usb_c/usbc_vbus.h`

## 101.3\_原页交叉引用（Cross References）

- [zephyr/drivers/usb_c/usbc_vbus.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__vbus_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [device](../device_reference/P002_设备对象结构.md)
- [tc_vbus_level](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga015455a6c5620dfc96cfb713bbb72161)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P100_usbc_ppc_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P102_wuc_driver_api_结构体.md)
