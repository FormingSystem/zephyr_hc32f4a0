---
id: learning.zephyr-docs.platform-security-model-reference.page-63
title: tee_version_info_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtee__version__info.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第63章\_tee\_version\_info\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtee__version__info.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

可信执行环境（TEE）的版本。

```c
#include <zephyr/drivers/tee.h>
```

<a id="details"></a>

TEE 版本（Version）。标识 TEE 实现；`impl_id` 为上述 `TEE_IMPL_ID_*` 值之一。`impl_caps` 由具体实现定义，例如，当 `impl_id == TEE_IMPL_ID_OPTEE` 时，`TEE_OPTEE_CAP_*` 有效。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 63.1\_数据成员（Data Fields）

<a id="r_aaf74a1ff5fb899a0675724669a7d7e36"></a>

```c
uint32_t impl_id
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[impl_id](#aaf74a1ff5fb899a0675724669a7d7e36)。

[out] TEE 实现 ID。

<a id="r_a6cbf12676e5cfc1bdf4221a8188bf055"></a>

```c
uint32_t impl_caps
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[impl_caps](#a6cbf12676e5cfc1bdf4221a8188bf055)。

[out] 实现特定的能力（Capabilities）。

<a id="r_a56a3c50a69f125428dfbf7a867cb7177"></a>

```c
uint32_t gen_caps
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[gen_caps](#a56a3c50a69f125428dfbf7a867cb7177)。

通用能力（Generic capabilities），由上述 `TEE_GEN_CAPS_*` 定义。

## 63.2\_详细说明（Detailed Documentation）

<a id="a56a3c50a69f125428dfbf7a867cb7177"></a>

### `gen_caps`

```c
uint32_t tee_version_info::gen_caps
```

通用能力（Generic capabilities），由上述 `TEE_GEN_CAPS_*` 定义。

<a id="a6cbf12676e5cfc1bdf4221a8188bf055"></a>

### `impl_caps`

```c
uint32_t tee_version_info::impl_caps
```

[out] 实现特定的能力（Capabilities）。

<a id="aaf74a1ff5fb899a0675724669a7d7e36"></a>

### `impl_id`

```c
uint32_t tee_version_info::impl_id
```

[out] TEE 实现 ID。

本数据类型文档由以下文件生成：

- `zephyr/drivers/tee.h`

## 63.3\_原页交叉引用（Cross References）

- [zephyr/drivers/tee.h](https://docs.zephyrproject.org/latest/doxygen/html/tee_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P062_tee_shm_结构体.md) · [返回大纲](大纲.md) · [下一章](P064_tisci_clock_config_结构体.md)
