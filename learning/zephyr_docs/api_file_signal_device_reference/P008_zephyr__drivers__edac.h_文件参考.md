---
id: learning.zephyr-docs.api-file-signal-device-reference.page-8
title: zephyr__drivers__edac.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/edac_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_drivers\_\_edac.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/edac_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

错误检测与纠正（Error Detection and Correction，EDAC）驱动API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <sys/types.h>
```

查看此文件的源码。

错误检测与纠正（Error Detection and Correction，EDAC）驱动API的主头文件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 8.1\_枚举（Enumerations）

<a id="r_ga3eb3da4d056d8e6167083301eb1276d6"></a>

```c
enum edac_error_type { EDAC_ERROR_TYPE_DRAM_COR = BIT(0) , EDAC_ERROR_TYPE_DRAM_UC = BIT(1) }
```

相关声明：[edac_error_type](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga3eb3da4d056d8e6167083301eb1276d6)、[EDAC_ERROR_TYPE_DRAM_COR](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gga3eb3da4d056d8e6167083301eb1276d6a941e09125e6040d7114ee17328fd4b02)、[EDAC_ERROR_TYPE_DRAM_UC](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gga3eb3da4d056d8e6167083301eb1276d6a5b03fd27f37f01171e50c2997bc29a2f)。

错误检测与纠正（EDAC）的错误类型（Error Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.2\_函数（Functions）

<a id="func-members-0"></a>

### 可选接口（Optional Interfaces）

错误检测与纠正（EDAC）可选接口（Optional Interfaces）。

<a id="r_gad058d74c811e77b00730e25f2060cce5"></a>

```c
static int edac_inject_set_param1 (const struct device *dev, uint64_t value)
```

相关声明：[edac_inject_set_param1](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gad058d74c811e77b00730e25f2060cce5)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置注入参数（Injection Parameter）`param1`。

<a id="r_ga9817f47eeaf532e3789816e412eb5077"></a>

```c
static int edac_inject_get_param1 (const struct device *dev, uint64_t *value)
```

相关声明：[edac_inject_get_param1](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga9817f47eeaf532e3789816e412eb5077)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

获取注入参数（Injection Parameter）`param1`。

<a id="r_ga9ed608245ba68aee6b235752a87a5c39"></a>

```c
static int edac_inject_set_param2 (const struct device *dev, uint64_t value)
```

相关声明：[edac_inject_set_param2](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga9ed608245ba68aee6b235752a87a5c39)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

设置注入参数（Injection Parameter）`param2`。

<a id="r_ga37e097d550f91072b890d6c2d4b215fa"></a>

```c
static int edac_inject_get_param2 (const struct device *dev, uint64_t *value)
```

相关声明：[edac_inject_get_param2](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga37e097d550f91072b890d6c2d4b215fa)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

获取注入参数（Injection Parameter）`param2`。

<a id="r_ga2b0ea084501faf52aeec5af33a1ca97b"></a>

```c
static int edac_inject_set_error_type (const struct device *dev, uint32_t error_type)
```

相关声明：[edac_inject_set_error_type](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga2b0ea084501faf52aeec5af33a1ca97b)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

设置错误类型值（Error Type Value）。

<a id="r_gafb0cbc5082e88250a1e5955dd7d1770c"></a>

```c
static int edac_inject_get_error_type (const struct device *dev, uint32_t *error_type)
```

相关声明：[edac_inject_get_error_type](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gafb0cbc5082e88250a1e5955dd7d1770c)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取错误类型值（Error Type Value）。

<a id="r_gaf02830c2e621e73a7c4add38a92f6d7c"></a>

```c
static int edac_inject_error_trigger (const struct device *dev)
```

相关声明：[edac_inject_error_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gaf02830c2e621e73a7c4add38a92f6d7c)、[device](../device_reference/P002_设备对象结构.md)。

设置注入控制（Injection Control）。

<a id="func-members-1"></a>

### 必需接口（Mandatory Interfaces）

错误检测与纠正（EDAC）必需接口（Mandatory Interfaces）。

<a id="r_ga905539bb96ff8c9f6f6a9fde6b3928e2"></a>

```c
static int edac_ecc_error_log_get (const struct device *dev, uint64_t *value)
```

相关声明：[edac_ecc_error_log_get](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga905539bb96ff8c9f6f6a9fde6b3928e2)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

获取错误纠正码错误日志（ECC Error Log）。

<a id="r_gaa8c798b60b3b99ae6b8f8358253d1385"></a>

```c
static int edac_ecc_error_log_clear (const struct device *dev)
```

相关声明：[edac_ecc_error_log_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gaa8c798b60b3b99ae6b8f8358253d1385)、[device](../device_reference/P002_设备对象结构.md)。

清除错误纠正码错误日志（ECC Error Log）。

<a id="r_gaa6cba09e19de241ed045387c85cc3f1c"></a>

```c
static int edac_parity_error_log_get (const struct device *dev, uint64_t *value)
```

相关声明：[edac_parity_error_log_get](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gaa6cba09e19de241ed045387c85cc3f1c)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

获取奇偶校验错误日志（Parity Error Log）。

<a id="r_gab60aa37ba86e2038fe979481cc6134c2"></a>

```c
static int edac_parity_error_log_clear (const struct device *dev)
```

相关声明：[edac_parity_error_log_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gab60aa37ba86e2038fe979481cc6134c2)、[device](../device_reference/P002_设备对象结构.md)。

清除奇偶校验错误日志（Parity Error Log）。

<a id="r_gaea2915b6c3c4eef2c94c6f60e788dcfe"></a>

```c
static int edac_errors_cor_get (const struct device *dev)
```

相关声明：[edac_errors_cor_get](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gaea2915b6c3c4eef2c94c6f60e788dcfe)、[device](../device_reference/P002_设备对象结构.md)。

获取可纠正错误（Correctable Errors）的数量。

<a id="r_gaec79969648e56e98031d46abe73c2b82"></a>

```c
static int edac_errors_uc_get (const struct device *dev)
```

相关声明：[edac_errors_uc_get](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gaec79969648e56e98031d46abe73c2b82)、[device](../device_reference/P002_设备对象结构.md)。

获取不可纠正错误（Uncorrectable Errors）的数量。

<a id="r_ga2def500f72a06271d9a10243bfdf6527"></a>

```c
static int edac_notify_callback_set (const struct device *dev, edac_notify_callback_f cb)
```

相关声明：[edac_notify_callback_set](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga2def500f72a06271d9a10243bfdf6527)、[device](../device_reference/P002_设备对象结构.md)。

为内存错误异常（Memory Error Exception）注册回调函数。


## 8.3\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_network_reference/P004_edac.h_源码浏览.md)
- [edac_error_type](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga3eb3da4d056d8e6167083301eb1276d6)
- [EDAC_ERROR_TYPE_DRAM_COR](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gga3eb3da4d056d8e6167083301eb1276d6a941e09125e6040d7114ee17328fd4b02)
- [EDAC_ERROR_TYPE_DRAM_UC](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gga3eb3da4d056d8e6167083301eb1276d6a5b03fd27f37f01171e50c2997bc29a2f)
- [edac_inject_set_param1](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gad058d74c811e77b00730e25f2060cce5)
- [device](../device_reference/P002_设备对象结构.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [edac_inject_get_param1](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga9817f47eeaf532e3789816e412eb5077)
- [edac_inject_set_param2](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga9ed608245ba68aee6b235752a87a5c39)
- [edac_inject_get_param2](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga37e097d550f91072b890d6c2d4b215fa)
- [edac_inject_set_error_type](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga2b0ea084501faf52aeec5af33a1ca97b)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [edac_inject_get_error_type](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gafb0cbc5082e88250a1e5955dd7d1770c)
- [edac_inject_error_trigger](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gaf02830c2e621e73a7c4add38a92f6d7c)
- [edac_ecc_error_log_get](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga905539bb96ff8c9f6f6a9fde6b3928e2)
- [edac_ecc_error_log_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gaa8c798b60b3b99ae6b8f8358253d1385)
- [edac_parity_error_log_get](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gaa6cba09e19de241ed045387c85cc3f1c)
- [edac_parity_error_log_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gab60aa37ba86e2038fe979481cc6134c2)
- [edac_errors_cor_get](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gaea2915b6c3c4eef2c94c6f60e788dcfe)
- [edac_errors_uc_get](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#gaec79969648e56e98031d46abe73c2b82)
- [edac_notify_callback_set](https://docs.zephyrproject.org/latest/doxygen/html/group__edac__interface.html#ga2def500f72a06271d9a10243bfdf6527)

<a id="header-details"></a>

---

[上一章](P007_zephyr__dt-bindings__sensor__mcp9600.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__drivers__regulator__fake.h_文件参考.md)
