---
id: learning.zephyr-docs.api-file-runtime-reference.page-36
title: zephyr__drivers__reset__mchp_rstc_g1.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mchp__rstc__g1_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第36章\_zephyr\_\_drivers\_\_reset\_\_mchp\_rstc\_g1.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mchp__rstc__g1_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Microchip RSTC G1复位控制器（Reset Controller）的头文件。

查看此文件的源码。

<a id="details"></a>

Microchip RSTC G1 复位控制器头文件（Reset Controller Header）。本头文件包含 Microchip RSTC G1 的宏定义（Macro Definitions）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 36.1\_宏定义（Macros）

<a id="r_a8c71773e6386126b1a0f36ec8feb2e9b"></a>

```c
#define RSTC_UNSUPPORTED_RCAUSE 0U
```

相关声明：[RSTC_UNSUPPORTED_RCAUSE](#a8c71773e6386126b1a0f36ec8feb2e9b)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 36.2\_枚举（Enumerations）

<a id="r_a6af694fadfdfbe42200c31988c69ad43"></a>

```c
enum rstc_g1_rcause { RSTC_G1_RCAUSE_POR = 0 , RSTC_G1_RCAUSE_BOD12 = 1 , RSTC_G1_RCAUSE_BOD33 = 2 , RSTC_G1_RCAUSE_NVM = 3 , RSTC_G1_RCAUSE_EXT = 4 , RSTC_G1_RCAUSE_WDT = 5 , RSTC_G1_RCAUSE_SYST = 6 , RSTC_G1_RCAUSE_BACKUP = 7 }
```

相关声明：[rstc_g1_rcause](#a6af694fadfdfbe42200c31988c69ad43)、[RSTC_G1_RCAUSE_POR](#a6af694fadfdfbe42200c31988c69ad43a1a7e6a2780ee3126cde8a34cd1169fef)、[RSTC_G1_RCAUSE_BOD12](#a6af694fadfdfbe42200c31988c69ad43a7ab5a6787ea160f36c80e8b13f9dbb3a)、[RSTC_G1_RCAUSE_BOD33](#a6af694fadfdfbe42200c31988c69ad43a405a015f25eb5b6ff23fd98cf155ccfa)、[RSTC_G1_RCAUSE_NVM](#a6af694fadfdfbe42200c31988c69ad43a9168e6a7b1e10b08fd456a0444de0310)、[RSTC_G1_RCAUSE_EXT](#a6af694fadfdfbe42200c31988c69ad43a2a59fe99e59d04641461db953476ac31)、[RSTC_G1_RCAUSE_WDT](#a6af694fadfdfbe42200c31988c69ad43aeaee4fd0c513e69f21cbb4ba7cde26d7)、[RSTC_G1_RCAUSE_SYST](#a6af694fadfdfbe42200c31988c69ad43a5bf10ab2c8d2c18b238638ebe45e66a6)、[RSTC_G1_RCAUSE_BACKUP](#a6af694fadfdfbe42200c31988c69ad43ae2dd00e91b977026125424a6a3cbe739)。

Microchip RSTC G1 的复位原因标志（Reset Cause Flags）。

## 36.3\_详细说明（Detailed Documentation）

<a id="a8c71773e6386126b1a0f36ec8feb2e9b"></a>

### `RSTC_UNSUPPORTED_RCAUSE`

```c
#define RSTC_UNSUPPORTED_RCAUSE 0U
```

<a id="a6af694fadfdfbe42200c31988c69ad43"></a>

### `rstc_g1_rcause`

```c
enum rstc_g1_rcause
```

Microchip RSTC G1 的复位原因标志（Reset Cause Flags）。

本枚举（Enumeration）定义 Microchip RSTC G1 复位控制器中 `RSTC_RCAUSE` 寄存器所指示的各种复位原因（Reset Causes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `RSTC_G1_RCAUSE_POR` |  |
| `RSTC_G1_RCAUSE_BOD12` |  |
| `RSTC_G1_RCAUSE_BOD33` |  |
| `RSTC_G1_RCAUSE_NVM` |  |
| `RSTC_G1_RCAUSE_EXT` |  |
| `RSTC_G1_RCAUSE_WDT` |  |
| `RSTC_G1_RCAUSE_SYST` |  |
| `RSTC_G1_RCAUSE_BACKUP` |  |


## 36.4\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/mchp__rstc__g1_8h_source.html)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a6af694fadfdfbe42200c31988c69ad43a1a7e6a2780ee3126cde8a34cd1169fef"></a>
<a id="a6af694fadfdfbe42200c31988c69ad43a7ab5a6787ea160f36c80e8b13f9dbb3a"></a>
<a id="a6af694fadfdfbe42200c31988c69ad43a405a015f25eb5b6ff23fd98cf155ccfa"></a>
<a id="a6af694fadfdfbe42200c31988c69ad43a9168e6a7b1e10b08fd456a0444de0310"></a>
<a id="a6af694fadfdfbe42200c31988c69ad43a2a59fe99e59d04641461db953476ac31"></a>
<a id="a6af694fadfdfbe42200c31988c69ad43aeaee4fd0c513e69f21cbb4ba7cde26d7"></a>
<a id="a6af694fadfdfbe42200c31988c69ad43a5bf10ab2c8d2c18b238638ebe45e66a6"></a>
<a id="a6af694fadfdfbe42200c31988c69ad43ae2dd00e91b977026125424a6a3cbe739"></a>

---

[上一章](P035_zephyr__drivers__flash__mchp_nvmctrl_g3.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P037_zephyr__dt-bindings__gpio__microchip-port-g1-gpio.h_文件参考.md)
