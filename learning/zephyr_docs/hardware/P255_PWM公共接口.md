---
id: learning.zephyr-docs.hardware.pwmapi-0
title: PWM公共接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第255章\_PWM公共接口

原文：[group__pwm__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html)。读取日期：2026-10-13，`latest`。

<a id="gae1dcfb878163da76041efcedf0960fa0"></a>

## 255.1\_范围、类型与配置

本页定义 **脉宽调制（Pulse Width Modulation，PWM）**控制器的 **应用程序编程接口（Application Programming Interface，API）**，自 Zephyr 1.0 提供，本页版本为 1.0.0。主头文件为 `zephyr/drivers/pwm.h`；周期换算及极性宏来自 `zephyr/dt-bindings/pwm/pwm.h`。

<a id="ga5bc9607de7643cb78476ed354c51560b"></a>

类型 [`pwm_flags_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gae1dcfb878163da76041efcedf0960fa0) 定义为 [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)，保存配置标志。低 8 位为标准标志，高 8 位保留给 **片上系统（System on Chip，SoC）**专用标志。类型 [`pwm_events_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga5bc9607de7643cb78476ed354c51560b) 同样定义为 [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)，保存事件位掩码（Event Bitmask）。

捕获功能要求启用配置系统 Kconfig 的 [`CONFIG_PWM_CAPTURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_CAPTURE)，事件功能要求 [`CONFIG_PWM_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_EVENT)。配套结构为[设备树描述](P256_PWM设备树描述.md)和[事件回调结构](P257_PWM事件回调结构.md)。

## 255.2\_极性与捕获配置标志

<a id="ga2c706bbada711f383d7b42f09dace861"></a>

<a id="ga930c0ab50f81aeb571af9747947d7fae"></a>

极性（Polarity）宏用于 [`pwm_set_cycles()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gaff280789f7b45fdefc354b3f841fe3ef)、[`pwm_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gadd9049c9a56cd9419736b3514e42dc01) 或 [`pwm_configure_capture()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga9603146d7f9c2690c1e1983113d6c6bb)，位于 [`pwm_flags_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gae1dcfb878163da76041efcedf0960fa0) 的低 8 位：`PWM_POLARITY_NORMAL = (0 << 0)` 表示正常极性、脉冲高电平有效（Active High）；`PWM_POLARITY_INVERTED = (1 << 0)` 表示反相极性、脉冲低电平有效（Active Low）。

捕获（Capture）标志宏如下。`PWM_CAPTURE_TYPE_SHIFT` 和 `PWM_CAPTURE_MODE_SHIFT` 是相应标志的移位量标识，原页这些定义保留为表达式。

| 宏 | 值 | 含义 |
| --- | --- | --- |
| <a id="ga5b4b41ccdf8810a77f71c2155a521f44"></a>[`PWM_CAPTURE_TYPE_PERIOD`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga5b4b41ccdf8810a77f71c2155a521f44) | `(1U << PWM_CAPTURE_TYPE_SHIFT)` | 捕获周期（Period）。 |
| <a id="gab883b83cc5418555a437ce128f32ab01"></a>[`PWM_CAPTURE_TYPE_PULSE`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gab883b83cc5418555a437ce128f32ab01) | `(2U << PWM_CAPTURE_TYPE_SHIFT)` | 捕获脉宽（Pulse Width）。 |
| <a id="gad59fe75340facda843cad06993cf1814"></a>[`PWM_CAPTURE_MODE_SINGLE`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gad59fe75340facda843cad06993cf1814) | `(0U << PWM_CAPTURE_MODE_SHIFT)` | 单次捕获周期/脉宽。 |
| <a id="gabe9bbff9832b4fa40faa057fad8fdaa9"></a>[`PWM_CAPTURE_MODE_CONTINUOUS`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gabe9bbff9832b4fa40faa057fad8fdaa9) | `(1U << PWM_CAPTURE_MODE_SHIFT)` | 连续捕获周期/脉宽。 |

<a id="ga76175b0c2d5187ded5bbd314dc798bd5"></a>

宏 [`PWM_CAPTURE_TYPE_BOTH`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga76175b0c2d5187ded5bbd314dc798bd5) 同时捕获周期和脉宽，原展开式：

