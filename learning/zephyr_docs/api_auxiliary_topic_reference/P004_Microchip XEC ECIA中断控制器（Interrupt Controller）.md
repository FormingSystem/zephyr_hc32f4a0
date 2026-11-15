---
id: learning.zephyr-docs.api-auxiliary-topic-reference.page-4
title: Microchip XEC ECIA中断控制器（Interrupt Controller）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dt__mchp__xec__ecia.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_Microchip XEC ECIA中断控制器（Interrupt Controller）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__mchp__xec__ecia.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Microchip XEC ECIA 中断聚合器（Interrupt Aggregator）的设备树宏。

<a id="details"></a>

Microchip XEC 嵌入式控制器中断聚合器（Embedded Controller Interrupt Aggregator，ECIA）的设备树宏。用于为兼容 `microchip,xec-ecia` 的 ECIA 编码外设中断信息。`MCHP_XEC_ECIA()` 将分组中断请求（GIRQ）编号、该 GIRQ 内的源位位置以及聚合／直接 NVIC 输入打包为一个 32 位值；`MCHP_XEC_ECIA_GIRQ_ENC()` 仅编码 GIRQ 和位位置。相应的 `MCHP_XEC_ECIA_*` 访问宏提取各字段。下方保留原始配置示例。

```c
&some_device {
        girqs = <MCHP_XEC_ECIA(21, 8, 13, 119)>;
};
```

<a id="header-files"></a>
<a id="files"></a>

## 4.1\_文件（Files）

<a id="r_mchp-xec-ecia_2Eh"></a>

```c
file mchp-xec-ecia.h
```

相关声明：[mchp-xec-ecia.h](../api_file_management_reference/P029_zephyr__dt-bindings__interrupt-controller__mchp-xec-ecia.h_文件参考.md)。

Microchip XEC嵌入式控制器中断聚合器（ECIA）的设备树宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_gaca04c194e5bdd4922d927b35f39fbe79"></a>

```c
#define MCHP_XEC_ECIA_GIRQ_ENC(g, b)
```

