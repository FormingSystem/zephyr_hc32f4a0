---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-97
title: bt_le_cs_set_default_settings_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__cs__set__default__settings__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第97章\_bt\_le\_cs\_set\_default\_settings\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__cs__set__default__settings__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本地控制器（Controller）中的默认信道探测（CS）设置。

```c
#include <zephyr/bluetooth/cs.h>
```

<a id="details"></a>

本地控制器（Controller）中的默认信道探测（CS）设置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 97.1\_数据成员（Data Fields）

<a id="r_a6a68056e10ea18ab2bb33202a39387a4"></a>

```c
bool enable_initiator_role
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enable_initiator_role](#a6a68056e10ea18ab2bb33202a39387a4)。

启用信道探测发起方角色（CS initiator role）。

<a id="r_a7e532de60b09424da17be0e61dbafb2d"></a>

```c
bool enable_reflector_role
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[enable_reflector_role](#a7e532de60b09424da17be0e61dbafb2d)。

启用信道探测反射方角色（CS reflector role）。

<a id="r_a581ab5686e3eedfde84817d0ffcff587"></a>

```c
enum bt_le_cs_sync_antenna_selection_opt cs_sync_antenna_selection
```

相关声明：[bt_le_cs_sync_antenna_selection_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga9f286cdeeee0e9df06e6b3df1e9ab643)、[cs_sync_antenna_selection](#a581ab5686e3eedfde84817d0ffcff587)。

本地控制器发送 `CS_SYNC` 数据包所用的天线标识符（Antenna identifier）。

<a id="r_a31a3b73d2bc44306f6905a2a1958b62b"></a>

```c
int8_t max_tx_power
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[max_tx_power](#a31a3b73d2bc44306f6905a2a1958b62b)。

用于所有信道探测发送（CS transmissions）的最大输出功率，即有效全向辐射功率（Effective Isotropic Radiated Power），单位为 dBm。

## 97.2\_详细说明（Detailed Documentation）

<a id="a581ab5686e3eedfde84817d0ffcff587"></a>

### `cs_sync_antenna_selection`

```c
enum bt_le_cs_sync_antenna_selection_opt bt_le_cs_set_default_settings_param::cs_sync_antenna_selection
```

本地控制器发送 `CS_SYNC` 数据包所用的天线标识符（Antenna identifier）。

<a id="a6a68056e10ea18ab2bb33202a39387a4"></a>

### `enable_initiator_role`

```c
bool bt_le_cs_set_default_settings_param::enable_initiator_role
```

启用信道探测发起方角色（CS initiator role）。

<a id="a7e532de60b09424da17be0e61dbafb2d"></a>

### `enable_reflector_role`

```c
bool bt_le_cs_set_default_settings_param::enable_reflector_role
```

启用信道探测反射方角色（CS reflector role）。

<a id="a31a3b73d2bc44306f6905a2a1958b62b"></a>

### `max_tx_power`

```c
int8_t bt_le_cs_set_default_settings_param::max_tx_power
```

用于所有信道探测发送（CS transmissions）的最大输出功率，即有效全向辐射功率（Effective Isotropic Radiated Power），单位为 dBm。

取值范围为 `BT_HCI_OP_LE_CS_MIN_MAX_TX_POWER` 至 `BT_HCI_OP_LE_CS_MAX_MAX_TX_POWER`。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/cs.h`

## 97.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/cs.h](https://docs.zephyrproject.org/latest/doxygen/html/cs_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_le_cs_sync_antenna_selection_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__le__cs.html#ga9f286cdeeee0e9df06e6b3df1e9ab643)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [BT_HCI_OP_LE_CS_MIN_MAX_TX_POWER](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a040315a8ac4f80a2c497919a2fd4d7bc)
- [BT_HCI_OP_LE_CS_MAX_MAX_TX_POWER](https://docs.zephyrproject.org/latest/doxygen/html/hci__types_8h.html#a29a240b2d3f209b1f5f3d96e380dde08)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P096_bt_le_cs_procedure_enable_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P098_bt_le_cs_set_procedure_parameters_param_结构体.md)
