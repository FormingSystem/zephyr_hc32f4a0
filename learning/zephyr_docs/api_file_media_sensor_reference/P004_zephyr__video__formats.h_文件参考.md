---
id: learning.zephyr-docs.api-file-media-sensor-reference.page-4
title: zephyr__video__formats.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/formats_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_video\_\_formats.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/formats_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频格式（Video Format）API的主头文件。

<a id="details"></a>

```c
#include <stdint.h>
```

查看此文件的源码。

视频格式（Video Format）API的主头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.1\_宏定义（Macros）

<a id="r_gafb9e36597c39face52cd0c010df20951"></a>

```c
#define VIDEO_FOURCC(a, b, c, d)
```

相关声明：[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

唯一标识像素格式（Pixel Format）的四字符代码（Four-character-code，FOURCC）。

<a id="r_gafc6c4cb871f15464f2b7df86d91fd8f3"></a>

```c
#define VIDEO_FOURCC_FROM_STR(str)
```

相关声明：[VIDEO_FOURCC_FROM_STR](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafc6c4cb871f15464f2b7df86d91fd8f3)。

将四字符字符串（Four-character-string）转换为四字符代码（FOURCC）。

<a id="r_gacd3805f57633c3db8c6adcd87384bd5c"></a>

```c
#define VIDEO_FOURCC_TO_STR(fourcc)
```

相关声明：[VIDEO_FOURCC_TO_STR](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gacd3805f57633c3db8c6adcd87384bd5c)。

将四字符代码（FOURCC）转换为四字符字符串（Four-character-string）。

<a id="r_ga7793e9ac7b592429b0dac4da4ead3674"></a>

```c
#define VIDEO_FMT_IS_GRAYSCALE(pixfmt)
```

相关声明：[VIDEO_FMT_IS_GRAYSCALE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga7793e9ac7b592429b0dac4da4ead3674)。

检查 `fourcc` 是否为灰度格式（Grayscale Format）。

<a id="r_gae46d2e9dc794ebb59e2809187754f978"></a>

```c
#define VIDEO_FMT_IS_BAYER(pixfmt)
```

相关声明：[VIDEO_FMT_IS_BAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gae46d2e9dc794ebb59e2809187754f978)。

检查 `fourcc` 是否为拜耳格式（Bayer Format）。

<a id="r_gae95d61e79e7a102eedba629e4d26cf5d"></a>

```c
#define VIDEO_FMT_IS_RGB(pixfmt)
```

相关声明：[VIDEO_FMT_IS_RGB](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gae95d61e79e7a102eedba629e4d26cf5d)。

检查 `fourcc` 是否为 RGB 格式，不含拜耳格式（Bayer）。

<a id="r_ga3bac0f45c04fea1d141b65a1d7edb267"></a>

```c
#define VIDEO_FMT_IS_YUV(pixfmt)
```

相关声明：[VIDEO_FMT_IS_YUV](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga3bac0f45c04fea1d141b65a1d7edb267)。

检查 `fourcc` 是否为 YUV 格式。

<a id="r_ga81623ba4831653e1805018ec822f2ef1"></a>

```c
#define VIDEO_FMT_IS_MIPI_PACKED(pixfmt)
```

相关声明：[VIDEO_FMT_IS_MIPI_PACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga81623ba4831653e1805018ec822f2ef1)。

检查 `fourcc` 是否为任一种 MIPI 打包格式（MIPI-packed Format）。

<a id="r_gafdb3d79c7df1881b3946260e191e3cad"></a>

```c
#define VIDEO_FMT_IS_PADDED(pixfmt)
```

相关声明：[VIDEO_FMT_IS_PADDED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafdb3d79c7df1881b3946260e191e3cad)。

检查 `fourcc` 是否为任一种 MIPI 打包格式（MIPI-packed Format）。

<a id="r_ga236286b6c75a3dac10f7d82347dfdd9b"></a>

```c
#define VIDEO_FMT_IS_SEMI_PLANAR(pixfmt)
```

相关声明：[VIDEO_FMT_IS_SEMI_PLANAR](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga236286b6c75a3dac10f7d82347dfdd9b)。

检查 `fourcc` 是否为任一种半平面格式（Semi-planar Format）。

<a id="r_ga5fe20fff04af51e514eebc07bed44745"></a>

```c
#define VIDEO_FMT_IS_FULL_PLANAR(pixfmt)
```

相关声明：[VIDEO_FMT_IS_FULL_PLANAR](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga5fe20fff04af51e514eebc07bed44745)。

检查 `fourcc` 是否为任一种全平面格式（Full-planar Format）。

<a id="define-members-0"></a>

### 拜耳格式：R、G、B 通道（Bayer Formats）

完整的颜色信息（Color Information）分布在多个像素中。

当格式的每像素位数超过 8 位时，就需要一种将这些位打包到多个字节中的策略（Packing Strategy），各格式的示意中对此进行了说明。

`R`、`r`、`G`、`g`、`B`、`b` 上方的数字用于提示其后各位所属的像素编号（Pixel Number）。

<a id="r_gacaf01a28e346128216eaaec08591403b"></a>

```c
#define VIDEO_FOREACH_BAYER(X, ...)
```

相关声明：[VIDEO_FOREACH_BAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gacaf01a28e346128216eaaec08591403b)。

针对每种拜耳格式（Bayer Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_gaec20e32bf0da102bafc033ac2e48b8b5"></a>

```c
#define VIDEO_FOREACH_BAYER_PADDED(X, ...)
```

相关声明：[VIDEO_FOREACH_BAYER_PADDED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaec20e32bf0da102bafc033ac2e48b8b5)。

针对每种填充拜耳格式（Bayer Padded Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_gabb167fd4b58db338de823dc285e62342"></a>

```c
#define VIDEO_PIX_FMT_SBGGR8P16 VIDEO_FOURCC('p', 'B', '8', '2')
```

相关声明：[VIDEO_PIX_FMT_SBGGR8P16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabb167fd4b58db338de823dc285e62342)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

8 位拜耳格式（Bayer Format），拆成两个各 4 位且均以零填充的数据块，采用小端序（Little Endian）。

<a id="r_ga07b22957c7fdc64fd3089fbcb811d599"></a>

```c
#define VIDEO_PIX_FMT_SGBRG8P16 VIDEO_FOURCC('p', 'G', '8', '2')
```

相关声明：[VIDEO_PIX_FMT_SGBRG8P16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga07b22957c7fdc64fd3089fbcb811d599)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

8 位拜耳格式（Bayer Format），拆成两个各 4 位且均以零填充的数据块，采用小端序（Little Endian）。

<a id="r_ga4df33d1a41c2dbdc16c19113be13760b"></a>

```c
#define VIDEO_PIX_FMT_SGRBG8P16 VIDEO_FOURCC('p', 'g', '8', '2')
```

相关声明：[VIDEO_PIX_FMT_SGRBG8P16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga4df33d1a41c2dbdc16c19113be13760b)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

8 位拜耳格式（Bayer Format），拆成两个各 4 位且均以零填充的数据块，采用小端序（Little Endian）。

<a id="r_gab471cd15aa874a5deadf7b54b826a90e"></a>

```c
#define VIDEO_PIX_FMT_SRGGB8P16 VIDEO_FOURCC('p', 'R', '8', '2')
```

相关声明：[VIDEO_PIX_FMT_SRGGB8P16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gab471cd15aa874a5deadf7b54b826a90e)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

8 位拜耳格式（Bayer Format），拆成两个各 4 位且均以零填充的数据块，采用小端序（Little Endian）。

<a id="r_ga22517dda8497ba924ba8bffeaad0c67c"></a>

```c
#define VIDEO_FOREACH_BAYER_MIPI_PACKED(X, ...)
```

相关声明：[VIDEO_FOREACH_BAYER_MIPI_PACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga22517dda8497ba924ba8bffeaad0c67c)。

针对每种MIPI 打包拜耳格式（Bayer MIPI-packed Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_ga3751a8dce1c7459df06f83cd09449b5d"></a>

```c
#define VIDEO_PIX_FMT_SBGGR10P VIDEO_FOURCC('p', 'B', 'A', 'A')
```

相关声明：[VIDEO_PIX_FMT_SBGGR10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga3751a8dce1c7459df06f83cd09449b5d)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gad69ab9041428488051bdb45f42ad4271"></a>

```c
#define VIDEO_PIX_FMT_SGBRG10P VIDEO_FOURCC('p', 'G', 'A', 'A')
```

相关声明：[VIDEO_PIX_FMT_SGBRG10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gad69ab9041428488051bdb45f42ad4271)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gaa28c6306a3ed44a0e50c16e0eac86688"></a>

```c
#define VIDEO_PIX_FMT_SGRBG10P VIDEO_FOURCC('p', 'g', 'A', 'A')
```

相关声明：[VIDEO_PIX_FMT_SGRBG10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa28c6306a3ed44a0e50c16e0eac86688)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga604d2f3501407546aa924e2fdb37be2f"></a>

```c
#define VIDEO_PIX_FMT_SRGGB10P VIDEO_FOURCC('p', 'R', 'A', 'A')
```

相关声明：[VIDEO_PIX_FMT_SRGGB10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga604d2f3501407546aa924e2fdb37be2f)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gab5b5375f050d039e05032c77ac838b31"></a>

```c
#define VIDEO_PIX_FMT_SBGGR12P VIDEO_FOURCC('p', 'B', 'C', 'C')
```

相关声明：[VIDEO_PIX_FMT_SBGGR12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gab5b5375f050d039e05032c77ac838b31)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gaecedece3398a6e2f62c20c2eb3f6d3c2"></a>

```c
#define VIDEO_PIX_FMT_SGBRG12P VIDEO_FOURCC('p', 'G', 'C', 'C')
```

相关声明：[VIDEO_PIX_FMT_SGBRG12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaecedece3398a6e2f62c20c2eb3f6d3c2)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga02d91ebf4b5150d5fa437bb3a7a6e872"></a>

```c
#define VIDEO_PIX_FMT_SGRBG12P VIDEO_FOURCC('p', 'g', 'C', 'C')
```

相关声明：[VIDEO_PIX_FMT_SGRBG12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga02d91ebf4b5150d5fa437bb3a7a6e872)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga348c15cc77c728fdac773d58341cbc1d"></a>

```c
#define VIDEO_PIX_FMT_SRGGB12P VIDEO_FOURCC('p', 'R', 'C', 'C')
```

相关声明：[VIDEO_PIX_FMT_SRGGB12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga348c15cc77c728fdac773d58341cbc1d)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gac3413c36b3ce91e5658cd0f973c1f3d7"></a>

```c
#define VIDEO_PIX_FMT_SBGGR14P VIDEO_FOURCC('p', 'B', 'E', 'E')
```

相关声明：[VIDEO_PIX_FMT_SBGGR14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gac3413c36b3ce91e5658cd0f973c1f3d7)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga89eb47d1dd60794781ee91cb5ae199ad"></a>

```c
#define VIDEO_PIX_FMT_SGBRG14P VIDEO_FOURCC('p', 'G', 'E', 'E')
```

相关声明：[VIDEO_PIX_FMT_SGBRG14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga89eb47d1dd60794781ee91cb5ae199ad)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gae06f742e31a62295d3ee16af8eec1b06"></a>

```c
#define VIDEO_PIX_FMT_SGRBG14P VIDEO_FOURCC('p', 'g', 'E', 'E')
```

相关声明：[VIDEO_PIX_FMT_SGRBG14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gae06f742e31a62295d3ee16af8eec1b06)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga66646a639518285810335a70337277d7"></a>

```c
#define VIDEO_PIX_FMT_SRGGB14P VIDEO_FOURCC('p', 'R', 'E', 'E')
```

相关声明：[VIDEO_PIX_FMT_SRGGB14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga66646a639518285810335a70337277d7)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga275ba44fc86f0916a9b2a9f7915c0cfe"></a>

```c
#define VIDEO_FOREACH_BAYER_NON_PACKED(X, ...)
```

相关声明：[VIDEO_FOREACH_BAYER_NON_PACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga275ba44fc86f0916a9b2a9f7915c0cfe)。

针对每种非打包拜耳格式（Bayer Non-packed Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_gabc0205ce5c6426051fdec88d92f123e3"></a>

```c
#define VIDEO_PIX_FMT_SBGGR8 VIDEO_FOURCC('B', 'A', '8', '1')
```

相关声明：[VIDEO_PIX_FMT_SBGGR8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabc0205ce5c6426051fdec88d92f123e3)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gaa9edb9c562fc3c86b61e071970fae60d"></a>

```c
#define VIDEO_PIX_FMT_SGBRG8 VIDEO_FOURCC('G', 'B', 'R', 'G')
```

相关声明：[VIDEO_PIX_FMT_SGBRG8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa9edb9c562fc3c86b61e071970fae60d)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga19d8dc905695229097dffe659f2a806e"></a>

```c
#define VIDEO_PIX_FMT_SGRBG8 VIDEO_FOURCC('G', 'R', 'B', 'G')
```

相关声明：[VIDEO_PIX_FMT_SGRBG8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga19d8dc905695229097dffe659f2a806e)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gabf0dde810e75d37823891ed03811482c"></a>

```c
#define VIDEO_PIX_FMT_SRGGB8 VIDEO_FOURCC('R', 'G', 'G', 'B')
```

相关声明：[VIDEO_PIX_FMT_SRGGB8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabf0dde810e75d37823891ed03811482c)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga0b55190a343fe891bdbb7b148e7feeae"></a>

```c
#define VIDEO_PIX_FMT_SBGGR10 VIDEO_FOURCC('B', 'G', '1', '0')
```

相关声明：[VIDEO_PIX_FMT_SBGGR10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga0b55190a343fe891bdbb7b148e7feeae)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga8e0f47c16483b14b45a593e9e542a987"></a>

```c
#define VIDEO_PIX_FMT_SGBRG10 VIDEO_FOURCC('G', 'B', '1', '0')
```

相关声明：[VIDEO_PIX_FMT_SGBRG10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga8e0f47c16483b14b45a593e9e542a987)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga011cc337bc54480d1e11c3e6833ae398"></a>

```c
#define VIDEO_PIX_FMT_SGRBG10 VIDEO_FOURCC('B', 'A', '1', '0')
```

相关声明：[VIDEO_PIX_FMT_SGRBG10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga011cc337bc54480d1e11c3e6833ae398)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga249cbf808658dab777a705fd9deb2986"></a>

```c
#define VIDEO_PIX_FMT_SRGGB10 VIDEO_FOURCC('R', 'G', '1', '0')
```

相关声明：[VIDEO_PIX_FMT_SRGGB10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga249cbf808658dab777a705fd9deb2986)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gaa2d7712f655dfcb3c74b4f4ec9941402"></a>

```c
#define VIDEO_PIX_FMT_SBGGR12 VIDEO_FOURCC('B', 'G', '1', '2')
```

相关声明：[VIDEO_PIX_FMT_SBGGR12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa2d7712f655dfcb3c74b4f4ec9941402)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gaa3df9d0af327e609b25e050a4362c2e2"></a>

```c
#define VIDEO_PIX_FMT_SGBRG12 VIDEO_FOURCC('G', 'B', '1', '2')
```

相关声明：[VIDEO_PIX_FMT_SGBRG12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa3df9d0af327e609b25e050a4362c2e2)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gaf18e6647596613e07ec3c651574b08ba"></a>

```c
#define VIDEO_PIX_FMT_SGRBG12 VIDEO_FOURCC('B', 'A', '1', '2')
```

相关声明：[VIDEO_PIX_FMT_SGRBG12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaf18e6647596613e07ec3c651574b08ba)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga7b167f2b6a147d325a685825274cd2f2"></a>

```c
#define VIDEO_PIX_FMT_SRGGB12 VIDEO_FOURCC('R', 'G', '1', '2')
```

相关声明：[VIDEO_PIX_FMT_SRGGB12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga7b167f2b6a147d325a685825274cd2f2)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga403f40a7e15319365c6ca8f3f5f19d21"></a>

```c
#define VIDEO_PIX_FMT_SBGGR14 VIDEO_FOURCC('B', 'G', '1', '4')
```

相关声明：[VIDEO_PIX_FMT_SBGGR14](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga403f40a7e15319365c6ca8f3f5f19d21)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga6c98a7066d7d3bdd8fce3d3651772153"></a>

```c
#define VIDEO_PIX_FMT_SGBRG14 VIDEO_FOURCC('G', 'B', '1', '4')
```

相关声明：[VIDEO_PIX_FMT_SGBRG14](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga6c98a7066d7d3bdd8fce3d3651772153)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gaf58481956952b13b071b1a68541b9c21"></a>

```c
#define VIDEO_PIX_FMT_SGRBG14 VIDEO_FOURCC('G', 'R', '1', '4')
```

相关声明：[VIDEO_PIX_FMT_SGRBG14](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaf58481956952b13b071b1a68541b9c21)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gaa6e4c240372e53db8ea3472cc456af58"></a>

```c
#define VIDEO_PIX_FMT_SRGGB14 VIDEO_FOURCC('R', 'G', '1', '4')
```

相关声明：[VIDEO_PIX_FMT_SRGGB14](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa6e4c240372e53db8ea3472cc456af58)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gae096669643176203199270317dc3449d"></a>

```c
#define VIDEO_PIX_FMT_SBGGR16 VIDEO_FOURCC('B', 'Y', 'R', '2')
```

相关声明：[VIDEO_PIX_FMT_SBGGR16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gae096669643176203199270317dc3449d)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga7f00eb633dd312ea89097edc82dc8f0c"></a>

```c
#define VIDEO_PIX_FMT_SGBRG16 VIDEO_FOURCC('G', 'B', '1', '6')
```

相关声明：[VIDEO_PIX_FMT_SGBRG16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga7f00eb633dd312ea89097edc82dc8f0c)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga4269984ce806e64ba5ccd41c1429769a"></a>

```c
#define VIDEO_PIX_FMT_SGRBG16 VIDEO_FOURCC('G', 'R', '1', '6')
```

相关声明：[VIDEO_PIX_FMT_SGRBG16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga4269984ce806e64ba5ccd41c1429769a)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga4f31b5d397868e952d53022c6c8e5823"></a>

```c
#define VIDEO_PIX_FMT_SRGGB16 VIDEO_FOURCC('R', 'G', '1', '6')
```

相关声明：[VIDEO_PIX_FMT_SRGGB16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga4f31b5d397868e952d53022c6c8e5823)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="define-members-1"></a>

### 灰度格式（Grayscale Formats）

仅包含亮度通道（Luminance Channel，Y），具有不同的位深度（Bit Depth）和打包方式（Packing）。

当格式的每像素位数超过 8 位时，就需要一种将这些位打包到多个字节中的策略（Packing Strategy），各格式的示意中对此进行了说明。

`Y`、`y` 上方的数字用于提示其后各位所属的像素编号（Pixel Number）。

<a id="r_ga2cc6468e655d039ba07f624b032d3765"></a>

```c
#define VIDEO_FOREACH_GRAYSCALE(X, ...)
```

相关声明：[VIDEO_FOREACH_GRAYSCALE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga2cc6468e655d039ba07f624b032d3765)。

针对每种灰度格式（Grayscale Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_ga5e694f4181c9f861a1f9603075e20ceb"></a>

```c
#define VIDEO_FOREACH_GRAYSCALE_NON_PACKED(X, ...)
```

相关声明：[VIDEO_FOREACH_GRAYSCALE_NON_PACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga5e694f4181c9f861a1f9603075e20ceb)。

针对每种非打包灰度格式（Grayscale Non-packed Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_gaa3af19adaf282b83a6c16f265a4260dc"></a>

```c
#define VIDEO_PIX_FMT_GREY VIDEO_FOURCC('G', 'R', 'E', 'Y')
```

相关声明：[VIDEO_PIX_FMT_GREY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa3af19adaf282b83a6c16f265a4260dc)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

与 Y8 相同，即仅含 8 位亮度（Luma-only），使用标准 FOURCC 命名；在某些图形库中称为 L8。

<a id="r_ga0506f2c8aa1a82f02fc9383d99b43bc3"></a>

```c
#define VIDEO_PIX_FMT_Y10 VIDEO_FOURCC('Y', '1', '0', ' ')
```

相关声明：[VIDEO_PIX_FMT_Y10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga0506f2c8aa1a82f02fc9383d99b43bc3)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

采用小端序（Little Endian），最高 6 位设为零。

<a id="r_ga166b2144cec4b4f92fadda30e81b7d22"></a>

```c
#define VIDEO_PIX_FMT_Y12 VIDEO_FOURCC('Y', '1', '2', ' ')
```

相关声明：[VIDEO_PIX_FMT_Y12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga166b2144cec4b4f92fadda30e81b7d22)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

采用小端序（Little Endian），最高 4 位设为零。

<a id="r_ga7d9379f19abcbac17bad3d6359a42d9d"></a>

```c
#define VIDEO_PIX_FMT_Y14 VIDEO_FOURCC('Y', '1', '4', ' ')
```

相关声明：[VIDEO_PIX_FMT_Y14](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga7d9379f19abcbac17bad3d6359a42d9d)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

采用小端序（Little Endian），最高 2 位设为零。

<a id="r_gaa65fe8bd917dd2fe95fa87530fc3055f"></a>

```c
#define VIDEO_PIX_FMT_Y16 VIDEO_FOURCC('Y', '1', '6', ' ')
```

相关声明：[VIDEO_PIX_FMT_Y16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa65fe8bd917dd2fe95fa87530fc3055f)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

小端序（Little Endian）。

<a id="r_ga1580b8c54fa57958ebfb573a4a138b9c"></a>

```c
#define VIDEO_FOREACH_GRAYSCALE_PADDED(X, ...)
```

相关声明：[VIDEO_FOREACH_GRAYSCALE_PADDED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga1580b8c54fa57958ebfb573a4a138b9c)。

针对每种填充灰度格式（Grayscale Padded Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_gad40f2d8628a39f0d87d5f0a337d7f8c4"></a>

```c
#define VIDEO_PIX_FMT_Y8P16 VIDEO_FOURCC('Y', '8', 'P', '2')
```

相关声明：[VIDEO_PIX_FMT_Y8P16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gad40f2d8628a39f0d87d5f0a337d7f8c4)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

仅含 8 位亮度（Luma-only），拆成两个各 4 位且均以零填充的数据块，采用小端序（Little Endian）。

<a id="r_ga4580c65a689a43878c18e0dc985e52f5"></a>

```c
#define VIDEO_FOREACH_GRAYSCALE_MIPI_PACKED(X, ...)
```

相关声明：[VIDEO_FOREACH_GRAYSCALE_MIPI_PACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga4580c65a689a43878c18e0dc985e52f5)。

针对每种MIPI 打包灰度格式（Grayscale MIPI-packed Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_ga502df4612995fc39e03d6de3ec675159"></a>

```c
#define VIDEO_PIX_FMT_Y10P VIDEO_FOURCC('Y', '1', '0', 'P')
```

相关声明：[VIDEO_PIX_FMT_Y10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga502df4612995fc39e03d6de3ec675159)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga263e6553a77d00bc509c1b270efebb0b"></a>

```c
#define VIDEO_PIX_FMT_Y12P VIDEO_FOURCC('Y', '1', '2', 'P')
```

相关声明：[VIDEO_PIX_FMT_Y12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga263e6553a77d00bc509c1b270efebb0b)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gada0124aad9c10d403966b1e3851cd968"></a>

```c
#define VIDEO_PIX_FMT_Y14P VIDEO_FOURCC('Y', '1', '4', 'P')
```

相关声明：[VIDEO_PIX_FMT_Y14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gada0124aad9c10d403966b1e3851cd968)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="define-members-2"></a>

### RGB 格式（RGB Formats）

各颜色通道（Per-color Channels）：R、G、B。

<a id="r_ga8f1ce8a81f2aea6386a5168c9e1ed939"></a>

```c
#define VIDEO_FOREACH_RGB(X, ...)
```

相关声明：[VIDEO_FOREACH_RGB](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga8f1ce8a81f2aea6386a5168c9e1ed939)。

针对每种RGB 格式（RGB Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_gadec2c5cf7e59f4092eef6930580d93f0"></a>

```c
#define VIDEO_FOREACH_RGB_PACKED(X, ...)
```

相关声明：[VIDEO_FOREACH_RGB_PACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gadec2c5cf7e59f4092eef6930580d93f0)。

针对每种打包 RGB 格式（RGB Packed Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_gaf3830004bb857fa00a14d0a1209c61a8"></a>

```c
#define VIDEO_PIX_FMT_RGB565X VIDEO_FOURCC('R', 'G', 'B', 'R')
```

相关声明：[VIDEO_PIX_FMT_RGB565X](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaf3830004bb857fa00a14d0a1209c61a8)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

5 位红色（Red）位于 `[15:11]`，6 位绿色（Green）位于 `[10:5]`，5 位蓝色（Blue）位于 `[4:0]`。

<a id="r_gaf009d0eb7dbdb3bfd8883da03478c1ec"></a>

```c
#define VIDEO_PIX_FMT_RGB565 VIDEO_FOURCC('R', 'G', 'B', 'P')
```

相关声明：[VIDEO_PIX_FMT_RGB565](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaf009d0eb7dbdb3bfd8883da03478c1ec)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

5 位红色（Red）位于 `[15:11]`，6 位绿色（Green）位于 `[10:5]`，5 位蓝色（Blue）位于 `[4:0]`。

<a id="r_gaf667895d82c3dd5b6a4ec8e9e98dbd0a"></a>

```c
#define VIDEO_FOREACH_RGB_NON_PACKED(X, ...)
```

相关声明：[VIDEO_FOREACH_RGB_NON_PACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaf667895d82c3dd5b6a4ec8e9e98dbd0a)。

针对每种非打包 RGB 格式（RGB Non-packed Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_gaf1f8775bbdd0508c4e21a58dfcfc362d"></a>

```c
#define VIDEO_PIX_FMT_BGR24 VIDEO_FOURCC('B', 'G', 'R', '3')
```

相关声明：[VIDEO_PIX_FMT_BGR24](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaf1f8775bbdd0508c4e21a58dfcfc362d)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

24 位 RGB 格式，每个分量（Component）占 8 位。

<a id="r_ga03e6be04b23b9735c96231eebc687158"></a>

```c
#define VIDEO_PIX_FMT_RGB24 VIDEO_FOURCC('R', 'G', 'B', '3')
```

相关声明：[VIDEO_PIX_FMT_RGB24](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga03e6be04b23b9735c96231eebc687158)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

24 位 RGB 格式，每个分量（Component）占 8 位。

<a id="r_gacc88a5297ba55a0216e72de6fe087005"></a>

```c
#define VIDEO_FOREACH_RGB_ALPHA(X, ...)
```

相关声明：[VIDEO_FOREACH_RGB_ALPHA](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gacc88a5297ba55a0216e72de6fe087005)。

针对每种带透明度的 RGB 格式（RGB Alpha Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_ga5cd54fb54967a80576082cadd5941670"></a>

```c
#define VIDEO_PIX_FMT_ARGB32 VIDEO_FOURCC('B', 'A', '2', '4')
```

相关声明：[VIDEO_PIX_FMT_ARGB32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga5cd54fb54967a80576082cadd5941670)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

每个像素的第一个字节是透明度（Alpha，A）。

<a id="r_ga515e379bc7f59a8062f3e2a5980b0626"></a>

```c
#define VIDEO_PIX_FMT_BGRA32 VIDEO_FOURCC('A', 'R', '2', '4')
```

相关声明：[VIDEO_PIX_FMT_BGRA32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga515e379bc7f59a8062f3e2a5980b0626)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

每个像素的最后一个字节是透明度（Alpha，A）。

<a id="r_ga8ee1e3b82eeeb02188157aa4b4b5d842"></a>

```c
#define VIDEO_PIX_FMT_RGBA32 VIDEO_FOURCC('A', 'B', '2', '4')
```

相关声明：[VIDEO_PIX_FMT_RGBA32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga8ee1e3b82eeeb02188157aa4b4b5d842)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

每个像素的最后一个字节是透明度（Alpha，A）。

<a id="r_gaffb650a5f9b2b03890283ecfe95aee04"></a>

```c
#define VIDEO_PIX_FMT_ABGR32 VIDEO_FOURCC('R', 'A', '2', '4')
```

相关声明：[VIDEO_PIX_FMT_ABGR32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaffb650a5f9b2b03890283ecfe95aee04)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

每个像素的第一个字节是透明度（Alpha，A）。

<a id="r_ga34ee863f07f90bd14ccfe5b9c1058539"></a>

```c
#define VIDEO_FOREACH_RGB_PADDED(X, ...)
```

相关声明：[VIDEO_FOREACH_RGB_PADDED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga34ee863f07f90bd14ccfe5b9c1058539)。

针对每种填充 RGB 格式（RGB Padded Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_ga8be24c04210f8818d75082bd710db8b1"></a>

```c
#define VIDEO_PIX_FMT_XRGB32 VIDEO_FOURCC('B', 'X', '2', '4')
```

相关声明：[VIDEO_PIX_FMT_XRGB32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga8be24c04210f8818d75082bd710db8b1)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

每个像素的第一个字节为空（Empty，X）。

<a id="r_ga4ae1acc3d44a1698e0d48f299f061a49"></a>

```c
#define VIDEO_PIX_FMT_XBGR32 VIDEO_FOURCC('R', 'X', '2', '4')
```

相关声明：[VIDEO_PIX_FMT_XBGR32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga4ae1acc3d44a1698e0d48f299f061a49)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

每个像素的第一个字节为空（Empty，X）。

<a id="r_gadf53a84505c1299a5c97a0213c989103"></a>

```c
#define VIDEO_PIX_FMT_BGRX32 VIDEO_FOURCC('X', 'R', '2', '4')
```

相关声明：[VIDEO_PIX_FMT_BGRX32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gadf53a84505c1299a5c97a0213c989103)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

每个像素的最后一个字节为空（Empty，X）。

<a id="r_gadfdb271a780b10a29a356675014a25c2"></a>

```c
#define VIDEO_PIX_FMT_RGBX32 VIDEO_FOURCC('X', 'B', '2', '4')
```

相关声明：[VIDEO_PIX_FMT_RGBX32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gadfdb271a780b10a29a356675014a25c2)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

每个像素的最后一个字节为空（Empty，X）。

<a id="define-members-3"></a>

### YUV 格式（YUV Formats）

亮度通道（Luminance，Y）和色度通道（Chrominance，U、V）。

<a id="r_ga95b3d15b30a04e432543a250339cde93"></a>

```c
#define VIDEO_FOREACH_YUV(X, ...)
```

相关声明：[VIDEO_FOREACH_YUV](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga95b3d15b30a04e432543a250339cde93)。

针对每种YUV 格式（YUV Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_ga8de7c85dd4b32fa406aa121a3ee7f519"></a>

```c
#define VIDEO_FOREACH_YUV_NON_PLANAR(X, ...)
```

相关声明：[VIDEO_FOREACH_YUV_NON_PLANAR](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga8de7c85dd4b32fa406aa121a3ee7f519)。

针对每种非平面 YUV 格式（YUV Non-Planar Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_gad186d3166acec11c893ae57a0ae68f11"></a>

```c
#define VIDEO_PIX_FMT_YUYV VIDEO_FOURCC('Y', 'U', 'Y', 'V')
```

相关声明：[VIDEO_PIX_FMT_YUYV](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gad186d3166acec11c893ae57a0ae68f11)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

每个像素缺少一个通道（Channel），即 U 或 V。

<a id="r_ga299af047675a110c109cee954f55fca6"></a>

```c
#define VIDEO_PIX_FMT_YVYU VIDEO_FOURCC('Y', 'V', 'Y', 'U')
```

相关声明：[VIDEO_PIX_FMT_YVYU](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga299af047675a110c109cee954f55fca6)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga63c825ce5dc6c863d355195fde40acb1"></a>

```c
#define VIDEO_PIX_FMT_VYUY VIDEO_FOURCC('V', 'Y', 'U', 'Y')
```

相关声明：[VIDEO_PIX_FMT_VYUY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga63c825ce5dc6c863d355195fde40acb1)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gadca3ee56c798cf05b63cbfc87af98ce3"></a>

```c
#define VIDEO_PIX_FMT_UYVY VIDEO_FOURCC('U', 'Y', 'V', 'Y')
```

相关声明：[VIDEO_PIX_FMT_UYVY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gadca3ee56c798cf05b63cbfc87af98ce3)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga017bcbec587314f569d6d0e4fbdda351"></a>

```c
#define VIDEO_PIX_FMT_XYUV32 VIDEO_FOURCC('X', 'Y', 'U', 'V')
```

相关声明：[VIDEO_PIX_FMT_XYUV32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga017bcbec587314f569d6d0e4fbdda351)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

每个像素的第一个字节为空（Empty，X）。

<a id="r_gabcdd44434323cc0e0634e94f23f83146"></a>

```c
#define VIDEO_PIX_FMT_YUV24 VIDEO_FOURCC('Y', 'U', 'V', '3')
```

相关声明：[VIDEO_PIX_FMT_YUV24](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabcdd44434323cc0e0634e94f23f83146)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

24 位 YUV 格式，每个分量（Component）占 8 位。

<a id="r_gac7378ac0dcd5d2afeba4def9cab509f0"></a>

```c
#define VIDEO_FOREACH_YUV_SEMI_PLANAR(X, ...)
```

相关声明：[VIDEO_FOREACH_YUV_SEMI_PLANAR](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gac7378ac0dcd5d2afeba4def9cab509f0)。

针对每种半平面 YUV 格式（YUV Semi-Planar Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_ga6e5538e8f21a5be750eec38c2a16ad2f"></a>

```c
#define VIDEO_PIX_FMT_NV12 VIDEO_FOURCC('N', 'V', '1', '2')
```

相关声明：[VIDEO_PIX_FMT_NV12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga6e5538e8f21a5be750eec38c2a16ad2f)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

色度（Chroma，U/V）在水平和垂直方向均进行子采样（Subsampling）。

<a id="r_ga171cb239b78ca49b9232dcb9d5e9f43f"></a>

```c
#define VIDEO_PIX_FMT_NV21 VIDEO_FOURCC('N', 'V', '2', '1')
```

相关声明：[VIDEO_PIX_FMT_NV21](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga171cb239b78ca49b9232dcb9d5e9f43f)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

色度（Chroma，U/V）在水平和垂直方向均进行子采样（Subsampling）。

<a id="r_gabbfecc5e0c2c4115c57d4772eaa4918f"></a>

```c
#define VIDEO_PIX_FMT_NV16 VIDEO_FOURCC('N', 'V', '1', '6')
```

相关声明：[VIDEO_PIX_FMT_NV16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabbfecc5e0c2c4115c57d4772eaa4918f)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

色度（Chroma，U/V）在水平方向进行子采样（Subsampling）。

<a id="r_ga3463a33faa910f98280c96f40d3c65e7"></a>

```c
#define VIDEO_PIX_FMT_NV61 VIDEO_FOURCC('N', 'V', '6', '1')
```

相关声明：[VIDEO_PIX_FMT_NV61](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga3463a33faa910f98280c96f40d3c65e7)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

色度（Chroma，U/V）在水平方向进行子采样（Subsampling）。

<a id="r_ga06864b3b1b7d563a9cd2f15c33cdd2d8"></a>

```c
#define VIDEO_PIX_FMT_NV24 VIDEO_FOURCC('N', 'V', '2', '4')
```

相关声明：[VIDEO_PIX_FMT_NV24](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga06864b3b1b7d563a9cd2f15c33cdd2d8)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

色度（Chroma，U/V）不进行子采样（Subsampling）。

<a id="r_gace39ba88d298b1991412f73fb4fe9d18"></a>

```c
#define VIDEO_PIX_FMT_NV42 VIDEO_FOURCC('N', 'V', '4', '2')
```

相关声明：[VIDEO_PIX_FMT_NV42](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gace39ba88d298b1991412f73fb4fe9d18)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

色度（Chroma，U/V）不进行子采样（Subsampling）。

<a id="r_gac71db00c78d16191a6d613ca190a9ede"></a>

```c
#define VIDEO_FOREACH_YUV_FULL_PLANAR(X, ...)
```

相关声明：[VIDEO_FOREACH_YUV_FULL_PLANAR](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gac71db00c78d16191a6d613ca190a9ede)。

针对每种全平面 YUV 格式（YUV Full-Planar Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_ga9054aa564afdf3b6129539fbda30d9bf"></a>

```c
#define VIDEO_PIX_FMT_YUV420 VIDEO_FOURCC('Y', 'U', '1', '2')
```

相关声明：[VIDEO_PIX_FMT_YUV420](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga9054aa564afdf3b6129539fbda30d9bf)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

色度（Chroma，U/V）在水平和垂直方向均进行子采样（Subsampling）。

<a id="r_ga9294d7e95c9fe00df93248958b7bef0e"></a>

```c
#define VIDEO_PIX_FMT_YVU420 VIDEO_FOURCC('Y', 'V', '1', '2')
```

相关声明：[VIDEO_PIX_FMT_YVU420](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga9294d7e95c9fe00df93248958b7bef0e)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

色度（Chroma，U/V）在水平和垂直方向均进行子采样（Subsampling）。

<a id="define-members-4"></a>

### 压缩格式（Compressed Formats）

<a id="r_ga2b2310e1eee22f0e4c28d870e251ecc7"></a>

```c
#define VIDEO_FOREACH_COMPRESSED(X, ...)
```

相关声明：[VIDEO_FOREACH_COMPRESSED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga2b2310e1eee22f0e4c28d870e251ecc7)。

针对每种压缩格式（Compressed Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_ga035a13c38c4f123411547e2c40d58bd2"></a>

```c
#define VIDEO_PIX_FMT_JPEG VIDEO_FOURCC('J', 'P', 'E', 'G')
```

相关声明：[VIDEO_PIX_FMT_JPEG](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga035a13c38c4f123411547e2c40d58bd2)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

同时涵盖 JPEG 单帧格式，以及动态 JPEG（Motion-JPEG，MJPEG），后者由多个 JPEG 帧连接而成。

<a id="r_ga2f66735e0f52991abfc3188ff2c4310c"></a>

```c
#define VIDEO_PIX_FMT_H264 VIDEO_FOURCC('H', '2', '6', '4')
```

相关声明：[VIDEO_PIX_FMT_H264](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga2f66735e0f52991abfc3188ff2c4310c)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

带起始码（Start Code）的 H264。

<a id="r_ga8056c592a7794552c3e44531c643b7de"></a>

```c
#define VIDEO_PIX_FMT_H264_NO_SC VIDEO_FOURCC('A', 'V', 'C', '1')
```

相关声明：[VIDEO_PIX_FMT_H264_NO_SC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga8056c592a7794552c3e44531c643b7de)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

不带起始码（Start Code）的 H264。

<a id="r_gabb1779dc232fa3d1915ced0088df5f27"></a>

```c
#define VIDEO_PIX_FMT_PNG VIDEO_FOURCC('P', 'N', 'G', ' ')
```

相关声明：[VIDEO_PIX_FMT_PNG](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabb1779dc232fa3d1915ced0088df5f27)、[VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)。

PNG。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.2\_函数（Functions）

<a id="r_gabdbd1b0f40af6663d81402deefdd387f"></a>

```c
static unsigned int video_bits_per_pixel (uint32_t pixfmt)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[video_bits_per_pixel](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabdbd1b0f40af6663d81402deefdd387f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取像素格式的每像素位数（Bits per Pixel）。


## 4.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P073_formats.h_源码浏览.md)
- [VIDEO_FOURCC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafb9e36597c39face52cd0c010df20951)
- [VIDEO_FOURCC_FROM_STR](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafc6c4cb871f15464f2b7df86d91fd8f3)
- [VIDEO_FOURCC_TO_STR](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gacd3805f57633c3db8c6adcd87384bd5c)
- [VIDEO_FMT_IS_GRAYSCALE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga7793e9ac7b592429b0dac4da4ead3674)
- [VIDEO_FMT_IS_BAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gae46d2e9dc794ebb59e2809187754f978)
- [VIDEO_FMT_IS_RGB](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gae95d61e79e7a102eedba629e4d26cf5d)
- [VIDEO_FMT_IS_YUV](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga3bac0f45c04fea1d141b65a1d7edb267)
- [VIDEO_FMT_IS_MIPI_PACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga81623ba4831653e1805018ec822f2ef1)
- [VIDEO_FMT_IS_PADDED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gafdb3d79c7df1881b3946260e191e3cad)
- [VIDEO_FMT_IS_SEMI_PLANAR](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga236286b6c75a3dac10f7d82347dfdd9b)
- [VIDEO_FMT_IS_FULL_PLANAR](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga5fe20fff04af51e514eebc07bed44745)
- [VIDEO_FOREACH_BAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gacaf01a28e346128216eaaec08591403b)
- [VIDEO_FOREACH_BAYER_PADDED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaec20e32bf0da102bafc033ac2e48b8b5)
- [VIDEO_PIX_FMT_SBGGR8P16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabb167fd4b58db338de823dc285e62342)
- [VIDEO_PIX_FMT_SGBRG8P16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga07b22957c7fdc64fd3089fbcb811d599)
- [VIDEO_PIX_FMT_SGRBG8P16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga4df33d1a41c2dbdc16c19113be13760b)
- [VIDEO_PIX_FMT_SRGGB8P16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gab471cd15aa874a5deadf7b54b826a90e)
- [VIDEO_FOREACH_BAYER_MIPI_PACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga22517dda8497ba924ba8bffeaad0c67c)
- [VIDEO_PIX_FMT_SBGGR10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga3751a8dce1c7459df06f83cd09449b5d)
- [VIDEO_PIX_FMT_SGBRG10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gad69ab9041428488051bdb45f42ad4271)
- [VIDEO_PIX_FMT_SGRBG10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa28c6306a3ed44a0e50c16e0eac86688)
- [VIDEO_PIX_FMT_SRGGB10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga604d2f3501407546aa924e2fdb37be2f)
- [VIDEO_PIX_FMT_SBGGR12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gab5b5375f050d039e05032c77ac838b31)
- [VIDEO_PIX_FMT_SGBRG12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaecedece3398a6e2f62c20c2eb3f6d3c2)
- [VIDEO_PIX_FMT_SGRBG12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga02d91ebf4b5150d5fa437bb3a7a6e872)
- [VIDEO_PIX_FMT_SRGGB12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga348c15cc77c728fdac773d58341cbc1d)
- [VIDEO_PIX_FMT_SBGGR14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gac3413c36b3ce91e5658cd0f973c1f3d7)
- [VIDEO_PIX_FMT_SGBRG14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga89eb47d1dd60794781ee91cb5ae199ad)
- [VIDEO_PIX_FMT_SGRBG14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gae06f742e31a62295d3ee16af8eec1b06)
- [VIDEO_PIX_FMT_SRGGB14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga66646a639518285810335a70337277d7)
- [VIDEO_FOREACH_BAYER_NON_PACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga275ba44fc86f0916a9b2a9f7915c0cfe)
- [VIDEO_PIX_FMT_SBGGR8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabc0205ce5c6426051fdec88d92f123e3)
- [VIDEO_PIX_FMT_SGBRG8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa9edb9c562fc3c86b61e071970fae60d)
- [VIDEO_PIX_FMT_SGRBG8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga19d8dc905695229097dffe659f2a806e)
- [VIDEO_PIX_FMT_SRGGB8](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabf0dde810e75d37823891ed03811482c)
- [VIDEO_PIX_FMT_SBGGR10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga0b55190a343fe891bdbb7b148e7feeae)
- [VIDEO_PIX_FMT_SGBRG10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga8e0f47c16483b14b45a593e9e542a987)
- [VIDEO_PIX_FMT_SGRBG10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga011cc337bc54480d1e11c3e6833ae398)
- [VIDEO_PIX_FMT_SRGGB10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga249cbf808658dab777a705fd9deb2986)
- [VIDEO_PIX_FMT_SBGGR12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa2d7712f655dfcb3c74b4f4ec9941402)
- [VIDEO_PIX_FMT_SGBRG12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa3df9d0af327e609b25e050a4362c2e2)
- [VIDEO_PIX_FMT_SGRBG12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaf18e6647596613e07ec3c651574b08ba)
- [VIDEO_PIX_FMT_SRGGB12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga7b167f2b6a147d325a685825274cd2f2)
- [VIDEO_PIX_FMT_SBGGR14](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga403f40a7e15319365c6ca8f3f5f19d21)
- [VIDEO_PIX_FMT_SGBRG14](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga6c98a7066d7d3bdd8fce3d3651772153)
- [VIDEO_PIX_FMT_SGRBG14](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaf58481956952b13b071b1a68541b9c21)
- [VIDEO_PIX_FMT_SRGGB14](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa6e4c240372e53db8ea3472cc456af58)
- [VIDEO_PIX_FMT_SBGGR16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gae096669643176203199270317dc3449d)
- [VIDEO_PIX_FMT_SGBRG16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga7f00eb633dd312ea89097edc82dc8f0c)
- [VIDEO_PIX_FMT_SGRBG16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga4269984ce806e64ba5ccd41c1429769a)
- [VIDEO_PIX_FMT_SRGGB16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga4f31b5d397868e952d53022c6c8e5823)
- [VIDEO_FOREACH_GRAYSCALE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga2cc6468e655d039ba07f624b032d3765)
- [VIDEO_FOREACH_GRAYSCALE_NON_PACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga5e694f4181c9f861a1f9603075e20ceb)
- [VIDEO_PIX_FMT_GREY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa3af19adaf282b83a6c16f265a4260dc)
- [VIDEO_PIX_FMT_Y10](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga0506f2c8aa1a82f02fc9383d99b43bc3)
- [VIDEO_PIX_FMT_Y12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga166b2144cec4b4f92fadda30e81b7d22)
- [VIDEO_PIX_FMT_Y14](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga7d9379f19abcbac17bad3d6359a42d9d)
- [VIDEO_PIX_FMT_Y16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaa65fe8bd917dd2fe95fa87530fc3055f)
- [VIDEO_FOREACH_GRAYSCALE_PADDED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga1580b8c54fa57958ebfb573a4a138b9c)
- [VIDEO_PIX_FMT_Y8P16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gad40f2d8628a39f0d87d5f0a337d7f8c4)
- [VIDEO_FOREACH_GRAYSCALE_MIPI_PACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga4580c65a689a43878c18e0dc985e52f5)
- [VIDEO_PIX_FMT_Y10P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga502df4612995fc39e03d6de3ec675159)
- [VIDEO_PIX_FMT_Y12P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga263e6553a77d00bc509c1b270efebb0b)
- [VIDEO_PIX_FMT_Y14P](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gada0124aad9c10d403966b1e3851cd968)
- [VIDEO_FOREACH_RGB](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga8f1ce8a81f2aea6386a5168c9e1ed939)
- [VIDEO_FOREACH_RGB_PACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gadec2c5cf7e59f4092eef6930580d93f0)
- [VIDEO_PIX_FMT_RGB565X](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaf3830004bb857fa00a14d0a1209c61a8)
- [VIDEO_PIX_FMT_RGB565](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaf009d0eb7dbdb3bfd8883da03478c1ec)
- [VIDEO_FOREACH_RGB_NON_PACKED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaf667895d82c3dd5b6a4ec8e9e98dbd0a)
- [VIDEO_PIX_FMT_BGR24](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaf1f8775bbdd0508c4e21a58dfcfc362d)
- [VIDEO_PIX_FMT_RGB24](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga03e6be04b23b9735c96231eebc687158)
- [VIDEO_FOREACH_RGB_ALPHA](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gacc88a5297ba55a0216e72de6fe087005)
- [VIDEO_PIX_FMT_ARGB32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga5cd54fb54967a80576082cadd5941670)
- [VIDEO_PIX_FMT_BGRA32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga515e379bc7f59a8062f3e2a5980b0626)
- [VIDEO_PIX_FMT_RGBA32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga8ee1e3b82eeeb02188157aa4b4b5d842)
- [VIDEO_PIX_FMT_ABGR32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gaffb650a5f9b2b03890283ecfe95aee04)
- [VIDEO_FOREACH_RGB_PADDED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga34ee863f07f90bd14ccfe5b9c1058539)
- [VIDEO_PIX_FMT_XRGB32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga8be24c04210f8818d75082bd710db8b1)
- [VIDEO_PIX_FMT_XBGR32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga4ae1acc3d44a1698e0d48f299f061a49)
- [VIDEO_PIX_FMT_BGRX32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gadf53a84505c1299a5c97a0213c989103)
- [VIDEO_PIX_FMT_RGBX32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gadfdb271a780b10a29a356675014a25c2)
- [VIDEO_FOREACH_YUV](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga95b3d15b30a04e432543a250339cde93)
- [VIDEO_FOREACH_YUV_NON_PLANAR](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga8de7c85dd4b32fa406aa121a3ee7f519)
- [VIDEO_PIX_FMT_YUYV](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gad186d3166acec11c893ae57a0ae68f11)
- [VIDEO_PIX_FMT_YVYU](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga299af047675a110c109cee954f55fca6)
- [VIDEO_PIX_FMT_VYUY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga63c825ce5dc6c863d355195fde40acb1)
- [VIDEO_PIX_FMT_UYVY](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gadca3ee56c798cf05b63cbfc87af98ce3)
- [VIDEO_PIX_FMT_XYUV32](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga017bcbec587314f569d6d0e4fbdda351)
- [VIDEO_PIX_FMT_YUV24](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabcdd44434323cc0e0634e94f23f83146)
- [VIDEO_FOREACH_YUV_SEMI_PLANAR](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gac7378ac0dcd5d2afeba4def9cab509f0)
- [VIDEO_PIX_FMT_NV12](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga6e5538e8f21a5be750eec38c2a16ad2f)
- [VIDEO_PIX_FMT_NV21](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga171cb239b78ca49b9232dcb9d5e9f43f)
- [VIDEO_PIX_FMT_NV16](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabbfecc5e0c2c4115c57d4772eaa4918f)
- [VIDEO_PIX_FMT_NV61](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga3463a33faa910f98280c96f40d3c65e7)
- [VIDEO_PIX_FMT_NV24](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga06864b3b1b7d563a9cd2f15c33cdd2d8)
- [VIDEO_PIX_FMT_NV42](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gace39ba88d298b1991412f73fb4fe9d18)
- [VIDEO_FOREACH_YUV_FULL_PLANAR](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gac71db00c78d16191a6d613ca190a9ede)
- [VIDEO_PIX_FMT_YUV420](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga9054aa564afdf3b6129539fbda30d9bf)
- [VIDEO_PIX_FMT_YVU420](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga9294d7e95c9fe00df93248958b7bef0e)
- [VIDEO_FOREACH_COMPRESSED](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga2b2310e1eee22f0e4c28d870e251ecc7)
- [VIDEO_PIX_FMT_JPEG](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga035a13c38c4f123411547e2c40d58bd2)
- [VIDEO_PIX_FMT_H264](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga2f66735e0f52991abfc3188ff2c4310c)
- [VIDEO_PIX_FMT_H264_NO_SC](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#ga8056c592a7794552c3e44531c643b7de)
- [VIDEO_PIX_FMT_PNG](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabb1779dc232fa3d1915ced0088df5f27)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [video_bits_per_pixel](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html#gabdbd1b0f40af6663d81402deefdd387f)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>

---

[上一章](P003_zephyr__sys__fdtable.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__bluetooth__audio__mcc.h_文件参考.md)
