---
id: learning.zephyr-docs.api-file-reference.page-351
title: zephyr__dt-bindings__dma__renesas_rz_dma.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rz__dma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第351章\_zephyr\_\_dt-bindings\_\_dma\_\_renesas\_rz\_dma.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rz__dma_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 351.1\_宏定义（Macros）

<a id="r_a2b81e575b015aab7551dd910d5c8204d"></a>

```c
#define RZ_DMA_MODE_NORMAL (0U)
```

相关声明：[RZ_DMA_MODE_NORMAL](#a2b81e575b015aab7551dd910d5c8204d)。

<a id="r_a3dc76a9c51aa176eecf2fb0a7c58ce05"></a>

```c
#define RZ_DMA_MODE_BLOCK (1U)
```

相关声明：[RZ_DMA_MODE_BLOCK](#a3dc76a9c51aa176eecf2fb0a7c58ce05)。

<a id="r_a5a925aec5cb8d0e787c00e3bf28adabb"></a>

```c
#define RZ_DMA_CFG_SRC_DATA_SIZE(val)
```

相关声明：[RZ_DMA_CFG_SRC_DATA_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)。

<a id="r_ad2630f88edccd524379229c6d08c3d6f"></a>

```c
#define RZ_DMA_SRC_1_BYTE RZ_DMA_CFG_SRC_DATA_SIZE(0)
```

相关声明：[RZ_DMA_SRC_1_BYTE](#ad2630f88edccd524379229c6d08c3d6f)、[RZ_DMA_CFG_SRC_DATA_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)。

<a id="r_a06c39443f03c6bf1f4a10a46492a4fcf"></a>

```c
#define RZ_DMA_SRC_2_BYTE RZ_DMA_CFG_SRC_DATA_SIZE(1)
```

相关声明：[RZ_DMA_SRC_2_BYTE](#a06c39443f03c6bf1f4a10a46492a4fcf)、[RZ_DMA_CFG_SRC_DATA_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)。

<a id="r_a4bd983230d98d2a4bd98942f3b433765"></a>

```c
#define RZ_DMA_SRC_4_BYTE RZ_DMA_CFG_SRC_DATA_SIZE(2)
```

相关声明：[RZ_DMA_SRC_4_BYTE](#a4bd983230d98d2a4bd98942f3b433765)、[RZ_DMA_CFG_SRC_DATA_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)。

<a id="r_aadd165c44a5d9ec2d221f4de0fff99da"></a>

```c
#define RZ_DMA_SRC_8_BYTE RZ_DMA_CFG_SRC_DATA_SIZE(3)
```

相关声明：[RZ_DMA_SRC_8_BYTE](#aadd165c44a5d9ec2d221f4de0fff99da)、[RZ_DMA_CFG_SRC_DATA_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)。

<a id="r_a491d97dc4a9005cbf668fed70fe61292"></a>

```c
#define RZ_DMA_SRC_16_BYTE RZ_DMA_CFG_SRC_DATA_SIZE(4)
```

相关声明：[RZ_DMA_SRC_16_BYTE](#a491d97dc4a9005cbf668fed70fe61292)、[RZ_DMA_CFG_SRC_DATA_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)。

<a id="r_a05c3af12ddbc5abc07a635ee3dc184d8"></a>

```c
#define RZ_DMA_SRC_32_BYTE RZ_DMA_CFG_SRC_DATA_SIZE(5)
```

相关声明：[RZ_DMA_SRC_32_BYTE](#a05c3af12ddbc5abc07a635ee3dc184d8)、[RZ_DMA_CFG_SRC_DATA_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)。

<a id="r_a47c957c6ddbf73e702d3cc406396d598"></a>

```c
#define RZ_DMA_SRC_64_BYTE RZ_DMA_CFG_SRC_DATA_SIZE(6)
```

相关声明：[RZ_DMA_SRC_64_BYTE](#a47c957c6ddbf73e702d3cc406396d598)、[RZ_DMA_CFG_SRC_DATA_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)。

<a id="r_afbebd4bc7e8faafa874532416b9f5977"></a>

```c
#define RZ_DMA_SRC_128_BYTE RZ_DMA_CFG_SRC_DATA_SIZE(7)
```

相关声明：[RZ_DMA_SRC_128_BYTE](#afbebd4bc7e8faafa874532416b9f5977)、[RZ_DMA_CFG_SRC_DATA_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)。

<a id="r_aee9e5ee0e341869584ffcd22bec9d684"></a>

```c
#define RZ_DMA_CFG_DEST_DATA_SIZE(val)
```

相关声明：[RZ_DMA_CFG_DEST_DATA_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)。

<a id="r_a34bf5afed49353a0ecdff99cff12bd95"></a>

```c
#define RZ_DMA_DEST_1_BYTE RZ_DMA_CFG_DEST_DATA_SIZE(0)
```

相关声明：[RZ_DMA_DEST_1_BYTE](#a34bf5afed49353a0ecdff99cff12bd95)、[RZ_DMA_CFG_DEST_DATA_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)。

<a id="r_a16018c672b1ff17d2065617e1145ce85"></a>

```c
#define RZ_DMA_DEST_2_BYTE RZ_DMA_CFG_DEST_DATA_SIZE(1)
```

相关声明：[RZ_DMA_DEST_2_BYTE](#a16018c672b1ff17d2065617e1145ce85)、[RZ_DMA_CFG_DEST_DATA_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)。

<a id="r_ad5063a15c1612bbba264227a40b91d87"></a>

```c
#define RZ_DMA_DEST_4_BYTE RZ_DMA_CFG_DEST_DATA_SIZE(2)
```

相关声明：[RZ_DMA_DEST_4_BYTE](#ad5063a15c1612bbba264227a40b91d87)、[RZ_DMA_CFG_DEST_DATA_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)。

<a id="r_a8a02c00f90f4532b44a2c2ff7f1be3ab"></a>

```c
#define RZ_DMA_DEST_8_BYTE RZ_DMA_CFG_DEST_DATA_SIZE(3)
```

相关声明：[RZ_DMA_DEST_8_BYTE](#a8a02c00f90f4532b44a2c2ff7f1be3ab)、[RZ_DMA_CFG_DEST_DATA_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)。

<a id="r_acd01a438d73deaf6fe76b06c44593394"></a>

```c
#define RZ_DMA_DEST_16_BYTE RZ_DMA_CFG_DEST_DATA_SIZE(4)
```

相关声明：[RZ_DMA_DEST_16_BYTE](#acd01a438d73deaf6fe76b06c44593394)、[RZ_DMA_CFG_DEST_DATA_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)。

<a id="r_a47929d19f83967834a22b2a5bef7dde1"></a>

```c
#define RZ_DMA_DEST_32_BYTE RZ_DMA_CFG_DEST_DATA_SIZE(5)
```

相关声明：[RZ_DMA_DEST_32_BYTE](#a47929d19f83967834a22b2a5bef7dde1)、[RZ_DMA_CFG_DEST_DATA_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)。

<a id="r_a1a95a59ace78fbfadbfdb113975ee361"></a>

```c
#define RZ_DMA_DEST_64_BYTE RZ_DMA_CFG_DEST_DATA_SIZE(6)
```

相关声明：[RZ_DMA_DEST_64_BYTE](#a1a95a59ace78fbfadbfdb113975ee361)、[RZ_DMA_CFG_DEST_DATA_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)。

<a id="r_aa415a830c4e71f1c59869f1d1935a752"></a>

```c
#define RZ_DMA_DEST_128_BYTE RZ_DMA_CFG_DEST_DATA_SIZE(7)
```

相关声明：[RZ_DMA_DEST_128_BYTE](#aa415a830c4e71f1c59869f1d1935a752)、[RZ_DMA_CFG_DEST_DATA_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)。

<a id="r_a41b9387b512f2d26315db92a55b331bc"></a>

```c
#define RZ_DMA_CFG_SRC_ADDR_MODE(val)
```

相关声明：[RZ_DMA_CFG_SRC_ADDR_MODE](#a41b9387b512f2d26315db92a55b331bc)。

<a id="r_a272bea303fa2484c83a197831b17ea75"></a>

```c
#define RZ_DMA_SRC_INCREMENTED RZ_DMA_CFG_SRC_ADDR_MODE(0)
```

相关声明：[RZ_DMA_SRC_INCREMENTED](#a272bea303fa2484c83a197831b17ea75)、[RZ_DMA_CFG_SRC_ADDR_MODE](#a41b9387b512f2d26315db92a55b331bc)。

<a id="r_a0e47b6a3c30b6157d99d397641c672c1"></a>

```c
#define RZ_DMA_SRC_FIXED RZ_DMA_CFG_SRC_ADDR_MODE(1)
```

相关声明：[RZ_DMA_SRC_FIXED](#a0e47b6a3c30b6157d99d397641c672c1)、[RZ_DMA_CFG_SRC_ADDR_MODE](#a41b9387b512f2d26315db92a55b331bc)。

<a id="r_a35c2cf645fd17892b06760e79e7799e0"></a>

```c
#define RZ_DMA_CFG_DEST_ADDR_MODE(val)
```

相关声明：[RZ_DMA_CFG_DEST_ADDR_MODE](#a35c2cf645fd17892b06760e79e7799e0)。

<a id="r_a4d3de22701e71b2bb3dabcf63f04c35f"></a>

```c
#define RZ_DMA_DEST_INCREMENTED RZ_DMA_CFG_DEST_ADDR_MODE(0)
```

相关声明：[RZ_DMA_DEST_INCREMENTED](#a4d3de22701e71b2bb3dabcf63f04c35f)、[RZ_DMA_CFG_DEST_ADDR_MODE](#a35c2cf645fd17892b06760e79e7799e0)。

<a id="r_a5cb1d2cbda322e0524c3317fe830dd2e"></a>

```c
#define RZ_DMA_DEST_FIXED RZ_DMA_CFG_DEST_ADDR_MODE(1)
```

相关声明：[RZ_DMA_DEST_FIXED](#a5cb1d2cbda322e0524c3317fe830dd2e)、[RZ_DMA_CFG_DEST_ADDR_MODE](#a35c2cf645fd17892b06760e79e7799e0)。

<a id="r_a752b0f622d69a7eb8bffae025208f684"></a>

```c
#define RZ_DMA_MEM_TO_PERIPH
```

相关声明：[RZ_DMA_MEM_TO_PERIPH](#a752b0f622d69a7eb8bffae025208f684)。

<a id="r_a11c53b4c6de9c71d7b443ef02c2b9384"></a>

```c
#define RZ_DMA_PERIPH_TO_MEM
```

相关声明：[RZ_DMA_PERIPH_TO_MEM](#a11c53b4c6de9c71d7b443ef02c2b9384)。

## 351.2\_详细说明（Detailed Documentation）

<a id="a35c2cf645fd17892b06760e79e7799e0"></a>

### `RZ_DMA_CFG_DEST_ADDR_MODE`

```c
#define RZ_DMA_CFG_DEST_ADDR_MODE ( val)
```

展开值（Value）：

```c
((val & 0x1) << 8)
```

<a id="aee9e5ee0e341869584ffcd22bec9d684"></a>

### `RZ_DMA_CFG_DEST_DATA_SIZE`

```c
#define RZ_DMA_CFG_DEST_DATA_SIZE ( val)
```

展开值（Value）：

```c
((val & 0x7) << 4)
```

<a id="a41b9387b512f2d26315db92a55b331bc"></a>

### `RZ_DMA_CFG_SRC_ADDR_MODE`

```c
#define RZ_DMA_CFG_SRC_ADDR_MODE ( val)
```

展开值（Value）：

```c
((val & 0x1) << 7)
```

<a id="a5a925aec5cb8d0e787c00e3bf28adabb"></a>

### `RZ_DMA_CFG_SRC_DATA_SIZE`

```c
#define RZ_DMA_CFG_SRC_DATA_SIZE ( val)
```

展开值（Value）：

```c
((val & 0x7) << 1)
```

<a id="aa415a830c4e71f1c59869f1d1935a752"></a>

### `RZ_DMA_DEST_128_BYTE`

```c
#define RZ_DMA_DEST_128_BYTE RZ_DMA_CFG_DEST_DATA_SIZE(7)
```

<a id="acd01a438d73deaf6fe76b06c44593394"></a>

### `RZ_DMA_DEST_16_BYTE`

```c
#define RZ_DMA_DEST_16_BYTE RZ_DMA_CFG_DEST_DATA_SIZE(4)
```

<a id="a34bf5afed49353a0ecdff99cff12bd95"></a>

### `RZ_DMA_DEST_1_BYTE`

```c
#define RZ_DMA_DEST_1_BYTE RZ_DMA_CFG_DEST_DATA_SIZE(0)
```

<a id="a16018c672b1ff17d2065617e1145ce85"></a>

### `RZ_DMA_DEST_2_BYTE`

```c
#define RZ_DMA_DEST_2_BYTE RZ_DMA_CFG_DEST_DATA_SIZE(1)
```

<a id="a47929d19f83967834a22b2a5bef7dde1"></a>

### `RZ_DMA_DEST_32_BYTE`

```c
#define RZ_DMA_DEST_32_BYTE RZ_DMA_CFG_DEST_DATA_SIZE(5)
```

<a id="ad5063a15c1612bbba264227a40b91d87"></a>

### `RZ_DMA_DEST_4_BYTE`

```c
#define RZ_DMA_DEST_4_BYTE RZ_DMA_CFG_DEST_DATA_SIZE(2)
```

<a id="a1a95a59ace78fbfadbfdb113975ee361"></a>

### `RZ_DMA_DEST_64_BYTE`

```c
#define RZ_DMA_DEST_64_BYTE RZ_DMA_CFG_DEST_DATA_SIZE(6)
```

<a id="a8a02c00f90f4532b44a2c2ff7f1be3ab"></a>

### `RZ_DMA_DEST_8_BYTE`

```c
#define RZ_DMA_DEST_8_BYTE RZ_DMA_CFG_DEST_DATA_SIZE(3)
```

<a id="a5cb1d2cbda322e0524c3317fe830dd2e"></a>

### `RZ_DMA_DEST_FIXED`

```c
#define RZ_DMA_DEST_FIXED RZ_DMA_CFG_DEST_ADDR_MODE(1)
```

<a id="a4d3de22701e71b2bb3dabcf63f04c35f"></a>

### `RZ_DMA_DEST_INCREMENTED`

```c
#define RZ_DMA_DEST_INCREMENTED RZ_DMA_CFG_DEST_ADDR_MODE(0)
```

<a id="a752b0f622d69a7eb8bffae025208f684"></a>

### `RZ_DMA_MEM_TO_PERIPH`

```c
#define RZ_DMA_MEM_TO_PERIPH
```

展开值（Value）：

```c
(RZ_DMA_MODE_NORMAL | RZ_DMA_SRC_INCREMENTED | RZ_DMA_DEST_FIXED | RZ_DMA_SRC_1_BYTE |     \
 RZ_DMA_DEST_1_BYTE)
```

<a id="a3dc76a9c51aa176eecf2fb0a7c58ce05"></a>

### `RZ_DMA_MODE_BLOCK`

```c
#define RZ_DMA_MODE_BLOCK (1U)
```

<a id="a2b81e575b015aab7551dd910d5c8204d"></a>

### `RZ_DMA_MODE_NORMAL`

```c
#define RZ_DMA_MODE_NORMAL (0U)
```

<a id="a11c53b4c6de9c71d7b443ef02c2b9384"></a>

### `RZ_DMA_PERIPH_TO_MEM`

```c
#define RZ_DMA_PERIPH_TO_MEM
```

展开值（Value）：

```c
(RZ_DMA_MODE_NORMAL | RZ_DMA_SRC_FIXED | RZ_DMA_DEST_INCREMENTED | RZ_DMA_SRC_1_BYTE |     \
 RZ_DMA_DEST_1_BYTE)
```

<a id="afbebd4bc7e8faafa874532416b9f5977"></a>

### `RZ_DMA_SRC_128_BYTE`

```c
#define RZ_DMA_SRC_128_BYTE RZ_DMA_CFG_SRC_DATA_SIZE(7)
```

<a id="a491d97dc4a9005cbf668fed70fe61292"></a>

### `RZ_DMA_SRC_16_BYTE`

```c
#define RZ_DMA_SRC_16_BYTE RZ_DMA_CFG_SRC_DATA_SIZE(4)
```

<a id="ad2630f88edccd524379229c6d08c3d6f"></a>

### `RZ_DMA_SRC_1_BYTE`

```c
#define RZ_DMA_SRC_1_BYTE RZ_DMA_CFG_SRC_DATA_SIZE(0)
```

<a id="a06c39443f03c6bf1f4a10a46492a4fcf"></a>

### `RZ_DMA_SRC_2_BYTE`

```c
#define RZ_DMA_SRC_2_BYTE RZ_DMA_CFG_SRC_DATA_SIZE(1)
```

<a id="a05c3af12ddbc5abc07a635ee3dc184d8"></a>

### `RZ_DMA_SRC_32_BYTE`

```c
#define RZ_DMA_SRC_32_BYTE RZ_DMA_CFG_SRC_DATA_SIZE(5)
```

<a id="a4bd983230d98d2a4bd98942f3b433765"></a>

### `RZ_DMA_SRC_4_BYTE`

```c
#define RZ_DMA_SRC_4_BYTE RZ_DMA_CFG_SRC_DATA_SIZE(2)
```

<a id="a47c957c6ddbf73e702d3cc406396d598"></a>

### `RZ_DMA_SRC_64_BYTE`

```c
#define RZ_DMA_SRC_64_BYTE RZ_DMA_CFG_SRC_DATA_SIZE(6)
```

<a id="aadd165c44a5d9ec2d221f4de0fff99da"></a>

### `RZ_DMA_SRC_8_BYTE`

```c
#define RZ_DMA_SRC_8_BYTE RZ_DMA_CFG_SRC_DATA_SIZE(3)
```

<a id="a0e47b6a3c30b6157d99d397641c672c1"></a>

### `RZ_DMA_SRC_FIXED`

```c
#define RZ_DMA_SRC_FIXED RZ_DMA_CFG_SRC_ADDR_MODE(1)
```

<a id="a272bea303fa2484c83a197831b17ea75"></a>

### `RZ_DMA_SRC_INCREMENTED`

```c
#define RZ_DMA_SRC_INCREMENTED RZ_DMA_CFG_SRC_ADDR_MODE(0)
```


## 351.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rz__dma_8h_source.html)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="arenesas__rz__dma_8h_html_a272bea303fa2484c83a197831b17ea75"></a>
<a id="arenesas__rz__dma_8h_html_a2b81e575b015aab7551dd910d5c8204d"></a>
<a id="arenesas__rz__dma_8h_html_a34bf5afed49353a0ecdff99cff12bd95"></a>
<a id="arenesas__rz__dma_8h_html_a5cb1d2cbda322e0524c3317fe830dd2e"></a>
<a id="arenesas__rz__dma_8h_html_ad2630f88edccd524379229c6d08c3d6f"></a>
<a id="arenesas__rz__dma_8h_html_a0e47b6a3c30b6157d99d397641c672c1"></a>
<a id="arenesas__rz__dma_8h_html_a4d3de22701e71b2bb3dabcf63f04c35f"></a>

---

[上一章](P350_zephyr__dt-bindings__memory-controller__renesas,ra-sdram.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P352_zephyr__dt-bindings__pwm__renesas_rz_pwm.h_文件参考.md)
