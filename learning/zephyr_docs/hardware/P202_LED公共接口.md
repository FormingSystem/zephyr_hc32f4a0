---
id: learning.zephyr-docs.hardware.ledapi-0
title: LED公共接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第202章\_LED公共接口

原文：[group__led__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html)。读取日期：2026-10-13，`latest`。

## 202.1\_范围、版本与公共参数

本页提供 **发光二极管（Light-Emitting Diode，LED）**控制器的 **应用程序编程接口（Application Programming Interface，API）**。接口自 Zephyr 1.12 提供，本页版本为 1.0.0，主头文件为官方 `zephyr/drivers/led.h`。

相关结构包括设备树描述 [`led_dt_spec`](P203_LED设备树描述结构.md) 和信息结构 [`led_info`](P204_LED信息结构.md)。在下文普通接口中，`dev` 是 LED 设备，`led` 是该设备上的 LED 编号；带 `_dt` 后缀的接口用 `spec` 指向来自 **设备树（Devicetree，DT）**的 LED 描述结构。

本页所有返回 `int` 的函数都在成功时返回 0、出错时返回负值。就绪查询 [`led_is_ready_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gaa2994b959c730dad3432481bba278497) 返回布尔值，见本章最后一节。

## 202.2\_亮度上限宏

宏 [`LED_BRIGHTNESS_MAX`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga7bb18ca9f746ebcfbfc397886643f16d) 定义为 `100u`，亮度范围为 0 至 100。

## 202.3\_从设备树静态初始化描述结构

宏 `LED_DT_SPEC_GET(node_id)` 根据设备树节点标识符（Node Identifier）返回 `struct led_dt_spec` 的静态初始化器（Static Initializer）。译注：展开式中的 `DT_PARENT` 宏取父节点，`DEVICE_DT_GET` 宏取得该节点对应的设备指针，`DT_NODE_CHILD_IDX` 宏取得子节点索引；后续示例中的 `DT_NODELABEL` 宏将节点标签转换为节点标识符。其原始展开值为：

```c
{                                                                      \
        .dev = DEVICE_DT_GET(DT_PARENT(node_id)),                      \
        .index = DT_NODE_CHILD_IDX(node_id),                           \
}
```

原文设备树片段示例：

```dts
leds {
    compatible = "gpio-leds";
    led0: led_0 {
        ...
    };
};
```

原文使用示例：

```c
const struct led_dt_spec spec = LED_DT_SPEC_GET(DT_NODELABEL(led0));

// Initializes 'spec' to:
// {
//         .dev = DEVICE_DT_GET(DT_PARENT(led0)),
//         .index = 0,
// }
```

仍然必须检查 `dev` 设备是否就绪，例如调用 [`device_is_ready()`](../device_reference/P001_设备模型公共接口.md#gaa4944bd850e90cbd52b0489f9b12edfb)。译注：上面的 `...` 是省略的设备树内容，代码展示初始化关系；`gpio-leds` 表示通过 **通用输入输出（General-Purpose Input/Output，GPIO）**连接的 LED 设备。

宏 `LED_DT_SPEC_GET_OR(node_id, default_value)` 与 [`LED_DT_SPEC_GET()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga537f733ae3070fbe279834c76cda35ae) 类似；如果节点不存在，则使用备用值（Fallback Value）`default_value`。它返回相应的静态初始化结果，原始展开值为：

```c
COND_CODE_1(DT_NODE_EXISTS(node_id),                                   \
            (LED_DT_SPEC_GET(node_id)),                                \
            (default_value))
```

## 202.4\_闪烁

函数声明：

```c
int led_blink(const struct device *dev, uint32_t led,
              uint32_t delay_on, uint32_t delay_off);
static inline int led_blink_dt(const struct led_dt_spec *spec,
                               uint32_t delay_on, uint32_t delay_off);
```

[`led_blink()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga4f31fecd215e5597999be4d16b0d2dd5) 是可选操作，按指定时长使 LED 持续闪烁。`delay_on` 是亮灯时间，`delay_off` 是灭灯时间，单位均为毫秒。[`led_blink_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gab3581c7571b4623696ad57d25d6bd96f) 从 `spec` 获取设备和 LED 编号，其余参数含义相同。

两者成功返回 0，失败返回负值。

## 202.5\_读取LED信息

```c
int led_get_info(const struct device *dev, uint32_t led,
                 const struct led_info **info);
static inline int led_get_info_dt(const struct led_dt_spec *spec,
                                  const struct led_info **info);
```

[`led_get_info()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga9925483b97073354f7be6b40aa2dad1a) 是可选操作，提供 LED 信息。`info` 是指向指针的参数，函数通过它填写 LED 信息结构的指针。[`led_get_info_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga01ee05a71058adf86e950805524865a0) 从设备树描述取得对应 LED。两者成功返回 0，失败返回负值。

