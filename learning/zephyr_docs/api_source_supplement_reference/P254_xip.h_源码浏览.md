---
id: learning.zephyr-docs.api-source-supplement-reference.page-254
title: xip.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/xip_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第254章\_xip.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/xip_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/xip_8h.html)。

## 254.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="foldopen00017"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="axip_8h_html_a9fc66361388dd0b0f9761039791e8c29"></a>

```c
/*
 * Copyright The Zephyr Project Contributors
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_ARCH_COMMON_XIP_H_
#define ZEPHYR_INCLUDE_ARCH_COMMON_XIP_H_

#ifndef _ASMLANGUAGE
#ifdef __cplusplus
extern "C" {
#endif

#ifdef CONFIG_XIP
void arch_data_copy(void);
#else
static inline void arch_data_copy(void)
{
        /* Do nothing */
}
#endif /* CONFIG_XIP */
#ifdef __cplusplus
}
#endif

#endif  /* _ASMLANGUAGE */
#endif /* ZEPHYR_INCLUDE_ARCH_COMMON_XIP_H_ */
```

## 254.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：The Zephyr Project Contributors。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 19 行

不执行任何操作（Do nothing）。

### 注释 3：原第 21 行

条件编译配置（Configuration）标记：`CONFIG_XIP`。

### 注释 4：原第 26 行

条件编译标记：`_ASMLANGUAGE`。

### 注释 5：原第 27 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_ARCH_COMMON_XIP_H_`。

## 254.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/xip_8h.html)
- [arch_data_copy](https://docs.zephyrproject.org/latest/doxygen/html/xip_8h.html#a9fc66361388dd0b0f9761039791e8c29)

---

[上一章](P253_xg29-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P255_ztest_mock.h_源码浏览.md)
