---
id: learning.zephyr-docs.api-file-supplement-reference.page-64
title: zephyr__pmci__mctp__mctp_i3c_pec.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__pec_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第64章\_zephyr\_\_pmci\_\_mctp\_\_mctp\_i3c\_pec.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mctp__i3c__pec_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

基于I3C的MCTP数据包错误码（Packet Error Code，PEC）的辅助接口。

<a id="details"></a>

```c
#include <errno.h>
#include <stddef.h>
#include <stdint.h>
```

查看此文件的源码。

通过 I3C 传输 MCTP（MCTP-over-I3C）时使用的包错误码（Packet Error Code，PEC）辅助函数。内部辅助函数用于计算和验证附加在 MCTP-over-I3C 数据包后的、基于 CRC-8 的包错误码，其定义见 DSP0233。


## 64.1\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P509_mctp_i3c_pec.h_源码浏览.md)

<a id="header-details"></a>

---

[上一章](P063_zephyr__drivers__espi__mchp_xec_espi.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P065_zephyr__net__http__method.h_文件参考.md)
