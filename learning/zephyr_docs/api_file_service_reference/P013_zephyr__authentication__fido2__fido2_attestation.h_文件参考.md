---
id: learning.zephyr-docs.api-file-service-reference.page-13
title: zephyr__authentication__fido2__fido2_attestation.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fido2__attestation_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_zephyr\_\_authentication\_\_fido2\_\_fido2\_attestation.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fido2__attestation_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

FIDO2证明回调（Attestation Callback）的API。

<a id="details"></a>

```c
#include <stddef.h>
#include <stdint.h>
```

查看此文件的源码。

FIDO2证明回调（Attestation Callback）的API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 13.1\_数据结构（Data Structures）

<a id="r_fido2_5Fattestation_5Fresult"></a>

```c
struct fido2_attestation_result
```

相关声明：[fido2_attestation_result](../platform_security_model_reference/P006_fido2_attestation_result_结构体.md)。

证明回调（Attestation Callback）产生的证明结果。

<a id="r_gaa8a025dbfc332bb3b8b3829b3f4bda69"></a>

```c
#define FIDO2_ATTESTATION_FMT_PACKED "packed"
```

相关声明：[FIDO2_ATTESTATION_FMT_PACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaa8a025dbfc332bb3b8b3829b3f4bda69)。

FIDO2 证明（Attestation）。

<a id="r_ga09c488599bae6b3454023bf696ecd6e0"></a>

```c
#define FIDO2_ATTESTATION_FMT_NONE "none"
```

相关声明：[FIDO2_ATTESTATION_FMT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga09c488599bae6b3454023bf696ecd6e0)。

不提供证明（No Attestation）。

<a id="r_ga25c2604da4e7adb9ec186a846265b1bc"></a>

```c
#define FIDO2_ATTESTATION_FMT_MAX_LEN 32
```

相关声明：[FIDO2_ATTESTATION_FMT_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga25c2604da4e7adb9ec186a846265b1bc)。

证明格式标识（Attestation Format Identifier）的最大长度。

<a id="r_gaf81f2aff090633c893740db7b60ed614"></a>

```c
int fido2_attestation_sign (const uint8_t *auth_data, size_t auth_data_len, const uint8_t *client_data_hash, uint32_t credential_key_id, struct fido2_attestation_result *result)
```

相关声明：[fido2_attestation_sign](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaf81f2aff090633c893740db7b60ed614)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[fido2_attestation_result](../platform_security_model_reference/P006_fido2_attestation_result_结构体.md)。

为新凭据（Credential）签署 `authenticatorData`。


## 13.2\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P259_fido2_attestation.h_源码浏览.md)
- [fido2_attestation_result](../platform_security_model_reference/P006_fido2_attestation_result_结构体.md)
- [FIDO2_ATTESTATION_FMT_PACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaa8a025dbfc332bb3b8b3829b3f4bda69)
- [FIDO2_ATTESTATION_FMT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga09c488599bae6b3454023bf696ecd6e0)
- [FIDO2_ATTESTATION_FMT_MAX_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#ga25c2604da4e7adb9ec186a846265b1bc)
- [fido2_attestation_sign](https://docs.zephyrproject.org/latest/doxygen/html/group__fido2.html#gaf81f2aff090633c893740db7b60ed614)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>

---

[上一章](P012_zephyr__drivers__comparator__fake_comp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P014_zephyr__drivers__misc__ft8xx__ft8xx_memory.h_文件参考.md)
