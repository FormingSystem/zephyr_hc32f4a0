---
id: learning.zephyr-docs.hardware.adcbackend-1
title: ADC解码器API结构
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structadc__decoder__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第455章\_ADC解码器API结构

原文：[structadc__decoder__api](https://docs.zephyrproject.org/latest/doxygen/html/structadc__decoder__api.html)。读取日期：2026-10-13，`latest`。

## 455.1\_用途与头文件

`struct adc_decoder_api` 解码单个原始数据缓冲区，属于**模数转换器（Analog-to-Digital Converter，ADC）**的解码器应用程序接口（Decoder Application Programming Interface，Decoder API）。头文件为 `zephyr/drivers/adc.h`。

以下函数指针中的 `buffer` 都是**实时输入输出（Real-Time Input/Output，RTIO）**上下文提供的缓冲区。

## 455.2\_获取帧数

[`get_frame_count`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__decoder__api.html#a1d53d62e633b19f3b0ad3bb10174894e) 获取当前缓冲区中指定通道的帧（Frame）数量。

```c
int (*get_frame_count)(const uint8_t *buffer, uint32_t channel,
                       uint16_t *frame_count);
```

| 参数 | 方向 | 含义 |
| --- | --- | --- |
| `buffer` | 输入 | RTIO 上下文提供的缓冲区 |
| `channel` | 输入 | 要查询帧数的通道 |
| `frame_count` | 输出 | 缓冲区中的帧数，至少为 1 |

成功返回 0；未找到指定通道/通道索引时返回 `-ENOTSUP`（不支持，Not Supported）。原文把通道索引写为 `channel_idx`，函数声明仍按原文保留 `channel` 参数。

## 455.3\_获取解码所需空间

[`get_size_info`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__decoder__api.html#a2b40bb548037e1a8f811eeacf459636f) 获取解码指定通道所需的存储大小。

```c
int (*get_size_info)(struct adc_dt_spec adc_spec, uint32_t channel,
                    size_t *base_size, size_t *frame_size);
```

| 参数 | 方向 | 含义 |
| --- | --- | --- |
| `adc_spec` | 输入 | ADC 规格，按值传入 |
| `channel` | 输入 | 要查询的通道 |
| `base_size` | 输出 | 解码第一帧所需大小 |
| `frame_size` | 输出 | 每增加一帧所需的附加大小 |

只解码一帧时使用 `base_size`；每增加一帧，再增加一个 `frame_size`。例如，解码 3 帧需要 `base_size + 2 * frame_size`。

成功返回 0；不支持该通道时返回 `-ENOTSUP`。

## 455.4\_解码样本

[`decode`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__decoder__api.html#acdbfeda4bfbb7afd77fa86be27c3e333) 从缓冲区中最多解码 `max_count` 个样本，可以跨多个帧解码指定通道的数据。原文说明：同一通道存在多个实例时，用 `channel_index` 区分它们。

```c
int (*decode)(const uint8_t *buffer, uint32_t channel, uint32_t *fit,
              uint16_t max_count, void *data_out);
```

| 参数 | 方向 | 含义 |
| --- | --- | --- |
| `buffer` | 输入 | RTIO 上下文提供的缓冲区 |
| `channel` | 输入 | 要解码的通道 |
| `fit` | 输入/输出 | 当前帧迭代器（Frame Iterator） |
| `max_count` | 输入 | 原参数说明写作“最多解码的通道数” |
| `data_out` | 输出 | 解码后的数据 |

返回 0 表示没有更多样本可解码；返回正数表示解码出的帧数；负数表示错误。

译注：原摘要使用“样本数”，参数说明使用“通道数”，返回说明使用“帧数”，这里保留三处用词差异。`channel_index` 出现在说明中，但不是本函数声明中的独立参数，不能据此增加参数或改动签名。

## 455.5\_检查触发类型

[`has_trigger`](https://docs.zephyrproject.org/latest/doxygen/html/structadc__decoder__api.html#a13dfea96d809dc9705bbf030d44ccb20) 检查缓冲区是否包含给定触发类型（Trigger Type）。

```c
bool (*has_trigger)(const uint8_t *buffer, enum adc_trigger_type trigger);
```

`buffer` 为输入 RTIO 缓冲区，`trigger` 为要检查的输入触发类型。返回值表示该触发类型是否存在于缓冲区中。

---

[上一章：ADC驱动API结构](P454_ADC驱动API结构.md) · [下一章：ADC驱动后端](P456_ADC驱动后端.md) · [返回大纲](大纲.md)
