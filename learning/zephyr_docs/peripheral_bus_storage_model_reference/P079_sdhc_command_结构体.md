---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-79
title: sdhc_command_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsdhc__command.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第79章\_sdhc\_command\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsdhc__command.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

SD主控制器（Host Controller）的命令结构。

```c
#include <zephyr/drivers/sdhc.h>
```

<a id="details"></a>

SD 主机控制器命令结构体（Command structure）。用于向 SD 主机控制器发送命令请求，控制器随后将命令发送给 SD 设备。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 79.1\_数据成员（Data Fields）

<a id="r_a320ad415df67e1d9b4c09f95993dd17f"></a>

```c
uint32_t opcode
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[opcode](#a320ad415df67e1d9b4c09f95993dd17f)。

SD 主机规范定义的 CMD 索引。

<a id="r_af6b98d5f1cecf25af2480b1d359f200e"></a>

```c
uint32_t arg
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[arg](#af6b98d5f1cecf25af2480b1d359f200e)。

SD 主机规范定义的命令参数（Argument）。

<a id="r_a37a3c1608b5c13311c833c4ad24ff1f9"></a>

```c
uint32_t response [4]
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[response](#a37a3c1608b5c13311c833c4ad24ff1f9)。

SD 卡响应字段。

<a id="r_af758a4e0e3b090912f6e9abd7c4be8f3"></a>

```c
uint32_t response_type
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[response_type](#af758a4e0e3b090912f6e9abd7c4be8f3)。

预期的 SD 响应类型。

<a id="r_a39ba0b1e99814471939dc7bbb7d098eb"></a>

```c
unsigned int retries
```

相关声明：[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)、[retries](#a39ba0b1e99814471939dc7bbb7d098eb)。

最大重试次数（Retries）。

<a id="r_a92cf023d28aa6106d603ff7f67a7e04b"></a>

```c
int timeout_ms
```

相关声明：[timeout_ms](#a92cf023d28aa6106d603ff7f67a7e04b)。

命令超时，单位为毫秒。

## 79.2\_详细说明（Detailed Documentation）

<a id="af6b98d5f1cecf25af2480b1d359f200e"></a>

### `arg`

```c
uint32_t sdhc_command::arg
```

SD 主机规范定义的命令参数（Argument）。

<a id="a320ad415df67e1d9b4c09f95993dd17f"></a>

### `opcode`

```c
uint32_t sdhc_command::opcode
```

SD 主机规范定义的 CMD 索引。

<a id="a37a3c1608b5c13311c833c4ad24ff1f9"></a>

### `response`

```c
uint32_t sdhc_command::response[4]
```

SD 卡响应字段。

<a id="af758a4e0e3b090912f6e9abd7c4be8f3"></a>

### `response_type`

```c
uint32_t sdhc_command::response_type
```

预期的 SD 响应类型。

<a id="a39ba0b1e99814471939dc7bbb7d098eb"></a>

### `retries`

```c
unsigned int sdhc_command::retries
```

最大重试次数（Retries）。

<a id="a92cf023d28aa6106d603ff7f67a7e04b"></a>

### `timeout_ms`

```c
int sdhc_command::timeout_ms
```

命令超时，单位为毫秒。

本数据类型文档由以下文件生成：

- `zephyr/drivers/sdhc.h`

## 79.3\_原页交叉引用（Cross References）

- [zephyr/drivers/sdhc.h](https://docs.zephyrproject.org/latest/doxygen/html/sdhc_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P078_sd_switch_caps_结构体.md) · [返回大纲](大纲.md) · [下一章](P080_sdhc_data_结构体.md)
