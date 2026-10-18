---
id: learning.zephyr-docs.api-file-system-device-reference.page-14
title: zephyr__dt-bindings__clock__ifx_clock_source_psc3xx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__psc3xx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_zephyr\_\_dt-bindings\_\_clock\_\_ifx\_clock\_source\_psc3xx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ifx__clock__source__psc3xx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 14.1\_宏定义（Macros）

<a id="r_abe36899d8aba61aff9bf5540e204ebda"></a>

```c
#define IFX_CAT1_CLKPATH_IN_IMO 0
```

相关声明：[IFX_CAT1_CLKPATH_IN_IMO](#abe36899d8aba61aff9bf5540e204ebda)。

选择 IMO 作为路径多路选择器（path mux）的输出。

<a id="r_abde39b7df7df77a803d42ce22735e765"></a>

```c
#define IFX_CAT1_CLKPATH_IN_EXT 1
```

相关声明：[IFX_CAT1_CLKPATH_IN_EXT](#abde39b7df7df77a803d42ce22735e765)。

选择 EXT 作为路径多路选择器（path mux）的输出。

<a id="r_aef7e5c72b63d5491c13d80ae6e479c4b"></a>

```c
#define IFX_CAT1_CLKPATH_IN_ECO 2
```

相关声明：[IFX_CAT1_CLKPATH_IN_ECO](#aef7e5c72b63d5491c13d80ae6e479c4b)。

选择 ECO 作为路径多路选择器（path mux）的输出。

<a id="r_aebc9ca3ccaebdac864c435bf355eb527"></a>

```c
#define IFX_CAT1_CLKPATH_IN_ALTHF 3
```

相关声明：[IFX_CAT1_CLKPATH_IN_ALTHF](#aebc9ca3ccaebdac864c435bf355eb527)。

选择 ALTHF 作为路径多路选择器（path mux）的输出。

<a id="r_a929b692a2dbe28708e96960329a2e914"></a>

```c
#define IFX_CAT1_CLKPATH_IN_DSIMUX 4
```

相关声明：[IFX_CAT1_CLKPATH_IN_DSIMUX](#a929b692a2dbe28708e96960329a2e914)。

<a id="r_a9eecc86ae5ca7beefe9db98bc3a48bab"></a>

```c
#define IFX_CAT1_CLKPATH_IN_LPECO 5
```

相关声明：[IFX_CAT1_CLKPATH_IN_LPECO](#a9eecc86ae5ca7beefe9db98bc3a48bab)。

选择 LPECO 作为路径多路选择器（path mux）的输出。

<a id="r_abab79c73607eb511df27d6a8084ed3a4"></a>

```c
#define IFX_CAT1_CLKPATH_IN_IHO 6
```

相关声明：[IFX_CAT1_CLKPATH_IN_IHO](#abab79c73607eb511df27d6a8084ed3a4)。

选择 IHO 作为路径多路选择器（path mux）的输出。

<a id="r_ad714f40b9783754cf81c065f45a74a4b"></a>

```c
#define IFX_CAT1_CLKPATH_IN_DSI 0x100
```

相关声明：[IFX_CAT1_CLKPATH_IN_DSI](#ad714f40b9783754cf81c065f45a74a4b)。

选择 ILO（16）作为 DSI 多路选择器和路径多路选择器的输出。

<a id="r_a2b639675968e2a8d98a91450effd7e87"></a>

```c
#define IFX_CAT1_CLKPATH_IN_ILO 0x110
```

相关声明：[IFX_CAT1_CLKPATH_IN_ILO](#a2b639675968e2a8d98a91450effd7e87)。

选择 WCO（17）作为 DSI 多路选择器和路径多路选择器的输出。

<a id="r_a9771da452225a9a70d250b5c35e0fa9b"></a>

```c
#define IFX_CAT1_CLKPATH_IN_WCO 0x111
```

相关声明：[IFX_CAT1_CLKPATH_IN_WCO](#a9771da452225a9a70d250b5c35e0fa9b)。

选择 ALTLF（18）作为 DSI 多路选择器和路径多路选择器的输出。

<a id="r_ad2bd88f46b58cf062c4f05f96cfee4f9"></a>

```c
#define IFX_CAT1_CLKPATH_IN_ALTLF 0x112
```

相关声明：[IFX_CAT1_CLKPATH_IN_ALTLF](#ad2bd88f46b58cf062c4f05f96cfee4f9)。

选择 PILO（19）作为 DSI 多路选择器和路径多路选择器的输出。

<a id="r_abea78ff812f0b1d3772d527e04bdab75"></a>

```c
#define IFX_CAT1_CLKPATH_IN_PILO 0x113
```

相关声明：[IFX_CAT1_CLKPATH_IN_PILO](#abea78ff812f0b1d3772d527e04bdab75)。

选择 ILO1（20）作为 DSI 多路选择器和路径多路选择器的输出。

<a id="r_ac5bad5a43c1ed489ec83e96673f364e1"></a>

```c
#define IFX_CAT1_CLKPATH_IN_ILO1 0x114
```

相关声明：[IFX_CAT1_CLKPATH_IN_ILO1](#ac5bad5a43c1ed489ec83e96673f364e1)。

## 14.2\_详细说明（Detailed Documentation）

<a id="aebc9ca3ccaebdac864c435bf355eb527"></a>

### `IFX_CAT1_CLKPATH_IN_ALTHF`

```c
#define IFX_CAT1_CLKPATH_IN_ALTHF 3
```

选择 ALTHF 作为路径多路选择器（path mux）的输出。

<a id="ad2bd88f46b58cf062c4f05f96cfee4f9"></a>

### `IFX_CAT1_CLKPATH_IN_ALTLF`

```c
#define IFX_CAT1_CLKPATH_IN_ALTLF 0x112
```

选择 PILO（19）作为 DSI 多路选择器和路径多路选择器的输出。

请确保所用设备提供 PILO 时钟源（clock sources）。

<a id="ad714f40b9783754cf81c065f45a74a4b"></a>

### `IFX_CAT1_CLKPATH_IN_DSI`

```c
#define IFX_CAT1_CLKPATH_IN_DSI 0x100
```

选择 ILO（16）作为 DSI 多路选择器和路径多路选择器的输出。

<a id="a929b692a2dbe28708e96960329a2e914"></a>

### `IFX_CAT1_CLKPATH_IN_DSIMUX`

```c
#define IFX_CAT1_CLKPATH_IN_DSIMUX 4
```

<a id="aef7e5c72b63d5491c13d80ae6e479c4b"></a>

### `IFX_CAT1_CLKPATH_IN_ECO`

```c
#define IFX_CAT1_CLKPATH_IN_ECO 2
```

选择 ECO 作为路径多路选择器（path mux）的输出。

<a id="abde39b7df7df77a803d42ce22735e765"></a>

### `IFX_CAT1_CLKPATH_IN_EXT`

```c
#define IFX_CAT1_CLKPATH_IN_EXT 1
```

选择 EXT 作为路径多路选择器（path mux）的输出。

<a id="abab79c73607eb511df27d6a8084ed3a4"></a>

### `IFX_CAT1_CLKPATH_IN_IHO`

```c
#define IFX_CAT1_CLKPATH_IN_IHO 6
```

选择 IHO 作为路径多路选择器（path mux）的输出。

<a id="a2b639675968e2a8d98a91450effd7e87"></a>

### `IFX_CAT1_CLKPATH_IN_ILO`

```c
#define IFX_CAT1_CLKPATH_IN_ILO 0x110
```

选择 WCO（17）作为 DSI 多路选择器和路径多路选择器的输出。

<a id="ac5bad5a43c1ed489ec83e96673f364e1"></a>

### `IFX_CAT1_CLKPATH_IN_ILO1`

```c
#define IFX_CAT1_CLKPATH_IN_ILO1 0x114
```

<a id="abe36899d8aba61aff9bf5540e204ebda"></a>

### `IFX_CAT1_CLKPATH_IN_IMO`

```c
#define IFX_CAT1_CLKPATH_IN_IMO 0
```

选择 IMO 作为路径多路选择器（path mux）的输出。

<a id="a9eecc86ae5ca7beefe9db98bc3a48bab"></a>

### `IFX_CAT1_CLKPATH_IN_LPECO`

```c
#define IFX_CAT1_CLKPATH_IN_LPECO 5
```

选择 LPECO 作为路径多路选择器（path mux）的输出。

<a id="abea78ff812f0b1d3772d527e04bdab75"></a>

### `IFX_CAT1_CLKPATH_IN_PILO`

```c
#define IFX_CAT1_CLKPATH_IN_PILO 0x113
```

选择 ILO1（20）作为 DSI 多路选择器和路径多路选择器的输出。

<a id="a9771da452225a9a70d250b5c35e0fa9b"></a>

### `IFX_CAT1_CLKPATH_IN_WCO`

```c
#define IFX_CAT1_CLKPATH_IN_WCO 0x111
```

选择 ALTLF（18）作为 DSI 多路选择器和路径多路选择器的输出。

请确保所用设备提供 ALTLF 时钟源（clock sources）。


## 14.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P032_ifx_clock_source_psc3xx.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P013_zephyr__drivers__i3c__ibi.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P015_zephyr__mgmt__mcumgr__grp__img_mgmt__img_mgmt_client.h_文件参考.md)
