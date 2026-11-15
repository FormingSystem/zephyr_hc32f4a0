---
id: learning.zephyr-docs.api-file-management-reference.page-8
title: zephyr__gnss__rtk__decoder.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/decoder_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_gnss\_\_rtk\_\_decoder.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/decoder_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <stddef.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.1\_函数（Functions）

<a id="r_a036ac8162086665053e5ea7deaa48a93"></a>

```c
int gnss_rtk_decoder_frame_get (uint8_t *buf, size_t buf_len, uint8_t **data, size_t *data_len)
```

相关声明：[gnss_rtk_decoder_frame_get](#a036ac8162086665053e5ea7deaa48a93)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从缓冲区获取 RTK 帧（frame）。

## 8.2\_详细说明（Detailed Documentation）

<a id="a036ac8162086665053e5ea7deaa48a93"></a>

### `gnss_rtk_decoder_frame_get()`

```c
int gnss_rtk_decoder_frame_get ( uint8_t * buf, size_t buf_len, uint8_t ** data, size_t * data_len )
```

从缓冲区获取 RTK 帧（frame）。

供 RTK 客户端从数据缓冲区提取帧使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] buf` | 保存编码数据（encoded data）的缓冲区。 |
| `[in] buf_len` | 缓冲区长度。 |
| `[out] data` | 指向解码后帧（decoded frame）的指针。 |
| `[out] data_len` | 解码后帧的长度。 |

**返回（Returns）**：返回值：成功时返回 0；没有成功解码任何帧时返回 `-ENOENT`；解码失败时返回其他负错误码。


## 8.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P122_decoder.h_源码浏览.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_zephyr__drivers__haptics__cs40l5x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__drivers__biometrics__emul.h_文件参考.md)
