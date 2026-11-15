---
id: learning.zephyr-docs.kconfig-reference.page-277
title: "`soc/espressif`配置项参考（3/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第277章\_`soc/espressif`配置项参考（3/3）

本章翻译官方 Kconfig 数据库中 `soc/espressif` 的 54 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_SOC_ESP32_PM_WAKEUP_MARGIN_US"></a>

## 277.1 `CONFIG_SOC_ESP32_PM_WAKEUP_MARGIN_US`

**提示（Prompt）**：轻度睡眠 RTC 唤醒提前裕量，单位为微秒（Light sleep RTC wake pad）

**说明（Help）**

为轻度睡眠编程 RTC 唤醒定时器时，除减去从进入空闲状态起已测得的耗时之外，还额外减去这段时间。HAL 睡眠代码会根据启用的硬件资源估算退出延迟（exit latency）并进行补偿，但该补偿未覆盖睡眠路径涉及的全部代码。如果不加入额外裕量，某些配置下就无法满足内核唤醒截止时间（wake deadline）。Zephyr 的 `exit-latency-us`（DTS 设置）不能用于此补偿，因为唤醒信号来自低功耗定时器（LP timer），而非 Zephyr 调度所用的系统定时器。因此，需要重新计算唤醒截止时间并增加额外裕量。

启用外设断电时，默认值为 0（ESP32-C5 除外）：HAL 已高估该唤醒路径耗时，再加裕量只会浪费睡眠时间。ESP32-C5 在 CPU 断电时需要明显更大的提前量：缓存标记（cache tags）位于 CPU 电源域内，因此每次唤醒都从冷缓存（cold cache）开始，并从 Flash 重新填充，这构成恢复路径中的主要耗时。禁用 CPU 断电可消除额外延迟；IRAM 优化则通过使早期唤醒路径不依赖 Flash 缓存来缩短延迟。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_PM && CONFIG_TICKLESS_KERNEL && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
1000 if CONFIG_SOC_SERIES_ESP32C5 && CONFIG_ESP32_PM_POWER_DOWN_CPU_IN_LIGHT_SLEEP && CONFIG_ESP32_PM_SLP_IRAM_OPT
2000 if CONFIG_SOC_SERIES_ESP32C5 && CONFIG_ESP32_PM_POWER_DOWN_CPU_IN_LIGHT_SLEEP
0 if CONFIG_ESP32_PM_POWER_DOWN_PERIPHERAL_IN_LIGHT_SLEEP
300
```

**取值范围（Ranges）**

```text
[0, 2000]
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.pm:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.pm#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Espressif 电源管理配置（PM Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_ESP32_PM_POWER_DOWN_CPU_IN_LIGHT_SLEEP`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_PM_POWER_DOWN_CPU_IN_LIGHT_SLEEP)、[`CONFIG_ESP32_PM_SLP_IRAM_OPT`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_PM_SLP_IRAM_OPT)、[`CONFIG_ESP32_PM_POWER_DOWN_PERIPHERAL_IN_LIGHT_SLEEP`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_PM_POWER_DOWN_PERIPHERAL_IN_LIGHT_SLEEP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`、`CONFIG_SOC_SERIES_ESP32C5`。

<a id="CONFIG_SOC_ESP32_PROCPU"></a>

