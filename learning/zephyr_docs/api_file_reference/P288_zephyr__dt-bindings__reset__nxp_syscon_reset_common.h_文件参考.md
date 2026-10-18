---
id: learning.zephyr-docs.api-file-reference.page-288
title: zephyr__dt-bindings__reset__nxp_syscon_reset_common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp__syscon__reset__common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第288章\_zephyr\_\_dt-bindings\_\_reset\_\_nxp\_syscon\_reset\_common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nxp__syscon__reset__common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 288.1\_宏定义（Macros）

<a id="r_a47950c5f0d385f0ed535f55a27ef342c"></a>

```c
#define NXP_SYSCON_RESET(offset, bit)
```

相关声明：[NXP_SYSCON_RESET](#a47950c5f0d385f0ed535f55a27ef342c)。

## 288.2\_详细说明（Detailed Documentation）

<a id="a47950c5f0d385f0ed535f55a27ef342c"></a>

### `NXP_SYSCON_RESET`

```c
#define NXP_SYSCON_RESET ( offset, bit )
```

展开值（Value）：

```c
((offset << 16) | bit)
```


## 288.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P629_nxp_syscon_reset_common.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P287_zephyr__dt-bindings__clock__nxp_s32z2_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P289_zephyr__posix__netpacket__packet.h_文件参考.md)
