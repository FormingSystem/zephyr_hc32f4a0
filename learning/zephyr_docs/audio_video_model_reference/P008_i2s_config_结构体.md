---
id: learning.zephyr-docs.audio-video-model-reference.page-8
title: i2s_config_结构体
kind: reference
status: maintained
domains: [zephyr, multimedia, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structi2s__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_i2s\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structi2s__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

接口配置选项（Interface Configuration Options）。

```c
#include <zephyr/drivers/i2s.h>
```

<a id="details"></a>

接口配置选项。用户必须定义并初始化 `mem_slab` 字段指向的内存片（memory slab）。为了让 I2S 驱动正确工作，每个队列对应的内存片至少需要 2 个内存块。内存块大小应为帧大小 `frame_size` 的整数倍，其中 `frame_size = (channels * word_size_bytes)`。例如，16 位数据字占 2 字节，24 位或 32 位数据字占 4 字节。关于内存片的更多信息，请参阅 Zephyr 内核入门（Zephyr Kernel Primer）。备注：选择 I2S 数据格式时，忽略 `channels` 参数，每帧始终包含 2 个数据字。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 8.1\_数据成员（Data Fields）

<a id="r_a5a38a75f0b4a3356ed85495fb45d0cd2"></a>

```c
uint8_t word_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[word_size](#a5a38a75f0b4a3356ed85495fb45d0cd2)。

表示一个数据字的位数。

<a id="r_acd9ff8b9a0e79e95a8deb19df145478d"></a>

```c
uint8_t channels
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[channels](#acd9ff8b9a0e79e95a8deb19df145478d)。

每帧的数据字数。

<a id="r_a9ab2e8fa330473be99ce0713aec60daf"></a>

```c
i2s_fmt_t format
```

相关声明：[i2s_fmt_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga0939a3ba04a233d9d637fba8a42b0bbb)、[format](#a9ab2e8fa330473be99ce0713aec60daf)。

由 `I2S_FMT_*` 常量定义的数据流格式。

<a id="r_a56a9caaf8133ced8e47e3699e322fdab"></a>

```c
i2s_opt_t options
```

相关声明：[i2s_opt_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gad0ca475f9bf5edeecc7de65b4f56c119)、[options](#a56a9caaf8133ced8e47e3699e322fdab)。

由 `I2S_OPT_*` 常量定义的配置选项。

<a id="r_ab5b0556fcd113c6c645e265af4846b45"></a>

```c
uint32_t frame_clk_freq
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[frame_clk_freq](#ab5b0556fcd113c6c645e265af4846b45)。

帧时钟（WS）频率，即采样率。

<a id="r_a11991601fa180ead06a23b90a58136ff"></a>

```c
struct k_mem_slab * mem_slab
```

相关声明：[mem_slab](#a11991601fa180ead06a23b90a58136ff)。

用于存储 RX/TX 数据的内存片（memory slab）。

<a id="r_a62f504e954fc42c343d142513bbaf4ef"></a>

```c
size_t block_size
```

相关声明：[block_size](#a62f504e954fc42c343d142513bbaf4ef)。

单个接收/发送（RX/TX）内存块或缓冲区的大小，单位为字节。

<a id="r_a9bf6c6cb96cc9c3acd8efc3fad0cbca9"></a>

```c
int32_t timeout
```

相关声明：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)、[timeout](#a9bf6c6cb96cc9c3acd8efc3fad0cbca9)。

读写超时（Read/Write timeout）。

## 8.2\_详细说明（Detailed Documentation）

<a id="a62f504e954fc42c343d142513bbaf4ef"></a>

### `block_size`

```c
size_t i2s_config::block_size
```

单个接收/发送（RX/TX）内存块或缓冲区的大小，单位为字节。

<a id="acd9ff8b9a0e79e95a8deb19df145478d"></a>

### `channels`

```c
uint8_t i2s_config::channels
```

每帧的数据字数。

<a id="a9ab2e8fa330473be99ce0713aec60daf"></a>

### `format`

```c
i2s_fmt_t i2s_config::format
```

由 `I2S_FMT_*` 常量定义的数据流格式。

<a id="ab5b0556fcd113c6c645e265af4846b45"></a>

### `frame_clk_freq`

```c
uint32_t i2s_config::frame_clk_freq
```

帧时钟（WS）频率，即采样率。

<a id="a11991601fa180ead06a23b90a58136ff"></a>

### `mem_slab`

```c
struct k_mem_slab* i2s_config::mem_slab
```

用于存储 RX/TX 数据的内存片（memory slab）。

<a id="a56a9caaf8133ced8e47e3699e322fdab"></a>

### `options`

```c
i2s_opt_t i2s_config::options
```

由 `I2S_OPT_*` 常量定义的配置选项。

<a id="a9bf6c6cb96cc9c3acd8efc3fad0cbca9"></a>

### `timeout`

```c
int32_t i2s_config::timeout
```

读写超时（Read/Write timeout）。

发送队列已满或接收队列为空时等待的毫秒数，也可以为 0 或 `SYS_FOREVER_MS`。`i2s_buf_write()` 也将此超时应用于发送内存块的分配。

<a id="a5a38a75f0b4a3356ed85495fb45d0cd2"></a>

### `word_size`

```c
uint8_t i2s_config::word_size
```

表示一个数据字的位数。

本数据类型文档由以下文件生成：

- `zephyr/drivers/i2s.h`

## 8.3\_原页交叉引用（Cross References）

- [zephyr/drivers/i2s.h](https://docs.zephyrproject.org/latest/doxygen/html/i2s_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [i2s_fmt_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga0939a3ba04a233d9d637fba8a42b0bbb)
- [i2s_opt_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#gad0ca475f9bf5edeecc7de65b4f56c119)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [i2s_buf_write()](https://docs.zephyrproject.org/latest/doxygen/html/group__i2s__interface.html#ga98cbfe351a8dd5db361f4667959d0b58)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P007_dmic_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P009_i2s_driver_api_结构体.md)