## 277.2 `CONFIG_SOC_ESP32_PROCPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为协议 CPU（PROCPU，内核 0）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BOARD_YD_ESP32
CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32
CONFIG_BOARD_TTGO_T7V1_5
CONFIG_BOARD_TTGO_TBEAM
CONFIG_BOARD_TTGO_LORA32
CONFIG_BOARD_ESP32_ETHERNET_KIT
CONFIG_BOARD_ESP_WROVER_KIT
CONFIG_BOARD_ESP32_DEVKITC
CONFIG_BOARD_ESP32_DEVKITC
CONFIG_BOARD_ESP32_CAM
CONFIG_BOARD_INKPLATE_6COLOR
CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1
CONFIG_BOARD_LOLIN32_LITE
CONFIG_BOARD_UDOO_KEY
CONFIG_BOARD_M5STACK_CORE2
CONFIG_BOARD_M5STACK_FIRE
CONFIG_BOARD_M5STICKC_PLUS
CONFIG_BOARD_M5STACK_ATOM_LITE
CONFIG_BOARD_OLIMEX_ESP32_EVB
CONFIG_BOARD_CAN485DBV1
CONFIG_BOARD_KINCONY_KC868_A8
CONFIG_BOARD_KINCONY_KC868_A32
CONFIG_BOARD_ODROID_GO
CONFIG_BOARD_HELTEC_WIFI_LORA32_V2
```

**定义位置（Location）**：[`soc/espressif/esp32/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_YD_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_YD_ESP32)、[`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32)、[`CONFIG_BOARD_TTGO_T7V1_5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TTGO_T7V1_5)、[`CONFIG_BOARD_TTGO_TBEAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TTGO_TBEAM)、[`CONFIG_BOARD_TTGO_LORA32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_TTGO_LORA32)、[`CONFIG_BOARD_ESP32_ETHERNET_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32_ETHERNET_KIT)、[`CONFIG_BOARD_ESP_WROVER_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP_WROVER_KIT)、[`CONFIG_BOARD_ESP32_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32_DEVKITC)、[`CONFIG_BOARD_ESP32_CAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ESP32_CAM)、[`CONFIG_BOARD_INKPLATE_6COLOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_INKPLATE_6COLOR)、[`CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1)、[`CONFIG_BOARD_LOLIN32_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_LOLIN32_LITE)、[`CONFIG_BOARD_UDOO_KEY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_UDOO_KEY)、[`CONFIG_BOARD_M5STACK_CORE2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_CORE2)、[`CONFIG_BOARD_M5STACK_FIRE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_FIRE)、[`CONFIG_BOARD_M5STICKC_PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STICKC_PLUS)、[`CONFIG_BOARD_M5STACK_ATOM_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_M5STACK_ATOM_LITE)、[`CONFIG_BOARD_OLIMEX_ESP32_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_OLIMEX_ESP32_EVB)、[`CONFIG_BOARD_CAN485DBV1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_CAN485DBV1)、[`CONFIG_BOARD_KINCONY_KC868_A8`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_KINCONY_KC868_A8)、[`CONFIG_BOARD_KINCONY_KC868_A32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_KINCONY_KC868_A32)、[`CONFIG_BOARD_ODROID_GO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_ODROID_GO)、[`CONFIG_BOARD_HELTEC_WIFI_LORA32_V2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_HELTEC_WIFI_LORA32_V2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_YD_ESP32`、`CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32`、`CONFIG_BOARD_TTGO_T7V1_5`、`CONFIG_BOARD_TTGO_TBEAM`、`CONFIG_BOARD_TTGO_LORA32`、`CONFIG_BOARD_ESP32_ETHERNET_KIT`、`CONFIG_BOARD_ESP_WROVER_KIT`、`CONFIG_BOARD_ESP32_DEVKITC`、`CONFIG_BOARD_ESP32_CAM`、`CONFIG_BOARD_INKPLATE_6COLOR`、`CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1`、`CONFIG_BOARD_LOLIN32_LITE`、`CONFIG_BOARD_UDOO_KEY`、`CONFIG_BOARD_M5STACK_CORE2`、`CONFIG_BOARD_M5STACK_FIRE`、`CONFIG_BOARD_M5STICKC_PLUS`、`CONFIG_BOARD_M5STACK_ATOM_LITE`、`CONFIG_BOARD_OLIMEX_ESP32_EVB`、`CONFIG_BOARD_CAN485DBV1`、`CONFIG_BOARD_KINCONY_KC868_A8`、`CONFIG_BOARD_KINCONY_KC868_A32`、`CONFIG_BOARD_ODROID_GO`、`CONFIG_BOARD_HELTEC_WIFI_LORA32_V2`。

<a id="CONFIG_SOC_ESP32_SLEEP_DCM_VSET_VAL_IN_SLEEP"></a>

## 277.3 `CONFIG_SOC_ESP32_SLEEP_DCM_VSET_VAL_IN_SLEEP`

**提示（Prompt）**：睡眠期间的直流－直流转换器电压参数（DCDC voltage parameter）

**说明（Help）**

睡眠期间直流－直流转换器（DCDC converter）的电压。同一参数值在不同 DCDC 型号上可能对应不同电压，因此应根据硬件选择的外部 DCDC 调整。TI TLV62569／TLV62569P 的建议值为 14。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32P4 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
14
```

**取值范围（Ranges）**

```text
[0, 31]
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.flash:159`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.flash#L159)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SOC_SERIES_ESP32"></a>

## 277.4 `CONFIG_SOC_SERIES_ESP32`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ESP32 系列（Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**被选择（Selected by）**

```text
CONFIG_SOC_ESP32
```

**定义位置（Location）**：[`soc/espressif/esp32/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SOC_ESP32`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SOC_SERIES_ESP32C3"></a>

## 277.5 `CONFIG_SOC_SERIES_ESP32C3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ESP32C3 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**被选择（Selected by）**

```text
CONFIG_SOC_ESP32C3
```

**定义位置（Location）**：[`soc/espressif/esp32c3/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c3/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SOC_ESP32C3`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ESP32C3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SOC_SERIES_ESP32S2"></a>

## 277.6 `CONFIG_SOC_SERIES_ESP32S2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ESP32-S2 系列（Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**被选择（Selected by）**

```text
CONFIG_SOC_ESP32S2
```

**定义位置（Location）**：[`soc/espressif/esp32s2/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s2/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SOC_ESP32S2`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ESP32S2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SOC_SERIES_ESP32S3"></a>

## 277.7 `CONFIG_SOC_SERIES_ESP32S3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ESP32-S3 系列（Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**被选择（Selected by）**

```text
CONFIG_SOC_ESP32S3
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SOC_ESP32S3`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ESP32S3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SPIRAM_CUSTOM_SPIWP_SD3_PIN"></a>

## 277.8 `CONFIG_SPIRAM_CUSTOM_SPIWP_SD3_PIN`

**提示（Prompt）**：Flash 引脚由 eFuse 设置时，使用自定义 SPI PSRAM 写保护引脚 WP（SD3），请阅读帮助（Custom WP Pin）

**说明（Help）**

仅当通过设置 `SPI_PAD_CONFIG_xxx` eFuse 覆盖 SPI Flash 引脚，并且 SPI Flash 模式为 DIO 或 DOUT 时，才使用此设置。此时，eFuse 配置只定义四线 IO（Quad I/O）数据引脚中的三个，未指定写保护引脚 WP，即 ESP32 的 `SD_DATA_3` 引脚或 SPI Flash 的 `IO2` 引脚。PSRAM 只有 QPI 模式，因此必须设置 WP 引脚。

此配置为 `N`（默认）时，对于任何集成 Flash 的 Espressif 芯片或模组，都会自动使用正确的 WP 引脚。如果需要自定义设置，请设为 `Y`，并指定连接 WP 引脚的 GPIO 编号。Flash 模式为 QIO 或 QOUT 时，PSRAM WP 引脚将与引导加载程序中配置的 SPI Flash WP 引脚一致。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ESPTOOLPY_FLASHMODE_DIO || CONFIG_ESPTOOLPY_FLASHMODE_DOUT) && CONFIG_SOC_SERIES_ESP32 && CONFIG_ESP_SPIRAM && (CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L221)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_FLASHMODE_DIO`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHMODE_DIO)、[`CONFIG_ESPTOOLPY_FLASHMODE_DOUT`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHMODE_DOUT)、[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_ESP_SPIRAM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SPIRAM_ECC_ENABLE"></a>

## 277.9 `CONFIG_SPIRAM_ECC_ENABLE`

**提示（Prompt）**：允许启用 SPI RAM 错误纠正码（ECC）

**说明（Help）**

访问 SPI RAM 时启用 MSPI 错误纠正码功能（Error-Correcting Code，ECC）。启用后，将预留 SPI RAM 总容量的 1/16 用于错误纠正码；在 ESP32-C5 和 ESP32-C61 上为 1/8。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || (CONFIG_SPIRAM_MODE_OCT && CONFIG_SOC_SERIES_ESP32S3) || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_ESP_SPIRAM && (CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SPIRAM_MODE_OCT`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_MODE_OCT)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_ESP_SPIRAM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM)、[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SPIRAM_FETCH_INSTRUCTIONS"></a>

## 277.10 `CONFIG_SPIRAM_FETCH_INSTRUCTIONS`

**提示（Prompt）**：将 Flash 中的指令移到 PSRAM（Move Instructions to PSRAM）

**说明（Help）**

启用后，启动时会将 Flash 中的指令移到 PSRAM。如果同时启用 `SPIRAM_RODATA`，则需要在 SPI1 Flash 操作期间执行的代码可以不再放入指令 RAM（IRAM），从而优化 RAM 使用。更多细节请参阅外部 RAM 文档（External RAM documentation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3) && CONFIG_ESP_SPIRAM && (CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_ESP_SPIRAM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM)、[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SPIRAM_MODE"></a>

## 277.11 `CONFIG_SPIRAM_MODE`

**提示（Prompt）**：所用 SPI RAM 芯片的模式：四线／八线／十六线（QUAD/OCT/HEX）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_SPIRAM && (CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_SPIRAM_MODE_HEX if CONFIG_SOC_SERIES_ESP32P4
CONFIG_SPIRAM_MODE_QUAD
```

**可选项（Choices）**

```text
CONFIG_SPIRAM_MODE_QUAD
CONFIG_SPIRAM_MODE_OCT
CONFIG_SPIRAM_MODE_HEX
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config）

**配置项引用（Symbol References）**：[`CONFIG_ESP_SPIRAM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM)、[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SPIRAM_MODE_HEX`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_MODE_HEX)、[`CONFIG_SPIRAM_MODE_QUAD`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_MODE_QUAD)、[`CONFIG_SPIRAM_MODE_OCT`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_MODE_OCT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SPIRAM_MODE_HEX"></a>

## 277.12 `CONFIG_SPIRAM_MODE_HEX`

**提示（Prompt）**：十六线模式 PSRAM（16-Line Mode PSRAM）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32P4 && <choice CONFIG_SPIRAM_MODE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config） → 所用 SPI RAM 芯片的模式：四线／八线／十六线（QUAD/OCT/HEX）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SPIRAM_MODE`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_MODE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`。

<a id="CONFIG_SPIRAM_MODE_OCT"></a>

## 277.13 `CONFIG_SPIRAM_MODE_OCT`

**提示（Prompt）**：八线模式 PSRAM（Octal Mode PSRAM）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S3 && <choice CONFIG_SPIRAM_MODE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config） → 所用 SPI RAM 芯片的模式：四线／八线／十六线（QUAD/OCT/HEX）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SPIRAM_MODE`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_MODE)。

<a id="CONFIG_SPIRAM_MODE_QUAD"></a>

## 277.14 `CONFIG_SPIRAM_MODE_QUAD`

**提示（Prompt）**：四线模式 PSRAM（Quad Mode PSRAM）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_ESP32P4 && <choice CONFIG_SPIRAM_MODE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config） → 所用 SPI RAM 芯片的模式：四线／八线／十六线（QUAD/OCT/HEX）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SPIRAM_MODE`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_MODE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`。

<a id="CONFIG_SPIRAM_RODATA"></a>

## 277.15 `CONFIG_SPIRAM_RODATA`

**提示（Prompt）**：将 Flash 中的只读数据移到 PSRAM（Move Read-Only Data to PSRAM）

**说明（Help）**

启用后，启动时会将 Flash 中的只读数据（rodata）移到 PSRAM。如果同时启用 `SPIRAM_FETCH_INSTRUCTIONS`，则需要在 SPI1 Flash 操作期间执行的代码可以不再放入指令 RAM（IRAM），从而优化 RAM 使用。更多细节请参阅外部 RAM 文档（External RAM documentation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3) && CONFIG_ESP_SPIRAM && (CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_ESP_SPIRAM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM)、[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SPIRAM_SPEED"></a>

## 277.16 `CONFIG_SPIRAM_SPEED`

**提示（Prompt）**：设置 RAM 时钟速率（RAM clock speed）

**说明（Help）**

选择 SPI RAM 芯片的速率（speed）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_SPIRAM && (CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_SPIRAM_SPEED_200M if CONFIG_SOC_SERIES_ESP32P4
CONFIG_SPIRAM_SPEED_40M
```

**可选项（Choices）**

```text
CONFIG_SPIRAM_SPEED_20M
CONFIG_SPIRAM_SPEED_26M
CONFIG_SPIRAM_SPEED_40M
CONFIG_SPIRAM_SPEED_80M
CONFIG_SPIRAM_SPEED_120M
CONFIG_SPIRAM_SPEED_200M
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config）

**配置项引用（Symbol References）**：[`CONFIG_ESP_SPIRAM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM)、[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SPIRAM_SPEED_200M`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_SPEED_200M)、[`CONFIG_SPIRAM_SPEED_40M`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_SPEED_40M)、[`CONFIG_SPIRAM_SPEED_20M`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_SPEED_20M)、[`CONFIG_SPIRAM_SPEED_26M`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_SPEED_26M)、[`CONFIG_SPIRAM_SPEED_80M`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_SPEED_80M)、[`CONFIG_SPIRAM_SPEED_120M`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_SPEED_120M)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SPIRAM_SPEED_120M"></a>

## 277.17 `CONFIG_SPIRAM_SPEED_120M`

**提示（Prompt）**：120MHz 时钟速率（clock speed）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPIRAM_MODE_QUAD && (CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32S3) && CONFIG_ESPTOOLPY_FLASHFREQ_120M && <choice CONFIG_SPIRAM_SPEED>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config） → 设置 RAM 时钟速率（RAM clock speed）

**配置项引用（Symbol References）**：[`CONFIG_SPIRAM_MODE_QUAD`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_MODE_QUAD)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_ESPTOOLPY_FLASHFREQ_120M`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHFREQ_120M)、[`CONFIG_SPIRAM_SPEED`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_SPEED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`。

<a id="CONFIG_SPIRAM_SPEED_200M"></a>

## 277.18 `CONFIG_SPIRAM_SPEED_200M`

**提示（Prompt）**：200MHz 时钟速率（clock speed）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32P4 && <choice CONFIG_SPIRAM_SPEED>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config） → 设置 RAM 时钟速率（RAM clock speed）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SPIRAM_SPEED`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_SPEED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`。

<a id="CONFIG_SPIRAM_SPEED_20M"></a>

## 277.19 `CONFIG_SPIRAM_SPEED_20M`

**提示（Prompt）**：20MHz 时钟速率（clock speed）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32P4) && <choice CONFIG_SPIRAM_SPEED>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config） → 设置 RAM 时钟速率（RAM clock speed）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SPIRAM_SPEED`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_SPEED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`。

<a id="CONFIG_SPIRAM_SPEED_26M"></a>

## 277.20 `CONFIG_SPIRAM_SPEED_26M`

**提示（Prompt）**：26MHz 时钟速率（clock speed）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S2 && <choice CONFIG_SPIRAM_SPEED>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config） → 设置 RAM 时钟速率（RAM clock speed）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SPIRAM_SPEED`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_SPEED)。

<a id="CONFIG_SPIRAM_SPEED_40M"></a>

## 277.21 `CONFIG_SPIRAM_SPEED_40M`

**提示（Prompt）**：40MHz 时钟速率（clock speed）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_ESP32P4 && <choice CONFIG_SPIRAM_SPEED>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config） → 设置 RAM 时钟速率（RAM clock speed）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SPIRAM_SPEED`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_SPEED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`。

<a id="CONFIG_SPIRAM_SPEED_80M"></a>

## 277.22 `CONFIG_SPIRAM_SPEED_80M`

**提示（Prompt）**：80MHz 时钟速率（clock speed）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ESPTOOLPY_FLASHFREQ_80M || CONFIG_SOC_SERIES_ESP32P4) && <choice CONFIG_SPIRAM_SPEED>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config） → 设置 RAM 时钟速率（RAM clock speed）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_FLASHFREQ_80M`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHFREQ_80M)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SPIRAM_SPEED`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_SPEED)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`。

<a id="CONFIG_SPIRAM_SPIWP_SD3_PIN"></a>

## 277.23 `CONFIG_SPIRAM_SPIWP_SD3_PIN`

**提示（Prompt）**：自定义 SPI PSRAM 写保护引脚 WP（SD3）（Custom WP Pin）

**说明（Help）**

必须设置“使用自定义 SPI PSRAM WP（SD3）引脚”（Use custom SPI PSRAM WP(SD3) pin）选项，否则忽略此值。如果在 eFuse 中烧录了自定义 SPI Flash 引脚组合，并且 Flash 使用 DIO 或 DOUT 模式，请将此值设为 SPI RAM WP 引脚的 GPIO 编号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SPIRAM_CUSTOM_SPIWP_SD3_PIN && CONFIG_SOC_SERIES_ESP32 && CONFIG_ESP_SPIRAM && (CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
7
```

**取值范围（Ranges）**

```text
[0, 33]
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L239)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config） → Flash 引脚由 eFuse 设置时，使用自定义 SPI PSRAM 写保护引脚 WP（SD3），请阅读帮助（Custom WP Pin）

**配置项引用（Symbol References）**：[`CONFIG_SPIRAM_CUSTOM_SPIWP_SD3_PIN`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_CUSTOM_SPIWP_SD3_PIN)、[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_ESP_SPIRAM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SPIRAM_TYPE"></a>

## 277.24 `CONFIG_SPIRAM_TYPE`

**提示（Prompt）**：所用 SPI RAM 芯片类型（Type of SPI RAM chip）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_SOC_SERIES_ESP32P4 && CONFIG_ESP_SPIRAM && (CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_SPIRAM_TYPE_ESPPSRAM16 if CONFIG_SPIRAM_MODE_QUAD
CONFIG_SPIRAM_TYPE_ESPPSRAM64
```

