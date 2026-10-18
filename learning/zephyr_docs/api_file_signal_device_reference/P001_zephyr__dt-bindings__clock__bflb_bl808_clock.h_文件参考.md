---
id: learning.zephyr-docs.api-file-signal-device-reference.page-1
title: zephyr__dt-bindings__clock__bflb_bl808_clock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl808__clock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_dt-bindings\_\_clock\_\_bflb\_bl808\_clock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/bflb__bl808__clock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于设备树绑定（Device Tree Bindings）的BL808时钟ID和锁相环（PLL）配置常量。

<a id="details"></a>

```c
#include "bflb_clock_common.h"
```

查看此文件的源码。

用于设备树绑定（Device Tree Bindings）的BL808时钟ID和锁相环（PLL）配置常量。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="r_acd2b6c7f3812560d616c43312e747c70"></a>

```c
#define BL808_CLKID_CLK_ROOT BFLB_CLKID_CLK_ROOT
```

相关声明：[BL808_CLKID_CLK_ROOT](#acd2b6c7f3812560d616c43312e747c70)、[BFLB_CLKID_CLK_ROOT](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#af2d6e2a7c386b50358a9cf50fc8808b3)。

根时钟（Root Clock）。

<a id="r_a99b553bfe231791c2c7c40d8a88329ad"></a>

```c
#define BL808_CLKID_CLK_RC32M BFLB_CLKID_CLK_RC32M
```

相关声明：[BL808_CLKID_CLK_RC32M](#a99b553bfe231791c2c7c40d8a88329ad)、[BFLB_CLKID_CLK_RC32M](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a48bf5d6a4379c03c7817503d7fe66c8b)。

32 MHz RC 振荡器时钟（RC Oscillator Clock）。

<a id="r_af6a43433db32add4813c688ab1a4adc5"></a>

```c
#define BL808_CLKID_CLK_CRYSTAL BFLB_CLKID_CLK_CRYSTAL
```

相关声明：[BL808_CLKID_CLK_CRYSTAL](#af6a43433db32add4813c688ab1a4adc5)、[BFLB_CLKID_CLK_CRYSTAL](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a059c42552c94b942f53c644207776326)。

晶体时钟（Crystal Clock）。

<a id="r_ae5146bbdf74be5084e2c585f22857433"></a>

```c
#define BL808_CLKID_CLK_BCLK BFLB_CLKID_CLK_BCLK
```

相关声明：[BL808_CLKID_CLK_BCLK](#ae5146bbdf74be5084e2c585f22857433)、[BFLB_CLKID_CLK_BCLK](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a81f8f15faf5025212dbe96417515c358)。

总线时钟（Bus Clock）。

<a id="r_a7fee3bb46198223c41681c86f8574a28"></a>

```c
#define BL808_CLKID_CLK_F32K BFLB_CLKID_CLK_F32K
```

相关声明：[BL808_CLKID_CLK_F32K](#a7fee3bb46198223c41681c86f8574a28)、[BFLB_CLKID_CLK_F32K](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a5b8eca0197f839af7776f5d02c6eab13)。

F32K 时钟（Clock）。

<a id="r_a8be3db0e3d1933894c2917fb176a08f7"></a>

```c
#define BL808_CLKID_CLK_XTAL32K BFLB_CLKID_CLK_XTAL32K
```

相关声明：[BL808_CLKID_CLK_XTAL32K](#a8be3db0e3d1933894c2917fb176a08f7)、[BFLB_CLKID_CLK_XTAL32K](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a14b75b51b81786bb7ae26070e5e41e22)。

XTAL32K 时钟（Clock）。

<a id="r_af76d527c250ec896ed0d768a1a11616a"></a>

```c
#define BL808_CLKID_CLK_RC32K BFLB_CLKID_CLK_RC32K
```

相关声明：[BL808_CLKID_CLK_RC32K](#af76d527c250ec896ed0d768a1a11616a)、[BFLB_CLKID_CLK_RC32K](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#ad2b0e7bd97598e50d10ce66d5b52a360)。

RC32K 时钟（Clock）。

<a id="r_a2aa6a56fd934cc2657b4aeda89fc938f"></a>

```c
#define BL808_CLKID_CLK_WIFIPLL (BFLB_CLKID_CLK_PRIVATE + 0)
```

相关声明：[BL808_CLKID_CLK_WIFIPLL](#a2aa6a56fd934cc2657b4aeda89fc938f)、[BFLB_CLKID_CLK_PRIVATE](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#acc4f8e38984a2ec63e470b919b6d8aef)。

Wi-Fi 锁相环时钟（WiFi PLL Clock）。

<a id="r_a4698a9cec975c91e8eb835d905177686"></a>

```c
#define BL808_CLKID_CLK_AUPLL (BFLB_CLKID_CLK_PRIVATE + 1)
```

相关声明：[BL808_CLKID_CLK_AUPLL](#a4698a9cec975c91e8eb835d905177686)、[BFLB_CLKID_CLK_PRIVATE](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#acc4f8e38984a2ec63e470b919b6d8aef)。

音频锁相环时钟（Audio PLL Clock）。

<a id="r_aa9c012eb82f134cc040781f9f9eb37d2"></a>

```c
#define BL808_CLKID_CLK_CPUPLL (BFLB_CLKID_CLK_PRIVATE + 2)
```

相关声明：[BL808_CLKID_CLK_CPUPLL](#aa9c012eb82f134cc040781f9f9eb37d2)、[BFLB_CLKID_CLK_PRIVATE](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#acc4f8e38984a2ec63e470b919b6d8aef)。

CPU 锁相环时钟（CPU PLL Clock）。

<a id="r_a14ebe26a8a7978110db3b60b02c14cf5"></a>

```c
#define BL808_CLKID_CLK_160M (BFLB_CLKID_CLK_PRIVATE + 3)
```

相关声明：[BL808_CLKID_CLK_160M](#a14ebe26a8a7978110db3b60b02c14cf5)、[BFLB_CLKID_CLK_PRIVATE](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#acc4f8e38984a2ec63e470b919b6d8aef)。

160 MHz 时钟（Clock）。

<a id="r_ac6a515aeb3dc9b2a101c8ba3935fa029"></a>

```c
#define BL808_CLKID_CLK_UHSPLL (BFLB_CLKID_CLK_PRIVATE + 4)
```

相关声明：[BL808_CLKID_CLK_UHSPLL](#ac6a515aeb3dc9b2a101c8ba3935fa029)、[BFLB_CLKID_CLK_PRIVATE](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#acc4f8e38984a2ec63e470b919b6d8aef)。

UHS 锁相环时钟（PLL Clock），为 UHS PSRAM 物理层（PHY）专用 PLL。

<a id="r_a34149d4ba4e5d7c84aaacca3d67cb1f8"></a>

```c
#define BL808_CPUPLL_ID_DIV1 0
```

相关声明：[BL808_CPUPLL_ID_DIV1](#a34149d4ba4e5d7c84aaacca3d67cb1f8)。

CPU PLL 输出选择（Output Select）：1 分频。

<a id="r_a09e845c88455d650e087d54e5e0104df"></a>

```c
#define BL808_AUPLL_ID_DIV1 1
```

相关声明：[BL808_AUPLL_ID_DIV1](#a09e845c88455d650e087d54e5e0104df)。

AUPLL 输出选择（Output Select）：1 分频。

<a id="r_a4ad1ebd0d4c445b74d18f1409beeb8fe"></a>

```c
#define BL808_WIFIPLL_ID_DIV3_4 2
```

相关声明：[BL808_WIFIPLL_ID_DIV3_4](#a4ad1ebd0d4c445b74d18f1409beeb8fe)。

WiFi PLL 输出选择（Output Select）：最高频率（Top Frequency）的 `3/4`。

<a id="r_a7bf45d0ed63f9db31d1c61a9677b378c"></a>

```c
#define BL808_WIFIPLL_ID_DIV1 3
```

相关声明：[BL808_WIFIPLL_ID_DIV1](#a7bf45d0ed63f9db31d1c61a9677b378c)。

WiFi PLL 输出选择（Output Select）：最高频率（Top Frequency）。

<a id="r_acb181224dc5658205cc1d6047519d52d"></a>

```c
#define BL808_WIFIPLL_TOP_FREQ DT_FREQ_M(320)
```

相关声明：[BL808_WIFIPLL_TOP_FREQ](#acb181224dc5658205cc1d6047519d52d)。

WiFi PLL 最高频率（Top Frequency），`960 MHz VCO / 3 = 320 MHz`。

<a id="r_aa94669727f1a2fe2f030a683dbba7644"></a>

```c
#define BL808_AUPLL_TOP_FREQ 442368000
```

相关声明：[BL808_AUPLL_TOP_FREQ](#aa94669727f1a2fe2f030a683dbba7644)。

48 kHz 系列所用音频 PLL 最高频率（Top Frequency）为 442.368 MHz，经后分频（Post-divider）`/18` 得到 24.576 MHz。

<a id="r_a0e3929bae7d5d2451d83dd4ea40b1960"></a>

```c
#define BL808_AUPLL_TOP_FREQ_44K1 451584000
```

相关声明：[BL808_AUPLL_TOP_FREQ_44K1](#a0e3929bae7d5d2451d83dd4ea40b1960)。

44.1 kHz 系列所用音频 PLL 最高频率（Top Frequency）为 451.584 MHz，经后分频（Post-divider）`/20` 得到 22.5792 MHz。

<a id="r_a9b5da6c37cdda7252f4cd22309e18702"></a>

```c
#define BL808_WIFIPLL_TOP_FREQ_OC1 DT_FREQ_M(480)
```

相关声明：[BL808_WIFIPLL_TOP_FREQ_OC1](#a9b5da6c37cdda7252f4cd22309e18702)。

超频 WiFi PLL 最高频率（Overclocked Top Frequency），`960 MHz VCO / 2 = 480 MHz`。

<a id="r_a794fb843efa91b6c59611ead5799c0ef"></a>

```c
#define BL808_WIFIPLL_TOP_FREQ_OC2 DT_FREQ_M(640)
```

相关声明：[BL808_WIFIPLL_TOP_FREQ_OC2](#a794fb843efa91b6c59611ead5799c0ef)。

超频 WiFi PLL 最高频率（Overclocked Top Frequency），无分频时为 640 MHz。

<a id="r_a9e92ee2f1449fe9e3cf875e3faeaaded"></a>

```c
#define BL808_CPUPLL_TOP_FREQ DT_FREQ_M(480)
```

相关声明：[BL808_CPUPLL_TOP_FREQ](#a9e92ee2f1449fe9e3cf875e3faeaaded)。

CPU PLL 最高频率（Top Frequency）为 480 MHz。

<a id="r_aecb902e1a8d8861dc07010d1e6cb1908"></a>

```c
#define BL808_UHSPLL_TOP_FREQ DT_FREQ_M(2300)
```

相关声明：[BL808_UHSPLL_TOP_FREQ](#aecb902e1a8d8861dc07010d1e6cb1908)。

UHS PLL 最高频率（Top Frequency）为 2300 MHz。

## 1.2\_详细说明（Detailed Documentation）

<a id="a09e845c88455d650e087d54e5e0104df"></a>

### `BL808_AUPLL_ID_DIV1`

```c
#define BL808_AUPLL_ID_DIV1 1
```

AUPLL 输出选择（Output Select）：1 分频。

<a id="aa94669727f1a2fe2f030a683dbba7644"></a>

### `BL808_AUPLL_TOP_FREQ`

```c
#define BL808_AUPLL_TOP_FREQ 442368000
```

48 kHz 系列所用音频 PLL 最高频率（Top Frequency）为 442.368 MHz，经后分频（Post-divider）`/18` 得到 24.576 MHz。

<a id="a0e3929bae7d5d2451d83dd4ea40b1960"></a>

### `BL808_AUPLL_TOP_FREQ_44K1`

```c
#define BL808_AUPLL_TOP_FREQ_44K1 451584000
```

44.1 kHz 系列所用音频 PLL 最高频率（Top Frequency）为 451.584 MHz，经后分频（Post-divider）`/20` 得到 22.5792 MHz。

<a id="a14ebe26a8a7978110db3b60b02c14cf5"></a>

### `BL808_CLKID_CLK_160M`

```c
#define BL808_CLKID_CLK_160M (BFLB_CLKID_CLK_PRIVATE + 3)
```

160 MHz 时钟（Clock）。

<a id="a4698a9cec975c91e8eb835d905177686"></a>

### `BL808_CLKID_CLK_AUPLL`

```c
#define BL808_CLKID_CLK_AUPLL (BFLB_CLKID_CLK_PRIVATE + 1)
```

音频锁相环时钟（Audio PLL Clock）。

<a id="ae5146bbdf74be5084e2c585f22857433"></a>

### `BL808_CLKID_CLK_BCLK`

```c
#define BL808_CLKID_CLK_BCLK BFLB_CLKID_CLK_BCLK
```

总线时钟（Bus Clock）。

<a id="aa9c012eb82f134cc040781f9f9eb37d2"></a>

### `BL808_CLKID_CLK_CPUPLL`

```c
#define BL808_CLKID_CLK_CPUPLL (BFLB_CLKID_CLK_PRIVATE + 2)
```

CPU 锁相环时钟（CPU PLL Clock）。

<a id="af6a43433db32add4813c688ab1a4adc5"></a>

### `BL808_CLKID_CLK_CRYSTAL`

```c
#define BL808_CLKID_CLK_CRYSTAL BFLB_CLKID_CLK_CRYSTAL
```

晶体时钟（Crystal Clock）。

<a id="a7fee3bb46198223c41681c86f8574a28"></a>

### `BL808_CLKID_CLK_F32K`

```c
#define BL808_CLKID_CLK_F32K BFLB_CLKID_CLK_F32K
```

F32K 时钟（Clock）。

<a id="af76d527c250ec896ed0d768a1a11616a"></a>

### `BL808_CLKID_CLK_RC32K`

```c
#define BL808_CLKID_CLK_RC32K BFLB_CLKID_CLK_RC32K
```

RC32K 时钟（Clock）。

<a id="a99b553bfe231791c2c7c40d8a88329ad"></a>

### `BL808_CLKID_CLK_RC32M`

```c
#define BL808_CLKID_CLK_RC32M BFLB_CLKID_CLK_RC32M
```

32 MHz RC 振荡器时钟（RC Oscillator Clock）。

<a id="acd2b6c7f3812560d616c43312e747c70"></a>

### `BL808_CLKID_CLK_ROOT`

```c
#define BL808_CLKID_CLK_ROOT BFLB_CLKID_CLK_ROOT
```

根时钟（Root Clock）。

<a id="ac6a515aeb3dc9b2a101c8ba3935fa029"></a>

### `BL808_CLKID_CLK_UHSPLL`

```c
#define BL808_CLKID_CLK_UHSPLL (BFLB_CLKID_CLK_PRIVATE + 4)
```

UHS 锁相环时钟（PLL Clock），为 UHS PSRAM 物理层（PHY）专用 PLL。

<a id="a2aa6a56fd934cc2657b4aeda89fc938f"></a>

### `BL808_CLKID_CLK_WIFIPLL`

```c
#define BL808_CLKID_CLK_WIFIPLL (BFLB_CLKID_CLK_PRIVATE + 0)
```

Wi-Fi 锁相环时钟（WiFi PLL Clock）。

<a id="a8be3db0e3d1933894c2917fb176a08f7"></a>

### `BL808_CLKID_CLK_XTAL32K`

```c
#define BL808_CLKID_CLK_XTAL32K BFLB_CLKID_CLK_XTAL32K
```

XTAL32K 时钟（Clock）。

<a id="a34149d4ba4e5d7c84aaacca3d67cb1f8"></a>

### `BL808_CPUPLL_ID_DIV1`

```c
#define BL808_CPUPLL_ID_DIV1 0
```

CPU PLL 输出选择（Output Select）：1 分频。

<a id="a9e92ee2f1449fe9e3cf875e3faeaaded"></a>

### `BL808_CPUPLL_TOP_FREQ`

```c
#define BL808_CPUPLL_TOP_FREQ DT_FREQ_M(480)
```

CPU PLL 最高频率（Top Frequency）为 480 MHz。

<a id="aecb902e1a8d8861dc07010d1e6cb1908"></a>

### `BL808_UHSPLL_TOP_FREQ`

```c
#define BL808_UHSPLL_TOP_FREQ DT_FREQ_M(2300)
```

UHS PLL 最高频率（Top Frequency）为 2300 MHz。

<a id="a7bf45d0ed63f9db31d1c61a9677b378c"></a>

### `BL808_WIFIPLL_ID_DIV1`

```c
#define BL808_WIFIPLL_ID_DIV1 3
```

WiFi PLL 输出选择（Output Select）：最高频率（Top Frequency）。

<a id="a4ad1ebd0d4c445b74d18f1409beeb8fe"></a>

### `BL808_WIFIPLL_ID_DIV3_4`

```c
#define BL808_WIFIPLL_ID_DIV3_4 2
```

WiFi PLL 输出选择（Output Select）：最高频率（Top Frequency）的 `3/4`。

<a id="acb181224dc5658205cc1d6047519d52d"></a>

### `BL808_WIFIPLL_TOP_FREQ`

```c
#define BL808_WIFIPLL_TOP_FREQ DT_FREQ_M(320)
```

WiFi PLL 最高频率（Top Frequency），`960 MHz VCO / 3 = 320 MHz`。

<a id="a9b5da6c37cdda7252f4cd22309e18702"></a>

### `BL808_WIFIPLL_TOP_FREQ_OC1`

```c
#define BL808_WIFIPLL_TOP_FREQ_OC1 DT_FREQ_M(480)
```

超频 WiFi PLL 最高频率（Overclocked Top Frequency），`960 MHz VCO / 2 = 480 MHz`。

<a id="a794fb843efa91b6c59611ead5799c0ef"></a>

### `BL808_WIFIPLL_TOP_FREQ_OC2`

```c
#define BL808_WIFIPLL_TOP_FREQ_OC2 DT_FREQ_M(640)
```

超频 WiFi PLL 最高频率（Overclocked Top Frequency），无分频时为 640 MHz。


## 1.3\_原页交叉引用（Cross References）

- [bflb_clock_common.h](../api_source_reference/P065_bflb_clock_common.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P064_bflb_bl808_clock.h_源码浏览.md)
- [BFLB_CLKID_CLK_ROOT](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#af2d6e2a7c386b50358a9cf50fc8808b3)
- [BFLB_CLKID_CLK_RC32M](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a48bf5d6a4379c03c7817503d7fe66c8b)
- [BFLB_CLKID_CLK_CRYSTAL](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a059c42552c94b942f53c644207776326)
- [BFLB_CLKID_CLK_BCLK](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a81f8f15faf5025212dbe96417515c358)
- [BFLB_CLKID_CLK_F32K](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a5b8eca0197f839af7776f5d02c6eab13)
- [BFLB_CLKID_CLK_XTAL32K](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#a14b75b51b81786bb7ae26070e5e41e22)
- [BFLB_CLKID_CLK_RC32K](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#ad2b0e7bd97598e50d10ce66d5b52a360)
- [BFLB_CLKID_CLK_PRIVATE](../api_file_protocol_service_reference/P005_zephyr__dt-bindings__clock__bflb_clock_common.h_文件参考.md#acc4f8e38984a2ec63e470b919b6d8aef)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__bluetooth__audio__ccp.h_文件参考.md)
