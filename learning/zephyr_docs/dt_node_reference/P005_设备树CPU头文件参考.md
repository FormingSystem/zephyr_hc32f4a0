---
id: learning.zephyr-docs.dt-node-reference.page-5
title: 设备树CPU头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2cpu_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_设备树CPU头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/devicetree_2cpu_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：按[本册大纲](大纲.md)区分总线、所选节点、CPU遍历与依赖序号，先理解宏返回的对象再组合使用。源码跟踪译注与官方原文分开标示。

CPU设备树宏的公共API头文件。

<a id="details"></a>

```c
#include <zephyr/devicetree.h>
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

CPU设备树宏的公共API头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.1\_宏定义（Macros）

<a id="r_ga7d0c6fb9a2421a46cebab16be1bf94a8"></a>

```c
#define DT_FOREACH_CPU(fn)
```

相关声明：[DT_FOREACH_CPU](P003_设备树CPU节点宏.md#ga7d0c6fb9a2421a46cebab16be1bf94a8)。

对设备树/cpus节点中device_type为cpu的每个子节点调用fn。

<a id="r_ga7aa0d5f554d538fe43483671020422b4"></a>

```c
#define DT_FOREACH_CPU_SEP(fn, sep)
```

相关声明：[DT_FOREACH_CPU_SEP](P003_设备树CPU节点宏.md#ga7aa0d5f554d538fe43483671020422b4)。

对设备树/cpus节点中device_type为cpu的每个子节点调用fn，并附加分隔符（Separator）。

<a id="r_ga2778cf7e4d983b95330f8578c20c5567"></a>

```c
#define DT_FOREACH_CPU_VARGS(fn, ...)
```

相关声明：[DT_FOREACH_CPU_VARGS](P003_设备树CPU节点宏.md#ga2778cf7e4d983b95330f8578c20c5567)。

对设备树/cpus节点中device_type为cpu的每个子节点调用fn，并传递多个参数。

<a id="r_ga286a7fba9707d8994c6c5e9bea14e4a8"></a>

```c
#define DT_FOREACH_CPU_SEP_VARGS(fn, sep, ...)
```

相关声明：[DT_FOREACH_CPU_SEP_VARGS](P003_设备树CPU节点宏.md#ga286a7fba9707d8994c6c5e9bea14e4a8)。

对设备树/cpus节点中device_type为cpu的每个子节点调用fn，附加分隔符并传递多个参数。

<a id="r_ga35f31b2094458055d5f44f29f71a0857"></a>

```c
#define DT_FOREACH_CPU_STATUS_OKAY(fn)
```

相关声明：[DT_FOREACH_CPU_STATUS_OKAY](P003_设备树CPU节点宏.md#ga35f31b2094458055d5f44f29f71a0857)。

对设备树/cpus节点中device_type为cpu且status为okay的每个子节点调用fn。

<a id="r_gacef0f90236a41c2ae231e51fe66bd971"></a>

```c
#define DT_FOREACH_CPU_STATUS_OKAY_SEP(fn, sep)
```

相关声明：[DT_FOREACH_CPU_STATUS_OKAY_SEP](P003_设备树CPU节点宏.md#gacef0f90236a41c2ae231e51fe66bd971)。

对设备树/cpus节点中device_type为cpu且status为okay的每个子节点调用fn，并附加分隔符。

<a id="r_gac4f4e7d5a2e8efbcf1091107f87a76f9"></a>

```c
#define DT_FOREACH_CPU_STATUS_OKAY_SEP_VARGS(fn, sep, ...)
```

相关声明：[DT_FOREACH_CPU_STATUS_OKAY_SEP_VARGS](P003_设备树CPU节点宏.md#gac4f4e7d5a2e8efbcf1091107f87a76f9)。

对设备树/cpus节点中device_type为cpu且status为okay的每个子节点调用fn，附加分隔符并传递多个参数。

## 5.2\_源码定位与版本边界

本册收录总线、chosen、CPU和依赖顺序四组宏，以及CPU／依赖顺序头文件参考与源码。相对源码定位：[devicetree.h](../../../include/zephyr/devicetree.h)、[cpu.h](../../../include/zephyr/devicetree/cpu.h)、[ordinals.h](../../../include/zephyr/devicetree/ordinals.h)和[生成脚本](../../../scripts/dts/gen_defines.py)。本次官方文件摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：原文与筛选实现：原文描述只处理device_type值为cpu的子节点；本次cpu.h的内部宏实际只使用DT_NODE_HAS_PROP(node_id, device_type)检查该属性是否存在，没有在宏中比较字符串值。正常CPU绑定约束应与原文约定配合，但不能把宏自身描述为对任意输入都进行了值校验。示例power-states没有该属性，所以会被跳过。

> 译注——源码核对：遍历范围：宏通过DT_FOREACH_CHILD_VARGS遍历/cpus的直接子节点，不递归枚举任意后代，也不是运行时CPU枚举函数。普通版本不筛选status，STATUS_OKAY版本才进一步使用DT_NODE_HAS_STATUS_OKAY；它遵循Zephyr设备树对缺省status的规则，不应把“未写status”直接判成disabled。

> 译注——源码核对：参数和顺序：fn是宏名，单参数版本接收节点标识；VARGS版本把调用者额外参数接在节点标识之后。按最终设备树顺序展开，不保证按reg数值排序，也不代表运行时核心上线或调度顺序。/cpus节点、生成头文件及宏定义必须在当前构建上下文可用。

> 译注——源码核对：尾随分隔符：SEP内部实现为fn(...)后接DT_DEBRACKET_INTERNAL sep，因此每次保留的节点都会带分隔符，最后一次也有。传入逗号须写(,)，分号可写(;)。这与只在相邻元素之间插入分隔符的常见遍历形式不同，组合表达式前应核对语法。

> 译注——源码核对：版本与范围：本册仅翻译所列官方页面。CPU和依赖顺序源码去掉注释与展示空白后与本次官方头文件一致；总线和chosen展开式结合本次devicetree.h及生成脚本核对。相对源码定位用于跟踪，不把任意本地基线视为与滚动main相同。本次未编译展开示例或进行CPU、总线、初始化及实板实验。

本次验证范围为文档与源码对照，未编译或执行CPU、总线、初始化、宏边界及实板实验。

## 5.3\_原页交叉引用（Cross References）

- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码](P006_设备树CPU头文件源码.md)
- [DT_FOREACH_CPU](P003_设备树CPU节点宏.md#ga7d0c6fb9a2421a46cebab16be1bf94a8)
- [DT_FOREACH_CPU_SEP](P003_设备树CPU节点宏.md#ga7aa0d5f554d538fe43483671020422b4)
- [DT_FOREACH_CPU_VARGS](P003_设备树CPU节点宏.md#ga2778cf7e4d983b95330f8578c20c5567)
- [DT_FOREACH_CPU_SEP_VARGS](P003_设备树CPU节点宏.md#ga286a7fba9707d8994c6c5e9bea14e4a8)
- [DT_FOREACH_CPU_STATUS_OKAY](P003_设备树CPU节点宏.md#ga35f31b2094458055d5f44f29f71a0857)
- [DT_FOREACH_CPU_STATUS_OKAY_SEP](P003_设备树CPU节点宏.md#gacef0f90236a41c2ae231e51fe66bd971)
- [DT_FOREACH_CPU_STATUS_OKAY_SEP_VARGS](P003_设备树CPU节点宏.md#gac4f4e7d5a2e8efbcf1091107f87a76f9)

<a id="header-details"></a>

---

[上一章](P004_设备树依赖顺序宏.md) · [返回大纲](大纲.md) · [下一章](P006_设备树CPU头文件源码.md)
