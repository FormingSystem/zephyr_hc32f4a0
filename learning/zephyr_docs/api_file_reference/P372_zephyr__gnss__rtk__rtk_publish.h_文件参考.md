---
id: learning.zephyr-docs.api-file-reference.page-372
title: zephyr__gnss__rtk__rtk_publish.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rtk__publish_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第372章\_zephyr\_\_gnss\_\_rtk\_\_rtk\_publish.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rtk__publish_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <stddef.h>
#include <zephyr/gnss/rtk/rtk.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 372.1\_函数（Functions）

<a id="r_a50e9d50ca4e24b28f9982d8849bd1476"></a>

```c
void gnss_rtk_publish_data (const struct gnss_rtk_data *data)
```

相关声明：[gnss_rtk_publish_data](#a50e9d50ca4e24b28f9982d8849bd1476)、[gnss_rtk_data](../sensor_navigation_model_reference/P013_gnss_rtk_data_结构体.md)。

## 372.2\_详细说明（Detailed Documentation）

<a id="a50e9d50ca4e24b28f9982d8849bd1476"></a>

### `gnss_rtk_publish_data()`

```c
void gnss_rtk_publish_data ( const struct gnss_rtk_data * data)
```


## 372.3\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/gnss/rtk/rtk.h](../api_source_reference/P733_rtk.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P170_rtk_publish.h_源码浏览.md)
- [gnss_rtk_data](../sensor_navigation_model_reference/P013_gnss_rtk_data_结构体.md)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P371_zephyr__gnss__rtk__rtk.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P373_zephyr__dt-bindings__clock__rts5817_clock.h_文件参考.md)
