---
id: learning.zephyr-docs.api-file-reference.page-172
title: zephyr__drivers__interrupt_controller__ioapic.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ioapic_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第172章\_zephyr\_\_drivers\_\_interrupt\_controller\_\_ioapic.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ioapic_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 172.1\_宏定义（Macros）

<a id="r_afe15b2cc2000b86362e9fb0026ec4f32"></a>

```c
#define IOAPIC_INT_MASK 0x00010000
```

相关声明：[IOAPIC_INT_MASK](#afe15b2cc2000b86362e9fb0026ec4f32)。

<a id="r_ac66c78294836c1327cbbf6bd5111282a"></a>

```c
#define IOAPIC_TRIGGER_MASK 0x00008000
```

相关声明：[IOAPIC_TRIGGER_MASK](#ac66c78294836c1327cbbf6bd5111282a)。

<a id="r_afee8dca23363d2f9b785a21f6b5c4080"></a>

```c
#define IOAPIC_LEVEL 0x00008000
```

相关声明：[IOAPIC_LEVEL](#afee8dca23363d2f9b785a21f6b5c4080)。

<a id="r_a1d4cfd6f7d4aba0bc773e4d53333bb1d"></a>

```c
#define IOAPIC_EDGE 0x00000000
```

相关声明：[IOAPIC_EDGE](#a1d4cfd6f7d4aba0bc773e4d53333bb1d)。

<a id="r_a850d24fefdc5a1b0f92922a504eb43b5"></a>

```c
#define IOAPIC_REMOTE 0x00004000
```

相关声明：[IOAPIC_REMOTE](#a850d24fefdc5a1b0f92922a504eb43b5)。

<a id="r_a3d009fe11441cfd8ad68f91d764f447e"></a>

```c
#define IOAPIC_POLARITY_MASK 0x00002000
```

相关声明：[IOAPIC_POLARITY_MASK](#a3d009fe11441cfd8ad68f91d764f447e)。

<a id="r_a23ec31db6b36b64ad0d04c3caf2815f2"></a>

```c
#define IOAPIC_LOW 0x00002000
```

相关声明：[IOAPIC_LOW](#a23ec31db6b36b64ad0d04c3caf2815f2)。

<a id="r_a1677a4eb3aab3bea022e9ea2bf547888"></a>

```c
#define IOAPIC_HIGH 0x00000000
```

相关声明：[IOAPIC_HIGH](#a1677a4eb3aab3bea022e9ea2bf547888)。

<a id="r_af9cdfb74e72ef22f3c51f7b9a8b3afe9"></a>

```c
#define IOAPIC_LOGICAL 0x00000800
```

相关声明：[IOAPIC_LOGICAL](#af9cdfb74e72ef22f3c51f7b9a8b3afe9)。

<a id="r_aa4ef248efabc134ecad5f00fa34fa456"></a>

```c
#define IOAPIC_PHYSICAL 0x00000000
```

相关声明：[IOAPIC_PHYSICAL](#aa4ef248efabc134ecad5f00fa34fa456)。

<a id="r_a1d1756d4b243d2235d58ffa2caf4e5fc"></a>

```c
#define IOAPIC_DELIVERY_MODE_MASK 0x00000700
```

相关声明：[IOAPIC_DELIVERY_MODE_MASK](#a1d1756d4b243d2235d58ffa2caf4e5fc)。

<a id="r_af84ed8737d1822ded039bb975b8f5bc9"></a>

```c
#define IOAPIC_FIXED 0x00000000
```

相关声明：[IOAPIC_FIXED](#af84ed8737d1822ded039bb975b8f5bc9)。

<a id="r_add788ae14ffab1b56a831c2a39d2a617"></a>

```c
#define IOAPIC_LOWEST 0x00000100
```

相关声明：[IOAPIC_LOWEST](#add788ae14ffab1b56a831c2a39d2a617)。

<a id="r_aa01949d30064c45959fdfefcedd916f1"></a>

```c
#define IOAPIC_SMI 0x00000200
```

相关声明：[IOAPIC_SMI](#aa01949d30064c45959fdfefcedd916f1)。

<a id="r_a3e2f1930e2f92cff455b98b76c6c4397"></a>

```c
#define IOAPIC_NMI 0x00000400
```

相关声明：[IOAPIC_NMI](#a3e2f1930e2f92cff455b98b76c6c4397)。

<a id="r_a16099bc753e03fdf31f6aa35f01cf2fa"></a>

```c
#define IOAPIC_INIT 0x00000500
```

相关声明：[IOAPIC_INIT](#a16099bc753e03fdf31f6aa35f01cf2fa)。

<a id="r_aeff81f0a6186d2b188c7109baa670c52"></a>

```c
#define IOAPIC_EXTINT 0x00000700
```

相关声明：[IOAPIC_EXTINT](#aeff81f0a6186d2b188c7109baa670c52)。

## 172.2\_详细说明（Detailed Documentation）

<a id="a1d1756d4b243d2235d58ffa2caf4e5fc"></a>

### `IOAPIC_DELIVERY_MODE_MASK`

```c
#define IOAPIC_DELIVERY_MODE_MASK 0x00000700
```

<a id="a1d4cfd6f7d4aba0bc773e4d53333bb1d"></a>

### `IOAPIC_EDGE`

```c
#define IOAPIC_EDGE 0x00000000
```

<a id="aeff81f0a6186d2b188c7109baa670c52"></a>

### `IOAPIC_EXTINT`

```c
#define IOAPIC_EXTINT 0x00000700
```

<a id="af84ed8737d1822ded039bb975b8f5bc9"></a>

### `IOAPIC_FIXED`

```c
#define IOAPIC_FIXED 0x00000000
```

<a id="a1677a4eb3aab3bea022e9ea2bf547888"></a>

### `IOAPIC_HIGH`

```c
#define IOAPIC_HIGH 0x00000000
```

<a id="a16099bc753e03fdf31f6aa35f01cf2fa"></a>

### `IOAPIC_INIT`

```c
#define IOAPIC_INIT 0x00000500
```

<a id="afe15b2cc2000b86362e9fb0026ec4f32"></a>

### `IOAPIC_INT_MASK`

```c
#define IOAPIC_INT_MASK 0x00010000
```

<a id="afee8dca23363d2f9b785a21f6b5c4080"></a>

### `IOAPIC_LEVEL`

```c
#define IOAPIC_LEVEL 0x00008000
```

<a id="af9cdfb74e72ef22f3c51f7b9a8b3afe9"></a>

### `IOAPIC_LOGICAL`

```c
#define IOAPIC_LOGICAL 0x00000800
```

<a id="a23ec31db6b36b64ad0d04c3caf2815f2"></a>

### `IOAPIC_LOW`

```c
#define IOAPIC_LOW 0x00002000
```

<a id="add788ae14ffab1b56a831c2a39d2a617"></a>

### `IOAPIC_LOWEST`

```c
#define IOAPIC_LOWEST 0x00000100
```

<a id="a3e2f1930e2f92cff455b98b76c6c4397"></a>

### `IOAPIC_NMI`

```c
#define IOAPIC_NMI 0x00000400
```

<a id="aa4ef248efabc134ecad5f00fa34fa456"></a>

### `IOAPIC_PHYSICAL`

```c
#define IOAPIC_PHYSICAL 0x00000000
```

<a id="a3d009fe11441cfd8ad68f91d764f447e"></a>

### `IOAPIC_POLARITY_MASK`

```c
#define IOAPIC_POLARITY_MASK 0x00002000
```

<a id="a850d24fefdc5a1b0f92922a504eb43b5"></a>

### `IOAPIC_REMOTE`

```c
#define IOAPIC_REMOTE 0x00004000
```

<a id="aa01949d30064c45959fdfefcedd916f1"></a>

### `IOAPIC_SMI`

```c
#define IOAPIC_SMI 0x00000200
```

<a id="ac66c78294836c1327cbbf6bd5111282a"></a>

### `IOAPIC_TRIGGER_MASK`

```c
#define IOAPIC_TRIGGER_MASK 0x00008000
```


## 172.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P042_ioapic.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P171_____w__zephyr__zephyr__lib__libc__minimal__include__inttypes.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P173_zephyr__irq.h_文件参考.md)
