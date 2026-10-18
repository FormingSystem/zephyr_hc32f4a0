---
id: learning.zephyr-docs.api-file-service-reference.page-47
title: zephyr__dt-bindings__pinctrl__rv32m1-pinctrl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rv32m1-pinctrl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_zephyr\_\_dt-bindings\_\_pinctrl\_\_rv32m1-pinctrl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rv32m1-pinctrl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 47.1\_宏定义（Macros）

<a id="r_adc4ef31269f0084e7551566b199093df"></a>

```c
#define RV32M1_MUX(port, pin, mux)
```

相关声明：[RV32M1_MUX](#adc4ef31269f0084e7551566b199093df)。

指定 `PORTx->PCR` 寄存器的复用器字段（MUX Field）。

## 47.2\_详细说明（Detailed Documentation）

<a id="adc4ef31269f0084e7551566b199093df"></a>

### `RV32M1_MUX`

```c
#define RV32M1_MUX ( port, pin, mux )
```

展开值（Value）：

```c
(((((port) - 'A') & 0xF) << 28) |       \
(((pin) & 0x3F) << 22) |                \
(((mux) & 0x7) << 8))
```

指定 `PORTx->PCR` 寄存器的复用器字段（MUX Field）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `port` | 端口名称（Port Name）：`A`～`E`。 |
| `pin` | 端口引脚编号（Port Pin Number）：0～31。 |
| `mux` | 复用功能编号（Alternate Function Number）：0～7。 |


## 47.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P742_rv32m1-pinctrl.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P046_zephyr__drivers__misc__renesas_rx_external_interrupt__renesas_rx_external_interrupt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P048_zephyr__drivers__sensor__scd4x.h_文件参考.md)
