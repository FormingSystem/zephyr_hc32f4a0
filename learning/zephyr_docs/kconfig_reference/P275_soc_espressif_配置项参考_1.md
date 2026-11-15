---
id: learning.zephyr-docs.kconfig-reference.page-275
title: "`soc/espressif`配置项参考（1/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第275章\_`soc/espressif`配置项参考（1/3）

本章翻译官方 Kconfig 数据库中 `soc/espressif` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BOOTLOADER_FLASH_XMC_SUPPORT"></a>

## 275.1 `CONFIG_BOOTLOADER_FLASH_XMC_SUPPORT`

**提示（Prompt）**：支持 XMC Flash 芯片，请先阅读帮助（READ HELP FIRST）

**说明（Help）**

执行 XMC 建议的启动流程（startup flow）。关于该流程的详细信息，请咨询 XMC。禁用此选项后，将禁止使用 XMC 芯片。除非确切知道自己在做什么，否则不要禁用此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.flash:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.flash#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_BOOTLOADER_REGION_PROTECTION_ENABLE"></a>

## 275.2 `CONFIG_BOOTLOADER_REGION_PROTECTION_ENABLE`

**提示（Prompt）**：保护未映射内存区域，防止意外访问（Protect unmapped memory regions）

**说明（Help）**

保护整个地址空间中的未映射内存区域（unmapped memory region），防止意外访问。这样可确保 CPU 对未映射区域执行内存操作时触发异常（exception）。启用 `RISCV_PMP` 时此项会自动禁用，因为 Zephyr 会直接管理物理内存保护（PMP）。默认仅对由 MCUboot 加载的应用启用；此时引导加载程序已在启动阶段配置了未锁定的 PMP／物理内存属性（PMA）条目。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y if !CONFIG_RISCV_PMP && CONFIG_BOOTLOADER_MCUBOOT
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.flash:114`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.flash#L114)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_RISCV_PMP`](P035_arch_riscv_配置项参考_2.md#CONFIG_RISCV_PMP)、[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_BOOTLOADER_VDDSDIO_BOOST"></a>

## 275.3 `CONFIG_BOOTLOADER_VDDSDIO_BOOST`

**提示（Prompt）**：VDDSDIO 低压差稳压器电压（LDO voltage）

**说明（Help）**

如果启用此选项，并且 VDDSDIO 低压差稳压器（LDO）通过 eFuse 或 MTDI 启动配置引脚（bootstrapping pin）设置为 1.8V，则引导加载程序会更改 LDO 设置，使其改为输出 1.9V。这有助于防止 Flash 芯片在编程操作期间发生欠压（brownout）。如果 VDDSDIO 设为 3.3V，或内部 VDDSDIO 稳压器已通过 eFuse 禁用，则此选项无效。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_BOOTLOADER_VDDSDIO_BOOST_1_9V
```

**可选项（Choices）**

```text
CONFIG_BOOTLOADER_VDDSDIO_BOOST_1_8V
CONFIG_BOOTLOADER_VDDSDIO_BOOST_1_9V
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.flash:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.flash#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_BOOTLOADER_VDDSDIO_BOOST_1_9V`](P275_soc_espressif_配置项参考_1.md#CONFIG_BOOTLOADER_VDDSDIO_BOOST_1_9V)、[`CONFIG_BOOTLOADER_VDDSDIO_BOOST_1_8V`](P275_soc_espressif_配置项参考_1.md#CONFIG_BOOTLOADER_VDDSDIO_BOOST_1_8V)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_BOOTLOADER_VDDSDIO_BOOST_1_8V"></a>

## 275.4 `CONFIG_BOOTLOADER_VDDSDIO_BOOST_1_8V`

**提示（Prompt）**：电压（Voltage）：1.8 V。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ESPTOOLPY_FLASHFREQ_80M && <choice CONFIG_BOOTLOADER_VDDSDIO_BOOST>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.flash:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.flash#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → VDDSDIO 低压差稳压器电压（LDO voltage）

**配置项引用（Symbol References）**：[`CONFIG_ESPTOOLPY_FLASHFREQ_80M`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESPTOOLPY_FLASHFREQ_80M)、[`CONFIG_BOOTLOADER_VDDSDIO_BOOST`](P275_soc_espressif_配置项参考_1.md#CONFIG_BOOTLOADER_VDDSDIO_BOOST)。

<a id="CONFIG_BOOTLOADER_VDDSDIO_BOOST_1_9V"></a>

## 275.5 `CONFIG_BOOTLOADER_VDDSDIO_BOOST_1_9V`

**提示（Prompt）**：1.9 伏（1.9V）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BOOTLOADER_VDDSDIO_BOOST>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.flash:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.flash#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → VDDSDIO 低压差稳压器电压（LDO voltage）

**配置项引用（Symbol References）**：[`CONFIG_BOOTLOADER_VDDSDIO_BOOST`](P275_soc_espressif_配置项参考_1.md#CONFIG_BOOTLOADER_VDDSDIO_BOOST)。

<a id="CONFIG_D0WD_PSRAM_CLK_IO"></a>

## 275.6 `CONFIG_D0WD_PSRAM_CLK_IO`

**提示（Prompt）**：伪静态 RAM 时钟 IO 编号（PSRAM CLK IO number）

**说明（Help）**

PSRAM 时钟 IO（CLOCK IO）可以使用任意未使用的 GPIO，用户可根据硬件设计配置。如果使用 1.8V Flash 和 1.8V PSRAM，则此值只能为 6、7、8、9、10、11、16、17 之一。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32 && CONFIG_ESP_SPIRAM && (CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
17
```

**取值范围（Ranges）**

```text
[0, 33]
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L168)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config） → ESP32-DOWD 的 PSRAM 时钟和片选 IO（clock and cs IO）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_ESP_SPIRAM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_D0WD_PSRAM_CS_IO"></a>

## 275.7 `CONFIG_D0WD_PSRAM_CS_IO`

**提示（Prompt）**：PSRAM 片选 IO 编号（CS IO number）

**说明（Help）**

PSRAM 片选 IO（CS IO）可以使用任意未使用的 GPIO，用户可根据硬件设计配置。如果使用 1.8V Flash 和 1.8V PSRAM，则此值只能为 6、7、8、9、10、11、16、17 之一。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32 && CONFIG_ESP_SPIRAM && (CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[0, 33]
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:176`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L176)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config） → ESP32-DOWD 的 PSRAM 时钟和片选 IO（clock and cs IO）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_ESP_SPIRAM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_D2WD_PSRAM_CLK_IO"></a>

## 275.8 `CONFIG_D2WD_PSRAM_CLK_IO`

**提示（Prompt）**：伪静态 RAM 时钟 IO 编号（PSRAM CLK IO number）

**说明（Help）**

用户可根据硬件设计配置。对于 ESP32-D2WD 芯片，PSRAM 只能使用 1.8V PSRAM，因此此值只能为 6、7、8、9、10、11、16、17 之一。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32 && CONFIG_ESP_SPIRAM && (CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
9
```

**取值范围（Ranges）**

```text
[0, 33]
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:188`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L188)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config） → ESP32-D2WD 的 PSRAM 时钟和片选 IO（clock and cs IO）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_ESP_SPIRAM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_D2WD_PSRAM_CS_IO"></a>

## 275.9 `CONFIG_D2WD_PSRAM_CS_IO`

**提示（Prompt）**：PSRAM 片选 IO 编号（CS IO number）

**说明（Help）**

用户可根据硬件设计配置。对于 ESP32-D2WD 芯片，PSRAM 只能使用 1.8V PSRAM，因此此值只能为 6、7、8、9、10、11、16、17 之一。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32 && CONFIG_ESP_SPIRAM && (CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32S2 || CONFIG_SOC_SERIES_ESP32S3 || CONFIG_SOC_SERIES_ESP32P4) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[0, 33]
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.spiram:196`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.spiram#L196)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → SPI RAM 配置（SPI RAM config） → ESP32-D2WD 的 PSRAM 时钟和片选 IO（clock and cs IO）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_ESP_SPIRAM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32C2_UNIVERSAL_MAC_ADDRESSES"></a>

## 275.10 `CONFIG_ESP32C2_UNIVERSAL_MAC_ADDRESSES`

**提示（Prompt）**：由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**说明（Help）**

配置由 IEEE 全局管理的 MAC 地址（universally administered MAC address）数量。初始化时，每个网络接口的 MAC 地址都从单个基础 MAC 地址（base MAC address）生成或派生。

如果全局 MAC 地址数量为四个，则全部四个接口（Wi-Fi 站点、Wi-Fi 软件接入点 softap、蓝牙和以太网）都会获得全局管理的 MAC 地址。它们分别通过在基础 MAC 地址的最后一个八位组（octet）上加 0、1、2、3 依次生成。

如果全局 MAC 地址数量为两个，则只有两个接口（Wi-Fi 站点和蓝牙）获得全局管理的 MAC 地址，分别通过在基础 MAC 地址上加 0 和 1 依次生成。其余两个接口（Wi-Fi 软件接入点和以太网）获得本地 MAC 地址（local MAC address），分别从 Wi-Fi 站点和蓝牙的全局 MAC 地址派生。

使用默认的 Espressif 分配的基础 MAC 地址时，两种设置均可使用。使用自定义的全局 MAC 地址范围时，正确设置取决于该范围内的地址分配方式，即每台设备分配 2 个还是 4 个地址。

注意，ESP32-C6 没有集成以太网 MAC。虽然可以使用 `esp_read_mac()` API 返回以太网 MAC 地址，但该地址只能与外部 MAC 外设一起使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32C2 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32C2_UNIVERSAL_MAC_ADDRESSES_FOUR
```

**可选项（Choices）**

```text
CONFIG_ESP32C2_UNIVERSAL_MAC_ADDRESSES_TWO
CONFIG_ESP32C2_UNIVERSAL_MAC_ADDRESSES_FOUR
```

**定义位置（Location）**：[`soc/espressif/esp32c2/Kconfig.mac:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c2/Kconfig.mac#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32C2_UNIVERSAL_MAC_ADDRESSES_FOUR`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C2_UNIVERSAL_MAC_ADDRESSES_FOUR)、[`CONFIG_ESP32C2_UNIVERSAL_MAC_ADDRESSES_TWO`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C2_UNIVERSAL_MAC_ADDRESSES_TWO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32C2_UNIVERSAL_MAC_ADDRESSES_FOUR"></a>

## 275.11 `CONFIG_ESP32C2_UNIVERSAL_MAC_ADDRESSES_FOUR`

**提示（Prompt）**：四个（Four）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32C2_UNIVERSAL_MAC_ADDRESSES>
```

**主动选择（Selects）**

```text
CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP
CONFIG_ESP_MAC_ADDR_UNIVERSE_BT
CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH
```

**定义位置（Location）**：[`soc/espressif/esp32c2/Kconfig.mac:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c2/Kconfig.mac#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config） → 由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**配置项引用（Symbol References）**：[`CONFIG_ESP32C2_UNIVERSAL_MAC_ADDRESSES`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C2_UNIVERSAL_MAC_ADDRESSES)、[`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_BT)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH`。

<a id="CONFIG_ESP32C2_UNIVERSAL_MAC_ADDRESSES_TWO"></a>

## 275.12 `CONFIG_ESP32C2_UNIVERSAL_MAC_ADDRESSES_TWO`

**提示（Prompt）**：两个（Two）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32C2_UNIVERSAL_MAC_ADDRESSES>
```

**主动选择（Selects）**

```text
CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA
CONFIG_ESP_MAC_ADDR_UNIVERSE_BT
```

**定义位置（Location）**：[`soc/espressif/esp32c2/Kconfig.mac:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c2/Kconfig.mac#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config） → 由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**配置项引用（Symbol References）**：[`CONFIG_ESP32C2_UNIVERSAL_MAC_ADDRESSES`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C2_UNIVERSAL_MAC_ADDRESSES)、[`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`。

<a id="CONFIG_ESP32C3_UNIVERSAL_MAC_ADDRESSES"></a>

## 275.13 `CONFIG_ESP32C3_UNIVERSAL_MAC_ADDRESSES`

**提示（Prompt）**：由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**说明（Help）**

配置由 IEEE 全局管理的 MAC 地址（universally administered MAC address）数量。初始化时，每个网络接口的 MAC 地址都从单个基础 MAC 地址（base MAC address）生成或派生。

如果全局 MAC 地址数量为四个，则全部四个接口（Wi-Fi 站点、Wi-Fi 软件接入点 softap、蓝牙和以太网）都会获得全局管理的 MAC 地址。它们分别通过在基础 MAC 地址的最后一个八位组（octet）上加 0、1、2、3 依次生成。

如果全局 MAC 地址数量为两个，则只有两个接口（Wi-Fi 站点和蓝牙）获得全局管理的 MAC 地址，分别通过在基础 MAC 地址上加 0 和 1 依次生成。其余两个接口（Wi-Fi 软件接入点和以太网）获得本地 MAC 地址（local MAC address），分别从 Wi-Fi 站点和蓝牙的全局 MAC 地址派生。

使用默认的 Espressif 分配的基础 MAC 地址时，两种设置均可使用。使用自定义的全局 MAC 地址范围时，正确设置取决于该范围内的地址分配方式，即每台设备分配 2 个还是 4 个地址。

注意，ESP32-C3 没有集成以太网 MAC。虽然可以使用 `esp_read_mac()` API 返回以太网 MAC 地址，但该地址只能与外部 MAC 外设一起使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32C3 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32C3_UNIVERSAL_MAC_ADDRESSES_FOUR
```

**可选项（Choices）**

```text
CONFIG_ESP32C3_UNIVERSAL_MAC_ADDRESSES_TWO
CONFIG_ESP32C3_UNIVERSAL_MAC_ADDRESSES_FOUR
```

**定义位置（Location）**：[`soc/espressif/esp32c3/Kconfig.mac:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c3/Kconfig.mac#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32C3)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32C3_UNIVERSAL_MAC_ADDRESSES_FOUR`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C3_UNIVERSAL_MAC_ADDRESSES_FOUR)、[`CONFIG_ESP32C3_UNIVERSAL_MAC_ADDRESSES_TWO`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C3_UNIVERSAL_MAC_ADDRESSES_TWO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32C3_UNIVERSAL_MAC_ADDRESSES_FOUR"></a>

## 275.14 `CONFIG_ESP32C3_UNIVERSAL_MAC_ADDRESSES_FOUR`

**提示（Prompt）**：四个（Four）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32C3_UNIVERSAL_MAC_ADDRESSES>
```

**主动选择（Selects）**

```text
CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP
CONFIG_ESP_MAC_ADDR_UNIVERSE_BT
CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH
```

**定义位置（Location）**：[`soc/espressif/esp32c3/Kconfig.mac:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c3/Kconfig.mac#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config） → 由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**配置项引用（Symbol References）**：[`CONFIG_ESP32C3_UNIVERSAL_MAC_ADDRESSES`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C3_UNIVERSAL_MAC_ADDRESSES)、[`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_BT)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH`。

<a id="CONFIG_ESP32C3_UNIVERSAL_MAC_ADDRESSES_TWO"></a>

## 275.15 `CONFIG_ESP32C3_UNIVERSAL_MAC_ADDRESSES_TWO`

**提示（Prompt）**：两个（Two）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32C3_UNIVERSAL_MAC_ADDRESSES>
```

**主动选择（Selects）**

```text
CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA
CONFIG_ESP_MAC_ADDR_UNIVERSE_BT
```

**定义位置（Location）**：[`soc/espressif/esp32c3/Kconfig.mac:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c3/Kconfig.mac#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config） → 由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**配置项引用（Symbol References）**：[`CONFIG_ESP32C3_UNIVERSAL_MAC_ADDRESSES`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C3_UNIVERSAL_MAC_ADDRESSES)、[`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`。

<a id="CONFIG_ESP32C5_UNIVERSAL_MAC_ADDRESSES"></a>

## 275.16 `CONFIG_ESP32C5_UNIVERSAL_MAC_ADDRESSES`

**提示（Prompt）**：由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**说明（Help）**

配置由 IEEE 全局管理的 MAC 地址（universally administered MAC address）数量。初始化时，每个网络接口的 MAC 地址都从单个基础 MAC 地址（base MAC address）生成或派生。

如果全局 MAC 地址数量为四个，则全部四个接口（Wi-Fi 站点、Wi-Fi 软件接入点 softap、蓝牙和以太网）都会获得全局管理的 MAC 地址。它们分别通过在基础 MAC 地址的最后一个八位组（octet）上加 0、1、2、3 依次生成。

如果全局 MAC 地址数量为两个，则只有两个接口（Wi-Fi 站点和蓝牙）获得全局管理的 MAC 地址，分别通过在基础 MAC 地址上加 0 和 1 依次生成。其余两个接口（Wi-Fi 软件接入点和以太网）获得本地 MAC 地址（local MAC address），分别从 Wi-Fi 站点和蓝牙的全局 MAC 地址派生。

使用默认的 Espressif 分配的基础 MAC 地址时，两种设置均可使用。使用自定义的全局 MAC 地址范围时，正确设置取决于该范围内的地址分配方式，即每台设备分配 2 个还是 4 个地址。

注意，ESP32-C5 没有集成以太网 MAC。虽然可以使用 `esp_read_mac()` API 返回以太网 MAC 地址，但该地址只能与外部 MAC 外设一起使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32C5 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32C5_UNIVERSAL_MAC_ADDRESSES_FOUR
```

**可选项（Choices）**

```text
CONFIG_ESP32C5_UNIVERSAL_MAC_ADDRESSES_TWO
CONFIG_ESP32C5_UNIVERSAL_MAC_ADDRESSES_FOUR
```

**定义位置（Location）**：[`soc/espressif/esp32c5/Kconfig.mac:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c5/Kconfig.mac#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32C5_UNIVERSAL_MAC_ADDRESSES_FOUR`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C5_UNIVERSAL_MAC_ADDRESSES_FOUR)、[`CONFIG_ESP32C5_UNIVERSAL_MAC_ADDRESSES_TWO`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C5_UNIVERSAL_MAC_ADDRESSES_TWO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32C5_UNIVERSAL_MAC_ADDRESSES_FOUR"></a>

## 275.17 `CONFIG_ESP32C5_UNIVERSAL_MAC_ADDRESSES_FOUR`

**提示（Prompt）**：四个（Four）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32C5_UNIVERSAL_MAC_ADDRESSES>
```

**主动选择（Selects）**

```text
CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR
CONFIG_ESP_MAC_ADDR_UNIVERSE_IEEE802154
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP
CONFIG_ESP_MAC_ADDR_UNIVERSE_BT
CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH
```

**定义位置（Location）**：[`soc/espressif/esp32c5/Kconfig.mac:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c5/Kconfig.mac#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config） → 由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**配置项引用（Symbol References）**：[`CONFIG_ESP32C5_UNIVERSAL_MAC_ADDRESSES`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C5_UNIVERSAL_MAC_ADDRESSES)、[`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_IEEE802154)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_BT)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_IEEE802154`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH`。

<a id="CONFIG_ESP32C5_UNIVERSAL_MAC_ADDRESSES_TWO"></a>

## 275.18 `CONFIG_ESP32C5_UNIVERSAL_MAC_ADDRESSES_TWO`

**提示（Prompt）**：两个（Two）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32C5_UNIVERSAL_MAC_ADDRESSES>
```

**主动选择（Selects）**

```text
CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA
CONFIG_ESP_MAC_ADDR_UNIVERSE_BT
```

**定义位置（Location）**：[`soc/espressif/esp32c5/Kconfig.mac:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c5/Kconfig.mac#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config） → 由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**配置项引用（Symbol References）**：[`CONFIG_ESP32C5_UNIVERSAL_MAC_ADDRESSES`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C5_UNIVERSAL_MAC_ADDRESSES)、[`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`。

<a id="CONFIG_ESP32C61_UNIVERSAL_MAC_ADDRESSES"></a>

## 275.19 `CONFIG_ESP32C61_UNIVERSAL_MAC_ADDRESSES`

**提示（Prompt）**：由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**说明（Help）**

配置由 IEEE 全局管理的 MAC 地址（universally administered MAC address）数量。初始化时，每个网络接口的 MAC 地址都从单个基础 MAC 地址（base MAC address）生成或派生。

如果全局 MAC 地址数量为四个，则全部四个接口（Wi-Fi 站点、Wi-Fi 软件接入点 softap、蓝牙和以太网）都会获得全局管理的 MAC 地址。它们分别通过在基础 MAC 地址的最后一个八位组（octet）上加 0、1、2、3 依次生成。

如果全局 MAC 地址数量为两个，则只有两个接口（Wi-Fi 站点和蓝牙）获得全局管理的 MAC 地址，分别通过在基础 MAC 地址上加 0 和 1 依次生成。其余接口获得从全局 MAC 地址派生的本地 MAC 地址（local MAC address）。

使用默认的 Espressif 分配的基础 MAC 地址时，两种设置均可使用。使用自定义的全局 MAC 地址范围时，正确设置取决于该范围内的地址分配方式，即每台设备分配 2 个还是 4 个地址。

注意，ESP32-C61 没有集成以太网 MAC。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32C61 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32C61_UNIVERSAL_MAC_ADDRESSES_FOUR
```

**可选项（Choices）**

```text
CONFIG_ESP32C61_UNIVERSAL_MAC_ADDRESSES_TWO
CONFIG_ESP32C61_UNIVERSAL_MAC_ADDRESSES_FOUR
```

**定义位置（Location）**：[`soc/espressif/esp32c61/Kconfig.mac:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c61/Kconfig.mac#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32C61_UNIVERSAL_MAC_ADDRESSES_FOUR`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C61_UNIVERSAL_MAC_ADDRESSES_FOUR)、[`CONFIG_ESP32C61_UNIVERSAL_MAC_ADDRESSES_TWO`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C61_UNIVERSAL_MAC_ADDRESSES_TWO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32C61_UNIVERSAL_MAC_ADDRESSES_FOUR"></a>

## 275.20 `CONFIG_ESP32C61_UNIVERSAL_MAC_ADDRESSES_FOUR`

**提示（Prompt）**：四个（Four）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32C61_UNIVERSAL_MAC_ADDRESSES>
```

**主动选择（Selects）**

```text
CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP
CONFIG_ESP_MAC_ADDR_UNIVERSE_BT
CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH
```

**定义位置（Location）**：[`soc/espressif/esp32c61/Kconfig.mac:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c61/Kconfig.mac#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config） → 由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**配置项引用（Symbol References）**：[`CONFIG_ESP32C61_UNIVERSAL_MAC_ADDRESSES`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C61_UNIVERSAL_MAC_ADDRESSES)、[`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_BT)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH`。

<a id="CONFIG_ESP32C61_UNIVERSAL_MAC_ADDRESSES_TWO"></a>

## 275.21 `CONFIG_ESP32C61_UNIVERSAL_MAC_ADDRESSES_TWO`

**提示（Prompt）**：两个（Two）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32C61_UNIVERSAL_MAC_ADDRESSES>
```

**主动选择（Selects）**

```text
CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA
CONFIG_ESP_MAC_ADDR_UNIVERSE_BT
```

**定义位置（Location）**：[`soc/espressif/esp32c61/Kconfig.mac:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c61/Kconfig.mac#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config） → 由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**配置项引用（Symbol References）**：[`CONFIG_ESP32C61_UNIVERSAL_MAC_ADDRESSES`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C61_UNIVERSAL_MAC_ADDRESSES)、[`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`。

<a id="CONFIG_ESP32C6_UNIVERSAL_MAC_ADDRESSES"></a>

## 275.22 `CONFIG_ESP32C6_UNIVERSAL_MAC_ADDRESSES`

**提示（Prompt）**：由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**说明（Help）**

配置由 IEEE 全局管理的 MAC 地址（universally administered MAC address）数量。初始化时，每个网络接口的 MAC 地址都从单个基础 MAC 地址（base MAC address）生成或派生。

如果全局 MAC 地址数量为四个，则全部四个接口（Wi-Fi 站点、Wi-Fi 软件接入点 softap、蓝牙和以太网）都会获得全局管理的 MAC 地址。它们分别通过在基础 MAC 地址的最后一个八位组（octet）上加 0、1、2、3 依次生成。

如果全局 MAC 地址数量为两个，则只有两个接口（Wi-Fi 站点和蓝牙）获得全局管理的 MAC 地址，分别通过在基础 MAC 地址上加 0 和 1 依次生成。其余两个接口（Wi-Fi 软件接入点和以太网）获得本地 MAC 地址（local MAC address），分别从 Wi-Fi 站点和蓝牙的全局 MAC 地址派生。

使用默认的 Espressif 分配的基础 MAC 地址时，两种设置均可使用。使用自定义的全局 MAC 地址范围时，正确设置取决于该范围内的地址分配方式，即每台设备分配 2 个还是 4 个地址。

注意，ESP32-C6 没有集成以太网 MAC。虽然可以使用 `esp_read_mac()` API 返回以太网 MAC 地址，但该地址只能与外部 MAC 外设一起使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32C6 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32C6_UNIVERSAL_MAC_ADDRESSES_FOUR
```

**可选项（Choices）**

```text
CONFIG_ESP32C6_UNIVERSAL_MAC_ADDRESSES_TWO
CONFIG_ESP32C6_UNIVERSAL_MAC_ADDRESSES_FOUR
```

**定义位置（Location）**：[`soc/espressif/esp32c6/Kconfig.mac:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c6/Kconfig.mac#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32C6_UNIVERSAL_MAC_ADDRESSES_FOUR`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C6_UNIVERSAL_MAC_ADDRESSES_FOUR)、[`CONFIG_ESP32C6_UNIVERSAL_MAC_ADDRESSES_TWO`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C6_UNIVERSAL_MAC_ADDRESSES_TWO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32C6_UNIVERSAL_MAC_ADDRESSES_FOUR"></a>

## 275.23 `CONFIG_ESP32C6_UNIVERSAL_MAC_ADDRESSES_FOUR`

**提示（Prompt）**：四个（Four）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32C6_UNIVERSAL_MAC_ADDRESSES>
```

**主动选择（Selects）**

```text
CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR
CONFIG_ESP_MAC_ADDR_UNIVERSE_IEEE802154
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP
CONFIG_ESP_MAC_ADDR_UNIVERSE_BT
CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH
```

**定义位置（Location）**：[`soc/espressif/esp32c6/Kconfig.mac:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c6/Kconfig.mac#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config） → 由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**配置项引用（Symbol References）**：[`CONFIG_ESP32C6_UNIVERSAL_MAC_ADDRESSES`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C6_UNIVERSAL_MAC_ADDRESSES)、[`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_IEEE802154)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_BT)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_IEEE802154`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH`。

<a id="CONFIG_ESP32C6_UNIVERSAL_MAC_ADDRESSES_TWO"></a>

## 275.24 `CONFIG_ESP32C6_UNIVERSAL_MAC_ADDRESSES_TWO`

**提示（Prompt）**：两个（Two）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32C6_UNIVERSAL_MAC_ADDRESSES>
```

**主动选择（Selects）**

```text
CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA
CONFIG_ESP_MAC_ADDR_UNIVERSE_BT
```

**定义位置（Location）**：[`soc/espressif/esp32c6/Kconfig.mac:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32c6/Kconfig.mac#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config） → 由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**配置项引用（Symbol References）**：[`CONFIG_ESP32C6_UNIVERSAL_MAC_ADDRESSES`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32C6_UNIVERSAL_MAC_ADDRESSES)、[`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`。

<a id="CONFIG_ESP32H2_UNIVERSAL_MAC_ADDRESSES"></a>

## 275.25 `CONFIG_ESP32H2_UNIVERSAL_MAC_ADDRESSES`

**提示（Prompt）**：由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**说明（Help）**

配置由 IEEE 全局管理的 MAC 地址（universally administered MAC address）数量。初始化时，每个网络接口的 MAC 地址都从单个基础 MAC 地址（base MAC address）生成或派生。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32H2 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32H2_UNIVERSAL_MAC_ADDRESSES_TWO
```

**可选项（Choices）**

```text
CONFIG_ESP32H2_UNIVERSAL_MAC_ADDRESSES_TWO
```

**定义位置（Location）**：[`soc/espressif/esp32h2/Kconfig.mac:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32h2/Kconfig.mac#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32H2_UNIVERSAL_MAC_ADDRESSES_TWO`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32H2_UNIVERSAL_MAC_ADDRESSES_TWO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32H2`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32H2_UNIVERSAL_MAC_ADDRESSES_TWO"></a>

## 275.26 `CONFIG_ESP32H2_UNIVERSAL_MAC_ADDRESSES_TWO`

**提示（Prompt）**：两个（Two）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32H2_UNIVERSAL_MAC_ADDRESSES>
```

**主动选择（Selects）**

```text
CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO
CONFIG_ESP_MAC_ADDR_UNIVERSE_IEEE802154
CONFIG_ESP_MAC_ADDR_UNIVERSE_BT
```

**定义位置（Location）**：[`soc/espressif/esp32h2/Kconfig.mac:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32h2/Kconfig.mac#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config） → 由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**配置项引用（Symbol References）**：[`CONFIG_ESP32H2_UNIVERSAL_MAC_ADDRESSES`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32H2_UNIVERSAL_MAC_ADDRESSES)、[`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_IEEE802154)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_IEEE802154`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`。

<a id="CONFIG_ESP32P4_EMAC"></a>

## 275.27 `CONFIG_ESP32P4_EMAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于启用 ESP32-P4 以太网介质访问控制驱动（Ethernet MAC driver）的隐藏选项。以太网与管理数据输入／输出（MDIO）都依赖此驱动。此选项允许独立于以太网启用 MDIO。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32P4 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y if CONFIG_ETH_ESP32
y if CONFIG_ETH_ESP32_DWC_ETHER_1000
y if CONFIG_MDIO_ESP32
```

**定义位置（Location）**：[`soc/espressif/esp32p4/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32p4/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ETH_ESP32`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ESP32)、[`CONFIG_ETH_ESP32_DWC_ETHER_1000`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ESP32_DWC_ETHER_1000)、[`CONFIG_MDIO_ESP32`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32P4_UNIVERSAL_MAC_ADDRESSES"></a>

## 275.28 `CONFIG_ESP32P4_UNIVERSAL_MAC_ADDRESSES`

**提示（Prompt）**：由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**说明（Help）**

配置由 IEEE 全局管理的 MAC 地址（universally administered MAC address）数量。初始化时，每个网络接口的 MAC 地址都从单个基础 MAC 地址（base MAC address）生成或派生。全局 MAC 地址数量为两个时，仅两个接口（以太网和预留接口）获得全局管理的 MAC 地址，分别通过在基础 MAC 地址上加 0 和 1 依次生成。注意，ESP32-P4 集成了以太网 MAC，但没有 Wi-Fi 或蓝牙（Bluetooth）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32P4 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32P4_UNIVERSAL_MAC_ADDRESSES_TWO
```

**可选项（Choices）**

```text
CONFIG_ESP32P4_UNIVERSAL_MAC_ADDRESSES_TWO
```

**定义位置（Location）**：[`soc/espressif/esp32p4/Kconfig.mac:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32p4/Kconfig.mac#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32P4_UNIVERSAL_MAC_ADDRESSES_TWO`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32P4_UNIVERSAL_MAC_ADDRESSES_TWO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32P4_UNIVERSAL_MAC_ADDRESSES_TWO"></a>

## 275.29 `CONFIG_ESP32P4_UNIVERSAL_MAC_ADDRESSES_TWO`

**提示（Prompt）**：两个（Two）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32P4_UNIVERSAL_MAC_ADDRESSES>
```

**主动选择（Selects）**

```text
CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO
CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH
```

**定义位置（Location）**：[`soc/espressif/esp32p4/Kconfig.mac:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32p4/Kconfig.mac#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config） → 由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**配置项引用（Symbol References）**：[`CONFIG_ESP32P4_UNIVERSAL_MAC_ADDRESSES`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32P4_UNIVERSAL_MAC_ADDRESSES)、[`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH`。

<a id="CONFIG_ESP32S2_DATA_CACHE_0KB"></a>

## 275.30 `CONFIG_ESP32S2_DATA_CACHE_0KB`

**提示（Prompt）**：0 KB（千字节）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ESP_SPIRAM && <choice CONFIG_ESP32S2_DATA_CACHE_SIZE>
```

**定义位置（Location）**：[`soc/espressif/esp32s2/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s2/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 数据缓存大小（Data cache size）

**配置项引用（Symbol References）**：[`CONFIG_ESP_SPIRAM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM)、[`CONFIG_ESP32S2_DATA_CACHE_SIZE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S2_DATA_CACHE_SIZE)。

<a id="CONFIG_ESP32S2_DATA_CACHE_16KB"></a>

## 275.31 `CONFIG_ESP32S2_DATA_CACHE_16KB`

**提示（Prompt）**：16 KB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S2_DATA_CACHE_SIZE>
```

**定义位置（Location）**：[`soc/espressif/esp32s2/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s2/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 数据缓存大小（Data cache size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S2_DATA_CACHE_SIZE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S2_DATA_CACHE_SIZE)。

<a id="CONFIG_ESP32S2_DATA_CACHE_8KB"></a>

## 275.32 `CONFIG_ESP32S2_DATA_CACHE_8KB`

**提示（Prompt）**：8 KB（千字节）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S2_DATA_CACHE_SIZE>
```

**定义位置（Location）**：[`soc/espressif/esp32s2/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s2/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 数据缓存大小（Data cache size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S2_DATA_CACHE_SIZE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S2_DATA_CACHE_SIZE)。

<a id="CONFIG_ESP32S2_DATA_CACHE_LINE_16B"></a>

## 275.33 `CONFIG_ESP32S2_DATA_CACHE_LINE_16B`

**提示（Prompt）**：16 字节（16 Bytes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/espressif/esp32s2/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s2/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 数据缓存行大小（Data cache line size）

<a id="CONFIG_ESP32S2_DATA_CACHE_LINE_32B"></a>

## 275.34 `CONFIG_ESP32S2_DATA_CACHE_LINE_32B`

**提示（Prompt）**：32 字节（32 Bytes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`soc/espressif/esp32s2/Kconfig:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s2/Kconfig#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 数据缓存行大小（Data cache line size）

<a id="CONFIG_ESP32S2_DATA_CACHE_SIZE"></a>

## 275.35 `CONFIG_ESP32S2_DATA_CACHE_SIZE`

**提示（Prompt）**：数据缓存大小（Data cache size）

**说明（Help）**

应用启动时设置的数据缓存大小（data cache size）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S2 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32S2_DATA_CACHE_8KB
```

**可选项（Choices）**

```text
CONFIG_ESP32S2_DATA_CACHE_0KB
CONFIG_ESP32S2_DATA_CACHE_8KB
CONFIG_ESP32S2_DATA_CACHE_16KB
```

**定义位置（Location）**：[`soc/espressif/esp32s2/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s2/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32S2_DATA_CACHE_8KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S2_DATA_CACHE_8KB)、[`CONFIG_ESP32S2_DATA_CACHE_0KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S2_DATA_CACHE_0KB)、[`CONFIG_ESP32S2_DATA_CACHE_16KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S2_DATA_CACHE_16KB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32S2_INSTRUCTION_CACHE_16KB"></a>

## 275.36 `CONFIG_ESP32S2_INSTRUCTION_CACHE_16KB`

**提示（Prompt）**：16KB 指令缓存大小（instruction cache size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S2_INSTRUCTION_CACHE_SIZE>
```

**定义位置（Location）**：[`soc/espressif/esp32s2/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s2/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 指令缓存大小（Instruction cache size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S2_INSTRUCTION_CACHE_SIZE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S2_INSTRUCTION_CACHE_SIZE)。

<a id="CONFIG_ESP32S2_INSTRUCTION_CACHE_8KB"></a>

## 275.37 `CONFIG_ESP32S2_INSTRUCTION_CACHE_8KB`

**提示（Prompt）**：8KB 指令缓存大小（instruction cache size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S2_INSTRUCTION_CACHE_SIZE>
```

**定义位置（Location）**：[`soc/espressif/esp32s2/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s2/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 指令缓存大小（Instruction cache size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S2_INSTRUCTION_CACHE_SIZE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S2_INSTRUCTION_CACHE_SIZE)。

<a id="CONFIG_ESP32S2_INSTRUCTION_CACHE_LINE_16B"></a>

## 275.38 `CONFIG_ESP32S2_INSTRUCTION_CACHE_LINE_16B`

**提示（Prompt）**：16 字节（16 Bytes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S2_INSTRUCTION_CACHE_LINE_SIZE>
```

**定义位置（Location）**：[`soc/espressif/esp32s2/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s2/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 指令缓存行大小（Instruction cache line size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S2_INSTRUCTION_CACHE_LINE_SIZE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S2_INSTRUCTION_CACHE_LINE_SIZE)。

<a id="CONFIG_ESP32S2_INSTRUCTION_CACHE_LINE_32B"></a>

## 275.39 `CONFIG_ESP32S2_INSTRUCTION_CACHE_LINE_32B`

**提示（Prompt）**：32 字节（32 Bytes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S2_INSTRUCTION_CACHE_LINE_SIZE>
```

**定义位置（Location）**：[`soc/espressif/esp32s2/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s2/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 指令缓存行大小（Instruction cache line size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S2_INSTRUCTION_CACHE_LINE_SIZE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S2_INSTRUCTION_CACHE_LINE_SIZE)。

<a id="CONFIG_ESP32S2_INSTRUCTION_CACHE_LINE_SIZE"></a>

## 275.40 `CONFIG_ESP32S2_INSTRUCTION_CACHE_LINE_SIZE`

**提示（Prompt）**：指令缓存行大小（Instruction cache line size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S2 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32S2_INSTRUCTION_CACHE_LINE_32B
```

**可选项（Choices）**

```text
CONFIG_ESP32S2_INSTRUCTION_CACHE_LINE_16B
CONFIG_ESP32S2_INSTRUCTION_CACHE_LINE_32B
```

**定义位置（Location）**：[`soc/espressif/esp32s2/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s2/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32S2_INSTRUCTION_CACHE_LINE_32B`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S2_INSTRUCTION_CACHE_LINE_32B)、[`CONFIG_ESP32S2_INSTRUCTION_CACHE_LINE_16B`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S2_INSTRUCTION_CACHE_LINE_16B)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32S2_INSTRUCTION_CACHE_SIZE"></a>

## 275.41 `CONFIG_ESP32S2_INSTRUCTION_CACHE_SIZE`

**提示（Prompt）**：指令缓存大小（Instruction cache size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S2 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32S2_INSTRUCTION_CACHE_8KB
```

**可选项（Choices）**

```text
CONFIG_ESP32S2_INSTRUCTION_CACHE_8KB
CONFIG_ESP32S2_INSTRUCTION_CACHE_16KB
```

**定义位置（Location）**：[`soc/espressif/esp32s2/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s2/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32S2_INSTRUCTION_CACHE_8KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S2_INSTRUCTION_CACHE_8KB)、[`CONFIG_ESP32S2_INSTRUCTION_CACHE_16KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S2_INSTRUCTION_CACHE_16KB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32S2_UNIVERSAL_MAC_ADDRESSES"></a>

## 275.42 `CONFIG_ESP32S2_UNIVERSAL_MAC_ADDRESSES`

**提示（Prompt）**：由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**说明（Help）**

配置由 IEEE 全局管理的 MAC 地址（universally administered MAC address）数量。初始化时，每个网络接口的 MAC 地址都从单个基础 MAC 地址（base MAC address）生成或派生。

如果全局 MAC 地址数量为两个，所有接口（Wi-Fi 站点和 Wi-Fi 软件接入点，softap）都会获得全局管理的 MAC 地址，分别通过在基础 MAC 地址的最后一个八位组（octet）上加 0 和 1 依次生成。

如果全局 MAC 地址数量为一个，则只有 Wi-Fi 站点获得全局管理的 MAC 地址。Wi-Fi 软件接入点获得本地 MAC 地址（local MAC address），它从 Wi-Fi 站点的全局 MAC 地址派生。

使用默认的 Espressif 分配的基础 MAC 地址时，两种设置均可使用。使用自定义的全局 MAC 地址范围时，正确设置取决于该范围内的地址分配方式，即每台设备分配 1 个还是 2 个地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S2 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32S2_UNIVERSAL_MAC_ADDRESSES_TWO
```

**可选项（Choices）**

```text
CONFIG_ESP32S2_UNIVERSAL_MAC_ADDRESSES_ONE
CONFIG_ESP32S2_UNIVERSAL_MAC_ADDRESSES_TWO
```

**定义位置（Location）**：[`soc/espressif/esp32s2/Kconfig.mac:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s2/Kconfig.mac#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S2`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S2)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32S2_UNIVERSAL_MAC_ADDRESSES_TWO`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S2_UNIVERSAL_MAC_ADDRESSES_TWO)、[`CONFIG_ESP32S2_UNIVERSAL_MAC_ADDRESSES_ONE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S2_UNIVERSAL_MAC_ADDRESSES_ONE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32S2_UNIVERSAL_MAC_ADDRESSES_ONE"></a>

## 275.43 `CONFIG_ESP32S2_UNIVERSAL_MAC_ADDRESSES_ONE`

**提示（Prompt）**：一个（One）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S2_UNIVERSAL_MAC_ADDRESSES>
```

**主动选择（Selects）**

```text
CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_ONE
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA
```

**定义位置（Location）**：[`soc/espressif/esp32s2/Kconfig.mac:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s2/Kconfig.mac#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config） → 由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S2_UNIVERSAL_MAC_ADDRESSES`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S2_UNIVERSAL_MAC_ADDRESSES)、[`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_ONE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_ONE)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_ONE`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`。

<a id="CONFIG_ESP32S2_UNIVERSAL_MAC_ADDRESSES_TWO"></a>

## 275.44 `CONFIG_ESP32S2_UNIVERSAL_MAC_ADDRESSES_TWO`

**提示（Prompt）**：两个（Two）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S2_UNIVERSAL_MAC_ADDRESSES>
```

**主动选择（Selects）**

```text
CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP
```

**定义位置（Location）**：[`soc/espressif/esp32s2/Kconfig.mac:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s2/Kconfig.mac#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config） → 由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S2_UNIVERSAL_MAC_ADDRESSES`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S2_UNIVERSAL_MAC_ADDRESSES)、[`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP`。

<a id="CONFIG_ESP32S3_DATA_CACHE_16KB"></a>

## 275.45 `CONFIG_ESP32S3_DATA_CACHE_16KB`

**提示（Prompt）**：16 KB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S3_DATA_CACHE_SIZE>
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 数据缓存大小（Data cache size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S3_DATA_CACHE_SIZE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_DATA_CACHE_SIZE)。

<a id="CONFIG_ESP32S3_DATA_CACHE_32KB"></a>

## 275.46 `CONFIG_ESP32S3_DATA_CACHE_32KB`

**提示（Prompt）**：32 KB（千字节）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S3_DATA_CACHE_SIZE>
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 数据缓存大小（Data cache size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S3_DATA_CACHE_SIZE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_DATA_CACHE_SIZE)。

<a id="CONFIG_ESP32S3_DATA_CACHE_4WAYS"></a>

## 275.47 `CONFIG_ESP32S3_DATA_CACHE_4WAYS`

**提示（Prompt）**：4 路（4 ways）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S3_DCACHE_ASSOCIATED_WAYS>
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 数据缓存关联路数（Data cache associated ways）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S3_DCACHE_ASSOCIATED_WAYS`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_DCACHE_ASSOCIATED_WAYS)。

<a id="CONFIG_ESP32S3_DATA_CACHE_64KB"></a>

## 275.48 `CONFIG_ESP32S3_DATA_CACHE_64KB`

**提示（Prompt）**：64 KB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S3_DATA_CACHE_SIZE>
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 数据缓存大小（Data cache size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S3_DATA_CACHE_SIZE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_DATA_CACHE_SIZE)。

<a id="CONFIG_ESP32S3_DATA_CACHE_8WAYS"></a>

## 275.49 `CONFIG_ESP32S3_DATA_CACHE_8WAYS`

**提示（Prompt）**：8 路（8 ways）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S3_DCACHE_ASSOCIATED_WAYS>
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 数据缓存关联路数（Data cache associated ways）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S3_DCACHE_ASSOCIATED_WAYS`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_DCACHE_ASSOCIATED_WAYS)。

<a id="CONFIG_ESP32S3_DATA_CACHE_LINE_16B"></a>

## 275.50 `CONFIG_ESP32S3_DATA_CACHE_LINE_16B`

**提示（Prompt）**：16 字节（16 Bytes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ESP32S3_DATA_CACHE_16KB || CONFIG_ESP32S3_DATA_CACHE_32KB) && <choice CONFIG_ESP32S3_DATA_CACHE_LINE_SIZE>
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 数据缓存行大小（Data cache line size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S3_DATA_CACHE_16KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_DATA_CACHE_16KB)、[`CONFIG_ESP32S3_DATA_CACHE_32KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_DATA_CACHE_32KB)、[`CONFIG_ESP32S3_DATA_CACHE_LINE_SIZE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_DATA_CACHE_LINE_SIZE)。

<a id="CONFIG_ESP32S3_DATA_CACHE_LINE_32B"></a>

## 275.51 `CONFIG_ESP32S3_DATA_CACHE_LINE_32B`

**提示（Prompt）**：32 字节（32 Bytes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S3_DATA_CACHE_LINE_SIZE>
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 数据缓存行大小（Data cache line size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S3_DATA_CACHE_LINE_SIZE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_DATA_CACHE_LINE_SIZE)。

<a id="CONFIG_ESP32S3_DATA_CACHE_LINE_64B"></a>

## 275.52 `CONFIG_ESP32S3_DATA_CACHE_LINE_64B`

**提示（Prompt）**：64 字节（64 Bytes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S3_DATA_CACHE_LINE_SIZE>
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 数据缓存行大小（Data cache line size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S3_DATA_CACHE_LINE_SIZE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_DATA_CACHE_LINE_SIZE)。

<a id="CONFIG_ESP32S3_DATA_CACHE_LINE_SIZE"></a>

## 275.53 `CONFIG_ESP32S3_DATA_CACHE_LINE_SIZE`

**提示（Prompt）**：数据缓存行大小（Data cache line size）

**说明（Help）**

应用启动时设置的数据缓存行大小（data cache line size）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S3 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32S3_DATA_CACHE_LINE_32B
```

**可选项（Choices）**

```text
CONFIG_ESP32S3_DATA_CACHE_LINE_16B
CONFIG_ESP32S3_DATA_CACHE_LINE_32B
CONFIG_ESP32S3_DATA_CACHE_LINE_64B
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:135`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L135)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32S3_DATA_CACHE_LINE_32B`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_DATA_CACHE_LINE_32B)、[`CONFIG_ESP32S3_DATA_CACHE_LINE_16B`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_DATA_CACHE_LINE_16B)、[`CONFIG_ESP32S3_DATA_CACHE_LINE_64B`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_DATA_CACHE_LINE_64B)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32S3_DATA_CACHE_SIZE"></a>

