---
id: learning.zephyr-docs.dt-node-reference.page-2
title: 设备树chosen节点宏
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-generic-chosen.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_设备树chosen节点宏

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-generic-chosen.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：按[本册大纲](大纲.md)区分总线、所选节点、CPU遍历与依赖序号，先理解宏返回的对象再组合使用。源码跟踪译注与官方原文分开标示。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_ga3412d0acecffa828984cf9e2c89889ed"></a>

```c
#define DT_CHOSEN(prop)
```

相关声明：[DT_CHOSEN](#ga3412d0acecffa828984cf9e2c89889ed)。

取得/chosen节点属性对应的节点标识符。

<a id="r_ga9df6bacab5f579284f5f3c1e4856cd15"></a>

```c
#define DT_HAS_CHOSEN(prop)
```

相关声明：[DT_HAS_CHOSEN](#ga9df6bacab5f579284f5f3c1e4856cd15)。

检查设备树是否具有/chosen节点。

## 2.2\_详细说明（Detailed Documentation）

<a id="ga3412d0acecffa828984cf9e2c89889ed"></a>

### `DT_CHOSEN`

```c
#define DT_CHOSEN ( prop)
```

```c
#include <zephyr/devicetree.h>
```

展开值（Value）：

```c
DT_CAT(DT_CHOSEN_, prop)
```

取得/chosen节点属性对应的节点标识符。

只有DT_HAS_CHOSEN(prop)为1时，使用此宏才有效。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prop` | /chosen节点的属性名，采用小写字母和下划线形式。 |

返回（Returns）：所选节点属性对应的节点标识符。

<a id="ga9df6bacab5f579284f5f3c1e4856cd15"></a>

### `DT_HAS_CHOSEN`

```c
#define DT_HAS_CHOSEN ( prop)
```

```c
#include <zephyr/devicetree.h>
```

展开值（Value）：

```c
IS_ENABLED(DT_CAT3(DT_CHOSEN_, prop, _EXISTS))
```

检查设备树是否具有/chosen节点。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `prop` | 采用小写字母和下划线形式的设备树属性。 |

返回（Returns）：所选属性存在且引用了一个节点时为1，否则为0。

> 译注——源码核对：检查的对象：DT_HAS_CHOSEN(prop)的摘要说检查/chosen节点，但实际按传入的prop检查相应所选属性是否存在且指向节点，不是只判断/chosen这个容器是否存在。DT_CHOSEN返回该属性引用的节点标识，不是/chosen节点本身。

## 2.3\_源码定位与版本边界

本册收录总线、chosen、CPU和依赖顺序四组宏，以及CPU／依赖顺序头文件参考与源码。相对源码定位：[devicetree.h](../../../include/zephyr/devicetree.h)、[cpu.h](../../../include/zephyr/devicetree/cpu.h)、[ordinals.h](../../../include/zephyr/devicetree/ordinals.h)和[生成脚本](../../../scripts/dts/gen_defines.py)。本次官方文件摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：属性名：设备树中的逗号和连字符在宏参数中用下划线形式表达，例如zephyr,console对应zephyr_console。参数是预处理标记，不是运行时字符串；使用DT_CHOSEN之前应保证DT_HAS_CHOSEN为1，不能把不存在属性当成可自动返回NULL的普通函数。

> 译注——源码核对：存在与就绪：生成器为chosen_nodes中的条目生成节点引用及_EXISTS=1。所选引用存在不等于驱动启用、节点status为okay或设备初始化成功；这些条件应分别按需要检查，不能只用DT_HAS_CHOSEN判断硬件是否可用。

> 译注——源码核对：版本与范围：本册仅翻译所列官方页面。CPU和依赖顺序源码去掉注释与展示空白后与本次官方头文件一致；总线和chosen展开式结合本次devicetree.h及生成脚本核对。相对源码定位用于跟踪，不把任意本地基线视为与滚动main相同。本次未编译展开示例或进行CPU、总线、初始化及实板实验。

本次验证范围为文档与源码对照，未编译或执行CPU、总线、初始化、宏边界及实板实验。

## 2.4\_原页交叉引用（Cross References）

- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)

<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_ga111fe4e9d63758262fc6810a782cb32a"></a>

---

[上一章](P001_设备树总线查询宏.md) · [返回大纲](大纲.md) · [下一章](P003_设备树CPU节点宏.md)
