---
id: learning.zephyr-docs.api-file-reference.page-54
title: zephyr__drivers__dma__dma_mcux_pxp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dma__mcux__pxp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_zephyr\_\_drivers\_\_dma\_\_dma\_mcux\_pxp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dma__mcux__pxp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 54.1\_宏定义（Macros）

<a id="r_a1a447b1990a0a58a58b8f2c1b91f4596"></a>

```c
#define DMA_MCUX_PXP_CMD_MASK 0xE0
```

相关声明：[DMA_MCUX_PXP_CMD_MASK](#a1a447b1990a0a58a58b8f2c1b91f4596)。

<a id="r_a98023d4702873f806316fa8076217f2b"></a>

```c
#define DMA_MCUX_PXP_CMD_SHIFT 0x5
```

相关声明：[DMA_MCUX_PXP_CMD_SHIFT](#a98023d4702873f806316fa8076217f2b)。

<a id="r_a99a43acbabab4f6d3d16601776e64ef5"></a>

```c
#define DMA_MCUX_PXP_FMT_MASK 0x1F
```

相关声明：[DMA_MCUX_PXP_FMT_MASK](#a99a43acbabab4f6d3d16601776e64ef5)。

<a id="r_a5ecb10ea31b3b4841d1d1e50ef182b39"></a>

```c
#define DMA_MCUX_PXP_FMT_SHIFT 0x0
```

相关声明：[DMA_MCUX_PXP_FMT_SHIFT](#a5ecb10ea31b3b4841d1d1e50ef182b39)。

<a id="r_ae33fe6641b02a3af1910ba0ab30306a2"></a>

```c
#define DMA_MCUX_PXP_FMT(x)
```

相关声明：[DMA_MCUX_PXP_FMT](#ae33fe6641b02a3af1910ba0ab30306a2)。

<a id="r_a3b6888b7002f91c46c891497420a59a4"></a>

```c
#define DMA_MCUX_PXP_CMD(x)
```

相关声明：[DMA_MCUX_PXP_CMD](#a3b6888b7002f91c46c891497420a59a4)。

<a id="r_ad0e771ececbc5a7f6257d76b7d3667d7"></a>

```c
#define DMA_MCUX_PXP_CMD_ROTATE_0 0
```

相关声明：[DMA_MCUX_PXP_CMD_ROTATE_0](#ad0e771ececbc5a7f6257d76b7d3667d7)。

<a id="r_a26e4776708c27df4c2a17437ea944092"></a>

```c
#define DMA_MCUX_PXP_CMD_ROTATE_90 1
```

相关声明：[DMA_MCUX_PXP_CMD_ROTATE_90](#a26e4776708c27df4c2a17437ea944092)。

<a id="r_ab37674ee7555385cefe3cbc328201e31"></a>

```c
#define DMA_MCUX_PXP_CMD_ROTATE_180 2
```

相关声明：[DMA_MCUX_PXP_CMD_ROTATE_180](#ab37674ee7555385cefe3cbc328201e31)。

<a id="r_af53cad3d27fbd9d2ae8ca108201f882f"></a>

```c
#define DMA_MCUX_PXP_CMD_ROTATE_270 3
```

相关声明：[DMA_MCUX_PXP_CMD_ROTATE_270](#af53cad3d27fbd9d2ae8ca108201f882f)。

<a id="r_a39a2b6f27b7dae092f9cfe491bbd078f"></a>

```c
#define DMA_MCUX_PXP_FMT_RGB565 0
```

相关声明：[DMA_MCUX_PXP_FMT_RGB565](#a39a2b6f27b7dae092f9cfe491bbd078f)。

<a id="r_a3667a7b1faf41211b55c22d5f22edd3b"></a>

```c
#define DMA_MCUX_PXP_FMT_RGB888 1
```

相关声明：[DMA_MCUX_PXP_FMT_RGB888](#a3667a7b1faf41211b55c22d5f22edd3b)。

<a id="r_a4bd4d488dc602ce67c9a5bf9855517c9"></a>

```c
#define DMA_MCUX_PXP_FMT_ARGB8888 2
```

相关声明：[DMA_MCUX_PXP_FMT_ARGB8888](#a4bd4d488dc602ce67c9a5bf9855517c9)。

<a id="r_aee1fd30cf35c5a96dfe122aac2d92161"></a>

```c
#define DMA_MCUX_PXP_FLIP_MASK 0x3
```

相关声明：[DMA_MCUX_PXP_FLIP_MASK](#aee1fd30cf35c5a96dfe122aac2d92161)。

<a id="r_af549226b726bb0f0b61eed21e1a819fc"></a>

```c
#define DMA_MCUX_PXP_FLIP_SHIFT 0x0
```

相关声明：[DMA_MCUX_PXP_FLIP_SHIFT](#af549226b726bb0f0b61eed21e1a819fc)。

<a id="r_a9f0355cb6ba642eabe471d3d2c2b7134"></a>

```c
#define DMA_MCUX_PXP_FLIP(x)
```

相关声明：[DMA_MCUX_PXP_FLIP](#a9f0355cb6ba642eabe471d3d2c2b7134)。

<a id="r_aa8b7cf9b4c70c68c1d3acf5450dc6ddd"></a>

```c
#define DMA_MCUX_PXP_FLIP_DISABLE 0
```

相关声明：[DMA_MCUX_PXP_FLIP_DISABLE](#aa8b7cf9b4c70c68c1d3acf5450dc6ddd)。

<a id="r_a6bda2feae39d8241f08dcdc1452151b7"></a>

```c
#define DMA_MCUX_PXP_FLIP_HORIZONTAL 1
```

相关声明：[DMA_MCUX_PXP_FLIP_HORIZONTAL](#a6bda2feae39d8241f08dcdc1452151b7)。

<a id="r_a5f8907abd274e1caef6c806ba342b318"></a>

```c
#define DMA_MCUX_PXP_FLIP_VERTICAL 2
```

相关声明：[DMA_MCUX_PXP_FLIP_VERTICAL](#a5f8907abd274e1caef6c806ba342b318)。

<a id="r_a1fea61bad4d78fe0ceb2b9a2e8583cad"></a>

```c
#define DMA_MCUX_PXP_FLIP_BOTH 3
```

相关声明：[DMA_MCUX_PXP_FLIP_BOTH](#a1fea61bad4d78fe0ceb2b9a2e8583cad)。

## 54.2\_详细说明（Detailed Documentation）

<a id="a3b6888b7002f91c46c891497420a59a4"></a>

### `DMA_MCUX_PXP_CMD`

```c
#define DMA_MCUX_PXP_CMD ( x)
```

展开值（Value）：

```c
((x << DMA_MCUX_PXP_CMD_SHIFT) & DMA_MCUX_PXP_CMD_MASK)
```

<a id="a1a447b1990a0a58a58b8f2c1b91f4596"></a>

### `DMA_MCUX_PXP_CMD_MASK`

```c
#define DMA_MCUX_PXP_CMD_MASK 0xE0
```

<a id="ad0e771ececbc5a7f6257d76b7d3667d7"></a>

### `DMA_MCUX_PXP_CMD_ROTATE_0`

```c
#define DMA_MCUX_PXP_CMD_ROTATE_0 0
```

<a id="ab37674ee7555385cefe3cbc328201e31"></a>

### `DMA_MCUX_PXP_CMD_ROTATE_180`

```c
#define DMA_MCUX_PXP_CMD_ROTATE_180 2
```

<a id="af53cad3d27fbd9d2ae8ca108201f882f"></a>

### `DMA_MCUX_PXP_CMD_ROTATE_270`

```c
#define DMA_MCUX_PXP_CMD_ROTATE_270 3
```

<a id="a26e4776708c27df4c2a17437ea944092"></a>

### `DMA_MCUX_PXP_CMD_ROTATE_90`

```c
#define DMA_MCUX_PXP_CMD_ROTATE_90 1
```

<a id="a98023d4702873f806316fa8076217f2b"></a>

### `DMA_MCUX_PXP_CMD_SHIFT`

```c
#define DMA_MCUX_PXP_CMD_SHIFT 0x5
```

<a id="a9f0355cb6ba642eabe471d3d2c2b7134"></a>

### `DMA_MCUX_PXP_FLIP`

```c
#define DMA_MCUX_PXP_FLIP ( x)
```

展开值（Value）：

```c
((x << DMA_MCUX_PXP_FLIP_SHIFT) & DMA_MCUX_PXP_FLIP_MASK)
```

<a id="a1fea61bad4d78fe0ceb2b9a2e8583cad"></a>

### `DMA_MCUX_PXP_FLIP_BOTH`

```c
#define DMA_MCUX_PXP_FLIP_BOTH 3
```

<a id="aa8b7cf9b4c70c68c1d3acf5450dc6ddd"></a>

### `DMA_MCUX_PXP_FLIP_DISABLE`

```c
#define DMA_MCUX_PXP_FLIP_DISABLE 0
```

<a id="a6bda2feae39d8241f08dcdc1452151b7"></a>

### `DMA_MCUX_PXP_FLIP_HORIZONTAL`

```c
#define DMA_MCUX_PXP_FLIP_HORIZONTAL 1
```

<a id="aee1fd30cf35c5a96dfe122aac2d92161"></a>

### `DMA_MCUX_PXP_FLIP_MASK`

```c
#define DMA_MCUX_PXP_FLIP_MASK 0x3
```

<a id="af549226b726bb0f0b61eed21e1a819fc"></a>

### `DMA_MCUX_PXP_FLIP_SHIFT`

```c
#define DMA_MCUX_PXP_FLIP_SHIFT 0x0
```

<a id="a5f8907abd274e1caef6c806ba342b318"></a>

### `DMA_MCUX_PXP_FLIP_VERTICAL`

```c
#define DMA_MCUX_PXP_FLIP_VERTICAL 2
```

<a id="ae33fe6641b02a3af1910ba0ab30306a2"></a>

### `DMA_MCUX_PXP_FMT`

```c
#define DMA_MCUX_PXP_FMT ( x)
```

展开值（Value）：

```c
((x << DMA_MCUX_PXP_FMT_SHIFT) & DMA_MCUX_PXP_FMT_MASK)
```

<a id="a4bd4d488dc602ce67c9a5bf9855517c9"></a>

### `DMA_MCUX_PXP_FMT_ARGB8888`

```c
#define DMA_MCUX_PXP_FMT_ARGB8888 2
```

<a id="a99a43acbabab4f6d3d16601776e64ef5"></a>

### `DMA_MCUX_PXP_FMT_MASK`

```c
#define DMA_MCUX_PXP_FMT_MASK 0x1F
```

<a id="a39a2b6f27b7dae092f9cfe491bbd078f"></a>

### `DMA_MCUX_PXP_FMT_RGB565`

```c
#define DMA_MCUX_PXP_FMT_RGB565 0
```

<a id="a3667a7b1faf41211b55c22d5f22edd3b"></a>

### `DMA_MCUX_PXP_FMT_RGB888`

```c
#define DMA_MCUX_PXP_FMT_RGB888 1
```

<a id="a5ecb10ea31b3b4841d1d1e50ef182b39"></a>

### `DMA_MCUX_PXP_FMT_SHIFT`

```c
#define DMA_MCUX_PXP_FMT_SHIFT 0x0
```


## 54.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_configuration_reference/P017_dma_mcux_pxp.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="adma__mcux__pxp_8h_html_a1a447b1990a0a58a58b8f2c1b91f4596"></a>
<a id="adma__mcux__pxp_8h_html_a98023d4702873f806316fa8076217f2b"></a>
<a id="adma__mcux__pxp_8h_html_aee1fd30cf35c5a96dfe122aac2d92161"></a>
<a id="adma__mcux__pxp_8h_html_af549226b726bb0f0b61eed21e1a819fc"></a>
<a id="adma__mcux__pxp_8h_html_a5ecb10ea31b3b4841d1d1e50ef182b39"></a>
<a id="adma__mcux__pxp_8h_html_a99a43acbabab4f6d3d16601776e64ef5"></a>

---

[上一章](P053_zephyr__drivers__dma__dma_mcux_lpc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P055_zephyr__drivers__dma__dma_npcx_gdma.h_文件参考.md)
