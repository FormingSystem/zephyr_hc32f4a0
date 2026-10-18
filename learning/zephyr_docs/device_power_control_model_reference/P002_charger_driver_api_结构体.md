---
id: learning.zephyr-docs.device-power-control-model-reference.page-2
title: charger_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcharger__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_charger\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcharger__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动操作（Driver Operations）：充电器（Charger）驱动操作。

```c
#include <zephyr/drivers/charger.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：充电器（Charger）驱动操作。这是每个充电器驱动都需要定义的驱动 API 结构体。它包含驱动所实现操作的函数指针，以及其他驱动专用的常量数据。标记为 `REQ` 的成员必须由驱动设置，标记为 `OPT` 的成员为可选项。另请参阅 `DEVICE_DT_INST_DEFINE()`、`DEVICE_DT_DEFINE()` 和 `DEVICE_API()`。缓存（Caching）完全由客户端负责。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 2.1\_数据成员（Data Fields）

<a id="r_a945bfc62b0572da09480e97a6a819269"></a>

```c
charger_get_property_t get_property
```

相关声明：[charger_get_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__backend.html#gafb7488129e0a6c086d3ff0ffadb6c82b)、[get_property](#a945bfc62b0572da09480e97a6a819269)。

`REQ`：获取电池充电器属性。

<a id="r_a7a7942d11841d9ec02ff57f46323a3a3"></a>

```c
charger_set_property_t set_property
```

相关声明：[charger_set_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__backend.html#ga6556781abf0e81eee431c88cb894a8e6)、[set_property](#a7a7942d11841d9ec02ff57f46323a3a3)。

`REQ`：设置电池充电器属性。

<a id="r_a41ea553c8bb6a24915d73a00129ee67d"></a>

```c
charger_charge_enable_t charge_enable
```

相关声明：[charger_charge_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__backend.html#gaf035c2972693a8763fd08b7db8c9c0bd)、[charge_enable](#a41ea553c8bb6a24915d73a00129ee67d)。

`REQ`：启用或禁用充电周期（Charge cycle）。

## 2.2\_详细说明（Detailed Documentation）

<a id="a41ea553c8bb6a24915d73a00129ee67d"></a>

### `charge_enable`

```c
charger_charge_enable_t charger_driver_api::charge_enable
```

`REQ`：启用或禁用充电周期（Charge cycle）。

<a id="a945bfc62b0572da09480e97a6a819269"></a>

### `get_property`

```c
charger_get_property_t charger_driver_api::get_property
```

`REQ`：获取电池充电器属性。

<a id="a7a7942d11841d9ec02ff57f46323a3a3"></a>

### `set_property`

```c
charger_set_property_t charger_driver_api::set_property
```

`REQ`：设置电池充电器属性。

本数据类型文档由以下文件生成：

- `zephyr/drivers/charger.h`

## 2.3\_原页交叉引用（Cross References）

- [zephyr/drivers/charger.h](https://docs.zephyrproject.org/latest/doxygen/html/charger_8h_source.html)
- [charger_get_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__backend.html#gafb7488129e0a6c086d3ff0ffadb6c82b)
- [charger_set_property_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__backend.html#ga6556781abf0e81eee431c88cb894a8e6)
- [charger_charge_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__charger__interface__backend.html#gaf035c2972693a8763fd08b7db8c9c0bd)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P001_charger_current_notifier_结构体.md) · [返回大纲](大纲.md) · [下一章](P003_comp_nrf_comp_diff_config_结构体.md)
