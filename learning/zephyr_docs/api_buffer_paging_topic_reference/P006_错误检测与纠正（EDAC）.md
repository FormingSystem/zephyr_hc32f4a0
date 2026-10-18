---
id: learning.zephyr-docs.api-buffer-paging-topic-reference.page-6
title: 错误检测与纠正（EDAC）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_错误检测与纠正（EDAC）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

错误检测与纠正（Error Detection and Correction，EDAC）控制器接口。

<a id="details"></a>

错误检测与纠正控制器接口（Error Detection and Correction，EDAC）。引入版本（Since）：2.5；API 版本（Version）：0.8.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 6.1\_主题（Topics）

<a id="r_edac_5Finterface_5Fext"></a>

相关声明：[设备专用 EDAC API 扩展（Device-specific API extensions）](../api_topic_reference/P033_设备专用 EDAC API 扩展（Device-specific API extensions）.md)。

<a id="header-files"></a>
<a id="files"></a>

## 6.2\_文件（Files）

<a id="r_edac_2Eh"></a>

```c
file edac.h
```

相关声明：[edac.h](../api_file_signal_device_reference/P008_zephyr__drivers__edac.h_文件参考.md)。

错误检测与纠正（Error Detection and Correction，EDAC）驱动API的主头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.3\_枚举（Enumerations）

<a id="r_ga3eb3da4d056d8e6167083301eb1276d6"></a>

```c
enum edac_error_type { EDAC_ERROR_TYPE_DRAM_COR = BIT(0) , EDAC_ERROR_TYPE_DRAM_UC = BIT(1) }
```

