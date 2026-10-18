---
id: learning.zephyr-docs.kconfig-reference.page-50
title: "`drivers/audio`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第50章\_`drivers/audio`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/audio` 的 57 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_AUDIO"></a>

## 50.1 `CONFIG_AUDIO`

**提示（Prompt）**：音频驱动（Audio Drivers）

**说明（Help）**

启用音频（Audio）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`drivers/audio/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_AUDIO_CODEC"></a>

## 50.2 `CONFIG_AUDIO_CODEC`

**提示（Prompt）**：音频编解码器驱动（Audio Codec Drivers）

**说明（Help）**

启用音频编解码器（Audio Codec）驱动配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO
```

**定义位置（Location）**：[`drivers/audio/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_AUDIO_CODEC_AW88298"></a>

## 50.3 `CONFIG_AUDIO_CODEC_AW88298`

**提示（Prompt）**：艾为 AW88298 数字智能放大器（Awinic Digital Smart Amplifier）

**说明（Help）**

启用艾为（Awinic）AW88298 数字智能放大器（Digital Smart Amplifier）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AWINIC_AW88298_ENABLED && CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/audio/Kconfig.aw88298:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.aw88298#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_AUDIO_CODEC_CS35L5X"></a>

## 50.4 `CONFIG_AUDIO_CODEC_CS35L5X`

**提示（Prompt）**：Cirrus Logic CS35L5X 编解码器支持（Codec Support）

**说明（Help）**

启用 CS35L5X 智能放大器（Smart Amplifier）系列的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_CIRRUS_CS35L56_ENABLED || DT_HAS_CIRRUS_CS35L57_ENABLED) && CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/audio/Kconfig.cs35l5x:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.cs35l5x#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_AUDIO_CODEC_CS35L5X_INIT_PRIORITY"></a>

## 50.5 `CONFIG_AUDIO_CODEC_CS35L5X_INIT_PRIORITY`

**提示（Prompt）**：CS35L5X 音频编解码器初始化优先级（Audio Codec Init Priority）

**说明（Help）**

CS35L5X 音频编解码器（Audio Codec）驱动的初始化优先级。其数值必须大于所绑定稳压器（Regulator）的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_CODEC_CS35L5X && CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
60
```

**定义位置（Location）**：[`drivers/audio/Kconfig.cs35l5x:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.cs35l5x#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers） → Cirrus Logic CS35L5X 编解码器支持（Codec Support）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC_CS35L5X`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC_CS35L5X)、[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_AUDIO_CODEC_CS43L22"></a>

## 50.6 `CONFIG_AUDIO_CODEC_CS43L22`

**提示（Prompt）**：Cirrus CS43L22 驱动（Driver）

**说明（Help）**

启用 Cirrus CS43L22 驱动。该器件是低功耗立体声数模转换器（Stereo DAC），带有耳机和扬声器放大器（Headphone and Speaker Amplifiers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_CIRRUS_CS43L22_ENABLED && CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
CONFIG_GPIO
```

**定义位置（Location）**：[`drivers/audio/Kconfig.cs43l22:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.cs43l22#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)。

<a id="CONFIG_AUDIO_CODEC_DA7212"></a>

## 50.7 `CONFIG_AUDIO_CODEC_DA7212`

**提示（Prompt）**：Dialog DA7212 编解码器支持（Codec Support）

**说明（Help）**

启用 Dialog DA7212 音频编解码器（Audio Codec）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_DLG_DA7212_ENABLED && CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/audio/Kconfig.da7212:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.da7212#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_AUDIO_CODEC_DUMMY"></a>

## 50.8 `CONFIG_AUDIO_CODEC_DUMMY`

**提示（Prompt）**：虚拟音频编解码器驱动（Dummy Audio Codec Driver）

**说明（Help）**

启用无需实际硬件即可用于测试和开发的虚拟音频编解码器（Dummy Audio Codec）驱动。该驱动实现必要接口，但不执行任何实际音频处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_DUMMY_CODEC_ENABLED && CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/audio/Kconfig.codec_dummy:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.codec_dummy#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_AUDIO_CODEC_INIT_PRIORITY"></a>

## 50.9 `CONFIG_AUDIO_CODEC_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

音频编解码器（Audio Codec）设备驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
60
```

**定义位置（Location）**：[`drivers/audio/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_AUDIO_CODEC_MAX98091"></a>

## 50.10 `CONFIG_AUDIO_CODEC_MAX98091`

**提示（Prompt）**：美信 MAX98091 编解码器支持（Maxim Codec Support）

**说明（Help）**

通过 I2C 启用 MAX98091 I2S 编解码器（Codec）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_MAXIM_MAX98091_ENABLED && CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/audio/Kconfig.max98091:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.max98091#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_AUDIO_CODEC_PCM1681"></a>

## 50.11 `CONFIG_AUDIO_CODEC_PCM1681`

**提示（Prompt）**：PCM1681(-Q1) 数模转换器支持（DAC Support）

**说明（Help）**

启用 PCM1681 或 PCM1681-Q1 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_PCM1681_ENABLED && CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C if CONFIG_AUDIO_CODEC_PCM1681_I2C
CONFIG_SPI if CONFIG_AUDIO_CODEC_PCM1681_SPI
```

**定义位置（Location）**：[`drivers/audio/Kconfig.pcm1681:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.pcm1681#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)、[`CONFIG_AUDIO_CODEC_PCM1681_I2C`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC_PCM1681_I2C)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_AUDIO_CODEC_PCM1681_SPI`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC_PCM1681_SPI)。

<a id="CONFIG_AUDIO_CODEC_PCM1681_I2C"></a>

## 50.12 `CONFIG_AUDIO_CODEC_PCM1681_I2C`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

pcm1681xx 驱动的 I2C 版本（I2C Driver Version）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/audio/Kconfig.pcm1681:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.pcm1681#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

<a id="CONFIG_AUDIO_CODEC_PCM1681_SPI"></a>

## 50.13 `CONFIG_AUDIO_CODEC_PCM1681_SPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

pcm1681xx 驱动的 SPI 版本（SPI Driver Version）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/audio/Kconfig.pcm1681:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.pcm1681#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

<a id="CONFIG_AUDIO_CODEC_SF32LB"></a>

## 50.14 `CONFIG_AUDIO_CODEC_SF32LB`

**提示（Prompt）**：sf32lb 音频编解码器（Audio Codec）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SIFLI_SF32LB_AUDCODEC_ENABLED && CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/audio/Kconfig.sf32lb:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.sf32lb#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA)。

<a id="CONFIG_AUDIO_CODEC_SHELL"></a>

## 50.15 `CONFIG_AUDIO_CODEC_SHELL`

**提示（Prompt）**：音频编解码器命令行（Audio Codec Shell）

**说明（Help）**

启用音频编解码器命令行（Audio Codec Shell），提供音频编解码器相关命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**定义位置（Location）**：[`drivers/audio/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_AUDIO_CODEC_TLV320AIC26"></a>

## 50.16 `CONFIG_AUDIO_CODEC_TLV320AIC26`

**提示（Prompt）**：TLV320AIC26 音频编解码器（Audio Codec）

**说明（Help）**

启用 TI TLV320AIC26 低功耗立体声音频编解码器（Stereo Audio Codec）驱动。通过 SPI 控制寄存器，通过 I2S 传输音频数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TLV320AIC26_ENABLED && CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/audio/Kconfig.tlv320aic26:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.tlv320aic26#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_AUDIO_CODEC_WM8904"></a>

## 50.17 `CONFIG_AUDIO_CODEC_WM8904`

**提示（Prompt）**：Wolfson WM8904 编解码器支持（Codec Support）

**说明（Help）**

启用 Wolfson WM8904 编解码器（Codec）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WOLFSON_WM8904_ENABLED && CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/audio/Kconfig.wm8904:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.wm8904#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_AUDIO_CODEC_WM8960"></a>

## 50.18 `CONFIG_AUDIO_CODEC_WM8960`

**提示（Prompt）**：Wolfson WM8960 音频编解码器（Audio Codec）

**说明（Help）**

启用 Wolfson WM8960 音频编解码器（Audio Codec）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WOLFSON_WM8960_ENABLED && CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/audio/Kconfig.wm8960:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.wm8960#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_AUDIO_CODEC_WM8962"></a>

## 50.19 `CONFIG_AUDIO_CODEC_WM8962`

**提示（Prompt）**：Wolfson WM8962 编解码器支持（Codec Support）

**说明（Help）**

启用 Wolfson WM8962 编解码器（Codec）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_WOLFSON_WM8962_ENABLED && CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/audio/Kconfig.wm8962:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.wm8962#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_AUDIO_DMIC"></a>

## 50.20 `CONFIG_AUDIO_DMIC`

**提示（Prompt）**：数字麦克风音频驱动（Digital Microphone Audio Drivers）

**说明（Help）**

启用数字麦克风（Digital Microphone）驱动配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO
```

**定义位置（Location）**：[`drivers/audio/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_AUDIO_DMIC_AMBIQ_PDM"></a>

## 50.21 `CONFIG_AUDIO_DMIC_AMBIQ_PDM`

**提示（Prompt）**：Ambiq 脉冲密度调制驱动（PDM Driver）

**说明（Help）**

启用适用于 Apollo 5 微控制器（MCU）的 Ambiq 脉冲密度调制（PDM）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_AMBIQ_PDM_ENABLED && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_AMBIQ_HAL
CONFIG_AMBIQ_HAL_USE_PDM
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_ambiq_pdm:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_ambiq_pdm#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_AMBIQ_HAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL)、[`CONFIG_AMBIQ_HAL_USE_PDM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_AMBIQ_HAL_USE_PDM)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_AUDIO_DMIC_INFINEON"></a>

## 50.22 `CONFIG_AUDIO_DMIC_INFINEON`

**提示（Prompt）**：英飞凌数字麦克风驱动（Infineon DMIC Driver）

**说明（Help）**

启用英飞凌（Infineon）数字麦克风（DMIC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_PDM_ENABLED && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_INFINEON_PDM_PCM
CONFIG_PINCTRL
CONFIG_DMA
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_infineon:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_infineon#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_USE_INFINEON_PDM_PCM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_INFINEON_PDM_PCM)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)、[`CONFIG_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA)。

<a id="CONFIG_AUDIO_DMIC_INIT_PRIORITY"></a>

## 50.23 `CONFIG_AUDIO_DMIC_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Init Priority）

**说明（Help）**

音频数字麦克风（Audio Digital Microphone）设备驱动的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/audio/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_AUDIO_DMIC_MCUX"></a>

## 50.24 `CONFIG_AUDIO_DMIC_MCUX`

**提示（Prompt）**：MCUX 数字麦克风驱动（DMIC Driver）

**说明（Help）**

启用恩智浦（NXP）MCUX 片上系统（SoC）的数字麦克风（DMIC）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_DMIC_ENABLED && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DMA
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_mcux:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_mcux#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_DMA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_AUDIO_DMIC_MPXXDTYY"></a>

## 50.25 `CONFIG_AUDIO_DMIC_MPXXDTYY`

**提示（Prompt）**：连接到 I2S 的 ST 数字 PDM 麦克风支持（Digital PDM Microphone Support）

**说明（Help）**

在所选开发板上启用 MPXXDTYY 麦克风（Microphone）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_MPXXDTYY_ENABLED && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2S
CONFIG_HAS_STLIB
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_mpxxdtyy:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_mpxxdtyy#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_I2S`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2S)、[`CONFIG_HAS_STLIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STLIB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STLIB`。

<a id="CONFIG_AUDIO_DMIC_NATIVE_SIM"></a>

## 50.26 `CONFIG_AUDIO_DMIC_NATIVE_SIM`

**提示（Prompt）**：原生模拟器数字麦克风驱动（Native Simulator DMIC Driver）

**说明（Help）**

启用原生模拟器（Native Simulator）的数字麦克风（DMIC）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_NATIVE_SIM_DMIC_ENABLED && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NATIVE_USE_NSI_ERRNO
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_native_sim:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_native_sim#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_NATIVE_USE_NSI_ERRNO`](P033_arch_posix_配置项参考.md#CONFIG_NATIVE_USE_NSI_ERRNO)。

<a id="CONFIG_AUDIO_DMIC_NATIVE_SIM_FILE_PATH"></a>

## 50.27 `CONFIG_AUDIO_DMIC_NATIVE_SIM_FILE_PATH`

**提示（Prompt）**：输入 PCM 文件路径（Input PCM File Path）

**说明（Help）**

用作脉冲编码调制（PCM）采集源的主机文件路径（Host File Path）。可以是绝对路径，也可以是相对于当前工作目录的路径。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_DMIC_NATIVE_SIM && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
"dmic_in.pcm"
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_native_sim:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_native_sim#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → 原生模拟器数字麦克风驱动（Native Simulator DMIC Driver）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_NATIVE_SIM`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_NATIVE_SIM)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_AUDIO_DMIC_NATIVE_SIM_QUEUE_SIZE"></a>

## 50.28 `CONFIG_AUDIO_DMIC_NATIVE_SIM_QUEUE_SIZE`

**提示（Prompt）**：接收队列长度（Receive Queue Length）

**说明（Help）**

可以排队等待应用读取的采集块（Capture Block）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_DMIC_NATIVE_SIM && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_native_sim:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_native_sim#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → 原生模拟器数字麦克风驱动（Native Simulator DMIC Driver）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_NATIVE_SIM`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_NATIVE_SIM)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_AUDIO_DMIC_NATIVE_SIM_THREAD_PRIORITY"></a>

## 50.29 `CONFIG_AUDIO_DMIC_NATIVE_SIM_THREAD_PRIORITY`

**提示（Prompt）**：工作线程优先级（Worker Thread Priority）

**说明（Help）**

原生模拟器（Native Simulator）的数字麦克风（DMIC）工作线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_DMIC_NATIVE_SIM && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_native_sim:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_native_sim#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → 原生模拟器数字麦克风驱动（Native Simulator DMIC Driver）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_NATIVE_SIM`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_NATIVE_SIM)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_AUDIO_DMIC_NRFX_PDM"></a>

## 50.30 `CONFIG_AUDIO_DMIC_NRFX_PDM`

**提示（Prompt）**：nRF PDM nrfx 驱动（Driver）

**说明（Help）**

启用面向 nRF 微控制器（MCU）系列的 nrfx 脉冲密度调制（PDM）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_PDM_ENABLED && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_PDM
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_pdm_nrfx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_pdm_nrfx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_NRFX_PDM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_PDM)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_AUDIO_DMIC_NXP_MICFIL"></a>

## 50.31 `CONFIG_AUDIO_DMIC_NXP_MICFIL`

**提示（Prompt）**：恩智浦 MICFIL 驱动（NXP Driver）

**说明（Help）**

启用恩智浦（NXP）MICFIL 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MICFIL_ENABLED && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CLOCK_CONTROL
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_nxp_micfil:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_nxp_micfil#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_CLOCK_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_AUDIO_DMIC_RENESAS_RA_PDM"></a>

## 50.32 `CONFIG_AUDIO_DMIC_RENESAS_RA_PDM`

**提示（Prompt）**：瑞萨 RA PDM-IF 数字麦克风驱动（Renesas Digital Microphone Driver）

**说明（Help）**

启用瑞萨（Renesas）RA 脉冲密度调制接口（Pulse Density Modulation Interface）的数字麦克风驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_PDM_ENABLED && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_PDM
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_renesas_ra_pdm:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_renesas_ra_pdm#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_USE_RA_FSP_PDM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_PDM)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_AUDIO_DMIC_RENESAS_RA_PDM_BLOCK_COUNT"></a>

## 50.33 `CONFIG_AUDIO_DMIC_RENESAS_RA_PDM_BLOCK_COUNT`

**提示（Prompt）**：排队等待应用读取的采集块数量（Queued Capture Blocks）

**说明（Help）**

保存已转换数据块、等待 `dmic_read()` 读取的队列深度（Queue Depth）。队列满后会丢弃数据块，因此容量必须覆盖读取方可能无法执行读取的最长时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_DMIC_RENESAS_RA_PDM && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[2, 32]
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_renesas_ra_pdm:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_renesas_ra_pdm#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → 瑞萨 RA PDM-IF 数字麦克风驱动（Renesas Digital Microphone Driver）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_RENESAS_RA_PDM`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_RENESAS_RA_PDM)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_AUDIO_DMIC_RENESAS_RA_PDM_BLOCK_SAMPLES"></a>

## 50.34 `CONFIG_AUDIO_DMIC_RENESAS_RA_PDM_BLOCK_SAMPLES`

**提示（Prompt）**：最大采集块大小，单位为样本（Largest Capture Block）

**说明（Help）**

`dmic_configure()` 可以请求的最长数据块大小，单位为样本（Sample）。每个通道保留两个这样大小的数据块，每个样本 4 字节，以便在转换已完成的数据块时，由接口填充另一个数据块。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_DMIC_RENESAS_RA_PDM && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
512
```

**取值范围（Ranges）**

```text
[8, 4096]
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_renesas_ra_pdm:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_renesas_ra_pdm#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → 瑞萨 RA PDM-IF 数字麦克风驱动（Renesas Digital Microphone Driver）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_RENESAS_RA_PDM`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_RENESAS_RA_PDM)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_AUDIO_DMIC_SHELL"></a>

## 50.35 `CONFIG_AUDIO_DMIC_SHELL`

**提示（Prompt）**：音频数字麦克风命令行（Audio DMIC Shell）

**说明（Help）**

启用命令行（Shell）命令，用于从数字麦克风设备读取音频数据、显示实时音量单位表（VU Meter），以及将采集的脉冲编码调制（PCM）数据转储为 Base64。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**主动选择（Selects）**

```text
CONFIG_SHELL_VT100_COMMANDS
CONFIG_BASE64
```

**定义位置（Location）**：[`drivers/audio/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_SHELL_VT100_COMMANDS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_VT100_COMMANDS)、[`CONFIG_BASE64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BASE64)。

<a id="CONFIG_AUDIO_DMIC_SHELL_BLOCK_COUNT"></a>

## 50.36 `CONFIG_AUDIO_DMIC_SHELL_BLOCK_COUNT`

**提示（Prompt）**：采集缓冲区数量（Number of Capture Buffers）

**说明（Help）**

采集池（Capture Pool）中的缓冲区数量。至少需要两个，以便填充一个缓冲区时处理另一个。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_DMIC_SHELL && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[2, 16]
```

**定义位置（Location）**：[`drivers/audio/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → 音频数字麦克风命令行（Audio DMIC Shell）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_SHELL`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_SHELL)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_AUDIO_DMIC_SHELL_VU_CLIP_HOLD_MS"></a>

## 50.37 `CONFIG_AUDIO_DMIC_SHELL_VU_CLIP_HOLD_MS`

**提示（Prompt）**：电平表削波指示保持时间，单位为毫秒（Clip Indicator Hold Time）

**说明（Help）**

出现最近一次削波样本（Clipped Sample）后，`dmic vu` 电平表（Level Meter）保持红色削波指示符 `!` 亮起的时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_DMIC_SHELL && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
2000
```

**定义位置（Location）**：[`drivers/audio/Kconfig:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → 音频数字麦克风命令行（Audio DMIC Shell）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_SHELL`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_SHELL)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_AUDIO_DMIC_SHELL_VU_PEAK_HOLD_MS"></a>

## 50.38 `CONFIG_AUDIO_DMIC_SHELL_VU_PEAK_HOLD_MS`

**提示（Prompt）**：电平表峰值保持时间，单位为毫秒（Peak-Hold Time）

**说明（Help）**

出现新峰值后，`dmic vu` 电平表（Level Meter）的峰值保持标记 `|` 保持不变的时间；之后该标记才开始向底部衰减。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_DMIC_SHELL && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`drivers/audio/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → 音频数字麦克风命令行（Audio DMIC Shell）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_SHELL`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_SHELL)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_AUDIO_DMIC_SHELL_VU_STACK_SIZE"></a>

## 50.39 `CONFIG_AUDIO_DMIC_SHELL_VU_STACK_SIZE`

**提示（Prompt）**：电平表工作线程栈大小，单位为字节（Worker Thread Stack Size）

**说明（Help）**

运行 `dmic vu` 电平表（Level Meter）的后台工作线程（Background Worker Thread）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_DMIC_SHELL && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/audio/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → 音频数字麦克风命令行（Audio DMIC Shell）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_SHELL`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_SHELL)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_AUDIO_DMIC_STM32_DFSDM"></a>

## 50.40 `CONFIG_AUDIO_DMIC_STM32_DFSDM`

**提示（Prompt）**：STM32 DFSDM 数字麦克风驱动（DMIC Driver）

**说明（Help）**

启用 STM32 数字麦克风（DMIC）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_DFSDM_ENABLED && DT_HAS_ST_STM32_DFSDM_DMIC_ENABLED && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_DFSDM
CONFIG_RESET
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_stm32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_stm32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_USE_STM32_HAL_DFSDM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_DFSDM)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_AUDIO_DMIC_STM32_MDF"></a>

## 50.41 `CONFIG_AUDIO_DMIC_STM32_MDF`

**提示（Prompt）**：STM32 MDF 数字麦克风驱动（DMIC Driver）

**说明（Help）**

启用 STM32 数字麦克风（DMIC）驱动支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_MDF_ENABLED && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_MDF
CONFIG_RESET
CONFIG_PINCTRL
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_stm32:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_stm32#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_USE_STM32_HAL_MDF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_MDF)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)、[`CONFIG_PINCTRL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PINCTRL)。

