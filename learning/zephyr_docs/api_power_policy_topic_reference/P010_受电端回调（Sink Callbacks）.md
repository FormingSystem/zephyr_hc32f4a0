---
id: learning.zephyr-docs.api-power-policy-topic-reference.page-10
title: 受电端回调（Sink Callbacks）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__sink__callbacks.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_受电端回调（Sink Callbacks）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__sink__callbacks.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 10.1\_类型定义（Typedefs）

<a id="r_gaaed0161142c3481ce9180015b6968357"></a>

```c
typedef int(* policy_cb_get_snk_cap_t) (const struct device *dev, uint32_t **pdos, int *num_pdos)
```

相关声明：[policy_cb_get_snk_cap_t](#gaaed0161142c3481ce9180015b6968357)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取受电端能力（Sink Capabilities）的回调类型。

<a id="r_ga6096d6909698f1b86a1a9cbd1f8d4097"></a>

```c
typedef void(* policy_cb_set_src_cap_t) (const struct device *dev, const uint32_t *pdos, const int num_pdos)
```

相关声明：[policy_cb_set_src_cap_t](#ga6096d6909698f1b86a1a9cbd1f8d4097)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

报告收到的端口对端供电能力（Port Partner's Source Capabilities）的回调类型。

<a id="r_ga2aacd704d08a8cecbf818150e8ec51b6"></a>

```c
typedef bool(* policy_cb_check_t) (const struct device *dev, const enum usbc_policy_check_t policy_check)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[policy_cb_check_t](#ga2aacd704d08a8cecbf818150e8ec51b6)、[device](../device_reference/P002_设备对象结构.md)、[usbc_policy_check_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gafea882f4f3cc96c502d53a24a3e5aec5)。

检查策略（Policy）的回调类型。

<a id="r_gaea62016b263dfaf5f869dd6ea036fdad"></a>

```c
typedef bool(* policy_cb_wait_notify_t) (const struct device *dev, const enum usbc_policy_wait_t wait_notify)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[policy_cb_wait_notify_t](#gaea62016b263dfaf5f869dd6ea036fdad)、[device](../device_reference/P002_设备对象结构.md)、[usbc_policy_wait_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gadf5d2934b5dc8e2b01d20bb904988784)。

通知设备策略管理器（Device Policy Manager）收到 `WAIT` 消息的回调类型。

<a id="r_ga44af668d9c22e757983c803d7b8ff82e"></a>

```c
typedef void(* policy_cb_notify_t) (const struct device *dev, const enum usbc_policy_notify_t policy_notify)
```

相关声明：[policy_cb_notify_t](#ga44af668d9c22e757983c803d7b8ff82e)、[device](../device_reference/P002_设备对象结构.md)、[usbc_policy_notify_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga66f934a5c5cd88b574c71d1f18fbda23)。

通知设备策略管理器（Device Policy Manager）策略发生变化的回调类型。

<a id="r_gae0448c6b271273c5db59775c3a6260dc"></a>

```c
typedef uint32_t(* policy_cb_get_rdo_t) (const struct device *dev)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[policy_cb_get_rdo_t](#gae0448c6b271273c5db59775c3a6260dc)、[device](../device_reference/P002_设备对象结构.md)。

获取请求数据对象（Request Data Object，RDO）的回调类型。

<a id="r_ga1a3da6faad509213f607893fef16b673"></a>

```c
typedef bool(* policy_cb_is_snk_at_default_t) (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[policy_cb_is_snk_at_default_t](#ga1a3da6faad509213f607893fef16b673)、[device](../device_reference/P002_设备对象结构.md)。

检查受电端供电（Sink Power Supply）是否处于默认级别的回调类型。

## 10.2\_详细说明（Detailed Documentation）

<a id="ga2aacd704d08a8cecbf818150e8ec51b6"></a>

### `policy_cb_check_t`

```c
typedef bool(* policy_cb_check_t) (const struct device *dev, const enum usbc_policy_check_t policy_check)
```

```c
#include <zephyr/usb_c/usbc.h>
```

检查策略（Policy）的回调类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |
| `policy_check` | 要检查的策略（Policy）。 |

**返回（Returns）**：**返回值（Returns）：**设备策略管理器（Device Policy Manager）当前允许该策略时返回 `true`。

<a id="gae0448c6b271273c5db59775c3a6260dc"></a>

### `policy_cb_get_rdo_t`

```c
typedef uint32_t(* policy_cb_get_rdo_t) (const struct device *dev)
```

```c
#include <zephyr/usb_c/usbc.h>
```

获取请求数据对象（Request Data Object，RDO）的回调类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |

**返回（Returns）**：**返回值（Returns）：**请求数据对象（RDO）。

<a id="gaaed0161142c3481ce9180015b6968357"></a>

### `policy_cb_get_snk_cap_t`

```c
typedef int(* policy_cb_get_snk_cap_t) (const struct device *dev, uint32_t **pdos, int *num_pdos)
```

```c
#include <zephyr/usb_c/usbc.h>
```

获取受电端能力（Sink Capabilities）的回调类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |
| `pdos` | 用于存储电源数据对象（PDO）的指针。 |
| `num_pdos` | 用于存储电源数据对象（PDO）数量的指针。 |

返回（Returns）：成功为0。

<a id="ga1a3da6faad509213f607893fef16b673"></a>

### `policy_cb_is_snk_at_default_t`

```c
typedef bool(* policy_cb_is_snk_at_default_t) (const struct device *dev)
```

```c
#include <zephyr/usb_c/usbc.h>
```

检查受电端供电（Sink Power Supply）是否处于默认级别的回调类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |

**返回（Returns）**：**返回值（Returns）：**供电处于默认级别（Default Level）时返回 `true`。

<a id="ga44af668d9c22e757983c803d7b8ff82e"></a>

### `policy_cb_notify_t`

```c
typedef void(* policy_cb_notify_t) (const struct device *dev, const enum usbc_policy_notify_t policy_notify)
```

```c
#include <zephyr/usb_c/usbc.h>
```

通知设备策略管理器（Device Policy Manager）策略发生变化的回调类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |
| `policy_notify` | 策略通知（Policy Notification）。 |

<a id="ga6096d6909698f1b86a1a9cbd1f8d4097"></a>

### `policy_cb_set_src_cap_t`

```c
typedef void(* policy_cb_set_src_cap_t) (const struct device *dev, const uint32_t *pdos, const int num_pdos)
```

```c
#include <zephyr/usb_c/usbc.h>
```

报告收到的端口对端供电能力（Port Partner's Source Capabilities）的回调类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |
| `pdos` | 指向对端供电 PDO（Source PDOs）的指针。 |
| `num_pdos` | 供电 PDO（Source PDOs）的数量。 |

<a id="gaea62016b263dfaf5f869dd6ea036fdad"></a>

### `policy_cb_wait_notify_t`

```c
typedef bool(* policy_cb_wait_notify_t) (const struct device *dev, const enum usbc_policy_wait_t wait_notify)
```

```c
#include <zephyr/usb_c/usbc.h>
```

通知设备策略管理器（Device Policy Manager）收到 `WAIT` 消息的回调类型。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | USB-C 连接器实例（Connector Instance）。 |
| `wait_notify` | 等待通知（Wait Notification）。 |

**返回（Returns）**：**返回值（Returns）：**策略引擎（PE）应等待并重新发送消息时返回 `true`。


## 10.3\_原页交叉引用（Cross References）

- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [usbc_policy_check_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gafea882f4f3cc96c502d53a24a3e5aec5)
- [usbc_policy_wait_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#gadf5d2934b5dc8e2b01d20bb904988784)
- [usbc_policy_notify_t](https://docs.zephyrproject.org/latest/doxygen/html/group____usbc__device__api.html#ga66f934a5c5cd88b574c71d1f18fbda23)
- [zephyr/usb_c/usbc.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc_8h.html)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P009_基本过滤条件（Basic Filter Conditions）.md) · [返回大纲](大纲.md) · [下一章](P011_TEE 驱动后端 API.md)
