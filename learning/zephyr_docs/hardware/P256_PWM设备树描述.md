---
id: learning.zephyr-docs.hardware.pwmapi-1
title: PWM设备树描述
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpwm__dt__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第256章\_PWM设备树描述

原文：[structpwm__dt__spec](https://docs.zephyrproject.org/latest/doxygen/html/structpwm__dt__spec.html)。读取日期：2026-10-13，`latest`。

## 256.1\_用途

结构 [`pwm_dt_spec`](https://docs.zephyrproject.org/latest/doxygen/html/structpwm__dt__spec.html) 保存 **设备树（Devicetree，DT）**指定的 **脉宽调制（Pulse Width Modulation，PWM）**信息，定义来自 `zephyr/drivers/pwm.h`。

该类型包含设备指针、由该设备控制的通道号、纳秒周期，以及适用于该通道的标志。并非所有驱动都支持标志；不支持时 [`flags`](https://docs.zephyrproject.org/latest/doxygen/html/structpwm__dt__spec.html#a2ddb45cbde80314a5a50dffe2e43921b) 为 0。

## 256.2\_数据字段（Data Fields）

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| <a id="ad9f2991bcf978940e638d17c5e17311e"></a>[`dev`](https://docs.zephyrproject.org/latest/doxygen/html/structpwm__dt__spec.html#ad9f2991bcf978940e638d17c5e17311e) | `const struct device *` | PWM 设备实例。 |
| <a id="a739a2672afa1d56ec1d865d6d5be47b2"></a>[`channel`](https://docs.zephyrproject.org/latest/doxygen/html/structpwm__dt__spec.html#a739a2672afa1d56ec1d865d6d5be47b2) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 通道号（Channel Number）。 |
| <a id="a935c72595e2248ab75ce0c43a394c0b3"></a>[`period`](https://docs.zephyrproject.org/latest/doxygen/html/structpwm__dt__spec.html#a935c72595e2248ab75ce0c43a394c0b3) | [`uint32_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f) | 周期（Period），单位纳秒（Nanosecond）。 |
| <a id="a2ddb45cbde80314a5a50dffe2e43921b"></a>`flags` | [`pwm_flags_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gae1dcfb878163da76041efcedf0960fa0) | 配置标志（Configuration Flags）。 |

## 256.3\_关联初始化宏

原页关联宏为 [`PWM_DT_SPEC_GET_BY_NAME`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga88b92c580860441c83d1b03db25fc4f1)、[`PWM_DT_SPEC_GET_BY_NAME_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga5557add2123a7138b64997cd070e0ee6)、[`PWM_DT_SPEC_GET_BY_IDX`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga7e8375bcf95ae6a9500ce3aba4586de4)、[`PWM_DT_SPEC_GET_BY_IDX_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#gaf5808fd88b101208681820b53bca33e1)、[`PWM_DT_SPEC_GET`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga59a79f0b77c5b71252bde126f333a84b) 和 [`PWM_DT_SPEC_GET_OR`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__interface.html#ga82f8efe8f0bc088fdda58c09dd4be4ff)；完整初始化行为与例子见[PWM公共接口](P255_PWM公共接口.md)。

---

[上一章：PWM公共接口](P255_PWM公共接口.md) · [下一章：PWM事件回调结构](P257_PWM事件回调结构.md) · [返回大纲](大纲.md)
