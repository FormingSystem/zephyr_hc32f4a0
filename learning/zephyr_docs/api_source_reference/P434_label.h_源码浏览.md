---
id: learning.zephyr-docs.api-source-reference.page-434
title: label.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/label_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第434章\_label.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/label_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/label_8h.html)。

## 434.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="foldopen00031"></a>
<a id="l00031"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="astructprometheus__label_html"></a>
<a id="astructprometheus__label_html_a0cf2605f8904b2cd7ad14273816681b6"></a>
<a id="astructprometheus__label_html_a484ae44cbfdea3d66b010c765829da88"></a>

```c
/*
 * Copyright (c) 2024 Mustafa Abdullah Kus, Sparse Technology
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_PROMETHEUS_LABEL_H_
#define ZEPHYR_INCLUDE_NET_PROMETHEUS_LABEL_H_


#if defined(CONFIG_PROMETHEUS)
#define MAX_PROMETHEUS_LABELS_PER_METRIC CONFIG_PROMETHEUS_LABEL_MAX_COUNT
#else
#define MAX_PROMETHEUS_LABELS_PER_METRIC 1
#endif /* CONFIG_PROMETHEUS */

struct prometheus_label {
        const char *key;
        const char *value;
};


#endif /* ZEPHYR_INCLUDE_NET_PROMETHEUS_LABEL_H_ */
```

## 434.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Mustafa Abdullah Kus, Sparse Technology。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 24 行

条件编译配置（Configuration）标记：`CONFIG_PROMETHEUS`。

### 注释 3：原第 42 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_PROMETHEUS_LABEL_H_`。

## 434.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/label_8h.html)
- [prometheus_label](../network_service_model_reference/P050_prometheus_label_结构体.md)
- [key](../network_service_model_reference/P050_prometheus_label_结构体.md#a484ae44cbfdea3d66b010c765829da88)
- [value](../network_service_model_reference/P050_prometheus_label_结构体.md#a0cf2605f8904b2cd7ad14273816681b6)
- [prometheus_label::value](../network_service_model_reference/P050_prometheus_label_结构体.md#a0cf2605f8904b2cd7ad14273816681b6)
- [prometheus_label::key](../network_service_model_reference/P050_prometheus_label_结构体.md#a484ae44cbfdea3d66b010c765829da88)

---

[上一章](P433_l2cap_br.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P435_large_comp_data_cli.h_源码浏览.md)
