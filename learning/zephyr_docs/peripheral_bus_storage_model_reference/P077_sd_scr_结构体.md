---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-77
title: sd_scr_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsd__scr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第77章\_sd\_scr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsd__scr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SD卡配置寄存器（Card Configuration Register）。

```c
#include <zephyr/sd/sd_spec.h>
```

<a id="details"></a>

SD 卡配置寄存器（SD Configuration Register，SCR），包含更多 SD 卡数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 77.1\_数据成员（Data Fields）

<a id="r_a3fc37c731dfb5c5596b6389152479c07"></a>

```c
uint8_t scr_structure
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[scr_structure](#a3fc37c731dfb5c5596b6389152479c07)。

SCR 结构（SCR Structure）`[63:60]`。

<a id="r_ae6201af1083efa828cced000874bf197"></a>

```c
uint8_t sd_spec
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sd_spec](#ae6201af1083efa828cced000874bf197)。

SD 存储卡规范版本 `[59:56]`。

<a id="r_abda65da85e20979a1fc71f2aea1f947b"></a>

```c
uint16_t flags
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[flags](#abda65da85e20979a1fc71f2aea1f947b)。

`_sd_scr_flag` 中的 SCR 标志。

<a id="r_a9f8254b5fe6911156bae727e29262f5a"></a>

```c
uint8_t sd_sec
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sd_sec](#a9f8254b5fe6911156bae727e29262f5a)。

支持的安全规范（Security specification）`[54:52]`。

<a id="r_a40d30ccc4daf2c32f2ac162b402f3887"></a>

```c
uint8_t sd_width
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sd_width](#a40d30ccc4daf2c32f2ac162b402f3887)。

支持的数据总线宽度 `[51:48]`。

<a id="r_a15f60bc2115b943ce938f3a96dd8e547"></a>

```c
uint8_t sd_ext_sec
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[sd_ext_sec](#a15f60bc2115b943ce938f3a96dd8e547)。

扩展安全支持（Extended security support）`[46:43]`。

<a id="r_a9016ca73a668499289c52355ebb83cb1"></a>

```c
uint8_t cmd_support
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd_support](#a9016ca73a668499289c52355ebb83cb1)。

命令支持位 `[33:32]`：位 33 表示支持 `CMD23`，位 32 表示支持 `cmd20`。

<a id="r_aba20efcf752335f1a86d0a86607d92d0"></a>

```c
uint32_t rsvd
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[rsvd](#aba20efcf752335f1a86d0a86607d92d0)。

保留供制造商使用 `[31:0]`。

## 77.2\_详细说明（Detailed Documentation）

<a id="a9016ca73a668499289c52355ebb83cb1"></a>

### `cmd_support`

```c
uint8_t sd_scr::cmd_support
```

命令支持位 `[33:32]`：位 33 表示支持 `CMD23`，位 32 表示支持 `cmd20`。

<a id="abda65da85e20979a1fc71f2aea1f947b"></a>

### `flags`

```c
uint16_t sd_scr::flags
```

`_sd_scr_flag` 中的 SCR 标志。

<a id="aba20efcf752335f1a86d0a86607d92d0"></a>

### `rsvd`

```c
uint32_t sd_scr::rsvd
```

保留供制造商使用 `[31:0]`。

<a id="a3fc37c731dfb5c5596b6389152479c07"></a>

### `scr_structure`

```c
uint8_t sd_scr::scr_structure
```

SCR 结构（SCR Structure）`[63:60]`。

<a id="a15f60bc2115b943ce938f3a96dd8e547"></a>

### `sd_ext_sec`

```c
uint8_t sd_scr::sd_ext_sec
```

扩展安全支持（Extended security support）`[46:43]`。

<a id="a9f8254b5fe6911156bae727e29262f5a"></a>

### `sd_sec`

```c
uint8_t sd_scr::sd_sec
```

支持的安全规范（Security specification）`[54:52]`。

<a id="ae6201af1083efa828cced000874bf197"></a>

### `sd_spec`

```c
uint8_t sd_scr::sd_spec
```

SD 存储卡规范版本 `[59:56]`。

<a id="a40d30ccc4daf2c32f2ac162b402f3887"></a>

### `sd_width`

```c
uint8_t sd_scr::sd_width
```

支持的数据总线宽度 `[51:48]`。

本数据类型文档由以下文件生成：

- `zephyr/sd/sd_spec.h`

## 77.3\_原页交叉引用（Cross References）

- [zephyr/sd/sd_spec.h](https://docs.zephyrproject.org/latest/doxygen/html/sd__spec_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P076_sd_csd_结构体.md) · [返回大纲](大纲.md) · [下一章](P078_sd_switch_caps_结构体.md)
