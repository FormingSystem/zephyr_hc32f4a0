---
id: learning.zephyr-docs.api-file-service-reference.page-41
title: zephyr__net__ptp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ptp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_zephyr\_\_net\_\_ptp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ptp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

精确时间协议（Precision Time Protocol）的公共函数。

<a id="details"></a>

```c
#include <zephyr/net/ptp_time.h>
```

查看此文件的源码。

精确时间协议（Precision Time Protocol，PTP）的公共函数（Public Functions）。引用的规范为 2019 版 IEEE 1588（PTP）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 41.1\_宏定义（Macros）

<a id="r_ga7ee0c8e25e85663efbaaa12eac6bee7b"></a>

```c
#define PTP_MAJOR_VERSION 2
```

相关声明：[PTP_MAJOR_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp.html#ga7ee0c8e25e85663efbaaa12eac6bee7b)。

PTP 主版本号（Major Version）。

<a id="r_ga45adf4966a9012e08dbfbbccf2b806d0"></a>

```c
#define PTP_MINOR_VERSION 1
```

相关声明：[PTP_MINOR_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp.html#ga45adf4966a9012e08dbfbbccf2b806d0)。

PTP 次版本号（Minor Version）。

<a id="r_ga19395e019e5a96c94ac021bd788c6b55"></a>

```c
#define PTP_VERSION (PTP_MINOR_VERSION << 4 | PTP_MAJOR_VERSION)
```

相关声明：[PTP_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp.html#ga19395e019e5a96c94ac021bd788c6b55)、[PTP_MINOR_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp.html#ga45adf4966a9012e08dbfbbccf2b806d0)、[PTP_MAJOR_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp.html#ga7ee0c8e25e85663efbaaa12eac6bee7b)。

PTP 版本（Version）：IEEE-1588:2019。


## 41.2\_原页交叉引用（Cross References）

- [zephyr/net/ptp_time.h](../api_source_reference/P681_ptp_time.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P680_ptp.h_源码浏览.md)
- [PTP_MAJOR_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp.html#ga7ee0c8e25e85663efbaaa12eac6bee7b)
- [PTP_MINOR_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp.html#ga45adf4966a9012e08dbfbbccf2b806d0)
- [PTP_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__ptp.html#ga19395e019e5a96c94ac021bd788c6b55)

<a id="header-details"></a>

---

[上一章](P040_zephyr__psa__ps_ids.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P042_zephyr__drivers__ptp_clock.h_文件参考.md)