```c
(PWM_CAPTURE_TYPE_PERIOD | \
PWM_CAPTURE_TYPE_PULSE)
```

## 255.3\_设备树静态初始化宏

设备树（Devicetree，DT）宏返回 `struct pwm_dt_spec` 的 **静态初始化器（Static Initializer）**。参数 `node_id` 是节点标识，`idx` 是 `pwms` 属性中的逻辑索引；按名选择时，`name` 是 `pwm-names` 中对应元素的小写加下划线名称。`default_value` 是缺失节点或属性时的后备值。

<a id="ga59a79f0b77c5b71252bde126f333a84b"></a>

宏 `PWM_DT_SPEC_GET(node_id)` 取得索引 0 的描述，原展开式：

```c
PWM_DT_SPEC_GET_BY_IDX(node_id, 0)
```

<a id="ga7e8375bcf95ae6a9500ce3aba4586de4"></a>

宏 `PWM_DT_SPEC_GET_BY_IDX(node_id, idx)` 按节点与索引取得设备、通道、周期和标志。展开式中的 [`DEVICE_DT_GET`](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7) 取得设备，[`DT_PWMS_CTLR_BY_IDX`](P264_设备树PWM宏.md)、[`DT_PWMS_CHANNEL_BY_IDX`](P264_设备树PWM宏.md)、[`DT_PWMS_PERIOD_BY_IDX`](P264_设备树PWM宏.md)、[`DT_PWMS_FLAGS_BY_IDX`](P264_设备树PWM宏.md) 分别提取控制器、通道、周期和标志。

```c
{                                                                      \
        .dev = DEVICE_DT_GET(DT_PWMS_CTLR_BY_IDX(node_id, idx)),       \
        .channel = DT_PWMS_CHANNEL_BY_IDX(node_id, idx),               \
        .period = DT_PWMS_PERIOD_BY_IDX(node_id, idx),                 \
        .flags = DT_PWMS_FLAGS_BY_IDX(node_id, idx),                   \
}
```

原设备树例子：

```dts
n: node {
    pwms = <&pwm1 1 1000 PWM_POLARITY_NORMAL>,
           <&pwm2 3 2000 PWM_POLARITY_INVERTED>;
};
```

原使用示例中的 [`DT_NODELABEL`](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79) 按节点标签取得标识。索引 1 选择控制器节点 `pwm2`、通道 3、周期 2000 纳秒和反相极性：

```c
const struct pwm_dt_spec spec =
    PWM_DT_SPEC_GET_BY_IDX(DT_NODELABEL(n), 1);

// Initializes 'spec' to:
// {
//         .dev = DEVICE_DT_GET(DT_NODELABEL(pwm2)),
//         .channel = 3,
//         .period = 2000,
//         .flags = PWM_POLARITY_INVERTED,
// }
```