<a id="CONFIG_AUDIO_DMIC_STM32_QUEUE_SIZE"></a>

## 50.42 `CONFIG_AUDIO_DMIC_STM32_QUEUE_SIZE`

**提示（Prompt）**：DMIC 消息队列大小（Message Queue Size）

**说明（Help）**

可以排队的待处理音频缓冲区消息（Audio Buffer Message）数量。更大的值意味着更多缓冲和音频数据，也需要更多 RAM；更小的值可以减少内存占用和延迟，但可能增加溢出（Overrun）。此选项由所有 STM32 数字麦克风（DMIC）驱动共用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_AUDIO_DMIC_STM32_DFSDM || CONFIG_AUDIO_DMIC_STM32_MDF) && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_stm32:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_stm32#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_STM32_DFSDM`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_STM32_DFSDM)、[`CONFIG_AUDIO_DMIC_STM32_MDF`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_STM32_MDF)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_AUDIO_TAS2563"></a>

## 50.43 `CONFIG_AUDIO_TAS2563`

**提示（Prompt）**：TAS2563 音频放大器支持（Audio Amplifier Support）

**说明（Help）**

启用 TAS2563 音频编解码器（Audio Codec）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TAS2563_ENABLED && CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/audio/Kconfig.tas2563:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.tas2563#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_AUDIO_TAS6422DAC"></a>

