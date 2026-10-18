---
id: learning.zephyr-docs.api-guides.api_vendor
title: 厂商专用API放置规则
kind: reference
status: maintained
domains: [zephyr, api]
source_url: https://docs.zephyrproject.org/latest/develop/api/vendor_interfaces_policy.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_厂商专用API放置规则

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/api/vendor_interfaces_policy.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML摘要见[来源记录](../SOURCES.md)。

## 6.1\_概述

本规则定义如何在Zephyr中提交、组织和暴露厂商专用硬件能力，使公共API保持稳定，避免厂商扩展绕过标准API生命周期，并为可能跨厂商使用的能力演进为通用驱动类别提供路径。

除非满足Zephyr正式[API生命周期](P004_API生命周期.md)的纳入条件，否则不得将厂商专用API暴露为公共Zephyr接口。原页概括的生命周期为实验性→稳定→弃用；详细阶段以生命周期页为准。本质上只绑定单个SoC或厂商的能力，必须封装在该厂商的SoC目录内。这为贡献者和维护者提供一致的判断方法。

## 6.2\_指导原则

**公共Zephyr API不应含厂商专用接口。**置于 `include/zephyr/` 下的接口应能经历标准生命周期；不能满足这种演进要求的厂商接口不得作为公共API暴露。

**优先选择通用方案。**若硬件能力适用于多个厂商，或将来可能如此，应作为已有**驱动类别（Driver Class）**的一部分实现，或建立新的跨厂商驱动类别。

**厂商专用能力必须封装。**仅属于某厂商的机制应放在其平台命名空间内，例如SoC或开发板目录。

**保留演进可能。**目录放置不能妨碍将来把厂商实现提升为可移植的Zephyr驱动类别。

## 6.3\_决策过程

增加硬件能力或厂商行为时，必须按顺序判断：

1. **逻辑上是否扩展现有驱动类别？**如果是，扩展现有类别，不新建厂商专用API。
2. **是否可能成为跨厂商驱动类别？**如果硬件概念并非明显只属于单一厂商，或者类似模式可能出现在多种架构上，则创建新驱动类别。
3. **是否明确为厂商专用且难以通用化？**如果是，头文件和实现均置于：

```text
soc/<vendor>/..
```

这有助于真正封装、长期维护，并在停止支持某SoC时干净移除。具体而言，头文件放在 `soc/<vendor>/include`，实现放在 `soc/<vendor>/common` 或 `soc/<vendor>/<series>`。

这些接口是厂商内部或私有接口，用于支持其专有硬件。审查会特别关注它们，防止形成互不相通的厂商功能。使用这类接口的应用不应期待生命周期或向后兼容保证。

## 6.4\_允许的目录位置

### 6.4.1\_扩展已有驱动类别

位置：

```text
include/zephyr/drivers/<class>.h
drivers/<class>/
```

适用于能力能归入或扩展现有类别的情况。

### 6.4.2\_已有类别的厂商扩展

位置：

```text
include/zephyr/drivers/<class>/
drivers/<class>/
```

适用于已有类别的厂商专用扩展，但其核心概念并非单一厂商独有，将来可能标准化。

### 6.4.3\_创建跨厂商新类别

位置：

```text
include/zephyr/drivers/<class>.h
drivers/<class>/
```

适用于能力有合理机会用于多个厂商，或演进为通用抽象的情况。

### 6.4.4\_厂商专用的SoC内部代码

这是厂商独有能力的默认安排：头文件在 `soc/<vendor>/include`，实现代码在 `soc/<vendor>/common` 或 `soc/<vendor>/<series>`。

适用于仅属于某厂商／SoC、且不准备作为公共API提供的能力。

> 译注：原页保留“已有类别的厂商扩展”这一分支，但限定其核心概念有跨厂商标准化潜力；不能将其理解为任何私有接口都可放入公共头文件目录。以上路径均相对于Zephyr源码根，`<vendor>`、`<series>`、`<class>` 是需替换的分类名称。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：API设计指南](P005_API设计指南.md) · [本模块主线目录](../reading/api_guides.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：API设计指南](P005_API设计指南.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
