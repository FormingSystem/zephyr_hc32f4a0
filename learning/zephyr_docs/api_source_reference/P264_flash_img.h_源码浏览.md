---
id: learning.zephyr-docs.api-source-reference.page-264
title: flash_img.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/flash__img_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第264章\_flash\_img.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/flash__img_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/flash__img_8h.html)。

## 264.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="foldopen00044"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="agroup__flash__img__api_html_ga1b194edcb7e4ae34717d011f08d93e0c"></a>
<a id="agroup__flash__img__api_html_ga5a025255d8bf4a94f9e8d315d5502e88"></a>
<a id="agroup__flash__img__api_html_gac1ef017d400bda921ca894d13126b390"></a>
<a id="agroup__flash__img__api_html_gac6d1d7811516493242b318be2ecd82df"></a>
<a id="agroup__flash__img__api_html_gae3cb2d6be9f993bcf5a97931475d9a6d"></a>
<a id="agroup__flash__img__api_html_gaeb242ed3d7654bf94e0dce7d6c24c2a0"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astream__flash_8h_html"></a>
<a id="astructflash__img__check_html"></a>
<a id="astructflash__img__check_html_a6c4aebe9974ddebf0ceafe7f61af8ae9"></a>
<a id="astructflash__img__check_html_abac05d254f5fc46093808083c86be379"></a>
<a id="astructflash__img__context_html"></a>
<a id="astructflash__img__context_html_a80fb0afaa391d3242c7de9ffe0f10675"></a>
<a id="astructflash__img__context_html_a9bdb531f92f32957ab78e6cfcced6a3b"></a>
<a id="astructflash__img__context_html_ae98e6408fe707543f30094f89ae43bdd"></a>
<a id="astructstream__flash__ctx_html"></a>

```c
/*
 * Copyright (c) 2017 Nordic Semiconductor ASA
 * Copyright (c) 2017 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_DFU_FLASH_IMG_H_
#define ZEPHYR_INCLUDE_DFU_FLASH_IMG_H_

#include <zephyr/storage/stream_flash.h>


#ifdef __cplusplus
extern "C" {
#endif

struct flash_img_context {
        uint8_t buf[CONFIG_IMG_BLOCK_BUF_SIZE];
        const struct flash_area *flash_area;
        struct stream_flash_ctx stream;
};

struct flash_img_check {
        const uint8_t *match;
        size_t clen;
};

int flash_img_init_id(struct flash_img_context *ctx, uint8_t area_id);

int flash_img_init(struct flash_img_context *ctx);

size_t flash_img_bytes_written(struct flash_img_context *ctx);

int flash_img_buffered_write(struct flash_img_context *ctx, const uint8_t *data,
                    size_t len, bool flush);

int flash_img_check(struct flash_img_context *ctx,
                    const struct flash_img_check *fic,
                    uint8_t area_id);

uint8_t flash_img_get_upload_slot(void);

#ifdef __cplusplus
}
#endif


#endif  /* ZEPHYR_INCLUDE_DFU_FLASH_IMG_H_ */
```

## 264.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2017 Nordic Semiconductor ASA。

版权（Copyright）：© 2017 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 129 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DFU_FLASH_IMG_H_`。

## 264.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/flash__img_8h.html)
- [zephyr/storage/stream_flash.h](../stream_flash_reference/P001_流式Flash头文件参考.md)
- [flash_img_context](../system_service_model_reference/P029_flash_img_context_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [buf](../system_service_model_reference/P029_flash_img_context_结构体.md#a80fb0afaa391d3242c7de9ffe0f10675)
- [flash_area](../system_service_model_reference/P029_flash_img_context_结构体.md#ae98e6408fe707543f30094f89ae43bdd)
- [stream_flash_ctx](../stream_flash_reference/P003_流式Flash上下文.md)
- [stream](../system_service_model_reference/P029_flash_img_context_结构体.md#a9bdb531f92f32957ab78e6cfcced6a3b)
- [flash_img_check](../system_service_model_reference/P028_flash_img_check_结构体.md)
- [match](../system_service_model_reference/P028_flash_img_check_结构体.md#a6c4aebe9974ddebf0ceafe7f61af8ae9)
- [clen](../system_service_model_reference/P028_flash_img_check_结构体.md#abac05d254f5fc46093808083c86be379)
- [flash_img_init_id](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html#ga1b194edcb7e4ae34717d011f08d93e0c)
- [flash_img_init](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html#gac6d1d7811516493242b318be2ecd82df)
- [flash_img_bytes_written](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html#gac1ef017d400bda921ca894d13126b390)
- [flash_img_buffered_write](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html#gae3cb2d6be9f993bcf5a97931475d9a6d)
- [flash_img_check](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html#ga5a025255d8bf4a94f9e8d315d5502e88)
- [flash_img_get_upload_slot](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__img__api.html#gaeb242ed3d7654bf94e0dce7d6c24c2a0)
- [stream_flash.h](../stream_flash_reference/P001_流式Flash头文件参考.md)
- [flash_img_check::match](../system_service_model_reference/P028_flash_img_check_结构体.md#a6c4aebe9974ddebf0ceafe7f61af8ae9)
- [flash_img_check::clen](../system_service_model_reference/P028_flash_img_check_结构体.md#abac05d254f5fc46093808083c86be379)
- [flash_img_context::buf](../system_service_model_reference/P029_flash_img_context_结构体.md#a80fb0afaa391d3242c7de9ffe0f10675)
- [flash_img_context::stream](../system_service_model_reference/P029_flash_img_context_结构体.md#a9bdb531f92f32957ab78e6cfcced6a3b)
- [flash_img_context::flash_area](../system_service_model_reference/P029_flash_img_context_结构体.md#ae98e6408fe707543f30094f89ae43bdd)

---

[上一章](P263_fido2_up.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P265_flask.h_源码浏览.md)