## 50.44 `CONFIG_AUDIO_TAS6422DAC`

**提示（Prompt）**：TAS6422 音频放大器支持（Audio Amplifier Support）

**说明（Help）**

在所选开发板上启用 TAS6422 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TAS6422DAC_ENABLED && CONFIG_GPIO && CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/audio/Kconfig.tas6422dac:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.tas6422dac#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)、[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_AUDIO_TLV320AIC3110"></a>

## 50.45 `CONFIG_AUDIO_TLV320AIC3110`

**提示（Prompt）**：TLV320AIC3110 音频集成电路支持（AIC Support）

**说明（Help）**

在所选开发板上启用 TLV320AIC3110 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TLV320AIC3110_ENABLED && CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/audio/Kconfig.tlv320aic3110:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.tlv320aic3110#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_AUDIO_TLV320DAC"></a>

## 50.46 `CONFIG_AUDIO_TLV320DAC`

**提示（Prompt）**：TLV320DAC310x 数模转换器支持（DAC Support）

**说明（Help）**

在所选开发板上启用 TLV320DAC 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_TLV320DAC_ENABLED && CONFIG_GPIO && CONFIG_AUDIO_CODEC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_I2C
```

**定义位置（Location）**：[`drivers/audio/Kconfig.tlv320dac:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.tlv320dac#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 音频编解码器驱动（Audio Codec Drivers）

