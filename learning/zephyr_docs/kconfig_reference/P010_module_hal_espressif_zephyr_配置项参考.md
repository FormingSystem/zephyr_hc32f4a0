---
id: learning.zephyr-docs.kconfig-reference.page-10
title: "`<module:hal_espressif>/zephyr`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第10章\_`<module:hal_espressif>/zephyr`配置项参考

本章翻译官方 Kconfig 数据库中 `<module:hal_espressif>/zephyr` 的 13 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ESP_SLEEP_CACHE_SAFE_ASSERTION"></a>

## 10.1 `CONFIG_ESP_SLEEP_CACHE_SAFE_ASSERTION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

在 Flash 尚未就绪的休眠唤醒路径（Sleep Wake Path）中检查缓存安全性（Cache Safety）。仅供代码质量检查使用，会增加开销。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：`<module:hal_espressif>/zephyr/Kconfig:299`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_espressif`（Espressif 硬件抽象层模块；工作区相对路径 `modules/hal/espressif`） → 休眠配置（Sleep Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_SLEEP_FLASH_LEAKAGE_WORKAROUND"></a>

## 10.2 `CONFIG_ESP_SLEEP_FLASH_LEAKAGE_WORKAROUND`

**提示（Prompt）**：浅睡眠（Light Sleep）期间上拉 Flash CS 引脚

**说明（Help）**

浅睡眠（Light Sleep）期间，GPIO 可能悬空。如果 Flash 片选（Chip Select，CS）引脚被读取为低电平，芯片可能出现漏电流或伪总线活动。此选项在休眠期间将 CS 拉高。如果模块设计没有外部 CS 上拉，请保持启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FLASH_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:hal_espressif>/zephyr/Kconfig:332`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_espressif`（Espressif 硬件抽象层模块；工作区相对路径 `modules/hal/espressif`） → 休眠配置（Sleep Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FLASH_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_ESP32)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_SLEEP_GPIO_ENABLE_INTERNAL_RESISTORS"></a>

## 10.3 `CONFIG_ESP_SLEEP_GPIO_ENABLE_INTERNAL_RESISTORS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

当没有外部电阻时，允许为用作深睡眠唤醒 IO（Deep-sleep Wakeup IO）的 RTC GPIO 启用内部上拉／下拉（Pull-up/Pull-down）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:hal_espressif>/zephyr/Kconfig:305`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_espressif`（Espressif 硬件抽象层模块；工作区相对路径 `modules/hal/espressif`） → 休眠配置（Sleep Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_SLEEP_GPIO_RESET_WORKAROUND"></a>

## 10.4 `CONFIG_ESP_SLEEP_GPIO_RESET_WORKAROUND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

GPIO 静电放电（Electrostatic Discharge，ESD）复位问题的软件规避措施（Workaround）。在浅睡眠（Light Sleep）期间，如果配置为仅输入的 GPIO 接收到较小的静电脉冲（>6 V），可能在唤醒时触发复位。启用此选项后，会在休眠期间将所有 GPIO 引脚配置为隔离状态（Isolate State）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y if !(CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32S2)
```

**定义位置（Location）**：`<module:hal_espressif>/zephyr/Kconfig:290`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_espressif`（Espressif 硬件抽象层模块；工作区相对路径 `modules/hal/espressif`） → 休眠配置（Sleep Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_SLEEP_MSPI_NEED_ALL_IO_PU"></a>

## 10.5 `CONFIG_ESP_SLEEP_MSPI_NEED_ALL_IO_PU`

**提示（Prompt）**：浅睡眠（Light Sleep）期间上拉所有 MSPI 引脚

**说明（Help）**

某些 Flash/PSRAM 器件要求在休眠期间将所有 MSPI 线路保持在已知状态，而不仅是 CS。如果所用器件的数据手册（Datasheet）提出此建议，请启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ESP_SLEEP_FLASH_LEAKAGE_WORKAROUND || CONFIG_ESP_SLEEP_PSRAM_LEAKAGE_WORKAROUND) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32C2
```

**定义位置（Location）**：`<module:hal_espressif>/zephyr/Kconfig:350`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_espressif`（Espressif 硬件抽象层模块；工作区相对路径 `modules/hal/espressif`） → 休眠配置（Sleep Configuration）

