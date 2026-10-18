---
id: learning.zephyr-docs.api-file-runtime-reference.page-2
title: zephyr__drivers__video__arducam_mega.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arducam__mega_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_drivers\_\_video\_\_arducam\_mega.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/arducam__mega_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Copyright (c) 2023 Arducam Technology Co., Ltd.

查看此文件的源码。

<a id="details"></a>

版权所有（Copyright）2023 Arducam Technology Co., Ltd.（<https://www.arducam.com>）。SPDX-License-Identifier: Apache-2.0。

Arducam Mega 厂商特定控件（Vendor-Specific Controls）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_addac25f11861038dc749428ab834bf79"></a>

```c
#define VIDEO_CID_ARDUCAM_RESET (VIDEO_CID_PRIVATE_BASE + 1)
```

相关声明：[VIDEO_CID_ARDUCAM_RESET](#addac25f11861038dc749428ab834bf79)、[VIDEO_CID_PRIVATE_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga05e2fe16eafe259061af62ac31dfaeca)。

触发摄像头复位（Camera Reset）。

<a id="r_a9783516b90fb9074e31019d99633fabe"></a>

```c
#define VIDEO_CID_ARDUCAM_LOWPOWER (VIDEO_CID_PRIVATE_BASE + 2)
```

相关声明：[VIDEO_CID_ARDUCAM_LOWPOWER](#a9783516b90fb9074e31019d99633fabe)、[VIDEO_CID_PRIVATE_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga05e2fe16eafe259061af62ac31dfaeca)。

触发进入（1）或退出（0）低功耗模式（Low-Power Mode）。

## 2.2\_详细说明（Detailed Documentation）

<a id="a9783516b90fb9074e31019d99633fabe"></a>

### `VIDEO_CID_ARDUCAM_LOWPOWER`

```c
#define VIDEO_CID_ARDUCAM_LOWPOWER (VIDEO_CID_PRIVATE_BASE + 2)
```

触发进入（1）或退出（0）低功耗模式（Low-Power Mode）。

<a id="addac25f11861038dc749428ab834bf79"></a>

### `VIDEO_CID_ARDUCAM_RESET`

```c
#define VIDEO_CID_ARDUCAM_RESET (VIDEO_CID_PRIVATE_BASE + 1)
```

触发摄像头复位（Camera Reset）。


## 2.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P035_arducam_mega.h_源码浏览.md)
- [VIDEO_CID_PRIVATE_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga05e2fe16eafe259061af62ac31dfaeca)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P001_zephyr__drivers__sensor__adltc2990.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__dt-bindings__gpio__atmel-sam0-gpio.h_文件参考.md)
