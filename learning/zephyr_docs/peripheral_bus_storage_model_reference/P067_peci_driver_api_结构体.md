---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-67
title: peci_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpeci__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_peci\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpeci__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：平台环境控制接口（PECI）驱动操作。

```c
#include <zephyr/drivers/peci.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：平台环境控制接口（PECI）驱动操作。这是每个 PECI 驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 67.1\_数据成员（Data Fields）

<a id="r_ae41c38a71a700e8a5808218fbb639fcc"></a>

```c
peci_config_t config
```

相关声明：[peci_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#gabdb55d1aeea952970562c58f7c901361)、[config](#ae41c38a71a700e8a5808218fbb639fcc)。

`REQ`：配置平台环境控制接口（PECI）。

<a id="r_a718840a487a31212a042d36cbf3119c7"></a>

```c
peci_disable_t disable
```

相关声明：[peci_disable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#ga97cd68ca4d0b79a6ff8fc19828e0cb76)、[disable](#a718840a487a31212a042d36cbf3119c7)。

`REQ`：禁用 PECI 接口。

<a id="r_a2adf7c329d2b95cea596e5639fbe9e09"></a>

```c
peci_enable_t enable
```

相关声明：[peci_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#ga60a85f356ed8f18050f1a4cd02389c77)、[enable](#a2adf7c329d2b95cea596e5639fbe9e09)。

`REQ`：启用 PECI 接口。

<a id="r_a0ca94e90b589beb0ab525ee141be6b49"></a>

```c
peci_transfer_t transfer
```

相关声明：[peci_transfer_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#ga3addf7ae61d89626f7d8889910c6f5b9)、[transfer](#a0ca94e90b589beb0ab525ee141be6b49)。

`REQ`：执行 PECI 事务。

## 67.2\_详细说明（Detailed Documentation）

<a id="ae41c38a71a700e8a5808218fbb639fcc"></a>

### `config`

```c
peci_config_t peci_driver_api::config
```

`REQ`：配置平台环境控制接口（PECI）。

<a id="a718840a487a31212a042d36cbf3119c7"></a>

### `disable`

```c
peci_disable_t peci_driver_api::disable
```

`REQ`：禁用 PECI 接口。

<a id="a2adf7c329d2b95cea596e5639fbe9e09"></a>

### `enable`

```c
peci_enable_t peci_driver_api::enable
```

`REQ`：启用 PECI 接口。

<a id="a0ca94e90b589beb0ab525ee141be6b49"></a>

### `transfer`

```c
peci_transfer_t peci_driver_api::transfer
```

`REQ`：执行 PECI 事务。

本数据类型文档由以下文件生成：

- `zephyr/drivers/peci.h`

## 67.3\_原页交叉引用（Cross References）

- [zephyr/drivers/peci.h](https://docs.zephyrproject.org/latest/doxygen/html/peci_8h_source.html)
- [peci_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#gabdb55d1aeea952970562c58f7c901361)
- [peci_disable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#ga97cd68ca4d0b79a6ff8fc19828e0cb76)
- [peci_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#ga60a85f356ed8f18050f1a4cd02389c77)
- [peci_transfer_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#ga3addf7ae61d89626f7d8889910c6f5b9)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P066_peci_buf_结构体.md) · [返回大纲](大纲.md) · [下一章](P068_peci_msg_结构体.md)
