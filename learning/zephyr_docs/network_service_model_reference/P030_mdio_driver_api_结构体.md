---
id: learning.zephyr-docs.network-service-model-reference.page-30
title: mdio_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmdio__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_mdio\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmdio__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：管理数据输入输出（MDIO）驱动操作。

```c
#include <zephyr/drivers/mdio.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：管理数据输入/输出（MDIO）驱动操作。这是每个 MDIO 驱动都需要定义的驱动 API 结构体，其中包含指向驱动所实现操作的函数指针，以及其他驱动专用常量数据。标记为 REQ 的成员必须由驱动设置，标记为 OPT 的成员为可选。另见 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 30.1\_数据成员（Data Fields）

<a id="r_a37329cf08f4eb6a9e2ad36e987d4d329"></a>

```c
mdio_api_read_t read
```

相关声明：[mdio_api_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface__backend.html#gadd83bf9b8e4b4bd7189bc0b814c1f535)、[read](#a37329cf08f4eb6a9e2ad36e987d4d329)。

可选（OPT）：从 MDIO 总线读取。

<a id="r_ac5ad4a58e170d684416997f30c8ac8bb"></a>

```c
mdio_api_write_t write
```

相关声明：[mdio_api_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface__backend.html#ga09e5f0532a3d88249ee6e852be45e434)、[write](#ac5ad4a58e170d684416997f30c8ac8bb)。

可选（OPT）：向 MDIO 总线写入。

<a id="r_ae76af9e29b24d9840566d4659a001bdd"></a>

```c
mdio_api_read_c45_t read_c45
```

相关声明：[mdio_api_read_c45_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface__backend.html#gaba3f545bba5aa028f50c4a7f6e43abd0)、[read_c45](#ae76af9e29b24d9840566d4659a001bdd)。

可选（OPT）：使用第 45 条（Clause 45）访问方式从 MDIO 总线读取。

<a id="r_a95b8e08d326ea522e670c90e629b6c86"></a>

```c
mdio_api_write_c45_t write_c45
```

相关声明：[mdio_api_write_c45_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface__backend.html#ga98d32453b4b8ec4abb36113c54711570)、[write_c45](#a95b8e08d326ea522e670c90e629b6c86)。

可选（OPT）：使用第 45 条（Clause 45）访问方式向 MDIO 总线写入。

## 30.2\_详细说明（Detailed Documentation）

<a id="a37329cf08f4eb6a9e2ad36e987d4d329"></a>

### `read`

```c
mdio_api_read_t mdio_driver_api::read
```

可选（OPT）：从 MDIO 总线读取。

<a id="ae76af9e29b24d9840566d4659a001bdd"></a>

### `read_c45`

```c
mdio_api_read_c45_t mdio_driver_api::read_c45
```

可选（OPT）：使用第 45 条（Clause 45）访问方式从 MDIO 总线读取。

<a id="ac5ad4a58e170d684416997f30c8ac8bb"></a>

### `write`

```c
mdio_api_write_t mdio_driver_api::write
```

可选（OPT）：向 MDIO 总线写入。

<a id="a95b8e08d326ea522e670c90e629b6c86"></a>

### `write_c45`

```c
mdio_api_write_c45_t mdio_driver_api::write_c45
```

可选（OPT）：使用第 45 条（Clause 45）访问方式向 MDIO 总线写入。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mdio.h`

## 30.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mdio.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mdio_8h_source.html)
- [mdio_api_read_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface__backend.html#gadd83bf9b8e4b4bd7189bc0b814c1f535)
- [mdio_api_write_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface__backend.html#ga09e5f0532a3d88249ee6e852be45e434)
- [mdio_api_read_c45_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface__backend.html#gaba3f545bba5aa028f50c4a7f6e43abd0)
- [mdio_api_write_c45_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mdio__interface__backend.html#ga98d32453b4b8ec4abb36113c54711570)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P029_loopback_disk_access_结构体.md) · [返回大纲](大纲.md) · [下一章](P031_netmidi2_ep_结构体.md)
