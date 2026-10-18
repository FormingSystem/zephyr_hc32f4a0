---
id: learning.zephyr-docs.api-flash-connection-topic-reference.page-11
title: 视频格式（Video Formats）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_视频格式（Video Formats）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__video__formats.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

视频像素格式定义。

<a id="details"></a>

视频像素格式定义（Video Pixel Format Definitions）。起始版本（Since）：4.4。接口版本（Version）：0.0.1。字符 `|` 用于分隔像素或逻辑块（Logical Block），空格用于分隔字节。大写字母表示最高有效位（Most Significant Bit），小写字母表示其余各位。

<a id="header-files"></a>
<a id="files"></a>

## 11.1\_文件（Files）

<a id="r_formats_2Eh"></a>

```c
file formats.h
```

相关声明：[formats.h](../api_file_media_sensor_reference/P004_zephyr__video__formats.h_文件参考.md)。

视频格式（Video Format）API的主头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.2\_宏定义（Macros）

<a id="r_gafb9e36597c39face52cd0c010df20951"></a>

```c
#define VIDEO_FOURCC(a, b, c, d)
```

相关声明：[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

唯一标识像素格式（Pixel Format）的四字符代码（Four-character-code，FOURCC）。

<a id="r_gafc6c4cb871f15464f2b7df86d91fd8f3"></a>

```c
#define VIDEO_FOURCC_FROM_STR(str)
```

相关声明：[VIDEO_FOURCC_FROM_STR](#gafc6c4cb871f15464f2b7df86d91fd8f3)。

将四字符字符串（Four-character-string）转换为四字符代码（FOURCC）。

<a id="r_gacd3805f57633c3db8c6adcd87384bd5c"></a>

```c
#define VIDEO_FOURCC_TO_STR(fourcc)
```

相关声明：[VIDEO_FOURCC_TO_STR](#gacd3805f57633c3db8c6adcd87384bd5c)。

将四字符代码（FOURCC）转换为四字符字符串（Four-character-string）。

<a id="r_ga7793e9ac7b592429b0dac4da4ead3674"></a>

```c
#define VIDEO_FMT_IS_GRAYSCALE(pixfmt)
```

相关声明：[VIDEO_FMT_IS_GRAYSCALE](#ga7793e9ac7b592429b0dac4da4ead3674)。

检查 `fourcc` 是否为灰度格式（Grayscale Format）。

<a id="r_gae46d2e9dc794ebb59e2809187754f978"></a>

```c
#define VIDEO_FMT_IS_BAYER(pixfmt)
```

相关声明：[VIDEO_FMT_IS_BAYER](#gae46d2e9dc794ebb59e2809187754f978)。

检查 `fourcc` 是否为拜耳格式（Bayer Format）。

<a id="r_gae95d61e79e7a102eedba629e4d26cf5d"></a>

```c
#define VIDEO_FMT_IS_RGB(pixfmt)
```

相关声明：[VIDEO_FMT_IS_RGB](#gae95d61e79e7a102eedba629e4d26cf5d)。

检查 `fourcc` 是否为 RGB 格式，不含拜耳格式（Bayer）。

<a id="r_ga3bac0f45c04fea1d141b65a1d7edb267"></a>

```c
#define VIDEO_FMT_IS_YUV(pixfmt)
```

相关声明：[VIDEO_FMT_IS_YUV](#ga3bac0f45c04fea1d141b65a1d7edb267)。

检查 `fourcc` 是否为 YUV 格式。

<a id="r_ga81623ba4831653e1805018ec822f2ef1"></a>

```c
#define VIDEO_FMT_IS_MIPI_PACKED(pixfmt)
```

相关声明：[VIDEO_FMT_IS_MIPI_PACKED](#ga81623ba4831653e1805018ec822f2ef1)。

检查 `fourcc` 是否为任一种 MIPI 打包格式（MIPI-packed Format）。

<a id="r_gafdb3d79c7df1881b3946260e191e3cad"></a>

```c
#define VIDEO_FMT_IS_PADDED(pixfmt)
```

相关声明：[VIDEO_FMT_IS_PADDED](#gafdb3d79c7df1881b3946260e191e3cad)。

检查 `fourcc` 是否为任一种 MIPI 打包格式（MIPI-packed Format）。

<a id="r_ga236286b6c75a3dac10f7d82347dfdd9b"></a>

```c
#define VIDEO_FMT_IS_SEMI_PLANAR(pixfmt)
```

相关声明：[VIDEO_FMT_IS_SEMI_PLANAR](#ga236286b6c75a3dac10f7d82347dfdd9b)。

检查 `fourcc` 是否为任一种半平面格式（Semi-planar Format）。

<a id="r_ga5fe20fff04af51e514eebc07bed44745"></a>

```c
#define VIDEO_FMT_IS_FULL_PLANAR(pixfmt)
```

相关声明：[VIDEO_FMT_IS_FULL_PLANAR](#ga5fe20fff04af51e514eebc07bed44745)。

检查 `fourcc` 是否为任一种全平面格式（Full-planar Format）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.3\_函数（Functions）

<a id="r_gabdbd1b0f40af6663d81402deefdd387f"></a>

```c
static unsigned int video_bits_per_pixel (uint32_t pixfmt)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[video_bits_per_pixel](#gabdbd1b0f40af6663d81402deefdd387f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

获取像素格式的每像素位数（Bits per Pixel）。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 11.4\_拜耳格式：R、G、B 通道（Bayer Formats）

完整的颜色信息（Color Information）分布在多个像素中。

当格式的每像素位数超过 8 位时，就需要一种将这些位打包到多个字节中的策略（Packing Strategy），各格式的示意中对此进行了说明。

`R`、`r`、`G`、`g`、`B`、`b` 上方的数字用于提示其后各位所属的像素编号（Pixel Number）。

<a id="r_gacaf01a28e346128216eaaec08591403b"></a>

```c
#define VIDEO_FOREACH_BAYER(X, ...)
```

相关声明：[VIDEO_FOREACH_BAYER](#gacaf01a28e346128216eaaec08591403b)。

针对每种拜耳格式（Bayer Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_gaec20e32bf0da102bafc033ac2e48b8b5"></a>

```c
#define VIDEO_FOREACH_BAYER_PADDED(X, ...)
```

相关声明：[VIDEO_FOREACH_BAYER_PADDED](#gaec20e32bf0da102bafc033ac2e48b8b5)。

针对每种填充拜耳格式（Bayer Padded Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_gabb167fd4b58db338de823dc285e62342"></a>

```c
#define VIDEO_PIX_FMT_SBGGR8P16 VIDEO_FOURCC('p', 'B', '8', '2')
```

相关声明：[VIDEO_PIX_FMT_SBGGR8P16](#gabb167fd4b58db338de823dc285e62342)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

8 位拜耳格式（Bayer Format），拆成两个各 4 位且均以零填充的数据块，采用小端序（Little Endian）。

<a id="r_ga07b22957c7fdc64fd3089fbcb811d599"></a>

```c
#define VIDEO_PIX_FMT_SGBRG8P16 VIDEO_FOURCC('p', 'G', '8', '2')
```

相关声明：[VIDEO_PIX_FMT_SGBRG8P16](#ga07b22957c7fdc64fd3089fbcb811d599)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

8 位拜耳格式（Bayer Format），拆成两个各 4 位且均以零填充的数据块，采用小端序（Little Endian）。

<a id="r_ga4df33d1a41c2dbdc16c19113be13760b"></a>

```c
#define VIDEO_PIX_FMT_SGRBG8P16 VIDEO_FOURCC('p', 'g', '8', '2')
```

相关声明：[VIDEO_PIX_FMT_SGRBG8P16](#ga4df33d1a41c2dbdc16c19113be13760b)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

8 位拜耳格式（Bayer Format），拆成两个各 4 位且均以零填充的数据块，采用小端序（Little Endian）。

<a id="r_gab471cd15aa874a5deadf7b54b826a90e"></a>

```c
#define VIDEO_PIX_FMT_SRGGB8P16 VIDEO_FOURCC('p', 'R', '8', '2')
```

相关声明：[VIDEO_PIX_FMT_SRGGB8P16](#gab471cd15aa874a5deadf7b54b826a90e)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

8 位拜耳格式（Bayer Format），拆成两个各 4 位且均以零填充的数据块，采用小端序（Little Endian）。

<a id="r_ga22517dda8497ba924ba8bffeaad0c67c"></a>

```c
#define VIDEO_FOREACH_BAYER_MIPI_PACKED(X, ...)
```

相关声明：[VIDEO_FOREACH_BAYER_MIPI_PACKED](#ga22517dda8497ba924ba8bffeaad0c67c)。

针对每种MIPI 打包拜耳格式（Bayer MIPI-packed Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_ga3751a8dce1c7459df06f83cd09449b5d"></a>

```c
#define VIDEO_PIX_FMT_SBGGR10P VIDEO_FOURCC('p', 'B', 'A', 'A')
```

相关声明：[VIDEO_PIX_FMT_SBGGR10P](#ga3751a8dce1c7459df06f83cd09449b5d)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gad69ab9041428488051bdb45f42ad4271"></a>

```c
#define VIDEO_PIX_FMT_SGBRG10P VIDEO_FOURCC('p', 'G', 'A', 'A')
```

相关声明：[VIDEO_PIX_FMT_SGBRG10P](#gad69ab9041428488051bdb45f42ad4271)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gaa28c6306a3ed44a0e50c16e0eac86688"></a>

```c
#define VIDEO_PIX_FMT_SGRBG10P VIDEO_FOURCC('p', 'g', 'A', 'A')
```

相关声明：[VIDEO_PIX_FMT_SGRBG10P](#gaa28c6306a3ed44a0e50c16e0eac86688)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga604d2f3501407546aa924e2fdb37be2f"></a>

```c
#define VIDEO_PIX_FMT_SRGGB10P VIDEO_FOURCC('p', 'R', 'A', 'A')
```

相关声明：[VIDEO_PIX_FMT_SRGGB10P](#ga604d2f3501407546aa924e2fdb37be2f)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gab5b5375f050d039e05032c77ac838b31"></a>

```c
#define VIDEO_PIX_FMT_SBGGR12P VIDEO_FOURCC('p', 'B', 'C', 'C')
```

相关声明：[VIDEO_PIX_FMT_SBGGR12P](#gab5b5375f050d039e05032c77ac838b31)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gaecedece3398a6e2f62c20c2eb3f6d3c2"></a>

```c
#define VIDEO_PIX_FMT_SGBRG12P VIDEO_FOURCC('p', 'G', 'C', 'C')
```

相关声明：[VIDEO_PIX_FMT_SGBRG12P](#gaecedece3398a6e2f62c20c2eb3f6d3c2)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga02d91ebf4b5150d5fa437bb3a7a6e872"></a>

```c
#define VIDEO_PIX_FMT_SGRBG12P VIDEO_FOURCC('p', 'g', 'C', 'C')
```

相关声明：[VIDEO_PIX_FMT_SGRBG12P](#ga02d91ebf4b5150d5fa437bb3a7a6e872)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga348c15cc77c728fdac773d58341cbc1d"></a>

```c
#define VIDEO_PIX_FMT_SRGGB12P VIDEO_FOURCC('p', 'R', 'C', 'C')
```

相关声明：[VIDEO_PIX_FMT_SRGGB12P](#ga348c15cc77c728fdac773d58341cbc1d)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gac3413c36b3ce91e5658cd0f973c1f3d7"></a>

```c
#define VIDEO_PIX_FMT_SBGGR14P VIDEO_FOURCC('p', 'B', 'E', 'E')
```

相关声明：[VIDEO_PIX_FMT_SBGGR14P](#gac3413c36b3ce91e5658cd0f973c1f3d7)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga89eb47d1dd60794781ee91cb5ae199ad"></a>

```c
#define VIDEO_PIX_FMT_SGBRG14P VIDEO_FOURCC('p', 'G', 'E', 'E')
```

相关声明：[VIDEO_PIX_FMT_SGBRG14P](#ga89eb47d1dd60794781ee91cb5ae199ad)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gae06f742e31a62295d3ee16af8eec1b06"></a>

```c
#define VIDEO_PIX_FMT_SGRBG14P VIDEO_FOURCC('p', 'g', 'E', 'E')
```

相关声明：[VIDEO_PIX_FMT_SGRBG14P](#gae06f742e31a62295d3ee16af8eec1b06)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga66646a639518285810335a70337277d7"></a>

```c
#define VIDEO_PIX_FMT_SRGGB14P VIDEO_FOURCC('p', 'R', 'E', 'E')
```

相关声明：[VIDEO_PIX_FMT_SRGGB14P](#ga66646a639518285810335a70337277d7)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga275ba44fc86f0916a9b2a9f7915c0cfe"></a>

```c
#define VIDEO_FOREACH_BAYER_NON_PACKED(X, ...)
```

相关声明：[VIDEO_FOREACH_BAYER_NON_PACKED](#ga275ba44fc86f0916a9b2a9f7915c0cfe)。

针对每种非打包拜耳格式（Bayer Non-packed Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_gabc0205ce5c6426051fdec88d92f123e3"></a>

```c
#define VIDEO_PIX_FMT_SBGGR8 VIDEO_FOURCC('B', 'A', '8', '1')
```

相关声明：[VIDEO_PIX_FMT_SBGGR8](#gabc0205ce5c6426051fdec88d92f123e3)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gaa9edb9c562fc3c86b61e071970fae60d"></a>

```c
#define VIDEO_PIX_FMT_SGBRG8 VIDEO_FOURCC('G', 'B', 'R', 'G')
```

相关声明：[VIDEO_PIX_FMT_SGBRG8](#gaa9edb9c562fc3c86b61e071970fae60d)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga19d8dc905695229097dffe659f2a806e"></a>

```c
#define VIDEO_PIX_FMT_SGRBG8 VIDEO_FOURCC('G', 'R', 'B', 'G')
```

相关声明：[VIDEO_PIX_FMT_SGRBG8](#ga19d8dc905695229097dffe659f2a806e)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gabf0dde810e75d37823891ed03811482c"></a>

```c
#define VIDEO_PIX_FMT_SRGGB8 VIDEO_FOURCC('R', 'G', 'G', 'B')
```

相关声明：[VIDEO_PIX_FMT_SRGGB8](#gabf0dde810e75d37823891ed03811482c)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga0b55190a343fe891bdbb7b148e7feeae"></a>

```c
#define VIDEO_PIX_FMT_SBGGR10 VIDEO_FOURCC('B', 'G', '1', '0')
```

相关声明：[VIDEO_PIX_FMT_SBGGR10](#ga0b55190a343fe891bdbb7b148e7feeae)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga8e0f47c16483b14b45a593e9e542a987"></a>

```c
#define VIDEO_PIX_FMT_SGBRG10 VIDEO_FOURCC('G', 'B', '1', '0')
```

相关声明：[VIDEO_PIX_FMT_SGBRG10](#ga8e0f47c16483b14b45a593e9e542a987)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga011cc337bc54480d1e11c3e6833ae398"></a>

```c
#define VIDEO_PIX_FMT_SGRBG10 VIDEO_FOURCC('B', 'A', '1', '0')
```

相关声明：[VIDEO_PIX_FMT_SGRBG10](#ga011cc337bc54480d1e11c3e6833ae398)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga249cbf808658dab777a705fd9deb2986"></a>

```c
#define VIDEO_PIX_FMT_SRGGB10 VIDEO_FOURCC('R', 'G', '1', '0')
```

相关声明：[VIDEO_PIX_FMT_SRGGB10](#ga249cbf808658dab777a705fd9deb2986)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gaa2d7712f655dfcb3c74b4f4ec9941402"></a>

```c
#define VIDEO_PIX_FMT_SBGGR12 VIDEO_FOURCC('B', 'G', '1', '2')
```

相关声明：[VIDEO_PIX_FMT_SBGGR12](#gaa2d7712f655dfcb3c74b4f4ec9941402)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gaa3df9d0af327e609b25e050a4362c2e2"></a>

```c
#define VIDEO_PIX_FMT_SGBRG12 VIDEO_FOURCC('G', 'B', '1', '2')
```

相关声明：[VIDEO_PIX_FMT_SGBRG12](#gaa3df9d0af327e609b25e050a4362c2e2)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gaf18e6647596613e07ec3c651574b08ba"></a>

```c
#define VIDEO_PIX_FMT_SGRBG12 VIDEO_FOURCC('B', 'A', '1', '2')
```

相关声明：[VIDEO_PIX_FMT_SGRBG12](#gaf18e6647596613e07ec3c651574b08ba)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga7b167f2b6a147d325a685825274cd2f2"></a>

```c
#define VIDEO_PIX_FMT_SRGGB12 VIDEO_FOURCC('R', 'G', '1', '2')
```

相关声明：[VIDEO_PIX_FMT_SRGGB12](#ga7b167f2b6a147d325a685825274cd2f2)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga403f40a7e15319365c6ca8f3f5f19d21"></a>

```c
#define VIDEO_PIX_FMT_SBGGR14 VIDEO_FOURCC('B', 'G', '1', '4')
```

相关声明：[VIDEO_PIX_FMT_SBGGR14](#ga403f40a7e15319365c6ca8f3f5f19d21)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga6c98a7066d7d3bdd8fce3d3651772153"></a>

```c
#define VIDEO_PIX_FMT_SGBRG14 VIDEO_FOURCC('G', 'B', '1', '4')
```

相关声明：[VIDEO_PIX_FMT_SGBRG14](#ga6c98a7066d7d3bdd8fce3d3651772153)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gaf58481956952b13b071b1a68541b9c21"></a>

```c
#define VIDEO_PIX_FMT_SGRBG14 VIDEO_FOURCC('G', 'R', '1', '4')
```

相关声明：[VIDEO_PIX_FMT_SGRBG14](#gaf58481956952b13b071b1a68541b9c21)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gaa6e4c240372e53db8ea3472cc456af58"></a>

```c
#define VIDEO_PIX_FMT_SRGGB14 VIDEO_FOURCC('R', 'G', '1', '4')
```

相关声明：[VIDEO_PIX_FMT_SRGGB14](#gaa6e4c240372e53db8ea3472cc456af58)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gae096669643176203199270317dc3449d"></a>

```c
#define VIDEO_PIX_FMT_SBGGR16 VIDEO_FOURCC('B', 'Y', 'R', '2')
```

相关声明：[VIDEO_PIX_FMT_SBGGR16](#gae096669643176203199270317dc3449d)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga7f00eb633dd312ea89097edc82dc8f0c"></a>

```c
#define VIDEO_PIX_FMT_SGBRG16 VIDEO_FOURCC('G', 'B', '1', '6')
```

相关声明：[VIDEO_PIX_FMT_SGBRG16](#ga7f00eb633dd312ea89097edc82dc8f0c)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga4269984ce806e64ba5ccd41c1429769a"></a>

```c
#define VIDEO_PIX_FMT_SGRBG16 VIDEO_FOURCC('G', 'R', '1', '6')
```

相关声明：[VIDEO_PIX_FMT_SGRBG16](#ga4269984ce806e64ba5ccd41c1429769a)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga4f31b5d397868e952d53022c6c8e5823"></a>

```c
#define VIDEO_PIX_FMT_SRGGB16 VIDEO_FOURCC('R', 'G', '1', '6')
```

相关声明：[VIDEO_PIX_FMT_SRGGB16](#ga4f31b5d397868e952d53022c6c8e5823)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

## 11.5\_灰度格式（Grayscale Formats）

仅包含亮度通道（Luminance Channel，Y），具有不同的位深度（Bit Depth）和打包方式（Packing）。

当格式的每像素位数超过 8 位时，就需要一种将这些位打包到多个字节中的策略（Packing Strategy），各格式的示意中对此进行了说明。

`Y`、`y` 上方的数字用于提示其后各位所属的像素编号（Pixel Number）。

<a id="r_ga2cc6468e655d039ba07f624b032d3765"></a>

```c
#define VIDEO_FOREACH_GRAYSCALE(X, ...)
```

相关声明：[VIDEO_FOREACH_GRAYSCALE](#ga2cc6468e655d039ba07f624b032d3765)。

针对每种灰度格式（Grayscale Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_ga5e694f4181c9f861a1f9603075e20ceb"></a>

```c
#define VIDEO_FOREACH_GRAYSCALE_NON_PACKED(X, ...)
```

相关声明：[VIDEO_FOREACH_GRAYSCALE_NON_PACKED](#ga5e694f4181c9f861a1f9603075e20ceb)。

针对每种非打包灰度格式（Grayscale Non-packed Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_gaa3af19adaf282b83a6c16f265a4260dc"></a>

```c
#define VIDEO_PIX_FMT_GREY VIDEO_FOURCC('G', 'R', 'E', 'Y')
```

相关声明：[VIDEO_PIX_FMT_GREY](#gaa3af19adaf282b83a6c16f265a4260dc)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

与 Y8 相同，即仅含 8 位亮度（Luma-only），使用标准 FOURCC 命名；在某些图形库中称为 L8。

<a id="r_ga0506f2c8aa1a82f02fc9383d99b43bc3"></a>

```c
#define VIDEO_PIX_FMT_Y10 VIDEO_FOURCC('Y', '1', '0', ' ')
```

相关声明：[VIDEO_PIX_FMT_Y10](#ga0506f2c8aa1a82f02fc9383d99b43bc3)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

采用小端序（Little Endian），最高 6 位设为零。

<a id="r_ga166b2144cec4b4f92fadda30e81b7d22"></a>

```c
#define VIDEO_PIX_FMT_Y12 VIDEO_FOURCC('Y', '1', '2', ' ')
```

相关声明：[VIDEO_PIX_FMT_Y12](#ga166b2144cec4b4f92fadda30e81b7d22)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

采用小端序（Little Endian），最高 4 位设为零。

<a id="r_ga7d9379f19abcbac17bad3d6359a42d9d"></a>

```c
#define VIDEO_PIX_FMT_Y14 VIDEO_FOURCC('Y', '1', '4', ' ')
```

相关声明：[VIDEO_PIX_FMT_Y14](#ga7d9379f19abcbac17bad3d6359a42d9d)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

采用小端序（Little Endian），最高 2 位设为零。

<a id="r_gaa65fe8bd917dd2fe95fa87530fc3055f"></a>

```c
#define VIDEO_PIX_FMT_Y16 VIDEO_FOURCC('Y', '1', '6', ' ')
```

相关声明：[VIDEO_PIX_FMT_Y16](#gaa65fe8bd917dd2fe95fa87530fc3055f)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

小端序（Little Endian）。

<a id="r_ga1580b8c54fa57958ebfb573a4a138b9c"></a>

```c
#define VIDEO_FOREACH_GRAYSCALE_PADDED(X, ...)
```

相关声明：[VIDEO_FOREACH_GRAYSCALE_PADDED](#ga1580b8c54fa57958ebfb573a4a138b9c)。

针对每种填充灰度格式（Grayscale Padded Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_gad40f2d8628a39f0d87d5f0a337d7f8c4"></a>

```c
#define VIDEO_PIX_FMT_Y8P16 VIDEO_FOURCC('Y', '8', 'P', '2')
```

相关声明：[VIDEO_PIX_FMT_Y8P16](#gad40f2d8628a39f0d87d5f0a337d7f8c4)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

仅含 8 位亮度（Luma-only），拆成两个各 4 位且均以零填充的数据块，采用小端序（Little Endian）。

<a id="r_ga4580c65a689a43878c18e0dc985e52f5"></a>

```c
#define VIDEO_FOREACH_GRAYSCALE_MIPI_PACKED(X, ...)
```

相关声明：[VIDEO_FOREACH_GRAYSCALE_MIPI_PACKED](#ga4580c65a689a43878c18e0dc985e52f5)。

针对每种MIPI 打包灰度格式（Grayscale MIPI-packed Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_ga502df4612995fc39e03d6de3ec675159"></a>

```c
#define VIDEO_PIX_FMT_Y10P VIDEO_FOURCC('Y', '1', '0', 'P')
```

相关声明：[VIDEO_PIX_FMT_Y10P](#ga502df4612995fc39e03d6de3ec675159)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga263e6553a77d00bc509c1b270efebb0b"></a>

```c
#define VIDEO_PIX_FMT_Y12P VIDEO_FOURCC('Y', '1', '2', 'P')
```

相关声明：[VIDEO_PIX_FMT_Y12P](#ga263e6553a77d00bc509c1b270efebb0b)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gada0124aad9c10d403966b1e3851cd968"></a>

```c
#define VIDEO_PIX_FMT_Y14P VIDEO_FOURCC('Y', '1', '4', 'P')
```

相关声明：[VIDEO_PIX_FMT_Y14P](#gada0124aad9c10d403966b1e3851cd968)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

## 11.6\_RGB 格式（RGB Formats）

各颜色通道（Per-color Channels）：R、G、B。

<a id="r_ga8f1ce8a81f2aea6386a5168c9e1ed939"></a>

```c
#define VIDEO_FOREACH_RGB(X, ...)
```

相关声明：[VIDEO_FOREACH_RGB](#ga8f1ce8a81f2aea6386a5168c9e1ed939)。

针对每种RGB 格式（RGB Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_gadec2c5cf7e59f4092eef6930580d93f0"></a>

```c
#define VIDEO_FOREACH_RGB_PACKED(X, ...)
```

相关声明：[VIDEO_FOREACH_RGB_PACKED](#gadec2c5cf7e59f4092eef6930580d93f0)。

针对每种打包 RGB 格式（RGB Packed Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_gaf3830004bb857fa00a14d0a1209c61a8"></a>

```c
#define VIDEO_PIX_FMT_RGB565X VIDEO_FOURCC('R', 'G', 'B', 'R')
```

相关声明：[VIDEO_PIX_FMT_RGB565X](#gaf3830004bb857fa00a14d0a1209c61a8)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

5 位红色（Red）位于 `[15:11]`，6 位绿色（Green）位于 `[10:5]`，5 位蓝色（Blue）位于 `[4:0]`。

<a id="r_gaf009d0eb7dbdb3bfd8883da03478c1ec"></a>

```c
#define VIDEO_PIX_FMT_RGB565 VIDEO_FOURCC('R', 'G', 'B', 'P')
```

相关声明：[VIDEO_PIX_FMT_RGB565](#gaf009d0eb7dbdb3bfd8883da03478c1ec)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

5 位红色（Red）位于 `[15:11]`，6 位绿色（Green）位于 `[10:5]`，5 位蓝色（Blue）位于 `[4:0]`。

<a id="r_gaf667895d82c3dd5b6a4ec8e9e98dbd0a"></a>

```c
#define VIDEO_FOREACH_RGB_NON_PACKED(X, ...)
```

相关声明：[VIDEO_FOREACH_RGB_NON_PACKED](#gaf667895d82c3dd5b6a4ec8e9e98dbd0a)。

针对每种非打包 RGB 格式（RGB Non-packed Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_gaf1f8775bbdd0508c4e21a58dfcfc362d"></a>

```c
#define VIDEO_PIX_FMT_BGR24 VIDEO_FOURCC('B', 'G', 'R', '3')
```

相关声明：[VIDEO_PIX_FMT_BGR24](#gaf1f8775bbdd0508c4e21a58dfcfc362d)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

24 位 RGB 格式，每个分量（Component）占 8 位。

<a id="r_ga03e6be04b23b9735c96231eebc687158"></a>

```c
#define VIDEO_PIX_FMT_RGB24 VIDEO_FOURCC('R', 'G', 'B', '3')
```

相关声明：[VIDEO_PIX_FMT_RGB24](#ga03e6be04b23b9735c96231eebc687158)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

24 位 RGB 格式，每个分量（Component）占 8 位。

<a id="r_gacc88a5297ba55a0216e72de6fe087005"></a>

```c
#define VIDEO_FOREACH_RGB_ALPHA(X, ...)
```

相关声明：[VIDEO_FOREACH_RGB_ALPHA](#gacc88a5297ba55a0216e72de6fe087005)。

针对每种带透明度的 RGB 格式（RGB Alpha Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_ga5cd54fb54967a80576082cadd5941670"></a>

```c
#define VIDEO_PIX_FMT_ARGB32 VIDEO_FOURCC('B', 'A', '2', '4')
```

相关声明：[VIDEO_PIX_FMT_ARGB32](#ga5cd54fb54967a80576082cadd5941670)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

每个像素的第一个字节是透明度（Alpha，A）。

<a id="r_ga515e379bc7f59a8062f3e2a5980b0626"></a>

```c
#define VIDEO_PIX_FMT_BGRA32 VIDEO_FOURCC('A', 'R', '2', '4')
```

相关声明：[VIDEO_PIX_FMT_BGRA32](#ga515e379bc7f59a8062f3e2a5980b0626)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

每个像素的最后一个字节是透明度（Alpha，A）。

<a id="r_ga8ee1e3b82eeeb02188157aa4b4b5d842"></a>

```c
#define VIDEO_PIX_FMT_RGBA32 VIDEO_FOURCC('A', 'B', '2', '4')
```

相关声明：[VIDEO_PIX_FMT_RGBA32](#ga8ee1e3b82eeeb02188157aa4b4b5d842)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

每个像素的最后一个字节是透明度（Alpha，A）。

<a id="r_gaffb650a5f9b2b03890283ecfe95aee04"></a>

```c
#define VIDEO_PIX_FMT_ABGR32 VIDEO_FOURCC('R', 'A', '2', '4')
```

相关声明：[VIDEO_PIX_FMT_ABGR32](#gaffb650a5f9b2b03890283ecfe95aee04)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

每个像素的第一个字节是透明度（Alpha，A）。

<a id="r_ga34ee863f07f90bd14ccfe5b9c1058539"></a>

```c
#define VIDEO_FOREACH_RGB_PADDED(X, ...)
```

相关声明：[VIDEO_FOREACH_RGB_PADDED](#ga34ee863f07f90bd14ccfe5b9c1058539)。

针对每种填充 RGB 格式（RGB Padded Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_ga8be24c04210f8818d75082bd710db8b1"></a>

```c
#define VIDEO_PIX_FMT_XRGB32 VIDEO_FOURCC('B', 'X', '2', '4')
```

相关声明：[VIDEO_PIX_FMT_XRGB32](#ga8be24c04210f8818d75082bd710db8b1)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

每个像素的第一个字节为空（Empty，X）。

<a id="r_ga4ae1acc3d44a1698e0d48f299f061a49"></a>

```c
#define VIDEO_PIX_FMT_XBGR32 VIDEO_FOURCC('R', 'X', '2', '4')
```

相关声明：[VIDEO_PIX_FMT_XBGR32](#ga4ae1acc3d44a1698e0d48f299f061a49)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

每个像素的第一个字节为空（Empty，X）。

<a id="r_gadf53a84505c1299a5c97a0213c989103"></a>

```c
#define VIDEO_PIX_FMT_BGRX32 VIDEO_FOURCC('X', 'R', '2', '4')
```

相关声明：[VIDEO_PIX_FMT_BGRX32](#gadf53a84505c1299a5c97a0213c989103)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

每个像素的最后一个字节为空（Empty，X）。

<a id="r_gadfdb271a780b10a29a356675014a25c2"></a>

```c
#define VIDEO_PIX_FMT_RGBX32 VIDEO_FOURCC('X', 'B', '2', '4')
```

相关声明：[VIDEO_PIX_FMT_RGBX32](#gadfdb271a780b10a29a356675014a25c2)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

每个像素的最后一个字节为空（Empty，X）。

## 11.7\_YUV 格式（YUV Formats）

亮度通道（Luminance，Y）和色度通道（Chrominance，U、V）。

<a id="r_ga95b3d15b30a04e432543a250339cde93"></a>

```c
#define VIDEO_FOREACH_YUV(X, ...)
```

相关声明：[VIDEO_FOREACH_YUV](#ga95b3d15b30a04e432543a250339cde93)。

针对每种YUV 格式（YUV Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_ga8de7c85dd4b32fa406aa121a3ee7f519"></a>

```c
#define VIDEO_FOREACH_YUV_NON_PLANAR(X, ...)
```

相关声明：[VIDEO_FOREACH_YUV_NON_PLANAR](#ga8de7c85dd4b32fa406aa121a3ee7f519)。

针对每种非平面 YUV 格式（YUV Non-Planar Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_gad186d3166acec11c893ae57a0ae68f11"></a>

```c
#define VIDEO_PIX_FMT_YUYV VIDEO_FOURCC('Y', 'U', 'Y', 'V')
```

相关声明：[VIDEO_PIX_FMT_YUYV](#gad186d3166acec11c893ae57a0ae68f11)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

每个像素缺少一个通道（Channel），即 U 或 V。

<a id="r_ga299af047675a110c109cee954f55fca6"></a>

```c
#define VIDEO_PIX_FMT_YVYU VIDEO_FOURCC('Y', 'V', 'Y', 'U')
```

相关声明：[VIDEO_PIX_FMT_YVYU](#ga299af047675a110c109cee954f55fca6)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga63c825ce5dc6c863d355195fde40acb1"></a>

```c
#define VIDEO_PIX_FMT_VYUY VIDEO_FOURCC('V', 'Y', 'U', 'Y')
```

相关声明：[VIDEO_PIX_FMT_VYUY](#ga63c825ce5dc6c863d355195fde40acb1)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_gadca3ee56c798cf05b63cbfc87af98ce3"></a>

```c
#define VIDEO_PIX_FMT_UYVY VIDEO_FOURCC('U', 'Y', 'V', 'Y')
```

相关声明：[VIDEO_PIX_FMT_UYVY](#gadca3ee56c798cf05b63cbfc87af98ce3)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

<a id="r_ga017bcbec587314f569d6d0e4fbdda351"></a>

```c
#define VIDEO_PIX_FMT_XYUV32 VIDEO_FOURCC('X', 'Y', 'U', 'V')
```

相关声明：[VIDEO_PIX_FMT_XYUV32](#ga017bcbec587314f569d6d0e4fbdda351)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

每个像素的第一个字节为空（Empty，X）。

<a id="r_gabcdd44434323cc0e0634e94f23f83146"></a>

```c
#define VIDEO_PIX_FMT_YUV24 VIDEO_FOURCC('Y', 'U', 'V', '3')
```

相关声明：[VIDEO_PIX_FMT_YUV24](#gabcdd44434323cc0e0634e94f23f83146)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

24 位 YUV 格式，每个分量（Component）占 8 位。

<a id="r_gac7378ac0dcd5d2afeba4def9cab509f0"></a>

```c
#define VIDEO_FOREACH_YUV_SEMI_PLANAR(X, ...)
```

相关声明：[VIDEO_FOREACH_YUV_SEMI_PLANAR](#gac7378ac0dcd5d2afeba4def9cab509f0)。

针对每种半平面 YUV 格式（YUV Semi-Planar Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_ga6e5538e8f21a5be750eec38c2a16ad2f"></a>

```c
#define VIDEO_PIX_FMT_NV12 VIDEO_FOURCC('N', 'V', '1', '2')
```

相关声明：[VIDEO_PIX_FMT_NV12](#ga6e5538e8f21a5be750eec38c2a16ad2f)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

色度（Chroma，U/V）在水平和垂直方向均进行子采样（Subsampling）。

<a id="r_ga171cb239b78ca49b9232dcb9d5e9f43f"></a>

```c
#define VIDEO_PIX_FMT_NV21 VIDEO_FOURCC('N', 'V', '2', '1')
```

相关声明：[VIDEO_PIX_FMT_NV21](#ga171cb239b78ca49b9232dcb9d5e9f43f)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

色度（Chroma，U/V）在水平和垂直方向均进行子采样（Subsampling）。

<a id="r_gabbfecc5e0c2c4115c57d4772eaa4918f"></a>

```c
#define VIDEO_PIX_FMT_NV16 VIDEO_FOURCC('N', 'V', '1', '6')
```

相关声明：[VIDEO_PIX_FMT_NV16](#gabbfecc5e0c2c4115c57d4772eaa4918f)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

色度（Chroma，U/V）在水平方向进行子采样（Subsampling）。

<a id="r_ga3463a33faa910f98280c96f40d3c65e7"></a>

```c
#define VIDEO_PIX_FMT_NV61 VIDEO_FOURCC('N', 'V', '6', '1')
```

相关声明：[VIDEO_PIX_FMT_NV61](#ga3463a33faa910f98280c96f40d3c65e7)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

色度（Chroma，U/V）在水平方向进行子采样（Subsampling）。

<a id="r_ga06864b3b1b7d563a9cd2f15c33cdd2d8"></a>

```c
#define VIDEO_PIX_FMT_NV24 VIDEO_FOURCC('N', 'V', '2', '4')
```

相关声明：[VIDEO_PIX_FMT_NV24](#ga06864b3b1b7d563a9cd2f15c33cdd2d8)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

色度（Chroma，U/V）不进行子采样（Subsampling）。

<a id="r_gace39ba88d298b1991412f73fb4fe9d18"></a>

```c
#define VIDEO_PIX_FMT_NV42 VIDEO_FOURCC('N', 'V', '4', '2')
```

相关声明：[VIDEO_PIX_FMT_NV42](#gace39ba88d298b1991412f73fb4fe9d18)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

色度（Chroma，U/V）不进行子采样（Subsampling）。

<a id="r_gac71db00c78d16191a6d613ca190a9ede"></a>

```c
#define VIDEO_FOREACH_YUV_FULL_PLANAR(X, ...)
```

相关声明：[VIDEO_FOREACH_YUV_FULL_PLANAR](#gac71db00c78d16191a6d613ca190a9ede)。

针对每种全平面 YUV 格式（YUV Full-Planar Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_ga9054aa564afdf3b6129539fbda30d9bf"></a>

```c
#define VIDEO_PIX_FMT_YUV420 VIDEO_FOURCC('Y', 'U', '1', '2')
```

相关声明：[VIDEO_PIX_FMT_YUV420](#ga9054aa564afdf3b6129539fbda30d9bf)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

色度（Chroma，U/V）在水平和垂直方向均进行子采样（Subsampling）。

<a id="r_ga9294d7e95c9fe00df93248958b7bef0e"></a>

```c
#define VIDEO_PIX_FMT_YVU420 VIDEO_FOURCC('Y', 'V', '1', '2')
```

相关声明：[VIDEO_PIX_FMT_YVU420](#ga9294d7e95c9fe00df93248958b7bef0e)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

色度（Chroma，U/V）在水平和垂直方向均进行子采样（Subsampling）。

## 11.8\_压缩格式（Compressed Formats）

<a id="r_ga2b2310e1eee22f0e4c28d870e251ecc7"></a>

```c
#define VIDEO_FOREACH_COMPRESSED(X, ...)
```

相关声明：[VIDEO_FOREACH_COMPRESSED](#ga2b2310e1eee22f0e4c28d870e251ecc7)。

针对每种压缩格式（Compressed Format）重复调用宏，并将格式作为第一个参数传入。

<a id="r_ga035a13c38c4f123411547e2c40d58bd2"></a>

```c
#define VIDEO_PIX_FMT_JPEG VIDEO_FOURCC('J', 'P', 'E', 'G')
```

相关声明：[VIDEO_PIX_FMT_JPEG](#ga035a13c38c4f123411547e2c40d58bd2)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

同时涵盖 JPEG 单帧格式，以及动态 JPEG（Motion-JPEG，MJPEG），后者由多个 JPEG 帧连接而成。

<a id="r_ga2f66735e0f52991abfc3188ff2c4310c"></a>

```c
#define VIDEO_PIX_FMT_H264 VIDEO_FOURCC('H', '2', '6', '4')
```

相关声明：[VIDEO_PIX_FMT_H264](#ga2f66735e0f52991abfc3188ff2c4310c)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

带起始码（Start Code）的 H264。

<a id="r_ga8056c592a7794552c3e44531c643b7de"></a>

```c
#define VIDEO_PIX_FMT_H264_NO_SC VIDEO_FOURCC('A', 'V', 'C', '1')
```

相关声明：[VIDEO_PIX_FMT_H264_NO_SC](#ga8056c592a7794552c3e44531c643b7de)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

不带起始码（Start Code）的 H264。

<a id="r_gabb1779dc232fa3d1915ced0088df5f27"></a>

```c
#define VIDEO_PIX_FMT_PNG VIDEO_FOURCC('P', 'N', 'G', ' ')
```

相关声明：[VIDEO_PIX_FMT_PNG](#gabb1779dc232fa3d1915ced0088df5f27)、[VIDEO_FOURCC](#gafb9e36597c39face52cd0c010df20951)。

PNG。

## 11.9\_详细说明（Detailed Documentation）

<a id="gae46d2e9dc794ebb59e2809187754f978"></a>

### `VIDEO_FMT_IS_BAYER`

```c
#define VIDEO_FMT_IS_BAYER ( pixfmt)
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
(0 VIDEO_FOREACH_BAYER(_VIDEO_FMT_OR_EQ, pixfmt))
```

检查 `fourcc` 是否为拜耳格式（Bayer Format）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pixfmt` | 要检查的像素格式（Pixel Format）的 FourCC。 |

**返回（Returns）**：返回值（Returns）：是否已知该格式属于此类别（Category）。

<a id="ga5fe20fff04af51e514eebc07bed44745"></a>

### `VIDEO_FMT_IS_FULL_PLANAR`

```c
#define VIDEO_FMT_IS_FULL_PLANAR ( pixfmt)
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
(0 VIDEO_FOREACH_YUV_FULL_PLANAR(_VIDEO_FMT_OR_EQ, pixfmt))
```

检查 `fourcc` 是否为任一种全平面格式（Full-planar Format）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pixfmt` | 要检查的像素格式（Pixel Format）的 FourCC。 |

**返回（Returns）**：返回值（Returns）：是否已知该格式属于此类别（Category）。

<a id="ga7793e9ac7b592429b0dac4da4ead3674"></a>

### `VIDEO_FMT_IS_GRAYSCALE`

```c
#define VIDEO_FMT_IS_GRAYSCALE ( pixfmt)
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
(0 VIDEO_FOREACH_GRAYSCALE(_VIDEO_FMT_OR_EQ, pixfmt))
```

检查 `fourcc` 是否为灰度格式（Grayscale Format）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pixfmt` | 要检查的像素格式（Pixel Format）的 FourCC。 |

**返回（Returns）**：返回值（Returns）：是否已知该格式属于此类别（Category）。

<a id="ga81623ba4831653e1805018ec822f2ef1"></a>

### `VIDEO_FMT_IS_MIPI_PACKED`

```c
#define VIDEO_FMT_IS_MIPI_PACKED ( pixfmt)
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
(0 VIDEO_FOREACH_BAYER_MIPI_PACKED(_VIDEO_FMT_OR_EQ, pixfmt)            \
   VIDEO_FOREACH_GRAYSCALE_MIPI_PACKED(_VIDEO_FMT_OR_EQ, pixfmt))
```

检查 `fourcc` 是否为任一种 MIPI 打包格式（MIPI-packed Format）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pixfmt` | 要检查的像素格式（Pixel Format）的 FourCC。 |

**返回（Returns）**：返回值（Returns）：是否已知该格式属于此类别（Category）。

<a id="gafdb3d79c7df1881b3946260e191e3cad"></a>

### `VIDEO_FMT_IS_PADDED`

```c
#define VIDEO_FMT_IS_PADDED ( pixfmt)
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
(0 VIDEO_FOREACH_BAYER_PADDED(_VIDEO_FMT_OR_EQ, pixfmt)                 \
   VIDEO_FOREACH_GRAYSCALE_PADDED(_VIDEO_FMT_OR_EQ, pixfmt))
```

检查 `fourcc` 是否为任一种 MIPI 打包格式（MIPI-packed Format）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pixfmt` | 要检查的像素格式（Pixel Format）的 FourCC。 |

**返回（Returns）**：返回值（Returns）：是否已知该格式属于此类别（Category）。

<a id="gae95d61e79e7a102eedba629e4d26cf5d"></a>

### `VIDEO_FMT_IS_RGB`

```c
#define VIDEO_FMT_IS_RGB ( pixfmt)
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
(0 VIDEO_FOREACH_RGB(_VIDEO_FMT_OR_EQ, pixfmt))
```

检查 `fourcc` 是否为 RGB 格式，不含拜耳格式（Bayer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pixfmt` | 要检查的像素格式（Pixel Format）的 FourCC。 |

**返回（Returns）**：返回值（Returns）：是否已知该格式属于此类别（Category）。

<a id="ga236286b6c75a3dac10f7d82347dfdd9b"></a>

### `VIDEO_FMT_IS_SEMI_PLANAR`

```c
#define VIDEO_FMT_IS_SEMI_PLANAR ( pixfmt)
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
(0 VIDEO_FOREACH_YUV_SEMI_PLANAR(_VIDEO_FMT_OR_EQ, pixfmt))
```

检查 `fourcc` 是否为任一种半平面格式（Semi-planar Format）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pixfmt` | 要检查的像素格式（Pixel Format）的 FourCC。 |

**返回（Returns）**：返回值（Returns）：是否已知该格式属于此类别（Category）。

<a id="ga3bac0f45c04fea1d141b65a1d7edb267"></a>

### `VIDEO_FMT_IS_YUV`

```c
#define VIDEO_FMT_IS_YUV ( pixfmt)
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
(0 VIDEO_FOREACH_YUV(_VIDEO_FMT_OR_EQ, pixfmt))
```

检查 `fourcc` 是否为 YUV 格式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pixfmt` | 要检查的像素格式（Pixel Format）的 FourCC。 |

**返回（Returns）**：返回值（Returns）：是否已知该格式属于此类别（Category）。

<a id="gacaf01a28e346128216eaaec08591403b"></a>

### `VIDEO_FOREACH_BAYER`

```c
#define VIDEO_FOREACH_BAYER ( X, ... )
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
VIDEO_FOREACH_BAYER_PADDED(X, __VA_ARGS__)                              \
VIDEO_FOREACH_BAYER_MIPI_PACKED(X, __VA_ARGS__)                         \
VIDEO_FOREACH_BAYER_NON_PACKED(X, __VA_ARGS__)
```

针对每种拜耳格式（Bayer Format）重复调用宏，并将格式作为第一个参数传入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `X` | 要重复调用的宏（Macro）。 |
| `...` | 附加参数（Extra Parameters）。 |

<a id="ga22517dda8497ba924ba8bffeaad0c67c"></a>

### `VIDEO_FOREACH_BAYER_MIPI_PACKED`

```c
#define VIDEO_FOREACH_BAYER_MIPI_PACKED ( X, ... )
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
X(VIDEO_PIX_FMT_SBGGR10P, __VA_ARGS__)                                  \
X(VIDEO_PIX_FMT_SGBRG10P, __VA_ARGS__)                                  \
X(VIDEO_PIX_FMT_SGRBG10P, __VA_ARGS__)                                  \
X(VIDEO_PIX_FMT_SRGGB10P, __VA_ARGS__)                                  \
X(VIDEO_PIX_FMT_SBGGR12P, __VA_ARGS__)                                  \
X(VIDEO_PIX_FMT_SGBRG12P, __VA_ARGS__)                                  \
X(VIDEO_PIX_FMT_SGRBG12P, __VA_ARGS__)                                  \
X(VIDEO_PIX_FMT_SRGGB12P, __VA_ARGS__)                                  \
X(VIDEO_PIX_FMT_SBGGR14P, __VA_ARGS__)                                  \
X(VIDEO_PIX_FMT_SGBRG14P, __VA_ARGS__)                                  \
X(VIDEO_PIX_FMT_SGRBG14P, __VA_ARGS__)                                  \
X(VIDEO_PIX_FMT_SRGGB14P, __VA_ARGS__)
```

针对每种MIPI 打包拜耳格式（Bayer MIPI-packed Format）重复调用宏，并将格式作为第一个参数传入。

每个像素具有红、绿、蓝通道（Red/Green/Blue Channels），每像素位数不是 8 位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `X` | 要重复调用的宏（Macro）。 |
| `...` | 附加参数（Extra Parameters）。 |

<a id="ga275ba44fc86f0916a9b2a9f7915c0cfe"></a>

### `VIDEO_FOREACH_BAYER_NON_PACKED`

```c
#define VIDEO_FOREACH_BAYER_NON_PACKED ( X, ... )
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
X(VIDEO_PIX_FMT_SBGGR8, __VA_ARGS__)                                    \
X(VIDEO_PIX_FMT_SGBRG8, __VA_ARGS__)                                    \
X(VIDEO_PIX_FMT_SGRBG8, __VA_ARGS__)                                    \
X(VIDEO_PIX_FMT_SRGGB8, __VA_ARGS__)                                    \
X(VIDEO_PIX_FMT_SGBRG10, __VA_ARGS__)                                   \
X(VIDEO_PIX_FMT_SGRBG10, __VA_ARGS__)                                   \
X(VIDEO_PIX_FMT_SRGGB10, __VA_ARGS__)                                   \
X(VIDEO_PIX_FMT_SBGGR12, __VA_ARGS__)                                   \
X(VIDEO_PIX_FMT_SGBRG12, __VA_ARGS__)                                   \
X(VIDEO_PIX_FMT_SGRBG12, __VA_ARGS__)                                   \
X(VIDEO_PIX_FMT_SRGGB12, __VA_ARGS__)                                   \
X(VIDEO_PIX_FMT_SBGGR14, __VA_ARGS__)                                   \
X(VIDEO_PIX_FMT_SGBRG14, __VA_ARGS__)                                   \
X(VIDEO_PIX_FMT_SGRBG14, __VA_ARGS__)                                   \
X(VIDEO_PIX_FMT_SRGGB14, __VA_ARGS__)                                   \
X(VIDEO_PIX_FMT_SBGGR16, __VA_ARGS__)                                   \
X(VIDEO_PIX_FMT_SGBRG16, __VA_ARGS__)                                   \
X(VIDEO_PIX_FMT_SGRBG16, __VA_ARGS__)                                   \
X(VIDEO_PIX_FMT_SRGGB16, __VA_ARGS__)
```

针对每种非打包拜耳格式（Bayer Non-packed Format）重复调用宏，并将格式作为第一个参数传入。

每个像素具有红、绿、蓝通道（Red/Green/Blue Channels），每像素位数不是 8 位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `X` | 要重复调用的宏（Macro）。 |
| `...` | 附加参数（Extra Parameters）。 |

<a id="gaec20e32bf0da102bafc033ac2e48b8b5"></a>

### `VIDEO_FOREACH_BAYER_PADDED`

```c
#define VIDEO_FOREACH_BAYER_PADDED ( X, ... )
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
X(VIDEO_PIX_FMT_SBGGR8P16, __VA_ARGS__)                                 \
X(VIDEO_PIX_FMT_SGBRG8P16, __VA_ARGS__)                                 \
X(VIDEO_PIX_FMT_SGRBG8P16, __VA_ARGS__)                                 \
X(VIDEO_PIX_FMT_SRGGB8P16, __VA_ARGS__)
```

针对每种填充拜耳格式（Bayer Padded Format）重复调用宏，并将格式作为第一个参数传入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `X` | 要重复调用的宏（Macro）。 |
| `...` | 附加参数（Extra Parameters）。 |

<a id="ga2b2310e1eee22f0e4c28d870e251ecc7"></a>

### `VIDEO_FOREACH_COMPRESSED`

```c
#define VIDEO_FOREACH_COMPRESSED ( X, ... )
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
X(VIDEO_PIX_FMT_JPEG, __VA_ARGS__)                                      \
X(VIDEO_PIX_FMT_H264, __VA_ARGS__)                                      \
X(VIDEO_PIX_FMT_H264_NO_SC, __VA_ARGS__)                                \
X(VIDEO_PIX_FMT_PNG, __VA_ARGS__)
```

针对每种压缩格式（Compressed Format）重复调用宏，并将格式作为第一个参数传入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `X` | 要重复调用的宏（Macro）。 |
| `...` | 附加参数（Extra Parameters）。 |

<a id="ga2cc6468e655d039ba07f624b032d3765"></a>

### `VIDEO_FOREACH_GRAYSCALE`

```c
#define VIDEO_FOREACH_GRAYSCALE ( X, ... )
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
VIDEO_FOREACH_GRAYSCALE_NON_PACKED(X, __VA_ARGS__)                      \
VIDEO_FOREACH_GRAYSCALE_PADDED(X, __VA_ARGS__)                          \
VIDEO_FOREACH_GRAYSCALE_MIPI_PACKED(X, __VA_ARGS__)
```

针对每种灰度格式（Grayscale Format）重复调用宏，并将格式作为第一个参数传入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `X` | 要重复调用的宏（Macro）。 |
| `...` | 附加参数（Extra Parameters）。 |

<a id="ga4580c65a689a43878c18e0dc985e52f5"></a>

### `VIDEO_FOREACH_GRAYSCALE_MIPI_PACKED`

```c
#define VIDEO_FOREACH_GRAYSCALE_MIPI_PACKED ( X, ... )
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
X(VIDEO_PIX_FMT_Y10P, __VA_ARGS__)                                      \
X(VIDEO_PIX_FMT_Y12P, __VA_ARGS__)                                      \
X(VIDEO_PIX_FMT_Y14P, __VA_ARGS__)
```

针对每种MIPI 打包灰度格式（Grayscale MIPI-packed Format）重复调用宏，并将格式作为第一个参数传入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `X` | 要重复调用的宏（Macro）。 |
| `...` | 附加参数（Extra Parameters）。 |

<a id="ga5e694f4181c9f861a1f9603075e20ceb"></a>

### `VIDEO_FOREACH_GRAYSCALE_NON_PACKED`

```c
#define VIDEO_FOREACH_GRAYSCALE_NON_PACKED ( X, ... )
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
X(VIDEO_PIX_FMT_GREY, __VA_ARGS__)                                      \
X(VIDEO_PIX_FMT_Y10, __VA_ARGS__)                                       \
X(VIDEO_PIX_FMT_Y12, __VA_ARGS__)                                       \
X(VIDEO_PIX_FMT_Y14, __VA_ARGS__)                                       \
X(VIDEO_PIX_FMT_Y16, __VA_ARGS__)
```

针对每种非打包灰度格式（Grayscale Non-packed Format）重复调用宏，并将格式作为第一个参数传入。

每个像素具有红、绿、蓝通道（Red/Green/Blue Channels），每像素位数不是 8 位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `X` | 要重复调用的宏（Macro）。 |
| `...` | 附加参数（Extra Parameters）。 |

<a id="ga1580b8c54fa57958ebfb573a4a138b9c"></a>

### `VIDEO_FOREACH_GRAYSCALE_PADDED`

```c
#define VIDEO_FOREACH_GRAYSCALE_PADDED ( X, ... )
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
X(VIDEO_PIX_FMT_Y8P16, __VA_ARGS__)
```

针对每种填充灰度格式（Grayscale Padded Format）重复调用宏，并将格式作为第一个参数传入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `X` | 要重复调用的宏（Macro）。 |
| `...` | 附加参数（Extra Parameters）。 |

<a id="ga8f1ce8a81f2aea6386a5168c9e1ed939"></a>

### `VIDEO_FOREACH_RGB`

```c
#define VIDEO_FOREACH_RGB ( X, ... )
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
VIDEO_FOREACH_RGB_PACKED(X, __VA_ARGS__)                                \
VIDEO_FOREACH_RGB_NON_PACKED(X, __VA_ARGS__)                            \
VIDEO_FOREACH_RGB_ALPHA(X, __VA_ARGS__)                                 \
VIDEO_FOREACH_RGB_PADDED(X, __VA_ARGS__)
```

针对每种RGB 格式（RGB Format）重复调用宏，并将格式作为第一个参数传入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `X` | 要重复调用的宏（Macro）。 |
| `...` | 附加参数（Extra Parameters）。 |

<a id="gacc88a5297ba55a0216e72de6fe087005"></a>

### `VIDEO_FOREACH_RGB_ALPHA`

```c
#define VIDEO_FOREACH_RGB_ALPHA ( X, ... )
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
X(VIDEO_PIX_FMT_ARGB32, __VA_ARGS__)                                    \
X(VIDEO_PIX_FMT_ABGR32, __VA_ARGS__)                                    \
X(VIDEO_PIX_FMT_RGBA32, __VA_ARGS__)                                    \
X(VIDEO_PIX_FMT_BGRA32, __VA_ARGS__)
```

针对每种带透明度的 RGB 格式（RGB Alpha Format）重复调用宏，并将格式作为第一个参数传入。

每个像素具有红、绿、蓝和透明度通道（Red/Green/Blue/Alpha Channels）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `X` | 要重复调用的宏（Macro）。 |
| `...` | 附加参数（Extra Parameters）。 |

<a id="gaf667895d82c3dd5b6a4ec8e9e98dbd0a"></a>

### `VIDEO_FOREACH_RGB_NON_PACKED`

```c
#define VIDEO_FOREACH_RGB_NON_PACKED ( X, ... )
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
X(VIDEO_PIX_FMT_BGR24, __VA_ARGS__)                                     \
X(VIDEO_PIX_FMT_RGB24, __VA_ARGS__)
```

针对每种非打包 RGB 格式（RGB Non-packed Format）重复调用宏，并将格式作为第一个参数传入。

每个像素具有红、绿、蓝通道（Red/Green/Blue Channels），每像素 8 位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `X` | 要重复调用的宏（Macro）。 |
| `...` | 附加参数（Extra Parameters）。 |

<a id="gadec2c5cf7e59f4092eef6930580d93f0"></a>

### `VIDEO_FOREACH_RGB_PACKED`

```c
#define VIDEO_FOREACH_RGB_PACKED ( X, ... )
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
X(VIDEO_PIX_FMT_RGB565X, __VA_ARGS__)                                   \
X(VIDEO_PIX_FMT_RGB565, __VA_ARGS__)
```

针对每种打包 RGB 格式（RGB Packed Format）重复调用宏，并将格式作为第一个参数传入。

每个像素具有红、绿、蓝通道（Red/Green/Blue Channels），每像素位数不是 8 位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `X` | 要重复调用的宏（Macro）。 |
| `...` | 附加参数（Extra Parameters）。 |

<a id="ga34ee863f07f90bd14ccfe5b9c1058539"></a>

### `VIDEO_FOREACH_RGB_PADDED`

```c
#define VIDEO_FOREACH_RGB_PADDED ( X, ... )
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
X(VIDEO_PIX_FMT_XRGB32, __VA_ARGS__)
```

针对每种填充 RGB 格式（RGB Padded Format）重复调用宏，并将格式作为第一个参数传入。

每个像素具有红、绿、蓝通道（Red/Green/Blue Channels）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `X` | 要重复调用的宏（Macro）。 |
| `...` | 附加参数（Extra Parameters）。 |

<a id="ga95b3d15b30a04e432543a250339cde93"></a>

### `VIDEO_FOREACH_YUV`

```c
#define VIDEO_FOREACH_YUV ( X, ... )
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
VIDEO_FOREACH_YUV_FULL_PLANAR(X, __VA_ARGS__)                           \
VIDEO_FOREACH_YUV_NON_PLANAR(X, __VA_ARGS__)                            \
VIDEO_FOREACH_YUV_SEMI_PLANAR(X, __VA_ARGS__)
```

针对每种YUV 格式（YUV Format）重复调用宏，并将格式作为第一个参数传入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `X` | 要重复调用的宏（Macro）。 |
| `...` | 附加参数（Extra Parameters）。 |

<a id="gac71db00c78d16191a6d613ca190a9ede"></a>

### `VIDEO_FOREACH_YUV_FULL_PLANAR`

```c
#define VIDEO_FOREACH_YUV_FULL_PLANAR ( X, ... )
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
X(VIDEO_PIX_FMT_YUV420, __VA_ARGS__)                                    \
X(VIDEO_PIX_FMT_YVU420, __VA_ARGS__)
```

针对每种全平面 YUV 格式（YUV Full-Planar Format）重复调用宏，并将格式作为第一个参数传入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `X` | 要重复调用的宏（Macro）。 |
| `...` | 附加参数（Extra Parameters）。 |

<a id="ga8de7c85dd4b32fa406aa121a3ee7f519"></a>

### `VIDEO_FOREACH_YUV_NON_PLANAR`

```c
#define VIDEO_FOREACH_YUV_NON_PLANAR ( X, ... )
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
X(VIDEO_PIX_FMT_YUYV, __VA_ARGS__)                                      \
X(VIDEO_PIX_FMT_YVYU, __VA_ARGS__)                                      \
X(VIDEO_PIX_FMT_VYUY, __VA_ARGS__)                                      \
X(VIDEO_PIX_FMT_UYVY, __VA_ARGS__)                                      \
X(VIDEO_PIX_FMT_YUV24, __VA_ARGS__)                                     \
X(VIDEO_PIX_FMT_XYUV32, __VA_ARGS__)
```

针对每种非平面 YUV 格式（YUV Non-Planar Format）重复调用宏，并将格式作为第一个参数传入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `X` | 要重复调用的宏（Macro）。 |
| `...` | 附加参数（Extra Parameters）。 |

<a id="gac7378ac0dcd5d2afeba4def9cab509f0"></a>

### `VIDEO_FOREACH_YUV_SEMI_PLANAR`

```c
#define VIDEO_FOREACH_YUV_SEMI_PLANAR ( X, ... )
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
X(VIDEO_PIX_FMT_NV12, __VA_ARGS__)                                      \
X(VIDEO_PIX_FMT_NV21, __VA_ARGS__)                                      \
X(VIDEO_PIX_FMT_NV16, __VA_ARGS__)                                      \
X(VIDEO_PIX_FMT_NV61, __VA_ARGS__)                                      \
X(VIDEO_PIX_FMT_NV24, __VA_ARGS__)                                      \
X(VIDEO_PIX_FMT_NV42, __VA_ARGS__)
```

针对每种半平面 YUV 格式（YUV Semi-Planar Format）重复调用宏，并将格式作为第一个参数传入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `X` | 要重复调用的宏（Macro）。 |
| `...` | 附加参数（Extra Parameters）。 |

<a id="gafb9e36597c39face52cd0c010df20951"></a>

### `VIDEO_FOURCC`

```c
#define VIDEO_FOURCC ( a, b, c, d )
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
((uint32_t)(a) | ((uint32_t)(b) << 8) | ((uint32_t)(c) << 16) | ((uint32_t)(d) << 24))
```

唯一标识像素格式（Pixel Format）的四字符代码（Four-character-code，FOURCC）。

<a id="gafc6c4cb871f15464f2b7df86d91fd8f3"></a>

### `VIDEO_FOURCC_FROM_STR`

```c
#define VIDEO_FOURCC_FROM_STR ( str)
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
VIDEO_FOURCC((str)[0], (str)[1], (str)[2], (str)[3])
```

将四字符字符串（Four-character-string）转换为四字符代码（FOURCC）。

将字符串字面量（String Literal）或变量转换为 `VIDEO_FOURCC` 定义的四字符代码（Four-character-code）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `str` | 要转换的字符串（String）。 |

**返回（Returns）**：返回值（Returns）：四字符代码（Four-character-code）。

<a id="gacd3805f57633c3db8c6adcd87384bd5c"></a>

### `VIDEO_FOURCC_TO_STR`

```c
#define VIDEO_FOURCC_TO_STR ( fourcc)
```

```c
#include <zephyr/video/formats.h>
```

展开值（Value）：

```c
((char[]){                                                                                 \
        (char)((fourcc) & 0xFF),                                                           \
        (char)(((fourcc) >> 8) & 0xFF),                                                    \
        (char)(((fourcc) >> 16) & 0xFF),                                                   \
        (char)(((fourcc) >> 24) & 0xFF),                                                   \
        '\0'                                                                               \
})
```

将四字符代码（FOURCC）转换为四字符字符串（Four-character-string）。

将 `VIDEO_FOURCC` 定义的四字符代码（Four-character Code）转换为可在任意位置使用的字符串，例如使用 `s` 打印格式在调试日志（Debug Log）中输出。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fourcc` | 要转换的 32 位四字符代码整数（Four-character-code Integer），采用 CPU 本机字节序（CPU-native Endianness）。 |

**返回（Returns）**：返回值（Returns）：由该代码构建的四字符字符串（Four-character-string）。

<a id="gaffb650a5f9b2b03890283ecfe95aee04"></a>

### `VIDEO_PIX_FMT_ABGR32`

```c
#define VIDEO_PIX_FMT_ABGR32 VIDEO_FOURCC('R', 'A', '2', '4')
```

```c
#include <zephyr/video/formats.h>
```

每个像素的第一个字节是透明度（Alpha，A）。

原始示例（Example）：

```c
| Aaaaaaaa Bbbbbbbb Gggggggg Rrrrrrrr | ...
```

**警告（Warning）**：警告（Warning）：由于历史拼写错误，Linux 将此格式称为 `BGRA32`。

<a id="ga5cd54fb54967a80576082cadd5941670"></a>

### `VIDEO_PIX_FMT_ARGB32`

```c
#define VIDEO_PIX_FMT_ARGB32 VIDEO_FOURCC('B', 'A', '2', '4')
```

```c
#include <zephyr/video/formats.h>
```

每个像素的第一个字节是透明度（Alpha，A）。

原始示例（Example）：

```c
| Aaaaaaaa Rrrrrrrr Gggggggg Bbbbbbbb | ...
```

<a id="gaf1f8775bbdd0508c4e21a58dfcfc362d"></a>

### `VIDEO_PIX_FMT_BGR24`

```c
#define VIDEO_PIX_FMT_BGR24 VIDEO_FOURCC('B', 'G', 'R', '3')
```

```c
#include <zephyr/video/formats.h>
```

24 位 RGB 格式，每个分量（Component）占 8 位。

原始示例（Example）：

```c
| Bbbbbbbb Gggggggg Rggggggg | ...
```

<a id="ga515e379bc7f59a8062f3e2a5980b0626"></a>

### `VIDEO_PIX_FMT_BGRA32`

```c
#define VIDEO_PIX_FMT_BGRA32 VIDEO_FOURCC('A', 'R', '2', '4')
```

```c
#include <zephyr/video/formats.h>
```

每个像素的最后一个字节是透明度（Alpha，A）。

- 警告（Warning）：由于历史拼写错误，Linux 将此格式称为 `ABGR32`。

```c
| Bbbbbbbb Gggggggg Rrrrrrrr Aaaaaaaa | ...
```

**警告（Warning）**：警告（Warning）：由于历史拼写错误，Linux 将此格式称为 `ABGR32`。

<a id="gadf53a84505c1299a5c97a0213c989103"></a>

### `VIDEO_PIX_FMT_BGRX32`

```c
#define VIDEO_PIX_FMT_BGRX32 VIDEO_FOURCC('X', 'R', '2', '4')
```

```c
#include <zephyr/video/formats.h>
```

每个像素的最后一个字节为空（Empty，X）。

原始示例（Example）：

```c
| Bbbbbbbb Gggggggg Rrrrrrrr Xxxxxxxx | ...
```

**警告（Warning）**：警告（Warning）：由于历史拼写错误，Linux 将此格式称为 `XBGR32`。

<a id="gaa3af19adaf282b83a6c16f265a4260dc"></a>

### `VIDEO_PIX_FMT_GREY`

```c
#define VIDEO_PIX_FMT_GREY VIDEO_FOURCC('G', 'R', 'E', 'Y')
```

```c
#include <zephyr/video/formats.h>
```

与 Y8 相同，即仅含 8 位亮度（Luma-only），使用标准 FOURCC 命名；在某些图形库中称为 L8。

原始示例（Example）：

```c
  0          1          2          3
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | ...
```

<a id="ga2f66735e0f52991abfc3188ff2c4310c"></a>

### `VIDEO_PIX_FMT_H264`

```c
#define VIDEO_PIX_FMT_H264 VIDEO_FOURCC('H', '2', '6', '4')
```

```c
#include <zephyr/video/formats.h>
```

带起始码（Start Code）的 H264。

<a id="ga8056c592a7794552c3e44531c643b7de"></a>

### `VIDEO_PIX_FMT_H264_NO_SC`

```c
#define VIDEO_PIX_FMT_H264_NO_SC VIDEO_FOURCC('A', 'V', 'C', '1')
```

```c
#include <zephyr/video/formats.h>
```

不带起始码（Start Code）的 H264。

<a id="ga035a13c38c4f123411547e2c40d58bd2"></a>

### `VIDEO_PIX_FMT_JPEG`

```c
#define VIDEO_PIX_FMT_JPEG VIDEO_FOURCC('J', 'P', 'E', 'G')
```

```c
#include <zephyr/video/formats.h>
```

同时涵盖 JPEG 单帧格式，以及动态 JPEG（Motion-JPEG，MJPEG），后者由多个 JPEG 帧连接而成。

<a id="ga6e5538e8f21a5be750eec38c2a16ad2f"></a>

### `VIDEO_PIX_FMT_NV12`

```c
#define VIDEO_PIX_FMT_NV12 VIDEO_FOURCC('N', 'V', '1', '2')
```

```c
#include <zephyr/video/formats.h>
```

色度（Chroma，U/V）在水平和垂直方向均进行子采样（Subsampling）。

原始示例（Example）：

```c
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | ...
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | ...
| ... |
| Uuuuuuuu   Vvvvvvvv | Uuuuuuuu   Vvvvvvvv | ...
| ... |
```

下图说明亮度（Luma）与色度（Chroma）之间的关系。

原始示例（Example）：

```c
Y0        Y1        Y2        Y3        ...
Y6        Y7        Y8        Y9        ...
...

U0/1/6/7  V0/1/6/7  U2/3/8/9  V2/3/8/9  ...
...
```

<a id="gabbfecc5e0c2c4115c57d4772eaa4918f"></a>

### `VIDEO_PIX_FMT_NV16`

```c
#define VIDEO_PIX_FMT_NV16 VIDEO_FOURCC('N', 'V', '1', '6')
```

```c
#include <zephyr/video/formats.h>
```

色度（Chroma，U/V）在水平方向进行子采样（Subsampling）。

原始示例（Example）：

```c
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | ...
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | ...
| ... |
| Uuuuuuuu   Vvvvvvvv | Uuuuuuuu   Vvvvvvvv | ...
| Uuuuuuuu   Vvvvvvvv | Uuuuuuuu   Vvvvvvvv | ...
| ... |
```

下图说明亮度（Luma）与色度（Chroma）之间的关系。

原始示例（Example）：

```c
Y0        Y1        Y2        Y3        ...
Y6        Y7        Y8        Y9        ...
...

U0/1      V0/1      U2/3      V2/3      ...
U6/7      V6/7      U8/9      V8/9      ...
...
```

<a id="ga171cb239b78ca49b9232dcb9d5e9f43f"></a>

### `VIDEO_PIX_FMT_NV21`

```c
#define VIDEO_PIX_FMT_NV21 VIDEO_FOURCC('N', 'V', '2', '1')
```

```c
#include <zephyr/video/formats.h>
```

色度（Chroma，U/V）在水平和垂直方向均进行子采样（Subsampling）。

原始示例（Example）：

```c
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | ...
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | ...
| ... |
| Vvvvvvvv   Uuuuuuuu | Vvvvvvvv   Uuuuuuuu | ...
| ... |
```

下图说明亮度（Luma）与色度（Chroma）之间的关系。

原始示例（Example）：

```c
Y0        Y1        Y2        Y3        ...
Y6        Y7        Y8        Y9        ...
...

V0/1/6/7  U0/1/6/7  V2/3/8/9  U2/3/8/9  ...
...
```

<a id="ga06864b3b1b7d563a9cd2f15c33cdd2d8"></a>

### `VIDEO_PIX_FMT_NV24`

```c
#define VIDEO_PIX_FMT_NV24 VIDEO_FOURCC('N', 'V', '2', '4')
```

```c
#include <zephyr/video/formats.h>
```

色度（Chroma，U/V）不进行子采样（Subsampling）。

原始示例（Example）：

```c
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy |
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy |
| ... |
| Uuuuuuuu   Vvvvvvvv | Uuuuuuuu   Vvvvvvvv | Uuuuuuuu   Vvvvvvvv | Uuuuuuuu   Vvvvvvvv |
| Uuuuuuuu   Vvvvvvvv | Uuuuuuuu   Vvvvvvvv | Uuuuuuuu   Vvvvvvvv | Uuuuuuuu   Vvvvvvvv |
| ... |
```

下图说明亮度（Luma）与色度（Chroma）之间的关系。

原始示例（Example）：

```c
Y0        Y1        Y2        Y3        ...
Y6        Y7        Y8        Y9        ...
...

U0        V0        U1        V1        U2        V2        U3        V3        ...
U6        V6        U7        V7        U8        V8        U9        V9        ...
...
```

<a id="gace39ba88d298b1991412f73fb4fe9d18"></a>

### `VIDEO_PIX_FMT_NV42`

```c
#define VIDEO_PIX_FMT_NV42 VIDEO_FOURCC('N', 'V', '4', '2')
```

```c
#include <zephyr/video/formats.h>
```

色度（Chroma，U/V）不进行子采样（Subsampling）。

原始示例（Example）：

```c
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy |
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy |
| ... |
| Vvvvvvvv   Uuuuuuuu | Vvvvvvvv   Uuuuuuuu | Vvvvvvvv   Uuuuuuuu | Vvvvvvvv   Uuuuuuuu |
| Vvvvvvvv   Uuuuuuuu | Vvvvvvvv   Uuuuuuuu | Vvvvvvvv   Uuuuuuuu | Vvvvvvvv   Uuuuuuuu |
| ... |
```

下图说明亮度（Luma）与色度（Chroma）之间的关系。

原始示例（Example）：

```c
Y0        Y1        Y2        Y3        ...
Y6        Y7        Y8        Y9        ...
...

V0        U0        V1        U1        V2        U2        V3        U3        ...
V6        U6        V7        U7        V8        U8        V9        U9        ...
...
```

<a id="ga3463a33faa910f98280c96f40d3c65e7"></a>

### `VIDEO_PIX_FMT_NV61`

```c
#define VIDEO_PIX_FMT_NV61 VIDEO_FOURCC('N', 'V', '6', '1')
```

```c
#include <zephyr/video/formats.h>
```

色度（Chroma，U/V）在水平方向进行子采样（Subsampling）。

原始示例（Example）：

```c
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | ...
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | ...
| ... |
| Vvvvvvvv   Uuuuuuuu | Vvvvvvvv   Uuuuuuuu | ...
| Vvvvvvvv   Uuuuuuuu | Vvvvvvvv   Uuuuuuuu | ...
| ... |
```

下图说明亮度（Luma）与色度（Chroma）之间的关系。

原始示例（Example）：

```c
Y0        Y1        Y2        Y3        ...
Y6        Y7        Y8        Y9        ...
...

V0/1      U0/1      V2/3      U2/3      ...
V6/7      U6/7      V8/9      U8/9      ...
...
```

<a id="gabb1779dc232fa3d1915ced0088df5f27"></a>

### `VIDEO_PIX_FMT_PNG`

```c
#define VIDEO_PIX_FMT_PNG VIDEO_FOURCC('P', 'N', 'G', ' ')
```

```c
#include <zephyr/video/formats.h>
```

PNG。

<a id="ga03e6be04b23b9735c96231eebc687158"></a>

### `VIDEO_PIX_FMT_RGB24`

```c
#define VIDEO_PIX_FMT_RGB24 VIDEO_FOURCC('R', 'G', 'B', '3')
```

```c
#include <zephyr/video/formats.h>
```

24 位 RGB 格式，每个分量（Component）占 8 位。

原始示例（Example）：

```c
| Rggggggg Gggggggg Bbbbbbbb | ...
```

<a id="gaf009d0eb7dbdb3bfd8883da03478c1ec"></a>

### `VIDEO_PIX_FMT_RGB565`

```c
#define VIDEO_PIX_FMT_RGB565 VIDEO_FOURCC('R', 'G', 'B', 'P')
```

```c
#include <zephyr/video/formats.h>
```

5 位红色（Red）位于 `[15:11]`，6 位绿色（Green）位于 `[10:5]`，5 位蓝色（Blue）位于 `[4:0]`。

随后将这个 16 位整数按小端序（Little Endian）打包为两个字节：

原始示例（Example）：

```c
  7......0 15.....8
| gggBbbbb RrrrrGgg | ...
```

<a id="gaf3830004bb857fa00a14d0a1209c61a8"></a>

### `VIDEO_PIX_FMT_RGB565X`

```c
#define VIDEO_PIX_FMT_RGB565X VIDEO_FOURCC('R', 'G', 'B', 'R')
```

```c
#include <zephyr/video/formats.h>
```

5 位红色（Red）位于 `[15:11]`，6 位绿色（Green）位于 `[10:5]`，5 位蓝色（Blue）位于 `[4:0]`。

随后将这个 16 位整数按大端序（Big Endian）打包为两个字节：

原始示例（Example）：

```c
  15.....8 7......0
| RrrrrGgg gggBbbbb | ...
```

<a id="ga8ee1e3b82eeeb02188157aa4b4b5d842"></a>

### `VIDEO_PIX_FMT_RGBA32`

```c
#define VIDEO_PIX_FMT_RGBA32 VIDEO_FOURCC('A', 'B', '2', '4')
```

```c
#include <zephyr/video/formats.h>
```

每个像素的最后一个字节是透明度（Alpha，A）。

原始示例（Example）：

```c
| Rrrrrrrr Gggggggg Bbbbbbbb Aaaaaaaa | ...
```

<a id="gadfdb271a780b10a29a356675014a25c2"></a>

### `VIDEO_PIX_FMT_RGBX32`

```c
#define VIDEO_PIX_FMT_RGBX32 VIDEO_FOURCC('X', 'B', '2', '4')
```

```c
#include <zephyr/video/formats.h>
```

每个像素的最后一个字节为空（Empty，X）。

原始示例（Example）：

```c
| Rrrrrrrr Gggggggg Bbbbbbbb Xxxxxxxx | ...
```

<a id="ga0b55190a343fe891bdbb7b148e7feeae"></a>

### `VIDEO_PIX_FMT_SBGGR10`

```c
#define VIDEO_PIX_FMT_SBGGR10 VIDEO_FOURCC('B', 'G', '1', '0')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
| bbbbbbbb 000000Bb | gggggggg 000000Gg | bbbbbbbb 000000Bb | gggggggg 000000Gg | ...
| gggggggg 000000Gg | rrrrrrrr 000000Rr | gggggggg 000000Gg | rrrrrrrr 000000Rr | ...
```

<a id="ga3751a8dce1c7459df06f83cd09449b5d"></a>

### `VIDEO_PIX_FMT_SBGGR10P`

```c
#define VIDEO_PIX_FMT_SBGGR10P VIDEO_FOURCC('p', 'B', 'A', 'A')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
  0          1          2          3          3 2 1 0
| Bbbbbbbb | Gggggggg | Bbbbbbbb | Gggggggg | ggbbggbb | ...
| Gggggggg | Rrrrrrrr | Gggggggg | Rrrrrrrr | rrggrrgg | ...
```

<a id="gaa2d7712f655dfcb3c74b4f4ec9941402"></a>

### `VIDEO_PIX_FMT_SBGGR12`

```c
#define VIDEO_PIX_FMT_SBGGR12 VIDEO_FOURCC('B', 'G', '1', '2')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
| bbbbbbbb 0000Bbbb | gggggggg 0000Gggg | bbbbbbbb 0000Bbbb | gggggggg 0000Gggg | ...
| gggggggg 0000Gggg | rrrrrrrr 0000Rrrr | gggggggg 0000Gggg | rrrrrrrr 0000Rrrr | ...
```

<a id="gab5b5375f050d039e05032c77ac838b31"></a>

### `VIDEO_PIX_FMT_SBGGR12P`

```c
#define VIDEO_PIX_FMT_SBGGR12P VIDEO_FOURCC('p', 'B', 'C', 'C')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
  0          1          1   0      2          3          3   2
| Bbbbbbbb | Gggggggg | ggggbbbb | Bbbbbbbb | Gggggggg | ggggbbbb | ...
| Gggggggg | Rrrrrrrr | rrrrgggg | Gggggggg | Rrrrrrrr | rrrrgggg | ...
```

<a id="ga403f40a7e15319365c6ca8f3f5f19d21"></a>

### `VIDEO_PIX_FMT_SBGGR14`

```c
#define VIDEO_PIX_FMT_SBGGR14 VIDEO_FOURCC('B', 'G', '1', '4')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
| bbbbbbbb 00Bbbbbb | gggggggg 00Gggggg | bbbbbbbb 00Bbbbbb | gggggggg 00Gggggg | ...
| gggggggg 00Gggggg | rrrrrrrr 00Rrrrrr | gggggggg 00Gggggg | rrrrrrrr 00Rrrrrr | ...
```

<a id="gac3413c36b3ce91e5658cd0f973c1f3d7"></a>

### `VIDEO_PIX_FMT_SBGGR14P`

```c
#define VIDEO_PIX_FMT_SBGGR14P VIDEO_FOURCC('p', 'B', 'E', 'E')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
  0          1          2          3          1 0      2   1    3     2
| Bbbbbbbb | Gggggggg | Bbbbbbbb | Gggggggg | ggbbbbbb bbbbgggg ggggggbb | ...
| Gggggggg | Rrrrrrrr | Gggggggg | Rrrrrrrr | rrgggggg ggggrrrr rrrrrrgg | ...
```

<a id="gae096669643176203199270317dc3449d"></a>

### `VIDEO_PIX_FMT_SBGGR16`

```c
#define VIDEO_PIX_FMT_SBGGR16 VIDEO_FOURCC('B', 'Y', 'R', '2')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
| bbbbbbbb Bbbbbbbb | gggggggg Gggggggg | bbbbbbbb Bbbbbbbb | gggggggg Gggggggg | ...
| gggggggg Gggggggg | rrrrrrrr Rrrrrrrr | gggggggg Gggggggg | rrrrrrrr Rrrrrrrr | ...
```

<a id="gabc0205ce5c6426051fdec88d92f123e3"></a>

### `VIDEO_PIX_FMT_SBGGR8`

```c
#define VIDEO_PIX_FMT_SBGGR8 VIDEO_FOURCC('B', 'A', '8', '1')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
  0          1          2          3
| Bbbbbbbb | Gggggggg | Bbbbbbbb | Gggggggg | ...
| Gggggggg | Rrrrrrrr | Gggggggg | Rrrrrrrr | ...
```

<a id="gabb167fd4b58db338de823dc285e62342"></a>

### `VIDEO_PIX_FMT_SBGGR8P16`

```c
#define VIDEO_PIX_FMT_SBGGR8P16 VIDEO_FOURCC('p', 'B', '8', '2')
```

```c
#include <zephyr/video/formats.h>
```

8 位拜耳格式（Bayer Format），拆成两个各 4 位且均以零填充的数据块，采用小端序（Little Endian）。

原始示例（Example）：

```c
  0                   1                   2                   3
| 0000bbbb 0000Bbbb | 0000gggg 0000Gggg | 0000gggg 0000Gggg | 0000rrrr 0000Rrrr | ...
```

<a id="ga8e0f47c16483b14b45a593e9e542a987"></a>

### `VIDEO_PIX_FMT_SGBRG10`

```c
#define VIDEO_PIX_FMT_SGBRG10 VIDEO_FOURCC('G', 'B', '1', '0')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
| gggggggg 000000Gg | bbbbbbbb 000000Bb | gggggggg 000000Gg | bbbbbbbb 000000Bb | ...
| rrrrrrrr 000000Rr | gggggggg 000000Gg | rrrrrrrr 000000Rr | gggggggg 000000Gg | ...
```

<a id="gad69ab9041428488051bdb45f42ad4271"></a>

### `VIDEO_PIX_FMT_SGBRG10P`

```c
#define VIDEO_PIX_FMT_SGBRG10P VIDEO_FOURCC('p', 'G', 'A', 'A')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
  0          1          2          3          3 2 1 0
| Gggggggg | Bbbbbbbb | Gggggggg | Bbbbbbbb | bbggbbgg | ...
| Rrrrrrrr | Gggggggg | Rrrrrrrr | Gggggggg | ggrrggrr | ...
```

<a id="gaa3df9d0af327e609b25e050a4362c2e2"></a>

### `VIDEO_PIX_FMT_SGBRG12`

```c
#define VIDEO_PIX_FMT_SGBRG12 VIDEO_FOURCC('G', 'B', '1', '2')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
| gggggggg 0000Gggg | bbbbbbbb 0000Bbbb | gggggggg 0000Gggg | bbbbbbbb 0000Bbbb | ...
| rrrrrrrr 0000Rrrr | gggggggg 0000Gggg | rrrrrrrr 0000Rrrr | gggggggg 0000Gggg | ...
```

<a id="gaecedece3398a6e2f62c20c2eb3f6d3c2"></a>

### `VIDEO_PIX_FMT_SGBRG12P`

```c
#define VIDEO_PIX_FMT_SGBRG12P VIDEO_FOURCC('p', 'G', 'C', 'C')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
  0          1          1   0      2          3          3   2
| Gggggggg | Bbbbbbbb | bbbbgggg | Gggggggg | Bbbbbbbb | bbbbgggg | ...
| Rrrrrrrr | Gggggggg | ggggrrrr | Rrrrrrrr | Gggggggg | ggggrrrr | ...
```

<a id="ga6c98a7066d7d3bdd8fce3d3651772153"></a>

### `VIDEO_PIX_FMT_SGBRG14`

```c
#define VIDEO_PIX_FMT_SGBRG14 VIDEO_FOURCC('G', 'B', '1', '4')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
| gggggggg 00Gggggg | bbbbbbbb 00Bbbbbb | gggggggg 00Gggggg | bbbbbbbb 00Bbbbbb | ...
| rrrrrrrr 00Rrrrrr | gggggggg 00Gggggg | rrrrrrrr 00Rrrrrr | gggggggg 00Gggggg | ...
```

<a id="ga89eb47d1dd60794781ee91cb5ae199ad"></a>

### `VIDEO_PIX_FMT_SGBRG14P`

```c
#define VIDEO_PIX_FMT_SGBRG14P VIDEO_FOURCC('p', 'G', 'E', 'E')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
  0          1          2          3          1 0      2   1    3     2
| Gggggggg | Bbbbbbbb | Gggggggg | Bbbbbbbb | bbgggggg ggggbbbb bbbbbbgg | ...
| Rrrrrrrr | Gggggggg | Rrrrrrrr | Gggggggg | ggrrrrrr rrrrgggg ggggggrr | ...
```

<a id="ga7f00eb633dd312ea89097edc82dc8f0c"></a>

### `VIDEO_PIX_FMT_SGBRG16`

```c
#define VIDEO_PIX_FMT_SGBRG16 VIDEO_FOURCC('G', 'B', '1', '6')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
| gggggggg Gggggggg | bbbbbbbb Bbbbbbbb | gggggggg Gggggggg | bbbbbbbb Bbbbbbbb | ...
| rrrrrrrr Rrrrrrrr | gggggggg Gggggggg | rrrrrrrr Rrrrrrrr | gggggggg Gggggggg | ...
```

<a id="gaa9edb9c562fc3c86b61e071970fae60d"></a>

### `VIDEO_PIX_FMT_SGBRG8`

```c
#define VIDEO_PIX_FMT_SGBRG8 VIDEO_FOURCC('G', 'B', 'R', 'G')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
  0          1          2          3
| Gggggggg | Bbbbbbbb | Gggggggg | Bbbbbbbb | ...
| Rrrrrrrr | Gggggggg | Rrrrrrrr | Gggggggg | ...
```

<a id="ga07b22957c7fdc64fd3089fbcb811d599"></a>

### `VIDEO_PIX_FMT_SGBRG8P16`

```c
#define VIDEO_PIX_FMT_SGBRG8P16 VIDEO_FOURCC('p', 'G', '8', '2')
```

```c
#include <zephyr/video/formats.h>
```

8 位拜耳格式（Bayer Format），拆成两个各 4 位且均以零填充的数据块，采用小端序（Little Endian）。

原始示例（Example）：

```c
  0                   1                   2                   3
| 0000gggg 0000Gggg | 0000bbbb 0000Bbbb | 0000rrrr 0000Rrrr | 0000gggg 0000Gggg | ...
```

<a id="ga011cc337bc54480d1e11c3e6833ae398"></a>

### `VIDEO_PIX_FMT_SGRBG10`

```c
#define VIDEO_PIX_FMT_SGRBG10 VIDEO_FOURCC('B', 'A', '1', '0')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
| gggggggg 000000Gg | rrrrrrrr 000000Rr | gggggggg 000000Gg | rrrrrrrr 000000Rr | ...
| bbbbbbbb 000000Bb | gggggggg 000000Gg | bbbbbbbb 000000Bb | gggggggg 000000Gg | ...
```

<a id="gaa28c6306a3ed44a0e50c16e0eac86688"></a>

### `VIDEO_PIX_FMT_SGRBG10P`

```c
#define VIDEO_PIX_FMT_SGRBG10P VIDEO_FOURCC('p', 'g', 'A', 'A')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
  0          1          2          3          3 2 1 0
| Gggggggg | Rrrrrrrr | Gggggggg | Rrrrrrrr | rrggrrgg | ...
| Bbbbbbbb | Gggggggg | Bbbbbbbb | Gggggggg | ggbbggbb | ...
```

<a id="gaf18e6647596613e07ec3c651574b08ba"></a>

### `VIDEO_PIX_FMT_SGRBG12`

```c
#define VIDEO_PIX_FMT_SGRBG12 VIDEO_FOURCC('B', 'A', '1', '2')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
| gggggggg 0000Gggg | rrrrrrrr 0000Rrrr | gggggggg 0000Gggg | rrrrrrrr 0000Rrrr | ...
| bbbbbbbb 0000Bbbb | gggggggg 0000Gggg | bbbbbbbb 0000Bbbb | gggggggg 0000Gggg | ...
```

<a id="ga02d91ebf4b5150d5fa437bb3a7a6e872"></a>

### `VIDEO_PIX_FMT_SGRBG12P`

```c
#define VIDEO_PIX_FMT_SGRBG12P VIDEO_FOURCC('p', 'g', 'C', 'C')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
  0          1          1   0      2          3          3   2
| Gggggggg | Rrrrrrrr | rrrrgggg | Gggggggg | Rrrrrrrr | rrrrgggg | ...
| Bbbbbbbb | Gggggggg | ggggbbbb | Bbbbbbbb | Gggggggg | ggggbbbb | ...
```

<a id="gaf58481956952b13b071b1a68541b9c21"></a>

### `VIDEO_PIX_FMT_SGRBG14`

```c
#define VIDEO_PIX_FMT_SGRBG14 VIDEO_FOURCC('G', 'R', '1', '4')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
| gggggggg 00Gggggg | rrrrrrrr 00Rrrrrr | gggggggg 00Gggggg | rrrrrrrr 00Rrrrrr | ...
| bbbbbbbb 00Bbbbbb | gggggggg 00Gggggg | bbbbbbbb 00Bbbbbb | gggggggg 00Gggggg | ...
```

<a id="gae06f742e31a62295d3ee16af8eec1b06"></a>

### `VIDEO_PIX_FMT_SGRBG14P`

```c
#define VIDEO_PIX_FMT_SGRBG14P VIDEO_FOURCC('p', 'g', 'E', 'E')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
  0          1          2          3          1 0      2   1    3     2
| Gggggggg | Rrrrrrrr | Gggggggg | Rrrrrrrr | rrgggggg ggggrrrr rrrrrrgg | ...
| Bbbbbbbb | Gggggggg | Bbbbbbbb | Gggggggg | ggbbbbbb bbbbgggg ggggggbb | ...
```

<a id="ga4269984ce806e64ba5ccd41c1429769a"></a>

### `VIDEO_PIX_FMT_SGRBG16`

```c
#define VIDEO_PIX_FMT_SGRBG16 VIDEO_FOURCC('G', 'R', '1', '6')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
| gggggggg Gggggggg | rrrrrrrr Rrrrrrrr | gggggggg Gggggggg | rrrrrrrr Rrrrrrrr | ...
| bbbbbbbb Bbbbbbbb | gggggggg Gggggggg | bbbbbbbb Bbbbbbbb | gggggggg Gggggggg | ...
```

<a id="ga19d8dc905695229097dffe659f2a806e"></a>

### `VIDEO_PIX_FMT_SGRBG8`

```c
#define VIDEO_PIX_FMT_SGRBG8 VIDEO_FOURCC('G', 'R', 'B', 'G')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
  0          1          2          3
| Gggggggg | Rrrrrrrr | Gggggggg | Rrrrrrrr | ...
| Bbbbbbbb | Gggggggg | Bbbbbbbb | Gggggggg | ...
```

<a id="ga4df33d1a41c2dbdc16c19113be13760b"></a>

### `VIDEO_PIX_FMT_SGRBG8P16`

```c
#define VIDEO_PIX_FMT_SGRBG8P16 VIDEO_FOURCC('p', 'g', '8', '2')
```

```c
#include <zephyr/video/formats.h>
```

8 位拜耳格式（Bayer Format），拆成两个各 4 位且均以零填充的数据块，采用小端序（Little Endian）。

原始示例（Example）：

```c
  0                   1                   2                   3
| 0000gggg 0000Gggg | 0000rrrr 0000Rrrr | 0000bbbb 0000Bbbb | 0000gggg 0000Gggg | ...
```

<a id="ga249cbf808658dab777a705fd9deb2986"></a>

### `VIDEO_PIX_FMT_SRGGB10`

```c
#define VIDEO_PIX_FMT_SRGGB10 VIDEO_FOURCC('R', 'G', '1', '0')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
| rrrrrrrr 000000Rr | gggggggg 000000Gg | rrrrrrrr 000000Rr | gggggggg 000000Gg | ...
| gggggggg 000000Gg | bbbbbbbb 000000Bb | gggggggg 000000Gg | bbbbbbbb 000000Bb | ...
```

<a id="ga604d2f3501407546aa924e2fdb37be2f"></a>

### `VIDEO_PIX_FMT_SRGGB10P`

```c
#define VIDEO_PIX_FMT_SRGGB10P VIDEO_FOURCC('p', 'R', 'A', 'A')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
  0          1          2          3          3 2 1 0
| Rrrrrrrr | Gggggggg | Rrrrrrrr | Gggggggg | ggrrggrr | ...
| Gggggggg | Bbbbbbbb | Gggggggg | Bbbbbbbb | bbggbbgg | ...
```

<a id="ga7b167f2b6a147d325a685825274cd2f2"></a>

### `VIDEO_PIX_FMT_SRGGB12`

```c
#define VIDEO_PIX_FMT_SRGGB12 VIDEO_FOURCC('R', 'G', '1', '2')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
| rrrrrrrr 0000Rrrr | gggggggg 0000Gggg | rrrrrrrr 0000Rrrr | gggggggg 0000Gggg | ...
| gggggggg 0000Gggg | bbbbbbbb 0000Bbbb | gggggggg 0000Gggg | bbbbbbbb 0000Bbbb | ...
```

<a id="ga348c15cc77c728fdac773d58341cbc1d"></a>

### `VIDEO_PIX_FMT_SRGGB12P`

```c
#define VIDEO_PIX_FMT_SRGGB12P VIDEO_FOURCC('p', 'R', 'C', 'C')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
  0          1          1   0      2          3          3   2
| Rrrrrrrr | Gggggggg | ggggrrrr | Rrrrrrrr | Gggggggg | ggggrrrr | ...
| Gggggggg | Bbbbbbbb | bbbbgggg | Gggggggg | Bbbbbbbb | bbbbgggg | ...
```

<a id="gaa6e4c240372e53db8ea3472cc456af58"></a>

### `VIDEO_PIX_FMT_SRGGB14`

```c
#define VIDEO_PIX_FMT_SRGGB14 VIDEO_FOURCC('R', 'G', '1', '4')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
| rrrrrrrr 00Rrrrrr | gggggggg 00Gggggg | rrrrrrrr 00Rrrrrr | gggggggg 00Gggggg | ...
| gggggggg 00Gggggg | bbbbbbbb 00Bbbbbb | gggggggg 00Gggggg | bbbbbbbb 00Bbbbbb | ...
```

<a id="ga66646a639518285810335a70337277d7"></a>

### `VIDEO_PIX_FMT_SRGGB14P`

```c
#define VIDEO_PIX_FMT_SRGGB14P VIDEO_FOURCC('p', 'R', 'E', 'E')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
  0          1          2          3          1 0      2   1    3     2
| Rrrrrrrr | Gggggggg | Rrrrrrrr | Gggggggg | ggrrrrrr rrrrgggg ggggggrr | ...
| Gggggggg | Bbbbbbbb | Gggggggg | Bbbbbbbb | bbgggggg ggggbbbb bbbbbbgg | ...
```

<a id="ga4f31b5d397868e952d53022c6c8e5823"></a>

### `VIDEO_PIX_FMT_SRGGB16`

```c
#define VIDEO_PIX_FMT_SRGGB16 VIDEO_FOURCC('R', 'G', '1', '6')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
| rrrrrrrr Rrrrrrrr | gggggggg Gggggggg | rrrrrrrr Rrrrrrrr | gggggggg Gggggggg | ...
| gggggggg Gggggggg | bbbbbbbb Bbbbbbbb | gggggggg Gggggggg | bbbbbbbb Bbbbbbbb | ...
```

<a id="gabf0dde810e75d37823891ed03811482c"></a>

### `VIDEO_PIX_FMT_SRGGB8`

```c
#define VIDEO_PIX_FMT_SRGGB8 VIDEO_FOURCC('R', 'G', 'G', 'B')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
  0          1          2          3
| Rrrrrrrr | Gggggggg | Rrrrrrrr | Gggggggg | ...
| Gggggggg | Bbbbbbbb | Gggggggg | Bbbbbbbb | ...
```

<a id="gab471cd15aa874a5deadf7b54b826a90e"></a>

### `VIDEO_PIX_FMT_SRGGB8P16`

```c
#define VIDEO_PIX_FMT_SRGGB8P16 VIDEO_FOURCC('p', 'R', '8', '2')
```

```c
#include <zephyr/video/formats.h>
```

8 位拜耳格式（Bayer Format），拆成两个各 4 位且均以零填充的数据块，采用小端序（Little Endian）。

原始示例（Example）：

```c
  0                   1                   2                   3
| 0000rrrr 0000Rrrr | 0000gggg 0000Gggg | 0000gggg 0000Gggg | 0000bbbb 0000Bbbb | ...
```

<a id="gadca3ee56c798cf05b63cbfc87af98ce3"></a>

### `VIDEO_PIX_FMT_UYVY`

```c
#define VIDEO_PIX_FMT_UYVY VIDEO_FOURCC('U', 'Y', 'V', 'Y')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
| Uuuuuuuu Yyyyyyyy | Vvvvvvvv Yyyyyyyy | ...
```

<a id="ga63c825ce5dc6c863d355195fde40acb1"></a>

### `VIDEO_PIX_FMT_VYUY`

```c
#define VIDEO_PIX_FMT_VYUY VIDEO_FOURCC('V', 'Y', 'U', 'Y')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
| Vvvvvvvv Yyyyyyyy | Uuuuuuuu Yyyyyyyy | ...
```

<a id="ga4ae1acc3d44a1698e0d48f299f061a49"></a>

### `VIDEO_PIX_FMT_XBGR32`

```c
#define VIDEO_PIX_FMT_XBGR32 VIDEO_FOURCC('R', 'X', '2', '4')
```

```c
#include <zephyr/video/formats.h>
```

每个像素的第一个字节为空（Empty，X）。

原始示例（Example）：

```c
| Xxxxxxxx Bbbbbbbb Gggggggg Rrrrrrrr | ...
```

**警告（Warning）**：警告（Warning）：由于历史拼写错误，Linux 将此格式称为 `BGRX32`。

<a id="ga8be24c04210f8818d75082bd710db8b1"></a>

### `VIDEO_PIX_FMT_XRGB32`

```c
#define VIDEO_PIX_FMT_XRGB32 VIDEO_FOURCC('B', 'X', '2', '4')
```

```c
#include <zephyr/video/formats.h>
```

每个像素的第一个字节为空（Empty，X）。

原始示例（Example）：

```c
| Xxxxxxxx Rrrrrrrr Gggggggg Bbbbbbbb | ...
```

<a id="ga017bcbec587314f569d6d0e4fbdda351"></a>

### `VIDEO_PIX_FMT_XYUV32`

```c
#define VIDEO_PIX_FMT_XYUV32 VIDEO_FOURCC('X', 'Y', 'U', 'V')
```

```c
#include <zephyr/video/formats.h>
```

每个像素的第一个字节为空（Empty，X）。

原始示例（Example）：

```c
| Xxxxxxxx Yyyyyyyy Uuuuuuuu Vvvvvvvv | ...
```

<a id="ga0506f2c8aa1a82f02fc9383d99b43bc3"></a>

### `VIDEO_PIX_FMT_Y10`

```c
#define VIDEO_PIX_FMT_Y10 VIDEO_FOURCC('Y', '1', '0', ' ')
```

```c
#include <zephyr/video/formats.h>
```

采用小端序（Little Endian），最高 6 位设为零。

原始示例（Example）：

```c
  0                   1                   2                   3
| yyyyyyyy 000000Yy | yyyyyyyy 000000Yy | yyyyyyyy 000000Yy | yyyyyyyy 000000Yy | ...
| yyyyyyyy 000000Yy | yyyyyyyy 000000Yy | yyyyyyyy 000000Yy | yyyyyyyy 000000Yy | ...
```

<a id="ga502df4612995fc39e03d6de3ec675159"></a>

### `VIDEO_PIX_FMT_Y10P`

```c
#define VIDEO_PIX_FMT_Y10P VIDEO_FOURCC('Y', '1', '0', 'P')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
  0          1          2          3          3 2 1 0
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | yyyyyyyy | ...
```

<a id="ga166b2144cec4b4f92fadda30e81b7d22"></a>

### `VIDEO_PIX_FMT_Y12`

```c
#define VIDEO_PIX_FMT_Y12 VIDEO_FOURCC('Y', '1', '2', ' ')
```

```c
#include <zephyr/video/formats.h>
```

采用小端序（Little Endian），最高 4 位设为零。

原始示例（Example）：

```c
  0                   1                   2                   3
| yyyyyyyy 0000Yyyy | yyyyyyyy 0000Yyyy | yyyyyyyy 0000Yyyy | yyyyyyyy 0000Yyyy | ...
| yyyyyyyy 0000Yyyy | yyyyyyyy 0000Yyyy | yyyyyyyy 0000Yyyy | yyyyyyyy 0000Yyyy | ...
```

<a id="ga263e6553a77d00bc509c1b270efebb0b"></a>

### `VIDEO_PIX_FMT_Y12P`

```c
#define VIDEO_PIX_FMT_Y12P VIDEO_FOURCC('Y', '1', '2', 'P')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
  0          1          1   0      2          3          3   2
| Yyyyyyyy | Yyyyyyyy | yyyyyyyy | Yyyyyyyy | Yyyyyyyy | yyyyyyyy | ...
| Yyyyyyyy | Yyyyyyyy | yyyyyyyy | Yyyyyyyy | Yyyyyyyy | yyyyyyyy | ...
```

<a id="ga7d9379f19abcbac17bad3d6359a42d9d"></a>

### `VIDEO_PIX_FMT_Y14`

```c
#define VIDEO_PIX_FMT_Y14 VIDEO_FOURCC('Y', '1', '4', ' ')
```

```c
#include <zephyr/video/formats.h>
```

采用小端序（Little Endian），最高 2 位设为零。

原始示例（Example）：

```c
  0                   1                   2                   3
| yyyyyyyy 00Yyyyyy | yyyyyyyy 00Yyyyyy | yyyyyyyy 00Yyyyyy | yyyyyyyy 00Yyyyyy | ...
| yyyyyyyy 00Yyyyyy | yyyyyyyy 00Yyyyyy | yyyyyyyy 00Yyyyyy | yyyyyyyy 00Yyyyyy | ...
```

<a id="gada0124aad9c10d403966b1e3851cd968"></a>

### `VIDEO_PIX_FMT_Y14P`

```c
#define VIDEO_PIX_FMT_Y14P VIDEO_FOURCC('Y', '1', '4', 'P')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
  0          1          2          3          1 0      2   1    3     2
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | yyyyyyyy yyyyyyyy yyyyyyyy | ...
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | yyyyyyyy yyyyyyyy yyyyyyyy | ...
```

<a id="gaa65fe8bd917dd2fe95fa87530fc3055f"></a>

### `VIDEO_PIX_FMT_Y16`

```c
#define VIDEO_PIX_FMT_Y16 VIDEO_FOURCC('Y', '1', '6', ' ')
```

```c
#include <zephyr/video/formats.h>
```

小端序（Little Endian）。

原始示例（Example）：

```c
  0                   1                   2                   3
| yyyyyyyy Yyyyyyyy | yyyyyyyy Yyyyyyyy | yyyyyyyy Yyyyyyyy | yyyyyyyy Yyyyyyyy | ...
| yyyyyyyy Yyyyyyyy | yyyyyyyy Yyyyyyyy | yyyyyyyy Yyyyyyyy | yyyyyyyy Yyyyyyyy | ...
```

<a id="gad40f2d8628a39f0d87d5f0a337d7f8c4"></a>

### `VIDEO_PIX_FMT_Y8P16`

```c
#define VIDEO_PIX_FMT_Y8P16 VIDEO_FOURCC('Y', '8', 'P', '2')
```

```c
#include <zephyr/video/formats.h>
```

仅含 8 位亮度（Luma-only），拆成两个各 4 位且均以零填充的数据块，采用小端序（Little Endian）。

原始示例（Example）：

```c
  0                   1                   2                   3
| 0000yyyy 0000Yyyy | 0000yyyy 0000Yyyy | 0000yyyy 0000Yyyy | 0000yyyy 0000Yyyy | ...
```

<a id="gabcdd44434323cc0e0634e94f23f83146"></a>

### `VIDEO_PIX_FMT_YUV24`

```c
#define VIDEO_PIX_FMT_YUV24 VIDEO_FOURCC('Y', 'U', 'V', '3')
```

```c
#include <zephyr/video/formats.h>
```

24 位 YUV 格式，每个分量（Component）占 8 位。

原始示例（Example）：

```c
| Yyyyyyyy Uuuuuuuu Vvvvvvvv | ...
```

<a id="ga9054aa564afdf3b6129539fbda30d9bf"></a>

### `VIDEO_PIX_FMT_YUV420`

```c
#define VIDEO_PIX_FMT_YUV420 VIDEO_FOURCC('Y', 'U', '1', '2')
```

```c
#include <zephyr/video/formats.h>
```

色度（Chroma，U/V）在水平和垂直方向均进行子采样（Subsampling）。

原始示例（Example）：

```c
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy |
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy |
| ... |
| Uuuuuuuu | Uuuuuuuu |
| ... |
| Vvvvvvvv | Vvvvvvvv |
| ... |
```

下图说明亮度（Luma）与色度（Chroma）之间的关系。

原始示例（Example）：

```c
Y0        Y1        Y2        Y3        ...
Y6        Y7        Y8        Y9        ...
...

U0/1/6/7      U2/3/8/9      ...
...

V0/1/6/7      V2/3/8/9      ...
...
```

<a id="gad186d3166acec11c893ae57a0ae68f11"></a>

### `VIDEO_PIX_FMT_YUYV`

```c
#define VIDEO_PIX_FMT_YUYV VIDEO_FOURCC('Y', 'U', 'Y', 'V')
```

```c
#include <zephyr/video/formats.h>
```

每个像素缺少一个通道（Channel），即 U 或 V。

该值应在 2 个像素上取平均，以得到单个像素的值（Individual Pixel Value）。

原始示例（Example）：

```c
| Yyyyyyyy Uuuuuuuu | Yyyyyyyy Vvvvvvvv | ...
```

<a id="ga9294d7e95c9fe00df93248958b7bef0e"></a>

### `VIDEO_PIX_FMT_YVU420`

```c
#define VIDEO_PIX_FMT_YVU420 VIDEO_FOURCC('Y', 'V', '1', '2')
```

```c
#include <zephyr/video/formats.h>
```

色度（Chroma，U/V）在水平和垂直方向均进行子采样（Subsampling）。

原始示例（Example）：

```c
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy |
| Yyyyyyyy | Yyyyyyyy | Yyyyyyyy | Yyyyyyyy |
| ... |
| Vvvvvvvv | Vvvvvvvv |
| ... |
| Uuuuuuuu | Uuuuuuuu |
| ... |
```

下图说明亮度（Luma）与色度（Chroma）之间的关系。

原始示例（Example）：

```c
Y0        Y1        Y2        Y3        ...
Y6        Y7        Y8        Y9        ...
...

V0/1/6/7      V2/3/8/9      ...
...

U0/1/6/7      U2/3/8/9      ...
...
```

<a id="ga299af047675a110c109cee954f55fca6"></a>

### `VIDEO_PIX_FMT_YVYU`

```c
#define VIDEO_PIX_FMT_YVYU VIDEO_FOURCC('Y', 'V', 'Y', 'U')
```

```c
#include <zephyr/video/formats.h>
```

原始示例（Example）：

```c
| Yyyyyyyy Vvvvvvvv | Yyyyyyyy Uuuuuuuu | ...
```

<a id="gabdbd1b0f40af6663d81402deefdd387f"></a>

### `video_bits_per_pixel()`

```c
unsigned int video_bits_per_pixel ( uint32_t pixfmt)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/video/formats.h>
```

获取像素格式的每像素位数（Bits per Pixel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pixfmt` | 四字符代码（FourCC）像素格式值，参见视频格式（Video Formats）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 该格式未处理，或每像素位数（Number of Bits）可变。 |

**返回（Returns）**：返回值（Returns）：此格式一个像素的位数（Bit Size）。


## 11.10\_原页交叉引用（Cross References）

- [formats.h](../api_file_media_sensor_reference/P004_zephyr__video__formats.h_文件参考.md)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [视频格式（Video Formats）](P011_视频格式（Video Formats）.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__video__formats_html_gacaf01a28e346128216eaaec08591403b"></a>
<a id="agroup__video__formats_html_gac71db00c78d16191a6d613ca190a9ede"></a>
<a id="agroup__video__formats_html_ga2cc6468e655d039ba07f624b032d3765"></a>
<a id="agroup__video__formats_html_ga22517dda8497ba924ba8bffeaad0c67c"></a>
<a id="agroup__video__formats_html_gaec20e32bf0da102bafc033ac2e48b8b5"></a>
<a id="agroup__video__formats_html_ga8f1ce8a81f2aea6386a5168c9e1ed939"></a>
<a id="agroup__video__formats_html_gac7378ac0dcd5d2afeba4def9cab509f0"></a>
<a id="agroup__video__formats_html_ga95b3d15b30a04e432543a250339cde93"></a>
<a id="agroup__video__formats_html_ga02d91ebf4b5150d5fa437bb3a7a6e872"></a>
<a id="agroup__video__formats_html_ga348c15cc77c728fdac773d58341cbc1d"></a>
<a id="agroup__video__formats_html_ga3751a8dce1c7459df06f83cd09449b5d"></a>
<a id="agroup__video__formats_html_ga604d2f3501407546aa924e2fdb37be2f"></a>
<a id="agroup__video__formats_html_ga66646a639518285810335a70337277d7"></a>
<a id="agroup__video__formats_html_ga89eb47d1dd60794781ee91cb5ae199ad"></a>
<a id="agroup__video__formats_html_gaa28c6306a3ed44a0e50c16e0eac86688"></a>
<a id="agroup__video__formats_html_gab5b5375f050d039e05032c77ac838b31"></a>
<a id="agroup__video__formats_html_gac3413c36b3ce91e5658cd0f973c1f3d7"></a>
<a id="agroup__video__formats_html_gad69ab9041428488051bdb45f42ad4271"></a>
<a id="agroup__video__formats_html_gae06f742e31a62295d3ee16af8eec1b06"></a>
<a id="agroup__video__formats_html_gaecedece3398a6e2f62c20c2eb3f6d3c2"></a>
<a id="agroup__video__formats_html_ga011cc337bc54480d1e11c3e6833ae398"></a>
<a id="agroup__video__formats_html_ga19d8dc905695229097dffe659f2a806e"></a>
<a id="agroup__video__formats_html_ga249cbf808658dab777a705fd9deb2986"></a>
<a id="agroup__video__formats_html_ga403f40a7e15319365c6ca8f3f5f19d21"></a>
<a id="agroup__video__formats_html_ga4269984ce806e64ba5ccd41c1429769a"></a>
<a id="agroup__video__formats_html_ga4f31b5d397868e952d53022c6c8e5823"></a>
<a id="agroup__video__formats_html_ga6c98a7066d7d3bdd8fce3d3651772153"></a>
<a id="agroup__video__formats_html_ga7b167f2b6a147d325a685825274cd2f2"></a>
<a id="agroup__video__formats_html_ga7f00eb633dd312ea89097edc82dc8f0c"></a>
<a id="agroup__video__formats_html_ga8e0f47c16483b14b45a593e9e542a987"></a>
<a id="agroup__video__formats_html_gaa2d7712f655dfcb3c74b4f4ec9941402"></a>
<a id="agroup__video__formats_html_gaa3df9d0af327e609b25e050a4362c2e2"></a>
<a id="agroup__video__formats_html_gaa6e4c240372e53db8ea3472cc456af58"></a>
<a id="agroup__video__formats_html_gaa9edb9c562fc3c86b61e071970fae60d"></a>
<a id="agroup__video__formats_html_gabc0205ce5c6426051fdec88d92f123e3"></a>
<a id="agroup__video__formats_html_gabf0dde810e75d37823891ed03811482c"></a>
<a id="agroup__video__formats_html_gae096669643176203199270317dc3449d"></a>
<a id="agroup__video__formats_html_gaf18e6647596613e07ec3c651574b08ba"></a>
<a id="agroup__video__formats_html_gaf58481956952b13b071b1a68541b9c21"></a>
<a id="agroup__video__formats_html_ga07b22957c7fdc64fd3089fbcb811d599"></a>
<a id="agroup__video__formats_html_ga4df33d1a41c2dbdc16c19113be13760b"></a>
<a id="agroup__video__formats_html_gab471cd15aa874a5deadf7b54b826a90e"></a>
<a id="agroup__video__formats_html_gabb167fd4b58db338de823dc285e62342"></a>
<a id="agroup__video__formats_html_ga035a13c38c4f123411547e2c40d58bd2"></a>
<a id="agroup__video__formats_html_ga2f66735e0f52991abfc3188ff2c4310c"></a>
<a id="agroup__video__formats_html_ga8056c592a7794552c3e44531c643b7de"></a>
<a id="agroup__video__formats_html_gabb1779dc232fa3d1915ced0088df5f27"></a>
<a id="agroup__video__formats_html_ga5e694f4181c9f861a1f9603075e20ceb"></a>
<a id="agroup__video__formats_html_ga263e6553a77d00bc509c1b270efebb0b"></a>
<a id="agroup__video__formats_html_ga502df4612995fc39e03d6de3ec675159"></a>
<a id="agroup__video__formats_html_gada0124aad9c10d403966b1e3851cd968"></a>
<a id="agroup__video__formats_html_ga0506f2c8aa1a82f02fc9383d99b43bc3"></a>
<a id="agroup__video__formats_html_ga166b2144cec4b4f92fadda30e81b7d22"></a>
<a id="agroup__video__formats_html_ga7d9379f19abcbac17bad3d6359a42d9d"></a>
<a id="agroup__video__formats_html_gaa3af19adaf282b83a6c16f265a4260dc"></a>
<a id="agroup__video__formats_html_gaa65fe8bd917dd2fe95fa87530fc3055f"></a>
<a id="agroup__video__formats_html_gad40f2d8628a39f0d87d5f0a337d7f8c4"></a>
<a id="agroup__video__formats_html_gadec2c5cf7e59f4092eef6930580d93f0"></a>
<a id="agroup__video__formats_html_ga515e379bc7f59a8062f3e2a5980b0626"></a>
<a id="agroup__video__formats_html_ga5cd54fb54967a80576082cadd5941670"></a>
<a id="agroup__video__formats_html_ga8ee1e3b82eeeb02188157aa4b4b5d842"></a>
<a id="agroup__video__formats_html_gaffb650a5f9b2b03890283ecfe95aee04"></a>
<a id="agroup__video__formats_html_ga03e6be04b23b9735c96231eebc687158"></a>
<a id="agroup__video__formats_html_gaf1f8775bbdd0508c4e21a58dfcfc362d"></a>
<a id="agroup__video__formats_html_gaf009d0eb7dbdb3bfd8883da03478c1ec"></a>
<a id="agroup__video__formats_html_gaf3830004bb857fa00a14d0a1209c61a8"></a>
<a id="agroup__video__formats_html_ga8be24c04210f8818d75082bd710db8b1"></a>
<a id="agroup__video__formats_html_ga9054aa564afdf3b6129539fbda30d9bf"></a>
<a id="agroup__video__formats_html_ga9294d7e95c9fe00df93248958b7bef0e"></a>
<a id="agroup__video__formats_html_ga017bcbec587314f569d6d0e4fbdda351"></a>
<a id="agroup__video__formats_html_ga299af047675a110c109cee954f55fca6"></a>
<a id="agroup__video__formats_html_ga63c825ce5dc6c863d355195fde40acb1"></a>
<a id="agroup__video__formats_html_gabcdd44434323cc0e0634e94f23f83146"></a>
<a id="agroup__video__formats_html_gad186d3166acec11c893ae57a0ae68f11"></a>
<a id="agroup__video__formats_html_gadca3ee56c798cf05b63cbfc87af98ce3"></a>
<a id="agroup__video__formats_html_ga06864b3b1b7d563a9cd2f15c33cdd2d8"></a>
<a id="agroup__video__formats_html_ga171cb239b78ca49b9232dcb9d5e9f43f"></a>
<a id="agroup__video__formats_html_ga3463a33faa910f98280c96f40d3c65e7"></a>
<a id="agroup__video__formats_html_ga6e5538e8f21a5be750eec38c2a16ad2f"></a>
<a id="agroup__video__formats_html_gabbfecc5e0c2c4115c57d4772eaa4918f"></a>
<a id="agroup__video__formats_html_gace39ba88d298b1991412f73fb4fe9d18"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="agroup__video__formats_html_gafb9e36597c39face52cd0c010df20951"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_USB Type-C 端口控制器驱动后端 API.md) · [返回大纲](大纲.md)
