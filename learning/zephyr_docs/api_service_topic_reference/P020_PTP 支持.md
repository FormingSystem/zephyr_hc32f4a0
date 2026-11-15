---
id: learning.zephyr-docs.api-service-topic-reference.page-20
title: PTP 支持
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ptp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_PTP 支持

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

精确时间协议（Precision Time Protocol，PTP）支持。

<a id="details"></a>

精确时间协议支持（Precision Time Protocol，PTP）。

自 3.7 版提供（Since 3.7）；接口版本（Version）0.1.0。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 20.1\_宏定义（Macros）

<a id="r_ga7ee0c8e25e85663efbaaa12eac6bee7b"></a>

```c
#define PTP_MAJOR_VERSION 2
```

相关声明：[PTP_MAJOR_VERSION](#ga7ee0c8e25e85663efbaaa12eac6bee7b)。

PTP 主版本号（Major Version）。

<a id="r_ga45adf4966a9012e08dbfbbccf2b806d0"></a>

```c
#define PTP_MINOR_VERSION 1
```

相关声明：[PTP_MINOR_VERSION](#ga45adf4966a9012e08dbfbbccf2b806d0)。

PTP 次版本号（Minor Version）。

<a id="r_ga19395e019e5a96c94ac021bd788c6b55"></a>

```c
#define PTP_VERSION (PTP_MINOR_VERSION << 4 | PTP_MAJOR_VERSION)
```

相关声明：[PTP_VERSION](#ga19395e019e5a96c94ac021bd788c6b55)、[PTP_MINOR_VERSION](#ga45adf4966a9012e08dbfbbccf2b806d0)、[PTP_MAJOR_VERSION](#ga7ee0c8e25e85663efbaaa12eac6bee7b)。

PTP 版本（Version）：IEEE-1588:2019。

## 20.2\_详细说明（Detailed Documentation）

<a id="ga7ee0c8e25e85663efbaaa12eac6bee7b"></a>

### `PTP_MAJOR_VERSION`

```c
#define PTP_MAJOR_VERSION 2
```

```c
#include <zephyr/net/ptp.h>
```

PTP 主版本号（Major Version）。

<a id="ga45adf4966a9012e08dbfbbccf2b806d0"></a>

### `PTP_MINOR_VERSION`

```c
#define PTP_MINOR_VERSION 1
```

```c
#include <zephyr/net/ptp.h>
```

PTP 次版本号（Minor Version）。

<a id="ga19395e019e5a96c94ac021bd788c6b55"></a>

### `PTP_VERSION`

```c
#define PTP_VERSION (PTP_MINOR_VERSION << 4 | PTP_MAJOR_VERSION)
```

```c
#include <zephyr/net/ptp.h>
```

PTP 版本（Version）：IEEE-1588:2019。


## 20.3\_原页交叉引用（Cross References）

- [zephyr/net/ptp.h](../api_file_service_reference/P041_zephyr__net__ptp.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P019_混杂模式（Promiscuous mode）.md) · [返回大纲](大纲.md) · [下一章](P021_Realtek Bee 正交解码器（QDEC）.md)