## 275.54 `CONFIG_ESP32S3_DATA_CACHE_SIZE`

**提示（Prompt）**：数据缓存大小（Data cache size）

**说明（Help）**

应用启动时设置的数据缓存大小（data cache size）。如果使用 32KB 数据缓存而非 64KB 数据缓存，剩余 32KB 会加入堆（heap）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S3 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32S3_DATA_CACHE_32KB
```

**可选项（Choices）**

```text
CONFIG_ESP32S3_DATA_CACHE_16KB
CONFIG_ESP32S3_DATA_CACHE_32KB
CONFIG_ESP32S3_DATA_CACHE_64KB
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32S3_DATA_CACHE_32KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_DATA_CACHE_32KB)、[`CONFIG_ESP32S3_DATA_CACHE_16KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_DATA_CACHE_16KB)、[`CONFIG_ESP32S3_DATA_CACHE_64KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_DATA_CACHE_64KB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32S3_DATA_CACHE_WRAP"></a>

## 275.55 `CONFIG_ESP32S3_DATA_CACHE_WRAP`

**提示（Prompt）**：定义数据缓存回绕模式（data cache wrap mode）

**说明（Help）**

启用后，数据缓存（data cache）会使用回绕模式（wrap mode）读取 SPI Flash 或 SPI RAM。回绕长度等于 `ESP32S3_DATA_CACHE_LINE_SIZE`。不过，此行为取决于复杂的条件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S3 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:159`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L159)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32S3_DCACHE_ASSOCIATED_WAYS"></a>

## 275.56 `CONFIG_ESP32S3_DCACHE_ASSOCIATED_WAYS`

**提示（Prompt）**：数据缓存关联路数（Data cache associated ways）

**说明（Help）**

应用启动时设置的数据缓存关联路数（data cache associated ways）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S3 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32S3_DATA_CACHE_8WAYS
```

**可选项（Choices）**

```text
CONFIG_ESP32S3_DATA_CACHE_4WAYS
CONFIG_ESP32S3_DATA_CACHE_8WAYS
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32S3_DATA_CACHE_8WAYS`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_DATA_CACHE_8WAYS)、[`CONFIG_ESP32S3_DATA_CACHE_4WAYS`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_DATA_CACHE_4WAYS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32S3_ICACHE_ASSOCIATED_WAYS"></a>

## 275.57 `CONFIG_ESP32S3_ICACHE_ASSOCIATED_WAYS`

**提示（Prompt）**：指令缓存关联路数（Instruction cache associated ways）

**说明（Help）**

应用启动时设置的指令缓存关联路数（instruction cache associated ways）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S3 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32S3_INSTRUCTION_CACHE_8WAYS
```

**可选项（Choices）**

```text
CONFIG_ESP32S3_INSTRUCTION_CACHE_4WAYS
CONFIG_ESP32S3_INSTRUCTION_CACHE_8WAYS
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32S3_INSTRUCTION_CACHE_8WAYS`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_INSTRUCTION_CACHE_8WAYS)、[`CONFIG_ESP32S3_INSTRUCTION_CACHE_4WAYS`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_INSTRUCTION_CACHE_4WAYS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32S3_INSTRUCTION_CACHE_16KB"></a>

## 275.58 `CONFIG_ESP32S3_INSTRUCTION_CACHE_16KB`

**提示（Prompt）**：16 KB

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S3_INSTRUCTION_CACHE_SIZE>
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 指令缓存大小（Instruction cache size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S3_INSTRUCTION_CACHE_SIZE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_INSTRUCTION_CACHE_SIZE)。

<a id="CONFIG_ESP32S3_INSTRUCTION_CACHE_32KB"></a>

## 275.59 `CONFIG_ESP32S3_INSTRUCTION_CACHE_32KB`

**提示（Prompt）**：32 KB（千字节）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S3_INSTRUCTION_CACHE_SIZE>
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 指令缓存大小（Instruction cache size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S3_INSTRUCTION_CACHE_SIZE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_INSTRUCTION_CACHE_SIZE)。

<a id="CONFIG_ESP32S3_INSTRUCTION_CACHE_4WAYS"></a>

## 275.60 `CONFIG_ESP32S3_INSTRUCTION_CACHE_4WAYS`

**提示（Prompt）**：4 路（4 ways）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S3_ICACHE_ASSOCIATED_WAYS>
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 指令缓存关联路数（Instruction cache associated ways）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S3_ICACHE_ASSOCIATED_WAYS`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_ICACHE_ASSOCIATED_WAYS)。

