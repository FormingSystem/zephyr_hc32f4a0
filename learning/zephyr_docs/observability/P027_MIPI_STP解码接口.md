---
id: learning.zephyr-docs.observability.obapi-2
title: MIPI_STP解码接口
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__stp__decoder__apis.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第27章\_MIPI_STP解码接口

原文：[group__mipi__stp__decoder__apis](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__stp__decoder__apis.html)。读取日期：2026-10-13，`latest`。

## 27.1\_头文件与数据类型

本页描述 **MIPI系统跟踪协议第2版（MIPI System Trace Protocol v2，STPv2）**解码器。

```c
#include <zephyr/debug/mipi_stp_decoder.h>
```

关联类型包括[解码配置结构 [`mipi_stp_decoder_config`](https://docs.zephyrproject.org/latest/doxygen/html/structmipi__stp__decoder__config.html)](P028_MIPI_STP解码配置.md)和[操作码数据联合体 [`mipi_stp_decoder_data`](https://docs.zephyrproject.org/latest/doxygen/html/unionmipi__stp__decoder__data.html)](P029_MIPI_STP解码数据.md)。

## 27.2\_操作码类型

枚举 [`mipi_stp_decoder_ctrl_type`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__stp__decoder__apis.html#ga6e1f4b66b14ab44e549292f97046a50d) 定义 STPv2 **操作码（Opcode）**类型。以下保留全部枚举项及显式赋值；原文没有为各项提供单独说明。

<a id="ga6e1f4b66b14ab44e549292f97046a50d"></a>

<pre><code class="language-c">enum mipi_stp_decoder_ctrl_type {
<a id="gga6e1f4b66b14ab44e549292f97046a50da0aa61c6c20ce10ac93ab5d0903af06e5"></a>    STP_DATA4 = 1,
<a id="gga6e1f4b66b14ab44e549292f97046a50da63596fdd07425a6a1a5342528ac22100"></a>    STP_DATA8 = 2,
<a id="gga6e1f4b66b14ab44e549292f97046a50da38ae6c0f7c2f37cdb7068fc6dabb2184"></a>    STP_DATA16 = 4,
<a id="gga6e1f4b66b14ab44e549292f97046a50da43d3753e29c66c1a5c1b9da0b55cd36e"></a>    STP_DATA32 = 8,
<a id="gga6e1f4b66b14ab44e549292f97046a50da6efb90a9074b3ed4d63be65e4245345a"></a>    STP_DATA64 = 16,
<a id="gga6e1f4b66b14ab44e549292f97046a50da062e36cbfa898f544fea1e5ddfed205e"></a>    STP_DECODER_NULL = 128,
<a id="gga6e1f4b66b14ab44e549292f97046a50da4b94577fa87699f6aca63ab9062e42b1"></a>    STP_DECODER_MAJOR,
<a id="gga6e1f4b66b14ab44e549292f97046a50daa0f541093b78f948a6770f16e362560a"></a>    STP_DECODER_MERROR,
<a id="gga6e1f4b66b14ab44e549292f97046a50da6c85b02588c7c1bb07657b4b316bf360"></a>    STP_DECODER_CHANNEL,
<a id="gga6e1f4b66b14ab44e549292f97046a50daf8b791424b5f0e281c64e2258b19129f"></a>    STP_DECODER_VERSION,
<a id="gga6e1f4b66b14ab44e549292f97046a50da2697b0f2083731fb03fd197d2905dd37"></a>    STP_DECODER_FREQ,
<a id="gga6e1f4b66b14ab44e549292f97046a50da853c25efa06fc63571ac14c5696838b7"></a>    STP_DECODER_GERROR,
<a id="gga6e1f4b66b14ab44e549292f97046a50da2007260749b9d89c598a528cc8468ab5"></a>    STP_DECODER_FLAG,
<a id="gga6e1f4b66b14ab44e549292f97046a50da7082b6a478ef3ce82bd97b2aa29bf0ef"></a>    STP_DECODER_ASYNC,
<a id="gga6e1f4b66b14ab44e549292f97046a50da7be5f983d725712fd258d2368d4689c4"></a>    STP_DECODER_NOT_SUPPORTED
};
</code></pre>

## 27.3\_类型名称宏

宏 `STP_DECODER_TYPE2STR(_type)` 将参数 `_type` 表示的类型转换为字符串字面量（String Literal），返回对应字符串。官方给出的宏值如下：

```c
_type == STP_DATA4 ? "DATA4" : (\
_type == STP_DATA8 ? "DATA8" : (\
_type == STP_DATA16 ? "DATA16" : (\
_type == STP_DATA32 ? "DATA32" : (\
_type == STP_DATA64 ? "DATA64" : (\
_type == STP_DECODER_NULL ? "NULL" : (\
_type == STP_DECODER_MAJOR ? "MAJOR" : (\
_type == STP_DECODER_MERROR ? "MERROR" : (\
_type == STP_DECODER_CHANNEL ? "CHANNEL" : (\
_type == STP_DECODER_VERSION ? "VERSION" : (\
_type == STP_DECODER_FREQ ? "FREQ" : (\
_type == STP_DECODER_GERROR ? "GERROR" : (\
_type == STP_DECODER_FLAG ? "FLAG" : (\
_type == STP_DECODER_ASYNC ? "ASYNC" : (\
"Unknown"))))))))))))))
```

## 27.4\_解码回调

回调类型 [`mipi_stp_decoder_cb`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__stp__decoder__apis.html#ga8c6fdc2927d954291a12e4c31ad8abe2) 定义为：

<a id="ga8c6fdc2927d954291a12e4c31ad8abe2"></a>

```c
typedef bool (*mipi_stp_decoder_cb)(enum mipi_stp_decoder_ctrl_type type,
                                  union mipi_stp_decoder_data data,
                                  uint64_t *ts, bool marked);
```

每解出一个 STPv2 流元素，就调用一次回调。**调用回调时中断处于锁定状态。**

| 参数 | 含义 |
| --- | --- |
| `type` | 类型，见 [`mipi_stp_decoder_ctrl_type`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__stp__decoder__apis.html#ga6e1f4b66b14ab44e549292f97046a50d) |
| `data` | 与该类型关联的数据 |
| `ts` | 时间戳（Timestamp）指针；非 `NULL` 时存在时间戳 |
| `marked` | 操作码带标记（Marked）时为 `true` |

回调返回 `true` 表示数据有效；返回 `false` 表示数据指示同步丢失（Synchronization Loss）。

## 27.5\_初始化与解码

<a id="ga4a67705c849793f02c7ae409434b4e79"></a>

<a id="ga520104e814b15cce22ec74a4e827a5b9"></a>

```c
int mipi_stp_decoder_init(const struct mipi_stp_decoder_config *config);
int mipi_stp_decoder_decode(const uint8_t *data, size_t len);
```

[`mipi_stp_decoder_init()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__stp__decoder__apis.html#ga4a67705c849793f02c7ae409434b4e79) 初始化解码器，参数 `config` 为配置。成功返回 `0`，失败返回小于 `0` 的值。

[`mipi_stp_decoder_decode()`](https://docs.zephyrproject.org/latest/doxygen/html/group__mipi__stp__decoder__apis.html#ga520104e814b15cce22ec74a4e827a5b9) 解码 STPv2 流，为每个解出的元素调用回调。`data` 指向数据，`len` 是数据长度。成功返回 `0`，失败返回小于 `0` 的值。

## 27.6\_通知同步丢失

<a id="ga0e1be10f234d72e81b48d21bfe8a42f8"></a>

```c
void mipi_stp_decoder_sync_loss(void);
```

通知解码器发生同步丢失。解码器随后寻找 `ASYNC` 同步标记，在找到之前丢弃所有数据。数据丢失，例如溢出，可能导致同步丢失。

---

[上一章：CoreSight解格式接口](P026_CoreSight解格式接口.md) · [下一章：MIPI_STP解码配置](P028_MIPI_STP解码配置.md) · [返回大纲](大纲.md)