**配置项引用（Symbol References）**：[`CONFIG_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO)、[`CONFIG_AUDIO_CODEC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_CODEC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_I2C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C)。

<a id="CONFIG_DMIC_INFINEON_QUEUE_SIZE"></a>

## 50.47 `CONFIG_DMIC_INFINEON_QUEUE_SIZE`

**提示（Prompt）**：接收队列长度（Receive Queue Length）

**说明（Help）**

设置为接收软件队列（RX Software Queue）分配的元素数量。应与用于保存接收到的脉冲编码调制（PCM）样本的内存块池（Memory Slab）中的块数量一致。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_DMIC_INFINEON && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_infineon:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_infineon#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → 英飞凌数字麦克风驱动（Infineon DMIC Driver）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_INFINEON`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_INFINEON)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_DMIC_MCUX_DMA_BUFFERS"></a>

## 50.48 `CONFIG_DMIC_MCUX_DMA_BUFFERS`

**提示（Prompt）**：为 DMIC DMA 预留的缓冲区数量（Reserved Buffers）

**说明（Help）**

决定驱动应为直接内存访问（DMA）引擎分配并预留多少个缓冲区。数字麦克风（DMIC）API 使用的内存块池（Memory Slab）至少应比此值多提供一个缓冲区，因为接收队列（RX Queue）中始终会有一个缓冲区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_DMIC_MCUX && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[2, 16]
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_mcux:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_mcux#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → MCUX 数字麦克风驱动（DMIC Driver）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_MCUX`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_MCUX)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_DMIC_MCUX_QUEUE_SIZE"></a>