<a id="CONFIG_ESP32S3_INSTRUCTION_CACHE_8WAYS"></a>

## 275.61 `CONFIG_ESP32S3_INSTRUCTION_CACHE_8WAYS`

**提示（Prompt）**：8 路（8 ways）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S3_ICACHE_ASSOCIATED_WAYS>
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 指令缓存关联路数（Instruction cache associated ways）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S3_ICACHE_ASSOCIATED_WAYS`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_ICACHE_ASSOCIATED_WAYS)。

<a id="CONFIG_ESP32S3_INSTRUCTION_CACHE_LINE_16B"></a>

## 275.62 `CONFIG_ESP32S3_INSTRUCTION_CACHE_LINE_16B`

**提示（Prompt）**：16 字节（16 Bytes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32S3_INSTRUCTION_CACHE_16KB && <choice CONFIG_ESP32S3_INSTRUCTION_CACHE_LINE_SIZE>
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 指令缓存行大小（Instruction cache line size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S3_INSTRUCTION_CACHE_16KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_INSTRUCTION_CACHE_16KB)、[`CONFIG_ESP32S3_INSTRUCTION_CACHE_LINE_SIZE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_INSTRUCTION_CACHE_LINE_SIZE)。

<a id="CONFIG_ESP32S3_INSTRUCTION_CACHE_LINE_32B"></a>

