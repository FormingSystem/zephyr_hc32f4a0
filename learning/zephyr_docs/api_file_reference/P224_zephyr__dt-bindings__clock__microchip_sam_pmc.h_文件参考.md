---
id: learning.zephyr-docs.api-file-reference.page-224
title: zephyr__dt-bindings__clock__microchip_sam_pmc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/microchip__sam__pmc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第224章\_zephyr\_\_dt-bindings\_\_clock\_\_microchip\_sam\_pmc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/microchip__sam__pmc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 224.1\_宏定义（Macros）

<a id="r_a2b1fc195c22e06289bfe1955086d42dd"></a>

```c
#define PMC_TYPE_CORE 0
```

相关声明：[PMC_TYPE_CORE](#a2b1fc195c22e06289bfe1955086d42dd)。

<a id="r_a5745534115e0096059c693406055573b"></a>

```c
#define PMC_TYPE_SYSTEM 1
```

相关声明：[PMC_TYPE_SYSTEM](#a5745534115e0096059c693406055573b)。

<a id="r_a60e3c44dd11ea566f718972995374019"></a>

```c
#define PMC_TYPE_PERIPHERAL 2
```

相关声明：[PMC_TYPE_PERIPHERAL](#a60e3c44dd11ea566f718972995374019)。

<a id="r_ab998f9758b4c3e603ca20bfd262f3327"></a>

```c
#define PMC_TYPE_GCK 3
```

相关声明：[PMC_TYPE_GCK](#ab998f9758b4c3e603ca20bfd262f3327)。

<a id="r_a7fc62d1954529184d102cb7585973fb5"></a>

```c
#define PMC_TYPE_PROGRAMMABLE 4
```

相关声明：[PMC_TYPE_PROGRAMMABLE](#a7fc62d1954529184d102cb7585973fb5)。

<a id="r_a854154863c97c71801ff4684a407e237"></a>

```c
#define PMC_SLOW 0
```

相关声明：[PMC_SLOW](#a854154863c97c71801ff4684a407e237)。

<a id="r_a2d6b8cadcedb6522e88264b09da73d7d"></a>

```c
#define PMC_MCK 1
```

相关声明：[PMC_MCK](#a2d6b8cadcedb6522e88264b09da73d7d)。

<a id="r_a5a54df8ddd142b8e6ed67b72d7bab401"></a>

```c
#define PMC_UTMI 2
```

相关声明：[PMC_UTMI](#a5a54df8ddd142b8e6ed67b72d7bab401)。

<a id="r_a072e63108608597768994a00b21d955d"></a>

```c
#define PMC_MAIN 3
```

相关声明：[PMC_MAIN](#a072e63108608597768994a00b21d955d)。

<a id="r_a1f28358ab0151521b3121ff4d57ca700"></a>

```c
#define PMC_CPUPLL (PMC_MAIN + 1)
```

相关声明：[PMC_CPUPLL](#a1f28358ab0151521b3121ff4d57ca700)、[PMC_MAIN](#a072e63108608597768994a00b21d955d)。

<a id="r_a996cc1d45786ee499ccc23355a05db37"></a>

```c
#define PMC_SYSPLL (PMC_MAIN + 2)
```

相关声明：[PMC_SYSPLL](#a996cc1d45786ee499ccc23355a05db37)、[PMC_MAIN](#a072e63108608597768994a00b21d955d)。

<a id="r_ab8a01a73ca6952f39be1ed7a3791feb3"></a>

```c
#define PMC_DDRPLL (PMC_MAIN + 3)
```

相关声明：[PMC_DDRPLL](#ab8a01a73ca6952f39be1ed7a3791feb3)、[PMC_MAIN](#a072e63108608597768994a00b21d955d)。

<a id="r_a441d7b97d246e52e75bf348ac3b90c76"></a>

```c
#define PMC_IMGPLL (PMC_MAIN + 4)
```

相关声明：[PMC_IMGPLL](#a441d7b97d246e52e75bf348ac3b90c76)、[PMC_MAIN](#a072e63108608597768994a00b21d955d)。

<a id="r_aae1ca2d39f81fa9fc9094619ce3b19c4"></a>

```c
#define PMC_BAUDPLL (PMC_MAIN + 5)
```

相关声明：[PMC_BAUDPLL](#aae1ca2d39f81fa9fc9094619ce3b19c4)、[PMC_MAIN](#a072e63108608597768994a00b21d955d)。

<a id="r_af716bb9061d8d6a5a96ade2c0102f4c0"></a>

```c
#define PMC_AUDIOPMCPLL (PMC_MAIN + 6)
```

相关声明：[PMC_AUDIOPMCPLL](#af716bb9061d8d6a5a96ade2c0102f4c0)、[PMC_MAIN](#a072e63108608597768994a00b21d955d)。

<a id="r_a2374e2a9b2baf97196cb9900ab41f2b1"></a>

```c
#define PMC_AUDIOIOPLL (PMC_MAIN + 7)
```

相关声明：[PMC_AUDIOIOPLL](#a2374e2a9b2baf97196cb9900ab41f2b1)、[PMC_MAIN](#a072e63108608597768994a00b21d955d)。

<a id="r_a2707b5189d0c0a383e8765aa4dc0c702"></a>

```c
#define PMC_ETHPLL (PMC_MAIN + 8)
```

相关声明：[PMC_ETHPLL](#a2707b5189d0c0a383e8765aa4dc0c702)、[PMC_MAIN](#a072e63108608597768994a00b21d955d)。

<a id="r_a79ea6d33c03bc659e505516f10dd4909"></a>

```c
#define PMC_CPU (PMC_MAIN + 9)
```

相关声明：[PMC_CPU](#a79ea6d33c03bc659e505516f10dd4909)、[PMC_MAIN](#a072e63108608597768994a00b21d955d)。

<a id="r_a373a027bd6c4c22ba1bb333109c4b4b5"></a>

```c
#define PMC_MCK1 (PMC_MAIN + 10)
```

相关声明：[PMC_MCK1](#a373a027bd6c4c22ba1bb333109c4b4b5)、[PMC_MAIN](#a072e63108608597768994a00b21d955d)。

<a id="r_acf4ff24d07135ac8ba9095f4b0e8202f"></a>

```c
#define UTMI1 0
```

相关声明：[UTMI1](#acf4ff24d07135ac8ba9095f4b0e8202f)。

<a id="r_a536bbd6e8cf19611a64b62a6173bebae"></a>

```c
#define UTMI2 1
```

相关声明：[UTMI2](#a536bbd6e8cf19611a64b62a6173bebae)。

<a id="r_ab950647ecce7b6ed9a94770434a9504c"></a>

```c
#define UTMI3 2
```

相关声明：[UTMI3](#ab950647ecce7b6ed9a94770434a9504c)。

<a id="r_af7ababade336761d419000117f26729b"></a>

```c
#define PMC_LVDSPLL (PMC_MAIN + 12)
```

相关声明：[PMC_LVDSPLL](#af7ababade336761d419000117f26729b)、[PMC_MAIN](#a072e63108608597768994a00b21d955d)。

<a id="r_a26c4f89876d53e70aaa08503a1e376ca"></a>

```c
#define PMC_MCK3 (PMC_MAIN + 20)
```

相关声明：[PMC_MCK3](#a26c4f89876d53e70aaa08503a1e376ca)、[PMC_MAIN](#a072e63108608597768994a00b21d955d)。

<a id="r_af08ab4f17eff3aa6f62de4d7addbdf68"></a>

```c
#define PMC_MCK5 (PMC_MAIN + 21)
```

相关声明：[PMC_MCK5](#af08ab4f17eff3aa6f62de4d7addbdf68)、[PMC_MAIN](#a072e63108608597768994a00b21d955d)。

## 224.2\_详细说明（Detailed Documentation）

<a id="a2374e2a9b2baf97196cb9900ab41f2b1"></a>

### `PMC_AUDIOIOPLL`

```c
#define PMC_AUDIOIOPLL (PMC_MAIN + 7)
```

<a id="af716bb9061d8d6a5a96ade2c0102f4c0"></a>

### `PMC_AUDIOPMCPLL`

```c
#define PMC_AUDIOPMCPLL (PMC_MAIN + 6)
```

<a id="aae1ca2d39f81fa9fc9094619ce3b19c4"></a>

### `PMC_BAUDPLL`

```c
#define PMC_BAUDPLL (PMC_MAIN + 5)
```

<a id="a79ea6d33c03bc659e505516f10dd4909"></a>

### `PMC_CPU`

```c
#define PMC_CPU (PMC_MAIN + 9)
```

<a id="a1f28358ab0151521b3121ff4d57ca700"></a>

### `PMC_CPUPLL`

```c
#define PMC_CPUPLL (PMC_MAIN + 1)
```

<a id="ab8a01a73ca6952f39be1ed7a3791feb3"></a>

### `PMC_DDRPLL`

```c
#define PMC_DDRPLL (PMC_MAIN + 3)
```

<a id="a2707b5189d0c0a383e8765aa4dc0c702"></a>

### `PMC_ETHPLL`

```c
#define PMC_ETHPLL (PMC_MAIN + 8)
```

<a id="a441d7b97d246e52e75bf348ac3b90c76"></a>

### `PMC_IMGPLL`

```c
#define PMC_IMGPLL (PMC_MAIN + 4)
```

<a id="af7ababade336761d419000117f26729b"></a>

### `PMC_LVDSPLL`

```c
#define PMC_LVDSPLL (PMC_MAIN + 12)
```

<a id="a072e63108608597768994a00b21d955d"></a>

### `PMC_MAIN`

```c
#define PMC_MAIN 3
```

<a id="a2d6b8cadcedb6522e88264b09da73d7d"></a>

### `PMC_MCK`

```c
#define PMC_MCK 1
```

<a id="a373a027bd6c4c22ba1bb333109c4b4b5"></a>

### `PMC_MCK1`

```c
#define PMC_MCK1 (PMC_MAIN + 10)
```

<a id="a26c4f89876d53e70aaa08503a1e376ca"></a>

### `PMC_MCK3`

```c
#define PMC_MCK3 (PMC_MAIN + 20)
```

<a id="af08ab4f17eff3aa6f62de4d7addbdf68"></a>

### `PMC_MCK5`

```c
#define PMC_MCK5 (PMC_MAIN + 21)
```

<a id="a854154863c97c71801ff4684a407e237"></a>

### `PMC_SLOW`

```c
#define PMC_SLOW 0
```

<a id="a996cc1d45786ee499ccc23355a05db37"></a>

### `PMC_SYSPLL`

```c
#define PMC_SYSPLL (PMC_MAIN + 2)
```

<a id="a2b1fc195c22e06289bfe1955086d42dd"></a>

### `PMC_TYPE_CORE`

```c
#define PMC_TYPE_CORE 0
```

<a id="ab998f9758b4c3e603ca20bfd262f3327"></a>

### `PMC_TYPE_GCK`

```c
#define PMC_TYPE_GCK 3
```

<a id="a60e3c44dd11ea566f718972995374019"></a>

### `PMC_TYPE_PERIPHERAL`

```c
#define PMC_TYPE_PERIPHERAL 2
```

<a id="a7fc62d1954529184d102cb7585973fb5"></a>

### `PMC_TYPE_PROGRAMMABLE`

```c
#define PMC_TYPE_PROGRAMMABLE 4
```

<a id="a5745534115e0096059c693406055573b"></a>

### `PMC_TYPE_SYSTEM`

```c
#define PMC_TYPE_SYSTEM 1
```

<a id="a5a54df8ddd142b8e6ed67b72d7bab401"></a>

### `PMC_UTMI`

```c
#define PMC_UTMI 2
```

<a id="acf4ff24d07135ac8ba9095f4b0e8202f"></a>

### `UTMI1`

```c
#define UTMI1 0
```

<a id="a536bbd6e8cf19611a64b62a6173bebae"></a>

### `UTMI2`

```c
#define UTMI2 1
```

<a id="ab950647ecce7b6ed9a94770434a9504c"></a>

### `UTMI3`

```c
#define UTMI3 2
```


## 224.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P056_microchip_sam_pmc.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P223_zephyr__dt-bindings__interrupt-controller__microchip-smartfusion2-irq.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P225_zephyr__drivers__mipi_dsi__mipi_dsi_mcux_2l.h_文件参考.md)
