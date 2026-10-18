---
id: learning.zephyr-docs.api-input-runtime-topic-reference.page-18
title: 供电端回调（Source Callbacks）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__source__callbacks.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_供电端回调（Source Callbacks）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__source__callbacks.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 18.1\_类型定义（Typedefs）

<a id="r_ga4bbf78bd752d38d915412dd942d3aab8"></a>

```c
typedef int(* policy_cb_get_src_caps_t) (const struct device *dev, const uint32_t **pdos, uint32_t *num_pdos)
```

相关声明：[policy_cb_get_src_caps_t](#ga4bbf78bd752d38d915412dd942d3aab8)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从设备策略管理器（Device Policy Manager）获取供电端能力（Source Capabilities）的回调类型。

<a id="r_gaeeda677224456f685137e4b345c0e173"></a>

```c
typedef enum usbc_snk_req_reply_t(* policy_cb_check_sink_request_t) (const struct device *dev, const uint32_t request_msg)
```

相关声明：[usbc_snk_req_reply_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga4c4f0592a034b4e49eee85e95af33f94)、[policy_cb_check_sink_request_t](#gaeeda677224456f685137e4b345c0e173)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

检查受电端请求（Sink Request）是否有效的回调类型。

<a id="r_gae7391e858485e44a74e5fcdbb7931ca7"></a>

```c
typedef bool(* policy_cb_is_ps_ready_t) (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[policy_cb_is_ps_ready_t](#gae7391e858485e44a74e5fcdbb7931ca7)、[device](../device_reference/P002_设备对象结构.md)。

检查供电端电源（Source Power Supply）是否就绪的回调类型。

<a id="r_ga2925e462140a700920251d92ae5a3aa4"></a>

```c
typedef bool(* policy_cb_present_contract_is_valid_t) (const struct device *dev, const uint32_t present_contract)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[policy_cb_present_contract_is_valid_t](#ga2925e462140a700920251d92ae5a3aa4)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

检查当前供电契约（Contract）是否仍有效的回调类型。

<a id="r_ga699811c862990b31ec0126dd3a4c3e4d"></a>

```c
typedef bool(* policy_cb_change_src_caps_t) (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[policy_cb_change_src_caps_t](#ga699811c862990b31ec0126dd3a4c3e4d)、[device](../device_reference/P002_设备对象结构.md)。

请求向受电端（Sink）发送另一组供电端能力（Source Caps）的回调类型。

<a id="r_gae903c8108e8d1563cb0b1ccdd901c925"></a>

```c
typedef void(* policy_cb_set_port_partner_snk_cap_t) (const struct device *dev, const uint32_t *pdos, const int num_pdos)
```

相关声明：[policy_cb_set_port_partner_snk_cap_t](#gae903c8108e8d1563cb0b1ccdd901c925)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

报告从受电端口对端（Sink Port Partner）收到的能力（Capabilities）的回调类型。

<a id="r_ga7c75f8192001179f20bf1fe48316f3c6"></a>

```c
typedef int(* policy_cb_get_src_rp_t) (const struct device *dev, enum tc_rp_value *rp)
```

相关声明：[policy_cb_get_src_rp_t](#ga7c75f8192001179f20bf1fe48316f3c6)、[device](../device_reference/P002_设备对象结构.md)、[tc_rp_value](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga4e0eec97f7c5c97b87eff9561deea2d5)。

获取应施加到配置通道（CC）线上的 Rp 值的回调类型。

<a id="r_gaaecac7683d7092c0a477e8d9ca0e5a33"></a>

```c
typedef int(* policy_cb_src_en_t) (const struct device *dev, bool en)
```

相关声明：[policy_cb_src_en_t](#gaaecac7683d7092c0a477e8d9ca0e5a33)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

启用 VBUS 的回调类型。

## 18.2\_详细说明（Detailed Documentation）

<a id="ga699811c862990b31ec0126dd3a4c3e4d"></a>

### `policy_cb_change_src_caps_t`

```c
typedef bool(* policy_cb_change_src_caps_t) (const struct device *dev)
```

```c
#include <zephyr/usb_c/usbc.h>
```

请求向受电端（Sink）发送另一组供电端能力（Source Caps）的回调类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |

**返回（Returns）**：**返回值（Returns）：**存在另一组供电端能力（Source Caps）时返回 `true`。

<a id="gaeeda677224456f685137e4b345c0e173"></a>

### `policy_cb_check_sink_request_t`

```c
typedef enum usbc_snk_req_reply_t(* policy_cb_check_sink_request_t) (const struct device *dev, const uint32_t request_msg)
```

```c
#include <zephyr/usb_c/usbc.h>
```

检查受电端请求（Sink Request）是否有效的回调类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |
| `request_msg` | 要检查的请求消息（Request Message）。 |

**返回（Returns）**：**返回值（Returns）：**受电端请求回复（Sink Request Reply）。

<a id="ga4bbf78bd752d38d915412dd942d3aab8"></a>

### `policy_cb_get_src_caps_t`

```c
typedef int(* policy_cb_get_src_caps_t) (const struct device *dev, const uint32_t **pdos, uint32_t *num_pdos)
```

```c
#include <zephyr/usb_c/usbc.h>
```

从设备策略管理器（Device Policy Manager）获取供电端能力（Source Capabilities）的回调类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |
| `pdos` | 指向供电能力 PDO（Source Capability PDOs）的指针。 |
| `num_pdos` | 指向供电能力 PDO（Source Capability PDOs）数量的指针。 |

返回（Returns）：成功为0。

<a id="ga7c75f8192001179f20bf1fe48316f3c6"></a>

### `policy_cb_get_src_rp_t`

```c
typedef int(* policy_cb_get_src_rp_t) (const struct device *dev, enum tc_rp_value *rp)
```

```c
#include <zephyr/usb_c/usbc.h>
```

获取应施加到配置通道（CC）线上的 Rp 值的回调类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |
| `rp` | Rp 值（Value）。 |

返回（Returns）：成功为0。

<a id="gae7391e858485e44a74e5fcdbb7931ca7"></a>

### `policy_cb_is_ps_ready_t`

```c
typedef bool(* policy_cb_is_ps_ready_t) (const struct device *dev)
```

```c
#include <zephyr/usb_c/usbc.h>
```

检查供电端电源（Source Power Supply）是否就绪的回调类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |

**返回（Returns）**：**返回值（Returns）：**电源就绪（Ready）返回 `true`，否则返回 `false`。

<a id="ga2925e462140a700920251d92ae5a3aa4"></a>

### `policy_cb_present_contract_is_valid_t`

```c
typedef bool(* policy_cb_present_contract_is_valid_t) (const struct device *dev, const uint32_t present_contract)
```

```c
#include <zephyr/usb_c/usbc.h>
```

检查当前供电契约（Contract）是否仍有效的回调类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |
| `present_contract` | 当前供电契约（Present Contract）。 |

**返回（Returns）**：**返回值（Returns）：**当前供电契约（Present Contract）仍有效时返回 `true`。

<a id="gae903c8108e8d1563cb0b1ccdd901c925"></a>

### `policy_cb_set_port_partner_snk_cap_t`

```c
typedef void(* policy_cb_set_port_partner_snk_cap_t) (const struct device *dev, const uint32_t *pdos, const int num_pdos)
```

```c
#include <zephyr/usb_c/usbc.h>
```

报告从受电端口对端（Sink Port Partner）收到的能力（Capabilities）的回调类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |
| `pdos` | 指向受电端能力 PDO（Sink Capability PDOs）的指针。 |
| `num_pdos` | 受电端能力 PDO（Sink Capability PDOs）的数量。 |

<a id="gaaecac7683d7092c0a477e8d9ca0e5a33"></a>

### `policy_cb_src_en_t`

```c
typedef int(* policy_cb_src_en_t) (const struct device *dev, bool en)
```

```c
#include <zephyr/usb_c/usbc.h>
```

启用 VBUS 的回调类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |
| `en` | `true` 表示启用 VBUS，`false` 表示禁用。 |

返回（Returns）：成功为0。


## 18.3\_原页交叉引用（Cross References）

- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [usbc_snk_req_reply_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga4c4f0592a034b4e49eee85e95af33f94)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [tc_rp_value](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga4e0eec97f7c5c97b87eff9561deea2d5)
- [zephyr/usb_c/usbc.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc_8h.html)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P017_传感器——感知子系统（Sensors，Sensing）.md) · [返回大纲](大纲.md) · [下一章](P019_TMC6460 其他功能（MISC）.md)
