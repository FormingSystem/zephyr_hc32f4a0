---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-95
title: w1_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structw1__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第95章\_w1\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structw1__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：单总线（1-Wire）驱动操作。

```c
#include <zephyr/drivers/w1.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：1-Wire驱动操作。这是每个 1-Wire 驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 95.1\_数据成员（Data Fields）

<a id="r_a2c3312afc1929fafed6db5607e4f7d2c"></a>

```c
w1_reset_bus_t reset_bus
```

相关声明：[w1_reset_bus_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga87232322cd487772d377aa0a8e9e5bfc)、[reset_bus](#a2c3312afc1929fafed6db5607e4f7d2c)。

`REQ`：复位单总线（1-Wire），使从设备准备通信。

<a id="r_ae7d6cef0458e281c1b653a4e6ecbe3f1"></a>

```c
w1_read_bit_t read_bit
```

相关声明：[w1_read_bit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gabb495014dd7b9583009b34d9eba02ddc)、[read_bit](#ae7d6cef0458e281c1b653a4e6ecbe3f1)。

`REQ`：从 1-Wire 总线读取单个位。

<a id="r_ac89908044403cd1d8768425617bd1b86"></a>

```c
w1_write_bit_t write_bit
```

相关声明：[w1_write_bit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga126e501ef9a74cbc3c375ca64025cdbc)、[write_bit](#ac89908044403cd1d8768425617bd1b86)。

`REQ`：向 1-Wire 总线写入单个位。

<a id="r_aec4d570356600e1c769626d3cb9e75f2"></a>

```c
w1_read_byte_t read_byte
```

相关声明：[w1_read_byte_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga861af0744a5f102558294422de50f6ae)、[read_byte](#aec4d570356600e1c769626d3cb9e75f2)。

`REQ`：从 1-Wire 总线读取单个字节。

<a id="r_ae930e72652123e0f616ed59ebf179f0c"></a>

```c
w1_write_byte_t write_byte
```

相关声明：[w1_write_byte_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga18924f833820d5f70d73ab33de6615dd)、[write_byte](#ae930e72652123e0f616ed59ebf179f0c)。

`REQ`：向 1-Wire 总线写入单个字节。

<a id="r_a84f92f1c855550e54a4c5d53e72af5c7"></a>

```c
w1_read_block_t read_block
```

相关声明：[w1_read_block_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gae2673a21841ad196af69e5b4e6769ea8)、[read_block](#a84f92f1c855550e54a4c5d53e72af5c7)。

`OPT`：从 1-Wire 总线读取一个数据块。

<a id="r_a145e07fc821cf21795db761f6c82d650"></a>

```c
w1_write_block_t write_block
```

相关声明：[w1_write_block_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gafbbba20705697154d29a91ac94cc3747)、[write_block](#a145e07fc821cf21795db761f6c82d650)。

`OPT`：向 1-Wire 总线写入一个数据块。

<a id="r_a1ee0dae9846d2e7ba9a016d3333b040e"></a>

```c
w1_configure_t configure
```

相关声明：[w1_configure_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gab831da9314fce3e6ec10526ca5224515)、[configure](#a1ee0dae9846d2e7ba9a016d3333b040e)。

`REQ`：配置 1-Wire 主机的参数。

<a id="r_a34ea6f69f0cc3502a5639f7a5a3c3c1f"></a>

```c
w1_change_bus_lock_t change_bus_lock
```

相关声明：[w1_change_bus_lock_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gaa64e8b894df8a3a44f3b91ea647cc0c1)、[change_bus_lock](#a34ea6f69f0cc3502a5639f7a5a3c3c1f)。

`OPT`：锁定或解锁总线访问。

## 95.2\_详细说明（Detailed Documentation）

<a id="a34ea6f69f0cc3502a5639f7a5a3c3c1f"></a>

### `change_bus_lock`

```c
w1_change_bus_lock_t w1_driver_api::change_bus_lock
```

`OPT`：锁定或解锁总线访问。

如果未实现此操作，子系统会使用基于互斥锁（Mutex）的锁作为后备方案。

<a id="a1ee0dae9846d2e7ba9a016d3333b040e"></a>

### `configure`

```c
w1_configure_t w1_driver_api::configure
```

`REQ`：配置 1-Wire 主机的参数。

<a id="ae7d6cef0458e281c1b653a4e6ecbe3f1"></a>

### `read_bit`

```c
w1_read_bit_t w1_driver_api::read_bit
```

`REQ`：从 1-Wire 总线读取单个位。

<a id="a84f92f1c855550e54a4c5d53e72af5c7"></a>

### `read_block`

```c
w1_read_block_t w1_driver_api::read_block
```

`OPT`：从 1-Wire 总线读取一个数据块。

如果未实现此操作，子系统会通过重复调用 `w1_driver_api::read_byte` 完成读取。

<a id="aec4d570356600e1c769626d3cb9e75f2"></a>

### `read_byte`

```c
w1_read_byte_t w1_driver_api::read_byte
```

`REQ`：从 1-Wire 总线读取单个字节。

<a id="a2c3312afc1929fafed6db5607e4f7d2c"></a>

### `reset_bus`

```c
w1_reset_bus_t w1_driver_api::reset_bus
```

`REQ`：复位单总线（1-Wire），使从设备准备通信。

<a id="ac89908044403cd1d8768425617bd1b86"></a>

### `write_bit`

```c
w1_write_bit_t w1_driver_api::write_bit
```

`REQ`：向 1-Wire 总线写入单个位。

<a id="a145e07fc821cf21795db761f6c82d650"></a>

### `write_block`

```c
w1_write_block_t w1_driver_api::write_block
```

`OPT`：向 1-Wire 总线写入一个数据块。

如果未实现此操作，子系统会通过重复调用 `w1_driver_api::write_byte` 完成写入。

<a id="ae930e72652123e0f616ed59ebf179f0c"></a>

### `write_byte`

```c
w1_write_byte_t w1_driver_api::write_byte
```

`REQ`：向 1-Wire 总线写入单个字节。

本数据类型文档由以下文件生成：

- `zephyr/drivers/w1.h`

## 95.3\_原页交叉引用（Cross References）

- [zephyr/drivers/w1.h](https://docs.zephyrproject.org/latest/doxygen/html/w1_8h_source.html)
- [w1_reset_bus_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga87232322cd487772d377aa0a8e9e5bfc)
- [w1_read_bit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gabb495014dd7b9583009b34d9eba02ddc)
- [w1_write_bit_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga126e501ef9a74cbc3c375ca64025cdbc)
- [w1_read_byte_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga861af0744a5f102558294422de50f6ae)
- [w1_write_byte_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#ga18924f833820d5f70d73ab33de6615dd)
- [w1_read_block_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gae2673a21841ad196af69e5b4e6769ea8)
- [w1_write_block_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gafbbba20705697154d29a91ac94cc3747)
- [w1_configure_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gab831da9314fce3e6ec10526ca5224515)
- [w1_change_bus_lock_t](https://docs.zephyrproject.org/latest/doxygen/html/group__w1__interface__backend.html#gaa64e8b894df8a3a44f3b91ea647cc0c1)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P094_swdp_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P096_w1_master_config_结构体.md)
