---
id: learning.zephyr-docs.api-source-reference.page-862
title: testing.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/testing_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第862章\_testing.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/testing_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/testing_8h.html)。

## 862.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="anet__buf_8h_html"></a>
<a id="astructnet__buf_html"></a>
<a id="atesting_8h_html_a818681eaff28ef3f170c7329920e508d"></a>
<a id="atesting_8h_html_aa1b44cdccf5bdbae54334fef4859d886"></a>
<a id="atesting_8h_html_ad881c44e84d8ba4650a33ef6bae19c4c"></a>

```c
/* Copyright (c) 2024 Nordic Semiconductor ASA
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_BLUETOOTH_TESTING_H_
#define ZEPHYR_INCLUDE_BLUETOOTH_TESTING_H_

#include <zephyr/net_buf.h>

void bt_testing_trace_event_acl_pool_destroy(struct net_buf *buf);

void bt_testing_trace_ext_adv_reassembly_timeout(void);

void bt_testing_trace_ext_adv_reassembly_complete(void);

#endif /* ZEPHYR_INCLUDE_BLUETOOTH_TESTING_H_ */
```

## 862.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 45 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_BLUETOOTH_TESTING_H_`。

## 862.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/testing_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [bt_testing_trace_event_acl_pool_destroy](https://docs.zephyrproject.org/latest/doxygen/html/testing_8h.html#ad881c44e84d8ba4650a33ef6bae19c4c)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bt_testing_trace_ext_adv_reassembly_timeout](https://docs.zephyrproject.org/latest/doxygen/html/testing_8h.html#a818681eaff28ef3f170c7329920e508d)
- [bt_testing_trace_ext_adv_reassembly_complete](https://docs.zephyrproject.org/latest/doxygen/html/testing_8h.html#aa1b44cdccf5bdbae54334fef4859d886)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)

---

[上一章](P861_test_toolchain.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P863_ti-cc13xx-cc26xx-gpio.h_源码浏览.md)