## 202.6\_设置亮度

```c
int led_set_brightness(const struct device *dev, uint32_t led, uint8_t value);
static inline int led_set_brightness_dt(const struct led_dt_spec *spec,
                                        uint8_t value);
```

[`led_set_brightness()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gaca479fd77518331f4fc84f788e345882) 是可选操作，`value` 为要设置的百分比亮度。在 [`led_blink()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga4f31fecd215e5597999be4d16b0d2dd5) 之后调用它，不会改变正在进行的闪烁行为。

只能开关的 LED 不必实现此操作：系统会自动使用开关接口，当 `value` 非零时点亮，为零时关闭。

[`led_set_brightness_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gaecc33acfc2b1dde870b411d7f30eed82) 使用设备树描述中的设备与编号，`value` 同样为百分比。两者成功返回 0，失败返回负值。

## 202.7\_写入连续通道与单个通道

```c
int led_write_channels(const struct device *dev, uint32_t start_channel,
                       uint32_t num_channels, const uint8_t *buf);
int led_set_channel(const struct device *dev, uint32_t channel, uint8_t value);
```

可选函数 [`led_write_channels()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga24d4007f81483d0fe8b9988288adf59a) 用数组中的值写入或更新一段连续 LED 通道（Channel），可同时配置多个 LED。

| 参数 | 含义 |
| --- | --- |
| `start_channel` | 首个待更新通道的绝对编号，不是相对于某一个 LED 的编号。 |
| `num_channels` | 要写入或更新的通道数量。 |
| `buf` | 通道配置值数组，必须提供 `num_channels` 个条目。 |

可选函数 [`led_set_channel()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga717bdbe76331b6286c58feb6e3e214dd) 把单个通道设为 `value`。`channel` 也是绝对通道编号，不是相对于某个 LED 的编号。

在 [`led_blink()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga4f31fecd215e5597999be4d16b0d2dd5) 之后调用上述任一函数，都不会改变闪烁行为。两者成功返回 0，失败返回负值。

## 202.8\_设置颜色

```c
int led_set_color(const struct device *dev, uint32_t led,
                   uint8_t num_colors, const uint8_t *color);
static inline int led_set_color_dt(const struct led_dt_spec *spec,
                                    uint8_t num_colors, const uint8_t *color);
```

[`led_set_color()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga94dd46cc96f6ade5cebaa46a5f7ca5ea) 用给定颜色数组配置一个 LED 的全部颜色通道。`num_colors` 为数组中的颜色数量，`color` 指向数组；数组顺序必须遵守控制器的颜色映射（Color Mapping），见 [`led_info`](https://docs.zephyrproject.org/latest/doxygen/html/structled__info.html) 的 `color_mapping` 成员。

在 [`led_blink()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga4f31fecd215e5597999be4d16b0d2dd5) 之后设置颜色，不会改变闪烁行为。[`led_set_color_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga4a30a26f21d80f40ce3364880e0dfee3) 从设备树描述取得对应 LED，对数组数量与顺序的要求相同。两者成功返回 0，失败返回负值。

## 202.9\_点亮与关闭

```c
int led_on(const struct device *dev, uint32_t led);
int led_off(const struct device *dev, uint32_t led);
static inline int led_on_dt(const struct led_dt_spec *spec);
static inline int led_off_dt(const struct led_dt_spec *spec);
```

函数 [`led_on()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gad4daafd7fcab22d1d68745b7264d0f73) 点亮 LED，[`led_off()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga22c9dbe76f06fec327aebe06448d1542) 关闭 LED。已实现亮度控制的设备不必单独实现这两个操作，系统会自动使用 `set_brightness` 驱动接口。

函数 [`led_on_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#gaa2b262a309e4ede4cb5715c69d900804)、[`led_off_dt()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__interface.html#ga8b6618e4fea4f44f218f95fd16abc16b) 对设备树描述中的 LED 执行相同操作。四个函数均在成功时返回 0，出错时返回负值。

## 202.10\_检查就绪状态

```c
static inline bool led_is_ready_dt(const struct led_dt_spec *spec);
```

`led_is_ready_dt()` 检查 `spec` 指定的 LED 设备是否可用。就绪返回 [`true`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a41f9c5fb8b08eb5dc3edce4dcb37fee7)，尚未就绪返回 [`false`](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#a65e9886d74aaee76545e83dd09011727)。

## 202.11\_相关主题

[模拟LED控制器（Fake LED Controller）](P207_模拟LED控制器.md)、[LED驱动后端接口（LED Driver Backend API）](P205_LED驱动后端接口.md)以及[驱动示例目录](P187_LED驱动示例目录.md)。

[上一章：XEC呼吸闪烁灯示例](P201_XEC呼吸闪烁灯示例.md) · [下一章：LED设备树描述结构](P203_LED设备树描述结构.md) · [返回大纲](大纲.md)
