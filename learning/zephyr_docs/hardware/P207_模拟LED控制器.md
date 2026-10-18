---
id: learning.zephyr-docs.hardware.ledbackend-2
title: 模拟LED控制器
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第207章\_模拟LED控制器

原文：[group__led__fake](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html)。读取日期：2026-10-13，`latest`。

## 207.1\_用途与启用方式

这是用于测试的 **模拟发光二极管控制器（Fake Light-Emitting Diode Controller）**驱动，使用 **模拟函数框架（Fake Function Framework，FFF）**实现 LED **应用程序编程接口（Application Programming Interface，API）**。

通过 Kconfig 配置项 [`CONFIG_LED_FAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LED_FAKE) 启用驱动，并从兼容标识为 [`zephyr,fake-leds`](https://docs.zephyrproject.org/latest/build/dts/api/bindings/led/zephyr%2Cfake-leds.html#std-dtcompatible-zephyr-fake-leds) 的设备树（Devicetree）节点实例化。相关声明来自官方头文件 `zephyr/drivers/led/led_fake.h`。

## 207.2\_控制模拟行为

每个模拟函数（Fake Function）都有一个配套的 FFF 控制结构，名称为函数名再加 `_fake` 后缀。测试可以通过它设置返回值、安装自定义模拟函数，或检查调用次数和捕获的参数。

本页不列出这些控制结构的完整定义，原文指向[通过FFF模拟函数](https://docs.zephyrproject.org/latest/develop/test/ztest.html#mocking-fff)。

对于只报告状态的函数，可设置 `return_val`。具有输出参数的模拟函数必须通过 `custom_fake` 驱动，因为仅设置 `return_val` 不会修改那些输出参数。

启用 Kconfig 配置项 [`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST) 时，Zephyr 单元测试框架 ztest 的规则会在每个测试用例（Test Case）之前重置所有模拟函数。

[`fake_led_get_info()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#gae4f88da2cfa43c93bc0f2d294b6f848e) 和 [`fake_led_set_color()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#ga1860bf2d9d105ee8ecb7a092e2017b63) 默认有 `custom_fake`，根据设备树节点解析 LED 索引与颜色数量；每次重置都会重新安装这些默认实现。要改变它们报告的内容，应在测试用例内安装自己的 `custom_fake`。

## 207.3\_原文测试示例

下例把点亮操作的返回值设为 `-EIO`，并断言错误码、调用次数和捕获到的 LED 编号。[`EIO`](../error_reference/P003_系统错误号公共接口.md#ga70979f50f9c83e5aebab3d6a1bd4cf35) 表示 **输入输出错误（Input/Output Error）**；`return_val` 为返回值，`call_count` 字段为调用计数，`arg1_val` 字段保存第二个实参，即 LED 编号。

译注：这是使用模拟器件的测试片段，依赖测试工程内已有的 `fake_leds` 节点及框架环境。[`DEVICE_DT_GET`](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7) 宏取得设备指针，[`DT_NODELABEL`](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79) 宏按标签获取节点标识，[`zassert_equal`](P503_ZTest断言宏.md) 是相等断言宏。

```c
const struct device *dev = DEVICE_DT_GET(DT_NODELABEL(fake_leds));

fake_led_on_fake.return_val = -EIO;

zassert_equal(-EIO, led_on(dev, 2));
zassert_equal(1, fake_led_on_fake.call_count);
zassert_equal(2, fake_led_on_fake.arg1_val);
```



## 207.4\_七个模拟操作

以下保留原页未给出形参名称的声明形式：

```c
int fake_led_on(const struct device *, uint32_t);
int fake_led_off(const struct device *, uint32_t);
int fake_led_set_brightness(const struct device *, uint32_t, uint8_t);
int fake_led_blink(const struct device *, uint32_t, uint32_t, uint32_t);
int fake_led_get_info(const struct device *, uint32_t, const struct led_info **);
int fake_led_set_color(const struct device *, uint32_t, uint8_t, const uint8_t *);
int fake_led_write_channels(const struct device *, uint32_t, uint32_t,
                             const uint8_t *);
```

| 模拟函数 | 对应的驱动操作 |
| --- | --- |
| [`fake_led_on()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#gab6d86a816ed9dcd8d393126a8dc3d2dd) | [`led_driver_api::on`](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a9ce7322282f8c525256d3c16a514ecc4)，点亮。 |
| [`fake_led_off()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#ga4475c7869fd8ab92c5b7fea4ec3c1a3d) | [`led_driver_api::off`](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a19ad736a130da2aff6bd5b299d8c33a7)，关闭。 |
| [`fake_led_set_brightness()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#ga68b14d1f205726941cb591f177ef89af) | [`led_driver_api::set_brightness`](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a9c3e3c4d40c4b8219755df6df96b0058)，设置亮度。 |
| [`fake_led_blink()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#ga276f41b4376784bf588d7785afdffd56) | [`led_driver_api::blink`](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#af1974c5cc20c818e0e387b34cd14ac3b)，闪烁。 |
| [`fake_led_get_info()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#gae4f88da2cfa43c93bc0f2d294b6f848e) | [`led_driver_api::get_info`](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a7c68219e44bcf6e766e64fd3967ecf7e)，获取信息。 |
| [`fake_led_set_color()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#ga1860bf2d9d105ee8ecb7a092e2017b63) | [`led_driver_api::set_color`](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#a336f30f2c1bd3d99213cae66911c142a)，设置颜色。 |
| [`fake_led_write_channels()`](https://docs.zephyrproject.org/latest/doxygen/html/group__led__fake.html#gacf6109ac62eafca13ab6b56fb4676877) | [`led_driver_api::write_channels`](https://docs.zephyrproject.org/latest/doxygen/html/structled__driver__api.html#ada1dfb1830b48afb020c7e60dbd92337)，写入连续通道。 |

接口契约见[LED公共接口](P202_LED公共接口.md)，各驱动操作见[LED驱动函数表](P206_LED驱动函数表.md)。

[上一章：LED驱动函数表](P206_LED驱动函数表.md) · [下一章：LED灯带公共接口](P208_LED灯带公共接口.md) · [返回大纲](大纲.md)
