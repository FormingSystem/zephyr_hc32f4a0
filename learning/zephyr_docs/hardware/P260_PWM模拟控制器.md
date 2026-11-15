---
id: learning.zephyr-docs.hardware.pwmbackend-2
title: PWM模拟控制器
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__fake.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第260章\_PWM模拟控制器

原文：[group__pwm__fake](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__fake.html)。读取日期：2026-10-13，`latest`。

## 260.1\_用途与启用

本页提供用于测试的 **模拟脉宽调制（Fake Pulse Width Modulation，Fake PWM）**驱动，它用 **模拟函数框架（Fake Function Framework，FFF）**实现 PWM 接口。声明来自 `zephyr/drivers/pwm/pwm_fake.h`。

通过配置系统 Kconfig 的 [`CONFIG_PWM_FAKE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_FAKE) 启用，并从设备树（Devicetree）兼容属性为 `zephyr,fake-pwm` 的节点实例化。

## 260.2\_模拟控制与重置

每个模拟函数都配有一个名称追加 `_fake` 后缀的 FFF 控制结构，用于设置返回值、安装自定义模拟函数或检查调用次数和捕获的参数。原页没有列出这些控制结构，关联说明为[使用FFF进行模拟](https://docs.zephyrproject.org/latest/develop/test/ztest.html#mocking-via-fff)。

控制字段 `return_val` 设置仅返回状态的模拟函数之返回值；有输出参数时应使用自定义模拟字段 `custom_fake`，因为 `return_val` 不会修改输出参数。

启用测试框架配置项 [`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST) 时，一条 ztest 规则会在每个测试用例之前重置所有模拟函数。

## 260.3\_原测试示例

示例中的 [`DEVICE_DT_GET`](../device_reference/P001_设备模型公共接口.md#ga9a65996ce21f43acb7db061e23b48ec7) 是取得设备的宏，[`DT_NODELABEL`](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79) 是由节点标签取得标识的宏。断言宏 [`zassert_ok`](P503_ZTest断言宏.md) 检查成功返回值，[`zassert_equal`](P503_ZTest断言宏.md) 检查相等；`fake_pwm_set_cycles_fake` 为控制结构，`call_count` 为调用次数，`arg2_val`、`arg3_val` 分别保存从零编号的第2、3号参数，即周期与脉宽。

```c
const struct device *dev = DEVICE_DT_GET(DT_NODELABEL(fake_pwm));

zassert_ok(pwm_set_cycles(dev, 0, 1000, 500, 0));

zassert_equal(1, fake_pwm_set_cycles_fake.call_count);
zassert_equal(1000, fake_pwm_set_cycles_fake.arg2_val);
zassert_equal(500, fake_pwm_set_cycles_fake.arg3_val);
```

## 260.4\_模拟函数

函数 [`fake_pwm_set_cycles()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__fake.html#ga2dc0e23bd07cecf5ec38bf37b576ff57) 模拟[PWM驱动函数表](P259_PWM驱动函数表.md)的 `set_cycles` 操作，原声明未给参数名称：

```c
int fake_pwm_set_cycles(const struct device *, uint32_t, uint32_t, uint32_t,
                        pwm_flags_t);
```

参数语义对应[PWM公共接口](P255_PWM公共接口.md)的周期与脉宽设置函数。

---

[上一章：PWM驱动函数表](P259_PWM驱动函数表.md) · [下一章：PWM器件扩展目录](P261_PWM器件扩展目录.md) · [返回大纲](大纲.md)
