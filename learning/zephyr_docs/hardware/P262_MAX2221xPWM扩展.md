---
id: learning.zephyr-docs.hardware.pwmext-1
title: MAX2221xPWM扩展
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第262章\_MAX2221xPWM扩展

原文：[group__pwm__max2221x__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html)。读取日期：2026-10-13，官方 `latest` 文档版本。

## 262.1\_接口与斩波频率

本页为 MAX2221X 提供 **脉宽调制（Pulse Width Modulation，PWM）**专用接口，声明来自 `zephyr/drivers/pwm/max2221x.h`。

枚举 [`max2221x_master_chop_freq`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#ga8f702fe056959c707d495a5b49ec7647) 表示主斩波频率（Master Chop Frequency）：

| 枚举项 | 对应频率 |
| --- | --- |
| [`MAX2221X_FREQ_100KHZ`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647ab689b993d9fa98c5bf140162723d2feb)（枚举值为 `0`） | 100 kHz |
| [`MAX2221X_FREQ_80KHZ`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a1a478348731bd456313912f6b4a59f1f) | 80 kHz |
| [`MAX2221X_FREQ_60KHZ`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a93bf099ae22e26de9885c76bc8428eb8) | 60 kHz |
| [`MAX2221X_FREQ_50KHZ`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a1710af28d11faf44c423f2f771f02980) | 50 kHz |
| [`MAX2221X_FREQ_40KHZ`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a34a90a18c91e8e6f547c0788d4061612) | 40 kHz |
| [`MAX2221X_FREQ_30KHZ`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647ab4e2229b6516ea4f7278fa2931f262ed) | 30 kHz |
| [`MAX2221X_FREQ_25KHZ`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a8a11aacff6d925230f8719508b432cef) | 25 kHz |
| [`MAX2221X_FREQ_20KHZ`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a5cdbdb4c266cca9ae859f20dc0187a15) | 20 kHz |
| [`MAX2221X_FREQ_15KHZ`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647aa39e41621ac0f7f7073d95cfa18c99a4) | 15 kHz |
| [`MAX2221X_FREQ_10KHZ`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647abcaa72d42d74f8054480c73bf3fa61f5) | 10 kHz |
| [`MAX2221X_FREQ_7500HZ`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a208bff3bc2c214ea84404ba49c1037cb) | 7.5 kHz |
| [`MAX2221X_FREQ_5000HZ`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a0e56c34ed02843a63bbcfe0d219b2dbc) | 5 kHz |
| [`MAX2221X_FREQ_2500HZ`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a30dbf5e8aa5f7aa61cff6cf7391e39c9) | 2.5 kHz |
| [`MAX2221X_FREQ_INVALID`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga8f702fe056959c707d495a5b49ec7647a2bfeae761213ed84221a6bda013599aa) | 无效频率 |

枚举 [`max2221x_individual_chop_freq`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#ga41010c75c9cb6ed23e06cfec0ebbe413) 表示独立通道斩波频率（Individual Chop Frequency），通过主频分频取得：

| 枚举项 | 含义 |
| --- | --- |
| [`MAX2221X_FREQ_M`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413a4cee57aef5be5d79919513fea3891490)（枚举值为 `0`） | 不分频 |
| [`MAX2221X_FREQ_M_2`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413a120c21fdf16a48795233bae403a0c3f1) | 主频除以 2 |
| [`MAX2221X_FREQ_M_4`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413a84119a5bb314c03760637ebb05a7f16a) | 主频除以 4 |
| [`MAX2221X_FREQ_M_8`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413ac0955ebf50e1c3d7a51e6aa42e008cfd) | 主频除以 8 |
| [`MAX2221X_FREQ_M_INVALID`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gga41010c75c9cb6ed23e06cfec0ebbe413af6f9cae164f70b5fc9a7003e526d15b2) | 无效分频 |

> 译注：枚举编码与以 Hz 表示的频率不是同一个数值。

## 262.2\_计算占空比

函数 [`max2221x_calculate_duty_cycle()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gadc23c2818b49d4387b6641217603ca78) 计算占空比（Duty Cycle）：

```c
int max2221x_calculate_duty_cycle(uint32_t pulse, uint32_t period,
                                uint16_t *duty_cycle);
```

`pulse` 为给 PWM 设置的脉宽，`period` 为周期，两者均以微秒为单位，具体取值与硬件有关。`duty_cycle` 指向接收占空比的变量。成功返回 `0`，失败返回负错误码。

## 262.3\_计算主频分频系数

函数 [`max2221x_calculate_master_freq_divisor()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#ga21eb84d347badc0905f27c4d86621226) 计算用于获得独立通道频率的主频分频系数（Master Frequency Divisor）：

```c
int max2221x_calculate_master_freq_divisor(uint32_t master_freq,
                                         uint32_t period,
                                         int *freq_divisor);
```

`master_freq` 为设置给 PWM 的主频，单位为 Hz；`period` 为周期，单位为微秒。两者均与硬件有关。`freq_divisor` 接收每个通道设置的主频分频系数。成功返回 `0`，失败返回负错误码。

## 262.4\_读取独立通道频率

函数 [`max2221x_get_channel_freq()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#ga70b9870d016b7db7d616f3f393e4e427) 读取 MAX2221X 设备的独立通道频率：

```c
int max2221x_get_channel_freq(const struct device *dev, uint32_t channel,
                            uint32_t *channel_freq);
```

`dev` 指向驱动实例的设备结构，`channel` 为待读取的通道，`channel_freq` 指向保存通道频率的变量。原文返回值说明为：成功返回以 Hz 为单位的独立通道频率，失败返回负错误码。

> 译注：原页同时列出了输出指针与上述成功返回值说明，此处保留两者；不能仅凭其他函数的约定，将本函数的成功返回值改写成 `0`。

## 262.5\_读取每秒周期数

函数 [`max2221x_get_cycles_per_sec()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gabfc15fdf828ab5bcad2c4ef7f208e599) 读取 PWM 通道每秒的周期数（Cycles per Second）：

```c
int max2221x_get_cycles_per_sec(const struct device *dev, uint32_t channel,
                              uint64_t *cycles);
```

`dev` 指向驱动实例，`channel` 指定通道，`cycles` 指向保存周期数的变量。成功返回 `0`，失败返回负错误码。

## 262.6\_读取主斩波频率

函数 [`max2221x_get_master_chop_freq()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#gad283a38e9b32e9e721163feb2a7dc036) 读取 MAX2221X 主斩波频率：

```c
int max2221x_get_master_chop_freq(const struct device *dev);
```

`dev` 指向驱动实例的设备结构。成功返回以 Hz 为单位的主斩波频率，失败返回负错误码。

## 262.7\_设置通道占空比

函数 [`max2221x_set_cycles()`](https://docs.zephyrproject.org/latest/doxygen/html/group__pwm__max2221x__interface.html#ga8c202d4ecf8908c5f40124dddf7d40d6) 设置 PWM 通道占空比：

```c
int max2221x_set_cycles(const struct device *dev, uint32_t channel,
                       uint32_t period, uint32_t pulse, pwm_flags_t flags);
```

`dev` 指向驱动实例，`channel` 指定设置的通道；`period` 为周期，`pulse` 为脉宽，原页明确两者均以微秒为单位且与硬件有关。[`flags`](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9) 为引脚配置标志。成功返回 `0`，失败返回负错误码。

> 译注：这里沿用器件扩展页的微秒单位，不能仅依据函数名中的 `cycles`，就套用通用 PWM 接口以时钟周期计数的参数单位。

---

[上一章：PWM器件扩展目录](P261_PWM器件扩展目录.md) · [下一章：MAX31790PWM扩展](P263_MAX31790PWM扩展.md) · [返回大纲](大纲.md)
