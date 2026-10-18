---
id: learning.zephyr-docs.devicetree.api-usage
title: 从 C 与 C++ 访问设备树
kind: reference
status: maintained
domains: [zephyr, devicetree, api]
source_url: https://docs.zephyrproject.org/latest/build/dts/api-usage.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第12章\_从C与C++访问设备树

原文：[Devicetree access from C/C++](https://docs.zephyrproject.org/latest/build/dts/api-usage.html)。读取日期：2026-10-12，`latest`。

本页介绍 `<zephyr/devicetree.h>` 中从 C 源码读取设备树的 **应用程序编程接口（Application Programming Interface，API）**，假定已理解[设备树概念](P001_设备树介绍.md)与[绑定](P008_绑定概述.md)。完整接口参考见[设备树参考](https://docs.zephyrproject.org/latest/build/dts/api/api.html)。

## 12.1\_与Linux使用方式的区别

熟悉 Linux 的读者要注意，两者使用设备树的方式差别很大。Linux 内核在运行时解析二进制设备树，例如用于加载和初始化驱动；Zephyr 则把所有设备树数据生成到 C 头文件，再通过宏 API 抽象访问。

Zephyr 面向的设备资源较少，二进制设备树及配套运行时处理代码占用过大，因此采用构建时处理。

## 12.2\_节点标识符

读取节点信息前，需要 node identifier（节点标识符），它是引用节点的 C 宏。主要获取方式如下：

| 方式 | API 与用途 |
| --- | --- |
| 路径 | `DT_PATH()` 从根开始给出完整路径，适合已知准确位置时 |
| 节点标签 | `DT_NODELABEL()`；**片上系统（System on Chip，SoC）** DTSI 常提供与手册对应的 `i2c1`、`spi2` 等标签 |
| 别名 | `DT_ALIAS()` 从 `/aliases` 属性取得；应用可只关心“用户 **发光二极管（Light-Emitting Diode，LED）**”而不绑定某个硬件节点，例如 Blinky 的 led0。`DT_HAS_ALIAS()` 可检查别名存在 |
| 实例编号 | `DT_INST()` 按 compatible 对应实例获取，主要供驱动使用；编号不能随意假定 |
| chosen | `DT_CHOSEN()` 取得 `/chosen` 属性指定的节点 |
| 父子关系 | 从已有标识符使用 `DT_PARENT()` 或 `DT_CHILD()` |

指向同一节点的标识符相同，可互换。以下虚构硬件是本页贯穿示例：

```dts
/dts-v1/;

/ {
	aliases {
		sensor-controller = &i2c1;
	};

	soc {
		i2c1: i2c@40002000 {
			compatible = "vnd,soc-i2c";
			label = "I2C_1";
			reg = <0x40002000 0x1000>;
			status = "okay";
			clock-frequency = <100000>;
		};
	};
};
```

取得 `i2c@40002000` 的几种写法为 `DT_PATH(soc, i2c_40002000)`、`DT_NODELABEL(i2c1)`、`DT_ALIAS(sensor_controller)`，以及编号尚需确定的 `DT_INST(x, vnd_soc_i2c)`。**设备树源文件（Devicetree Source，DTS）** 名称转换为 C 参数时要小写，并把 `-`、`@` 等非字母数字字符换成 `_`。

> 译注：原例保留了历史 `label` 属性，本页的节点宏不依赖它；新绑定不建议新增该属性，见[重要属性](P003_语法与结构.md)。地址是虚构示例，不用于 HC32 配置。

### 12.2.1\_节点标识符不是运行时数值

不能把节点标识符存入变量，以下写法会产生编译错误：

```c
/* These will give you compiler errors: */

void *i2c_0 = DT_INST(0, vnd_soc_i2c);
unsigned int i2c_1 = DT_INST(1, vnd_soc_i2c);
long my_i2c = DT_NODELABEL(i2c1);
```

要减少重复输入，应定义 C 宏：

```c
/* Use something like this instead: */

#define MY_I2C DT_NODELABEL(i2c1)

#define INST(i) DT_INST(i, vnd_soc_i2c)
#define I2C_0 INST(0)
#define I2C_1 INST(1)
```

## 12.3\_读取属性

正确 API 取决于节点及属性类型；普通属性、寄存器、中断和 phandle 使用不同接口。

### 12.3.1\_检查属性与基本值

`DT_NODE_HAS_PROP()` 检查属性是否存在，分别展开为 1 和 0：

```c
DT_NODE_HAS_PROP(DT_NODELABEL(i2c1), clock_frequency)  /* expands to 1 */
DT_NODE_HAS_PROP(DT_NODELABEL(i2c1), not_a_property)   /* expands to 0 */
```

整数、布尔、字符串、数值数组和字符串数组可用 `DT_PROP(node_id, property)`。上例时钟频率用以下写法读取，结果都是 100000：

```c
DT_PROP(DT_PATH(soc, i2c_40002000), clock_frequency)  /* This is 100000, */
DT_PROP(DT_NODELABEL(i2c1), clock_frequency)          /* and so is this, */
DT_PROP(DT_ALIAS(sensor_controller), clock_frequency) /* and this. */
```

DTS 的 `clock-frequency` 在 C 中写成 `clock_frequency`；属性名同样需要小写和特殊字符替换。字符串属性展开为字符串字面量，布尔属性为 0 或 1：

```c
#define I2C1 DT_NODELABEL(i2c1)

DT_PROP(I2C1, status)  /* expands to the string literal "okay" */
```

**布尔属性应使用 `DT_PROP()`，不要用 `DT_NODE_HAS_PROP()` 读取布尔值。** 它会按属性存在与否展开为 1 或 0。

array、uint8-array、string-array 会让 `DT_PROP()` 展开为数组初始化器。例如：

```dts
foo: foo@1234 {
        a = <1000 2000 3000>; /* array */
        b = [aa bb cc dd];    /* uint8-array */
        c = "bar", "baz";     /* string-array */
};
```

在 C 中读取：

```c
#define FOO DT_NODELABEL(foo)

int a[] = DT_PROP(FOO, a);           /* {1000, 2000, 3000} */
unsigned char b[] = DT_PROP(FOO, b); /* {0xaa, 0xbb, 0xcc, 0xdd} */
char* c[] = DT_PROP(FOO, c);         /* {"bar", "baz"} */
```

用 `DT_PROP_LEN()` 取得逻辑元素数：

```c
size_t a_len = DT_PROP_LEN(FOO, a); /* 3 */
size_t b_len = DT_PROP_LEN(FOO, b); /* 4 */
size_t c_len = DT_PROP_LEN(FOO, c); /* 2 */
```

这里依次为 3、4、2。`DT_PROP_LEN()` 不能用于特殊的 `reg` 或 `interrupts`，它们有专用接口。

### 12.3.2\_reg属性

`DT_NUM_REGS(node_id)` 取得寄存器块数量。不能用 `DT_PROP(node, reg)` 读取块地址和长度；只有一个块时用 `DT_REG_ADDR(node_id)` 和 `DT_REG_SIZE(node_id)`，多个块时用 `DT_REG_ADDR_BY_IDX(node_id, idx)` 和 `DT_REG_SIZE_BY_IDX(node_id, idx)`。

idx 必须是整数常量，或无需算术求值就展开为整数常量的宏，不能是变量。以下运行时循环会编译失败：

```c
/* This will cause a compiler error. */

for (size_t i = 0; i < DT_NUM_REGS(node_id); i++) {
        size_t addr = DT_REG_ADDR_BY_IDX(node_id, i);
}
```

### 12.3.3\_interrupts属性

`DT_NUM_IRQS(node_id)` 取得中断说明项数，通用读取宏为：

```c
DT_IRQ_BY_IDX(node_id, idx, val)
```

idx 是 interrupts 的逻辑项索引，val 是该中断说明项中某个 cell 的名字，应查相关绑定确定。多数绑定有名为 irq 的 cell，表示中断号；`DT_IRQN` 可方便地取得经过处理的中断号。

这里“处理”指设备树脚本为适应某些 SoC 限制及 Zephyr 多级中断编号规则，对 `zephyr.dts` 中的编号进行转换。原文提示这一部分尚缺少充分文档，编写驱动时需要查处理脚本和现有驱动。

### 12.3.4\_phandle属性

通过 `&another-node` 引用其他节点的属性，其绑定类型为 phandle、phandles 或 phandle-array。按类型可用 `DT_PHANDLE`、`DT_PHANDLE_BY_IDX`、`DT_PHANDLE_BY_NAME` 转成节点标识符，概念详见[phandle 指南](https://docs.zephyrproject.org/latest/build/dts/phandles.html)。

常见用途是引用其他硬件，再从节点标识符取得驱动层 `struct device`，见[操作指南](P006_设备树操作指南.md)。另一个用途是读取 phandle-array 中的说明项参数，通用接口为 `DT_PHA_BY_IDX`、`DT_PHA`，**通用输入输出（General-Purpose Input/Output，GPIO）** 则有 `DT_GPIO_CTLR_BY_IDX`、`DT_GPIO_CTLR`、`DT_GPIO_PIN_BY_IDX`、`DT_GPIO_PIN`、`DT_GPIO_FLAGS_BY_IDX`、`DT_GPIO_FLAGS` 等简写。

可用 `DT_PHA_HAS_CELL_AT_IDX` 和 `DT_PROP_HAS_IDX` 检查相关说明项内容是否存在。

## 12.4\_其他接口与驱动便利宏

其他常用 API 包括：`DT_CHOSEN`、`DT_HAS_CHOSEN` 处理 `/chosen`；`DT_HAS_COMPAT_STATUS_OKAY`、`DT_NODE_HAS_COMPAT` 分别作全局或节点范围的 compatible 检查；`DT_BUS` 取得总线控制器；`DT_ENUM_IDX` 用于固定枚举值属性。

固定及映射 Flash 分区也有相应[设备树 API](https://docs.zephyrproject.org/latest/build/dts/api/api.html)；[Flash map](https://docs.zephyrproject.org/latest/services/storage/flash_map/flash_map.html)在它们之上提供更便于使用的接口。

驱动常依赖实例编号。先把 `DT_DRV_COMPAT` 定义为驱动支持的 compatible 的 C token 形式，也就是通常传给 `DT_INST` 的值，就可简写实例访问：

```c
#include <zephyr/devicetree.h>

#define DT_DRV_COMPAT my_driver_compat

/* This is same thing as DT_INST(0, my_driver_compat): */
DT_DRV_INST(0)

/*
 * This is the same thing as
 * DT_PROP(DT_INST(0, my_driver_compat), clock_frequency)
 */
DT_INST_PROP(0, clock_frequency)
```

`DT_DRV_INST(0)` 等价于 `DT_INST(0, my_driver_compat)`；`DT_INST_PROP(0, clock_frequency)` 等价于 `DT_PROP(DT_INST(0, my_driver_compat), clock_frequency)`。通用实例接口和硬件专用便利宏见[设备树 API 参考](https://docs.zephyrproject.org/latest/build/dts/api/api.html)。硬件专用宏建立在上述 API 之上，以改善相应代码的可读性。

## 12.5\_自动生成宏的语法说明

`zephyr/devicetree.h` 本身不是生成文件，但它依赖每次应用构建产生的 `devicetree_generated.h`。生成宏的命名复杂，公共 API 将其隐藏；它们属于实现细节，但常出现在编译错误中，理解形式有助于排错。

原文使用扩充巴科斯范式（ABNF）描述生成宏，语法见 [RFC 7405](https://www.rfc-editor.org/rfc/rfc7405)及其扩展的 [RFC 5234](https://www.rfc-editor.org/rfc/rfc5234)。下面先逐组翻译注释含义，再保留完整语法和原注释，方便与生成头文件逐项对照。本语法只覆盖直接生成的 `DT_` 宏，不包括经 Kconfig 提取的 `CONFIG_SRAM_BASE_ADDRESS` 等宏。

### 12.5.1\_节点宏

顶层 `dt-macro` 分为与具体节点相关的 node-macro 和其他类型 other-macro。节点宏可以描述属性、pinctrl、GPIO hog、map，也可以表示以下信息：

- `_EXISTS`：节点存在。
- `_BUS`：总线控制器；附加 `spi`、`i2c` 等 dt-name 后缀用于匹配总线类型。
- `_CLASS_...`：绑定声明的设备 API 类成员关系，例如 adc。
- `_REG_...`：寄存器块数量、按索引/名称存在性、地址/大小，以及遍历各块的辅助宏。
- `_IRQ_...`：中断数量、层级、索引/名称、cell 值和控制器。
- `_RANGES_...`：ranges 数量、条目存在性、子总线标志、子总线地址、父总线地址和长度，另有遍历辅助宏。
- `_PARTITION_ID...`：fixed-partitions 子节点各自的唯一序号。
- `_COMPAT_...`：每个 compatible 的匹配信息、厂商与型号字段。
- `_BINDING_COMPAT_TOKEN`、`_BINDING_COMPAT_UPPER_TOKEN`、`_BINDING_COMPAT_UNQUOTED`：真正匹配绑定的 compatible，分别作为 token、大写 token、不带引号字符串；只为有匹配绑定的节点定义。
- `_PARENT`：所有非根节点的父节点标识符。
- `_FOREACH_PROP_ELEM...`：遍历属性元素；带 SEP、VARGS 的变体供相应公共宏使用。
- `_CHILD_NUM`、`_CHILD_NUM_STATUS_OKAY`：子节点数及启用子节点数。
- `_DESCENDANT_NUM_ON_BUS_...`：控制器下某种总线的后代数，可仅计 okay；排除子总线控制器后面的后代。
- `_CHILD_UNIT_ADDR_INT_...`：供 `DT_CHILD_BY_UNIT_ADDR_INT` 使用。
- `_FOREACH_CHILD...`、`_FOREACH_CHILD_STATUS_OKAY...`：遍历全部或已启用子节点的内部辅助宏。
- `_FOREACH_NODELABEL...`、`_NODELABEL_NUM`：遍历/统计节点标签。
- `_CHILD_IDX`：当前节点在父节点子列表中从 0 开始的索引。
- `_STATUS_...`：如 okay、disabled 的状态。
- `_ORD`：表示依赖关系的非负序号；`_REQUIRES_ORDS` 是直接依赖的序号，`_SUPPORTS_ORDS` 是反向直接依赖的序号。
- `_PATH`、`_FULL_NAME`：节点路径和 name@unit-addr 的字符串字面量。

### 12.5.2\_pinctrl、GPIO hog与map

pinctrl 有数组般的结构，但索引对应各个 `pinctrl-DIGIT` 属性，所以宏与整个节点相关，而非单一属性。原例有 pinctrl-0、pinctrl-1，名称 default、sleep；生成宏记录总数 2、索引存在性、名称存在性、名称对应索引，以及命名属性中的 phandle 节点标识符。按索引访问属性已由普通 property-macro 覆盖；额外名称宏用于表达名称到属性的隐式映射。

GPIO hog 原例中，控制器 gpio1 的 `node-1` 自动占用两条 GPIO，pin 为 0、1，flags 为 `0x10`、`0x20`，输出高；`node-2` 占用 pin 2，flags 为 `0x30`，输出低。绑定的 gpio-cells 分别名为 pin 和 flags。生成宏记录是否包含 hog、数量、逻辑索引存在性、控制器 phandle，以及 pin/flags 的存在性和值。原文指出其中 phandle 宏目前没有被 Zephyr 使用。

以 `-map` 结尾的属性还会生成 map 宏。原例 `interrupt-map = <0 1 &intc0 2 3>` 包含一个映射条目，宏分别表示条目存在、子地址长度/元素/存在性、子说明项长度/元素/存在性、父节点、父地址及父说明项的同类信息，以及四种遍历辅助宏。

> 译注：原文 GPIO hog 的 ABNF 非终结符混用了 `gpiohogs-macro` 和 `gpioshogs-macro`。下方为忠实对照保留原文拼写，不能把这个文档语法段当作已经通过 ABNF 工具验证的语法文件。map 示例中的个别宏展开注释也是示意，实际以所用版本生成文件为准。

### 12.5.3\_路径、属性及后缀

普通属性宏由节点标识与“小写加下划线”属性名组合，形式为 `DT_N_<node path>_P_<property name>`，可附加特定子值后缀。

`path-id` 把每个 `/` 变成 `_S_`，字母变小写，其他非字母数字字符变下划线。原例 `/foo@123/bar-BAZ` 对应 `_S_foo_123_S_bar_baz`。`prop-id` 对属性名进行同样大小写和字符转换，例如 `zephyr,console` 为 `zephyr_console`，`WHY,AM_I_SHOUTING` 为 `why_am_i_shouting`。

`prop-suf` 为需要细分值的情况提供后缀：规范特殊属性（reg、中断等）、数组类型、绑定枚举、设备 API 专用 phandle-array、`foo-names` 等说明项名称。例子包括 `_EXISTS` 存在标志、`_SIZE` 逻辑长度、`_IDX_<i>` 元素、`_IDX_<DIGIT>_VAL_<dt-name>` 说明项 cell、`_ADDR_<i>` 寄存器块地址及 `_LEN_<i>` 块长度。原文为避免过时没有穷举全部形式，细节须看 devicetree.h。

### 12.5.4\_其他宏和替代标识

other-macro 包括替代节点标识、某 compatible 的启用实例数量，以及供遍历全部节点、okay 节点、某 compatible 节点/实例使用的辅助宏；还有 chosen 宏、某 compatible 是否出现在特定总线、是否存在 okay 节点、设备类是否存在 okay 节点及其数量、按设备类遍历、把 label 映射到 fixed-partitions 节点、从 phandle 取得节点标签等宏。

alternate-id 提供路径之外的节点名。原例 `/soc/device@123` 的标签是 `dev_1`，别名是 dev，compatible 为 vnd,device，于是可有 `ALIAS_dev`、`NODELABEL_dev_1`、`INST_0_vnd_device`，完整宏都展开到同一 `DT_N_S_soc_S_device_123`。它们主要用来与 `_P_<prop-id>` 拼接访问属性。实例形式前缀含由脚本生成的编号，其他形式直接取设备树名称。

`dt-name` 由一个或多个小写 ASCII 字母、数字、下划线组成，对应设备树名称转成合法 C 标识符片段后的形式。`gen-name` 表示不直接来自设备树的宏名组成部分，采用大写字母、数字、下划线。`lower = %x61-7A` 表示 a–z，`upper = %x41-5A` 表示 A–Z。

### 12.5.5\_完整原文ABNF

下面完整保留生成宏语法、示例与原英文注释；各组注释含义已在上面中文说明中对应展开。

```abnf
; An RFC 7405 ABNF grammar for devicetree macros.
;
; This does *not* cover macros pulled out of DT via Kconfig,
; like CONFIG_SRAM_BASE_ADDRESS, etc. It only describes the
; ones that start with DT_ and are directly generated.

; --------------------------------------------------------------------
; dt-macro: the top level nonterminal for a devicetree macro
;
; A dt-macro starts with uppercase "DT_", and is one of:
;
; - a <node-macro>, generated for a particular node
; - some <other-macro>, a catch-all for other types of macros
dt-macro = node-macro / other-macro

; --------------------------------------------------------------------
; node-macro: a macro related to a node

; A macro about a property value
node-macro =  property-macro
; A macro about the pinctrl properties in a node.
node-macro =/ pinctrl-macro
; A macro about the GPIO hog properties in a node.
node-macro =/ gpiohogs-macro
; A macro about the map properties in a node.
node-macro =/ map-macro
; EXISTS macro: node exists in the devicetree
node-macro =/ %s"DT_N" path-id %s"_EXISTS"
; Bus macros: the plain BUS is a way to access a node's bus controller.
; The additional dt-name suffix is added to match that node's bus type;
; the dt-name in this case is something like "spi" or "i2c".
node-macro =/ %s"DT_N" path-id %s"_BUS" ["_" dt-name]
; Device class macros: declares that the node's binding declares
; membership of a device class; the dt-name is something like "adc".
node-macro =/ %s"DT_N" path-id %s"_CLASS_" dt-name
; The reg property is special and has its own macros.
node-macro =/ %s"DT_N" path-id %s"_REG_NUM"
node-macro =/ %s"DT_N" path-id %s"_REG_IDX_" DIGIT "_EXISTS"
node-macro =/ %s"DT_N" path-id %s"_REG_IDX_" DIGIT
              %s"_VAL_" ( %s"ADDRESS" / %s"SIZE")
node-macro =/ %s"DT_N" path-id %s"_REG_NAME_" dt-name
              %s"_VAL_" ( %s"ADDRESS" / %s"SIZE")
node-macro =/ %s"DT_N" path-id %s"_REG_NAME_" dt-name "_EXISTS"
node-macro =/ %s"DT_N" path-id %s"_FOREACH_REG"
node-macro =/ %s"DT_N" path-id %s"_FOREACH_REG_SEP"
node-macro =/ %s"DT_N" path-id %s"_FOREACH_REG_VARGS"
node-macro =/ %s"DT_N" path-id %s"_FOREACH_REG_SEP_VARGS"
; The interrupts property is also special.
node-macro =/ %s"DT_N" path-id %s"_IRQ_NUM"
node-macro =/ %s"DT_N" path-id %s"_IRQ_LEVEL"
node-macro =/ %s"DT_N" path-id %s"_IRQ_IDX_" DIGIT "_EXISTS"
node-macro =/ %s"DT_N" path-id %s"_IRQ_IDX_" DIGIT
              %s"_VAL_" dt-name [ %s"_EXISTS" ]
node-macro =/ %s"DT_N" path-id %s"_CONTROLLER"
node-macro =/ %s"DT_N" path-id %s"_IRQ_NAME_" dt-name
              %s"_VAL_" dt-name [ %s"_EXISTS" ]
node-macro =/ %s"DT_N" path-id %s"_IRQ_NAME_" dt-name "_CONTROLLER"
; The ranges property is also special.
node-macro =/ %s"DT_N" path-id %s"_RANGES_NUM"
node-macro =/ %s"DT_N" path-id %s"_RANGES_IDX_" DIGIT "_EXISTS"
node-macro =/ %s"DT_N" path-id %s"_RANGES_IDX_" DIGIT
              %s"_VAL_" ( %s"CHILD_BUS_FLAGS" / %s"CHILD_BUS_ADDRESS" /
                          %s"PARENT_BUS_ADDRESS" / %s"LENGTH")
node-macro =/ %s"DT_N" path-id %s"_RANGES_IDX_" DIGIT
              %s"_VAL_CHILD_BUS_FLAGS_EXISTS"
node-macro =/ %s"DT_N" path-id %s"_FOREACH_RANGE"
; Subnodes of the fixed-partitions compatible get macros which contain
; a unique ordinal value for each partition
node-macro =/ %s"DT_N" path-id %s"_PARTITION_ID" DIGIT
; Macros are generated for each of a node's compatibles;
; dt-name in this case is something like "vnd_device".
node-macro =/ %s"DT_N" path-id %s"_COMPAT_MATCHES_" dt-name
node-macro =/ %s"DT_N" path-id %s"_COMPAT_VENDOR_IDX_" DIGIT "_EXISTS"
node-macro =/ %s"DT_N" path-id %s"_COMPAT_VENDOR_IDX_" DIGIT
node-macro =/ %s"DT_N" path-id %s"_COMPAT_MODEL_IDX_" DIGIT "_EXISTS"
node-macro =/ %s"DT_N" path-id %s"_COMPAT_MODEL_IDX_" DIGIT
; The binding compatible (the compatible that matched a binding) as a token,
; uppercased token, or unquoted string. Only defined for nodes with a
; matching binding.
node-macro =/ %s"DT_N" path-id %s"_BINDING_COMPAT_TOKEN"
node-macro =/ %s"DT_N" path-id %s"_BINDING_COMPAT_UPPER_TOKEN"
node-macro =/ %s"DT_N" path-id %s"_BINDING_COMPAT_UNQUOTED"
; Every non-root node gets one of these macros, which expands to the node
; identifier for that node's parent in the devicetree.
node-macro =/ %s"DT_N" path-id %s"_PARENT"
; These are used internally by DT_FOREACH_PROP_ELEM(_SEP)(_VARGS), which
; iterates over each property element.
node-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_FOREACH_PROP_ELEM"
node-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_FOREACH_PROP_ELEM_SEP"
node-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_FOREACH_PROP_ELEM_VARGS"
node-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_FOREACH_PROP_ELEM_SEP_VARGS"
; These are used by DT_CHILD_NUM and DT_CHILD_NUM_STATUS_OKAY macros
node-macro =/ %s"DT_N" path-id %s"_CHILD_NUM"
node-macro =/ %s"DT_N" path-id %s"_CHILD_NUM_STATUS_OKAY"
; These are used by DT_DESCENDANT_NUM_ON_BUS and
; DT_DESCENDANT_NUM_ON_BUS_STATUS_OKAY
; macros to count descendants on a given bus under a controller node.
; Descendants behind child bus-controller nodes are excluded.
; dt-name in this case is something like "spi" or "i2c".
node-macro =/ %s"DT_N" path-id %s"_DESCENDANT_NUM_ON_BUS_" dt-name
node-macro =/ %s"DT_N" path-id %s"_DESCENDANT_NUM_ON_BUS_" dt-name %s"_STATUS_OKAY"
; This is used by DT_CHILD_BY_UNIT_ADDR_INT
node-macro =/ %s"DT_N" path-id %s"_CHILD_UNIT_ADDR_INT_" DIGIT
; These are used internally by DT_FOREACH_CHILD, which iterates over
; each child node.
node-macro =/ %s"DT_N" path-id %s"_FOREACH_CHILD"
node-macro =/ %s"DT_N" path-id %s"_FOREACH_CHILD_SEP"
node-macro =/ %s"DT_N" path-id %s"_FOREACH_CHILD_VARGS"
node-macro =/ %s"DT_N" path-id %s"_FOREACH_CHILD_SEP_VARGS"
; These are used internally by DT_FOREACH_CHILD_STATUS_OKAY, which iterates
; over each child node with status "okay".
node-macro =/ %s"DT_N" path-id %s"_FOREACH_CHILD_STATUS_OKAY"
node-macro =/ %s"DT_N" path-id %s"_FOREACH_CHILD_STATUS_OKAY_SEP"
node-macro =/ %s"DT_N" path-id %s"_FOREACH_CHILD_STATUS_OKAY_VARGS"
node-macro =/ %s"DT_N" path-id %s"_FOREACH_CHILD_STATUS_OKAY_SEP_VARGS"
; These are used internally by DT_FOREACH_NODELABEL and
; DT_FOREACH_NODELABEL_VARGS, which iterate over a node's node labels.
node-macro =/ %s"DT_N" path-id %s"_FOREACH_NODELABEL" [ %s"_VARGS" ]
; These are used internally by DT_NUM_NODELABELS
node-macro =/ %s"DT_N" path-id %s"_NODELABEL_NUM"
; The node's zero-based index in the list of it's parent's child nodes.
node-macro =/ %s"DT_N" path-id %s"_CHILD_IDX"
; The node's status macro; dt-name in this case is something like "okay"
; or "disabled".
node-macro =/ %s"DT_N" path-id %s"_STATUS_" dt-name
; The node's dependency ordinal. This is a non-negative integer
; value that is used to represent dependency information.
node-macro =/ %s"DT_N" path-id %s"_ORD"
; The node's path, as a string literal
node-macro =/ %s"DT_N" path-id %s"_PATH"
; The node's name@unit-addr, as a string literal
node-macro =/ %s"DT_N" path-id %s"_FULL_NAME"
; The dependency ordinals of a node's requirements (direct dependencies).
node-macro =/ %s"DT_N" path-id %s"_REQUIRES_ORDS"
; The dependency ordinals of a node supports (reverse direct dependencies).
node-macro =/ %s"DT_N" path-id %s"_SUPPORTS_ORDS"

; --------------------------------------------------------------------
; pinctrl-macro: a macro related to the pinctrl properties in a node
;
; These are a bit of a special case because they kind of form an array,
; but the array indexes correspond to pinctrl-DIGIT properties in a node.
;
; So they're related to a node, but not just one property within the node.
;
; The following examples assume something like this:
;
;      foo {
;              pinctrl-0 = <&bar>;
;              pinctrl-1 = <&baz>;
;              pinctrl-names = "default", "sleep";
;      };

; Total number of pinctrl-DIGIT properties in the node. May be zero.
;
;   #define DT_N_<node path>_PINCTRL_NUM 2
pinctrl-macro = %s"DT_N" path-id %s"_PINCTRL_NUM"
; A given pinctrl-DIGIT property exists.
;
;     #define DT_N_<node path>_PINCTRL_IDX_0_EXISTS 1
;     #define DT_N_<node path>_PINCTRL_IDX_1_EXISTS 1
pinctrl-macro =/ %s"DT_N" path-id %s"_PINCTRL_IDX_" DIGIT %s"_EXISTS"
; A given pinctrl property name exists.
;
;     #define DT_N_<node path>_PINCTRL_NAME_default_EXISTS 1
;     #define DT_N_<node path>_PINCTRL_NAME_sleep_EXISTS 1
pinctrl-macro =/ %s"DT_N" path-id %s"_PINCTRL_NAME_" dt-name %s"_EXISTS"
; The corresponding index number of a named pinctrl property.
;
;     #define DT_N_<node path>_PINCTRL_NAME_default_IDX 0
;     #define DT_N_<node path>_PINCTRL_NAME_sleep_IDX 1
pinctrl-macro =/ %s"DT_N" path-id %s"_PINCTRL_NAME_" dt-name %s"_IDX"
; The node identifier for the phandle in a named pinctrl property.
;
;    #define DT_N_<node path>_PINCTRL_NAME_default_IDX_0_PH <node id for 'bar'>
;
; There's no need for a separate macro for access by index: that's
; covered by property-macro. We only need this because the map from
; names to properties is implicit in the structure of the DT.
pinctrl-macro =/ %s"DT_N" path-id %s"_PINCTRL_NAME_" dt-name %s"_IDX_" DIGIT %s"_PH"

; --------------------------------------------------------------------
; gpiohogs-macro: a macro related to GPIO hog nodes
;
; The following examples assume something like this:
;
;     gpio1: gpio@... {
;       compatible = "vnd,gpio";
;       #gpio-cells = <2>;
;
;       node-1 {
;               gpio-hog;
;               gpios = <0x0 0x10>, <0x1 0x20>;
;               output-high;
;       };
;
;       node-2 {
;               gpio-hog;
;               gpios = <0x2 0x30>;
;               output-low;
;       };
;     };
;
; Bindings fragment for the vnd,gpio compatible:
;
;     gpio-cells:
;       - pin
;       - flags

; The node contains GPIO hogs.
;
;   #define DT_N_<node-1 path>_GPIO_HOGS_EXISTS 1
;   #define DT_N_<node-2 path>_GPIO_HOGS_EXISTS 1
gpioshogs-macro = %s"DT_N" path-id %s"_GPIO_HOGS_EXISTS"
; Number of hogged GPIOs in a node.
;
;   #define DT_N_<node-1 path>_GPIO_HOGS_NUM 2
;   #define DT_N_<node-2 path>_GPIO_HOGS_NUM 1
gpioshogs-macro =/ %s"DT_N" path-id %s"_GPIO_HOGS_NUM"
; A given logical GPIO hog array index exists.
;
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_0_EXISTS 1
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_1_EXISTS 1
;   #define DT_N_<node-2 path>_GPIO_HOGS_IDX_0_EXISTS 1
gpiohogs-macro =/ %s"DT_N" path-id %s"_GPIO_HOGS_IDX_" DIGIT %s"_EXISTS"
; The node identifier for the phandle of a logical index in the GPIO hogs array.
; These macros are currently unused by Zephyr.
;
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_0_PH <node id for 'gpio1'>
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_1_PH <node id for 'gpio1'>
;   #define DT_N_<node-2 path>_GPIO_HOGS_IDX_0_PH <node id for 'gpio1'>
gpiohogs-macro =/ %s"DT_N" path-id %s"_GPIO_HOGS_IDX_" DIGIT %s"_PH"
; The pin cell of a logical index in the GPIO hogs array exists.
;
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_0_VAL_pin_EXISTS 1
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_1_VAL_pin_EXISTS 1
;   #define DT_N_<node-2 path>_GPIO_HOGS_IDX_0_VAL_pin_EXISTS 1
gpiohogs-macro =/ %s"DT_N" path-id %s"_GPIO_HOGS_IDX_" DIGIT %s"_VAL_pin_EXISTS"
; The value of the pin cell of a logical index in the GPIO hogs array.
;
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_0_VAL_pin 0
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_1_VAL_pin 1
;   #define DT_N_<node-2 path>_GPIO_HOGS_IDX_0_VAL_pin 2
gpiohogs-macro =/ %s"DT_N" path-id %s"_GPIO_HOGS_IDX_" DIGIT %s"_VAL_pin"
; The flags cell of a logical index in the GPIO hogs array exists.
;
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_0_VAL_flags_EXISTS 1
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_1_VAL_flags_EXISTS 1
;   #define DT_N_<node-2 path>_GPIO_HOGS_IDX_0_VAL_flags_EXISTS 1
gpiohogs-macro =/ %s"DT_N" path-id %s"_GPIO_HOGS_IDX_" DIGIT %s"_VAL_flags_EXISTS"
; The value of the flags cell of a logical index in the GPIO hogs array.
;
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_0_VAL_flags 0x10
;   #define DT_N_<node-1 path>_GPIO_HOGS_IDX_1_VAL_flags 0x20
;   #define DT_N_<node-2 path>_GPIO_HOGS_IDX_0_VAL_flags 0x30
gpiohogs-macro =/ %s"DT_N" path-id %s"_GPIO_HOGS_IDX_" DIGIT %s"_VAL_flags"


; --------------------------------------------------------------------
; map-macro: a macro related to map properties
;
; Macros are generated when there is a property ending with '-map' as shown below.
;
; connector {
;     ...
;     interrupt-map = <0 1 &intc0 2 3>;
; };
;
; The existence of map entry;
;
; #define DT_N_S_connector_P_interrupt_map_MAP_ENTRY_0_EXISTS 1
map-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_MAP_ENTRY_" DIGIT %s"_EXISTS"
;
; The child address length, value, and existence.
;
; #define DT_N_S_connector_P_interrupt_map_MAP_ENTRY_0_CHILD_ADDRESS_LEN 1
; #define DT_N_S_connector_P_interrupt_map_MAP_ENTRY_0_CHILD_ADDRESS_IDX_0 0
; #define DT_N_S_connector_P_interrupt_map_MAP_ENTRY_0_CHILD_ADDRESS_IDX_0_EXISTS 1
map-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_MAP_ENTRY_" DIGIT %s"_CHILD_ADDRESS_LEN"
map-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_MAP_ENTRY_" DIGIT %s"_CHILD_ADDRESS_IDX_" DIGIT
map-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_MAP_ENTRY_" DIGIT %s"_CHILD_ADDRESS_IDX_" DIGIT %s"_EXISTS"
;
; The length of child specifiers length, value, and existence.
;
; #define DT_N_S_connector_P_interrupt_map_MAP_ENTRY_0_CHILD_SPECIFIER_LEN 1
; #define DT_N_S_connector_P_interrupt_map_MAP_ENTRY_0_CHILD_SPECIFIER_IDX_0_EXISTS 1
; #define DT_N_S_connector_P_interrupt_map_MAP_ENTRY_0_CHILD_SPECIFIER_IDX_0 0
map-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_MAP_ENTRY_" DIGIT %s"_CHILD_SPECIFIER_LEN"
map-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_MAP_ENTRY_" DIGIT %s"_CHILD_SPECIFIER_IDX_" DIGIT
map-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_MAP_ENTRY_" DIGIT %s"_CHILD_SPECIFIER_IDX_" DIGIT %s"_EXISTS"
;
; The parent node of this map.
;
; #define DT_N_S_connector_P_interrupt_map_MAP_ENTRY_0_PARENT DT_N_S_gpio_emul
map-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_MAP_ENTRY_" DIGIT %s"_PARENT"
;
; The length of parent address, value, and existence.
;
; #define DT_N_S_connector_P_interrupt_map_MAP_ENTRY_0_PARENT_ADDRESS_LEN 1
; #define DT_N_S_connector_P_interrupt_map_MAP_ENTRY_0_PARENT_ADDRESS_IDX_0 2
; #define DT_N_S_connector_P_interrupt_map_MAP_ENTRY_0_PARENT_ADDRESS_IDX_0_EXISTS 1
map-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_MAP_ENTRY_" DIGIT %s"_PARENT_ADDRESS_LEN"
map-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_MAP_ENTRY_" DIGIT %s"_PARENT_ADDRESS_IDX_" DIGIT
map-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_MAP_ENTRY_" DIGIT %s"_PARENT_ADDRESS_IDX_" DIGIT %s"_EXISTS"
;
; The length of parent specifiers length, value, and existence.
;
; #define DT_N_S_connector_P_interrupt_map_MAP_ENTRY_0_PARENT_SPECIFIER_LEN 1
; #define DT_N_S_connector_P_interrupt_map_MAP_ENTRY_0_PARENT_SPECIFIER_IDX_0_EXISTS 1
; #define DT_N_S_connector_P_interrupt_map_MAP_ENTRY_0_PARENT_SPECIFIER_IDX_0 3
map-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_MAP_ENTRY_" DIGIT %s"_PARENT_SPECIFIER_LEN"
map-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_MAP_ENTRY_" DIGIT %s"_PARENT_SPECIFIER_IDX_" DIGIT
map-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_MAP_ENTRY_" DIGIT %s"_PARENT_SPECIFIER_IDX_" DIGIT %s"_EXISTS"
;
; Iteration helpers for map.
;
map-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_FOREACH_MAP_ENTRY"
map-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_FOREACH_MAP_ENTRY_SEP"
map-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_FOREACH_MAP_ENTRY_VARGS"
map-macro =/ %s"DT_N" path-id %s"_P_" prop-id %s"_FOREACH_MAP_ENTRY_SEP_VARGS"


; --------------------------------------------------------------------
; property-macro: a macro related to a node property
;
; These combine a node identifier with a "lowercase-and-underscores form"
; property name. The value expands to something related to the property's
; value.
;
; The optional prop-suf suffix is when there's some specialized
; subvalue that deserves its own macro, like the macros for an array
; property's individual elements
;
; The "plain vanilla" macro for a property's value, with no prop-suf,
; looks like this:
;
;   DT_N_<node path>_P_<property name>
;
; Components:
;
; - path-id: node's devicetree path converted to a C token
; - prop-id: node's property name converted to a C token
; - prop-suf: an optional property-specific suffix
property-macro =  %s"DT_N" path-id %s"_P_" prop-id [prop-suf]

; --------------------------------------------------------------------
; path-id: a node's path-based macro identifier
;
; This in "lowercase-and-underscores" form. I.e. it is
; the node's devicetree path converted to a C token by changing:
;
; - each slash (/) to _S_
; - all letters to lowercase
; - non-alphanumerics characters to underscores
;
; For example, the leaf node "bar-BAZ" in this devicetree:
;
;   / {
;           foo@123 {
;                   bar-BAZ {};
;           };
;   };
;
; has path-id "_S_foo_123_S_bar_baz".
path-id = 1*( %s"_S_" dt-name )

; ----------------------------------------------------------------------
; prop-id: a property identifier
;
; A property name converted to a C token by changing:
;
; - all letters to lowercase
; - non-alphanumeric characters to underscores
;
; Example node:
;
;   chosen {
;       zephyr,console = &uart1;
;       WHY,AM_I_SHOUTING = "unclear";
;   };
;
; The 'zephyr,console' property has prop-id 'zephyr_console'.
; 'WHY,AM_I_SHOUTING' has prop-id 'why_am_i_shouting'.
prop-id = dt-name

; ----------------------------------------------------------------------
; prop-suf: a property-specific macro suffix
;
; Extra macros are generated for properties:
;
; - that are special to the specification ("reg", "interrupts", etc.)
; - with array types (uint8-array, phandle-array, etc.)
; - with "enum:" in their bindings
; - that have zephyr device API specific macros for phandle-arrays
; - related to phandle specifier names ("foo-names")
;
; Here are some examples:
;
; - _EXISTS: property, index or name existence flag
; - _SIZE: logical property length
; - _IDX_<i>: values of individual array elements
; - _IDX_<DIGIT>_VAL_<dt-name>: values of individual specifier
;   cells within a phandle array
; - _ADDR_<i>: for reg properties, the i-th register block address
; - _LEN_<i>: for reg properties, the i-th register block length
;
; The different cases are not exhaustively documented here to avoid
; this file going stale. Please see devicetree.h if you need to know
; the details.
prop-suf = 1*( "_" gen-name ["_" dt-name] )

; --------------------------------------------------------------------
; other-macro: grab bag for everything that isn't a node-macro.

; See examples below.
other-macro =  %s"DT_N_" alternate-id
; Total count of enabled instances of a compatible.
other-macro =/ %s"DT_N_INST_" dt-name %s"_NUM_OKAY"
; These are used internally by DT_FOREACH_NODE and
; DT_FOREACH_STATUS_OKAY_NODE respectively.
other-macro =/ %s"DT_FOREACH_HELPER"
other-macro =/ %s"DT_FOREACH_OKAY_HELPER"
; These are used internally by DT_FOREACH_STATUS_OKAY,
; which iterates over each enabled node of a compatible.
other-macro =/ %s"DT_FOREACH_OKAY_" dt-name
other-macro =/ %s"DT_FOREACH_OKAY_VARGS_" dt-name
; These are used internally by DT_INST_FOREACH_STATUS_OKAY,
; which iterates over each enabled instance of a compatible.
other-macro =/ %s"DT_FOREACH_OKAY_INST_" dt-name
other-macro =/ %s"DT_FOREACH_OKAY_INST_VARGS_" dt-name
; E.g.: #define DT_CHOSEN_zephyr_flash
other-macro =/ %s"DT_CHOSEN_" dt-name
; Declares that a compatible has at least one node on a bus.
; Example:
;
;   #define DT_COMPAT_vnd_dev_BUS_spi 1
other-macro =/ %s"DT_COMPAT_" dt-name %s"_BUS_" dt-name
; Declares that a compatible has at least one status "okay" node.
; Example:
;
;   #define DT_COMPAT_HAS_OKAY_vnd_dev 1
other-macro =/ %s"DT_COMPAT_HAS_OKAY_" dt-name
; Declares that a device class has at least one status "okay" node,
; and the count of such nodes.
; Example:
;
;   #define DT_CLASS_HAS_OKAY_adc 1
;   #define DT_N_CLASS_adc_NUM_OKAY 2
other-macro =/ %s"DT_CLASS_HAS_OKAY_" dt-name
other-macro =/ %s"DT_N_CLASS_" dt-name %s"_NUM_OKAY"
; These are used internally by DT_FOREACH_CLASS_STATUS_OKAY,
; which iterates over each enabled node of a device class.
other-macro =/ %s"DT_FOREACH_OKAY_CLASS_" dt-name
other-macro =/ %s"DT_FOREACH_OKAY_VARGS_CLASS_" dt-name
; Currently used to allow mapping a lowercase-and-underscores "label"
; property to a fixed-partitions node. See the flash map API docs
; for an example.
other-macro =/ %s"DT_COMPAT_" dt-name %s"_LABEL_" dt-name
; Get the node label of the phandle
other-macro =/ %s"DT_N_NODELABEL_" %s"DT_N" path-id "_IDX_" DIGIT "_C_TOKEN"

; --------------------------------------------------------------------
; alternate-id: another way to specify a node besides a path-id
;
; Example devicetree:
;
;   / {
;           aliases {
;                   dev = &dev_1;
;           };
;
;           soc {
;               dev_1: device@123 {
;                   compatible = "vnd,device";
;               };
;           };
;   };
;
; Node device@123 has these alternate-id values:
;
; - ALIAS_dev
; - NODELABEL_dev_1
; - INST_0_vnd_device
;
; The full alternate-id macros are:
;
;   #define DT_N_INST_0_vnd_device     DT_N_S_soc_S_device_123
;   #define DT_N_ALIAS_dev             DT_N_S_soc_S_device_123
;   #define DT_N_NODELABEL_dev_1       DT_N_S_soc_S_device_123
;
; These mainly exist to allow pasting an alternate-id macro onto a
; "_P_<prop-id>" to access node properties given a node's alias, etc.
;
; Notice that "inst"-type IDs have a leading instance identifier,
; which is generated by the devicetree scripts. The other types of
; alternate-id begin immediately with names taken from the devicetree.
alternate-id =  ( %s"ALIAS" / %s"NODELABEL" ) dt-name
alternate-id =/ %s"INST_" 1*DIGIT "_" dt-name

; --------------------------------------------------------------------
; miscellaneous helper definitions

; A dt-name is one or more:
; - lowercase ASCII letters (a-z)
; - numbers (0-9)
; - underscores ("_")
;
; They are the result of converting names or combinations of names
; from devicetree to a valid component of a C identifier by
; lowercasing letters (in practice, this is a no-op) and converting
; non-alphanumeric characters to underscores.
;
; You'll see these referred to as "lowercase-and-underscores" forms of
; various devicetree identifiers throughout the documentation.
dt-name = 1*( lower / DIGIT / "_" )

; gen-name is used as a stand-in for a component of a generated macro
; name which does not come from devicetree (dt-name covers that case).
;
; - uppercase ASCII letters (a-z)
; - numbers (0-9)
; - underscores ("_")
gen-name = upper 1*( upper / DIGIT / "_" )

; "lowercase ASCII letter" turns out to be pretty annoying to specify
; in RFC-7405 syntax.
;
; This is just ASCII letters a (0x61) through z (0x7a).
lower = %x61-7A

; "uppercase ASCII letter" in RFC-7405 syntax
upper = %x41-5A
```

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：提交上游的设备树绑定规则](P011_上游绑定规则.md) · [本模块主线目录](../reading/devicetree.md) · [全部主线](../reading/README.md) · [下一篇：设备树文档入口](P013_设备树文档入口.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：上游绑定规则](P011_上游绑定规则.md) · [返回大纲](大纲.md) · [下一章：设备树文档入口](P013_设备树文档入口.md)

</details>

<!-- reading-navigation:end -->
