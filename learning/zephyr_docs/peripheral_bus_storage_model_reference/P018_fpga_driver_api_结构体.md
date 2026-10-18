---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-18
title: fpga_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structfpga__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_fpga\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structfpga__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：现场可编程门阵列（FPGA）驱动操作。

```c
#include <zephyr/drivers/fpga.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：现场可编程门阵列（FPGA）驱动操作。这是每个 FPGA 驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 18.1\_数据成员（Data Fields）

<a id="r_aee587fbff9464efc2ab64c6187346d28"></a>

```c
fpga_api_get_status get_status
```

相关声明：[fpga_api_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga02d71e7a82f446220d67664d4cc7a5c9)、[get_status](#aee587fbff9464efc2ab64c6187346d28)。

`OPT`：读取现场可编程门阵列（FPGA）的状态。

<a id="r_ab3b316a07f35610b5bb00cd6c89fa0f1"></a>

```c
fpga_api_reset reset
```

相关声明：[fpga_api_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga3c53b90b9d0b50c44c01a534c61e9212)、[reset](#ab3b316a07f35610b5bb00cd6c89fa0f1)。

`OPT`：复位 FPGA。

<a id="r_a1a56d32b7e1c9931b7ddca9f802baecc"></a>

```c
fpga_api_load load
```

相关声明：[fpga_api_load](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga9860c64bbc2cfb89df9b51da655691b6)、[load](#a1a56d32b7e1c9931b7ddca9f802baecc)。

`OPT`：加载位流（Bitstream）并配置 FPGA。

<a id="r_a0dedc3ce6e6ac23b9907af1ebbddaa56"></a>

```c
fpga_api_on on
```

相关声明：[fpga_api_on](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#gaf3e8ea5d443fd09352e2b63f82a459be)、[on](#a0dedc3ce6e6ac23b9907af1ebbddaa56)。

`OPT`：开启 FPGA。

<a id="r_a89de57caf9882098e9c5f42f35bff2a3"></a>

```c
fpga_api_off off
```

相关声明：[fpga_api_off](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga872a8d75bb46de50a41b56170804ed27)、[off](#a89de57caf9882098e9c5f42f35bff2a3)。

`OPT`：关闭 FPGA。

<a id="r_aa2107eb303cc2e538441ba1058630ab4"></a>

```c
fpga_api_get_info get_info
```

相关声明：[fpga_api_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga24fd6ce4832b960b79914f42010774aa)、[get_info](#aa2107eb303cc2e538441ba1058630ab4)。

`OPT`：返回 FPGA 的相关信息。

## 18.2\_详细说明（Detailed Documentation）

<a id="aa2107eb303cc2e538441ba1058630ab4"></a>

### `get_info`

```c
fpga_api_get_info fpga_driver_api::get_info
```

`OPT`：返回 FPGA 的相关信息。

<a id="aee587fbff9464efc2ab64c6187346d28"></a>

### `get_status`

```c
fpga_api_get_status fpga_driver_api::get_status
```

`OPT`：读取现场可编程门阵列（FPGA）的状态。

<a id="a1a56d32b7e1c9931b7ddca9f802baecc"></a>

### `load`

```c
fpga_api_load fpga_driver_api::load
```

`OPT`：加载位流（Bitstream）并配置 FPGA。

<a id="a89de57caf9882098e9c5f42f35bff2a3"></a>

### `off`

```c
fpga_api_off fpga_driver_api::off
```

`OPT`：关闭 FPGA。

<a id="a0dedc3ce6e6ac23b9907af1ebbddaa56"></a>

### `on`

```c
fpga_api_on fpga_driver_api::on
```

`OPT`：开启 FPGA。

<a id="ab3b316a07f35610b5bb00cd6c89fa0f1"></a>

### `reset`

```c
fpga_api_reset fpga_driver_api::reset
```

`OPT`：复位 FPGA。

本数据类型文档由以下文件生成：

- `zephyr/drivers/fpga.h`

## 18.3\_原页交叉引用（Cross References）

- [zephyr/drivers/fpga.h](https://docs.zephyrproject.org/latest/doxygen/html/fpga_8h_source.html)
- [fpga_api_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga02d71e7a82f446220d67664d4cc7a5c9)
- [fpga_api_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga3c53b90b9d0b50c44c01a534c61e9212)
- [fpga_api_load](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga9860c64bbc2cfb89df9b51da655691b6)
- [fpga_api_on](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#gaf3e8ea5d443fd09352e2b63f82a459be)
- [fpga_api_off](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga872a8d75bb46de50a41b56170804ed27)
- [fpga_api_get_info](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface__backend.html#ga24fd6ce4832b960b79914f42010774aa)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P017_espi_saf_packet_结构体.md) · [返回大纲](大纲.md) · [下一章](P019_lin_config_结构体.md)