**配置项引用（Symbol References）**：[`CONFIG_ESP_SLEEP_FLASH_LEAKAGE_WORKAROUND`](P010_module_hal_espressif_zephyr_配置项参考.md#CONFIG_ESP_SLEEP_FLASH_LEAKAGE_WORKAROUND)、[`CONFIG_ESP_SLEEP_PSRAM_LEAKAGE_WORKAROUND`](P010_module_hal_espressif_zephyr_配置项参考.md#CONFIG_ESP_SLEEP_PSRAM_LEAKAGE_WORKAROUND)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SOC_SERIES_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`、`CONFIG_SOC_SERIES_ESP32C2`。

<a id="CONFIG_ESP_SLEEP_PSRAM_LEAKAGE_WORKAROUND"></a>

## 10.6 `CONFIG_ESP_SLEEP_PSRAM_LEAKAGE_WORKAROUND`

**提示（Prompt）**：浅睡眠（Light Sleep）期间上拉 PSRAM CS 引脚

**说明（Help）**

原因与 Flash CS 相同，此处适用于 PSRAM。使用 SPIRAM 且 CS 线没有外部上拉（Pull-up）时启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_SPIRAM && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:hal_espressif>/zephyr/Kconfig:342`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_espressif`（Espressif 硬件抽象层模块；工作区相对路径 `modules/hal/espressif`） → 休眠配置（Sleep Configuration）

**配置项引用（Symbol References）**：[`CONFIG_ESP_SPIRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_SPIRAM)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_SYSTEM_RTC_EXT_XTAL_BOOTSTRAP_CYCLES"></a>

## 10.7 `CONFIG_ESP_SYSTEM_RTC_EXT_XTAL_BOOTSTRAP_CYCLES`

**提示（Prompt）**：外部 32 kHz 晶体的助振周期数（Bootstrap Cycles）

**说明（Help）**

为缩短外部 RTC 晶体（Crystal）的启动时间，使用固定周期数的 32 kHz 方波进行助振（Bootstrap）。设为 `0` 将禁用助振；禁用后，晶体可能需要更长时间启动，或在某些条件下无法起振。如果该值过大，有故障的晶体可能最初能起振，随后又停止；如果该值过小，原本正常的晶体也可能无法启动。为准确判断晶体是否已启动，请将“RTC_SLOW_CLK 校准周期数（Number of Cycles for RTC_SLOW_CLK Calibration）”设为较大值，约为 3000。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_CRYS && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
5 if CONFIG_SOC_SERIES_ESP32
0
```

**取值范围（Ranges）**

```text
[0, 32768]
```

**定义位置（Location）**：`<module:hal_espressif>/zephyr/Kconfig:94`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_espressif`（Espressif 硬件抽象层模块；工作区相对路径 `modules/hal/espressif`）

**配置项引用（Symbol References）**：[`CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_CRYS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_ESP32_RTC_CLK_SRC_EXT_CRYS)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_WIFI_TASK_CORE_ID"></a>

## 10.8 `CONFIG_ESP_WIFI_TASK_CORE_ID`

**提示（Prompt）**：Wi-Fi 任务内核 ID（Task Core ID）

**说明（Help）**

将 Wi-Fi 任务绑定（Pin）到内核 0 或内核 1。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S3 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP_WIFI_TASK_PINNED_TO_CORE_0
```

**可选项（Choices）**

```text
CONFIG_ESP_WIFI_TASK_PINNED_TO_CORE_0
CONFIG_ESP_WIFI_TASK_PINNED_TO_CORE_1
```

**定义位置（Location）**：`<module:hal_espressif>/zephyr/Kconfig:259`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_espressif`（Espressif 硬件抽象层模块；工作区相对路径 `modules/hal/espressif`） → Wi-Fi 配置（Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP_WIFI_TASK_PINNED_TO_CORE_0`](P010_module_hal_espressif_zephyr_配置项参考.md#CONFIG_ESP_WIFI_TASK_PINNED_TO_CORE_0)、[`CONFIG_ESP_WIFI_TASK_PINNED_TO_CORE_1`](P010_module_hal_espressif_zephyr_配置项参考.md#CONFIG_ESP_WIFI_TASK_PINNED_TO_CORE_1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_WIFI_TASK_PINNED_TO_CORE_0"></a>

## 10.9 `CONFIG_ESP_WIFI_TASK_PINNED_TO_CORE_0`

**提示（Prompt）**：内核 0（Core 0）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP_WIFI_TASK_CORE_ID>
```

**定义位置（Location）**：`<module:hal_espressif>/zephyr/Kconfig:266`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_espressif`（Espressif 硬件抽象层模块；工作区相对路径 `modules/hal/espressif`） → Wi-Fi 配置（Configuration） → Wi-Fi 任务内核 ID（Task Core ID）

**配置项引用（Symbol References）**：[`CONFIG_ESP_WIFI_TASK_CORE_ID`](P010_module_hal_espressif_zephyr_配置项参考.md#CONFIG_ESP_WIFI_TASK_CORE_ID)。

<a id="CONFIG_ESP_WIFI_TASK_PINNED_TO_CORE_1"></a>

## 10.10 `CONFIG_ESP_WIFI_TASK_PINNED_TO_CORE_1`

**提示（Prompt）**：内核 1（Core 1）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP_WIFI_TASK_CORE_ID>
```

**定义位置（Location）**：`<module:hal_espressif>/zephyr/Kconfig:269`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_espressif`（Espressif 硬件抽象层模块；工作区相对路径 `modules/hal/espressif`） → Wi-Fi 配置（Configuration） → Wi-Fi 任务内核 ID（Task Core ID）

**配置项引用（Symbol References）**：[`CONFIG_ESP_WIFI_TASK_CORE_ID`](P010_module_hal_espressif_zephyr_配置项参考.md#CONFIG_ESP_WIFI_TASK_CORE_ID)。

<a id="CONFIG_PM_CHECK_SLEEP_RETENTION_FRAME"></a>

## 10.11 `CONFIG_PM_CHECK_SLEEP_RETENTION_FRAME`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

跨浅睡眠（Light Sleep）过程使用循环冗余校验（CRC）验证 CPU／外设休眠保留帧（Sleep Retention Frame）。这会增加休眠和唤醒开销，因此不可由用户选择，仅用于内部验证。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：`<module:hal_espressif>/zephyr/Kconfig:325`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_espressif`（Espressif 硬件抽象层模块；工作区相对路径 `modules/hal/espressif`） → 休眠配置（Sleep Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_PM_SLP_DISABLE_GPIO"></a>

## 10.12 `CONFIG_PM_SLP_DISABLE_GPIO`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

休眠期间禁用 GPIO 输出以减少漏电流（Leakage）。GPIO 复位规避措施（Reset Workaround）会弱选择（Imply）此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y if CONFIG_ESP_SLEEP_GPIO_RESET_WORKAROUND
```

**定义位置（Location）**：`<module:hal_espressif>/zephyr/Kconfig:318`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_espressif`（Espressif 硬件抽象层模块；工作区相对路径 `modules/hal/espressif`） → 休眠配置（Sleep Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP_SLEEP_GPIO_RESET_WORKAROUND`](P010_module_hal_espressif_zephyr_配置项参考.md#CONFIG_ESP_SLEEP_GPIO_RESET_WORKAROUND)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_PM_SLP_SPIRAM_HALFSLEEP_EXIT_WAIT_DELAY"></a>

## 10.13 `CONFIG_PM_SLP_SPIRAM_HALFSLEEP_EXIT_WAIT_DELAY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

PSRAM 从半休眠（Halfsleep）唤醒到首次访问它之间的延迟，以微秒为单位。此项对应 ESP-IDF 中的同名符号，使得即便应用程序未启用电源管理（PM），HAL 的半休眠恢复代码仍可编译。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
150
```

**定义位置（Location）**：`<module:hal_espressif>/zephyr/Kconfig:198`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_espressif`（Espressif 硬件抽象层模块；工作区相对路径 `modules/hal/espressif`）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<!-- kconfig-navigation -->

[上一章](P009_module_cmsis-dsp_zephyr_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P011_module_hal_intel_zephyr_配置项参考.md)
