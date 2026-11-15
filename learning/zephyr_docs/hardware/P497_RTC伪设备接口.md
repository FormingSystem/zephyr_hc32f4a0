---
id: learning.zephyr-docs.hardware.fakeapi-0
title: RTC伪设备接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__rtc__fake.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第497章\_RTC伪设备接口

原文：[group__rtc__fake](https://docs.zephyrproject.org/latest/doxygen/html/group__rtc__fake.html)。读取日期：2026-10-13，`latest`。

**实时时钟（Real-Time Clock，RTC）**伪驱动是 RTC 接口的**伪函数框架（Fake Function Framework，FFF）**实现，用于测试。启用 Kconfig 配置项 [`CONFIG_RTC_FAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_FAKE) 后，由 [`zephyr,fake-rtc` 设备树节点](https://docs.zephyrproject.org/latest/build/dts/api/bindings/rtc/zephyr%2Cfake-rtc.html#std-dtcompatible-zephyr-fake-rtc)实例化。全部接口位于 `zephyr/drivers/rtc/rtc_fake.h`。

## 497.1\_控制返回值与检查调用

每个伪函数（Fake）都有一个 FFF 控制结构，名称是函数名再加 `_fake` 后缀。测试通过它设置返回值、安装自定义伪函数、检查调用次数以及已捕获参数。本页不列出这些控制结构，使用方法见[通过 FFF 进行模拟（Mocking via FFF）](../testing/P002_Ztest测试框架.md)。

对于只报告状态的伪函数，可设置控制结构的 `return_val` 返回值字段。对于有输出参数的伪函数，必须用 `custom_fake` 自定义处理函数驱动它，因为 `return_val` **不会修改输出参数**。

启用 Kconfig 配置项 [`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST) 后，Zephyr 测试框架（Zephyr Testing Framework，ZTest）的规则会在每个测试用例之前重置全部伪函数。

下面的官方示例取得 `fake_rtc` 设备树节点的设备对象，将设置时间的返回值配置为无效参数错误 `-EINVAL`，再检查调用结果、次数和第一个参数。[`DEVICE_DT_GET`](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7) 与 [`DT_NODELABEL`](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79) 分别取得设备对象和节点标识；[`zassert_equal`](P503_ZTest断言宏.md) 是相等断言，`call_count` 是调用计数，`arg0_val` 是捕获的第一个实参；[`rtc_time`](../timer_reference/P011_实时时钟时间结构.md) 为 RTC 时间结构，[`rtc_set_time`](../timer_reference/P009_实时时钟公共接口.md) 为设置时间接口。

```c
const struct device *dev = DEVICE_DT_GET(DT_NODELABEL(fake_rtc));
struct rtc_time tm = {0};

rtc_fake_set_time_fake.return_val = -EINVAL;

zassert_equal(-EINVAL, rtc_set_time(dev, &tm));
zassert_equal(1, rtc_fake_set_time_fake.call_count);
zassert_equal(dev, rtc_fake_set_time_fake.arg0_val);
```

## 497.2\_设置与读取时间

以下每个函数都是 `rtc_driver_api` 中同名驱动操作的伪实现。原文的签名没有给形参命名，译文保持这一形式；`rtc_driver_api` 是 RTC 驱动的**应用程序编程接口（Application Programming Interface，API）**结构。

```c
int rtc_fake_set_time(const struct device *, const struct rtc_time *);
int rtc_fake_get_time(const struct device *, struct rtc_time *);
```

[`rtc_fake_set_time()`](P497_RTC伪设备接口.md) 对应 [`rtc_driver_api::set_time`](../timer_reference/P012_实时时钟驱动操作结构.md) 设置时间操作；[`rtc_fake_get_time()`](P497_RTC伪设备接口.md) 对应 [`rtc_driver_api::get_time`](../timer_reference/P012_实时时钟驱动操作结构.md) 读取时间操作。

## 497.3\_闹钟操作

**闹钟（Alarm）**接口仅在启用 Kconfig 配置项 [`CONFIG_RTC_ALARM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_ALARM) 时可用。下面五个函数逐一对应驱动的闹钟操作：

| 伪函数 | 对应驱动操作与用途 |
| --- | --- |
| [`rtc_fake_alarm_get_supported_fields()`](P497_RTC伪设备接口.md) | [`rtc_driver_api::alarm_get_supported_fields`](../timer_reference/P012_实时时钟驱动操作结构.md)：取得闹钟支持的字段 |
| [`rtc_fake_alarm_set_time()`](P497_RTC伪设备接口.md) | [`rtc_driver_api::alarm_set_time`](../timer_reference/P012_实时时钟驱动操作结构.md)：设置闹钟时间 |
| [`rtc_fake_alarm_get_time()`](P497_RTC伪设备接口.md) | [`rtc_driver_api::alarm_get_time`](../timer_reference/P012_实时时钟驱动操作结构.md)：读取闹钟时间 |
| [`rtc_fake_alarm_is_pending()`](P497_RTC伪设备接口.md) | [`rtc_driver_api::alarm_is_pending`](../timer_reference/P012_实时时钟驱动操作结构.md)：检查闹钟是否待处理 |
| [`rtc_fake_alarm_set_callback()`](P497_RTC伪设备接口.md) | [`rtc_driver_api::alarm_set_callback`](../timer_reference/P012_实时时钟驱动操作结构.md)：设置闹钟回调（Callback） |

完整签名如下，[`rtc_alarm_callback`](../timer_reference/P009_实时时钟公共接口.md) 为闹钟回调类型：

```c
int rtc_fake_alarm_get_supported_fields(const struct device *, uint16_t,
                                         uint16_t *);
int rtc_fake_alarm_set_time(const struct device *, uint16_t, uint16_t,
                             const struct rtc_time *);
int rtc_fake_alarm_get_time(const struct device *, uint16_t, uint16_t *,
                             struct rtc_time *);
int rtc_fake_alarm_is_pending(const struct device *, uint16_t);
int rtc_fake_alarm_set_callback(const struct device *, uint16_t,
                                 rtc_alarm_callback, void *);
```

## 497.4\_更新通知与校准

[`rtc_fake_update_set_callback()`](P497_RTC伪设备接口.md) 是 [`rtc_driver_api::update_set_callback`](../timer_reference/P012_实时时钟驱动操作结构.md) 更新回调设置操作的伪实现，**仅在启用 Kconfig 配置项 [`CONFIG_RTC_UPDATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_UPDATE) 时可用**。[`rtc_update_callback`](../timer_reference/P009_实时时钟公共接口.md) 是更新通知回调类型。

```c
int rtc_fake_update_set_callback(const struct device *, rtc_update_callback,
                                  void *);
```

以下两个**校准（Calibration）**接口仅在启用 Kconfig 配置项 [`CONFIG_RTC_CALIBRATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTC_CALIBRATION) 时可用：

```c
int rtc_fake_set_calibration(const struct device *, int32_t);
int rtc_fake_get_calibration(const struct device *, int32_t *);
```

[`rtc_fake_set_calibration()`](P497_RTC伪设备接口.md) 对应 [`rtc_driver_api::set_calibration`](../timer_reference/P012_实时时钟驱动操作结构.md) 设置校准操作；[`rtc_fake_get_calibration()`](P497_RTC伪设备接口.md) 对应 [`rtc_driver_api::get_calibration`](../timer_reference/P012_实时时钟驱动操作结构.md) 读取校准操作。

---

[上一章：通用传感器仿真接口](P496_通用传感器仿真接口.md) · [下一章：稳压器伪设备接口](P498_稳压器伪设备接口.md) · [返回大纲](大纲.md)
