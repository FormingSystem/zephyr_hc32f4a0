---
id: learning.zephyr-docs.api-file-reference.page-246
title: zephyr__dt-bindings__i2c__npcx-i2c.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/npcx-i2c_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第246章\_zephyr\_\_dt-bindings\_\_i2c\_\_npcx-i2c.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/npcx-i2c_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 246.1\_宏定义（Macros）

<a id="r_a9349b34193640f28fe8c07d192e408ee"></a>

```c
#define NPCX_I2C_CTRL_PORT(ctrl, port)
```

相关声明：[NPCX_I2C_CTRL_PORT](#a9349b34193640f28fe8c07d192e408ee)。

## 246.2\_详细说明（Detailed Documentation）

<a id="a9349b34193640f28fe8c07d192e408ee"></a>

### `NPCX_I2C_CTRL_PORT`

```c
#define NPCX_I2C_CTRL_PORT ( ctrl, port )
```

展开值（Value）：

```c
(((ctrl & 0xf) << 4) | (port & 0xf))
```


## 246.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P589_npcx-i2c.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P245_zephyr__dt-bindings__clock__npcm_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P247_zephyr__dt-bindings__pinctrl__npcx-pinctrl.h_文件参考.md)
