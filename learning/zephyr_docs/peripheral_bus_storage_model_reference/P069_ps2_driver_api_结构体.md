---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-69
title: ps2_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structps2__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第69章\_ps2\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structps2__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：PS/2驱动操作。

```c
#include <zephyr/drivers/ps2.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：PS/2驱动操作。这是每个 PS/2 驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 69.1\_数据成员（Data Fields）

<a id="r_abe4d10c3ad967796943d95f75c659d4d"></a>

```c
ps2_config_t config
```

相关声明：[ps2_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#ga7fb2edbebe2523efde6c7f73bffb850a)、[config](#abe4d10c3ad967796943d95f75c659d4d)。

`REQ`：配置 PS/2 设备实例。

<a id="r_abfaf41cc47cabb2d1710584586e5b93c"></a>

```c
ps2_read_t read
```

相关声明：[ps2_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#ga3d5a1b7e613e0e2b1a28689b9ab52ca5)、[read](#abfaf41cc47cabb2d1710584586e5b93c)。

`REQ`：从 PS/2 设备读取从设备到主机方向的数据值。

<a id="r_add947b91f9ca9bac20fac2fbb47b87e4"></a>

```c
ps2_write_t write
```

相关声明：[ps2_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#gaf7a935b2e1debd819792dbb02bd84ee2)、[write](#add947b91f9ca9bac20fac2fbb47b87e4)。

`REQ`：向 PS/2 设备写入。

<a id="r_a485227d96921b73da2041225535be74c"></a>

```c
ps2_disable_callback_t disable_callback
```

相关声明：[ps2_disable_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#gaaa51cb5cf5f5d7560c35374561746f6d)、[disable_callback](#a485227d96921b73da2041225535be74c)。

`OPT`：禁用回调。

<a id="r_ab0cdb648761d2de1f1d1b719f9b94005"></a>

```c
ps2_enable_callback_t enable_callback
```

相关声明：[ps2_enable_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#gaad5d2a31e2f4768953b6d611364e748c)、[enable_callback](#ab0cdb648761d2de1f1d1b719f9b94005)。

`OPT`：启用回调。

## 69.2\_详细说明（Detailed Documentation）

<a id="abe4d10c3ad967796943d95f75c659d4d"></a>

### `config`

```c
ps2_config_t ps2_driver_api::config
```

`REQ`：配置 PS/2 设备实例。

<a id="a485227d96921b73da2041225535be74c"></a>

### `disable_callback`

```c
ps2_disable_callback_t ps2_driver_api::disable_callback
```

`OPT`：禁用回调。

<a id="ab0cdb648761d2de1f1d1b719f9b94005"></a>

### `enable_callback`

```c
ps2_enable_callback_t ps2_driver_api::enable_callback
```

`OPT`：启用回调。

<a id="abfaf41cc47cabb2d1710584586e5b93c"></a>

### `read`

```c
ps2_read_t ps2_driver_api::read
```

`REQ`：从 PS/2 设备读取从设备到主机方向的数据值。

<a id="add947b91f9ca9bac20fac2fbb47b87e4"></a>

### `write`

```c
ps2_write_t ps2_driver_api::write
```

`REQ`：向 PS/2 设备写入。

本数据类型文档由以下文件生成：

- `zephyr/drivers/ps2.h`

## 69.3\_原页交叉引用（Cross References）

- [zephyr/drivers/ps2.h](https://docs.zephyrproject.org/latest/doxygen/html/ps2_8h_source.html)
- [ps2_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#ga7fb2edbebe2523efde6c7f73bffb850a)
- [ps2_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#ga3d5a1b7e613e0e2b1a28689b9ab52ca5)
- [ps2_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#gaf7a935b2e1debd819792dbb02bd84ee2)
- [ps2_disable_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#gaaa51cb5cf5f5d7560c35374561746f6d)
- [ps2_enable_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html#gaad5d2a31e2f4768953b6d611364e748c)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P068_peci_msg_结构体.md) · [返回大纲](大纲.md) · [下一章](P070_psi5_driver_api_结构体.md)
