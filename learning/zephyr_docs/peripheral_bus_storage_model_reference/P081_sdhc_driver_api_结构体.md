---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-81
title: sdhc_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsdhc__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第81章\_sdhc\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsdhc__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：SD主控制器（SDHC）驱动操作。

```c
#include <zephyr/drivers/sdhc.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：SD 主机控制器（SDHC）驱动操作。这是每个 SDHC 驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 81.1\_数据成员（Data Fields）

<a id="r_ac034dfc17e064170e76280394005c76c"></a>

```c
int(* reset )(const struct device *dev)
```

相关声明：[reset](#ac034dfc17e064170e76280394005c76c)、[device](../device_reference/P002_设备对象结构.md)。

`OPT`：复位 SDHC 控制器状态。

<a id="r_a577d162b282b2f9eeb91cf07e7578905"></a>

```c
int(* request )(const struct device *dev, struct sdhc_command *cmd, struct sdhc_data *data)
```

相关声明：[request](#a577d162b282b2f9eeb91cf07e7578905)、[device](../device_reference/P002_设备对象结构.md)、[sdhc_command](P079_sdhc_command_结构体.md)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[sdhc_data](P080_sdhc_data_结构体.md)。

`REQ`：向 SDHC 发送命令。

<a id="r_adb40a93f64a1a8dc1548a4651091ecf9"></a>

```c
int(* set_io )(const struct device *dev, struct sdhc_io *ios)
```

相关声明：[set_io](#adb40a93f64a1a8dc1548a4651091ecf9)、[device](../device_reference/P002_设备对象结构.md)、[sdhc_io](P084_sdhc_io_结构体.md)。

`REQ`：设置 SDHC 的 I/O 属性。

<a id="r_a06fb6fdfd0c528056c36476f914f94c9"></a>

```c
int(* get_card_present )(const struct device *dev)
```

相关声明：[get_card_present](#a06fb6fdfd0c528056c36476f914f94c9)、[device](../device_reference/P002_设备对象结构.md)。

`REQ`：检查 SDHC 是否检测到卡。

<a id="r_a6075f8ef38200e700ec133fbeb8c8121"></a>

```c
int(* execute_tuning )(const struct device *dev)
```

相关声明：[execute_tuning](#a6075f8ef38200e700ec133fbeb8c8121)、[device](../device_reference/P002_设备对象结构.md)。

`OPT`：执行 SDHC 调谐（Tuning）。

<a id="r_ac642c06d5ec9f697be8fa46cede3bc64"></a>

```c
int(* card_busy )(const struct device *dev)
```

相关声明：[card_busy](#ac642c06d5ec9f697be8fa46cede3bc64)、[device](../device_reference/P002_设备对象结构.md)。

`REQ`：检查 SD 卡是否忙。

<a id="r_af2b83b0ea2afbbdf065b5919c6b822c2"></a>

```c
int(* get_host_props )(const struct device *dev, struct sdhc_host_props *props)
```

相关声明：[get_host_props](#af2b83b0ea2afbbdf065b5919c6b822c2)、[device](../device_reference/P002_设备对象结构.md)、[sdhc_host_props](P083_sdhc_host_props_结构体.md)。

`REQ`：获取 SD 主机控制器属性。

<a id="r_a42941f226f2adfe5b8275923bff434ff"></a>

```c
int(* enable_interrupt )(const struct device *dev, sdhc_interrupt_cb_t callback, int sources, void *user_data)
```

相关声明：[enable_interrupt](#a42941f226f2adfe5b8275923bff434ff)、[device](../device_reference/P002_设备对象结构.md)、[sdhc_interrupt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga5d207e3b3d76ed9dbfa7d68a92755cbe)。

`OPT`：启用 SDHC 中断源。

<a id="r_aa50466e31e01d639e459bab204cf1ee5"></a>

```c
int(* disable_interrupt )(const struct device *dev, int sources)
```

相关声明：[disable_interrupt](#aa50466e31e01d639e459bab204cf1ee5)、[device](../device_reference/P002_设备对象结构.md)。

`OPT`：禁用 SDHC 中断源。

## 81.2\_详细说明（Detailed Documentation）

<a id="ac642c06d5ec9f697be8fa46cede3bc64"></a>

### `card_busy`

```c
int(* sdhc_driver_api::card_busy) (const struct device *dev)
```

`REQ`：检查 SD 卡是否忙。

<a id="aa50466e31e01d639e459bab204cf1ee5"></a>

### `disable_interrupt`

```c
int(* sdhc_driver_api::disable_interrupt) (const struct device *dev, int sources)
```

`OPT`：禁用 SDHC 中断源。

<a id="a42941f226f2adfe5b8275923bff434ff"></a>

### `enable_interrupt`

```c
int(* sdhc_driver_api::enable_interrupt) (const struct device *dev, sdhc_interrupt_cb_t callback, int sources, void *user_data)
```

`OPT`：启用 SDHC 中断源。

<a id="a6075f8ef38200e700ec133fbeb8c8121"></a>

### `execute_tuning`

```c
int(* sdhc_driver_api::execute_tuning) (const struct device *dev)
```

`OPT`：执行 SDHC 调谐（Tuning）。

<a id="a06fb6fdfd0c528056c36476f914f94c9"></a>

### `get_card_present`

```c
int(* sdhc_driver_api::get_card_present) (const struct device *dev)
```

`REQ`：检查 SDHC 是否检测到卡。

<a id="af2b83b0ea2afbbdf065b5919c6b822c2"></a>

### `get_host_props`

```c
int(* sdhc_driver_api::get_host_props) (const struct device *dev, struct sdhc_host_props *props)
```

`REQ`：获取 SD 主机控制器属性。

<a id="a577d162b282b2f9eeb91cf07e7578905"></a>

### `request`

```c
int(* sdhc_driver_api::request) (const struct device *dev, struct sdhc_command *cmd, struct sdhc_data *data)
```

`REQ`：向 SDHC 发送命令。

<a id="ac034dfc17e064170e76280394005c76c"></a>

### `reset`

```c
int(* sdhc_driver_api::reset) (const struct device *dev)
```

`OPT`：复位 SDHC 控制器状态。

<a id="adb40a93f64a1a8dc1548a4651091ecf9"></a>

### `set_io`

```c
int(* sdhc_driver_api::set_io) (const struct device *dev, struct sdhc_io *ios)
```

`REQ`：设置 SDHC 的 I/O 属性。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sdhc.h`

## 81.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sdhc.h](https://docs.zephyrproject.org/latest/doxygen/html/sdhc_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [sdhc_command](P079_sdhc_command_结构体.md)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [sdhc_data](P080_sdhc_data_结构体.md)
- [sdhc_io](P084_sdhc_io_结构体.md)
- [sdhc_host_props](P083_sdhc_host_props_结构体.md)
- [sdhc_interrupt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__sdhc__interface.html#ga5d207e3b3d76ed9dbfa7d68a92755cbe)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P080_sdhc_data_结构体.md) · [返回大纲](大纲.md) · [下一章](P082_sdhc_host_caps_结构体.md)