相关声明：[MCHP_XEC_ECIA_GIRQ_ENC](#gaca04c194e5bdd4922d927b35f39fbe79)。

仅编码外设的分组中断请求（GIRQ）及 GIRQ 位位置。

<a id="r_gac1daa9f5e1b5764f0748577ee60550d3"></a>

```c
#define MCHP_XEC_ECIA(g, gb, na, nd)
```

相关声明：[MCHP_XEC_ECIA](#gac1daa9f5e1b5764f0748577ee60550d3)。

将外设中断信息（peripheral interrupt information）编码为一个 32 位值。

<a id="r_ga6fee82b914dc9f73392586224f0708e7"></a>

```c
#define MCHP_XEC_ECIA_GIRQ(e)
```

相关声明：[MCHP_XEC_ECIA_GIRQ](#ga6fee82b914dc9f73392586224f0708e7)。

从已编码的 `MCHP_XEC_ECIA()` 值提取 GIRQ 编号。

<a id="r_ga32c0b5e661fbee763a496b3b06eae34a"></a>

```c
#define MCHP_XEC_ECIA_GIRQ_POS(e)
```

相关声明：[MCHP_XEC_ECIA_GIRQ_POS](#ga32c0b5e661fbee763a496b3b06eae34a)。

从已编码的 `MCHP_XEC_ECIA()` 值提取中断源位位置。

<a id="r_ga9099e944648c0d8b6946b2092f872122"></a>

```c
#define MCHP_XEC_ECIA_NVIC_AGGR(e)
```

相关声明：[MCHP_XEC_ECIA_NVIC_AGGR](#ga9099e944648c0d8b6946b2092f872122)。

从已编码的 `MCHP_XEC_ECIA()` 值提取聚合 GIRQ 的 NVIC 编号。

<a id="r_ga1efb0ece73d7b15da7cdc316c162bc3a"></a>

```c
#define MCHP_XEC_ECIA_NVIC_DIRECT(e)
```

相关声明：[MCHP_XEC_ECIA_NVIC_DIRECT](#ga1efb0ece73d7b15da7cdc316c162bc3a)。

从已编码的 `MCHP_XEC_ECIA()` 值提取直接中断的 NVIC 编号。

## 4.3\_详细说明（Detailed Documentation）

<a id="gac1daa9f5e1b5764f0748577ee60550d3"></a>

### `MCHP_XEC_ECIA`

```c
#define MCHP_XEC_ECIA ( g, gb, na, nd )
```

```c
#include <zephyr/dt-bindings/interrupt-controller/mchp-xec-ecia.h>
```

展开值（Value）：

```c
(((g) & 0x1f) + (((gb) & 0x1f) << 8) + (((na) & 0xff) << 16) +  \
(((nd) & 0xff) << 24))
```

将外设中断信息（peripheral interrupt information）编码为一个 32 位值。

位 `[4:0]` 保存 GIRQ 编号，范围为 `[8, 26]`；位 `[12:8]` 保存该 GIRQ 内的外设源位位置，范围为 `[0, 31]`；位 `[23:16]` 保存聚合 GIRQ 的 NVIC 编号；位 `[31:24]` 保存直接 NVIC 编号。对于没有直接连接的中断源，将 `nd` 设为与 `na` 相同。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `g` | GIRQ 编号，范围为 `[8, 26]`。 |
| `gb` | GIRQ 内的外设源位位置，范围为 `[0, 31]`。 |
| `na` | 聚合 GIRQ 的 NVIC 编号。 |
| `nd` | 直接 NVIC 编号。 |

**说明（Note）**：注意：GIRQ22 仅用于外设时钟唤醒（peripheral clock wake）。GIRQ22 及其各中断源未连接到 NVIC；`na` 和 `nd` 均应使用 255。

<a id="ga6fee82b914dc9f73392586224f0708e7"></a>

### `MCHP_XEC_ECIA_GIRQ`

```c
#define MCHP_XEC_ECIA_GIRQ ( e)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/mchp-xec-ecia.h>
```

展开值（Value）：

```c
((e) & 0x1f)
```

从已编码的 `MCHP_XEC_ECIA()` 值提取 GIRQ 编号。

<a id="gaca04c194e5bdd4922d927b35f39fbe79"></a>

### `MCHP_XEC_ECIA_GIRQ_ENC`

```c
#define MCHP_XEC_ECIA_GIRQ_ENC ( g, b )
```

```c
#include <zephyr/dt-bindings/interrupt-controller/mchp-xec-ecia.h>
```

展开值（Value）：

```c
(((g) & 0x1f) + (((b) & 0x1f) << 8))
```

仅编码外设的分组中断请求（GIRQ）及 GIRQ 位位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `g` | GIRQ 编号，范围为 `[8, 26]`。 |
| `b` | GIRQ 内的源位位置，范围为 `[0, 31]`。 |

<a id="ga32c0b5e661fbee763a496b3b06eae34a"></a>

### `MCHP_XEC_ECIA_GIRQ_POS`

```c
#define MCHP_XEC_ECIA_GIRQ_POS ( e)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/mchp-xec-ecia.h>
```

展开值（Value）：

```c
(((e) >> 8) & 0x1f)
```

从已编码的 `MCHP_XEC_ECIA()` 值提取中断源位位置。

<a id="ga9099e944648c0d8b6946b2092f872122"></a>

### `MCHP_XEC_ECIA_NVIC_AGGR`

```c
#define MCHP_XEC_ECIA_NVIC_AGGR ( e)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/mchp-xec-ecia.h>
```

展开值（Value）：

```c
(((e) >> 16) & 0xff)
```

从已编码的 `MCHP_XEC_ECIA()` 值提取聚合 GIRQ 的 NVIC 编号。

<a id="ga1efb0ece73d7b15da7cdc316c162bc3a"></a>

### `MCHP_XEC_ECIA_NVIC_DIRECT`

```c
#define MCHP_XEC_ECIA_NVIC_DIRECT ( e)
```

```c
#include <zephyr/dt-bindings/interrupt-controller/mchp-xec-ecia.h>
```

展开值（Value）：

```c
(((e) >> 24) & 0xff)
```

从已编码的 `MCHP_XEC_ECIA()` 值提取直接中断的 NVIC 编号。


## 4.4\_原页交叉引用（Cross References）

- [mchp-xec-ecia.h](../api_file_management_reference/P029_zephyr__dt-bindings__interrupt-controller__mchp-xec-ecia.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P003_设备多路复用器（Devmux）.md) · [返回大纲](大纲.md) · [下一章](P005_模拟器（Simulator）.md)