## 50.49 `CONFIG_DMIC_MCUX_QUEUE_SIZE`

**提示（Prompt）**：DMIC 缓冲区队列大小（Buffer Queue Size）

**说明（Help）**

设置数字麦克风（DMIC）的接收缓冲区队列（RX Buffer Queue）大小。触发 DMIC 后，最多可以排队此数量的缓冲区；达到该数量后，应用必须读取缓冲区，以免数据被丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_DMIC_MCUX && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_mcux:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_mcux#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → MCUX 数字麦克风驱动（DMIC Driver）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_MCUX`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_MCUX)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_DMIC_NXP_MICFIL_QUEUE_SIZE"></a>

## 50.50 `CONFIG_DMIC_NXP_MICFIL_QUEUE_SIZE`

**提示（Prompt）**：消息队列深度（Message Queue Depth）

**说明（Help）**

用于向应用传递已填满缓冲区的消息队列（Message Queue）深度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_DMIC_NXP_MICFIL && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_nxp_micfil:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_nxp_micfil#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → 恩智浦 MICFIL 驱动（NXP Driver）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_NXP_MICFIL`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_NXP_MICFIL)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_DMIC_STM32_DFSDM_MAX_SAMPLES"></a>

## 50.51 `CONFIG_DMIC_STM32_DFSDM_MAX_SAMPLES`