## 275.63 `CONFIG_ESP32S3_INSTRUCTION_CACHE_LINE_32B`

**提示（Prompt）**：32 字节（32 Bytes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S3_INSTRUCTION_CACHE_LINE_SIZE>
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 指令缓存行大小（Instruction cache line size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S3_INSTRUCTION_CACHE_LINE_SIZE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_INSTRUCTION_CACHE_LINE_SIZE)。

<a id="CONFIG_ESP32S3_INSTRUCTION_CACHE_LINE_SIZE"></a>

## 275.64 `CONFIG_ESP32S3_INSTRUCTION_CACHE_LINE_SIZE`

**提示（Prompt）**：指令缓存行大小（Instruction cache line size）

**说明（Help）**

应用启动时设置的指令缓存行大小（instruction cache line size）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S3 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32S3_INSTRUCTION_CACHE_LINE_32B
```

**可选项（Choices）**

```text
CONFIG_ESP32S3_INSTRUCTION_CACHE_LINE_16B
CONFIG_ESP32S3_INSTRUCTION_CACHE_LINE_32B
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32S3_INSTRUCTION_CACHE_LINE_32B`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_INSTRUCTION_CACHE_LINE_32B)、[`CONFIG_ESP32S3_INSTRUCTION_CACHE_LINE_16B`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_INSTRUCTION_CACHE_LINE_16B)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32S3_INSTRUCTION_CACHE_SIZE"></a>

## 275.65 `CONFIG_ESP32S3_INSTRUCTION_CACHE_SIZE`

**提示（Prompt）**：指令缓存大小（Instruction cache size）

**说明（Help）**

应用启动时设置的指令缓存大小（instruction cache size）。如果使用 16KB 指令缓存而非 32KB 指令缓存，剩余 16KB 将由堆分配器（heap allocator）管理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S3 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32S3_INSTRUCTION_CACHE_16KB
```

