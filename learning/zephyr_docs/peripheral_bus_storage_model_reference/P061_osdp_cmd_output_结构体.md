---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-61
title: osdp_cmd_output_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structosdp__cmd__output.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第61章\_osdp\_cmd\_output\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structosdp__cmd__output.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

控制面板（CP）发送的命令，用于控制外设（PD）的数字输出。

```c
#include <zephyr/mgmt/osdp.h>
```

<a id="details"></a>

控制面板（CP）发送的命令，用于控制外设（PD）的数字输出。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 61.1\_数据成员（Data Fields）

<a id="r_af5e1d55c987dd82ed4959f251a811846"></a>

```c
uint8_t output_no
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[output_no](#af5e1d55c987dd82ed4959f251a811846)。

输出编号。

<a id="r_a1037244ed5f7c78eab51d6c08130b5d0"></a>

```c
uint8_t control_code
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[control_code](#a1037244ed5f7c78eab51d6c08130b5d0)。

控制码（Control code）。

<a id="r_a4cd89d5c683b31d0e8eaf007443703a6"></a>

```c
uint16_t timer_count
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[timer_count](#a4cd89d5c683b31d0e8eaf007443703a6)。

时间，以 100 ms 为单位。

## 61.2\_详细说明（Detailed Documentation）

<a id="a1037244ed5f7c78eab51d6c08130b5d0"></a>

### `control_code`

```c
uint8_t osdp_cmd_output::control_code
```

控制码（Control code）。

- `0`：无操作（NOP），不改变此输出。
- `1`：将永久状态设为关闭（OFF），中止定时操作（如有）。
- `2`：将永久状态设为开启（ON），中止定时操作（如有）。
- `3`：将永久状态设为关闭（OFF），允许定时操作执行完毕。
- `4`：将永久状态设为开启（ON），允许定时操作执行完毕。
- `5`：将临时状态设为开启（ON），超时后恢复永久状态。
- `6`：将临时状态设为关闭（OFF），超时后恢复永久状态。

<a id="af5e1d55c987dd82ed4959f251a811846"></a>

### `output_no`

```c
uint8_t osdp_cmd_output::output_no
```

输出编号。

`0` 表示第一个输出，`1` 表示第二个输出，依此类推。

<a id="a4cd89d5c683b31d0e8eaf007443703a6"></a>

### `timer_count`

```c
uint16_t osdp_cmd_output::timer_count
```

时间，以 100 ms 为单位。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/osdp.h`

## 61.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/osdp.h](https://docs.zephyrproject.org/latest/doxygen/html/osdp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P060_osdp_cmd_led_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P062_osdp_cmd_text_结构体.md)
