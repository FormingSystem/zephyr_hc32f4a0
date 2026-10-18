---
id: learning.zephyr-docs.hardware.gpioapi-0
title: GPIO公共接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第266章\_GPIO公共接口

原文：[group__gpio__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html)。读取日期：2026-10-13，官方 `latest` 文档版本。

## 266.1\_接口范围与电平约定

本页定义 **通用输入/输出（General Purpose Input/Output，GPIO）**控制器接口，自 Zephyr 1.0 提供，接口版本为 1.0.0。主头文件为 `zephyr/drivers/gpio.h`，驱动辅助函数位于 `zephyr/drivers/gpio/gpio_utils.h`；设备树标志位来自 `zephyr/dt-bindings/gpio/gpio.h`。

物理电平（Physical Level）直接表示引脚高低；逻辑电平（Logical Level）还考虑有效极性。低电平有效（Active Low）时，物理低电平对应逻辑 `1`、有效状态（Active），物理高电平对应逻辑 `0`、无效状态（Inactive）。高电平有效（Active High）是默认设置，其物理值和逻辑值相同。名称带 `_raw` 的读写函数忽略低电平有效标志。

相关分组包括[器件扩展](P274_GPIO器件扩展目录.md)、[设备树GPIO接口](P290_设备树GPIO宏.md)、[模拟GPIO及其后端](P273_GPIO模拟接口.md)和[驱动后端](P271_GPIO驱动后端.md)。

## 266.2\_标志与基本类型

原定义中的 `BIT(n)` 表示第n位；`GPIO_OUTPUT_INIT_LOW`、`GPIO_OUTPUT_INIT_HIGH` 为输出初值标志，`GPIO_SINGLE_ENDED` 为单端模式标志，`GPIO_LINE_OPEN_DRAIN`、`GPIO_LINE_OPEN_SOURCE` 区分开漏与开源极。

下列宏表示有效极性、输入输出模式、驱动模式和偏置（Bias）：

| 宏 | 原定义 | 含义 |
| --- | --- | --- |
| <a id="gad93badd2828d065e7fd14cf40dd05039"></a>[`GPIO_ACTIVE_HIGH`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gad93badd2828d065e7fd14cf40dd05039) | `(0 << 0)` | 高电平时逻辑值为1 |
| <a id="ga62cea8989df2425e5e5e712217d65f46"></a>[`GPIO_ACTIVE_LOW`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga62cea8989df2425e5e5e712217d65f46) | `(1 << 0)` | 低电平时逻辑值为1 |
| <a id="ga7be6a0cc9aa65da1d4ee5751b4085853"></a>[`GPIO_INPUT`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga7be6a0cc9aa65da1d4ee5751b4085853) | `BIT(16)` | 启用输入 |
| <a id="ga0db9fe8a278e6ab7c5c6f14fe58e5eb1"></a>[`GPIO_OUTPUT`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1) | `BIT(17)` | 启用输出，不改变输出状态 |
| <a id="gaf82306c09450f6933366c4b821db21ed"></a>[`GPIO_DISCONNECTED`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gaf82306c09450f6933366c4b821db21ed) | `0` | 输入输出均禁用 |
| <a id="gaf85baf9f9c1ba554324b4cd7064487b0"></a>[`GPIO_OUTPUT_LOW`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gaf85baf9f9c1ba554324b4cd7064487b0) | `(GPIO_OUTPUT \| GPIO_OUTPUT_INIT_LOW)` | 输出并初始化为物理低电平 |
| <a id="ga10d31f204c0e927017d571352422fb09"></a>[`GPIO_OUTPUT_HIGH`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga10d31f204c0e927017d571352422fb09) | `(GPIO_OUTPUT \| GPIO_OUTPUT_INIT_HIGH)` | 输出并初始化为物理高电平 |
| <a id="ga72b7ac5b3613d972b88268bee9068e35"></a>[`GPIO_OPEN_DRAIN`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga72b7ac5b3613d972b88268bee9068e35) | `(GPIO_SINGLE_ENDED \| GPIO_LINE_OPEN_DRAIN)` | 开漏（Open Drain），线与（Wired AND） |
| <a id="ga5ace024873272a3f6727fc186afa0320"></a>[`GPIO_OPEN_SOURCE`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga5ace024873272a3f6727fc186afa0320) | `(GPIO_SINGLE_ENDED \| GPIO_LINE_OPEN_SOURCE)` | 开源极（Open Source），线或（Wired OR） |
| <a id="gaaa7921da231fd2b96575fa522e2c1970"></a>[`GPIO_PULL_UP`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gaaa7921da231fd2b96575fa522e2c1970) | `(1 << 4)` | 启用上拉（Pull-up） |
| <a id="gadec1802e074f3021d464da09cd66c7cf"></a>[`GPIO_PULL_DOWN`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gadec1802e074f3021d464da09cd66c7cf) | `(1 << 5)` | 启用下拉（Pull-down） |
| <a id="ga335bf7efee07e03961ab91a86295897a"></a>[`GPIO_DT_FLAGS_MASK`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga335bf7efee07e03961ab91a86295897a) | `0x7F` | 设备树GPIO标志掩码 |
| <a id="ga644109ce84c8feffe1226b9b50122a96"></a>[`GPIO_INT_WAKEUP`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga644109ce84c8feffe1226b9b50122a96) | `(1 << 6)` | 使GPIO中断能从低功耗模式唤醒系统 |
| <a id="ga91657faac28f9b213105dd61a419dd5a"></a>[`GPIO_INT_DISABLE`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga91657faac28f9b213105dd61a419dd5a) | `BIT(21)` | 禁用引脚中断 |
| <a id="ga1449ba90eaec5e6144fe4faae21f2e3f"></a>[`GPIO_MAX_PINS_PER_PORT`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga1449ba90eaec5e6144fe4faae21f2e3f) | `(sizeof(gpio_port_pins_t) * __CHAR_BIT__)` | 引脚集合类型支持的最大引脚数 |

开漏也称开集电极（Open Collector），行为类似一个接地或断开的开关。原文将开源极解释为软件工程中表示开漏相反输出模式的术语：行为类似连接电源或断开的开关；并指出没有对应的硬件原理图称谓，硬件工程师通常不熟悉这一名称。

