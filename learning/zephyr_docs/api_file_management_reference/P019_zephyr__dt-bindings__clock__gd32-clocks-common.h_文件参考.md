---
id: learning.zephyr-docs.api-file-management-reference.page-19
title: zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_zephyr\_\_dt-bindings\_\_clock\_\_gd32-clocks-common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gd32-clocks-common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 19.1\_宏定义（Macros）

<a id="r_a8b1e411caae3c88322d85671558b2bbc"></a>

```c
#define GD32_CLOCK_CONFIG(reg, bit)
```

相关声明：[GD32_CLOCK_CONFIG](#a8b1e411caae3c88322d85671558b2bbc)。

编码复位与时钟单元（RCU）的寄存器偏移量和配置位。

## 19.2\_详细说明（Detailed Documentation）

<a id="a8b1e411caae3c88322d85671558b2bbc"></a>

### `GD32_CLOCK_CONFIG`

```c
#define GD32_CLOCK_CONFIG ( reg, bit )
```

展开值（Value）：

```c
(((GD32_ ## reg ## _OFFSET) << 6U) | (bit))
```

编码复位与时钟单元（RCU）的寄存器偏移量和配置位。

- 位 0–5：位编号（bit number）。
- 位 6–14：偏移量（offset）。
- 位 15：保留（reserved）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `reg` | RCU 寄存器名称，展开为 `GD32_{reg}_OFFSET`。 |
| `bit` | 配置位（configuration bit）。 |


## 19.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P285_gd32-clocks-common.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P018_zephyr__platform__fwargs.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P020_zephyr__sys__heap_kasan.h_文件参考.md)