**可选项（Choices）**

```text
CONFIG_ESP32S3_INSTRUCTION_CACHE_16KB
CONFIG_ESP32S3_INSTRUCTION_CACHE_32KB
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32S3_INSTRUCTION_CACHE_16KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_INSTRUCTION_CACHE_16KB)、[`CONFIG_ESP32S3_INSTRUCTION_CACHE_32KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_INSTRUCTION_CACHE_32KB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32S3_INSTRUCTION_CACHE_WRAP"></a>

## 275.66 `CONFIG_ESP32S3_INSTRUCTION_CACHE_WRAP`

**提示（Prompt）**：定义指令缓存回绕模式（instruction cache wrap mode）

**说明（Help）**

启用后，指令缓存（instruction cache）会使用回绕模式（wrap mode）读取 SPI Flash 或 SPI RAM。回绕长度等于 `ESP32S3_INSTRUCTION_CACHE_LINE_SIZE`。不过，此行为取决于复杂的条件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S3 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32S3_UNIVERSAL_MAC_ADDRESSES"></a>

## 275.67 `CONFIG_ESP32S3_UNIVERSAL_MAC_ADDRESSES`

**提示（Prompt）**：由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**说明（Help）**

配置由 IEEE 全局管理的 MAC 地址（universally administered MAC address）数量。初始化时，每个网络接口的 MAC 地址都从单个基础 MAC 地址（base MAC address）生成或派生。

如果全局 MAC 地址数量为四个，则全部四个接口（Wi-Fi 站点、Wi-Fi 软件接入点 softap、蓝牙和以太网）都会获得全局管理的 MAC 地址。它们分别通过在基础 MAC 地址的最后一个八位组（octet）上加 0、1、2、3 依次生成。

如果全局 MAC 地址数量为两个，则只有两个接口（Wi-Fi 站点和蓝牙）获得全局管理的 MAC 地址，分别通过在基础 MAC 地址上加 0 和 1 依次生成。其余两个接口（Wi-Fi 软件接入点和以太网）获得本地 MAC 地址（local MAC address），分别从 Wi-Fi 站点和蓝牙的全局 MAC 地址派生。

使用默认的 Espressif 分配的基础 MAC 地址时，两种设置均可使用。使用自定义的全局 MAC 地址范围时，正确设置取决于该范围内的地址分配方式，即每台设备分配 2 个还是 4 个地址。