**可选项（Choices）**

```text
CONFIG_SPIRAM_TYPE_ESPPSRAM16
CONFIG_SPIRAM_TYPE_ESPPSRAM32
CONFIG_SPIRAM_TYPE_ESPPSRAM64
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_ESP_SPIRAM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM)、[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SPIRAM_TYPE_ESPPSRAM16`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_TYPE_ESPPSRAM16)、[`CONFIG_SPIRAM_MODE_QUAD`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_MODE_QUAD)、[`CONFIG_SPIRAM_TYPE_ESPPSRAM64`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_TYPE_ESPPSRAM64)、[`CONFIG_SPIRAM_TYPE_ESPPSRAM32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_TYPE_ESPPSRAM32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SPIRAM_TYPE_ESPPSRAM16"></a>

## 277.25 `CONFIG_SPIRAM_TYPE_ESPPSRAM16`

**提示（Prompt）**：ESP-PSRAM16 或 APS1604（芯片类型，chip type）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPIRAM_MODE_QUAD && CONFIG_ESP_SPIRAM_SIZE = 2097152 && <choice CONFIG_SPIRAM_TYPE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config） → 所用 SPI RAM 芯片类型（Type of SPI RAM chip）

**配置项引用（Symbol References）**：[`CONFIG_SPIRAM_MODE_QUAD`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_MODE_QUAD)、[`CONFIG_ESP_SPIRAM_SIZE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM_SIZE)、[`CONFIG_SPIRAM_TYPE`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_TYPE)。

<a id="CONFIG_SPIRAM_TYPE_ESPPSRAM32"></a>

## 277.26 `CONFIG_SPIRAM_TYPE_ESPPSRAM32`

**提示（Prompt）**：ESP-PSRAM32 或 IS25WP032（芯片类型，chip type）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SPIRAM_MODE_QUAD && CONFIG_ESP_SPIRAM_SIZE = 4194304 && <choice CONFIG_SPIRAM_TYPE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config） → 所用 SPI RAM 芯片类型（Type of SPI RAM chip）

**配置项引用（Symbol References）**：[`CONFIG_SPIRAM_MODE_QUAD`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_MODE_QUAD)、[`CONFIG_ESP_SPIRAM_SIZE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM_SIZE)、[`CONFIG_SPIRAM_TYPE`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_TYPE)。

<a id="CONFIG_SPIRAM_TYPE_ESPPSRAM64"></a>

## 277.27 `CONFIG_SPIRAM_TYPE_ESPPSRAM64`

**提示（Prompt）**：ESP-PSRAM64、LY68L6400 或 APS6408（芯片类型，chip type）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP_SPIRAM_SIZE = 8388608 && <choice CONFIG_SPIRAM_TYPE>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config） → 所用 SPI RAM 芯片类型（Type of SPI RAM chip）

**配置项引用（Symbol References）**：[`CONFIG_ESP_SPIRAM_SIZE`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM_SIZE)、[`CONFIG_SPIRAM_TYPE`](P277_soc_espressif_配置项参考_3.md#CONFIG_SPIRAM_TYPE)。

<a id="CONFIG_SPI_FLASH_HPM_ENABLE"></a>

## 277.28 `CONFIG_SPI_FLASH_HPM_ENABLE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项不可见，选择 `ESPTOOLPY_FLASHFREQ_120M` 时会自动选择它。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S3 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**被选择（Selected by）**

```text
CONFIG_ESPTOOLPY_FLASHFREQ_120M
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.flash:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.flash#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESPTOOLPY_FLASHFREQ_120M`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHFREQ_120M)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SPI_FLASH_ROM_DRIVER_PATCH"></a>

## 277.29 `CONFIG_SPI_FLASH_ROM_DRIVER_PATCH`

**提示（Prompt）**：SPI Flash ROM 驱动的修补版函数（patched functions）

**说明（Help）**

启用此标志以使用 SPI Flash ROM 驱动函数的修补版（patched versions）。满足以下任一条件时应启用：

1. 需要在 ESP32-D2WD 上写入 Flash。
2. 主 SPI Flash 连接到非默认引脚。
3. 主 SPI Flash 芯片由 ISSI 制造。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.flash:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.flash#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SPI_FLASH_SUPPORT_BOYA_CHIP"></a>

## 277.30 `CONFIG_SPI_FLASH_SUPPORT_BOYA_CHIP`

**提示（Prompt）**：BOYA Flash 厂商（vendor）

**说明（Help）**

如果芯片结构体的 `chip_drv` 成员未直接给出芯片厂商，启用此项可支持自动检测 BOYA 芯片。这样会增加对不同芯片型号的支持，但也会延长检测时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y if !CONFIG_SOC_SERIES_ESP32
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.flash:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.flash#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SPI_FLASH_SUPPORT_GD_CHIP"></a>

## 277.31 `CONFIG_SPI_FLASH_SUPPORT_GD_CHIP`

**提示（Prompt）**：兆易创新（GigaDevice）

**说明（Help）**

如果芯片结构体的 `chip_drv` 成员未直接给出芯片厂商，启用此项可支持自动检测 GD（GigaDevice，兆易创新）芯片。如果使用 Wrover 模组，请不要禁用，否则 Flash 可能无法在 4 位模式下工作。这样会增加对不同芯片型号的支持，但也会延长检测时间并增大镜像体积。注意，默认芯片驱动支持产品 ID 为 60H 的 GD 芯片。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.flash:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.flash#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SPI_FLASH_SUPPORT_ISSI_CHIP"></a>

## 277.32 `CONFIG_SPI_FLASH_SUPPORT_ISSI_CHIP`

**提示（Prompt）**：ISSI Flash 厂商（vendor）

**说明（Help）**

如果芯片结构体的 `chip_drv` 成员未直接给出芯片厂商，启用此项可支持自动检测 ISSI 芯片。这样会增加对不同芯片型号的支持，但也会延长检测时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.flash:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.flash#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SPI_FLASH_SUPPORT_MXIC_CHIP"></a>

## 277.33 `CONFIG_SPI_FLASH_SUPPORT_MXIC_CHIP`

**提示（Prompt）**：MXIC Flash 厂商（vendor）

**说明（Help）**

如果芯片结构体的 `chip_drv` 成员未直接给出芯片厂商，启用此项可支持自动检测 MXIC 芯片。这样会增加对不同芯片型号的支持，但也会延长检测时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.flash:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.flash#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SPI_FLASH_SUPPORT_MXIC_OPI_CHIP"></a>

## 277.34 `CONFIG_SPI_FLASH_SUPPORT_MXIC_OPI_CHIP`

**提示（Prompt）**：MXIC 八线外设接口（mxic, opi）

**说明（Help）**

如果芯片结构体的 `chip_drv` 成员未直接给出芯片厂商，启用此项可支持自动检测八线 MXIC 芯片（Octal MXIC chips）。这样会增加对不同芯片型号的支持，但也会延长检测时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S3 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.flash:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.flash#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SPI_FLASH_SUPPORT_TH_CHIP"></a>

## 277.35 `CONFIG_SPI_FLASH_SUPPORT_TH_CHIP`

**提示（Prompt）**：TH Flash 厂商（vendor）

**说明（Help）**

如果芯片结构体的 `chip_drv` 成员未直接给出芯片厂商，启用此项可支持自动检测 TH 芯片。这样会增加对不同芯片型号的支持，但也会延长检测时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y if !CONFIG_SOC_SERIES_ESP32
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.flash:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.flash#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_SPI_FLASH_SUPPORT_WINBOND_CHIP"></a>

## 277.36 `CONFIG_SPI_FLASH_SUPPORT_WINBOND_CHIP`

**提示（Prompt）**：华邦（Winbond）

**说明（Help）**

如果芯片结构体的 `chip_drv` 成员未直接给出芯片厂商，启用此项可支持自动检测 Winbond（华邦）芯片。这样会增加对不同芯片型号的支持，但也会延长检测时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.flash:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.flash#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="SB_CONFIG_SOC_ESP32"></a>

## 277.37 `SB_CONFIG_SOC_ESP32`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ESP32 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_ESP32
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_YD_ESP32
SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32
SB_CONFIG_BOARD_TTGO_T7V1_5
SB_CONFIG_BOARD_TTGO_TBEAM
SB_CONFIG_BOARD_TTGO_LORA32
SB_CONFIG_BOARD_ESP32_ETHERNET_KIT
SB_CONFIG_BOARD_ESP_WROVER_KIT
SB_CONFIG_BOARD_ESP32_DEVKITC
SB_CONFIG_BOARD_ESP32_CAM
SB_CONFIG_BOARD_INKPLATE_6COLOR
SB_CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1
SB_CONFIG_BOARD_LOLIN32_LITE
SB_CONFIG_BOARD_UDOO_KEY
SB_CONFIG_BOARD_M5STACK_CORE2
SB_CONFIG_BOARD_M5STACK_FIRE
SB_CONFIG_BOARD_M5STICKC_PLUS
SB_CONFIG_BOARD_M5STACK_ATOM_LITE
SB_CONFIG_BOARD_OLIMEX_ESP32_EVB
SB_CONFIG_BOARD_CAN485DBV1
SB_CONFIG_BOARD_KINCONY_KC868_A8
SB_CONFIG_BOARD_KINCONY_KC868_A32
SB_CONFIG_BOARD_ODROID_GO
SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V2
```

**定义位置（Location）**：[`soc/espressif/esp32/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#SB_CONFIG_SOC_SERIES_ESP32)、[`SB_CONFIG_BOARD_YD_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_YD_ESP32)、[`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32)、[`SB_CONFIG_BOARD_TTGO_T7V1_5`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TTGO_T7V1_5)、[`SB_CONFIG_BOARD_TTGO_TBEAM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TTGO_TBEAM)、[`SB_CONFIG_BOARD_TTGO_LORA32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TTGO_LORA32)、[`SB_CONFIG_BOARD_ESP32_ETHERNET_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32_ETHERNET_KIT)、[`SB_CONFIG_BOARD_ESP_WROVER_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP_WROVER_KIT)、[`SB_CONFIG_BOARD_ESP32_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32_DEVKITC)、[`SB_CONFIG_BOARD_ESP32_CAM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32_CAM)、[`SB_CONFIG_BOARD_INKPLATE_6COLOR`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_INKPLATE_6COLOR)、[`SB_CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1)、[`SB_CONFIG_BOARD_LOLIN32_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_LOLIN32_LITE)、[`SB_CONFIG_BOARD_UDOO_KEY`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_UDOO_KEY)、[`SB_CONFIG_BOARD_M5STACK_CORE2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_CORE2)、[`SB_CONFIG_BOARD_M5STACK_FIRE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_FIRE)、[`SB_CONFIG_BOARD_M5STICKC_PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STICKC_PLUS)、[`SB_CONFIG_BOARD_M5STACK_ATOM_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_ATOM_LITE)、[`SB_CONFIG_BOARD_OLIMEX_ESP32_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_OLIMEX_ESP32_EVB)、[`SB_CONFIG_BOARD_CAN485DBV1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_CAN485DBV1)、[`SB_CONFIG_BOARD_KINCONY_KC868_A8`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_KINCONY_KC868_A8)、[`SB_CONFIG_BOARD_KINCONY_KC868_A32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_KINCONY_KC868_A32)、[`SB_CONFIG_BOARD_ODROID_GO`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ODROID_GO)、[`SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_YD_ESP32`、`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32`、`SB_CONFIG_BOARD_TTGO_T7V1_5`、`SB_CONFIG_BOARD_TTGO_TBEAM`、`SB_CONFIG_BOARD_TTGO_LORA32`、`SB_CONFIG_BOARD_ESP32_ETHERNET_KIT`、`SB_CONFIG_BOARD_ESP_WROVER_KIT`、`SB_CONFIG_BOARD_ESP32_DEVKITC`、`SB_CONFIG_BOARD_ESP32_CAM`、`SB_CONFIG_BOARD_INKPLATE_6COLOR`、`SB_CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1`、`SB_CONFIG_BOARD_LOLIN32_LITE`、`SB_CONFIG_BOARD_UDOO_KEY`、`SB_CONFIG_BOARD_M5STACK_CORE2`、`SB_CONFIG_BOARD_M5STACK_FIRE`、`SB_CONFIG_BOARD_M5STICKC_PLUS`、`SB_CONFIG_BOARD_M5STACK_ATOM_LITE`、`SB_CONFIG_BOARD_OLIMEX_ESP32_EVB`、`SB_CONFIG_BOARD_CAN485DBV1`、`SB_CONFIG_BOARD_KINCONY_KC868_A8`、`SB_CONFIG_BOARD_KINCONY_KC868_A32`、`SB_CONFIG_BOARD_ODROID_GO`、`SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V2`。

