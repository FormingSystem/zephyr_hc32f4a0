---
id: learning.zephyr-docs.api-file-supplement-reference.page-8
title: zephyr__retention__blinfo.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/blinfo_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_retention\_\_blinfo.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/blinfo_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

启动模式接口（Boot Mode Interface）的公共 API。

<a id="details"></a>

```c
#include <stdint.h>
#include <stddef.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

启动模式接口（Boot Mode Interface）的公共 API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.1\_函数（Functions）

<a id="r_ga7b172c65244678070c9b6ca6e24cee0f"></a>

```c
int blinfo_lookup (uint16_t key, char *val, int val_len_max)
```

相关声明：[blinfo_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__bootloader__info__interface.html#ga7b172c65244678070c9b6ca6e24cee0f)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

返回引导信息（Bootinfo）。


## 8.2\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P067_blinfo.h_源码浏览.md)
- [blinfo_lookup](https://docs.zephyrproject.org/latest/doxygen/html/group__bootloader__info__interface.html#ga7b172c65244678070c9b6ca6e24cee0f)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>

---

[上一章](P007_zephyr__drivers__clock_control__bee_clock_control.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__bluetooth__mesh__blob_io_flash.h_文件参考.md)