译注：原文末尾还重复附有一段残句，其意思为“……取决于该范围内的 MAC 地址分配方式（每台设备 1 个或 2 个）”。这与前文每台设备 2 个或 4 个的表述不一致，保留此差异，不将残句当作已确认的配置规则。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S3 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32S3_UNIVERSAL_MAC_ADDRESSES_FOUR
```

**可选项（Choices）**

```text
CONFIG_ESP32S3_UNIVERSAL_MAC_ADDRESSES_TWO
CONFIG_ESP32S3_UNIVERSAL_MAC_ADDRESSES_FOUR
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig.mac:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig.mac#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32S3_UNIVERSAL_MAC_ADDRESSES_FOUR`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_UNIVERSAL_MAC_ADDRESSES_FOUR)、[`CONFIG_ESP32S3_UNIVERSAL_MAC_ADDRESSES_TWO`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_UNIVERSAL_MAC_ADDRESSES_TWO)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32S3_UNIVERSAL_MAC_ADDRESSES_FOUR"></a>

## 275.68 `CONFIG_ESP32S3_UNIVERSAL_MAC_ADDRESSES_FOUR`

**提示（Prompt）**：四个（Four）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S3_UNIVERSAL_MAC_ADDRESSES>
```

**主动选择（Selects）**

```text
CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP
CONFIG_ESP_MAC_ADDR_UNIVERSE_BT
CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig.mac:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig.mac#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config） → 由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S3_UNIVERSAL_MAC_ADDRESSES`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_UNIVERSAL_MAC_ADDRESSES)、[`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_BT)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_FOUR`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_AP`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_ETH`。

<a id="CONFIG_ESP32S3_UNIVERSAL_MAC_ADDRESSES_TWO"></a>

## 275.69 `CONFIG_ESP32S3_UNIVERSAL_MAC_ADDRESSES_TWO`

**提示（Prompt）**：两个（Two）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32S3_UNIVERSAL_MAC_ADDRESSES>
```

**主动选择（Selects）**

```text
CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO
CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA
CONFIG_ESP_MAC_ADDR_UNIVERSE_BT
```

**定义位置（Location）**：[`soc/espressif/esp32s3/Kconfig.mac:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32s3/Kconfig.mac#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → MAC 配置（MAC Config） → 由 IEEE 全局管理的 MAC 地址数量（universally administered MAC addresses）

**配置项引用（Symbol References）**：[`CONFIG_ESP32S3_UNIVERSAL_MAC_ADDRESSES`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_UNIVERSAL_MAC_ADDRESSES)、[`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA)、[`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP_MAC_ADDR_UNIVERSE_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ESP_MAC_UNIVERSAL_MAC_ADDRESSES_TWO`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_WIFI_STA`、`CONFIG_ESP_MAC_ADDR_UNIVERSE_BT`。

<a id="CONFIG_ESP32_BT_RESERVE_DRAM"></a>

## 275.70 `CONFIG_ESP32_BT_RESERVE_DRAM`

**提示（Prompt）**：蓝牙控制器保留 RAM 区域（Bluetooth controller reserved RAM region）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
0xdb5c if CONFIG_BT
0
```

**定义位置（Location）**：[`soc/espressif/esp32/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_CACHE_L2_128KB"></a>

## 275.71 `CONFIG_ESP32_CACHE_L2_128KB`

**提示（Prompt）**：128 KB（千字节）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_CACHE_L2_SIZE_CHOICE>
```

**定义位置（Location）**：[`soc/espressif/esp32p4/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32p4/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 二级缓存大小（L2 cache size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_CACHE_L2_SIZE_CHOICE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_CACHE_L2_SIZE_CHOICE)。

<a id="CONFIG_ESP32_CACHE_L2_256KB"></a>

## 275.72 `CONFIG_ESP32_CACHE_L2_256KB`

**提示（Prompt）**：256 KB（千字节）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_CACHE_L2_SIZE_CHOICE>
```

**定义位置（Location）**：[`soc/espressif/esp32p4/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32p4/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 二级缓存大小（L2 cache size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_CACHE_L2_SIZE_CHOICE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_CACHE_L2_SIZE_CHOICE)。

<a id="CONFIG_ESP32_CACHE_L2_512KB"></a>

## 275.73 `CONFIG_ESP32_CACHE_L2_512KB`

**提示（Prompt）**：512 KB（千字节）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_CACHE_L2_SIZE_CHOICE>
```

**定义位置（Location）**：[`soc/espressif/esp32p4/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32p4/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 二级缓存大小（L2 cache size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_CACHE_L2_SIZE_CHOICE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_CACHE_L2_SIZE_CHOICE)。

<a id="CONFIG_ESP32_CACHE_L2_LINE_128B"></a>

## 275.74 `CONFIG_ESP32_CACHE_L2_LINE_128B`

**提示（Prompt）**：128 字节（128 Bytes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_CACHE_L2_LINE_SIZE_CHOICE>
```

**定义位置（Location）**：[`soc/espressif/esp32p4/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32p4/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 二级缓存行大小（L2 cache line size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_CACHE_L2_LINE_SIZE_CHOICE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_CACHE_L2_LINE_SIZE_CHOICE)。

<a id="CONFIG_ESP32_CACHE_L2_LINE_64B"></a>

## 275.75 `CONFIG_ESP32_CACHE_L2_LINE_64B`

