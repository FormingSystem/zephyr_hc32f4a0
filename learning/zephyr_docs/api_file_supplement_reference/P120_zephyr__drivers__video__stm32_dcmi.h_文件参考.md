---
id: learning.zephyr-docs.api-file-supplement-reference.page-120
title: zephyr__drivers__video__stm32_dcmi.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stm32__dcmi_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第120章\_zephyr\_\_drivers\_\_video\_\_stm32\_dcmi.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stm32__dcmi_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

STM32数字摄像头接口（DCMI）的专用控制项。

查看此文件的源码。

<a id="details"></a>

STM32数字摄像头接口（DCMI）的专用控制项。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 120.1\_宏定义（Macros）

<a id="r_a39ee136711fec84a949d6f2bc19d8c11"></a>

```c
#define VIDEO_CID_ST_SNAPSHOT_MODE (VIDEO_CID_PRIVATE_BASE + 1)
```

相关声明：[VIDEO_CID_ST_SNAPSHOT_MODE](#a39ee136711fec84a949d6f2bc19d8c11)、[VIDEO_CID_PRIVATE_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga05e2fe16eafe259061af62ac31dfaeca)。

在视频模式（Video Mode，0）和快照模式（Snapshot Mode，1）之间切换摄像头（Camera）。

## 120.2\_详细说明（Detailed Documentation）

<a id="a39ee136711fec84a949d6f2bc19d8c11"></a>

### `VIDEO_CID_ST_SNAPSHOT_MODE`

```c
#define VIDEO_CID_ST_SNAPSHOT_MODE (VIDEO_CID_PRIVATE_BASE + 1)
```

在视频模式（Video Mode，0）和快照模式（Snapshot Mode，1）之间切换摄像头（Camera）。


## 120.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P831_stm32_dcmi.h_源码浏览.md)
- [VIDEO_CID_PRIVATE_BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__video__control__ids.html#ga05e2fe16eafe259061af62ac31dfaeca)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P119_zephyr__dt-bindings__clock__stm32_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P121_zephyr__drivers__sensor__tcs3400.h_文件参考.md)
