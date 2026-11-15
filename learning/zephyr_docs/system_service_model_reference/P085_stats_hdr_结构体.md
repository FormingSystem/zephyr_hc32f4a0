---
id: learning.zephyr-docs.system-service-model-reference.page-85
title: stats_hdr_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structstats__hdr.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第85章\_stats\_hdr\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structstats__hdr.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

存储单个统计组（Statistics Group）的元数据。

```c
#include <zephyr/stats/stats.h>
```

<a id="details"></a>

保存一个统计组（statistics group）的元数据。应用通常将其作为不透明的组句柄使用：它可以由 `stats_group_find()` 返回，也可以通过遍历回调收到，或者作为 `STATS_SECT_START` 生成结构体的首个成员嵌入。

本数据类型文档由以下文件生成：

- `zephyr/stats/stats.h`

## 85.1\_原页交叉引用（Cross References）

- [zephyr/stats/stats.h](https://docs.zephyrproject.org/latest/doxygen/html/stats_2stats_8h_source.html)
- [stats_group_find()](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#ga8cb611a313ede400835eb56a4d209c7a)
- [STATS_SECT_START](https://docs.zephyrproject.org/latest/doxygen/html/group__stats__apis.html#gae8e85c3ce2d901f4668d7237b19999fe)

<a id="header-details"></a>

---

[上一章](P084_stat_mgmt_entry_结构体.md) · [返回大纲](大纲.md) · [下一章](P086_stats_name_map_结构体.md)