| 类型 | C类型 | 含义 |
| --- | --- | --- |
| <a id="ga7f40ed51f14fd8000e9b52ab347b273f"></a>[`gpio_port_pins_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga7f40ed51f14fd8000e9b52ab347b273f) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 端口引脚集合；当且仅当 `(1U << n)` 对应位置1时集合包含引脚n |
| <a id="gabcebe24c93486896e1dfc2459ec25693"></a>[`gpio_port_value_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gabcebe24c93486896e1dfc2459ec25693) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 端口引脚值；第n位置1表示物理高或逻辑有效，置0表示物理低或逻辑无效 |
| <a id="ga38179eb7a46a743c12cfac28f347fb34"></a>[`gpio_pin_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga38179eb7a46a743c12cfac28f347fb34) | [`uint8_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | 引脚索引；较小的类型足以保存例如设备树中的引脚编号 |
| <a id="gad435719dccdc37c05852960a7218fbd2"></a>[`gpio_dt_flags_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gad435719dccdc37c05852960a7218fbd2) | [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) | 设备树标志，低8位为标准标志，高8位保留给片上系统（System on Chip，SoC）专用标志 |
| <a id="ga5f5cb5e7dae6d58e072bb450af029d2e"></a>[`gpio_flags_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga5f5cb5e7dae6d58e072bb450af029d2e) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 足以保存引脚和中断的全部配置标志 |

所有设备树可表达的GPIO标志都能放入完整标志字段的低16位，因此描述结构使用较小的 [`gpio_dt_flags_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gad435719dccdc37c05852960a7218fbd2)。端口值通常与引脚集合配对，后者指出哪些位对当前操作有效。

结构 [`gpio_dt_spec`](P267_GPIO设备树描述.md) 保存设备树引脚信息；[`gpio_driver_config`](P268_GPIO公共驱动配置.md) 是各GPIO驱动共享的配置，应放在设备 `config` 所指对象的首成员；[`gpio_driver_data`](P269_GPIO公共驱动数据.md) 应放在驱动 `driver_data` 结构的首成员；[`gpio_callback`](P270_GPIO回调结构.md) 保存回调信息。

## 266.3\_设备树宏参数与公共配置

设备树（Devicetree）宏使用以下参数：`node_id` 为节点标识符，控制器掩码宏中指GPIO控制器；`inst` 为与驱动兼容标识 `DT_DRV_COMPAT` 匹配的实例编号，`DT_DRV_INST(inst)` 将其变为节点标识符；`ngpios` 为GPIO数量；`prop` 为用小写字母和下划线书写的属性名；`idx` 为属性中的逻辑索引；`default_value` 为回退值。

<a id="gafa496e01d480334049c9bb574267659d"></a>

宏 `GPIO_COMMON_CONFIG_FROM_DT_INST(inst)` 从实例编号构造 [`gpio_driver_config`](P268_GPIO公共驱动配置.md) 初始化器，声明位于辅助头文件，原展开为：

```c
GPIO_COMMON_CONFIG_FROM_DT_NODE(DT_DRV_INST(inst))
```

<a id="ga7b248bc1a6d7b922df7dae15b7c7855f"></a>

宏 `GPIO_COMMON_CONFIG_FROM_DT_NODE(node_id)` 从节点标识符构造同一类型初始化器，设置支持引脚的位掩码（Bitmask）字段 `port_pin_mask`：

```c
{                                                                  \
        .port_pin_mask = GPIO_PORT_PIN_MASK_FROM_DT_NODE(node_id), \
}
```

> 译注：下文原展开包含若干辅助宏：`COND_CODE_0`、`COND_CODE_1` 按条件选择展开分支，`DT_NODE_HAS_PROP` 检查属性，`DT_PROP` 读取属性，`DT_PROP_OR` 提供属性缺省值，`GENMASK64` 生成64位范围掩码。`BITS_PER_LONG_LONG` 表示对应整数类型位数；`FOR_EACH_FIXED_ARG` 带固定参数逐项展开，`LIST_DROP_EMPTY` 去除空项；`Z_GPIO_GEN_RESERVED_RANGES_COND`、`Z_SPARSE_LIST_ODD_NUMBERS` 是保留范围生成所用内部宏。原示例中的 `DT_LABEL` 写法按官方保留，不能据此把它当作现代节点标识宏。

## 266.4\_实例的可用与保留引脚掩码

<a id="ga856fe8042e496a39ef3a4e19fff2c4ce"></a>

宏 `GPIO_DT_INST_PORT_PIN_MASK_NGPIOS_EXC(inst, ngpios)` 根据实例的保留范围属性和给定数量，返回**可用**GPIO位掩码：

```c
GPIO_DT_PORT_PIN_MASK_NGPIOS_EXC(DT_DRV_INST(inst), ngpios)
```

<a id="ga9136b467eaddcc734bc6a0a7d8b34e14"></a>

宏 `GPIO_DT_INST_RESERVED_RANGES(inst)` 根据实例的 `gpio-reserved-ranges` 与 `ngpios` 属性，返回**保留**GPIO位掩码：

```c
GPIO_DT_RESERVED_RANGES(DT_DRV_INST(inst))
```

<a id="gaebaea00f6f7649c61651e8d50c7cdf07"></a>

宏 `GPIO_DT_INST_RESERVED_RANGES_NGPIOS(inst, ngpios)` 从实例保留范围属性及显式数量得到保留位掩码：

```c
GPIO_DT_RESERVED_RANGES_NGPIOS(DT_DRV_INST(inst), ngpios)
```

## 266.5\_节点的可用引脚掩码

<a id="ga274e09d7082d97b2f90c6a7fd4b71d49"></a>

宏 `GPIO_DT_PORT_PIN_MASK_NGPIOS_EXC(node_id, ngpios)` 与保留范围宏配对，但返回的是**允许使用**的GPIO位掩码。数量为0时结果为0，存在保留范围时从有效范围中排除它们：

```c
((gpio_port_pins_t)                                                    \
COND_CODE_0(ngpios,                                                    \
        (0),                                                           \
        (COND_CODE_1(DT_NODE_HAS_PROP(node_id, gpio_reserved_ranges),  \
                ((GENMASK64(ngpios - 1, 0) &                           \
                ~GPIO_DT_RESERVED_RANGES_NGPIOS(node_id, ngpios))),    \
                (GENMASK64(ngpios - 1, 0)))                            \
        )                                                              \
))
```

原设备树片段：

```dts
a {
   compatible = "some,gpio-controller";
   ngpios = <32>;
   gpio-reserved-ranges = <0 8>, <9 5>, <15 16>;
};
```

原用法：

```c
struct some_config {
   uint32_t port_pin_mask;
};

static const struct some_config dev_cfg = {
   .port_pin_mask = GPIO_DT_PORT_PIN_MASK_NGPIOS_EXC(
                           DT_LABEL(a), 32),
};
```

展开结果：

```c
struct some_config {
   uint32_t port_pin_mask;
};

static const struct some_config dev_cfg = {
   .port_pin_mask = 0x80004100,
                   // 0b1000 0000 0000 0000 0100 0001 00000 000
};
```

## 266.6\_节点的保留引脚掩码

<a id="ga648fcc0633d57b52d3df683efda98440"></a>

宏 `GPIO_DT_RESERVED_RANGES(node_id)` 根据节点的保留范围和数量属性返回保留位掩码：

```c
GPIO_DT_RESERVED_RANGES_NGPIOS(node_id, DT_PROP(node_id, ngpios))
```

<a id="ga439c3d29aa585b00853aba6d6416028a"></a>

宏 `GPIO_DT_RESERVED_RANGES_NGPIOS(node_id, ngpios)` 根据保留范围属性与显式数量返回保留位掩码：

```c
((gpio_port_pins_t)                                                    \
COND_CODE_1(DT_NODE_HAS_PROP(node_id, gpio_reserved_ranges),           \
        (GENMASK64(BITS_PER_LONG_LONG - 1, ngpios)                     \
        | FOR_EACH_FIXED_ARG(Z_GPIO_GEN_RESERVED_RANGES_COND,          \
                (|),                                                   \
                node_id,                                               \
                LIST_DROP_EMPTY(Z_SPARSE_LIST_ODD_NUMBERS))),          \
        (0)))
```

属性 `gpio-reserved-ranges` 用“起始偏移、范围长度”数对表示 `0...ngpios-1` 中禁用或保留的GPIO。例如 `<3 2>, <10 1>` 表示偏移3、4、10不可用，即使 `ngpios = <18>` 也是如此。

实现继承了通用设备树限制，最多支持64组数对，最终结果仍受 [`gpio_port_pins_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga7f40ed51f14fd8000e9b52ab347b273f) 位宽限制。C宏对重叠、越界等错误数对可能产生未定义结果。若 `ngpios` 小于设备树整数类型的32位宽，数量范围以外未使用的高有效位（Most Significant Bits，MSBs）也会标为保留。

原设备树示例：

```dts
a {
        compatible = "some,gpio-controller";
        ngpios = <32>;
        gpio-reserved-ranges = <0  4>, <5  3>, <9  5>, <11 2>, <15 2>,
                                <18 2>, <21 1>, <23 1>, <25 4>, <30 2>;
};

b {
        compatible = "some,gpio-controller";
        ngpios = <18>;
        gpio-reserved-ranges = <3 2>, <10 1>;
};
```

原调用：

```c
struct some_config {
        uint32_t ngpios;
        uint32_t gpios_reserved;
};

static const struct some_config dev_cfg_a = {
        .ngpios = DT_PROP_OR(DT_LABEL(a), ngpios, 0),
        .gpios_reserved = GPIO_DT_RESERVED_RANGES_NGPIOS(DT_LABEL(a),
                                DT_PROP(DT_LABEL(a), ngpios)),
};

static const struct some_config dev_cfg_b = {
        .ngpios = DT_PROP_OR(DT_LABEL(b), ngpios, 0),
        .gpios_reserved = GPIO_DT_RESERVED_RANGES_NGPIOS(DT_LABEL(b),
                                DT_PROP(DT_LABEL(b), ngpios)),
};
```

展开结果：

```c
struct some_config {
        uint32_t ngpios;
        uint32_t gpios_reserved;
};

static const struct some_config dev_cfg_a = {
        .ngpios = 32,
        .gpios_reserved = 0xdeadbeef,
                       // 0b1101 1110 1010 1101 1011 1110 1110 1111
};
static const struct some_config dev_cfg_b = {
        .ngpios = 18,
        .gpios_reserved = 0xfffc0418,
                       // 0b1111 1111 1111 1100 0000 0100 0001 1000
                       // unused MSBs were marked as reserved too
};
```

> 译注：本页保留了原示例的 `DT_LABEL(a)`、`DT_LABEL(b)` 写法，片段节点本身未展示这些标签定义；保留范围示例还包含重叠数对。请同时注意上文的未定义结果限制，不将示例视作已编译验证的设备树配置。

## 266.7\_设备树引脚描述初始化

<a id="ga2fa6bb5880f46984f9fc29c70f7d503e"></a>

以下宏返回 [`gpio_dt_spec`](P267_GPIO设备树描述.md) 的静态初始化器（Static Initializer）。`GPIO_DT_SPEC_GET(node_id, prop)` 等价于索引0版本：

```c
GPIO_DT_SPEC_GET_BY_IDX(node_id, prop, 0)
```

<a id="gacb1077b77aecf8f1a9c7636ea583c4cf"></a>

宏 `GPIO_DT_SPEC_GET_BY_IDX(node_id, prop, idx)` 根据节点、GPIO属性及索引取得控制器、引脚和标志：

```c
{                                                                      \
        .port = DEVICE_DT_GET(DT_GPIO_CTLR_BY_IDX(node_id, prop, idx)),\
        .pin = DT_GPIO_PIN_BY_IDX(node_id, prop, idx),                 \
        .dt_flags = DT_GPIO_FLAGS_BY_IDX(node_id, prop, idx),          \
}
```

原设备树片段：

```dts
 n: node {
    foo-gpios = <&gpio0 1 GPIO_ACTIVE_LOW>,
                <&gpio1 2 GPIO_ACTIVE_LOW>;
 }
```

原用法与初始化结果：

```c
 const struct gpio_dt_spec spec = GPIO_DT_SPEC_GET_BY_IDX(DT_NODELABEL(n),
                                                     foo_gpios, 1);
 // Initializes 'spec' to:
 // {
 //         .port = DEVICE_DT_GET(DT_NODELABEL(gpio1)),
 //         .pin = 2,
 //         .dt_flags = GPIO_ACTIVE_LOW
 // }
```

使用前仍需通过 [`device_is_ready()`](../device_reference/P001_设备模型公共接口.md#gaa4944bd850e90cbd52b0489f9b12edfb) 等方法检查控制器就绪状态。节点必须存在，具有指定属性，属性还必须按示例提供GPIO控制器、引脚号及标志，否则使用本宏是错误的。

> 译注：原文将需检查的成员称为 `gpio`，实际展示的结构初始化器使用 `port`。此处按展示的控制器含义说明；原设备树片段末尾也没有分号，代码保持原样。

<a id="ga3db4fa464e191016287f4c4d7eb9a983"></a>

宏 `GPIO_DT_SPEC_GET_BY_IDX_OR(node_id, prop, idx, default_value)` 提供回退：当节点有该属性且索引有效时使用常规初始化器，并且**不展开** `default_value`；否则展开回退值。与仅检查属性存在的宏不同，这里也检查索引：

```c
COND_CODE_1(DT_PROP_HAS_IDX(node_id, prop, idx),                \
            (GPIO_DT_SPEC_GET_BY_IDX(node_id, prop, idx)),      \
            (default_value))
```

<a id="ga26b2205aa82819df1d80a22761352e71"></a>

宏 `GPIO_DT_SPEC_GET_OR(node_id, prop, default_value)` 采用索引0及相同回退规则：

```c
GPIO_DT_SPEC_GET_BY_IDX_OR(node_id, prop, 0, default_value)
```

<a id="ga168f5c6e39a0111191f606a9a0826e89"></a>

宏 `GPIO_DT_SPEC_INST_GET(inst, prop)` 取得实例属性索引0的静态初始化器：

```c
GPIO_DT_SPEC_INST_GET_BY_IDX(inst, prop, 0)
```

<a id="gabbdbef450f14fd0af73667e2728ad084"></a>

宏 `GPIO_DT_SPEC_INST_GET_BY_IDX(inst, prop, idx)` 取得实例属性指定索引的静态初始化器：

```c
GPIO_DT_SPEC_GET_BY_IDX(DT_DRV_INST(inst), prop, idx)
```

<a id="gaf07edf6bc88af18e9976c76f6c3c3bf1"></a>

宏 `GPIO_DT_SPEC_INST_GET_BY_IDX_OR(inst, prop, idx, default_value)` 为实例的指定索引提供回退：

```c
COND_CODE_1(DT_PROP_HAS_IDX(DT_DRV_INST(inst), prop, idx),              \
            (GPIO_DT_SPEC_GET_BY_IDX(DT_DRV_INST(inst), prop, idx)),    \
            (default_value))
```

<a id="gae6b4a354c3cf0e042a390aac4bc37c69"></a>

宏 `GPIO_DT_SPEC_INST_GET_OR(inst, prop, default_value)` 为实例的索引0提供回退：

```c
GPIO_DT_SPEC_INST_GET_BY_IDX_OR(inst, prop, 0, default_value)
```

## 266.8\_中断触发标志

宏族 `GPIO_INT_*` 决定输入引脚如何触发中断（Interrupt）。逻辑触发考虑 `GPIO_ACTIVE_LOW`，物理触发按高低电平本身判断。控制器在配置触发属性时应复位中断状态，例如清除挂起位（Pending Bit）。若仅希望启用或禁用中断而不更改GPIO设置，应使用 [`GPIO_INT_MODE_ENABLE_ONLY`](P271_GPIO驱动后端.md) 或 [`GPIO_INT_MODE_DISABLE_ONLY`](P271_GPIO驱动后端.md)。

下列宏都会启用中断。其展开中的 `GPIO_INT_ENABLE` 表示启用，`GPIO_INT_EDGE` 表示边沿触发（Edge Trigger），`GPIO_INT_LEVELS_LOGICAL` 表示使用逻辑电平，`GPIO_INT_LOW_0`、`GPIO_INT_HIGH_1` 分别指定低/逻辑0及高/逻辑1条件。

<a id="ga10fa307ab17d02819108165a09f8e08b"></a>

[`GPIO_INT_EDGE_BOTH`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga10fa307ab17d02819108165a09f8e08b)：在上升沿或下降沿触发。

```c
(GPIO_INT_ENABLE | \
GPIO_INT_EDGE | \
GPIO_INT_LOW_0 | \
GPIO_INT_HIGH_1)
```

<a id="ga73bed10383a27d4a03feb300e64af8e8"></a>

[`GPIO_INT_EDGE_FALLING`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga73bed10383a27d4a03feb300e64af8e8)：在下降沿触发。

```c
(GPIO_INT_ENABLE | \
GPIO_INT_EDGE | \
GPIO_INT_LOW_0)
```

<a id="gaed642a4e482f73aa917477370d0e241b"></a>

[`GPIO_INT_EDGE_RISING`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gaed642a4e482f73aa917477370d0e241b)：在上升沿触发。

```c
(GPIO_INT_ENABLE | \
GPIO_INT_EDGE | \
GPIO_INT_HIGH_1)
```

<a id="ga35d2ff0e041236d82004a4bb2b5bf634"></a>

[`GPIO_INT_EDGE_TO_ACTIVE`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga35d2ff0e041236d82004a4bb2b5bf634)：在状态变为逻辑1、有效状态的边沿触发。

```c
(GPIO_INT_ENABLE | \
GPIO_INT_LEVELS_LOGICAL | \
GPIO_INT_EDGE | \
GPIO_INT_HIGH_1)
```

<a id="ga7b922529a3cb9396b0d82ca823e9d010"></a>

[`GPIO_INT_EDGE_TO_INACTIVE`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga7b922529a3cb9396b0d82ca823e9d010)：在状态变为逻辑0、无效状态的边沿触发。

```c
(GPIO_INT_ENABLE | \
GPIO_INT_LEVELS_LOGICAL | \
GPIO_INT_EDGE | \
GPIO_INT_LOW_0)
```

<a id="gae51c68ff83959994bb942bb253505ca1"></a>

[`GPIO_INT_LEVEL_ACTIVE`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gae51c68ff83959994bb942bb253505ca1)：在逻辑1、有效电平触发。

```c
(GPIO_INT_ENABLE | \
GPIO_INT_LEVELS_LOGICAL | \
GPIO_INT_HIGH_1)
```

<a id="ga233690d9a6a64bc9f804e3caa6d4a88f"></a>

[`GPIO_INT_LEVEL_HIGH`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga233690d9a6a64bc9f804e3caa6d4a88f)：在物理高电平触发。

```c
(GPIO_INT_ENABLE | \
GPIO_INT_HIGH_1)
```

<a id="gacb9bb1b63f172af2da7eb193e234c4f2"></a>

[`GPIO_INT_LEVEL_INACTIVE`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gacb9bb1b63f172af2da7eb193e234c4f2)：在逻辑0、无效电平触发。

```c
(GPIO_INT_ENABLE | \
GPIO_INT_LEVELS_LOGICAL | \
GPIO_INT_LOW_0)
```

<a id="gaddbb5ad576875af9c2d73b73df55c893"></a>

[`GPIO_INT_LEVEL_LOW`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gaddbb5ad576875af9c2d73b73df55c893)：在物理低电平触发。

```c
(GPIO_INT_ENABLE | \
GPIO_INT_LOW_0)
```

## 266.9\_逻辑输出初值与通用掩码

<a id="ga0f5cc126d6a690eb3e303eb29aa718ce"></a>

[`GPIO_OUTPUT_ACTIVE`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga0f5cc126d6a690eb3e303eb29aa718ce) 配置为输出并初始化为逻辑1。展开中的 `GPIO_OUTPUT_INIT_LOGICAL` 表示初始化值使用逻辑极性：

```c
(GPIO_OUTPUT |                 \
GPIO_OUTPUT_INIT_HIGH |        \
GPIO_OUTPUT_INIT_LOGICAL)
```

<a id="ga1e1d6be5f2f788f89468a0ce8b854634"></a>

[`GPIO_OUTPUT_INACTIVE`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga1e1d6be5f2f788f89468a0ce8b854634) 配置为输出并初始化为逻辑0：

```c
(GPIO_OUTPUT |                 \
GPIO_OUTPUT_INIT_LOW |         \
GPIO_OUTPUT_INIT_LOGICAL)
```

<a id="ga34528b682ca57bfc77cef745ed235e04"></a>

以下三个宏位于辅助头文件。`GPIO_PORT_PIN_MASK_FROM_DT_INST(inst)` 根据实例的保留范围与数量属性返回允许使用的引脚掩码：

```c
GPIO_PORT_PIN_MASK_FROM_DT_NODE(DT_DRV_INST(inst))
```

<a id="ga570c8e724c799b1bb0edeafa249d9730"></a>

宏 `GPIO_PORT_PIN_MASK_FROM_DT_NODE(node_id)` 根据控制器节点的相应属性返回允许使用的引脚掩码：

```c
GPIO_DT_PORT_PIN_MASK_NGPIOS_EXC(node_id, DT_PROP(node_id, ngpios))
```

<a id="ga696fbe0e6868902fbec77afc06f55e0a"></a>

宏 `GPIO_PORT_PIN_MASK_FROM_NGPIOS(ngpios)` 从引脚数量返回允许使用的位掩码：

```c
((gpio_port_pins_t)(((uint64_t)1 << (ngpios)) - 1U))
```

## 266.10\_回调类型与函数参数约定

<a id="gaf0aa40279d32b1b8332f2f23a39510af"></a>

应用回调（Callback）处理函数的类型为：

```c
typedef void (*gpio_callback_handler_t)(const struct device *port,
                                      struct gpio_callback *cb,
                                      gpio_port_pins_t pins);
```

`port` 是GPIO设备结构，`cb` 是拥有该处理函数的原回调结构，`pins` 是触发回调的引脚掩码。若回调结构嵌入应用私有结构，可用容器反查宏 [`CONTAINER_OF()`](../util_reference/P001_通用工具公共接口.md#gac5bc561d1bfd1bf68877fe577779bd2f) 根据 `cb` 找回私有数据。

以下函数中，`port` 或 `dev` 指向驱动实例的设备结构，`pin` 为引脚号，`spec` 指向设备树GPIO描述。每项函数列出的返回值均应检查：错误 `-EIO` 表示访问外部GPIO芯片时出现输入/输出（Input/Output，I/O）错误；`-EWOULDBLOCK` 表示该操作会阻塞；`-ENOSYS` 表示驱动未实现；`-ENOTSUP` 表示配置不受支持；`-EINVAL` 表示参数无效；`-EBUSY` 表示资源已被占用。

<a id="ga05fd15af20386d69f9332354285b0cca"></a>

## 266.11\_gpio_add_callback

函数 [`gpio_add_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga05fd15af20386d69f9332354285b0cca) 的声明为：

```c
static inline int gpio_add_callback(const struct device * port, struct gpio_callback * callback);
```

添加应用回调。`callback` 必须指向有效应用回调结构。同一端口可添加所需数量的回调。成功返回 `0`，失败返回负错误码；未实现操作时返回 `-ENOSYS`。可以在某个回调正在执行时添加回调，但新回调是否参与当前GPIO事件并无规定。

<a id="ga54845eb95bc9636c3e6ff285300b6979"></a>

## 266.12\_gpio_add_callback_dt

函数 [`gpio_add_callback_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga54845eb95bc9636c3e6ff285300b6979) 的声明为：

```c
static inline int gpio_add_callback_dt(const struct gpio_dt_spec * spec, struct gpio_callback * callback);
```

根据 `spec` 添加 `callback` 指向的有效应用回调，等价于下面的调用，返回该调用的结果。

```c
gpio_add_callback(spec->port, callback);
```

<a id="gac7193ccc60e2f1c62569f80cd9973702"></a>

## 266.13\_gpio_fire_callbacks

函数 [`gpio_fire_callbacks()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gac7193ccc60e2f1c62569f80cd9973702) 的声明为：

```c
static inline void gpio_fire_callbacks(sys_slist_t * list, const struct device * port, uint32_t pins);
```

遍历回调链表并触发其中的回调。`list` 指向GPIO回调链表，`port` 指向GPIO驱动实例，`pins` 是实际触发中断的引脚掩码。本辅助函数位于 `zephyr/drivers/gpio/gpio_utils.h`，没有返回值。

<a id="ga3f9e45de172a27f49c31a072c0c241e1"></a>

## 266.14\_gpio_get_pending_int

函数 [`gpio_get_pending_int()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga3f9e45de172a27f49c31a072c0c241e1) 的声明为：

```c
int gpio_get_pending_int(const struct device * dev);
```

取得设备中断状态寄存器，尤其用于从低功耗状态唤醒后检查唤醒来源。`dev` 指向设备实例。有至少一个GPIO中断挂起时返回非零状态；没有挂起中断时返回 `0`；驱动未实现时返回 `-ENOSYS`。

> 译注：应先处理负错误码，不能将所有非零返回值都直接解释为有效的挂起状态。

<a id="ga7a7dd7c1f3a2135a9f378e1c34b6232c"></a>

## 266.15\_gpio_init_callback

函数 [`gpio_init_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga7a7dd7c1f3a2135a9f378e1c34b6232c) 的声明为：

```c
static inline void gpio_init_callback(struct gpio_callback * callback, gpio_callback_handler_t handler, gpio_port_pins_t pin_mask);
```

初始化回调结构。`callback` 指向有效应用回调结构，`handler` 是有效处理函数指针，`pin_mask` 是处理函数关注的引脚位掩码。没有返回值。

## 266.16\_gpio_is_ready_dt

<a id="gaaec9ad17c08a0d527d66445fe82d8327"></a>

函数 [`gpio_is_ready_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gaaec9ad17c08a0d527d66445fe82d8327) 的声明为：

```c
static inline bool gpio_is_ready_dt(const struct gpio_dt_spec * spec);
```

检查设备树描述中的GPIO端口是否就绪。`spec` 可供使用时返回 [`true`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a41f9c5fb8b08eb5dc3edce4dcb37fee7)，尚未就绪时返回 [`false`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a65e9886d74aaee76545e83dd09011727)。

<a id="gac9d36599625b79bd2ebb9f3603a2a122"></a>

## 266.17\_gpio_manage_callback

函数 [`gpio_manage_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gac9d36599625b79bd2ebb9f3603a2a122) 的声明为：

```c
static inline int gpio_manage_callback(sys_slist_t * callbacks, struct gpio_callback * callback, bool set);
```

向回调链表插入或从中删除一个回调。`callbacks` 指向原链表，原文允许其为 `NULL`；`callback` 指向待插入或删除的回调；布尔参数 `set` 指示插入或删除。成功返回 `0`，否则返回负错误码。本辅助函数位于 `zephyr/drivers/gpio/gpio_utils.h`。

<a id="gaed4a2051d76db7eead8ed1719ce2ba33"></a>

## 266.18\_gpio_pin_configure

函数 [`gpio_pin_configure()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gaed4a2051d76db7eead8ed1719ce2ba33) 的声明为：

```c
int gpio_pin_configure(const struct device * port, gpio_pin_t pin, gpio_flags_t flags);
```

配置单个引脚。`port`、`pin`、[`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 均为输入参数，[`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 包含输入/输出配置、引脚驱动及偏置标志。成功返回 `0`；配置不受支持时返回 `-ENOTSUP`，除非对应标志文档另有规定；还可能返回 `-EINVAL`、`-EIO`、`-EWOULDBLOCK`。

<a id="ga423db4f985098ddcaa504ec430e91913"></a>

## 266.19\_gpio_pin_configure_dt

函数 [`gpio_pin_configure_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga423db4f985098ddcaa504ec430e91913) 的声明为：

```c
static inline int gpio_pin_configure_dt(const struct gpio_dt_spec * spec, gpio_flags_t extra_flags);
```

根据设备树描述和额外标志配置单个引脚。`extra_flags` 是附加标志，与 `spec->dt_flags` 按位或合并。返回 [`gpio_pin_configure()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gaed4a2051d76db7eead8ed1719ce2ba33) 的结果，等价调用为：

```c
gpio_pin_configure(spec->port, spec->pin, spec->dt_flags | extra_flags);
```

<a id="ga496cd45fd6a2826c75d70c71f967234b"></a>

## 266.20\_gpio_pin_get

函数 [`gpio_pin_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga496cd45fd6a2826c75d70c71f967234b) 的声明为：

```c
int gpio_pin_get(const struct device * port, gpio_pin_t pin);
```

读取输入引脚的逻辑电平，考虑 `GPIO_ACTIVE_LOW`。高电平有效时，物理低电平读为逻辑0；低电平有效时，物理低电平读为逻辑1。默认高电平有效配置下，此函数等价于 [`gpio_pin_get_raw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga635975f1df6157c7e8a6c67bac55fbc0)。有效/逻辑1返回 `1`，无效/逻辑0返回 `0`；错误为 `-EIO`、`-EWOULDBLOCK`。

<a id="ga133284b60a13c6dc50b87c1d04259f5e"></a>

## 266.21\_gpio_pin_get_config

函数 [`gpio_pin_get_config()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga133284b60a13c6dc50b87c1d04259f5e) 的声明为：

```c
int gpio_pin_get_config(const struct device * port, gpio_pin_t pin, gpio_flags_t * flags);
```

取得单个引脚当前配置；成功时写入 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 指向的变量。成功返回 `0`；驱动未实现读取配置时返回 `-ENOSYS`；其他错误为 `-EINVAL`、`-EIO`、`-EWOULDBLOCK`。

<a id="ga820448aa4be8b14839bc6a00c9f34bb4"></a>

## 266.22\_gpio_pin_get_config_dt

函数 [`gpio_pin_get_config_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga820448aa4be8b14839bc6a00c9f34bb4) 的声明为：

```c
static inline int gpio_pin_get_config_dt(const struct gpio_dt_spec * spec, gpio_flags_t * flags);
```

根据设备树描述读取单个引脚配置，成功时保存在 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 指向的变量中。原文给出的等价调用为：

```c
gpio_pin_get_config(spec->port, spec->pin, flags);
```

> 译注：原页返回值栏写成“来自 [`gpio_pin_configure()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gaed4a2051d76db7eead8ed1719ce2ba33) 的值”，但上方等价调用是 `gpio_pin_get_config()`；两处不一致，使用时应按读取配置的实际接口核对。

<a id="gaabeb2d0d98856c7ff78be36651d6bbc1"></a>

## 266.23\_gpio_pin_get_dt

函数 [`gpio_pin_get_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gaabeb2d0d98856c7ff78be36651d6bbc1) 的声明为：

```c
static inline int gpio_pin_get_dt(const struct gpio_dt_spec * spec);
```

从设备树描述读取输入引脚的逻辑电平，返回 [`gpio_pin_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga496cd45fd6a2826c75d70c71f967234b) 的结果，等价调用为：

```c
gpio_pin_get(spec->port, spec->pin);
```

<a id="ga635975f1df6157c7e8a6c67bac55fbc0"></a>

## 266.24\_gpio_pin_get_raw

函数 [`gpio_pin_get_raw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga635975f1df6157c7e8a6c67bac55fbc0) 的声明为：

```c
int gpio_pin_get_raw(const struct device * port, gpio_pin_t pin);
```

读取输入引脚的物理电平，忽略 `GPIO_ACTIVE_LOW`。高电平返回 `1`，低电平返回 `0`；错误为 `-EIO`、`-EWOULDBLOCK`。

<a id="ga9618f254365381063439a0e9c5e787cb"></a>

## 266.25\_gpio_pin_interrupt_configure

函数 [`gpio_pin_interrupt_configure()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga9618f254365381063439a0e9c5e787cb) 的声明为：

```c
int gpio_pin_interrupt_configure(const struct device * port, gpio_pin_t pin, gpio_flags_t flags);
```

配置引脚中断；可在中断服务程序（Interrupt Service Routine，ISR）中调用。也可以为未由GPIO模块直接控制、而是路由到集成电路间总线（Inter-Integrated Circuit，I²C）、串行外设接口（Serial Peripheral Interface，SPI）或通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）等模块的引脚配置中断。`port`、`pin`、[`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 均为输入，[`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 使用 `GPIO_INT_*` 中断标志。成功返回 `0`；未实现返回 `-ENOSYS`；配置不受支持返回 `-ENOTSUP`，除非标志文档另有规定；引脚所需中断线已被使用返回 `-EBUSY`；还可能返回 `-EINVAL`、`-EIO`、`-EWOULDBLOCK`。

<a id="ga24f0b4ad30e6a8c81f51a2813478c793"></a>

## 266.26\_gpio_pin_interrupt_configure_dt

函数 [`gpio_pin_interrupt_configure_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga24f0b4ad30e6a8c81f51a2813478c793) 的声明为：

```c
static inline int gpio_pin_interrupt_configure_dt(const struct gpio_dt_spec * spec, gpio_flags_t flags);
```

根据设备树描述配置引脚中断，也可在ISR中调用。[`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 为中断配置标志，返回 [`gpio_pin_interrupt_configure()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga9618f254365381063439a0e9c5e787cb) 的结果，等价调用为：

```c
gpio_pin_interrupt_configure(spec->port, spec->pin, combined_flags);
```

其中 `combined_flags` 合并传入的 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 与 `spec->dt_flags` 中已设置的 [`GPIO_INT_WAKEUP`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga644109ce84c8feffe1226b9b50122a96)。设备树标志中的其他位被忽略。

<a id="ga1454bc223fc2200aff3c4aab7d747da2"></a>

## 266.27\_gpio_pin_is_input

函数 [`gpio_pin_is_input()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga1454bc223fc2200aff3c4aab7d747da2) 的声明为：

```c
static inline int gpio_pin_is_input(const struct device * port, gpio_pin_t pin);
```

检查引脚是否配置为输入。配置了 [`GPIO_INPUT`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga7be6a0cc9aa65da1d4ee5751b4085853) 返回 `1`，否则返回 `0`；错误为 `-ENOSYS`、`-EIO`、`-EWOULDBLOCK`。

<a id="ga7aaec28a83cac63bd87fc94cc72664b1"></a>

## 266.28\_gpio_pin_is_input_dt

函数 [`gpio_pin_is_input_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga7aaec28a83cac63bd87fc94cc72664b1) 的声明为：

```c
static inline int gpio_pin_is_input_dt(const struct gpio_dt_spec * spec);
```

检查设备树描述中的引脚是否为输入，返回 [`gpio_pin_is_input()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga1454bc223fc2200aff3c4aab7d747da2) 的结果：

```c
gpio_pin_is_input(spec->port, spec->pin);
```

<a id="ga3b854d759180e222299ea445b401acc1"></a>

## 266.29\_gpio_pin_is_output

函数 [`gpio_pin_is_output()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga3b854d759180e222299ea445b401acc1) 的声明为：

```c
static inline int gpio_pin_is_output(const struct device * port, gpio_pin_t pin);
```

检查引脚是否配置为输出。配置了 [`GPIO_OUTPUT`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1) 返回 `1`，否则返回 `0`；错误为 `-ENOSYS`、`-EIO`、`-EWOULDBLOCK`。

<a id="ga2255c5681d17952ab89a4b6016d8e80d"></a>

## 266.30\_gpio_pin_is_output_dt

函数 [`gpio_pin_is_output_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga2255c5681d17952ab89a4b6016d8e80d) 的声明为：

```c
static inline int gpio_pin_is_output_dt(const struct gpio_dt_spec * spec);
```

检查设备树描述中的引脚是否为输出，返回 [`gpio_pin_is_output()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga3b854d759180e222299ea445b401acc1) 的结果：

```c
gpio_pin_is_output(spec->port, spec->pin);
```

<a id="gadac09ef40fc1ba5d8bb40965efde0fda"></a>

## 266.31\_gpio_pin_set

函数 [`gpio_pin_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gadac09ef40fc1ba5d8bb40965efde0fda) 的声明为：

```c
int gpio_pin_set(const struct device * port, gpio_pin_t pin, int value);
```

设置输出引脚的逻辑电平，考虑 `GPIO_ACTIVE_LOW`。`value` 为 `0` 时设置逻辑0/无效状态，任意非零值设置逻辑1/有效状态。默认高电平有效配置下，无效状态为物理低电平，且此函数等价于 [`gpio_pin_set_raw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga08824e05ea87c4ad2e48edaa13aad30a)；低电平有效配置下，无效状态为物理高电平。成功返回 `0`；错误为 `-EIO`、`-EWOULDBLOCK`，含义见前述约定。

<a id="ga541064fb9e575c0c559c101754466fa8"></a>

## 266.32\_gpio_pin_set_dt

函数 [`gpio_pin_set_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga541064fb9e575c0c559c101754466fa8) 的声明为：

```c
static inline int gpio_pin_set_dt(const struct gpio_dt_spec * spec, int value);
```

根据设备树描述设置输出引脚逻辑电平，`value` 为目标值，返回 [`gpio_pin_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gadac09ef40fc1ba5d8bb40965efde0fda) 的结果：

```c
gpio_pin_set(spec->port, spec->pin, value);
```

<a id="ga08824e05ea87c4ad2e48edaa13aad30a"></a>

## 266.33\_gpio_pin_set_raw

函数 [`gpio_pin_set_raw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga08824e05ea87c4ad2e48edaa13aad30a) 的声明为：

```c
int gpio_pin_set_raw(const struct device * port, gpio_pin_t pin, int value);
```

设置输出引脚物理电平，忽略 `GPIO_ACTIVE_LOW`。`value` 为 `0` 时输出低电平，任意非零值输出高电平。成功返回 `0`；错误为 `-EIO`、`-EWOULDBLOCK`，含义见前述约定。

<a id="gaa761788e22a185db227dce7c24915154"></a>

## 266.34\_gpio_pin_toggle

函数 [`gpio_pin_toggle()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gaa761788e22a185db227dce7c24915154) 的声明为：

```c
int gpio_pin_toggle(const struct device * port, gpio_pin_t pin);
```

翻转指定引脚的电平。成功返回 `0`；错误为 `-EIO`、`-EWOULDBLOCK`，含义见前述约定。

<a id="ga3272e866489da6c2e12c48f803c59e81"></a>

## 266.35\_gpio_pin_toggle_dt

函数 [`gpio_pin_toggle_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga3272e866489da6c2e12c48f803c59e81) 的声明为：

```c
static inline int gpio_pin_toggle_dt(const struct gpio_dt_spec * spec);
```

翻转设备树描述中引脚的电平，返回 [`gpio_pin_toggle()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gaa761788e22a185db227dce7c24915154) 的结果：

```c
gpio_pin_toggle(spec->port, spec->pin);
```

<a id="ga9318c349663568f1fb9400b9458765dc"></a>

## 266.36\_gpio_port_clear_bits

函数 [`gpio_port_clear_bits()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga9318c349663568f1fb9400b9458765dc) 的声明为：

```c
int gpio_port_clear_bits(const struct device * port, gpio_port_pins_t pins);
```

将 `pins` 掩码指定的输出引脚设置为逻辑无效状态。成功返回 `0`；错误为 `-EIO`、`-EWOULDBLOCK`，含义见前述约定。

<a id="ga9d2c9daeec7ce127fc786ead566ad27f"></a>

## 266.37\_gpio_port_clear_bits_raw

函数 [`gpio_port_clear_bits_raw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga9d2c9daeec7ce127fc786ead566ad27f) 的声明为：

```c
int gpio_port_clear_bits_raw(const struct device * port, gpio_port_pins_t pins);
```

将 `pins` 掩码指定的输出引脚设置为物理低电平。成功返回 `0`；错误为 `-EIO`、`-EWOULDBLOCK`，含义见前述约定。

<a id="ga7c7a53371834c7646dc7f41ca0bb7921"></a>

## 266.38\_gpio_port_get

函数 [`gpio_port_get()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga7c7a53371834c7646dc7f41ca0bb7921) 的声明为：

```c
int gpio_port_get(const struct device * port, gpio_port_value_t * value);
```

读取端口所有输入引脚的逻辑电平，考虑 `GPIO_ACTIVE_LOW`。引脚n的值保存为 `value` 所指变量的第n位。高电平有效时物理低读为0，低电平有效时物理低读为1。成功返回 `0`；错误为 `-EIO`、`-EWOULDBLOCK`，含义见前述约定。

<a id="gad2b2945dbe6987ac425e000721a894c4"></a>

## 266.39\_gpio_port_get_direction

函数 [`gpio_port_get_direction()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gad2b2945dbe6987ac425e000721a894c4) 的声明为：

```c
int gpio_port_get_direction(const struct device * port, gpio_port_pins_t map, gpio_port_pins_t * inputs, gpio_port_pins_t * outputs);
```

读取 `map` 位图指定的各引脚方向，将输入方向保存在 `inputs` 所指变量，将输出方向保存在 `outputs` 所指变量；任一指针为 `NULL` 时不取得对应方向信息。成功返回 `0`；错误为 `-ENOSYS`、`-EIO`、`-EWOULDBLOCK`。

<a id="gae2a49b36cae2e17fc665a3bd844f50b4"></a>

## 266.40\_gpio_port_get_raw

函数 [`gpio_port_get_raw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gae2a49b36cae2e17fc665a3bd844f50b4) 的声明为：

```c
int gpio_port_get_raw(const struct device * port, gpio_port_value_t * value);
```

读取端口所有输入引脚的物理电平，忽略 `GPIO_ACTIVE_LOW`。物理低表示0、物理高表示1；引脚n的值保存在 `value` 所指变量的第n位。成功返回 `0`；错误为 `-EIO`、`-EWOULDBLOCK`，含义见前述约定。

<a id="gab7465c5401aa9d47d68980455847be9f"></a>

## 266.41\_gpio_port_pin_is_supported

函数 [`gpio_port_pin_is_supported()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gab7465c5401aa9d47d68980455847be9f) 的声明为：

```c
static inline bool gpio_port_pin_is_supported(gpio_port_pins_t port_pin_mask, gpio_pin_t pin);
```

检查引脚是否在范围内且受控制器支持。`port_pin_mask` 是控制器支持引脚的掩码，即 [`gpio_driver_config::port_pin_mask`](P268_GPIO公共驱动配置.md)；`pin` 是待检查引脚号。在将引脚号用作移位数前，先与 [`GPIO_MAX_PINS_PER_PORT`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga1449ba90eaec5e6144fe4faae21f2e3f) 检查范围。驱动必须使用此辅助函数，不应直接测试 `port_pin_mask & BIT(pin)`，因为引脚号可能来自不可信调用方。范围有效且受支持返回 [`true`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a41f9c5fb8b08eb5dc3edce4dcb37fee7)，否则返回 [`false`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a65e9886d74aaee76545e83dd09011727)。

<a id="gae450ff904686aa4b8fd81bc0dbbafdb5"></a>

## 266.42\_gpio_port_set_bits

函数 [`gpio_port_set_bits()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gae450ff904686aa4b8fd81bc0dbbafdb5) 的声明为：

```c
int gpio_port_set_bits(const struct device * port, gpio_port_pins_t pins);
```

将 `pins` 掩码指定的输出引脚设置为逻辑有效状态。成功返回 `0`；错误为 `-EIO`、`-EWOULDBLOCK`，含义见前述约定。

<a id="ga18e6ca0df95566fecc0633efb04a075a"></a>

## 266.43\_gpio_port_set_bits_raw

函数 [`gpio_port_set_bits_raw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga18e6ca0df95566fecc0633efb04a075a) 的声明为：

```c
int gpio_port_set_bits_raw(const struct device * port, gpio_port_pins_t pins);
```

将 `pins` 掩码指定的输出引脚设置为物理高电平。成功返回 `0`；错误为 `-EIO`、`-EWOULDBLOCK`，含义见前述约定。

<a id="ga45172f2b1bb09e8f3c89fa951cdefc14"></a>

## 266.44\_gpio_port_set_clr_bits

函数 [`gpio_port_set_clr_bits()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga45172f2b1bb09e8f3c89fa951cdefc14) 的声明为：

```c
int gpio_port_set_clr_bits(const struct device * port, gpio_port_pins_t set_pins, gpio_port_pins_t clear_pins);
```

设置所选输出引脚的逻辑电平。`set_pins` 指定设置为有效状态的引脚，`clear_pins` 指定设置为无效状态的引脚。成功返回 `0`；错误为 `-EIO`、`-EWOULDBLOCK`，含义见前述约定。

<a id="ga1a06f729e76d39937d0572b6c531e038"></a>

## 266.45\_gpio_port_set_clr_bits_raw

函数 [`gpio_port_set_clr_bits_raw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga1a06f729e76d39937d0572b6c531e038) 的声明为：

```c
int gpio_port_set_clr_bits_raw(const struct device * port, gpio_port_pins_t set_pins, gpio_port_pins_t clear_pins);
```

设置所选输出引脚的物理电平。`set_pins` 指定设置为高电平的引脚，`clear_pins` 指定设置为低电平的引脚。成功返回 `0`；错误为 `-EIO`、`-EWOULDBLOCK`，含义见前述约定。

<a id="ga0c5ddbec7eb194ffed6cf12ae235ae04"></a>

## 266.46\_gpio_port_set_masked

函数 [`gpio_port_set_masked()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga0c5ddbec7eb194ffed6cf12ae235ae04) 的声明为：

```c
int gpio_port_set_masked(const struct device * port, gpio_port_pins_t mask, gpio_port_value_t value);
```

设置端口输出引脚的逻辑电平，考虑 `GPIO_ACTIVE_LOW`。`mask` 指定需要修改的引脚，`value` 指定输出值；两者第n位均对应引脚n。值位0表示逻辑0/无效，值位1表示逻辑1/有效。默认高电平有效时，无效状态为物理低电平；低电平有效时，无效状态为物理高电平。成功返回 `0`；错误为 `-EIO`、`-EWOULDBLOCK`，含义见前述约定。

<a id="ga9e7b50d720fda362941acc1e3b3b2922"></a>

## 266.47\_gpio_port_set_masked_raw

函数 [`gpio_port_set_masked_raw()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga9e7b50d720fda362941acc1e3b3b2922) 的声明为：

```c
int gpio_port_set_masked_raw(const struct device * port, gpio_port_pins_t mask, gpio_port_value_t value);
```

设置端口输出引脚的物理电平，忽略 `GPIO_ACTIVE_LOW`。`mask` 指定修改哪些引脚，`value` 给出目标值；两者第n位均对应引脚n。值位0输出低电平，值位1输出高电平。成功返回 `0`；错误为 `-EIO`、`-EWOULDBLOCK`，含义见前述约定。

<a id="ga82977d8706fb9f464db455bd0e9ac2e4"></a>

## 266.48\_gpio_port_toggle_bits

函数 [`gpio_port_toggle_bits()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga82977d8706fb9f464db455bd0e9ac2e4) 的声明为：

```c
int gpio_port_toggle_bits(const struct device * port, gpio_port_pins_t pins);
```

翻转 `pins` 掩码指定的输出引脚电平。成功返回 `0`；错误为 `-EIO`、`-EWOULDBLOCK`，含义见前述约定。

<a id="gac1e94ba8faac79f469447e9b5d2f8c06"></a>

## 266.49\_gpio_remove_callback

函数 [`gpio_remove_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gac1e94ba8faac79f469447e9b5d2f8c06) 的声明为：

```c
static inline int gpio_remove_callback(const struct device * port, struct gpio_callback * callback);
```

移除 `callback` 指向的有效应用回调，可以移除此前用 [`gpio_add_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga05fd15af20386d69f9332354285b0cca) 添加的各个回调。成功返回 `0`，失败返回负错误码；驱动未实现时返回 `-ENOSYS`。

**警告：**允许在回调处理函数内部移除当前正在执行的这个回调注册；尝试移除同一设备上的其他注册可能导致未定义行为，例如本应保留的回调未被调用，或已移除的回调被意外调用。

<a id="ga2c9f8fee2addfc0aeeeeb011d534f304"></a>

## 266.50\_gpio_remove_callback_dt

函数 [`gpio_remove_callback_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#ga2c9f8fee2addfc0aeeeeb011d534f304) 的声明为：

```c
static inline int gpio_remove_callback_dt(const struct gpio_dt_spec * spec, struct gpio_callback * callback);
```

根据设备树描述移除 `callback` 指向的有效应用回调，返回 [`gpio_remove_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface.html#gac1e94ba8faac79f469447e9b5d2f8c06) 的结果：

```c
gpio_remove_callback(spec->port, callback);
```


---

[上一章：WisBlockPWM通道](P265_WisBlockPWM通道.md) · [下一章：GPIO设备树描述](P267_GPIO设备树描述.md) · [返回大纲](大纲.md)