相关声明：[edac_error_type](#ga3eb3da4d056d8e6167083301eb1276d6)、[EDAC_ERROR_TYPE_DRAM_COR](#gga3eb3da4d056d8e6167083301eb1276d6a941e09125e6040d7114ee17328fd4b02)、[EDAC_ERROR_TYPE_DRAM_UC](#gga3eb3da4d056d8e6167083301eb1276d6a5b03fd27f37f01171e50c2997bc29a2f)。

错误检测与纠正（EDAC）的错误类型（Error Type）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 6.4\_可选接口（Optional Interfaces）

错误检测与纠正（EDAC）可选接口（Optional Interfaces）。

<a id="r_gad058d74c811e77b00730e25f2060cce5"></a>

```c
static int edac_inject_set_param1 (const struct device *dev, uint64_t value)
```

相关声明：[edac_inject_set_param1](#gad058d74c811e77b00730e25f2060cce5)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置注入参数（Injection Parameter）`param1`。

<a id="r_ga9817f47eeaf532e3789816e412eb5077"></a>

```c
static int edac_inject_get_param1 (const struct device *dev, uint64_t *value)
```

相关声明：[edac_inject_get_param1](#ga9817f47eeaf532e3789816e412eb5077)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

获取注入参数（Injection Parameter）`param1`。

<a id="r_ga9ed608245ba68aee6b235752a87a5c39"></a>

```c
static int edac_inject_set_param2 (const struct device *dev, uint64_t value)
```

相关声明：[edac_inject_set_param2](#ga9ed608245ba68aee6b235752a87a5c39)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置注入参数（Injection Parameter）`param2`。

<a id="r_ga37e097d550f91072b890d6c2d4b215fa"></a>

```c
static int edac_inject_get_param2 (const struct device *dev, uint64_t *value)
```

相关声明：[edac_inject_get_param2](#ga37e097d550f91072b890d6c2d4b215fa)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

获取注入参数（Injection Parameter）`param2`。

<a id="r_ga2b0ea084501faf52aeec5af33a1ca97b"></a>

```c
static int edac_inject_set_error_type (const struct device *dev, uint32_t error_type)
```

相关声明：[edac_inject_set_error_type](#ga2b0ea084501faf52aeec5af33a1ca97b)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置错误类型值（Error Type Value）。

<a id="r_gafb0cbc5082e88250a1e5955dd7d1770c"></a>

```c
static int edac_inject_get_error_type (const struct device *dev, uint32_t *error_type)
```

相关声明：[edac_inject_get_error_type](#gafb0cbc5082e88250a1e5955dd7d1770c)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取错误类型值（Error Type Value）。

<a id="r_gaf02830c2e621e73a7c4add38a92f6d7c"></a>

```c
static int edac_inject_error_trigger (const struct device *dev)
```

相关声明：[edac_inject_error_trigger](#gaf02830c2e621e73a7c4add38a92f6d7c)、[device](../device_reference/P002_设备对象结构.md)。

设置注入控制（Injection Control）。

## 6.5\_必需接口（Mandatory Interfaces）

错误检测与纠正（EDAC）必需接口（Mandatory Interfaces）。

<a id="r_ga905539bb96ff8c9f6f6a9fde6b3928e2"></a>

```c
static int edac_ecc_error_log_get (const struct device *dev, uint64_t *value)
```

相关声明：[edac_ecc_error_log_get](#ga905539bb96ff8c9f6f6a9fde6b3928e2)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

获取错误纠正码错误日志（ECC Error Log）。

<a id="r_gaa8c798b60b3b99ae6b8f8358253d1385"></a>

```c
static int edac_ecc_error_log_clear (const struct device *dev)
```

相关声明：[edac_ecc_error_log_clear](#gaa8c798b60b3b99ae6b8f8358253d1385)、[device](../device_reference/P002_设备对象结构.md)。

清除错误纠正码错误日志（ECC Error Log）。

<a id="r_gaa6cba09e19de241ed045387c85cc3f1c"></a>

```c
static int edac_parity_error_log_get (const struct device *dev, uint64_t *value)
```

相关声明：[edac_parity_error_log_get](#gaa6cba09e19de241ed045387c85cc3f1c)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

获取奇偶校验错误日志（Parity Error Log）。

<a id="r_gab60aa37ba86e2038fe979481cc6134c2"></a>

```c
static int edac_parity_error_log_clear (const struct device *dev)
```

相关声明：[edac_parity_error_log_clear](#gab60aa37ba86e2038fe979481cc6134c2)、[device](../device_reference/P002_设备对象结构.md)。

清除奇偶校验错误日志（Parity Error Log）。

<a id="r_gaea2915b6c3c4eef2c94c6f60e788dcfe"></a>

```c
static int edac_errors_cor_get (const struct device *dev)
```

相关声明：[edac_errors_cor_get](#gaea2915b6c3c4eef2c94c6f60e788dcfe)、[device](../device_reference/P002_设备对象结构.md)。

获取可纠正错误（Correctable Errors）的数量。

<a id="r_gaec79969648e56e98031d46abe73c2b82"></a>

```c
static int edac_errors_uc_get (const struct device *dev)
```

相关声明：[edac_errors_uc_get](#gaec79969648e56e98031d46abe73c2b82)、[device](../device_reference/P002_设备对象结构.md)。

获取不可纠正错误（Uncorrectable Errors）的数量。

<a id="r_ga2def500f72a06271d9a10243bfdf6527"></a>

```c
static int edac_notify_callback_set (const struct device *dev, edac_notify_callback_f cb)
```

相关声明：[edac_notify_callback_set](#ga2def500f72a06271d9a10243bfdf6527)、[device](../device_reference/P002_设备对象结构.md)。

为内存错误异常（Memory Error Exception）注册回调函数。

## 6.6\_详细说明（Detailed Documentation）

<a id="ga3eb3da4d056d8e6167083301eb1276d6"></a>

### `edac_error_type`

```c
enum edac_error_type
```

```c
#include <zephyr/drivers/edac.h>
```

错误检测与纠正（EDAC）的错误类型（Error Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `EDAC_ERROR_TYPE_DRAM_COR` | 可纠正错误类型（Correctable Error Type）。 |
| `EDAC_ERROR_TYPE_DRAM_UC` | 不可纠正错误类型（Uncorrectable Error Type）。 |

<a id="gaa8c798b60b3b99ae6b8f8358253d1385"></a>

### `edac_ecc_error_log_clear()`

```c
int edac_ecc_error_log_clear ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/edac.h>
```

清除错误纠正码错误日志（ECC Error Log）。

清除 ECC 错误日志（Error Log）的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时的返回值；否则返回错误码。 |
| `-ENOSYS` | 未实现必需接口（Mandatory Interface）时。 |

<a id="ga905539bb96ff8c9f6f6a9fde6b3928e2"></a>

### `edac_ecc_error_log_get()`

```c
int edac_ecc_error_log_get ( const struct device * dev, uint64_t * value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/edac.h>
```

获取错误纠正码错误日志（ECC Error Log）。

读取 ECC 错误日志（Error Log）的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |
| `value` | 指向 ECC 错误日志值的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时的返回值；否则返回错误码。 |
| `-ENOSYS` | 未实现必需接口（Mandatory Interface）时。 |

<a id="gaea2915b6c3c4eef2c94c6f60e788dcfe"></a>

### `edac_errors_cor_get()`

```c
int edac_errors_cor_get ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/edac.h>
```

获取可纠正错误（Correctable Errors）的数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `num` | 可纠正错误（Correctable Errors）的数量 |
| `-ENOSYS` | 未实现必需接口（Mandatory Interface）时。 |

<a id="gaec79969648e56e98031d46abe73c2b82"></a>

### `edac_errors_uc_get()`

```c
int edac_errors_uc_get ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/edac.h>
```

获取不可纠正错误（Uncorrectable Errors）的数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `num` | 不可纠正错误（Uncorrectable Errors）的数量 |
| `-ENOSYS` | 未实现必需接口（Mandatory Interface）时。 |

<a id="gaf02830c2e621e73a7c4add38a92f6d7c"></a>

### `edac_inject_error_trigger()`

```c
int edac_inject_error_trigger ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/edac.h>
```

设置注入控制（Injection Control）。

触发错误注入（Error Injection）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现可选接口（Optional Interface）时。 |
| `0` | 成功时的返回值；否则返回错误码。 |

<a id="gafb0cbc5082e88250a1e5955dd7d1770c"></a>

### `edac_inject_get_error_type()`

```c
int edac_inject_get_error_type ( const struct device * dev, uint32_t * error_type )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/edac.h>
```

获取错误类型值（Error Type Value）。

获取待注入的错误类型（Error Type）值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |
| `error_type` | 指向错误类型值的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现可选接口（Optional Interface）时。 |
| `0` | 成功时的返回值；否则返回错误码。 |

<a id="ga9817f47eeaf532e3789816e412eb5077"></a>

### `edac_inject_get_param1()`

```c
int edac_inject_get_param1 ( const struct device * dev, uint64_t * value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/edac.h>
```

获取注入参数（Injection Parameter）`param1`。

获取第一个错误注入参数（Injection Parameter）的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |
| `value` | 指向第一个注入参数的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现可选接口（Optional Interface）时。 |
| `0` | 成功时的返回值；否则返回错误码。 |

<a id="ga37e097d550f91072b890d6c2d4b215fa"></a>

### `edac_inject_get_param2()`

```c
int edac_inject_get_param2 ( const struct device * dev, uint64_t * value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/edac.h>
```

获取注入参数（Injection Parameter）`param2`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |
| `value` | 指向第二个注入参数的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现可选接口（Optional Interface）时。 |
| `0` | 成功时的返回值；否则返回错误码。 |

<a id="ga2b0ea084501faf52aeec5af33a1ca97b"></a>

### `edac_inject_set_error_type()`

```c
int edac_inject_set_error_type ( const struct device * dev, uint32_t error_type )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/edac.h>
```

设置错误类型值（Error Type Value）。

设置待注入的错误类型（Error Type）值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |
| `error_type` | 错误类型值 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现可选接口（Optional Interface）时。 |
| `0` | 成功时的返回值；否则返回错误码。 |

<a id="gad058d74c811e77b00730e25f2060cce5"></a>

### `edac_inject_set_param1()`

```c
int edac_inject_set_param1 ( const struct device * dev, uint64_t value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/edac.h>
```

设置注入参数（Injection Parameter）`param1`。

设置第一个错误注入参数（Injection Parameter）的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |
| `value` | 第一个注入参数 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现可选接口（Optional Interface）时。 |
| `0` | 成功时的返回值；否则返回其他错误码。 |

<a id="ga9ed608245ba68aee6b235752a87a5c39"></a>

### `edac_inject_set_param2()`

```c
int edac_inject_set_param2 ( const struct device * dev, uint64_t value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/edac.h>
```

设置注入参数（Injection Parameter）`param2`。

设置第二个错误注入参数（Injection Parameter）的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |
| `value` | 第二个注入参数 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现可选接口（Optional Interface）时。 |
| `0` | 成功时的返回值；否则返回错误码。 |

<a id="ga2def500f72a06271d9a10243bfdf6527"></a>

### `edac_notify_callback_set()`

```c
int edac_notify_callback_set ( const struct device * dev, edac_notify_callback_f cb )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/edac.h>
```

为内存错误异常（Memory Error Exception）注册回调函数。

此回调在中断上下文（Interrupt Context）中运行。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 要安装回调的 EDAC 驱动设备 |
| `cb` | 回调函数指针（Callback Function Pointer） |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时的返回值；否则返回错误码。 |
| `-ENOSYS` | 未实现必需接口（Mandatory Interface）时。 |

<a id="gab60aa37ba86e2038fe979481cc6134c2"></a>

### `edac_parity_error_log_clear()`

```c
int edac_parity_error_log_clear ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/edac.h>
```

清除奇偶校验错误日志（Parity Error Log）。

清除奇偶校验错误日志（Parity Error Log）的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时的返回值；否则返回错误码。 |
| `-ENOSYS` | 未实现必需接口（Mandatory Interface）时。 |

<a id="gaa6cba09e19de241ed045387c85cc3f1c"></a>

### `edac_parity_error_log_get()`

```c
int edac_parity_error_log_get ( const struct device * dev, uint64_t * value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/edac.h>
```

获取奇偶校验错误日志（Parity Error Log）。

读取奇偶校验错误日志（Parity Error Log）的值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向设备结构体的指针。 |
| `value` | 指向奇偶校验错误日志值的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时的返回值；否则返回错误码。 |
| `-ENOSYS` | 未实现必需接口（Mandatory Interface）时。 |


## 6.7\_原页交叉引用（Cross References）

- [设备专用 EDAC API 扩展（Device-specific API extensions）](../api_topic_reference/P033_设备专用 EDAC API 扩展（Device-specific API extensions）.md)
- [edac.h](../api_file_signal_device_reference/P008_zephyr__drivers__edac.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga3eb3da4d056d8e6167083301eb1276d6a941e09125e6040d7114ee17328fd4b02"></a>
<a id="gga3eb3da4d056d8e6167083301eb1276d6a5b03fd27f37f01171e50c2997bc29a2f"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_动态主机配置协议第 4 版（DHCPv4）.md) · [返回大纲](大纲.md) · [下一章](P007_IPSRSTCR 复位控制（Reset Control）.md)
