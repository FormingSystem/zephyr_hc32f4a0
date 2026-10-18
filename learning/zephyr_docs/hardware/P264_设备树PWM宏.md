---
id: learning.zephyr-docs.hardware.pwmext-3
title: 设备树PWM宏
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-pwms.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第264章\_设备树PWM宏

原文：[group__devicetree-pwms](https://docs.zephyrproject.org/latest/doxygen/html/group__devicetree-pwms.html)。读取日期：2026-10-13，官方 `latest` 文档版本。

## 264.1\_头文件与公共参数

这些宏从 **设备树（Devicetree）**的 `pwms` 属性中取得 **脉宽调制（Pulse Width Modulation，PWM）**控制器、通道、周期和标志。声明来自 `zephyr/devicetree/pwms.h`。

PWM 描述符（PWM Specifier）由指向控制器的节点句柄（Phandle）及其参数单元（Cell）组成。绑定（Binding）规定参数单元的名称；需要确认时应查阅节点绑定。下文的通道宏要求参数单元名为 `channel`，周期宏要求名为 `period`，标志宏读取 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

| 参数 | 含义 |
| --- | --- |
| `node_id` | 具有 `pwms` 属性的节点标识符（Node Identifier） |
| `inst` | 与驱动兼容标识 `DT_DRV_COMPAT` 匹配的实例编号；`DT_DRV_INST(inst)` 取得其节点标识符 |
| `idx` | `pwms` 属性中的逻辑索引（Logical Index），从零开始 |
| `name` | 节点 `pwm-names` 属性定义的元素名，以小写字母和下划线形式传入 |
| `cell` | 所需参数单元名称，以小写字母和下划线形式传入 |

没有 `_BY_IDX` 或 `_BY_NAME` 后缀的宏都读取索引 `0`。返回控制器的宏得到的是节点标识符；返回参数单元的宏得到的是单元值。

## 264.2\_实例的参数单元

<a id="ga199804a2d06c301f19c5c8de232ede15"></a>

宏 `DT_INST_PWMS_CELL(inst, cell)` 从实例的 `pwms` 属性中按索引 `0`取得指定 `cell` 的值。原展开如下：

```c
DT_INST_PWMS_CELL_BY_IDX(inst, 0, cell)
```

<a id="gad106bf22d9dc90384519cd6ccc8fd1c6"></a>

宏 `DT_INST_PWMS_CELL_BY_IDX(inst, idx, cell)` 从实例的 `pwms` 属性中按索引 `idx`取得指定 `cell` 的值。原展开如下：

```c
DT_PWMS_CELL_BY_IDX(DT_DRV_INST(inst), idx, cell)
```

<a id="ga5731d949be09461f5da040e451cc509c"></a>

宏 `DT_INST_PWMS_CELL_BY_NAME(inst, name, cell)` 从实例的 `pwms` 属性中按名称 `name`取得指定 `cell` 的值。原展开如下：

```c
DT_PWMS_CELL_BY_NAME(DT_DRV_INST(inst), name, cell)
```

## 264.3\_实例的通道

<a id="gad871b89fd1b2d62aae84dc35a0819032"></a>

宏 `DT_INST_PWMS_CHANNEL(inst)` 从实例的 `pwms` 属性中按索引 `0`取得`channel` 参数单元值。原展开如下：

```c
DT_INST_PWMS_CHANNEL_BY_IDX(inst, 0)
```

<a id="ga154ece84d782a7df2ce31b2a34f43870"></a>

宏 `DT_INST_PWMS_CHANNEL_BY_IDX(inst, idx)` 从实例的 `pwms` 属性中按索引 `idx`取得`channel` 参数单元值。原展开如下：

```c
DT_INST_PWMS_CELL_BY_IDX(inst, idx, channel)
```

<a id="ga60901952d81e29dbfbbe88ee3ffe3e17"></a>

宏 `DT_INST_PWMS_CHANNEL_BY_NAME(inst, name)` 从实例的 `pwms` 属性中按名称 `name`取得`channel` 参数单元值。原展开如下：

```c
DT_INST_PWMS_CELL_BY_NAME(inst, name, channel)
```

这些宏仅适用于具有名为 `channel` 的参数单元的 PWM 描述符；必要时检查绑定。

## 264.4\_实例的控制器

<a id="ga2f79a0a48e08c89bac58d16d9731e683"></a>

宏 `DT_INST_PWMS_CTLR(inst)` 从实例的 `pwms` 属性中按索引 `0`取得PWM 控制器节点标识符。原展开如下：

```c
DT_INST_PWMS_CTLR_BY_IDX(inst, 0)
```

<a id="ga4f751ba5f3c1aad5d62178b166f36c24"></a>

宏 `DT_INST_PWMS_CTLR_BY_IDX(inst, idx)` 从实例的 `pwms` 属性中按索引 `idx`取得PWM 控制器节点标识符。原展开如下：

```c
DT_PWMS_CTLR_BY_IDX(DT_DRV_INST(inst), idx)
```

<a id="gae66d3e710496bff9789996ddb72e1ebe"></a>

宏 `DT_INST_PWMS_CTLR_BY_NAME(inst, name)` 从实例的 `pwms` 属性中按名称 `name`取得PWM 控制器节点标识符。原展开如下：

```c
DT_PWMS_CTLR_BY_NAME(DT_DRV_INST(inst), name)
```

## 264.5\_实例的标志

<a id="ga5ca45d33eae6b50012e8c052e3bd5df0"></a>

宏 `DT_INST_PWMS_FLAGS(inst)` 从实例的 `pwms` 属性中按索引 `0`取得[`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 参数单元值。原展开如下：

```c
DT_INST_PWMS_FLAGS_BY_IDX(inst, 0)
```

<a id="ga9cfbc4e3c0ab9d419cfb7700a5b42ced"></a>

宏 `DT_INST_PWMS_FLAGS_BY_IDX(inst, idx)` 从实例的 `pwms` 属性中按索引 `idx`取得[`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 参数单元值。原展开如下：

```c
DT_INST_PWMS_CELL_BY_IDX(inst, idx, flags)
```

<a id="ga23a8815368cbd82a8673e00abdfeab6b"></a>

宏 `DT_INST_PWMS_FLAGS_BY_NAME(inst, name)` 从实例的 `pwms` 属性中按名称 `name`取得[`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 参数单元值。原展开如下：

```c
DT_INST_PWMS_CELL_BY_NAME(inst, name, flags)
```

原文规定：没有 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 参数单元时返回 `0`。

> 译注：本页给出的实例版 `_BY_IDX`、`_BY_NAME` 展开使用通用参数单元宏，而后面的节点版明确使用带 `_OR` 的缺省宏。这里保留原说明和原展开，不将它们擅自改成一致；依赖缺省值前应核对所用版本的头文件。

## 264.6\_实例的周期

<a id="ga2b122199764cff41c04bad243f4456dc"></a>

宏 `DT_INST_PWMS_PERIOD(inst)` 从实例的 `pwms` 属性中按索引 `0`取得`period` 参数单元值。原展开如下：

```c
DT_INST_PWMS_PERIOD_BY_IDX(inst, 0)
```

<a id="ga7e7408507ecdac75cb7c9ba2b9176ec8"></a>

宏 `DT_INST_PWMS_PERIOD_BY_IDX(inst, idx)` 从实例的 `pwms` 属性中按索引 `idx`取得`period` 参数单元值。原展开如下：

```c
DT_INST_PWMS_CELL_BY_IDX(inst, idx, period)
```

<a id="ga7ac719270232e67f91bc65e3786be1a1"></a>

宏 `DT_INST_PWMS_PERIOD_BY_NAME(inst, name)` 从实例的 `pwms` 属性中按名称 `name`取得`period` 参数单元值。原展开如下：

```c
DT_INST_PWMS_CELL_BY_NAME(inst, name, period)
```

这些宏仅适用于具有名为 `period` 的参数单元的 PWM 描述符；必要时检查绑定。

## 264.7\_节点的参数单元

<a id="ga2062b31a090c05ccd267ae1468b182ef"></a>

宏 `DT_PWMS_CELL(node_id, cell)` 等价于读取索引 `0` 的 `cell` 参数单元，返回该单元值：

```c
DT_PWMS_CELL_BY_IDX(node_id, 0, cell)
```

<a id="ga0c1ab3329448f92936d57a83b5b3594e"></a>

宏 `DT_PWMS_CELL_BY_IDX(node_id, idx, cell)` 返回 `pwms` 中索引 `idx` 的描述符所含 `cell` 参数单元值，基于 [`DT_PHA_BY_IDX()`](../dt_property_reference/P001_设备树属性读取宏.md#ga118b63fd22c20ef940ac2fa073c126ed)：

```c
DT_PHA_BY_IDX(node_id, pwms, idx, cell)
```

原设备树片段中的 `PWM_POLARITY_NORMAL` 表示正常极性（Normal Polarity），`PWM_POLARITY_INVERTED` 表示反向极性（Inverted Polarity）。片段如下：

```dts
pwm1: pwm-controller@... {
        compatible = "vnd,pwm";
        #pwm-cells = <2>;
};

pwm2: pwm-controller@... {
        compatible = "vnd,pwm";
        #pwm-cells = <2>;
};

n: node {
        pwms = <&pwm1 1 200000 PWM_POLARITY_NORMAL>,
               <&pwm2 3 100000 PWM_POLARITY_INVERTED>;
};
```

假设两个控制器的绑定都声明以下参数单元：

```yaml
pwm-cells:
  - channel
  - period
  - flags
```

则用法和所得值如下。其中 `DT_NODELABEL()` 从节点标签取得节点标识符；`PWM_POLARITY_NORMAL` 为正常极性，`PWM_POLARITY_INVERTED` 为反向极性。

```c
DT_PWMS_CELL_BY_IDX(DT_NODELABEL(n), 0, channel) // 1
DT_PWMS_CELL_BY_IDX(DT_NODELABEL(n), 1, channel) // 3
DT_PWMS_CELL_BY_IDX(DT_NODELABEL(n), 0, period)  // 200000
DT_PWMS_CELL_BY_IDX(DT_NODELABEL(n), 1, period)  // 100000
DT_PWMS_CELL_BY_IDX(DT_NODELABEL(n), 0, flags)   // PWM_POLARITY_NORMAL
DT_PWMS_CELL_BY_IDX(DT_NODELABEL(n), 1, flags)   // PWM_POLARITY_INVERTED
```

> 译注：上面的官方片段写了 `#pwm-cells = <2>`，绑定和调用却使用 `channel`、`period`、[`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 三个参数单元。这是原示例的不一致，代码按原文保留；不能原样作为已验证的设备树配置使用。

<a id="ga69233198a489283068bc1ded5072ca26"></a>

宏 `DT_PWMS_CELL_BY_NAME(node_id, name, cell)` 返回 `pwm-names` 所命名元素的 `cell` 参数单元值，基于 [`DT_PHA_BY_NAME()`](../dt_property_reference/P001_设备树属性读取宏.md#gae469615356a867c49416da15bdc44a26)：

```c
DT_PHA_BY_NAME(node_id, pwms, name, cell)
```

原文的命名片段如下：

```dts
pwm1: pwm-controller@... {
        compatible = "vnd,pwm";
        #pwm-cells = <2>;
};

pwm2: pwm-controller@... {
        compatible = "vnd,pwm";
        #pwm-cells = <2>;
};

n: node {
        pwms = <&pwm1 1 200000 PWM_POLARITY_NORMAL>,
               <&pwm2 3 100000 PWM_POLARITY_INVERTED>;
        pwm-names = "alpha", "beta";
};
```

两个控制器的绑定同样声明：

```yaml
pwm-cells:
  - channel
  - period
  - flags
```

于是可以按 `alpha`、`beta` 名称取得参数单元：

```c
DT_PWMS_CELL_BY_NAME(DT_NODELABEL(n), alpha, channel) // 1
DT_PWMS_CELL_BY_NAME(DT_NODELABEL(n), beta, channel)  // 3
DT_PWMS_CELL_BY_NAME(DT_NODELABEL(n), alpha, period)  // 200000
DT_PWMS_CELL_BY_NAME(DT_NODELABEL(n), beta, period)   // 100000
DT_PWMS_CELL_BY_NAME(DT_NODELABEL(n), alpha, flags)   // PWM_POLARITY_NORMAL
DT_PWMS_CELL_BY_NAME(DT_NODELABEL(n), beta, flags)    // PWM_POLARITY_INVERTED
```

> 译注：这个按名称访问的示例也保留了同一个参数单元数量不一致问题。

## 264.8\_节点的通道

<a id="gaeb0a10ad37fdfd3dcc75bd379908acdc"></a>

宏 `DT_PWMS_CHANNEL(node_id)` 返回索引 `0` 的通道参数单元值：

```c
DT_PWMS_CHANNEL_BY_IDX(node_id, 0)
```

<a id="ga10a372e44c7e3feb551ca996c6ca5a8f"></a>

宏 `DT_PWMS_CHANNEL_BY_IDX(node_id, idx)` 返回索引 `idx` 的 `channel` 参数单元值：

```c
DT_PWMS_CELL_BY_IDX(node_id, idx, channel)
```

<a id="ga59a4b9884e9620eac04c3808a3a6d164"></a>

宏 `DT_PWMS_CHANNEL_BY_NAME(node_id, name)` 返回命名元素的 `channel` 参数单元值：

```c
DT_PWMS_CELL_BY_NAME(node_id, name, channel)
```

以上宏仅适用于具有名为 `channel` 的参数单元的 PWM 描述符；必要时检查节点绑定。后两者分别等价于相应的通用参数单元宏以 `channel` 为最后一个参数的调用。

## 264.9\_节点的控制器

<a id="gaff7a0b201d97a1d1bb1893b556d5a194"></a>

宏 `DT_PWMS_CTLR(node_id)` 返回索引 `0` 的 PWM 控制器节点标识符：

```c
DT_PWMS_CTLR_BY_IDX(node_id, 0)
```

<a id="ga2f16d00a53717a66668fb8bc967acce5"></a>

宏 `DT_PWMS_CTLR_BY_IDX(node_id, idx)` 返回索引 `idx` 的 PWM 控制器节点标识符：

```c
DT_PHANDLE_BY_IDX(node_id, pwms, idx)
```

原设备树片段：

```dts
pwm1: pwm-controller@... { ... };

pwm2: pwm-controller@... { ... };

n: node {
        pwms = <&pwm1 1 PWM_POLARITY_NORMAL>,
               <&pwm2 3 PWM_POLARITY_INVERTED>;
};
```

原用法与所得节点标识符：

```c
DT_PWMS_CTLR_BY_IDX(DT_NODELABEL(n), 0) // DT_NODELABEL(pwm1)
DT_PWMS_CTLR_BY_IDX(DT_NODELABEL(n), 1) // DT_NODELABEL(pwm2)
```

原文另指向 [`DT_PROP_BY_PHANDLE_IDX()`](../dt_property_reference/P001_设备树属性读取宏.md#gaeba973992914d493cff5506ecf86a00d) 作为相关接口。

<a id="ga6922e69c707219cd766fe317484dac8a"></a>

宏 `DT_PWMS_CTLR_BY_NAME(node_id, name)` 返回命名元素的 PWM 控制器节点标识符，相关宏为 [`DT_PHANDLE_BY_NAME()`](../dt_property_reference/P001_设备树属性读取宏.md#ga65c90d2d96255b8569c5b869b637c2fd)：

```c
DT_PHANDLE_BY_NAME(node_id, pwms, name)
```

原设备树片段第一部分以代码块呈现：

```dts
pwm1: pwm-controller@... { ... };
```

原页面紧接着以正文形式显示片段余下内容，下面保持其内容并放入代码块便于阅读：

```dts
pwm2: pwm-controller... { ... };
n: node { pwms = <&pwm1 1 PWM_POLARITY_NORMAL>, <&pwm2 3 PWM_POLARITY_INVERTED>; pwm-names = "alpha", "beta"; };
```

对应调用为：

```c
DT_PWMS_CTLR_BY_NAME(DT_NODELABEL(n), alpha) // DT_NODELABEL(pwm1)
DT_PWMS_CTLR_BY_NAME(DT_NODELABEL(n), beta)  // DT_NODELABEL(pwm2)
```

> 译注：这两个控制器示例包含省略号，参数布局也与前面的三参数示例不同；按名称示例的 `pwm2` 节点名还缺少 `@`。它们用于示意节点引用和查找关系，并非可以直接编译的完整配置。

## 264.10\_节点的标志

<a id="ga8dcd2d18129504d1a4ab71ae05c48c44"></a>

宏 `DT_PWMS_FLAGS(node_id)` 返回索引 `0` 的 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 参数单元值；没有该单元时返回 `0`：

```c
DT_PWMS_FLAGS_BY_IDX(node_id, 0)
```

<a id="gaf9c1ac7f3a39f4022f3ec31ef8de98e6"></a>

宏 `DT_PWMS_FLAGS_BY_IDX(node_id, idx)` 返回索引 `idx` 的 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 参数单元值；没有该单元时返回 `0`：

```c
DT_PHA_BY_IDX_OR(node_id, pwms, idx, flags, 0)
```

<a id="ga7a1621bfb223da23aa030b64fc0c0bcd"></a>

宏 `DT_PWMS_FLAGS_BY_NAME(node_id, name)` 返回命名元素的 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 参数单元值；没有该单元时返回 `0`：

```c
DT_PHA_BY_NAME_OR(node_id, pwms, name, flags, 0)
```

这些宏预期描述符中有名为 `flags` 的参数单元，必要时参照绑定确认。原文将按索引版本描述为等价于 `DT_PWMS_CELL_BY_IDX(node_id, idx, flags)`；按名称版本则明确限定：有 `flags` 时等价于 `DT_PWMS_CELL_BY_NAME(node_id, name, flags)`，否则展开为 `0`。

> 译注：按索引版本展示的实际展开也含有缺省值 `0`，因此原文所说的通用参数单元宏等价关系不能忽略“没有 `flags`”这一分支。

## 264.11\_节点的周期

<a id="gac6006a723932325b96a1b50619be153b"></a>

宏 `DT_PWMS_PERIOD(node_id)` 返回索引 `0` 的周期参数单元值：

```c
DT_PWMS_PERIOD_BY_IDX(node_id, 0)
```

<a id="ga9456f65777e6fc7c057c6e0709c9245f"></a>

宏 `DT_PWMS_PERIOD_BY_IDX(node_id, idx)` 返回索引 `idx` 的 `period` 参数单元值：

```c
DT_PWMS_CELL_BY_IDX(node_id, idx, period)
```

<a id="ga74af83d31fc38f331808dedfaecf4c74"></a>

宏 `DT_PWMS_PERIOD_BY_NAME(node_id, name)` 返回命名元素的 `period` 参数单元值：

```c
DT_PWMS_CELL_BY_NAME(node_id, name, period)
```

以上宏仅适用于具有名为 `period` 的参数单元的 PWM 描述符；必要时检查节点绑定。按索引和按名称版本分别等价于相应通用参数单元宏以 `period` 为最后一个参数的调用。

---

[上一章：MAX31790PWM扩展](P263_MAX31790PWM扩展.md) · [下一章：WisBlockPWM通道](P265_WisBlockPWM通道.md) · [返回大纲](大纲.md)