**提示（Prompt）**：每个 DMIC 块的最大样本数（Maximum Samples per Block）

**说明（Help）**

定义用于连续音频传输（Continuous Audio Transfers）的内部静态 DMA 缓冲区大小。驱动为每个活动滤波器（Active Filter）分配两个这样的数据块，即乒／乓缓冲（Ping / Pong）。更大的值允许 `k_mem_slab` 使用更大的块，但会消耗更多 RAM。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_DMIC_STM32_DFSDM && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_stm32:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_stm32#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → STM32 DFSDM 数字麦克风驱动（DMIC Driver）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_STM32_DFSDM`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_STM32_DFSDM)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_DMIC_STM32_MDF_DELAY"></a>

## 50.52 `CONFIG_DMIC_STM32_MDF_DELAY`

**提示（Prompt）**：DMIC 延迟（Delay）

**说明（Help）**

对数据源施加的延迟（Delay），以样本数计。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_DMIC_STM32_MDF && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_stm32:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_stm32#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → STM32 MDF 数字麦克风驱动（DMIC Driver）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_STM32_MDF`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_STM32_MDF)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_DMIC_STM32_MDF_DISCARD_SAMPLES"></a>

## 50.53 `CONFIG_DMIC_STM32_MDF_DISCARD_SAMPLES`

