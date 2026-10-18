---
id: learning.zephyr-docs.platform-security-model-reference.page-62
title: tee_shm_结构体
kind: reference
status: maintained
domains: [zephyr, platform, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structtee__shm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_tee\_shm\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structtee__shm.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

可信执行环境（TEE）的共享内存结构。

```c
#include <zephyr/drivers/tee.h>
```

<a id="details"></a>

可信执行环境（TEE）的共享内存结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 62.1\_数据成员（Data Fields）

<a id="r_ab761c1d3d5e64c21725eff97521b4b86"></a>

```c
const struct device * dev
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[dev](#ab761c1d3d5e64c21725eff97521b4b86)。

[out] 指向设备驱动结构体的指针。

<a id="r_a65446310f73319aa5f8e100e4d83198e"></a>

```c
void * addr
```

相关声明：[addr](#a65446310f73319aa5f8e100e4d83198e)。

[out] 共享缓冲区指针。

<a id="r_a02fe0fd69f1e8d5650cfa116136ea9ca"></a>

```c
uint64_t size
```

相关声明：[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[size](#a02fe0fd69f1e8d5650cfa116136ea9ca)。

[out] 共享缓冲区大小。

<a id="r_ac2738d87cbe439f093cad67a375c2807"></a>

```c
uint32_t flags
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[flags](#ac2738d87cbe439f093cad67a375c2807)。

[out] 共享缓冲区标志。

## 62.2\_详细说明（Detailed Documentation）

<a id="a65446310f73319aa5f8e100e4d83198e"></a>

### `addr`

```c
void* tee_shm::addr
```

[out] 共享缓冲区指针。

<a id="ab761c1d3d5e64c21725eff97521b4b86"></a>

### `dev`

```c
const struct device* tee_shm::dev
```

[out] 指向设备驱动结构体的指针。

<a id="ac2738d87cbe439f093cad67a375c2807"></a>

### `flags`

```c
uint32_t tee_shm::flags
```

[out] 共享缓冲区标志。

<a id="a02fe0fd69f1e8d5650cfa116136ea9ca"></a>

### `size`

```c
uint64_t tee_shm::size
```

[out] 共享缓冲区大小。

本数据类型文档由以下文件生成：

- `zephyr/drivers/tee.h`

## 62.3\_原页交叉引用（Cross References）

- [zephyr/drivers/tee.h](https://docs.zephyrproject.org/latest/doxygen/html/tee_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P061_tee_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P063_tee_version_info_结构体.md)
