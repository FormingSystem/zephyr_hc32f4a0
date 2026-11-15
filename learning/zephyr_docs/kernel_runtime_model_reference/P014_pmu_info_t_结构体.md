---
id: learning.zephyr-docs.kernel-runtime-model-reference.page-14
title: pmu_info_t_结构体
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpmu__info__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_pmu\_info\_t\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpmu__info__t.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

没有架构补充实现（Arch Supplement）时使用的pmu_info_t占位类型。

```c
#include <zephyr/arch/pmu.h>
```

<a id="details"></a>

没有架构补充实现（Arch Supplement）时使用的pmu_info_t占位类型。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 14.1\_数据成员（Data Fields）

<a id="r_a20ad7ea312a6f3199078d9cdb7c224f1"></a>

```c
uint32_t implementer
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[implementer](#a20ad7ea312a6f3199078d9cdb7c224f1)。

后端报告的性能监测单元（PMU）实现者标识值。

<a id="r_a5b11627370ddcc76202fd7c59f6e7e3d"></a>

```c
uint32_t idcode
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[idcode](#a5b11627370ddcc76202fd7c59f6e7e3d)。

后端报告的性能监测单元（PMU）部件号或ID代码。

## 14.2\_详细说明（Detailed Documentation）

<a id="a5b11627370ddcc76202fd7c59f6e7e3d"></a>

### `idcode`

```c
uint32_t pmu_info_t::idcode
```

后端报告的性能监测单元（PMU）部件号或ID代码。

<a id="a20ad7ea312a6f3199078d9cdb7c224f1"></a>

### `implementer`

```c
uint32_t pmu_info_t::implementer
```

后端报告的性能监测单元（PMU）实现者标识值。

本数据类型文档由以下文件生成：

- `zephyr/arch/pmu.h`

## 14.3\_原页交叉引用（Cross References）

- [pmu_info_t](P014_pmu_info_t_结构体.md)
- [zephyr/arch/pmu.h](https://docs.zephyrproject.org/latest/doxygen/html/pmu_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P013_pmu_counter_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P015_sys_getopt_option_结构体.md)