**提示（Prompt）**：64 字节（64 Bytes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ESP32_CACHE_L2_128KB || CONFIG_ESP32_CACHE_L2_256KB) && <choice CONFIG_ESP32_CACHE_L2_LINE_SIZE_CHOICE>
```

**定义位置（Location）**：[`soc/espressif/esp32p4/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32p4/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config） → 二级缓存行大小（L2 cache line size）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_CACHE_L2_128KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_CACHE_L2_128KB)、[`CONFIG_ESP32_CACHE_L2_256KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_CACHE_L2_256KB)、[`CONFIG_ESP32_CACHE_L2_LINE_SIZE_CHOICE`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_CACHE_L2_LINE_SIZE_CHOICE)。

<a id="CONFIG_ESP32_CACHE_L2_LINE_SIZE_CHOICE"></a>

## 275.76 `CONFIG_ESP32_CACHE_L2_LINE_SIZE_CHOICE`

**提示（Prompt）**：二级缓存行大小（L2 cache line size）

**说明（Help）**

应用启动时设置的二级缓存行大小（L2 cache line size）。64B 缓存行仅适用于 128KB 和 256KB 缓存；512KB 缓存固定使用 128B 缓存行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32P4 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32_CACHE_L2_LINE_64B if CONFIG_ESP32_CACHE_L2_128KB
CONFIG_ESP32_CACHE_L2_LINE_64B if CONFIG_ESP32_CACHE_L2_256KB
CONFIG_ESP32_CACHE_L2_LINE_128B if CONFIG_ESP32_CACHE_L2_512KB
```

**可选项（Choices）**

```text
CONFIG_ESP32_CACHE_L2_LINE_64B
CONFIG_ESP32_CACHE_L2_LINE_128B
```

**定义位置（Location）**：[`soc/espressif/esp32p4/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32p4/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32_CACHE_L2_LINE_64B`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_CACHE_L2_LINE_64B)、[`CONFIG_ESP32_CACHE_L2_128KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_CACHE_L2_128KB)、[`CONFIG_ESP32_CACHE_L2_256KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_CACHE_L2_256KB)、[`CONFIG_ESP32_CACHE_L2_LINE_128B`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_CACHE_L2_LINE_128B)、[`CONFIG_ESP32_CACHE_L2_512KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_CACHE_L2_512KB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_CACHE_L2_SIZE_CHOICE"></a>

## 275.77 `CONFIG_ESP32_CACHE_L2_SIZE_CHOICE`

**提示（Prompt）**：二级缓存大小（L2 cache size）

**说明（Help）**

应用启动时设置的二级缓存大小（L2 cache size）。L2 缓存从高性能 SRAM（HP SRAM）中划出，因此缓存越大，可用 SRAM 越少。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32P4 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32_CACHE_L2_128KB
```

**可选项（Choices）**

```text
CONFIG_ESP32_CACHE_L2_128KB
CONFIG_ESP32_CACHE_L2_256KB
CONFIG_ESP32_CACHE_L2_512KB
```

**定义位置（Location）**：[`soc/espressif/esp32p4/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32p4/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 缓存配置（Cache config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP32_CACHE_L2_128KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_CACHE_L2_128KB)、[`CONFIG_ESP32_CACHE_L2_256KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_CACHE_L2_256KB)、[`CONFIG_ESP32_CACHE_L2_512KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_CACHE_L2_512KB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_DEEP_SLEEP_WAKEUP_DELAY"></a>

## 275.78 `CONFIG_ESP32_DEEP_SLEEP_WAKEUP_DELAY`

**提示（Prompt）**：深度睡眠唤醒桩代码中的额外延迟，单位为微秒（deep sleep wake stub）

**说明（Help）**

ESP32 退出深度睡眠（deep sleep）时，CPU 和 Flash 芯片同时上电。CPU 先运行深度睡眠桩代码（deep sleep stub），然后从 Flash 加载代码。有些 Flash 芯片要求从上电到首次读取操作之间留出足够时间。默认不增加额外延迟时，这段时间约为 900us，但某些 Flash 芯片需要更长时间。额外延迟默认为 2000us。对需要缩短启动时间的应用进行优化时，可以减小此值。如果深度睡眠复位后控制台出现 `flash read err, 1000` 消息，请尝试增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
2000
```

**取值范围（Ranges）**

```text
[0, 5000]
```

**定义位置（Location）**：[`soc/espressif/esp32/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_EFUSE_VIRTUAL"></a>

## 275.79 `CONFIG_ESP32_EFUSE_VIRTUAL`

**提示（Prompt）**：在 RAM 中模拟 eFuse 操作（Simulate eFuse operations in RAM）

**说明（Help）**

设为 `y` 时，启用虚拟模式（virtual mode），所有 eFuse 读写操作重定向到 RAM，而不是 eFuse 寄存器，所有通过 eFuse 进行的永久修改都会被禁用。此项为 `y` 时不能使用 `SECURE_FLASH_ENCRYPTION_MODE_RELEASE`，因为 EFUSE VIRT 模式仅用于测试。启动时，eFuse 内容会复制到 RAM 中。此模式适合快速测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.efuse:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.efuse#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_EFUSE_VIRTUAL_KEEP_IN_FLASH"></a>

## 275.80 `CONFIG_ESP32_EFUSE_VIRTUAL_KEEP_IN_FLASH`

**提示（Prompt）**：将 eFuse 内容保存在 Flash 中（Keep eFuses in flash）

**说明（Help）**

在“在 RAM 中模拟 eFuse 操作”（Simulate eFuse operations in RAM）的基础上，此选项增加将 eFuse 内容保存在 Flash 中的功能，使其在重启后仍然保留。使用此模式时，分区表（partition_table）应包含 `sys_partition` 分区。启动时，从 Flash 将 eFuse 内容复制到 RAM；如果 Flash 为空，则从真实 eFuse 复制到 RAM，再更新 Flash。需要在重启后保留修改时，此模式很有用，例如测试安全启动（secure_boot）和 Flash 加密（flash_encryption）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_EFUSE_VIRTUAL && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.efuse:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.efuse#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 在 RAM 中模拟 eFuse 操作（Simulate eFuse operations in RAM）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_EFUSE_VIRTUAL`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_EFUSE_VIRTUAL)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_EMAC"></a>

## 275.81 `CONFIG_ESP32_EMAC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于启用 ESP32 以太网介质访问控制驱动（Ethernet MAC driver）的隐藏选项。以太网与管理数据输入／输出（MDIO）都依赖此驱动。此选项允许独立于以太网启用 MDIO。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y if CONFIG_ETH_ESP32
y if CONFIG_ETH_ESP32_DWC_ETHER_1000
y if CONFIG_MDIO_ESP32
```

**定义位置（Location）**：[`soc/espressif/esp32/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ETH_ESP32`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ESP32)、[`CONFIG_ETH_ESP32_DWC_ETHER_1000`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ESP32_DWC_ETHER_1000)、[`CONFIG_MDIO_ESP32`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_MDIO_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_ETM"></a>

## 275.82 `CONFIG_ESP32_ETM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Espressif 事件任务矩阵（Event Task Matrix，ETM）通道分配器。ETM 在硬件中将外设事件路由到外设任务。此符号由需要这种路由的驱动选择，不供用户直接启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ESP32_ETM_SUPPORTED && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**被选择（Selected by）**

```text
CONFIG_COUNTER_TMR_ESP32_CAPTURE
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ESP32_ETM_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_ETM_SUPPORTED)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_COUNTER_TMR_ESP32_CAPTURE`](P069_drivers_counter_配置项参考_2.md#CONFIG_COUNTER_TMR_ESP32_CAPTURE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ESP32_ETM_SUPPORTED`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_PHY_MAX_TX_POWER"></a>

## 275.83 `CONFIG_ESP32_PHY_MAX_TX_POWER`

**提示（Prompt）**：Wi-Fi／BLE／IEEE 802.15.4 最大发送功率，单位为 dBm（Max TX power）

**说明（Help）**

设置 ESP32 无线电的最大发送功率（maximum transmit power）。高数据速率下的实际发送功率可能低于此设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_ESP32 || CONFIG_WIFI_ESP32 || CONFIG_IEEE802154_ESP32) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[10, 20]
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_PM_CPU_RETENTION_DYNAMIC"></a>

## 275.84 `CONFIG_ESP32_PM_CPU_RETENTION_DYNAMIC`

**提示（Prompt）**：动态分配内存（Dynamically allocate memory）

**说明（Help）**

准备进入轻度睡眠（light sleep）时分配保留数据（retention data）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_PM_CPU_RETENTION_STRATEGY>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.pm:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.pm#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Espressif 电源管理配置（PM Config） → 轻度睡眠时关闭 CPU 电源（Power down CPU in light sleep） → 轻度睡眠保留内存分配策略（Retentive memory allocation strategy）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_PM_CPU_RETENTION_STRATEGY`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_PM_CPU_RETENTION_STRATEGY)。

<a id="CONFIG_ESP32_PM_CPU_RETENTION_STATIC"></a>

## 275.85 `CONFIG_ESP32_PM_CPU_RETENTION_STATIC`

**提示（Prompt）**：静态分配内存（Statically allocate memory）

**说明（Help）**

系统初始化期间预先分配所需的全部保留内存（retention memory）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_PM_CPU_RETENTION_STRATEGY>
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.pm:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.pm#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Espressif 电源管理配置（PM Config） → 轻度睡眠时关闭 CPU 电源（Power down CPU in light sleep） → 轻度睡眠保留内存分配策略（Retentive memory allocation strategy）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_PM_CPU_RETENTION_STRATEGY`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_PM_CPU_RETENTION_STRATEGY)。

<a id="CONFIG_ESP32_PM_CPU_RETENTION_STRATEGY"></a>

## 275.86 `CONFIG_ESP32_PM_CPU_RETENTION_STRATEGY`

**提示（Prompt）**：轻度睡眠保留内存分配策略（Retentive memory allocation strategy）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ESP32_PM_CPU_RETENTION_BY_SW && CONFIG_ESP32_PM_POWER_DOWN_CPU_IN_LIGHT_SLEEP && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_PM && CONFIG_TICKLESS_KERNEL && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP32_PM_CPU_RETENTION_DYNAMIC
```

**可选项（Choices）**

```text
CONFIG_ESP32_PM_CPU_RETENTION_DYNAMIC
CONFIG_ESP32_PM_CPU_RETENTION_STATIC
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.pm:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.pm#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Espressif 电源管理配置（PM Config） → 轻度睡眠时关闭 CPU 电源（Power down CPU in light sleep）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ESP32_PM_CPU_RETENTION_BY_SW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_PM_CPU_RETENTION_BY_SW)、[`CONFIG_ESP32_PM_POWER_DOWN_CPU_IN_LIGHT_SLEEP`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_PM_POWER_DOWN_CPU_IN_LIGHT_SLEEP)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_ESP32_PM_CPU_RETENTION_DYNAMIC`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_PM_CPU_RETENTION_DYNAMIC)、[`CONFIG_ESP32_PM_CPU_RETENTION_STATIC`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_PM_CPU_RETENTION_STATIC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ESP32_PM_CPU_RETENTION_BY_SW`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_PM_POWER_DOWN_CPU_IN_LIGHT_SLEEP"></a>

## 275.87 `CONFIG_ESP32_PM_POWER_DOWN_CPU_IN_LIGHT_SLEEP`

**提示（Prompt）**：轻度睡眠时关闭 CPU 电源（Power down CPU in light sleep）

**说明（Help）**

允许在轻度睡眠（light sleep）中关闭 CPU 电源域（power domain）。硬件会保存和恢复 CPU 上下文，因此应用代码不必显式处理该状态转换。保留镜像（retention image）会占用少量内部内存。与保持 CPU 电源域开启相比，这会降低轻度睡眠电流。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ESP32_PM_SUPPORT_CPU_PD && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_PM && CONFIG_TICKLESS_KERNEL && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_ESP32_PM_RESTORE_CACHE_TAGMEM_AFTER_LIGHT_SLEEP if CONFIG_ESP32S3_DATA_CACHE_16KB
```

**被选择（Selected by）**

```text
CONFIG_ESP32_PM_POWER_DOWN_PERIPHERAL_IN_LIGHT_SLEEP
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.pm:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.pm#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Espressif 电源管理配置（PM Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ESP32_PM_SUPPORT_CPU_PD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_PM_SUPPORT_CPU_PD)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_ESP32_PM_RESTORE_CACHE_TAGMEM_AFTER_LIGHT_SLEEP`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_PM_RESTORE_CACHE_TAGMEM_AFTER_LIGHT_SLEEP)、[`CONFIG_ESP32S3_DATA_CACHE_16KB`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32S3_DATA_CACHE_16KB)、[`CONFIG_ESP32_PM_POWER_DOWN_PERIPHERAL_IN_LIGHT_SLEEP`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_PM_POWER_DOWN_PERIPHERAL_IN_LIGHT_SLEEP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ESP32_PM_SUPPORT_CPU_PD`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_PM_POWER_DOWN_PERIPHERAL_IN_LIGHT_SLEEP"></a>

## 275.88 `CONFIG_ESP32_PM_POWER_DOWN_PERIPHERAL_IN_LIGHT_SLEEP`

**提示（Prompt）**：轻度睡眠时关闭数字外设电源（Power down digital peripherals）［实验性，EXPERIMENTAL］

**说明（Help）**

允许在轻度睡眠（light sleep）中关闭主数字外设电源域（TOP）。PAU 和 REGDMA 硬件会在睡眠期间保存并恢复所选外设的寄存器上下文；如果驱动实现了睡眠保留（sleep retention），外设便可恢复运行，无需完整重新初始化。此选项可显著降低轻度睡眠电流，但也增加保留元数据和运行时开销。进入睡眠时会使用堆（heap），因此应确保有足够空闲堆，否则睡眠期间的外设断电可能无法完成。某次睡眠中 TOP 是否真正关闭，仍取决于 HAL 睡眠设置和各驱动的策略；如果系统中的某部分仍需要该电源域，它可能保持开启。

注意：UART 等外设可能运行睡眠前的排空逻辑（pre-sleep flush logic），延长进入睡眠的流程。如果唤醒后无时钟节拍空闲（tickless idle）行为异常，可考虑增加进入睡眠前所需的最小空闲时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ESP32_PM_SUPPORT_TOP_PD && CONFIG_SOC_ESP32_PAU_SUPPORTED && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_PM && CONFIG_TICKLESS_KERNEL && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**主动选择（Selects）**

```text
CONFIG_ESP32_PM_POWER_DOWN_CPU_IN_LIGHT_SLEEP
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.pm:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.pm#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Espressif 电源管理配置（PM Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ESP32_PM_SUPPORT_TOP_PD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_PM_SUPPORT_TOP_PD)、[`CONFIG_SOC_ESP32_PAU_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_PAU_SUPPORTED)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_ESP32_PM_POWER_DOWN_CPU_IN_LIGHT_SLEEP`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_PM_POWER_DOWN_CPU_IN_LIGHT_SLEEP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ESP32_PM_SUPPORT_TOP_PD`、`CONFIG_SOC_ESP32_PAU_SUPPORTED`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_PM_RESTORE_CACHE_TAGMEM_AFTER_LIGHT_SLEEP"></a>

## 275.89 `CONFIG_ESP32_PM_RESTORE_CACHE_TAGMEM_AFTER_LIGHT_SLEEP`

**提示（Prompt）**：CPU 断电的轻度睡眠后恢复指令／数据缓存标记内存（I/D-cache tag memory）

**说明（Help）**

缓存标记内存（cache tag memory）与 CPU 共享 CPU 电源域。启用后，睡眠前会将标记 RAM（tag RAM）备份到内部 RAM，唤醒时恢复，使外部内存的缓存内容在轻度睡眠前后保持有效。禁用时，睡眠前会回写数据缓存（D-cache write-back），唤醒后使其失效；在缓存重新填充之前，外部内存访问会发生缓存未命中（cache miss）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32S3 && CONFIG_ESP32_PM_POWER_DOWN_CPU_IN_LIGHT_SLEEP && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_PM && CONFIG_TICKLESS_KERNEL && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_ESP32_PM_POWER_DOWN_CPU_IN_LIGHT_SLEEP
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.pm:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.pm#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Espressif 电源管理配置（PM Config） → 轻度睡眠时关闭 CPU 电源（Power down CPU in light sleep）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)、[`CONFIG_ESP32_PM_POWER_DOWN_CPU_IN_LIGHT_SLEEP`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_PM_POWER_DOWN_CPU_IN_LIGHT_SLEEP)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_PM_SLP_IRAM_OPT"></a>

## 275.90 `CONFIG_ESP32_PM_SLP_IRAM_OPT`

**提示（Prompt）**：将轻度睡眠路径代码放入内部 RAM（internal RAM）

**说明（Help）**

将轻度睡眠流程的一部分放入指令 RAM（IRAM），使其在缓存暂停时仍能运行。使用轻度睡眠中的 SPI Flash 深度掉电（deep power-down）或 Flash 供电关闭功能（下列选项）时，应启用此项。约占用 2 KB IRAM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_PM && CONFIG_TICKLESS_KERNEL && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**主动选择（Selects）**

```text
CONFIG_ESP32_TIMER_IN_IRAM
```

**被选择（Selected by）**

```text
CONFIG_ESP32_SLEEP_POWER_DOWN_FLASH
CONFIG_ESP32_SLEEP_SET_FLASH_DPD
CONFIG_ESP32_WIFI_SLP_IRAM_OPT
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.pm:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.pm#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Espressif 电源管理配置（PM Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_ESP32_TIMER_IN_IRAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP32_TIMER_IN_IRAM)、[`CONFIG_ESP32_SLEEP_POWER_DOWN_FLASH`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_SLEEP_POWER_DOWN_FLASH)、[`CONFIG_ESP32_SLEEP_SET_FLASH_DPD`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_SLEEP_SET_FLASH_DPD)、[`CONFIG_ESP32_WIFI_SLP_IRAM_OPT`](P188_drivers_wifi_配置项参考_1.md#CONFIG_ESP32_WIFI_SLP_IRAM_OPT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`、`CONFIG_ESP32_TIMER_IN_IRAM`。

<a id="CONFIG_ESP32_PPA"></a>

## 275.91 `CONFIG_ESP32_PPA`

**提示（Prompt）**：ESP32 像素处理加速器（pixel processing accelerator）

**说明（Help）**

启用像素处理加速器（pixel processing accelerator）支持，在硬件中执行填充（fill）、混合（blend）以及缩放－旋转－镜像（scale-rotate-mirror）操作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_PPA_ENABLED && CONFIG_SOC_SERIES_ESP32P4 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.ppa:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.ppa#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32P4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32P4)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32P4`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_PPA_MAX_PENDING"></a>

## 275.92 `CONFIG_ESP32_PPA_MAX_PENDING`

**提示（Prompt）**：操作队列深度（Operation queue depth）

**说明（Help）**

一次可排队的操作数量，包括硬件上正在运行的操作。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_PPA && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.ppa:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.ppa#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → ESP32 像素处理加速器（pixel processing accelerator）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_PPA`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_PPA)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_PPA_WAIT_TIMEOUT_US"></a>

## 275.93 `CONFIG_ESP32_PPA_WAIT_TIMEOUT_US`

**提示（Prompt）**：阻塞操作超时，单位为微秒（Blocking operation timeout）

**说明（Help）**

阻塞操作（blocking operation）在放弃前等待硬件完成的时长。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_PPA && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
100000
```

**取值范围（Ranges）**

```text
[1000, 1000000]
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.ppa:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.ppa#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → ESP32 像素处理加速器（pixel processing accelerator）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_PPA`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_PPA)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_REGION_1_NOINIT"></a>

## 275.94 `CONFIG_ESP32_REGION_1_NOINIT`

**提示（Prompt）**：使用 DRAM 区域 1 容纳 noinit 节（spill noinit section）

**说明（Help）**

ESP32 有两个可用作数据 RAM（DRAM）的存储体（bank），大小分别为 192K 和 128K。启用此项会将 `.noinit` 节分配到 DRAM 区域 1，而非默认区域 0。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y if !(CONFIG_SOC_ENABLE_APPCPU || CONFIG_SOC_ESP32_APPCPU || CONFIG_BOOTLOADER_MCUBOOT)
```

**定义位置（Location）**：[`soc/espressif/esp32/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/esp32/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SOC_ENABLE_APPCPU`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ENABLE_APPCPU)、[`CONFIG_SOC_ESP32_APPCPU`](P276_soc_espressif_配置项参考_2.md#CONFIG_SOC_ESP32_APPCPU)、[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_SLEEP_POWER_DOWN_FLASH"></a>

## 275.95 `CONFIG_ESP32_SLEEP_POWER_DOWN_FLASH`

**提示（Prompt）**：轻度睡眠时关闭 Flash 供电，采用 VDDSDIO 路径（Power down flash supply）

**说明（Help）**

在硬件允许时，轻度睡眠期间关闭 Flash 供电（VDDSDIO／Flash 电源域）。与通过 SPI 命令进入深度掉电（deep power-down）相比，此方式的唤醒延迟更高，约束也更严格。除非 PSRAM 具有独立供电，否则不要在使用 SPIRAM 时启用；Zephyr Kconfig 尚未对独立供电情况建模。风险和开发板要求请参阅 Espressif 睡眠文档。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ESP32_PM_SUPPORT_VDDSDIO_PD && CONFIG_SOC_ESP32_FLASH_SUPPORTED && !CONFIG_SOC_ESP32_PM_FLASH_KEEP_POWER_IN_LSLP && !CONFIG_ESP_SPIRAM && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_PM && CONFIG_TICKLESS_KERNEL && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**主动选择（Selects）**

```text
CONFIG_ESP32_PM_SLP_IRAM_OPT
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.pm:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.pm#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Espressif 电源管理配置（PM Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ESP32_PM_SUPPORT_VDDSDIO_PD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_PM_SUPPORT_VDDSDIO_PD)、[`CONFIG_SOC_ESP32_FLASH_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_FLASH_SUPPORTED)、[`CONFIG_SOC_ESP32_PM_FLASH_KEEP_POWER_IN_LSLP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_PM_FLASH_KEEP_POWER_IN_LSLP)、[`CONFIG_ESP_SPIRAM`](P276_soc_espressif_配置项参考_2.md#CONFIG_ESP_SPIRAM)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_ESP32_PM_SLP_IRAM_OPT`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_PM_SLP_IRAM_OPT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ESP32_PM_SUPPORT_VDDSDIO_PD`、`CONFIG_SOC_ESP32_FLASH_SUPPORTED`、`CONFIG_SOC_ESP32_PM_FLASH_KEEP_POWER_IN_LSLP`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_SLEEP_SET_FLASH_DPD"></a>

## 275.96 `CONFIG_ESP32_SLEEP_SET_FLASH_DPD`

**提示（Prompt）**：轻度睡眠中的 SPI Flash 深度掉电模式（deep power-down mode）

**说明（Help）**

当睡眠时间足够长时，在轻度睡眠期间使主 SPI Flash 进入深度掉电（deep power-down，通常使用命令 B9h）。在许多器件上，与待机相比可节省约 10 uA。此功能要求 Flash 兼容该模式，退出命令通常为 ABh。应根据数据手册调整进入／退出延迟。启用后，SoC 链接器脚本还会将 `clk_utils` 放入指令 RAM（IRAM），使轻度睡眠后的 MSPI／CPU 时钟同步能够在缓存恢复后立即执行，即在 HAL 解除 Flash 深度掉电状态之前执行。此项与上面的“关闭 Flash 供电”（Power down flash supply）互斥。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_ESP32_FLASH_SUPPORTED && !CONFIG_ESP32_SLEEP_POWER_DOWN_FLASH && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_PM && CONFIG_TICKLESS_KERNEL && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**主动选择（Selects）**

```text
CONFIG_ESP32_PM_SLP_IRAM_OPT
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.pm:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.pm#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Espressif 电源管理配置（PM Config）

**配置项引用（Symbol References）**：[`CONFIG_SOC_ESP32_FLASH_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_ESP32_FLASH_SUPPORTED)、[`CONFIG_ESP32_SLEEP_POWER_DOWN_FLASH`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_SLEEP_POWER_DOWN_FLASH)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_ESP32_PM_SLP_IRAM_OPT`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_PM_SLP_IRAM_OPT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_ESP32_FLASH_SUPPORTED`、`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_SLEEP_SPI_FLASH_ENTER_DPD_MODE_DELAY"></a>

## 275.97 `CONFIG_ESP32_SLEEP_SPI_FLASH_ENTER_DPD_MODE_DELAY`

**提示（Prompt）**：SPI Flash 进入深度掉电延迟，单位为微秒（enter deep power-down delay）

**说明（Help）**

发送进入深度掉电命令（enter-DPD）后，CS 必须保持高电平的时间，即数据手册中的 tDP。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_SLEEP_SET_FLASH_DPD && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_PM && CONFIG_TICKLESS_KERNEL && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
25
```

