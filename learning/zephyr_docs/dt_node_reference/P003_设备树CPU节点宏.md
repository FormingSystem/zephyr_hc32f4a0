---
id: learning.zephyr-docs.dt-node-reference.page-3
title: 设备树CPU节点宏
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-cpu.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_设备树CPU节点宏

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-cpu.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：按[本册大纲](大纲.md)区分总线、所选节点、CPU遍历与依赖序号，先理解宏返回的对象再组合使用。源码跟踪译注与官方原文分开标示。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="r_ga7d0c6fb9a2421a46cebab16be1bf94a8"></a>

```c
#define DT_FOREACH_CPU(fn)
```

相关声明：[DT_FOREACH_CPU](#ga7d0c6fb9a2421a46cebab16be1bf94a8)。

对设备树/cpus节点中device_type为cpu的每个子节点调用fn。

<a id="r_ga7aa0d5f554d538fe43483671020422b4"></a>

```c
#define DT_FOREACH_CPU_SEP(fn, sep)
```

相关声明：[DT_FOREACH_CPU_SEP](#ga7aa0d5f554d538fe43483671020422b4)。

对设备树/cpus节点中device_type为cpu的每个子节点调用fn，并附加分隔符（Separator）。

<a id="r_ga2778cf7e4d983b95330f8578c20c5567"></a>

```c
#define DT_FOREACH_CPU_VARGS(fn, ...)
```

相关声明：[DT_FOREACH_CPU_VARGS](#ga2778cf7e4d983b95330f8578c20c5567)。

对设备树/cpus节点中device_type为cpu的每个子节点调用fn，并传递多个参数。

<a id="r_ga286a7fba9707d8994c6c5e9bea14e4a8"></a>

```c
#define DT_FOREACH_CPU_SEP_VARGS(fn, sep, ...)
```

相关声明：[DT_FOREACH_CPU_SEP_VARGS](#ga286a7fba9707d8994c6c5e9bea14e4a8)。

对设备树/cpus节点中device_type为cpu的每个子节点调用fn，附加分隔符并传递多个参数。

<a id="r_ga35f31b2094458055d5f44f29f71a0857"></a>

```c
#define DT_FOREACH_CPU_STATUS_OKAY(fn)
```

相关声明：[DT_FOREACH_CPU_STATUS_OKAY](#ga35f31b2094458055d5f44f29f71a0857)。

对设备树/cpus节点中device_type为cpu且status为okay的每个子节点调用fn。

<a id="r_gacef0f90236a41c2ae231e51fe66bd971"></a>

```c
#define DT_FOREACH_CPU_STATUS_OKAY_SEP(fn, sep)
```

相关声明：[DT_FOREACH_CPU_STATUS_OKAY_SEP](#gacef0f90236a41c2ae231e51fe66bd971)。

对设备树/cpus节点中device_type为cpu且status为okay的每个子节点调用fn，并附加分隔符。

<a id="r_gac4f4e7d5a2e8efbcf1091107f87a76f9"></a>

```c
#define DT_FOREACH_CPU_STATUS_OKAY_SEP_VARGS(fn, sep, ...)
```

相关声明：[DT_FOREACH_CPU_STATUS_OKAY_SEP_VARGS](#gac4f4e7d5a2e8efbcf1091107f87a76f9)。

对设备树/cpus节点中device_type为cpu且status为okay的每个子节点调用fn，附加分隔符并传递多个参数。

## 3.2\_详细说明（Detailed Documentation）

<a id="ga7d0c6fb9a2421a46cebab16be1bf94a8"></a>

### `DT_FOREACH_CPU`

```c
#define DT_FOREACH_CPU ( fn)
```

```c
#include <zephyr/devicetree/cpu.h>
```

展开值（Value）：

```c
DT_FOREACH_CHILD_VARGS(DT_PATH(cpus), DT_FOREACH_CPU_INTERNAL, fn)
```

对设备树/cpus节点中device_type为cpu的每个子节点调用fn。

宏fn必须接收一个参数，即/cpus下device_type = "cpu"的子节点标识符。/cpus下device_type不为cpu的子节点会被跳过。

设备树（Devicetree）片段示例：

原始示例（Example）：

```dts
cpus {
        cpu0: cpu@0 {
                device_type = "cpu";
                reg = <0>;
        };
        cpu1: cpu@1 {
                device_type = "cpu";
                reg = <1>;
        };
        power-states {
                idle: idle { ... };
        };
};
```

使用示例：

原始示例（Example）：

```c
#define REG_AND_COMMA(node_id) DT_REG_ADDR(node_id),

const uint32_t cpu_regs[] = {
    DT_FOREACH_CPU(REG_AND_COMMA)
};
```

展开为：

原始示例（Example）：

```c
const uint32_t cpu_regs[] = {
    0, 1,
};
```

注意，power-states会被跳过，因为它的device_type不是cpu。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fn` | 要调用的宏。 |

> 译注——源码核对：原文与筛选实现：原文描述只处理device_type值为cpu的子节点；本次cpu.h的内部宏实际只使用DT_NODE_HAS_PROP(node_id, device_type)检查该属性是否存在，没有在宏中比较字符串值。正常CPU绑定约束应与原文约定配合，但不能把宏自身描述为对任意输入都进行了值校验。示例power-states没有该属性，所以会被跳过。

<a id="ga7aa0d5f554d538fe43483671020422b4"></a>

### `DT_FOREACH_CPU_SEP`

```c
#define DT_FOREACH_CPU_SEP ( fn, sep )
```

```c
#include <zephyr/devicetree/cpu.h>
```

展开值（Value）：

```c
DT_FOREACH_CHILD_VARGS(DT_PATH(cpus), DT_FOREACH_CPU_SEP_INTERNAL, fn, sep)
```

对设备树/cpus节点中device_type为cpu的每个子节点调用fn，并附加分隔符（Separator）。

宏fn必须接收一个参数，即/cpus下device_type = "cpu"的子节点标识符。/cpus下device_type不为cpu的子节点会被跳过。

sep放在fn的每次调用之后，并非仅放在两次调用之间。因此展开结果带有尾部分隔符；这适用于初始化器，因为尾随逗号是合法的。

使用示例：

原始示例（Example）：

```c
const uint32_t cpu_regs[] = {
    DT_FOREACH_CPU_SEP(DT_REG_ADDR, (,))
};
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fn` | 要调用的宏。 |
| `sep` | 放在fn每次调用之后的分隔符，例如逗号或分号。必须用圆括号包围，以便能够传入逗号作为分隔符。 |

另见（See Also）：DT_FOREACH_CPU。

> 译注——源码核对：尾随分隔符：SEP内部实现为fn(...)后接DT_DEBRACKET_INTERNAL sep，因此每次保留的节点都会带分隔符，最后一次也有。传入逗号须写(,)，分号可写(;)。这与只在相邻元素之间插入分隔符的常见遍历形式不同，组合表达式前应核对语法。

<a id="ga286a7fba9707d8994c6c5e9bea14e4a8"></a>

### `DT_FOREACH_CPU_SEP_VARGS`

```c
#define DT_FOREACH_CPU_SEP_VARGS ( fn, sep, ... )
```

```c
#include <zephyr/devicetree/cpu.h>
```

展开值（Value）：

```c
DT_FOREACH_CHILD_VARGS(DT_PATH(cpus), DT_FOREACH_CPU_SEP_VARGS_INTERNAL, fn, sep,          \
                       __VA_ARGS__)
```

对设备树/cpus节点中device_type为cpu的每个子节点调用fn，附加分隔符并传递多个参数。

宏fn接收多个参数，其余参数由调用者传入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fn` | 要调用的宏。 |
| `sep` | 放在fn每次调用之后的分隔符，例如逗号或分号。必须用圆括号包围，以便能够传入逗号作为分隔符。 |
| `...` | 要传递给fn的可变数量参数（Variable Arguments）。 |

另见（See Also）：DT_FOREACH_CPU_SEP。

<a id="ga35f31b2094458055d5f44f29f71a0857"></a>

### `DT_FOREACH_CPU_STATUS_OKAY`

```c
#define DT_FOREACH_CPU_STATUS_OKAY ( fn)
```

```c
#include <zephyr/devicetree/cpu.h>
```

展开值（Value）：

```c
DT_FOREACH_CHILD_VARGS(DT_PATH(cpus), DT_FOREACH_CPU_STATUS_OKAY_INTERNAL, fn)
```

对设备树/cpus节点中device_type为cpu且status为okay的每个子节点调用fn。

此宏按子节点在最终设备树中出现的顺序遍历/cpus的子节点，还会跳过status不是okay的子节点。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fn` | 要调用的宏。 |

另见（See Also）：DT_FOREACH_CPU。

<a id="gacef0f90236a41c2ae231e51fe66bd971"></a>

### `DT_FOREACH_CPU_STATUS_OKAY_SEP`

```c
#define DT_FOREACH_CPU_STATUS_OKAY_SEP ( fn, sep )
```

```c
#include <zephyr/devicetree/cpu.h>
```

展开值（Value）：

```c
DT_FOREACH_CHILD_VARGS(DT_PATH(cpus), DT_FOREACH_CPU_STATUS_OKAY_SEP_INTERNAL, fn, sep)
```

对设备树/cpus节点中device_type为cpu且status为okay的每个子节点调用fn，并附加分隔符。

此宏按子节点在最终设备树中出现的顺序遍历/cpus的子节点，还会跳过status不是okay的子节点。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fn` | 要调用的宏。 |
| `sep` | 放在fn每次调用之后的分隔符，例如逗号或分号。必须用圆括号包围，以便能够传入逗号作为分隔符。 |

另见（See Also）：DT_FOREACH_CPU_SEP。

<a id="gac4f4e7d5a2e8efbcf1091107f87a76f9"></a>

### `DT_FOREACH_CPU_STATUS_OKAY_SEP_VARGS`

```c
#define DT_FOREACH_CPU_STATUS_OKAY_SEP_VARGS ( fn, sep, ... )
```

```c
#include <zephyr/devicetree/cpu.h>
```

展开值（Value）：

```c
DT_FOREACH_CHILD_VARGS(DT_PATH(cpus), DT_FOREACH_CPU_STATUS_OKAY_SEP_VARGS_INTERNAL, fn,   \
                       sep, __VA_ARGS__)
```

对设备树/cpus节点中device_type为cpu且status为okay的每个子节点调用fn，附加分隔符并传递多个参数。

此宏按子节点在最终设备树中出现的顺序遍历/cpus的子节点，还会跳过status不是okay的子节点。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fn` | 要调用的宏。 |
| `sep` | 放在fn每次调用之后的分隔符，例如逗号或分号。必须用圆括号包围，以便能够传入逗号作为分隔符。 |
| `...` | 要传递给fn的可变数量参数（Variable Arguments）。 |

另见（See Also）：DT_FOREACH_CPU_STATUS_OKAY_SEP。

<a id="ga2778cf7e4d983b95330f8578c20c5567"></a>

### `DT_FOREACH_CPU_VARGS`

```c
#define DT_FOREACH_CPU_VARGS ( fn, ... )
```

```c
#include <zephyr/devicetree/cpu.h>
```

展开值（Value）：

```c
DT_FOREACH_CHILD_VARGS(DT_PATH(cpus), DT_FOREACH_CPU_VARGS_INTERNAL, fn, __VA_ARGS__)
```

对设备树/cpus节点中device_type为cpu的每个子节点调用fn，并传递多个参数。

宏fn接收多个参数。第一个参数应为/cpus子节点的节点标识符，其余参数由调用者传入。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fn` | 要调用的宏。 |
| `...` | 要传递给fn的可变数量参数（Variable Arguments）。 |

另见（See Also）：DT_FOREACH_CPU。

## 3.3\_源码定位与版本边界

本册收录总线、chosen、CPU和依赖顺序四组宏，以及CPU／依赖顺序头文件参考与源码。相对源码定位：[devicetree.h](../../../include/zephyr/devicetree.h)、[cpu.h](../../../include/zephyr/devicetree/cpu.h)、[ordinals.h](../../../include/zephyr/devicetree/ordinals.h)和[生成脚本](../../../scripts/dts/gen_defines.py)。本次官方文件摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：遍历范围：宏通过DT_FOREACH_CHILD_VARGS遍历/cpus的直接子节点，不递归枚举任意后代，也不是运行时CPU枚举函数。普通版本不筛选status，STATUS_OKAY版本才进一步使用DT_NODE_HAS_STATUS_OKAY；它遵循Zephyr设备树对缺省status的规则，不应把“未写status”直接判成disabled。

> 译注——源码核对：参数和顺序：fn是宏名，单参数版本接收节点标识；VARGS版本把调用者额外参数接在节点标识之后。按最终设备树顺序展开，不保证按reg数值排序，也不代表运行时核心上线或调度顺序。/cpus节点、生成头文件及宏定义必须在当前构建上下文可用。

> 译注——源码核对：版本与范围：本册仅翻译所列官方页面。CPU和依赖顺序源码去掉注释与展示空白后与本次官方头文件一致；总线和chosen展开式结合本次devicetree.h及生成脚本核对。相对源码定位用于跟踪，不把任意本地基线视为与滚动main相同。本次未编译展开示例或进行CPU、总线、初始化及实板实验。

本次验证范围为文档与源码对照，未编译或执行CPU、总线、初始化、宏边界及实板实验。

## 3.4\_原页交叉引用（Cross References）

- [zephyr/devicetree/cpu.h](P005_设备树CPU头文件参考.md)
- [DT_FOREACH_CHILD_VARGS](../dt_foreach_reference/P001_设备树遍历宏.md#gae7461e9fa4687bf88cdd7c76f30986de)
- [DT_PATH](../dt_identity_reference/P001_设备树节点标识宏.md#ga015b4819473797982e83cae497697086)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [DT_REG_ADDR](../dt_reg_reference/P001_设备树寄存器属性宏.md#gac6d8279c32351ced4c0ac7f32270974e)

<a id="details"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-generic-foreach_html_gae7461e9fa4687bf88cdd7c76f30986de"></a>
<a id="agroup__devicetree-generic-id_html_ga015b4819473797982e83cae497697086"></a>
<a id="agroup__devicetree-cpu_html_ga7d0c6fb9a2421a46cebab16be1bf94a8"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="agroup__devicetree-cpu_html_ga7aa0d5f554d538fe43483671020422b4"></a>
<a id="agroup__devicetree-reg-prop_html_gac6d8279c32351ced4c0ac7f32270974e"></a>

---

[上一章](P002_设备树chosen节点宏.md) · [返回大纲](大纲.md) · [下一章](P004_设备树依赖顺序宏.md)