<a id="SB_CONFIG_SOC_ESP32C3"></a>

## 277.38 `SB_CONFIG_SOC_ESP32C3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ESP32C3 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_ESP32C3
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_BEETLE_ESP32C3
SB_CONFIG_BOARD_WE_ORTHOSIE1EV
SB_CONFIG_BOARD_UEDX24240013_MD50E
SB_CONFIG_BOARD_GLYPH_C3
SB_CONFIG_BOARD_XIAO_ESP32C3
SB_CONFIG_BOARD_TTGO_T8C3
SB_CONFIG_BOARD_TTGO_TOIPLUS
SB_CONFIG_BOARD_ESP32C3_RUST
SB_CONFIG_BOARD_ESP32C3_DEVKITC
SB_CONFIG_BOARD_ESP32C3_DEVKITM
SB_CONFIG_BOARD_ESP32C3_042_OLED
SB_CONFIG_BOARD_ICEV_WIRELESS
SB_CONFIG_BOARD_ESP32C3_SUPERMINI
SB_CONFIG_BOARD_ESP32C3_LCKFB
SB_CONFIG_BOARD_STAMP_C3
SB_CONFIG_BOARD_WEACT_ESP32C3_MINI
SB_CONFIG_BOARD_ESP32C3_LUATOS_CORE
```

**定义位置（Location）**：[`soc/espressif/esp32c3/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c3/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_ESP32C3`](P277_soc_espressif_配置项参考_3.md#SB_CONFIG_SOC_SERIES_ESP32C3)、[`SB_CONFIG_BOARD_BEETLE_ESP32C3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_BEETLE_ESP32C3)、[`SB_CONFIG_BOARD_WE_ORTHOSIE1EV`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_WE_ORTHOSIE1EV)、[`SB_CONFIG_BOARD_UEDX24240013_MD50E`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_UEDX24240013_MD50E)、[`SB_CONFIG_BOARD_GLYPH_C3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_GLYPH_C3)、[`SB_CONFIG_BOARD_XIAO_ESP32C3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_XIAO_ESP32C3)、[`SB_CONFIG_BOARD_TTGO_T8C3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TTGO_T8C3)、[`SB_CONFIG_BOARD_TTGO_TOIPLUS`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TTGO_TOIPLUS)、[`SB_CONFIG_BOARD_ESP32C3_RUST`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32C3_RUST)、[`SB_CONFIG_BOARD_ESP32C3_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32C3_DEVKITC)、[`SB_CONFIG_BOARD_ESP32C3_DEVKITM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32C3_DEVKITM)、[`SB_CONFIG_BOARD_ESP32C3_042_OLED`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32C3_042_OLED)、[`SB_CONFIG_BOARD_ICEV_WIRELESS`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ICEV_WIRELESS)、[`SB_CONFIG_BOARD_ESP32C3_SUPERMINI`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32C3_SUPERMINI)、[`SB_CONFIG_BOARD_ESP32C3_LCKFB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32C3_LCKFB)、[`SB_CONFIG_BOARD_STAMP_C3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_STAMP_C3)、[`SB_CONFIG_BOARD_WEACT_ESP32C3_MINI`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_WEACT_ESP32C3_MINI)、[`SB_CONFIG_BOARD_ESP32C3_LUATOS_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32C3_LUATOS_CORE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_BEETLE_ESP32C3`、`SB_CONFIG_BOARD_WE_ORTHOSIE1EV`、`SB_CONFIG_BOARD_UEDX24240013_MD50E`、`SB_CONFIG_BOARD_GLYPH_C3`、`SB_CONFIG_BOARD_XIAO_ESP32C3`、`SB_CONFIG_BOARD_TTGO_T8C3`、`SB_CONFIG_BOARD_TTGO_TOIPLUS`、`SB_CONFIG_BOARD_ESP32C3_RUST`、`SB_CONFIG_BOARD_ESP32C3_DEVKITC`、`SB_CONFIG_BOARD_ESP32C3_DEVKITM`、`SB_CONFIG_BOARD_ESP32C3_042_OLED`、`SB_CONFIG_BOARD_ICEV_WIRELESS`、`SB_CONFIG_BOARD_ESP32C3_SUPERMINI`、`SB_CONFIG_BOARD_ESP32C3_LCKFB`、`SB_CONFIG_BOARD_STAMP_C3`、`SB_CONFIG_BOARD_WEACT_ESP32C3_MINI`、`SB_CONFIG_BOARD_ESP32C3_LUATOS_CORE`。

<a id="SB_CONFIG_SOC_ESP32C5_HPCORE"></a>

## 277.39 `SB_CONFIG_SOC_ESP32C5_HPCORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为高性能内核（HP CORE）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_XIAO_ESP32C5
SB_CONFIG_BOARD_ESP32C5_DEVKITC
```

**定义位置（Location）**：[`soc/espressif/esp32c5/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c5/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOARD_XIAO_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_XIAO_ESP32C5)、[`SB_CONFIG_BOARD_ESP32C5_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32C5_DEVKITC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_XIAO_ESP32C5`、`SB_CONFIG_BOARD_ESP32C5_DEVKITC`。

<a id="SB_CONFIG_SOC_ESP32C5_LPCORE"></a>

## 277.40 `SB_CONFIG_SOC_ESP32C5_LPCORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为低功耗内核（LP CORE）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_XIAO_ESP32C5
SB_CONFIG_BOARD_ESP32C5_DEVKITC
```

**定义位置（Location）**：[`soc/espressif/esp32c5/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c5/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOARD_XIAO_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_XIAO_ESP32C5)、[`SB_CONFIG_BOARD_ESP32C5_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32C5_DEVKITC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_XIAO_ESP32C5`、`SB_CONFIG_BOARD_ESP32C5_DEVKITC`。

<a id="SB_CONFIG_SOC_ESP32C6_HPCORE"></a>

## 277.41 `SB_CONFIG_SOC_ESP32C6_HPCORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为高性能内核（HP CORE）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_GLYPH_C6
SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32C6
SB_CONFIG_BOARD_XIAO_ESP32C6
SB_CONFIG_BOARD_ARDUINO_NESSO_N1
SB_CONFIG_BOARD_ESP32C6_DEVKITC
SB_CONFIG_BOARD_ESP32C6_LCD_1_47
SB_CONFIG_BOARD_M5STACK_NANOC6
SB_CONFIG_BOARD_M5STACK_UNITC6L
SB_CONFIG_BOARD_WEACT_ESP32C6_MINI
```

**定义位置（Location）**：[`soc/espressif/esp32c6/Kconfig.soc:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c6/Kconfig.soc#L12)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOARD_GLYPH_C6`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_GLYPH_C6)、[`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32C6)、[`SB_CONFIG_BOARD_XIAO_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_XIAO_ESP32C6)、[`SB_CONFIG_BOARD_ARDUINO_NESSO_N1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ARDUINO_NESSO_N1)、[`SB_CONFIG_BOARD_ESP32C6_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32C6_DEVKITC)、[`SB_CONFIG_BOARD_ESP32C6_LCD_1_47`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32C6_LCD_1_47)、[`SB_CONFIG_BOARD_M5STACK_NANOC6`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_NANOC6)、[`SB_CONFIG_BOARD_M5STACK_UNITC6L`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_UNITC6L)、[`SB_CONFIG_BOARD_WEACT_ESP32C6_MINI`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_WEACT_ESP32C6_MINI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_GLYPH_C6`、`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32C6`、`SB_CONFIG_BOARD_XIAO_ESP32C6`、`SB_CONFIG_BOARD_ARDUINO_NESSO_N1`、`SB_CONFIG_BOARD_ESP32C6_DEVKITC`、`SB_CONFIG_BOARD_ESP32C6_LCD_1_47`、`SB_CONFIG_BOARD_M5STACK_NANOC6`、`SB_CONFIG_BOARD_M5STACK_UNITC6L`、`SB_CONFIG_BOARD_WEACT_ESP32C6_MINI`。

<a id="SB_CONFIG_SOC_ESP32C6_LPCORE"></a>

## 277.42 `SB_CONFIG_SOC_ESP32C6_LPCORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为低功耗内核（LP CORE）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_GLYPH_C6
SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32C6
SB_CONFIG_BOARD_XIAO_ESP32C6
SB_CONFIG_BOARD_ARDUINO_NESSO_N1
SB_CONFIG_BOARD_ESP32C6_DEVKITC
SB_CONFIG_BOARD_ESP32C6_LCD_1_47
SB_CONFIG_BOARD_M5STACK_NANOC6
SB_CONFIG_BOARD_M5STACK_UNITC6L
SB_CONFIG_BOARD_WEACT_ESP32C6_MINI
```

**定义位置（Location）**：[`soc/espressif/esp32c6/Kconfig.soc:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c6/Kconfig.soc#L17)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOARD_GLYPH_C6`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_GLYPH_C6)、[`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32C6)、[`SB_CONFIG_BOARD_XIAO_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_XIAO_ESP32C6)、[`SB_CONFIG_BOARD_ARDUINO_NESSO_N1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ARDUINO_NESSO_N1)、[`SB_CONFIG_BOARD_ESP32C6_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32C6_DEVKITC)、[`SB_CONFIG_BOARD_ESP32C6_LCD_1_47`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32C6_LCD_1_47)、[`SB_CONFIG_BOARD_M5STACK_NANOC6`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_NANOC6)、[`SB_CONFIG_BOARD_M5STACK_UNITC6L`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_UNITC6L)、[`SB_CONFIG_BOARD_WEACT_ESP32C6_MINI`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_WEACT_ESP32C6_MINI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_GLYPH_C6`、`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32C6`、`SB_CONFIG_BOARD_XIAO_ESP32C6`、`SB_CONFIG_BOARD_ARDUINO_NESSO_N1`、`SB_CONFIG_BOARD_ESP32C6_DEVKITC`、`SB_CONFIG_BOARD_ESP32C6_LCD_1_47`、`SB_CONFIG_BOARD_M5STACK_NANOC6`、`SB_CONFIG_BOARD_M5STACK_UNITC6L`、`SB_CONFIG_BOARD_WEACT_ESP32C6_MINI`。

<a id="SB_CONFIG_SOC_ESP32P4_HPCORE"></a>

## 277.43 `SB_CONFIG_SOC_ESP32P4_HPCORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为高性能内核（HP CORE）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_ESP32P4
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ESP32P4X_FUNCTION_EV_BOARD
SB_CONFIG_BOARD_ESP32P4_FUNCTION_EV_BOARD
SB_CONFIG_BOARD_WAVESHARE_ESP32P4_ETH
SB_CONFIG_BOARD_ESP32P4_WIFI6_DEV_KIT
SB_CONFIG_BOARD_ESP32P4_WIFI6
SB_CONFIG_BOARD_ESP32P4_PC
```

**定义位置（Location）**：[`soc/espressif/esp32p4/Kconfig.soc:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32p4/Kconfig.soc#L40)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ESP32P4)、[`SB_CONFIG_BOARD_ESP32P4X_FUNCTION_EV_BOARD`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32P4X_FUNCTION_EV_BOARD)、[`SB_CONFIG_BOARD_ESP32P4_FUNCTION_EV_BOARD`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32P4_FUNCTION_EV_BOARD)、[`SB_CONFIG_BOARD_WAVESHARE_ESP32P4_ETH`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_WAVESHARE_ESP32P4_ETH)、[`SB_CONFIG_BOARD_ESP32P4_WIFI6_DEV_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32P4_WIFI6_DEV_KIT)、[`SB_CONFIG_BOARD_ESP32P4_WIFI6`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32P4_WIFI6)、[`SB_CONFIG_BOARD_ESP32P4_PC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32P4_PC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_ESP32P4`、`SB_CONFIG_BOARD_ESP32P4X_FUNCTION_EV_BOARD`、`SB_CONFIG_BOARD_ESP32P4_FUNCTION_EV_BOARD`、`SB_CONFIG_BOARD_WAVESHARE_ESP32P4_ETH`、`SB_CONFIG_BOARD_ESP32P4_WIFI6_DEV_KIT`、`SB_CONFIG_BOARD_ESP32P4_WIFI6`、`SB_CONFIG_BOARD_ESP32P4_PC`。

<a id="SB_CONFIG_SOC_ESP32P4_LPCORE"></a>

## 277.44 `SB_CONFIG_SOC_ESP32P4_LPCORE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为低功耗内核（LP CORE）。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_ESP32P4
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ESP32P4X_FUNCTION_EV_BOARD
SB_CONFIG_BOARD_ESP32P4_FUNCTION_EV_BOARD
SB_CONFIG_BOARD_WAVESHARE_ESP32P4_ETH
SB_CONFIG_BOARD_ESP32P4_WIFI6_DEV_KIT
SB_CONFIG_BOARD_ESP32P4_WIFI6
SB_CONFIG_BOARD_ESP32P4_PC
```

**定义位置（Location）**：[`soc/espressif/esp32p4/Kconfig.soc:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32p4/Kconfig.soc#L46)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_ESP32P4)、[`SB_CONFIG_BOARD_ESP32P4X_FUNCTION_EV_BOARD`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32P4X_FUNCTION_EV_BOARD)、[`SB_CONFIG_BOARD_ESP32P4_FUNCTION_EV_BOARD`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32P4_FUNCTION_EV_BOARD)、[`SB_CONFIG_BOARD_WAVESHARE_ESP32P4_ETH`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_WAVESHARE_ESP32P4_ETH)、[`SB_CONFIG_BOARD_ESP32P4_WIFI6_DEV_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32P4_WIFI6_DEV_KIT)、[`SB_CONFIG_BOARD_ESP32P4_WIFI6`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32P4_WIFI6)、[`SB_CONFIG_BOARD_ESP32P4_PC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32P4_PC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_ESP32P4`、`SB_CONFIG_BOARD_ESP32P4X_FUNCTION_EV_BOARD`、`SB_CONFIG_BOARD_ESP32P4_FUNCTION_EV_BOARD`、`SB_CONFIG_BOARD_WAVESHARE_ESP32P4_ETH`、`SB_CONFIG_BOARD_ESP32P4_WIFI6_DEV_KIT`、`SB_CONFIG_BOARD_ESP32P4_WIFI6`、`SB_CONFIG_BOARD_ESP32P4_PC`。

<a id="SB_CONFIG_SOC_ESP32S2"></a>

## 277.45 `SB_CONFIG_SOC_ESP32S2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ESP32S2 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_ESP32S2
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2
SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2_TFT
SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2_TFT_REVERSE
SB_CONFIG_BOARD_ESP32S2_DEVKITC
SB_CONFIG_BOARD_ESP32S2_SAOLA
SB_CONFIG_BOARD_ESP32S2_LOLIN_MINI
SB_CONFIG_BOARD_ESP32S2_FRANZININHO
```

**定义位置（Location）**：[`soc/espressif/esp32s2/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s2/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#SB_CONFIG_SOC_SERIES_ESP32S2)、[`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2)、[`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2_TFT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2_TFT)、[`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2_TFT_REVERSE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2_TFT_REVERSE)、[`SB_CONFIG_BOARD_ESP32S2_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S2_DEVKITC)、[`SB_CONFIG_BOARD_ESP32S2_SAOLA`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S2_SAOLA)、[`SB_CONFIG_BOARD_ESP32S2_LOLIN_MINI`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S2_LOLIN_MINI)、[`SB_CONFIG_BOARD_ESP32S2_FRANZININHO`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S2_FRANZININHO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2`、`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2_TFT`、`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S2_TFT_REVERSE`、`SB_CONFIG_BOARD_ESP32S2_DEVKITC`、`SB_CONFIG_BOARD_ESP32S2_SAOLA`、`SB_CONFIG_BOARD_ESP32S2_LOLIN_MINI`、`SB_CONFIG_BOARD_ESP32S2_FRANZININHO`。

<a id="SB_CONFIG_SOC_ESP32S3"></a>

## 277.46 `SB_CONFIG_SOC_ESP32S3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ESP32S3 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_SERIES_ESP32S3
```

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MATOUCH_MTRO128G
SB_CONFIG_BOARD_UEDX24320028E_WB_A
SB_CONFIG_BOARD_UEDX32480035E_WB_A
SB_CONFIG_BOARD_DNESP32S3B
SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3
SB_CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3
SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE
SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT
SB_CONFIG_BOARD_RETERMINAL_E1001
SB_CONFIG_BOARD_XIAO_ESP32S3
SB_CONFIG_BOARD_RETERMINAL_E1003
SB_CONFIG_BOARD_RETERMINAL_E1002
SB_CONFIG_BOARD_EORA_HUB_900TB
SB_CONFIG_BOARD_TWATCH_S3
SB_CONFIG_BOARD_TDONGLE_S3
SB_CONFIG_BOARD_TTGO_T8S3
SB_CONFIG_BOARD_T_DECK
SB_CONFIG_BOARD_ESP32S3_BOX3
SB_CONFIG_BOARD_ESP_THREADBR
SB_CONFIG_BOARD_ESP32S3_DEVKITC
SB_CONFIG_BOARD_ESP32S3_EYE
SB_CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28
SB_CONFIG_BOARD_ESP32S3_GEEK
SB_CONFIG_BOARD_ESP32S3_MATRIX
SB_CONFIG_BOARD_ESP32S3_RLCD_4_2
SB_CONFIG_BOARD_WALTER
SB_CONFIG_BOARD_SHRIKE_FI
SB_CONFIG_BOARD_RAK3112
SB_CONFIG_BOARD_M5STACK_ATOMS3_LITE
SB_CONFIG_BOARD_M5STACK_CORES3
SB_CONFIG_BOARD_M5STACK_STAMPS3
SB_CONFIG_BOARD_M5STACK_ATOMS3
SB_CONFIG_BOARD_M5STACK_STACKCHAN
SB_CONFIG_BOARD_M5STACK_PAPER_COLOR
SB_CONFIG_BOARD_M5STACK_STICKS3
SB_CONFIG_BOARD_WEACT_ESP32S3_MINI
SB_CONFIG_BOARD_WEACT_ESP32S3_B
SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V3
SB_CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3
SB_CONFIG_BOARD_HELTEC_WIRELESS_TRACKER
SB_CONFIG_BOARD_ESP32S3_LUATOS_CORE
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig.soc:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig.soc#L10)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#SB_CONFIG_SOC_SERIES_ESP32S3)、[`SB_CONFIG_BOARD_MATOUCH_MTRO128G`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MATOUCH_MTRO128G)、[`SB_CONFIG_BOARD_UEDX24320028E_WB_A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_UEDX24320028E_WB_A)、[`SB_CONFIG_BOARD_UEDX32480035E_WB_A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_UEDX32480035E_WB_A)、[`SB_CONFIG_BOARD_DNESP32S3B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_DNESP32S3B)、[`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3)、[`SB_CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3)、[`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE)、[`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT)、[`SB_CONFIG_BOARD_RETERMINAL_E1001`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RETERMINAL_E1001)、[`SB_CONFIG_BOARD_XIAO_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_XIAO_ESP32S3)、[`SB_CONFIG_BOARD_RETERMINAL_E1003`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RETERMINAL_E1003)、[`SB_CONFIG_BOARD_RETERMINAL_E1002`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RETERMINAL_E1002)、[`SB_CONFIG_BOARD_EORA_HUB_900TB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EORA_HUB_900TB)、[`SB_CONFIG_BOARD_TWATCH_S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TWATCH_S3)、[`SB_CONFIG_BOARD_TDONGLE_S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TDONGLE_S3)、[`SB_CONFIG_BOARD_TTGO_T8S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TTGO_T8S3)、[`SB_CONFIG_BOARD_T_DECK`](P045_boards_lilygo_配置项参考.md#SB_CONFIG_BOARD_T_DECK)、[`SB_CONFIG_BOARD_ESP32S3_BOX3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_BOX3)、[`SB_CONFIG_BOARD_ESP_THREADBR`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP_THREADBR)、[`SB_CONFIG_BOARD_ESP32S3_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_DEVKITC)、[`SB_CONFIG_BOARD_ESP32S3_EYE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_EYE)、[`SB_CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28)、[`SB_CONFIG_BOARD_ESP32S3_GEEK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_GEEK)、[`SB_CONFIG_BOARD_ESP32S3_MATRIX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_MATRIX)、[`SB_CONFIG_BOARD_ESP32S3_RLCD_4_2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_RLCD_4_2)、[`SB_CONFIG_BOARD_WALTER`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_WALTER)、[`SB_CONFIG_BOARD_SHRIKE_FI`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_SHRIKE_FI)、[`SB_CONFIG_BOARD_RAK3112`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RAK3112)、[`SB_CONFIG_BOARD_M5STACK_ATOMS3_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_ATOMS3_LITE)、[`SB_CONFIG_BOARD_M5STACK_CORES3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_CORES3)、[`SB_CONFIG_BOARD_M5STACK_STAMPS3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_STAMPS3)、[`SB_CONFIG_BOARD_M5STACK_ATOMS3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_ATOMS3)、[`SB_CONFIG_BOARD_M5STACK_STACKCHAN`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_STACKCHAN)、[`SB_CONFIG_BOARD_M5STACK_PAPER_COLOR`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_PAPER_COLOR)、[`SB_CONFIG_BOARD_M5STACK_STICKS3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_STICKS3)、[`SB_CONFIG_BOARD_WEACT_ESP32S3_MINI`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_WEACT_ESP32S3_MINI)、[`SB_CONFIG_BOARD_WEACT_ESP32S3_B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_WEACT_ESP32S3_B)、[`SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V3)、[`SB_CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3)、[`SB_CONFIG_BOARD_HELTEC_WIRELESS_TRACKER`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_HELTEC_WIRELESS_TRACKER)、[`SB_CONFIG_BOARD_ESP32S3_LUATOS_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_LUATOS_CORE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_MATOUCH_MTRO128G`、`SB_CONFIG_BOARD_UEDX24320028E_WB_A`、`SB_CONFIG_BOARD_UEDX32480035E_WB_A`、`SB_CONFIG_BOARD_DNESP32S3B`、`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3`、`SB_CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3`、`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE`、`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT`、`SB_CONFIG_BOARD_RETERMINAL_E1001`、`SB_CONFIG_BOARD_XIAO_ESP32S3`、`SB_CONFIG_BOARD_RETERMINAL_E1003`、`SB_CONFIG_BOARD_RETERMINAL_E1002`、`SB_CONFIG_BOARD_EORA_HUB_900TB`、`SB_CONFIG_BOARD_TWATCH_S3`、`SB_CONFIG_BOARD_TDONGLE_S3`、`SB_CONFIG_BOARD_TTGO_T8S3`、`SB_CONFIG_BOARD_ESP32S3_BOX3`、`SB_CONFIG_BOARD_ESP_THREADBR`、`SB_CONFIG_BOARD_ESP32S3_DEVKITC`、`SB_CONFIG_BOARD_ESP32S3_EYE`、`SB_CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28`、`SB_CONFIG_BOARD_ESP32S3_GEEK`、`SB_CONFIG_BOARD_ESP32S3_MATRIX`、`SB_CONFIG_BOARD_ESP32S3_RLCD_4_2`、`SB_CONFIG_BOARD_WALTER`、`SB_CONFIG_BOARD_SHRIKE_FI`、`SB_CONFIG_BOARD_RAK3112`、`SB_CONFIG_BOARD_M5STACK_ATOMS3_LITE`、`SB_CONFIG_BOARD_M5STACK_CORES3`、`SB_CONFIG_BOARD_M5STACK_STAMPS3`、`SB_CONFIG_BOARD_M5STACK_ATOMS3`、`SB_CONFIG_BOARD_M5STACK_STACKCHAN`、`SB_CONFIG_BOARD_M5STACK_PAPER_COLOR`、`SB_CONFIG_BOARD_M5STACK_STICKS3`、`SB_CONFIG_BOARD_WEACT_ESP32S3_MINI`、`SB_CONFIG_BOARD_WEACT_ESP32S3_B`、`SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V3`、`SB_CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3`、`SB_CONFIG_BOARD_HELTEC_WIRELESS_TRACKER`、`SB_CONFIG_BOARD_ESP32S3_LUATOS_CORE`。

<a id="SB_CONFIG_SOC_ESP32S3_APPCPU"></a>

## 277.47 `SB_CONFIG_SOC_ESP32S3_APPCPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为应用 CPU（APPCPU，内核 1）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MATOUCH_MTRO128G
SB_CONFIG_BOARD_UEDX24320028E_WB_A
SB_CONFIG_BOARD_UEDX32480035E_WB_A
SB_CONFIG_BOARD_DNESP32S3B
SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3
SB_CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3
SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE
SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT
SB_CONFIG_BOARD_RETERMINAL_E1001
SB_CONFIG_BOARD_XIAO_ESP32S3
SB_CONFIG_BOARD_RETERMINAL_E1003
SB_CONFIG_BOARD_RETERMINAL_E1002
SB_CONFIG_BOARD_EORA_HUB_900TB
SB_CONFIG_BOARD_TWATCH_S3
SB_CONFIG_BOARD_TDONGLE_S3
SB_CONFIG_BOARD_TTGO_T8S3
SB_CONFIG_BOARD_T_DECK
SB_CONFIG_BOARD_ESP32S3_BOX3
SB_CONFIG_BOARD_ESP_THREADBR
SB_CONFIG_BOARD_ESP32S3_DEVKITC
SB_CONFIG_BOARD_ESP32S3_EYE
SB_CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28
SB_CONFIG_BOARD_ESP32S3_GEEK
SB_CONFIG_BOARD_ESP32S3_MATRIX
SB_CONFIG_BOARD_ESP32S3_RLCD_4_2
SB_CONFIG_BOARD_WALTER
SB_CONFIG_BOARD_SHRIKE_FI
SB_CONFIG_BOARD_RAK3112
SB_CONFIG_BOARD_M5STACK_ATOMS3_LITE
SB_CONFIG_BOARD_M5STACK_CORES3
SB_CONFIG_BOARD_M5STACK_STAMPS3
SB_CONFIG_BOARD_M5STACK_ATOMS3
SB_CONFIG_BOARD_M5STACK_STACKCHAN
SB_CONFIG_BOARD_M5STACK_PAPER_COLOR
SB_CONFIG_BOARD_M5STACK_STICKS3
SB_CONFIG_BOARD_WEACT_ESP32S3_MINI
SB_CONFIG_BOARD_WEACT_ESP32S3_B
SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V3
SB_CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3
SB_CONFIG_BOARD_HELTEC_WIRELESS_TRACKER
SB_CONFIG_BOARD_ESP32S3_LUATOS_CORE
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig.soc:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig.soc#L21)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOARD_MATOUCH_MTRO128G`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MATOUCH_MTRO128G)、[`SB_CONFIG_BOARD_UEDX24320028E_WB_A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_UEDX24320028E_WB_A)、[`SB_CONFIG_BOARD_UEDX32480035E_WB_A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_UEDX32480035E_WB_A)、[`SB_CONFIG_BOARD_DNESP32S3B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_DNESP32S3B)、[`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3)、[`SB_CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3)、[`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE)、[`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT)、[`SB_CONFIG_BOARD_RETERMINAL_E1001`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RETERMINAL_E1001)、[`SB_CONFIG_BOARD_XIAO_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_XIAO_ESP32S3)、[`SB_CONFIG_BOARD_RETERMINAL_E1003`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RETERMINAL_E1003)、[`SB_CONFIG_BOARD_RETERMINAL_E1002`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RETERMINAL_E1002)、[`SB_CONFIG_BOARD_EORA_HUB_900TB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EORA_HUB_900TB)、[`SB_CONFIG_BOARD_TWATCH_S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TWATCH_S3)、[`SB_CONFIG_BOARD_TDONGLE_S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TDONGLE_S3)、[`SB_CONFIG_BOARD_TTGO_T8S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TTGO_T8S3)、[`SB_CONFIG_BOARD_T_DECK`](P045_boards_lilygo_配置项参考.md#SB_CONFIG_BOARD_T_DECK)、[`SB_CONFIG_BOARD_ESP32S3_BOX3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_BOX3)、[`SB_CONFIG_BOARD_ESP_THREADBR`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP_THREADBR)、[`SB_CONFIG_BOARD_ESP32S3_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_DEVKITC)、[`SB_CONFIG_BOARD_ESP32S3_EYE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_EYE)、[`SB_CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28)、[`SB_CONFIG_BOARD_ESP32S3_GEEK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_GEEK)、[`SB_CONFIG_BOARD_ESP32S3_MATRIX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_MATRIX)、[`SB_CONFIG_BOARD_ESP32S3_RLCD_4_2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_RLCD_4_2)、[`SB_CONFIG_BOARD_WALTER`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_WALTER)、[`SB_CONFIG_BOARD_SHRIKE_FI`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_SHRIKE_FI)、[`SB_CONFIG_BOARD_RAK3112`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RAK3112)、[`SB_CONFIG_BOARD_M5STACK_ATOMS3_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_ATOMS3_LITE)、[`SB_CONFIG_BOARD_M5STACK_CORES3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_CORES3)、[`SB_CONFIG_BOARD_M5STACK_STAMPS3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_STAMPS3)、[`SB_CONFIG_BOARD_M5STACK_ATOMS3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_ATOMS3)、[`SB_CONFIG_BOARD_M5STACK_STACKCHAN`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_STACKCHAN)、[`SB_CONFIG_BOARD_M5STACK_PAPER_COLOR`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_PAPER_COLOR)、[`SB_CONFIG_BOARD_M5STACK_STICKS3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_STICKS3)、[`SB_CONFIG_BOARD_WEACT_ESP32S3_MINI`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_WEACT_ESP32S3_MINI)、[`SB_CONFIG_BOARD_WEACT_ESP32S3_B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_WEACT_ESP32S3_B)、[`SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V3)、[`SB_CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3)、[`SB_CONFIG_BOARD_HELTEC_WIRELESS_TRACKER`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_HELTEC_WIRELESS_TRACKER)、[`SB_CONFIG_BOARD_ESP32S3_LUATOS_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_LUATOS_CORE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_MATOUCH_MTRO128G`、`SB_CONFIG_BOARD_UEDX24320028E_WB_A`、`SB_CONFIG_BOARD_UEDX32480035E_WB_A`、`SB_CONFIG_BOARD_DNESP32S3B`、`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3`、`SB_CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3`、`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE`、`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT`、`SB_CONFIG_BOARD_RETERMINAL_E1001`、`SB_CONFIG_BOARD_XIAO_ESP32S3`、`SB_CONFIG_BOARD_RETERMINAL_E1003`、`SB_CONFIG_BOARD_RETERMINAL_E1002`、`SB_CONFIG_BOARD_EORA_HUB_900TB`、`SB_CONFIG_BOARD_TWATCH_S3`、`SB_CONFIG_BOARD_TDONGLE_S3`、`SB_CONFIG_BOARD_TTGO_T8S3`、`SB_CONFIG_BOARD_ESP32S3_BOX3`、`SB_CONFIG_BOARD_ESP_THREADBR`、`SB_CONFIG_BOARD_ESP32S3_DEVKITC`、`SB_CONFIG_BOARD_ESP32S3_EYE`、`SB_CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28`、`SB_CONFIG_BOARD_ESP32S3_GEEK`、`SB_CONFIG_BOARD_ESP32S3_MATRIX`、`SB_CONFIG_BOARD_ESP32S3_RLCD_4_2`、`SB_CONFIG_BOARD_WALTER`、`SB_CONFIG_BOARD_SHRIKE_FI`、`SB_CONFIG_BOARD_RAK3112`、`SB_CONFIG_BOARD_M5STACK_ATOMS3_LITE`、`SB_CONFIG_BOARD_M5STACK_CORES3`、`SB_CONFIG_BOARD_M5STACK_STAMPS3`、`SB_CONFIG_BOARD_M5STACK_ATOMS3`、`SB_CONFIG_BOARD_M5STACK_STACKCHAN`、`SB_CONFIG_BOARD_M5STACK_PAPER_COLOR`、`SB_CONFIG_BOARD_M5STACK_STICKS3`、`SB_CONFIG_BOARD_WEACT_ESP32S3_MINI`、`SB_CONFIG_BOARD_WEACT_ESP32S3_B`、`SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V3`、`SB_CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3`、`SB_CONFIG_BOARD_HELTEC_WIRELESS_TRACKER`、`SB_CONFIG_BOARD_ESP32S3_LUATOS_CORE`。

<a id="SB_CONFIG_SOC_ESP32S3_PROCPU"></a>

## 277.48 `SB_CONFIG_SOC_ESP32S3_PROCPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为协议 CPU（PROCPU，内核 0）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_MATOUCH_MTRO128G
SB_CONFIG_BOARD_UEDX24320028E_WB_A
SB_CONFIG_BOARD_UEDX32480035E_WB_A
SB_CONFIG_BOARD_DNESP32S3B
SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3
SB_CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3
SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE
SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT
SB_CONFIG_BOARD_RETERMINAL_E1001
SB_CONFIG_BOARD_XIAO_ESP32S3
SB_CONFIG_BOARD_RETERMINAL_E1003
SB_CONFIG_BOARD_RETERMINAL_E1002
SB_CONFIG_BOARD_EORA_HUB_900TB
SB_CONFIG_BOARD_TWATCH_S3
SB_CONFIG_BOARD_TDONGLE_S3
SB_CONFIG_BOARD_TTGO_T8S3
SB_CONFIG_BOARD_T_DECK
SB_CONFIG_BOARD_ESP32S3_BOX3
SB_CONFIG_BOARD_ESP_THREADBR
SB_CONFIG_BOARD_ESP32S3_DEVKITC
SB_CONFIG_BOARD_ESP32S3_EYE
SB_CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28
SB_CONFIG_BOARD_ESP32S3_GEEK
SB_CONFIG_BOARD_ESP32S3_MATRIX
SB_CONFIG_BOARD_ESP32S3_RLCD_4_2
SB_CONFIG_BOARD_WALTER
SB_CONFIG_BOARD_SHRIKE_FI
SB_CONFIG_BOARD_RAK3112
SB_CONFIG_BOARD_M5STACK_ATOMS3_LITE
SB_CONFIG_BOARD_M5STACK_CORES3
SB_CONFIG_BOARD_M5STACK_STAMPS3
SB_CONFIG_BOARD_M5STACK_ATOMS3
SB_CONFIG_BOARD_M5STACK_STACKCHAN
SB_CONFIG_BOARD_M5STACK_PAPER_COLOR
SB_CONFIG_BOARD_M5STACK_STICKS3
SB_CONFIG_BOARD_WEACT_ESP32S3_MINI
SB_CONFIG_BOARD_WEACT_ESP32S3_B
SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V3
SB_CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3
SB_CONFIG_BOARD_HELTEC_WIRELESS_TRACKER
SB_CONFIG_BOARD_ESP32S3_LUATOS_CORE
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOARD_MATOUCH_MTRO128G`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_MATOUCH_MTRO128G)、[`SB_CONFIG_BOARD_UEDX24320028E_WB_A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_UEDX24320028E_WB_A)、[`SB_CONFIG_BOARD_UEDX32480035E_WB_A`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_UEDX32480035E_WB_A)、[`SB_CONFIG_BOARD_DNESP32S3B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_DNESP32S3B)、[`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3)、[`SB_CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3)、[`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE)、[`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT)、[`SB_CONFIG_BOARD_RETERMINAL_E1001`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RETERMINAL_E1001)、[`SB_CONFIG_BOARD_XIAO_ESP32S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_XIAO_ESP32S3)、[`SB_CONFIG_BOARD_RETERMINAL_E1003`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RETERMINAL_E1003)、[`SB_CONFIG_BOARD_RETERMINAL_E1002`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RETERMINAL_E1002)、[`SB_CONFIG_BOARD_EORA_HUB_900TB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_EORA_HUB_900TB)、[`SB_CONFIG_BOARD_TWATCH_S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TWATCH_S3)、[`SB_CONFIG_BOARD_TDONGLE_S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TDONGLE_S3)、[`SB_CONFIG_BOARD_TTGO_T8S3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TTGO_T8S3)、[`SB_CONFIG_BOARD_T_DECK`](P045_boards_lilygo_配置项参考.md#SB_CONFIG_BOARD_T_DECK)、[`SB_CONFIG_BOARD_ESP32S3_BOX3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_BOX3)、[`SB_CONFIG_BOARD_ESP_THREADBR`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP_THREADBR)、[`SB_CONFIG_BOARD_ESP32S3_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_DEVKITC)、[`SB_CONFIG_BOARD_ESP32S3_EYE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_EYE)、[`SB_CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28)、[`SB_CONFIG_BOARD_ESP32S3_GEEK`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_GEEK)、[`SB_CONFIG_BOARD_ESP32S3_MATRIX`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_MATRIX)、[`SB_CONFIG_BOARD_ESP32S3_RLCD_4_2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_RLCD_4_2)、[`SB_CONFIG_BOARD_WALTER`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_WALTER)、[`SB_CONFIG_BOARD_SHRIKE_FI`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_SHRIKE_FI)、[`SB_CONFIG_BOARD_RAK3112`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_RAK3112)、[`SB_CONFIG_BOARD_M5STACK_ATOMS3_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_ATOMS3_LITE)、[`SB_CONFIG_BOARD_M5STACK_CORES3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_CORES3)、[`SB_CONFIG_BOARD_M5STACK_STAMPS3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_STAMPS3)、[`SB_CONFIG_BOARD_M5STACK_ATOMS3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_ATOMS3)、[`SB_CONFIG_BOARD_M5STACK_STACKCHAN`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_STACKCHAN)、[`SB_CONFIG_BOARD_M5STACK_PAPER_COLOR`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_PAPER_COLOR)、[`SB_CONFIG_BOARD_M5STACK_STICKS3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_STICKS3)、[`SB_CONFIG_BOARD_WEACT_ESP32S3_MINI`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_WEACT_ESP32S3_MINI)、[`SB_CONFIG_BOARD_WEACT_ESP32S3_B`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_WEACT_ESP32S3_B)、[`SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V3)、[`SB_CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3)、[`SB_CONFIG_BOARD_HELTEC_WIRELESS_TRACKER`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_HELTEC_WIRELESS_TRACKER)、[`SB_CONFIG_BOARD_ESP32S3_LUATOS_CORE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32S3_LUATOS_CORE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_MATOUCH_MTRO128G`、`SB_CONFIG_BOARD_UEDX24320028E_WB_A`、`SB_CONFIG_BOARD_UEDX32480035E_WB_A`、`SB_CONFIG_BOARD_DNESP32S3B`、`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3`、`SB_CONFIG_BOARD_ADAFRUIT_QT_PY_ESP32S3`、`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT_REVERSE`、`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32S3_TFT`、`SB_CONFIG_BOARD_RETERMINAL_E1001`、`SB_CONFIG_BOARD_XIAO_ESP32S3`、`SB_CONFIG_BOARD_RETERMINAL_E1003`、`SB_CONFIG_BOARD_RETERMINAL_E1002`、`SB_CONFIG_BOARD_EORA_HUB_900TB`、`SB_CONFIG_BOARD_TWATCH_S3`、`SB_CONFIG_BOARD_TDONGLE_S3`、`SB_CONFIG_BOARD_TTGO_T8S3`、`SB_CONFIG_BOARD_ESP32S3_BOX3`、`SB_CONFIG_BOARD_ESP_THREADBR`、`SB_CONFIG_BOARD_ESP32S3_DEVKITC`、`SB_CONFIG_BOARD_ESP32S3_EYE`、`SB_CONFIG_BOARD_ESP32S3_TOUCH_LCD_1_28`、`SB_CONFIG_BOARD_ESP32S3_GEEK`、`SB_CONFIG_BOARD_ESP32S3_MATRIX`、`SB_CONFIG_BOARD_ESP32S3_RLCD_4_2`、`SB_CONFIG_BOARD_WALTER`、`SB_CONFIG_BOARD_SHRIKE_FI`、`SB_CONFIG_BOARD_RAK3112`、`SB_CONFIG_BOARD_M5STACK_ATOMS3_LITE`、`SB_CONFIG_BOARD_M5STACK_CORES3`、`SB_CONFIG_BOARD_M5STACK_STAMPS3`、`SB_CONFIG_BOARD_M5STACK_ATOMS3`、`SB_CONFIG_BOARD_M5STACK_STACKCHAN`、`SB_CONFIG_BOARD_M5STACK_PAPER_COLOR`、`SB_CONFIG_BOARD_M5STACK_STICKS3`、`SB_CONFIG_BOARD_WEACT_ESP32S3_MINI`、`SB_CONFIG_BOARD_WEACT_ESP32S3_B`、`SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V3`、`SB_CONFIG_BOARD_HELTEC_WIRELESS_STICK_LITE_V3`、`SB_CONFIG_BOARD_HELTEC_WIRELESS_TRACKER`、`SB_CONFIG_BOARD_ESP32S3_LUATOS_CORE`。

<a id="SB_CONFIG_SOC_ESP32_APPCPU"></a>

## 277.49 `SB_CONFIG_SOC_ESP32_APPCPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为应用 CPU（APPCPU，内核 1）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_YD_ESP32
SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32
SB_CONFIG_BOARD_TTGO_T7V1_5
SB_CONFIG_BOARD_TTGO_TBEAM
SB_CONFIG_BOARD_TTGO_LORA32
SB_CONFIG_BOARD_ESP32_ETHERNET_KIT
SB_CONFIG_BOARD_ESP_WROVER_KIT
SB_CONFIG_BOARD_ESP32_DEVKITC
SB_CONFIG_BOARD_ESP32_CAM
SB_CONFIG_BOARD_INKPLATE_6COLOR
SB_CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1
SB_CONFIG_BOARD_LOLIN32_LITE
SB_CONFIG_BOARD_UDOO_KEY
SB_CONFIG_BOARD_M5STACK_CORE2
SB_CONFIG_BOARD_M5STACK_FIRE
SB_CONFIG_BOARD_M5STICKC_PLUS
SB_CONFIG_BOARD_M5STACK_ATOM_LITE
SB_CONFIG_BOARD_OLIMEX_ESP32_EVB
SB_CONFIG_BOARD_CAN485DBV1
SB_CONFIG_BOARD_KINCONY_KC868_A8
SB_CONFIG_BOARD_KINCONY_KC868_A32
SB_CONFIG_BOARD_ODROID_GO
SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V2
```

**定义位置（Location）**：[`soc/espressif/esp32/Kconfig.soc:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32/Kconfig.soc#L21)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOARD_YD_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_YD_ESP32)、[`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32)、[`SB_CONFIG_BOARD_TTGO_T7V1_5`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TTGO_T7V1_5)、[`SB_CONFIG_BOARD_TTGO_TBEAM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TTGO_TBEAM)、[`SB_CONFIG_BOARD_TTGO_LORA32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TTGO_LORA32)、[`SB_CONFIG_BOARD_ESP32_ETHERNET_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32_ETHERNET_KIT)、[`SB_CONFIG_BOARD_ESP_WROVER_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP_WROVER_KIT)、[`SB_CONFIG_BOARD_ESP32_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32_DEVKITC)、[`SB_CONFIG_BOARD_ESP32_CAM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32_CAM)、[`SB_CONFIG_BOARD_INKPLATE_6COLOR`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_INKPLATE_6COLOR)、[`SB_CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1)、[`SB_CONFIG_BOARD_LOLIN32_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_LOLIN32_LITE)、[`SB_CONFIG_BOARD_UDOO_KEY`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_UDOO_KEY)、[`SB_CONFIG_BOARD_M5STACK_CORE2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_CORE2)、[`SB_CONFIG_BOARD_M5STACK_FIRE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_FIRE)、[`SB_CONFIG_BOARD_M5STICKC_PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STICKC_PLUS)、[`SB_CONFIG_BOARD_M5STACK_ATOM_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_ATOM_LITE)、[`SB_CONFIG_BOARD_OLIMEX_ESP32_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_OLIMEX_ESP32_EVB)、[`SB_CONFIG_BOARD_CAN485DBV1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_CAN485DBV1)、[`SB_CONFIG_BOARD_KINCONY_KC868_A8`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_KINCONY_KC868_A8)、[`SB_CONFIG_BOARD_KINCONY_KC868_A32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_KINCONY_KC868_A32)、[`SB_CONFIG_BOARD_ODROID_GO`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ODROID_GO)、[`SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_YD_ESP32`、`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32`、`SB_CONFIG_BOARD_TTGO_T7V1_5`、`SB_CONFIG_BOARD_TTGO_TBEAM`、`SB_CONFIG_BOARD_TTGO_LORA32`、`SB_CONFIG_BOARD_ESP32_ETHERNET_KIT`、`SB_CONFIG_BOARD_ESP_WROVER_KIT`、`SB_CONFIG_BOARD_ESP32_DEVKITC`、`SB_CONFIG_BOARD_ESP32_CAM`、`SB_CONFIG_BOARD_INKPLATE_6COLOR`、`SB_CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1`、`SB_CONFIG_BOARD_LOLIN32_LITE`、`SB_CONFIG_BOARD_UDOO_KEY`、`SB_CONFIG_BOARD_M5STACK_CORE2`、`SB_CONFIG_BOARD_M5STACK_FIRE`、`SB_CONFIG_BOARD_M5STICKC_PLUS`、`SB_CONFIG_BOARD_M5STACK_ATOM_LITE`、`SB_CONFIG_BOARD_OLIMEX_ESP32_EVB`、`SB_CONFIG_BOARD_CAN485DBV1`、`SB_CONFIG_BOARD_KINCONY_KC868_A8`、`SB_CONFIG_BOARD_KINCONY_KC868_A32`、`SB_CONFIG_BOARD_ODROID_GO`、`SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V2`。

<a id="SB_CONFIG_SOC_ESP32_PROCPU"></a>

## 277.50 `SB_CONFIG_SOC_ESP32_PROCPU`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏配置表示构建目标为协议 CPU（PROCPU，内核 0）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_BOARD_YD_ESP32
SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32
SB_CONFIG_BOARD_TTGO_T7V1_5
SB_CONFIG_BOARD_TTGO_TBEAM
SB_CONFIG_BOARD_TTGO_LORA32
SB_CONFIG_BOARD_ESP32_ETHERNET_KIT
SB_CONFIG_BOARD_ESP_WROVER_KIT
SB_CONFIG_BOARD_ESP32_DEVKITC
SB_CONFIG_BOARD_ESP32_DEVKITC
SB_CONFIG_BOARD_ESP32_CAM
SB_CONFIG_BOARD_INKPLATE_6COLOR
SB_CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1
SB_CONFIG_BOARD_LOLIN32_LITE
SB_CONFIG_BOARD_UDOO_KEY
SB_CONFIG_BOARD_M5STACK_CORE2
SB_CONFIG_BOARD_M5STACK_FIRE
SB_CONFIG_BOARD_M5STICKC_PLUS
SB_CONFIG_BOARD_M5STACK_ATOM_LITE
SB_CONFIG_BOARD_OLIMEX_ESP32_EVB
SB_CONFIG_BOARD_CAN485DBV1
SB_CONFIG_BOARD_KINCONY_KC868_A8
SB_CONFIG_BOARD_KINCONY_KC868_A32
SB_CONFIG_BOARD_ODROID_GO
SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V2
```

**定义位置（Location）**：[`soc/espressif/esp32/Kconfig.soc:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32/Kconfig.soc#L16)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOARD_YD_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_YD_ESP32)、[`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32)、[`SB_CONFIG_BOARD_TTGO_T7V1_5`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TTGO_T7V1_5)、[`SB_CONFIG_BOARD_TTGO_TBEAM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TTGO_TBEAM)、[`SB_CONFIG_BOARD_TTGO_LORA32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_TTGO_LORA32)、[`SB_CONFIG_BOARD_ESP32_ETHERNET_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32_ETHERNET_KIT)、[`SB_CONFIG_BOARD_ESP_WROVER_KIT`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP_WROVER_KIT)、[`SB_CONFIG_BOARD_ESP32_DEVKITC`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32_DEVKITC)、[`SB_CONFIG_BOARD_ESP32_CAM`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ESP32_CAM)、[`SB_CONFIG_BOARD_INKPLATE_6COLOR`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_INKPLATE_6COLOR)、[`SB_CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1)、[`SB_CONFIG_BOARD_LOLIN32_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_LOLIN32_LITE)、[`SB_CONFIG_BOARD_UDOO_KEY`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_UDOO_KEY)、[`SB_CONFIG_BOARD_M5STACK_CORE2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_CORE2)、[`SB_CONFIG_BOARD_M5STACK_FIRE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_FIRE)、[`SB_CONFIG_BOARD_M5STICKC_PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STICKC_PLUS)、[`SB_CONFIG_BOARD_M5STACK_ATOM_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_M5STACK_ATOM_LITE)、[`SB_CONFIG_BOARD_OLIMEX_ESP32_EVB`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_OLIMEX_ESP32_EVB)、[`SB_CONFIG_BOARD_CAN485DBV1`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_CAN485DBV1)、[`SB_CONFIG_BOARD_KINCONY_KC868_A8`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_KINCONY_KC868_A8)、[`SB_CONFIG_BOARD_KINCONY_KC868_A32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_KINCONY_KC868_A32)、[`SB_CONFIG_BOARD_ODROID_GO`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_ODROID_GO)、[`SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V2`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_BOARD_YD_ESP32`、`SB_CONFIG_BOARD_ADAFRUIT_FEATHER_ESP32`、`SB_CONFIG_BOARD_TTGO_T7V1_5`、`SB_CONFIG_BOARD_TTGO_TBEAM`、`SB_CONFIG_BOARD_TTGO_LORA32`、`SB_CONFIG_BOARD_ESP32_ETHERNET_KIT`、`SB_CONFIG_BOARD_ESP_WROVER_KIT`、`SB_CONFIG_BOARD_ESP32_DEVKITC`、`SB_CONFIG_BOARD_ESP32_CAM`、`SB_CONFIG_BOARD_INKPLATE_6COLOR`、`SB_CONFIG_BOARD_DOIT_ESP32_DEVKIT_V1`、`SB_CONFIG_BOARD_LOLIN32_LITE`、`SB_CONFIG_BOARD_UDOO_KEY`、`SB_CONFIG_BOARD_M5STACK_CORE2`、`SB_CONFIG_BOARD_M5STACK_FIRE`、`SB_CONFIG_BOARD_M5STICKC_PLUS`、`SB_CONFIG_BOARD_M5STACK_ATOM_LITE`、`SB_CONFIG_BOARD_OLIMEX_ESP32_EVB`、`SB_CONFIG_BOARD_CAN485DBV1`、`SB_CONFIG_BOARD_KINCONY_KC868_A8`、`SB_CONFIG_BOARD_KINCONY_KC868_A32`、`SB_CONFIG_BOARD_ODROID_GO`、`SB_CONFIG_BOARD_HELTEC_WIFI_LORA32_V2`。

<a id="SB_CONFIG_SOC_SERIES_ESP32"></a>

## 277.51 `SB_CONFIG_SOC_SERIES_ESP32`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ESP32 系列（Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_ESP32
```

**定义位置（Location）**：[`soc/espressif/esp32/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`SB_CONFIG_SOC_ESP32`](P277_soc_espressif_配置项参考_3.md#SB_CONFIG_SOC_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="SB_CONFIG_SOC_SERIES_ESP32C3"></a>

## 277.52 `SB_CONFIG_SOC_SERIES_ESP32C3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ESP32C3 片上系统（SoC）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_ESP32C3
```

**定义位置（Location）**：[`soc/espressif/esp32c3/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c3/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`SB_CONFIG_SOC_ESP32C3`](P277_soc_espressif_配置项参考_3.md#SB_CONFIG_SOC_ESP32C3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="SB_CONFIG_SOC_SERIES_ESP32S2"></a>

## 277.53 `SB_CONFIG_SOC_SERIES_ESP32S2`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ESP32-S2 系列（Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_ESP32S2
```

**定义位置（Location）**：[`soc/espressif/esp32s2/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s2/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`SB_CONFIG_SOC_ESP32S2`](P277_soc_espressif_配置项参考_3.md#SB_CONFIG_SOC_ESP32S2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="SB_CONFIG_SOC_SERIES_ESP32S3"></a>

## 277.54 `SB_CONFIG_SOC_SERIES_ESP32S3`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ESP32-S3 系列（Series）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
SB_CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**被选择（Selected by）**

```text
SB_CONFIG_SOC_ESP32S3
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig.soc:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig.soc#L4)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`SB_CONFIG_SOC_ESP32S3`](P277_soc_espressif_配置项参考_3.md#SB_CONFIG_SOC_ESP32S3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<!-- kconfig-navigation -->

[上一章](P276_soc_espressif_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P278_soc_focaltech_配置项参考.md)