**取值范围（Ranges）**

```text
[0, 100]
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.pm:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.pm#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Espressif 电源管理配置（PM Config） → 轻度睡眠中的 SPI Flash 深度掉电模式（deep power-down mode）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_SLEEP_SET_FLASH_DPD`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_SLEEP_SET_FLASH_DPD)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_SLEEP_SPI_FLASH_EXIT_DPD_MODE_DELAY"></a>

## 275.98 `CONFIG_ESP32_SLEEP_SPI_FLASH_EXIT_DPD_MODE_DELAY`

**提示（Prompt）**：SPI Flash 退出深度掉电延迟，单位为微秒（exit deep power-down delay）

**说明（Help）**

发送退出深度掉电命令（exit-DPD）后，CS 必须保持高电平的时间，即数据手册中的 tRES1。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_SLEEP_SET_FLASH_DPD && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_PM && CONFIG_TICKLESS_KERNEL && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
40
```

**取值范围（Ranges）**

```text
[0, 100]
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.pm:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.pm#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → Espressif 电源管理配置（PM Config） → 轻度睡眠中的 SPI Flash 深度掉电模式（deep power-down mode）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_SLEEP_SET_FLASH_DPD`](P275_soc_espressif_配置项参考_1.md#CONFIG_ESP32_SLEEP_SET_FLASH_DPD)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_SLEEP_WAIT_FLASH_READY_EXTRA_DELAY"></a>

## 275.99 `CONFIG_ESP32_SLEEP_WAIT_FLASH_READY_EXTRA_DELAY`

**提示（Prompt）**：Flash 断电睡眠唤醒后等待 Flash 就绪的额外延迟，单位为微秒（extra delay）

**说明（Help）**

芯片退出睡眠时，CPU 和 Flash 芯片同时上电。CPU 先执行 ROM 代码（深度睡眠）或 RAM 代码（轻度睡眠），然后从 Flash 加载或执行代码。有些 Flash 芯片要求在上电与首次读取操作之间增加时间；没有额外延迟时，这段时间约为 900us。请将此值设为 Flash 数据手册中的 tVSL 减去 900us。如果深度睡眠后出现 `flash read err, 1000`，或轻度睡眠唤醒后触发 RTC_WDT／LP_WDT，请增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_ESPRESSIF_ESP32 && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
2000 if CONFIG_SOC_SERIES_ESP32 || CONFIG_SOC_SERIES_ESP32S3
0
```

**取值范围（Ranges）**

```text
[0, 5000]
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig.flash:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig.flash#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_SOC_SERIES_ESP32`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_SOC_SERIES_ESP32S3`](P277_soc_espressif_配置项参考_3.md#CONFIG_SOC_SERIES_ESP32S3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP32_SW_COEXIST_ENABLE"></a>

## 275.100 `CONFIG_ESP32_SW_COEXIST_ENABLE`

**提示（Prompt）**：由软件控制 Wi-Fi／蓝牙共存（Software controls Wi-Fi/Bluetooth coexistence）

**说明（Help）**

启用后，由软件而非硬件控制 Wi-Fi 与蓝牙共存（coexistence）。建议在高流量场景中使用。两个共存配置选项都由系统自动管理，无需用户干预。如果只使用蓝牙，建议禁用此项以减小二进制文件体积。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_ESP32 || CONFIG_WIFI_ESP32 || CONFIG_IEEE802154_ESP32) && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
y if (CONFIG_BT_ESP32 && CONFIG_WIFI_ESP32) || (CONFIG_WIFI_ESP32 && CONFIG_IEEE802154_ESP32) || (CONFIG_IEEE802154_ESP32 && CONFIG_BT_ESP32)
```

**定义位置（Location）**：[`soc/espressif/common/Kconfig:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/espressif/common/Kconfig#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_WIFI_ESP32`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_ESP32)、[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<!-- kconfig-navigation -->

[上一章](P274_soc_ene_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P276_soc_espressif_配置项参考_2.md)