**提示（Prompt）**：DMIC 丢弃样本数（Discarded Samples）

**说明（Help）**

每次重新启动滤波器（Filter）时丢弃的样本数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_DMIC_STM32_MDF && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_stm32:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_stm32#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → STM32 MDF 数字麦克风驱动（DMIC Driver）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_STM32_MDF`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_STM32_MDF)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_HEAP_MEM_POOL_ADD_SIZE_AUDIO_DMIC_SHELL"></a>

## 50.54 `CONFIG_HEAP_MEM_POOL_ADD_SIZE_AUDIO_DMIC_SHELL`

**提示（Prompt）**：为音频 DMIC 命令行预留的系统堆，单位为字节（Reserved System Heap）

**说明（Help）**

为命令行采集缓冲区（Shell Capture Buffers）预留的堆内存（Heap）。采样率、通道数或 PCM 位宽更高时，应增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_DMIC_SHELL && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
8192
```

**定义位置（Location）**：[`drivers/audio/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → 音频数字麦克风命令行（Audio DMIC Shell）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_SHELL`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_SHELL)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<a id="CONFIG_INTEL_ADSP_MIC_PRIVACY"></a>

## 50.55 `CONFIG_INTEL_ADSP_MIC_PRIVACY`

**提示（Prompt）**：麦克风隐私设备驱动支持（MIC PRIVACY Device Driver Support）

**说明（Help）**

启用麦克风隐私（MIC PRIVACY）设备驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INTEL_ADSP_MIC_PRIVACY_ENABLED
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/audio/mic_privacy/intel/Kconfig.mic_privacy:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/mic_privacy/intel/Kconfig.mic_privacy#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

<a id="CONFIG_PDM_AMBIQ_BUFFER_ALIGNMENT"></a>

## 50.56 `CONFIG_PDM_AMBIQ_BUFFER_ALIGNMENT`

**提示（Prompt）**：设置 PDM DMA TCB 缓冲区对齐（Buffer Alignment）

**说明（Help）**

脉冲密度调制（PDM）缓冲区放置在可缓存区域（Cacheable Region）时，应按 32 字节对齐。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_AUDIO_DMIC_AMBIQ_PDM && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
CONFIG_DCACHE_LINE_SIZE if CONFIG_DCACHE
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_ambiq_pdm:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_ambiq_pdm#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → Ambiq 脉冲密度调制驱动（PDM Driver）

**配置项引用（Symbol References）**：[`CONFIG_AUDIO_DMIC_AMBIQ_PDM`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_AMBIQ_PDM)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)、[`CONFIG_DCACHE_LINE_SIZE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE_LINE_SIZE)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)。

<a id="CONFIG_PDM_AMBIQ_HANDLE_CACHE"></a>

## 50.57 `CONFIG_PDM_AMBIQ_HANDLE_CACHE`

**提示（Prompt）**：在 PDM 驱动中启用缓存处理（Cache Handling）

**说明（Help）**

如果上层已处理缓存（Cache），则禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CACHE_MANAGEMENT && CONFIG_DCACHE && CONFIG_AUDIO_DMIC_AMBIQ_PDM && CONFIG_AUDIO_DMIC && CONFIG_AUDIO
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/audio/Kconfig.dmic_ambiq_pdm:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/audio/Kconfig.dmic_ambiq_pdm#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 音频驱动（Audio Drivers） → 数字麦克风音频驱动（Digital Microphone Audio Drivers） → Ambiq 脉冲密度调制驱动（PDM Driver）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_AUDIO_DMIC_AMBIQ_PDM`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC_AMBIQ_PDM)、[`CONFIG_AUDIO_DMIC`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO_DMIC)、[`CONFIG_AUDIO`](P050_drivers_audio_配置项参考.md#CONFIG_AUDIO)。

<!-- kconfig-navigation -->

[上一章](P049_drivers_adc_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P051_drivers_auxdisplay_配置项参考.md)
