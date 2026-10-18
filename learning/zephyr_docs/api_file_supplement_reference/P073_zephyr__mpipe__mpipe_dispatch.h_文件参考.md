---
id: learning.zephyr-docs.api-file-supplement-reference.page-73
title: zephyr__mpipe__mpipe_dispatch.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpipe__dispatch_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第73章\_zephyr\_\_mpipe\_\_mpipe\_dispatch.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mpipe__dispatch_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

元素（Elements）之间交换的查询和事件。

<a id="details"></a>

```c
#include <zephyr/mpipe/mpipe_buffer.h>
#include <zephyr/mpipe/mpipe_structure.h>
```

查看此文件的源码。

元素（Elements）之间交换的查询和事件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 73.1\_数据结构（Data Structures）

<a id="r_mpipe_5Fdispatch"></a>

```c
struct mpipe_dispatch
```

相关声明：[mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)。

沿端口连接（Pad Link）传递的查询或事件。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 73.2\_枚举（Enumerations）

<a id="r_gae32e15ab045bc017100a7e713c3999b1"></a>

```c
enum mpipe_dispatch_type { MPIPE_DISPATCH_UNKNOWN = 0 , MPIPE_DISPATCH_EOS , MPIPE_DISPATCH_CAPS , MPIPE_DISPATCH_BUFFER_POOL , MPIPE_DISPATCH_END = UINT8_MAX }
```

相关声明：[mpipe_dispatch_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#gae32e15ab045bc017100a7e713c3999b1)、[MPIPE_DISPATCH_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#ggae32e15ab045bc017100a7e713c3999b1a8c9d64cd72d6864da7f03786906fe08d)、[MPIPE_DISPATCH_EOS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#ggae32e15ab045bc017100a7e713c3999b1a729237cee6bba4d22ce3035bd01c82ed)、[MPIPE_DISPATCH_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#ggae32e15ab045bc017100a7e713c3999b1a63a565f281055915f13e3ec202fe177d)、[MPIPE_DISPATCH_BUFFER_POOL](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#ggae32e15ab045bc017100a7e713c3999b1a9db1cfed44ee98fa15d75e3916a26fd3)、[MPIPE_DISPATCH_END](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#ggae32e15ab045bc017100a7e713c3999b1a6e9d033347db915fffd909f373e4095a)。

支持的分派类型（Dispatch Types）。


## 73.3\_原页交叉引用（Cross References）

- [zephyr/mpipe/mpipe_buffer.h](../api_source_reference/P546_mpipe_buffer.h_源码浏览.md)
- [zephyr/mpipe/mpipe_structure.h](../api_source_reference/P560_mpipe_structure.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P548_mpipe_dispatch.h_源码浏览.md)
- [mpipe_dispatch](../audio_video_model_reference/P020_mpipe_dispatch_结构体.md)
- [mpipe_dispatch_type](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#gae32e15ab045bc017100a7e713c3999b1)
- [MPIPE_DISPATCH_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#ggae32e15ab045bc017100a7e713c3999b1a8c9d64cd72d6864da7f03786906fe08d)
- [MPIPE_DISPATCH_EOS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#ggae32e15ab045bc017100a7e713c3999b1a729237cee6bba4d22ce3035bd01c82ed)
- [MPIPE_DISPATCH_CAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#ggae32e15ab045bc017100a7e713c3999b1a63a565f281055915f13e3ec202fe177d)
- [MPIPE_DISPATCH_BUFFER_POOL](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#ggae32e15ab045bc017100a7e713c3999b1a9db1cfed44ee98fa15d75e3916a26fd3)
- [MPIPE_DISPATCH_END](https://docs.zephyrproject.org/latest/doxygen/html/group__mpipe__dispatch.html#ggae32e15ab045bc017100a7e713c3999b1a6e9d033347db915fffd909f373e4095a)

<a id="header-details"></a>

---

[上一章](P072_zephyr__mpipe__mpipe.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P074_zephyr__mpipe__mpipe_transform_client.h_文件参考.md)
