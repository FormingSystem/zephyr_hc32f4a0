---
id: learning.zephyr-docs.api-source-reference.page-35
title: arducam_mega.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/arducam__mega_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第35章\_arducam\_mega.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/arducam__mega_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/arducam__mega_8h.html)。

## 35.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>

```c



#ifndef ZEPHYR_INCLUDE_DRIVERS_CAMERA_ARDUCAM_MEGA_H_
#define ZEPHYR_INCLUDE_DRIVERS_CAMERA_ARDUCAM_MEGA_H_

#ifdef __cplusplus
extern "C" {
#endif

#define VIDEO_CID_ARDUCAM_RESET    (VIDEO_CID_PRIVATE_BASE + 1)

#define VIDEO_CID_ARDUCAM_LOWPOWER (VIDEO_CID_PRIVATE_BASE + 2)

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_CAMERA_ARDUCAM_MEGA_H_ */
```

## 35.2\_可见注释译文（Comments）

### 注释 1：原第 30 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_CAMERA_ARDUCAM_MEGA_H_`。

## 35.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/arducam__mega_8h.html)

---

[上一章](P034_arducam-ffc-40pin-connector.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P036_arduino-header-r3.h_源码浏览.md)
