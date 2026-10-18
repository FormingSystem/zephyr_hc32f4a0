---
id: learning.zephyr-docs.api-source-reference.page-79
title: buf_loader.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/buf__loader_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第79章\_buf\_loader.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/buf__loader_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/buf__loader_8h.html)。

## 79.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00024"></a>
<a id="foldopen00028"></a>
<a id="l00028"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="foldopen00077"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="foldopen00105"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="foldopen00118"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="aloader_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructllext__buf__loader_html"></a>
<a id="astructllext__buf__loader_html_a8ffcae668c62c0e2488e4bf460a8a196"></a>
<a id="astructllext__loader_html"></a>

```c
/*
 * Copyright (c) 2023 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_LLEXT_BUF_LOADER_H_
#define ZEPHYR_INCLUDE_LLEXT_BUF_LOADER_H_

#include <zephyr/llext/loader.h>

#ifdef __cplusplus
extern "C" {
#endif


struct llext_buf_loader {
        struct llext_loader loader;

        const uint8_t *buf;
        size_t len;
        size_t pos;
};

int llext_buf_read(struct llext_loader *ldr, void *buf, size_t len);
int llext_buf_seek(struct llext_loader *ldr, size_t pos);
void *llext_buf_peek(struct llext_loader *ldr, size_t pos);

#define Z_LLEXT_BUF_LOADER(_buf, _buf_len, _storage)                                               \
        {                                                                                          \
                .loader =                                                                          \
                        {                                                                          \
                                .prepare = NULL,                                                   \
                                .read = llext_buf_read,                                            \
                                .seek = llext_buf_seek,                                            \
                                .peek = llext_buf_peek,                                            \
                                .finalize = NULL,                                                  \
                                .storage = _storage,                                               \
                        },                                                                         \
                .buf = (_buf),                                                                     \
                .len = (_buf_len),                                                                 \
                .pos = 0,                                                                          \
        }

#define LLEXT_BUF_LOADER(_buf, _buf_len) \
        Z_LLEXT_BUF_LOADER(_buf, _buf_len,                                                         \
                           IS_ENABLED(CONFIG_LLEXT_STORAGE_WRITABLE) ?                             \
                                LLEXT_STORAGE_WRITABLE : LLEXT_STORAGE_PERSISTENT)

#define LLEXT_TEMPORARY_BUF_LOADER(_buf, _buf_len) \
        Z_LLEXT_BUF_LOADER(_buf, _buf_len, LLEXT_STORAGE_TEMPORARY)

#define LLEXT_PERSISTENT_BUF_LOADER(_buf, _buf_len) \
        Z_LLEXT_BUF_LOADER(_buf, _buf_len, LLEXT_STORAGE_PERSISTENT)

#define LLEXT_WRITABLE_BUF_LOADER(_buf, _buf_len) \
        Z_LLEXT_BUF_LOADER(_buf, _buf_len, LLEXT_STORAGE_WRITABLE)


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_LLEXT_BUF_LOADER_H_ */
```

## 79.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 129 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_LLEXT_BUF_LOADER_H_`。

## 79.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/buf__loader_8h.html)
- [zephyr/llext/loader.h](https://docs.zephyrproject.org/latest/doxygen/html/loader_8h.html)
- [llext_buf_loader](../llext/P021_缓冲区加载器.md)
- [llext_loader](../llext/P025_扩展加载器上下文.md)
- [loader](../llext/P021_缓冲区加载器.md#a8ffcae668c62c0e2488e4bf460a8a196)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [loader.h](https://docs.zephyrproject.org/latest/doxygen/html/loader_8h.html)
- [llext_buf_loader::loader](../llext/P021_缓冲区加载器.md#a8ffcae668c62c0e2488e4bf460a8a196)

---

[上一章](P078_brg_cfg_srv.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P080_busy_sim.h_源码浏览.md)