生成描述后仍需检查 `dev` 是否就绪，例如调用函数 [`device_is_ready()`](../device_reference/P001_设备模型公共接口.md#gaa4944bd850e90cbd52b0489f9b12edfb)。只有节点存在、具有 `pwms` 属性，且属性给出了 PWM 控制器、通道、纳秒周期和可选标志时才能使用这些初始化宏，否则是错误用法。

<a id="gaf5808fd88b101208681820b53bca33e1"></a>

宏 `PWM_DT_SPEC_GET_BY_IDX_OR(node_id, idx, default_value)` 提供后备值：节点有 `pwms` 属性时展开为按索引版本，**此时不展开 `default_value`**；否则展开为后备值。原定义通过条件宏 [`COND_CODE_1`](../util_reference/P001_通用工具公共接口.md#ga358bc3e7669c860a98839a51cd526b20) 和属性检查宏 [`DT_NODE_HAS_PROP`](../dt_identity_reference/P002_设备树存在性与状态宏.md#gacce67bf20541cd2d07d8540058964692) 判断：

```c
COND_CODE_1(DT_NODE_HAS_PROP(node_id, pwms),                           \
            (PWM_DT_SPEC_GET_BY_IDX(node_id, idx)),                    \
            (default_value))
```

<a id="ga88b92c580860441c83d1b03db25fc4f1"></a>

宏 `PWM_DT_SPEC_GET_BY_NAME(node_id, name)` 按名称取得描述。宏 `DT_PWMS_CTLR_BY_NAME`、`DT_PWMS_CHANNEL_BY_NAME`、`DT_PWMS_PERIOD_BY_NAME`、`DT_PWMS_FLAGS_BY_NAME` 分别提取控制器、通道、周期和标志，与前面的索引版本对应：

```c
{                                                                      \
        .dev = DEVICE_DT_GET(DT_PWMS_CTLR_BY_NAME(node_id, name)),     \
        .channel = DT_PWMS_CHANNEL_BY_NAME(node_id, name),             \
        .period = DT_PWMS_PERIOD_BY_NAME(node_id, name),               \
        .flags = DT_PWMS_FLAGS_BY_NAME(node_id, name),                 \
}
```

原设备树例子增加 `pwm-names`：

```dts
n: node {
    pwms = <&pwm1 1 1000 PWM_POLARITY_NORMAL>,
           <&pwm2 3 2000 PWM_POLARITY_INVERTED>;
    pwm-names = "alpha", "beta";
};
```

原用法按名称 `alpha` 选择控制器节点 `pwm1`、通道 1、周期 1000 纳秒和正常极性：

```c
const struct pwm_dt_spec spec =
    PWM_DT_SPEC_GET_BY_NAME(DT_NODELABEL(n), alpha);

// Initializes 'spec' to:
// {
//         .dev = DEVICE_DT_GET(DT_NODELABEL(pwm1)),
//         .channel = 1,
//         .period = 1000,
//         .flags = PWM_POLARITY_NORMAL,
// }
```

按名版本同样要求节点与 `pwms` 属性有效，且生成后仍需检查设备就绪。译注：该宏原说明概述写“节点标识和索引”，但参数、展开式和例子均按名称选择，这里明确其按名语义。

<a id="ga5557add2123a7138b64997cd070e0ee6"></a>

宏 `PWM_DT_SPEC_GET_BY_NAME_OR(node_id, name, default_value)` 在有 `pwms` 属性时使用按名版本且不展开后备值，否则使用后备值：

```c
COND_CODE_1(DT_NODE_HAS_PROP(node_id, pwms),                           \
            (PWM_DT_SPEC_GET_BY_NAME(node_id, name)),                  \
            (default_value))
```

<a id="ga82f8efe8f0bc088fdda58c09dd4be4ff"></a>

宏 `PWM_DT_SPEC_GET_OR(node_id, default_value)` 等价于带后备值的索引 0 版本：

```c
PWM_DT_SPEC_GET_BY_IDX_OR(node_id, 0, default_value)
```

## 255.4\_设备实例初始化宏

下面的 `inst` 都是驱动兼容标识宏 `DT_DRV_COMPAT` 对应的实例编号；[`DT_DRV_INST`](../dt_instance_reference/P001_设备树驱动实例宏.md#ga219f413efba2f4c0151468b9a25a8dc1) 将它转换为节点标识。`idx`、`name`、`default_value` 含义与上一节相同；带 `_OR` 的版本在节点或属性不存在时返回后备值。

<a id="gaa346428c6cb1f11aafaa6306486e8a4b"></a>

宏 `PWM_DT_SPEC_INST_GET(inst)` 取得实例的索引 0 描述：

```c
PWM_DT_SPEC_GET(DT_DRV_INST(inst))
```

<a id="ga3c1c557fa4461e61f4a147fc72f87f8d"></a>

宏 `PWM_DT_SPEC_INST_GET_BY_IDX(inst, idx)` 按实例与索引取得描述：

```c
PWM_DT_SPEC_GET_BY_IDX(DT_DRV_INST(inst), idx)
```

<a id="ga7eeef648c3142fced48b7ab52c9c1ead"></a>

宏 `PWM_DT_SPEC_INST_GET_BY_IDX_OR(inst, idx, default_value)` 是带后备值的按索引版本：

```c
PWM_DT_SPEC_GET_BY_IDX_OR(DT_DRV_INST(inst), idx, default_value)
```

<a id="ga104a81a3481362d2da9046c0e93a8cd0"></a>

宏 `PWM_DT_SPEC_INST_GET_BY_NAME(inst, name)` 按实例与名称取得描述：

```c
PWM_DT_SPEC_GET_BY_NAME(DT_DRV_INST(inst), name)
```

<a id="gac00e53eccaf9eb515aed0921404adb31"></a>

宏 `PWM_DT_SPEC_INST_GET_BY_NAME_OR(inst, name, default_value)` 是带后备值的按名版本：

```c
PWM_DT_SPEC_GET_BY_NAME_OR(DT_DRV_INST(inst), name, default_value)
```

<a id="ga6bd84121715beb62a3ca2672dfae0630"></a>

宏 `PWM_DT_SPEC_INST_GET_OR(inst, default_value)` 是带后备值的索引 0 版本，等价于 `PWM_DT_SPEC_INST_GET_BY_IDX_OR(inst, 0, default_value)`：

```c
PWM_DT_SPEC_GET_OR(DT_DRV_INST(inst), default_value)
```

## 255.5\_周期与频率换算宏

PWM 描述符的周期单元（Period Cell）必须以纳秒（Nanosecond）给出；下列宏方便以其他尺度指定周期或频率，参数 `x` 为所需数值。

<a id="ga4a5edbee48c4a5706cf75524aef2364a"></a>

宏 `PWM_HZ(x)` 用赫兹（Hertz，Hz）指定频率：

```c
(PWM_SEC(1UL) / (x))
```

<a id="gaf846cf23d31d14296e0cbc1f82a530f4"></a>

宏 `PWM_KHZ(x)` 用千赫兹（Kilohertz，kHz）指定频率：

```c
(PWM_HZ((x) * 1000UL))
```

<a id="ga1cccc226a23866dd2dcac9467ff3af0e"></a>

宏 `PWM_MSEC(x)` 用毫秒（Millisecond）指定周期：

```c
(PWM_USEC(x) * 1000UL)
```

<a id="ga17f20d628bcc81d5023c39e4cdfad405"></a>

宏 `PWM_NSEC(x)` 用纳秒指定周期：

```c
(x)
```

<a id="ga4da4565d4dbded0efb640bd538cba3c2"></a>

宏 `PWM_SEC(x)` 用秒（Second）指定周期：

```c
(PWM_MSEC(x) * 1000UL)
```

<a id="ga368f28c8daaee25e546484bd908e675e"></a>

宏 `PWM_USEC(x)` 用微秒（Microsecond）指定周期：

```c
(PWM_NSEC(x) * 1000UL)
```

<a id="gaff280789f7b45fdefc354b3f841fe3ef"></a>

<a id="gadd9049c9a56cd9419736b3514e42dc01"></a>

## 255.6\_设置输出周期与脉宽

以下各函数中的 `dev` 为 PWM 设备实例，`channel` 为通道号。

```c
int pwm_set_cycles(const struct device *dev, uint32_t channel,
                    uint32_t period, uint32_t pulse, pwm_flags_t flags);
static inline int pwm_set(const struct device *dev, uint32_t channel,
                            uint32_t period, uint32_t pulse, pwm_flags_t flags);
```

函数 [`pwm_set_cycles()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gaff280789f7b45fdefc354b3f841fe3ef) 为一个输出设置周期 `period`、脉宽 `pulse`，两者单位为硬件相关的时钟周期（Clock Cycle）；[`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 为引脚配置标志。

原文规定周期和脉宽同步更新以避免毛刺（Glitch），调用不会阻塞等待更新生效；同时明确：**并非所有控制器都支持同步、无毛刺更新**，实际硬件在更改周期或脉宽时可能产生毛刺。某些多通道控制器共享周期，更改一个通道可能影响其他通道。

`pulse=0` 使引脚保持恒定无效电平；`pulse` 非零且等于 `period` 时保持恒定有效电平。成功返回 0，失败返回负错误码；`-EINVAL` 表示脉宽超过周期。

函数 [`pwm_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gadd9049c9a56cd9419736b3514e42dc01) 参数含义相同，但周期和脉宽以**纳秒**表示，[`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 用于极性配置。可用 [`PWM_MSEC()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga1cccc226a23866dd2dcac9467ff3af0e) 等宏转换其他单位。成功返回 0，失败返回负错误码；`-ENOTSUP` 表示不支持请求的周期或脉宽所对应的时钟周期数。

## 255.7\_从设备树描述设置输出

```c
static inline int pwm_set_dt(const struct pwm_dt_spec *spec,
                              uint32_t period, uint32_t pulse);
static inline int pwm_set_pulse_dt(const struct pwm_dt_spec *spec, uint32_t pulse);
```

<a id="ga225ce58ceb3de3d76df3e03439d655b9"></a>

函数 [`pwm_set_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga225ce58ceb3de3d76df3e03439d655b9) 使用设备树描述 `spec` 的设备、通道及标志，但用显式 `period` 覆盖其周期；`period`、`pulse` 都以纳秒表示，适合运行时改变设备树原周期。等价调用为：

```c
pwm_set(spec->dev, spec->channel, period, pulse, spec->flags)
```

<a id="ga8ff263177143d33c6d0a284b837bc4da"></a>

函数 [`pwm_set_pulse_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga8ff263177143d33c6d0a284b837bc4da) 使用 `spec` 中的周期，只传入纳秒脉宽 `pulse`，等价调用为：

```c
pwm_set(spec->dev, spec->channel, spec->period, pulse, spec->flags)
```

两个函数都返回 [`pwm_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gadd9049c9a56cd9419736b3514e42dc01) 的结果。

## 255.8\_时钟频率查询与周期换算

```c
int pwm_get_cycles_per_sec(const struct device *dev, uint32_t channel, uint64_t *cycles);
static inline int pwm_cycles_to_usec(const struct device *dev, uint32_t channel,
                                      uint32_t cycles, uint64_t *usec);
static inline int pwm_cycles_to_nsec(const struct device *dev, uint32_t channel,
                                      uint32_t cycles, uint64_t *nsec);
```

<a id="ga310d416087a619f90e946222668135af"></a>

函数 [`pwm_get_cycles_per_sec()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga310d416087a619f90e946222668135af) 查询一个 PWM 输出的硬件相关时钟速率，将每秒周期数写入 `cycles` 指向的存储。

<a id="gae57fb205e43dde82d96abe79966539a9"></a>

<a id="ga6f0281398611dd876386c66a63373a2e"></a>

函数 [`pwm_cycles_to_usec()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gae57fb205e43dde82d96abe79966539a9)、[`pwm_cycles_to_nsec()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga6f0281398611dd876386c66a63373a2e) 将输入 `cycles` 分别换算为微秒、纳秒，结果写入 `usec` 或 `nsec` 指向的存储。

三者成功返回 0，失败返回负错误码；两个换算函数列出 `-ERANGE`，表示结果太大（Result Too Large）。

## 255.9\_捕获回调类型与配置

<a id="ga2395ef29b77674d9f1b56d8091b8695a"></a>

捕获处理函数类型 [`pwm_capture_callback_handler_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga2395ef29b77674d9f1b56d8091b8695a) 的声明为：

```c
typedef void (*pwm_capture_callback_handler_t)(const struct device *dev,
    uint32_t channel, uint32_t period_cycles, uint32_t pulse_cycles,
    int status, void *user_data);
```

`dev`、`channel` 指明设备及通道；`period_cycles`、`pulse_cycles` 是硬件相关的时钟周期计数，分别表示捕获周期和脉宽。`status=0` 表示无错误，否则为负错误码，含义见单次捕获返回值；`user_data` 来自配置函数。**捕获回调在中断上下文（Interrupt Context）执行**，必须启用 [`CONFIG_PWM_CAPTURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_CAPTURE)。

<a id="ga9603146d7f9c2690c1e1983113d6c6bb"></a>

配置函数 [`pwm_configure_capture()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga9603146d7f9c2690c1e1983113d6c6bb) 的声明：

```c
static inline int pwm_configure_capture(const struct device *dev, uint32_t channel,
    pwm_flags_t flags, pwm_capture_callback_handler_t cb, void *user_data);
int pwm_enable_capture(const struct device *dev, uint32_t channel);
int pwm_disable_capture(const struct device *dev, uint32_t channel);
```

[`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 为捕获标志，`cb` 是捕获后调用的应用处理函数，`user_data` 为传给该函数的数据。配置后通过 [`pwm_enable_capture()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gad14ca53862a465d1789e8936ce394f9a) 启用，通过 [`pwm_disable_capture()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga1df2bb40af2fa3ce945cc9cd67edc2bf) 禁用；**启用前必须先配置**。这三个函数均要求 [`CONFIG_PWM_CAPTURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_CAPTURE)。

因为配置函数使用回调，它不能从 **用户空间（User Space）**调用；用户空间可使用后面的单次捕获接口。

| 函数 | 成功值 | 原文错误返回 |
| --- | --- | --- |
| [`pwm_configure_capture()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga9603146d7f9c2690c1e1983113d6c6bb) | 0 | `-EINVAL` 参数无效；`-ENOSYS` 不支持捕获或给定标志；`-EIO` 配置时输入输出错误；`-EBUSY` 捕获已经进行中。 |
| <a id="gad14ca53862a465d1789e8936ce394f9a"></a>[`pwm_enable_capture()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gad14ca53862a465d1789e8936ce394f9a) | 0 | `-EINVAL` 参数无效；`-ENOSYS` 不支持捕获；`-EIO` 启用时输入输出错误；`-EBUSY` 捕获已经进行中。 |
| <a id="ga1df2bb40af2fa3ce945cc9cd67edc2bf"></a>[`pwm_disable_capture()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga1df2bb40af2fa3ce945cc9cd67edc2bf) | 0 | `-EINVAL` 参数无效；`-ENOSYS` 不支持捕获；`-EIO` 禁用时输入输出错误。 |

上述错误码标识分别对应无效参数（Invalid Argument）、未实现支持（Not Implemented）、输入输出错误（Input/Output Error）和忙（Busy）。

## 255.10\_阻塞式单次捕获

```c
int pwm_capture_cycles(const struct device *dev, uint32_t channel,
    pwm_flags_t flags, uint32_t *period, uint32_t *pulse, k_timeout_t timeout);
static inline int pwm_capture_usec(const struct device *dev, uint32_t channel,
    pwm_flags_t flags, uint64_t *period, uint64_t *pulse, k_timeout_t timeout);
static inline int pwm_capture_nsec(const struct device *dev, uint32_t channel,
    pwm_flags_t flags, uint64_t *period, uint64_t *pulse, k_timeout_t timeout);
```

三个函数都对一个输入执行单次周期/脉宽捕获，要求 [`CONFIG_PWM_CAPTURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_CAPTURE)。[`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 是捕获标志；`period`、`pulse` 指向结果存储；`timeout` 是内核超时类型 [`k_timeout_t`](../timer_reference/P087_内核超时类型.md) 的等待期限，**不支持立即返回值 `K_NO_WAIT`**。

<a id="ga09767ae3c8d970675dbf9e3e50291743"></a>

<a id="ga3a1552ea924eeec21477396da6d3890b"></a>

<a id="ga6489095d890224d23c5ed05bc884d24a"></a>

函数 [`pwm_capture_cycles()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga09767ae3c8d970675dbf9e3e50291743) 包装配置、启用、禁用捕获调用，以硬件相关的时钟周期数返回结果。[`pwm_capture_usec()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga3a1552ea924eeec21477396da6d3890b) 包装它与微秒换算函数，输出微秒；[`pwm_capture_nsec()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga6489095d890224d23c5ed05bc884d24a) 包装它与纳秒换算函数，输出纳秒。三者都**阻塞到捕获完成或等待超时**。

成功返回 0，失败为负错误码：`-EINVAL` 表示传入 `K_NO_WAIT`；`-EBUSY` 表示捕获已经进行中；`-EAGAIN` 表示等待超时（Waiting Period Timed Out）；`-EIO` 表示捕获时输入输出错误；`-ERANGE` 表示结果太大。

## 255.11\_事件类型与处理函数

<a id="ga94f1e31fe6b935569698e8f404955bd6"></a>

事件位移宏 `PWM_EVENT_TYPE_SHIFT = 0U`。各事件宏为：

| 宏 | 值 | 含义 |
| --- | --- | --- |
| <a id="gac438636e8379df41970b601fdf8a038a"></a>[`PWM_EVENT_TYPE_PERIOD`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gac438636e8379df41970b601fdf8a038a) | `(1U << PWM_EVENT_TYPE_SHIFT)` | 每个 PWM 周期结束时触发。 |
| <a id="ga70e0635a1187061921f559646a6e2456"></a>[`PWM_EVENT_TYPE_FAULT`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga70e0635a1187061921f559646a6e2456) | `(2U << PWM_EVENT_TYPE_SHIFT)` | 故障（Fault）触发，用来响应改变 PWM 外设行为的错误，通常会禁用输出；来源可以是内部，例如振荡器故障，或外部，例如原文的 pio。 |
| <a id="ga4e1b5b2c0a6b489eba876a8317acda45"></a>[`PWM_EVENT_TYPE_COMPARE_CAPTURE`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga4e1b5b2c0a6b489eba876a8317acda45) | `(4U << PWM_EVENT_TYPE_SHIFT)` | 比较/捕获匹配（Compare/Capture Match）触发：输出比较时计数器达到比较值，或输入捕获时捕获到外部边沿。 |

原文没有展开小写 `pio`，这里保留其外部故障来源示例名称。

<a id="gaedacc300332a9c01da48671f92bf0097"></a>

事件处理函数类型 [`pwm_event_callback_handler_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gaedacc300332a9c01da48671f92bf0097)：

```c
typedef void (*pwm_event_callback_handler_t)(const struct device *dev,
    struct pwm_event_callback *callback, uint32_t channel, pwm_events_t events);
```

`dev` 为设备实例，`callback` 指向拥有此处理函数的原始回调结构，`channel` 为通道，`events` 为事件掩码。回调**可能在中断上下文**执行，要求启用 [`CONFIG_PWM_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_EVENT)。

## 255.12\_事件回调初始化、添加与移除

```c
static inline void pwm_init_event_callback(struct pwm_event_callback *callback,
    pwm_event_callback_handler_t handler, uint32_t channel, pwm_events_t event_mask);
static inline int pwm_add_event_callback(const struct device *dev,
                                         struct pwm_event_callback *callback);
static inline int pwm_remove_event_callback(const struct device *dev,
                                            struct pwm_event_callback *callback);
```

<a id="gaf87ef431d50a482910e77e49d52a2e13"></a>

函数 [`pwm_init_event_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gaf87ef431d50a482910e77e49d52a2e13) 正确初始化回调结构：`callback` 为有效的应用回调结构指针，`handler` 为有效处理函数指针，`channel` 为关注的通道，`event_mask` 为关注事件的位掩码。函数无返回值。

<a id="ga09d1b358df32e798e0345cd647450d54"></a>

<a id="ga83d9ec60d3fef69c97602365b979aece"></a>

函数 [`pwm_add_event_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga09d1b358df32e798e0345cd647450d54) 添加应用回调，一个设备实例可以按需添加多个。函数 [`pwm_remove_event_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga83d9ec60d3fef69c97602365b979aece) 移除应用回调。两者的 `callback` 均必须为有效结构指针；成功返回 0，失败返回负错误码，`-ENOSYS` 表示驱动不管理事件回调。

本节三个函数均要求 [`CONFIG_PWM_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_EVENT)。回调结构的生命周期约束见[专用结构页](P257_PWM事件回调结构.md)。

## 255.13\_设备就绪与相关接口

<a id="ga70aad0d88e8041c880499e7cdaa9ae57"></a>

函数 [`pwm_is_ready_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga70aad0d88e8041c880499e7cdaa9ae57) 检查设备树 PWM 描述 `spec` 对应的设备是否就绪：

```c
static inline bool pwm_is_ready_dt(const struct pwm_dt_spec *spec);
```

可使用时返回 [`true`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a41f9c5fb8b08eb5dc3edce4dcb37fee7)，不可使用时返回 [`false`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a65e9886d74aaee76545e83dd09011727)。

原页相关专题还包括[器件扩展](P261_PWM器件扩展目录.md)、[设备树PWM宏](P264_设备树PWM宏.md)、[模拟PWM驱动](P260_PWM模拟控制器.md)与[驱动后端](P258_PWM驱动后端接口.md)。

---

[上一章：MIPI显示串行函数表](P254_MIPI显示串行函数表.md) · [下一章：PWM设备树描述](P256_PWM设备树描述.md) · [返回大纲](大纲.md)
