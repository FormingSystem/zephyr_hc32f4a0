---
id: learning.zephyr-docs.kconfig-reference.page-3
title: "`Kconfig.zephyr`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第3章\_`Kconfig.zephyr`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `Kconfig.zephyr` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_APPLICATION_DEFINED_SYSCALL"></a>

## 3.1 `CONFIG_APPLICATION_DEFINED_SYSCALL`

**提示（Prompt）**：扫描应用目录中的系统调用定义（Syscall Definitions）。

**说明（Help）**

扫描应用源码目录内的附加目录，查找应用定义的系统调用（Syscalls）。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:940`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L940)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<a id="CONFIG_ASSERT_ON_ERRORS"></a>

## 3.2 `CONFIG_ASSERT_ON_ERRORS`

**提示（Prompt）**：对所有错误执行断言（Assert on All Errors）。

**说明（Help）**

对 `CHECKIF()` 宏覆盖的错误执行断言。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`Kconfig.zephyr:669`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L669)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → `CHECK` 宏的错误检查行为（Error Checking Behavior）。

<a id="CONFIG_BOOTLOADER_BOSSA"></a>

## 3.3 `CONFIG_BOOTLOADER_BOSSA`

**提示（Prompt）**：BOSSA 引导加载程序支持（BOSSA Bootloader Support）。

**说明（Help）**

表示目标使用与 BOSSA 兼容的引导加载程序（Bootloader）。如果还启用了 CDC ACM USB 支持，则运行 `bossac` 时，开发板会自动重启进入引导加载程序。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_USE_DT_CODE_PARTITION
```

**定义位置（Location）**：[`Kconfig.zephyr:1094`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L1094)。

**菜单路径（Menu Path）**：顶层（Top） → 启动选项（Boot Options）。

**配置项引用（Symbol References）**：[`CONFIG_USE_DT_CODE_PARTITION`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_USE_DT_CODE_PARTITION)。

<a id="CONFIG_BOOTLOADER_BOSSA_ADAFRUIT_UF2"></a>

## 3.4 `CONFIG_BOOTLOADER_BOSSA_ADAFRUIT_UF2`

**提示（Prompt）**：Adafruit UF2。

**说明（Help）**

选择 BOSSA 引导加载程序的 Adafruit UF2 变体，使用魔数（Magic Value）`0xf01669ef` 进入引导加载程序。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`Kconfig.zephyr:1127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L1127)。

**菜单路径（Menu Path）**：顶层（Top） → 启动选项（Boot Options）。 → BOSSA 引导加载程序支持（BOSSA Bootloader Support）。 → BOSSA 引导加载程序变体（Bootloader Variant）。

<a id="CONFIG_BOOTLOADER_BOSSA_ARDUINO"></a>

## 3.5 `CONFIG_BOOTLOADER_BOSSA_ARDUINO`

**提示（Prompt）**：Arduino。

**说明（Help）**

选择 BOSSA 引导加载程序的 Arduino 变体，使用魔数（Magic Value）`0x07738135` 进入引导加载程序。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`Kconfig.zephyr:1121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L1121)。

**菜单路径（Menu Path）**：顶层（Top） → 启动选项（Boot Options）。 → BOSSA 引导加载程序支持（BOSSA Bootloader Support）。 → BOSSA 引导加载程序变体（Bootloader Variant）。

<a id="CONFIG_BOOTLOADER_BOSSA_DEVICE_NAME"></a>

## 3.6 `CONFIG_BOOTLOADER_BOSSA_DEVICE_NAME`

**提示（Prompt）**：BOSSA CDC ACM 设备名称（Device Name）。

**说明（Help）**

设置用于监听重启命令的 CDC ACM 端口。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BOOTLOADER_BOSSA && CONFIG_CDC_ACM_DTE_RATE_CALLBACK_SUPPORT
```

**默认值（Defaults）**

```text
"CDC_ACM_0"
```

**定义位置（Location）**：[`Kconfig.zephyr:1103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L1103)。

**菜单路径（Menu Path）**：顶层（Top） → 启动选项（Boot Options）。 → BOSSA 引导加载程序支持（BOSSA Bootloader Support）。

**配置项引用（Symbol References）**：[`CONFIG_BOOTLOADER_BOSSA`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BOOTLOADER_BOSSA)、[`CONFIG_CDC_ACM_DTE_RATE_CALLBACK_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CDC_ACM_DTE_RATE_CALLBACK_SUPPORT)。

<a id="CONFIG_BOOTLOADER_BOSSA_LEGACY"></a>

## 3.7 `CONFIG_BOOTLOADER_BOSSA_LEGACY`

**提示（Prompt）**：传统变体（Legacy）。

**说明（Help）**

选择 BOSSA 引导加载程序的传统变体（Legacy）。它仅用于兼容模式，推荐使用 Arduino 或 Adafruit UF2 等较新版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`Kconfig.zephyr:1114`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L1114)。

**菜单路径（Menu Path）**：顶层（Top） → 启动选项（Boot Options）。 → BOSSA 引导加载程序支持（BOSSA Bootloader Support）。 → BOSSA 引导加载程序变体（Bootloader Variant）。

<a id="CONFIG_BUILD_ALIGN_LMA"></a>

## 3.8 `CONFIG_BUILD_ALIGN_LMA`

**提示（Prompt）**：对齐输出镜像中的加载内存地址（LMA）。

**说明（Help）**

确保输出镜像每个节（Section）的加载内存地址（Load Memory Address，LMA）满足该节的对齐要求。`objcopy` 等工具需要满足此条件，才能调整 ELF 文件的 LMA。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y if CONFIG_BUILD_OUTPUT_ADJUST_LMA != ""
```

**定义位置（Location）**：[`Kconfig.zephyr:931`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L931)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

**配置项引用（Symbol References）**：[`CONFIG_BUILD_OUTPUT_ADJUST_LMA`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BUILD_OUTPUT_ADJUST_LMA)。

<a id="CONFIG_BUILD_GAP_FILL_PATTERN"></a>

## 3.9 `CONFIG_BUILD_GAP_FILL_PATTERN`

**提示（Prompt）**：空隙填充模式（Gap Fill Pattern）。

**说明（Help）**

用于填充输出文件空隙的数值模式。应将其设为擦除后闪存的值，这可显著缩短闪存写入时间。本设置仅定义空隙填充模式，不会启用填充。注意，二进制文件不含地址信息，因此始终会填充空隙。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**默认值（Defaults）**

```text
0xFF
```

**定义位置（Location）**：[`Kconfig.zephyr:758`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L758)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<a id="CONFIG_BUILD_OUTPUT_ADJUST_LMA"></a>

## 3.10 `CONFIG_BUILD_OUTPUT_ADJUST_LMA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用提供的值调整最终 ELF 和 HEX 文件的加载内存地址（LMA），不会影响镜像内部的地址符号。这可用于为烧录工具或多阶段加载器调整 LMA；例如，预加载程序可能先将镜像复制到另一位置，再启动第二个处理器核。该值按数学表达式求值，以下表达式均有效：

- `1024`
- `0x1000`
- `-0x1000`
- `0x20000000 - 0x10000000`

注意，允许负数。若要根据所选闪存分区调整，可以指定如下默认值：

```kconfig
DT_CHOSEN_IMAGE_<name> := <name>,<name>-partition
DT_CHOSEN_Z_FLASH := zephyr,flash
config BUILD_OUTPUT_ADJUST_LMA
  default "$(dt_chosen_reg_addr_hex,$(DT_CHOSEN_IMAGE_<name>))-\
           $(dt_chosen_reg_addr_hex,$(DT_CHOSEN_Z_FLASH))"
```

**类型（Type）**：字符串（String），`string`。

**定义位置（Location）**：[`Kconfig.zephyr:879`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L879)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<a id="CONFIG_BUILD_OUTPUT_ADJUST_LMA_SECTIONS"></a>

## 3.11 `CONFIG_BUILD_OUTPUT_ADJUST_LMA_SECTIONS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

确定上述加载内存地址（LMA）调整应用于哪些输出节（Section）。其值可以是最终 ELF 中的节名称，例如 `"text"`，也可以是 `"*bss"` 等可能匹配多个节的通配符模式。多个模式可用分号 `;` 分隔。还可提供以 `!` 开头的“否定”模式，排除前面模式已匹配的节。

默认调整所有节的 LMA。下面示例排除由代码重定位（Code Relocation）功能生成的一个节：

```kconfig
config BUILD_OUTPUT_ADJUST_LMA_SECTIONS
  default "*;!.extflash_text_reloc"
```

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_OUTPUT_ADJUST_LMA != ""
```

**默认值（Defaults）**

```text
"*"
```

**定义位置（Location）**：[`Kconfig.zephyr:903`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L903)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

**配置项引用（Symbol References）**：[`CONFIG_BUILD_OUTPUT_ADJUST_LMA`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BUILD_OUTPUT_ADJUST_LMA)。

<a id="CONFIG_BUILD_OUTPUT_BIN"></a>

## 3.12 `CONFIG_BUILD_OUTPUT_BIN`

**提示（Prompt）**：构建 BIN 格式的二进制文件。

**说明（Help）**

在构建目录生成“原始”二进制文件 `zephyr/zephyr.bin`。可通过 `CONFIG_KERNEL_BIN_NAME` 自定义文件名。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_ESPRESSIF_QEMU
CONFIG_SOC_FAMILY_KB106X
CONFIG_SOC_SERIES_PSOC4000T
CONFIG_SOC_SERIES_PSOC4100SMAX
CONFIG_SOC_SERIES_PSOC4100TP
CONFIG_SOC_AM13E23019
CONFIG_SOC_SERIES_PSE84
CONFIG_SOC_SERIES_CYW20829
CONFIG_SOC_SERIES_PSC3
CONFIG_SOC_FAMILY_GANYMED
CONFIG_SOC_SERIES_MSPM0G
CONFIG_SOC_SERIES_MSPM0L
CONFIG_SOC_SERIES_MSPM33C
CONFIG_SOC_SERIES_STM32N6X
```

**定义位置（Location）**：[`Kconfig.zephyr:781`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L781)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

**配置项引用（Symbol References）**：[`CONFIG_ESPRESSIF_QEMU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESPRESSIF_QEMU)、[`CONFIG_SOC_FAMILY_KB106X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KB106X)、[`CONFIG_SOC_SERIES_PSOC4000T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4000T)、[`CONFIG_SOC_SERIES_PSOC4100SMAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4100SMAX)、[`CONFIG_SOC_SERIES_PSOC4100TP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4100TP)、[`CONFIG_SOC_AM13E23019`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM13E23019)、[`CONFIG_SOC_SERIES_PSE84`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84)、[`CONFIG_SOC_SERIES_CYW20829`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYW20829)、[`CONFIG_SOC_SERIES_PSC3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSC3)、[`CONFIG_SOC_FAMILY_GANYMED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_GANYMED)、[`CONFIG_SOC_SERIES_MSPM0G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM0G)、[`CONFIG_SOC_SERIES_MSPM0L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM0L)、[`CONFIG_SOC_SERIES_MSPM33C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM33C)、[`CONFIG_SOC_SERIES_STM32N6X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_STM32N6X)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_KB106X`、`CONFIG_SOC_AM13E23019`、`CONFIG_SOC_SERIES_PSE84`、`CONFIG_SOC_SERIES_CYW20829`、`CONFIG_SOC_SERIES_PSC3`、`CONFIG_SOC_FAMILY_GANYMED`、`CONFIG_SOC_SERIES_STM32N6X`。

<a id="CONFIG_BUILD_OUTPUT_COMPRESS_DEBUG_SECTIONS"></a>

## 3.13 `CONFIG_BUILD_OUTPUT_COMPRESS_DEBUG_SECTIONS`

**提示（Prompt）**：压缩 ELF 文件中的调试节（Debug Sections）。

**说明（Help）**

压缩 ELF 文件的调试节（Debug Sections），以减小文件大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:874`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L874)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<a id="CONFIG_BUILD_OUTPUT_EFI"></a>

## 3.14 `CONFIG_BUILD_OUTPUT_EFI`

**提示（Prompt）**：构建为 EFI 应用（EFI Application）。

**说明（Help）**

构建为可扩展固件接口应用（EFI Application）。具体方式是从已构建的 `zephyr.elf` 提取 Zephyr 镜像，生成包含该镜像的 EFI 二进制文件 `zephyr.efi`。EFI 应用可重定位，不能放在指定的内存位置；启动时，入口包装代码（Stub Code）将嵌入的 Zephyr 各节复制到适当位置，清零 BSS 等零填充区域，然后跳转到 64 位入口点。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_X86_64
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`Kconfig.zephyr:788`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L788)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

**配置项引用（Symbol References）**：[`CONFIG_X86_64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_64)。

<a id="CONFIG_BUILD_OUTPUT_EXE"></a>

## 3.15 `CONFIG_BUILD_OUTPUT_EXE`

**提示（Prompt）**：构建扩展名为 `.exe` 的 ELF 格式二进制文件。

**说明（Help）**

在构建目录生成可在主机系统运行的 ELF 二进制文件 `zephyr/zephyr.exe`。可通过 `CONFIG_KERNEL_BIN_NAME` 自定义文件名。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:802`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L802)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<a id="CONFIG_BUILD_OUTPUT_HEX"></a>

## 3.16 `CONFIG_BUILD_OUTPUT_HEX`

**提示（Prompt）**：构建 HEX 格式的二进制文件。

**说明（Help）**

在构建目录生成 Intel HEX 文件 `zephyr/zephyr.hex`。可通过 `CONFIG_KERNEL_BIN_NAME` 自定义文件名。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_BUILD_WITH_TFM
CONFIG_BUILD_WITH_TFM
CONFIG_SOC_FAMILY_KB106X
CONFIG_SOC_SERIES_PSOC4000T
CONFIG_SOC_SERIES_PSOC4100SMAX
CONFIG_SOC_SERIES_PSOC4100TP
CONFIG_SOC_AM13E23019
CONFIG_SOC_FAMILY_CH32V
CONFIG_SOC_FT9001
CONFIG_SOC_FAMILY_SILABS_S0
CONFIG_SOC_FAMILY_SILABS_S1
CONFIG_SOC_FAMILY_SILABS_S2
CONFIG_SOC_FAMILY_SILABS_S3
CONFIG_SOC_FAMILY_SILABS_SIM3
CONFIG_NXP_FLEXSPI_ROM_RAMLOADER
CONFIG_SOC_SERIES_TM4C123X
CONFIG_SOC_FAMILY_REALTEK_AMEBA
CONFIG_SOC_FAMILY_PSOC6
CONFIG_SOC_FAMILY_PSOC6_LEGACY
CONFIG_SOC_SERIES_PSE84
CONFIG_SOC_SERIES_CYW20829
CONFIG_SOC_SERIES_PSC3
CONFIG_SOC_FAMILY_GD_GD32
CONFIG_SOC_SERIES_CC23X0
CONFIG_SOC_OPENISA_RV32M1
CONFIG_SOC_FAMILY_REALTEK_BEE
CONFIG_SOC_FAMILY_MAX32
CONFIG_SOC_SERIES_MSPM0G
CONFIG_SOC_SERIES_MSPM0L
CONFIG_SOC_SERIES_MSPM33C
CONFIG_SOC_FAMILY_STM32
CONFIG_SOC_SERIES_MUSCA
CONFIG_NXP_FLEXSPI_ROM_RAMLOADER
```

**定义位置（Location）**：[`Kconfig.zephyr:770`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L770)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_WITH_TFM)、[`CONFIG_SOC_FAMILY_KB106X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_KB106X)、[`CONFIG_SOC_SERIES_PSOC4000T`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4000T)、[`CONFIG_SOC_SERIES_PSOC4100SMAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4100SMAX)、[`CONFIG_SOC_SERIES_PSOC4100TP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSOC4100TP)、[`CONFIG_SOC_AM13E23019`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_AM13E23019)、[`CONFIG_SOC_FAMILY_CH32V`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_CH32V)、[`CONFIG_SOC_FT9001`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FT9001)、[`CONFIG_SOC_FAMILY_SILABS_S0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S0)、[`CONFIG_SOC_FAMILY_SILABS_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S1)、[`CONFIG_SOC_FAMILY_SILABS_S2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S2)、[`CONFIG_SOC_FAMILY_SILABS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3)、[`CONFIG_SOC_FAMILY_SILABS_SIM3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_SIM3)、[`CONFIG_NXP_FLEXSPI_ROM_RAMLOADER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_FLEXSPI_ROM_RAMLOADER)、[`CONFIG_SOC_SERIES_TM4C123X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_TM4C123X)、[`CONFIG_SOC_FAMILY_REALTEK_AMEBA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_AMEBA)、[`CONFIG_SOC_FAMILY_PSOC6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6)、[`CONFIG_SOC_FAMILY_PSOC6_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_PSOC6_LEGACY)、[`CONFIG_SOC_SERIES_PSE84`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSE84)、[`CONFIG_SOC_SERIES_CYW20829`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CYW20829)、[`CONFIG_SOC_SERIES_PSC3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_PSC3)、[`CONFIG_SOC_FAMILY_GD_GD32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_GD_GD32)、[`CONFIG_SOC_SERIES_CC23X0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_CC23X0)、[`CONFIG_SOC_OPENISA_RV32M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENISA_RV32M1)、[`CONFIG_SOC_FAMILY_REALTEK_BEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_REALTEK_BEE)、[`CONFIG_SOC_FAMILY_MAX32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32)、[`CONFIG_SOC_SERIES_MSPM0G`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM0G)、[`CONFIG_SOC_SERIES_MSPM0L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM0L)、[`CONFIG_SOC_SERIES_MSPM33C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MSPM33C)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_SOC_SERIES_MUSCA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_MUSCA)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_KB106X`、`CONFIG_SOC_AM13E23019`、`CONFIG_SOC_FAMILY_CH32V`、`CONFIG_SOC_FAMILY_SILABS_S0`、`CONFIG_SOC_FAMILY_SILABS_S1`、`CONFIG_SOC_FAMILY_SILABS_S2`、`CONFIG_SOC_FAMILY_SILABS_S3`、`CONFIG_SOC_FAMILY_SILABS_SIM3`、`CONFIG_SOC_SERIES_TM4C123X`、`CONFIG_SOC_FAMILY_REALTEK_AMEBA`、`CONFIG_SOC_FAMILY_PSOC6`、`CONFIG_SOC_FAMILY_PSOC6_LEGACY`、`CONFIG_SOC_SERIES_PSE84`、`CONFIG_SOC_SERIES_CYW20829`、`CONFIG_SOC_SERIES_PSC3`、`CONFIG_SOC_FAMILY_GD_GD32`、`CONFIG_SOC_FAMILY_REALTEK_BEE`、`CONFIG_SOC_FAMILY_MAX32`、`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_BUILD_OUTPUT_HEX_GAP_FILL"></a>

## 3.17 `CONFIG_BUILD_OUTPUT_HEX_GAP_FILL`

**提示（Prompt）**：填充 HEX 文件中的空隙（Fill Gaps）。

**说明（Help）**

填充基于 HEX 格式文件中的空隙。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING
```

**定义位置（Location）**：[`Kconfig.zephyr:776`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L776)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING)。

<a id="CONFIG_BUILD_OUTPUT_INFO_HEADER"></a>

## 3.18 `CONFIG_BUILD_OUTPUT_INFO_HEADER`

**提示（Prompt）**：创建镜像信息头文件（Image Information Header）。

**说明（Help）**

创建包含 Zephyr 二进制镜像信息的头文件，例如镜像中的段（Segment）数量、每段的加载内存地址（LMA）、虚拟内存地址（VMA）及大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:920`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L920)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<a id="CONFIG_BUILD_OUTPUT_META"></a>

## 3.19 `CONFIG_BUILD_OUTPUT_META`

**提示（Prompt）**：创建构建元信息文件（Build Meta File）。

**说明（Help）**

在构建目录创建元信息文件（Build Meta File），列出以下信息：Zephyr 的路径和修订版本（若为 Git 仓库）；Zephyr 模块的名称、路径和修订版本（若为 Git 仓库）；west 清单（Manifest）的路径和修订版本；west 项目的路径和修订版本；以及工作区状态。

工作区状态包括：

- `dirty`：一个或多个仓库被标记为有未提交修改。
- `extra`：手动将额外的 Zephyr 模块加入构建。
- `off`：一个或多个 west 项目的 SHA 与上次运行 `west update` 时清单规定的版本（`manifest-rev`）不同；仅在找到 west 工作区时才有此状态。

文件扩展名为 `.meta`。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:952`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L952)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<a id="CONFIG_BUILD_OUTPUT_META_STATE_PROPAGATE"></a>

## 3.20 `CONFIG_BUILD_OUTPUT_META_STATE_PROPAGATE`

**提示（Prompt）**：传播模块与项目状态（Propagate Module and Project State）。

**说明（Help）**

将每个模块的状态传播到 Zephyr 修订版本字段。如果使用 west，也将每个 west 项目的状态传播到该字段；west 清单仓库的修订版本字段同样标记为与 Zephyr 修订版本一致的状态。最终版本形式为 `<SHA>-<state1>-<state2>-<state3>...`。若 SHA 后未附加状态，则表示本次构建来自干净的源码树（Clean Tree）。

- `dirty`：一个或多个仓库被标记为有未提交修改。
- `extra`：手动将额外的 Zephyr 模块加入构建。
- `off`：一个或多个 west 项目的 SHA 与上次运行 `west update` 时清单规定的版本（`manifest-rev`）不同；仅在找到 west 工作区时才有此状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_OUTPUT_META
```

**定义位置（Location）**：[`Kconfig.zephyr:969`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L969)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。 → 创建构建元信息文件（Build Meta File）。

**配置项引用（Symbol References）**：[`CONFIG_BUILD_OUTPUT_META`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BUILD_OUTPUT_META)。

<a id="CONFIG_BUILD_OUTPUT_MOT"></a>

## 3.21 `CONFIG_BUILD_OUTPUT_MOT`

**提示（Prompt）**：构建 MOT 格式的二进制文件。

**说明（Help）**

在构建目录生成 MOT 文件 `zephyr/zephyr.mot`。可通过 `CONFIG_KERNEL_BIN_NAME` 自定义文件名。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_RENESAS_RX
```

**定义位置（Location）**：[`Kconfig.zephyr:841`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L841)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_RENESAS_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_RENESAS_RX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_RENESAS_RX`。

<a id="CONFIG_BUILD_OUTPUT_S19"></a>

## 3.22 `CONFIG_BUILD_OUTPUT_S19`

**提示（Prompt）**：构建 S19 格式的二进制文件。

**说明（Help）**

在构建目录生成 S19 文件 `zephyr/zephyr.s19`。可通过 `CONFIG_KERNEL_BIN_NAME` 自定义文件名。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:809`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L809)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<a id="CONFIG_BUILD_OUTPUT_S19_GAP_FILL"></a>

## 3.23 `CONFIG_BUILD_OUTPUT_S19_GAP_FILL`

**提示（Prompt）**：填充 S19 文件中的空隙（Fill Gaps）。

**说明（Help）**

填充基于 S19 格式文件中的空隙。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:815`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L815)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<a id="CONFIG_BUILD_OUTPUT_STRIPPED"></a>

## 3.24 `CONFIG_BUILD_OUTPUT_STRIPPED`

**提示（Prompt）**：构建剥离符号的二进制文件（Stripped Binary）。

**说明（Help）**

在构建目录生成剥离符号的二进制文件 `zephyr/zephyr.strip`。可通过 `CONFIG_KERNEL_BIN_NAME` 自定义文件名。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:868`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L868)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<a id="CONFIG_BUILD_OUTPUT_STRIP_PATHS"></a>

## 3.25 `CONFIG_BUILD_OUTPUT_STRIP_PATHS`

**提示（Prompt）**：从二进制文件中剔除绝对路径（Strip Absolute Paths）。

**说明（Help）**

如果编译器支持，从 `__ASSERT*` 使用的 `__FILE__` 宏、`.noinit` 节名称及所有应用代码中剔除 `$(ZEPHYR_BASE)` 前缀。例如，原文以 `.noinit` 节名称中包含某个用户工作区下 `fu/bar.c` 的完整路径为例，说明需要剔除的前缀。这样可以节省内存，避免二进制文件泄露用户位置，使失败日志更稳定，并提高构建的确定性（Determinism）。调试器通常提供路径映射（Path Mapping）功能，以确保仍能找到源码文件。译注：此处用读者自己的源码根说明原文示例，不将示例用户目录写成固定路径。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`Kconfig.zephyr:987`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L987)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<a id="CONFIG_BUILD_OUTPUT_UF2"></a>

## 3.26 `CONFIG_BUILD_OUTPUT_UF2`

**提示（Prompt）**：构建 UF2 格式的二进制文件。

**说明（Help）**

在构建目录生成 UF2 文件 `zephyr/zephyr.uf2`。可通过 `CONFIG_KERNEL_BIN_NAME` 自定义文件名。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_OUTPUT_BIN || CONFIG_BUILD_OUTPUT_HEX
```

**定义位置（Location）**：[`Kconfig.zephyr:834`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L834)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

**配置项引用（Symbol References）**：[`CONFIG_BUILD_OUTPUT_BIN`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BUILD_OUTPUT_BIN)、[`CONFIG_BUILD_OUTPUT_HEX`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BUILD_OUTPUT_HEX)。

<a id="CONFIG_BUILD_OUTPUT_UF2_FAMILY_ID"></a>

## 3.27 `CONFIG_BUILD_OUTPUT_UF2_FAMILY_ID`

**提示（Prompt）**：UF2 设备系列标识符（Device Family ID）。

**说明（Help）**

UF2 引导加载程序只接受系列标识符（Family ID）匹配的 UF2 文件。该值可以是十六进制数，例如 `0x68ed2b88`，也可以是已知的系列名称字符串。若 UF2 已知当前使用的 SoC，会预填其已知系列 ID。SoC 专用默认值在 SoC 层的 `Kconfig.defconfig` 文件中设置。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_OUTPUT_UF2
```

**定义位置（Location）**：[`Kconfig.zephyr:849`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L849)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

**配置项引用（Symbol References）**：[`CONFIG_BUILD_OUTPUT_UF2`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BUILD_OUTPUT_UF2)。

<a id="CONFIG_BUILD_OUTPUT_VERILOG"></a>

## 3.28 `CONFIG_BUILD_OUTPUT_VERILOG`

**提示（Prompt）**：构建 Verilog 内存十六进制转储格式（Memory Hex Dump）的文件。

**说明（Help）**

在构建目录生成 Verilog 内存十六进制转储文件 `zephyr/zephyr.mem`。可通过 `CONFIG_KERNEL_BIN_NAME` 自定义文件名。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:820`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L820)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<a id="CONFIG_BUILD_OUTPUT_VERILOG_DATA_WIDTH"></a>

## 3.29 `CONFIG_BUILD_OUTPUT_VERILOG_DATA_WIDTH`

**提示（Prompt）**：Verilog 输出格式的数据宽度（Data Width）。

**说明（Help）**

Verilog 内存十六进制转储输出格式的数据元素宽度，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_OUTPUT_VERILOG
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`Kconfig.zephyr:827`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L827)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。 → 构建 Verilog 内存十六进制转储格式（Memory Hex Dump）的文件。

**配置项引用（Symbol References）**：[`CONFIG_BUILD_OUTPUT_VERILOG`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BUILD_OUTPUT_VERILOG)。

<a id="CONFIG_CHECK_INIT_PRIORITIES"></a>

## 3.30 `CONFIG_CHECK_INIT_PRIORITIES`

**提示（Prompt）**：构建时初始化优先级检查（Initialization Priorities Check）。

**说明（Help）**

将构建中的初始化优先级与从设备树（Devicetree）定义推导的设备依赖关系进行比较，检查初始化优先级问题。出现优先级错误，例如依赖设备的优先级顺序颠倒时，使构建失败。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!(CONFIG_NATIVE_LIBRARY && (!CONFIG_BUILD_OUTPUT_EXE || CONFIG_NATIVE_SIMULATOR_EXTRA_IMAGE_PATHS != "")) && "zephyr" != "armclang"
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`Kconfig.zephyr:1001`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L1001)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

**配置项引用（Symbol References）**：[`CONFIG_NATIVE_LIBRARY`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NATIVE_LIBRARY)、[`CONFIG_BUILD_OUTPUT_EXE`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BUILD_OUTPUT_EXE)、[`CONFIG_NATIVE_SIMULATOR_EXTRA_IMAGE_PATHS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NATIVE_SIMULATOR_EXTRA_IMAGE_PATHS)。

<a id="CONFIG_CLEANUP_INTERMEDIATE_FILES"></a>

## 3.31 `CONFIG_CLEANUP_INTERMEDIATE_FILES`

**提示（Prompt）**：移除所有中间文件（Intermediate Files）。

**说明（Help）**

删除中间文件，以节省空间并清理构建过程产生的杂项。注意，这会破坏增量构建（Incremental Build）、`west spdx` 软件物料清单（Software Bill of Materials）生成，还可能影响其他功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:751`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L751)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<a id="CONFIG_CMAKE_LINKER_GENERATOR"></a>

## 3.32 `CONFIG_CMAKE_LINKER_GENERATOR`

**提示（Prompt）**：CMake 生成器（CMake Generator）。

**说明（Help）**

选择本选项，使用 Zephyr 的 CMake 链接脚本生成器（Linker Script Generator）。链接配置由 CMake 编写，最终链接脚本由工具链专用生成器生成。基于 LD 的链接器使用 ld 生成器；基于 ARMClang／armlink 的链接器使用分散加载文件生成器（Scatter Generator）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM && <choice CONFIG_LINKER_SCRIPT>
```

**定义位置（Location）**：[`Kconfig.zephyr:210`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L210)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。 → 链接脚本（Linker Script）。

**配置项引用（Symbol References）**：[`CONFIG_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM)、[`CONFIG_LINKER_SCRIPT`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LINKER_SCRIPT)。

<a id="CONFIG_CODING_GUIDELINE_CHECK"></a>

## 3.33 `CONFIG_CODING_GUIDELINE_CHECK`

**提示（Prompt）**：强制执行编码规范（Coding Guidelines）。

**说明（Help）**

使用可用的编译器标志，在构建期间检查编码规范规则。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:415`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L415)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

<a id="CONFIG_COMPILER_CODEGEN_VLIW"></a>

## 3.34 `CONFIG_COMPILER_CODEGEN_VLIW`

**提示（Prompt）**：超长指令字（Very Long Instruction Word，VLIW）。

**说明（Help）**

指定编译器是否使用超长指令字（VLIW）指令。VLIW 允许编译器合并指令以并行执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
CONFIG_COMPILER_CODEGEN_VLIW_AUTO
```

**可选项（Choices）**

```text
CONFIG_COMPILER_CODEGEN_VLIW_AUTO
CONFIG_COMPILER_CODEGEN_VLIW_ENABLED
CONFIG_COMPILER_CODEGEN_VLIW_DISABLED
```

**定义位置（Location）**：[`Kconfig.zephyr:634`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L634)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。 → 代码生成（Code Generation）。

**配置项引用（Symbol References）**：[`CONFIG_COMPILER_CODEGEN_VLIW_AUTO`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_COMPILER_CODEGEN_VLIW_AUTO)、[`CONFIG_COMPILER_CODEGEN_VLIW_ENABLED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_COMPILER_CODEGEN_VLIW_ENABLED)、[`CONFIG_COMPILER_CODEGEN_VLIW_DISABLED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_COMPILER_CODEGEN_VLIW_DISABLED)。

<a id="CONFIG_COMPILER_CODEGEN_VLIW_AUTO"></a>

## 3.35 `CONFIG_COMPILER_CODEGEN_VLIW_AUTO`

**提示（Prompt）**：自动（Auto）。

**说明（Help）**

由编译器决定是否生成超长指令字（VLIW）指令，通常意味着使用编译器默认设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COMPILER_CODEGEN_VLIW>
```

**定义位置（Location）**：[`Kconfig.zephyr:642`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L642)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。 → 代码生成（Code Generation）。 → 超长指令字（Very Long Instruction Word，VLIW）。

**配置项引用（Symbol References）**：[`CONFIG_COMPILER_CODEGEN_VLIW`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_COMPILER_CODEGEN_VLIW)。

<a id="CONFIG_COMPILER_CODEGEN_VLIW_DISABLED"></a>

## 3.36 `CONFIG_COMPILER_CODEGEN_VLIW_DISABLED`

**提示（Prompt）**：不生成超长指令字（VLIW）。

**说明（Help）**

明确要求编译器绝不生成超长指令字（VLIW）指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COMPILER_CODEGEN_VLIW>
```

**定义位置（Location）**：[`Kconfig.zephyr:654`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L654)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。 → 代码生成（Code Generation）。 → 超长指令字（Very Long Instruction Word，VLIW）。

**配置项引用（Symbol References）**：[`CONFIG_COMPILER_CODEGEN_VLIW`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_COMPILER_CODEGEN_VLIW)。

<a id="CONFIG_COMPILER_CODEGEN_VLIW_ENABLED"></a>

## 3.37 `CONFIG_COMPILER_CODEGEN_VLIW_ENABLED`

**提示（Prompt）**：生成超长指令字（VLIW）。

**说明（Help）**

明确要求编译器在可能时生成超长指令字（VLIW）指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COMPILER_CODEGEN_VLIW>
```

**定义位置（Location）**：[`Kconfig.zephyr:649`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L649)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。 → 代码生成（Code Generation）。 → 超长指令字（Very Long Instruction Word，VLIW）。

**配置项引用（Symbol References）**：[`CONFIG_COMPILER_CODEGEN_VLIW`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_COMPILER_CODEGEN_VLIW)。

<a id="CONFIG_COMPILER_COLOR_DIAGNOSTICS"></a>

## 3.38 `CONFIG_COMPILER_COLOR_DIAGNOSTICS`

**提示（Prompt）**：彩色诊断信息（Colored Diagnostics）。

**说明（Help）**

对编译器诊断消息使用颜色显示。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`Kconfig.zephyr:555`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L555)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

<a id="CONFIG_COMPILER_FREESTANDING"></a>

## 3.39 `CONFIG_COMPILER_FREESTANDING`

**提示（Prompt）**：以独立式编译器模式构建（Freestanding Mode）。

**说明（Help）**

按照 C 和 C++ 语言规范，将编译器配置为独立式模式（Freestanding Mode）。此模式降低对编译器及语言环境的要求，可能削弱编译器检测错误和执行优化的能力。

**类型（Type）**：布尔值（Boolean），`bool`。

**被弱选择（Implied by）**

```text
CONFIG_MINIMAL_LIBC
```

**定义位置（Location）**：[`Kconfig.zephyr:449`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L449)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

**配置项引用（Symbol References）**：[`CONFIG_MINIMAL_LIBC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MINIMAL_LIBC)。

<a id="CONFIG_COMPILER_OPT"></a>

## 3.40 `CONFIG_COMPILER_OPT`

**提示（Prompt）**：自定义编译器选项（Custom Compiler Options）。

**说明（Help）**

这是一个自由格式字符串，在构建项目所有部分（例如内核）时传给编译器。其中指定的选项补充构建系统预定义的编译器选项集，可用于改变编译优化、警告与错误消息等。

**类型（Type）**：字符串（String），`string`。

**定义位置（Location）**：[`Kconfig.zephyr:593`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L593)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

<a id="CONFIG_COMPILER_OPTIMIZATIONS"></a>

## 3.41 `CONFIG_COMPILER_OPTIMIZATIONS`

**提示（Prompt）**：优化级别（Optimization Level）。

**说明（Help）**

注意，这些标志只能控制编译器优化级别，不得依据它们条件编译额外的调试代码。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
CONFIG_NO_OPTIMIZATIONS if CONFIG_COVERAGE
CONFIG_DEBUG_OPTIMIZATIONS if CONFIG_DEBUG
CONFIG_SIZE_OPTIMIZATIONS_AGGRESSIVE if "" = "llvm"
CONFIG_SIZE_OPTIMIZATIONS
```

**可选项（Choices）**

```text
CONFIG_SIZE_OPTIMIZATIONS
CONFIG_SIZE_OPTIMIZATIONS_AGGRESSIVE
CONFIG_SPEED_OPTIMIZATIONS
CONFIG_DEBUG_OPTIMIZATIONS
CONFIG_NO_OPTIMIZATIONS
```

**定义位置（Location）**：[`Kconfig.zephyr:458`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L458)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

**配置项引用（Symbol References）**：[`CONFIG_NO_OPTIMIZATIONS`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NO_OPTIMIZATIONS)、[`CONFIG_COVERAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COVERAGE)、[`CONFIG_DEBUG_OPTIMIZATIONS`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEBUG_OPTIMIZATIONS)、[`CONFIG_DEBUG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEBUG)、[`CONFIG_SIZE_OPTIMIZATIONS_AGGRESSIVE`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_SIZE_OPTIMIZATIONS_AGGRESSIVE)、[`CONFIG_SIZE_OPTIMIZATIONS`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_SIZE_OPTIMIZATIONS)、[`CONFIG_SPEED_OPTIMIZATIONS`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_SPEED_OPTIMIZATIONS)。

<a id="CONFIG_COMPILER_SAVE_TEMPS"></a>

## 3.42 `CONFIG_COMPILER_SAVE_TEMPS`

**提示（Prompt）**：保存临时目标文件（Temporary Object Files）。

**说明（Help）**

要求编译器永久保留临时中间文件，可用于排查构建问题。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:541`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L541)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

<a id="CONFIG_COMPILER_SECURITY_FORTIFY"></a>

## 3.43 `CONFIG_COMPILER_SECURITY_FORTIFY`

**提示（Prompt）**：检测 C 标准库调用中的缓冲区溢出（Buffer Overflow）。

**说明（Help）**

检查 C 标准库（libc）调用中的缓冲区溢出。使用 Picolibc 或 Newlib 时，Clang 和 GCC 支持此功能；要求启用编译器优化。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
CONFIG_FORTIFY_SOURCE_NONE if CONFIG_NO_OPTIMIZATIONS || CONFIG_MINIMAL_LIBC || CONFIG_NATIVE_BUILD
CONFIG_FORTIFY_SOURCE_COMPILE_TIME
```

**可选项（Choices）**

```text
CONFIG_FORTIFY_SOURCE_NONE
CONFIG_FORTIFY_SOURCE_COMPILE_TIME
CONFIG_FORTIFY_SOURCE_RUN_TIME
```

**定义位置（Location）**：[`Kconfig.zephyr:561`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L561)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

**配置项引用（Symbol References）**：[`CONFIG_FORTIFY_SOURCE_NONE`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_FORTIFY_SOURCE_NONE)、[`CONFIG_NO_OPTIMIZATIONS`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NO_OPTIMIZATIONS)、[`CONFIG_MINIMAL_LIBC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MINIMAL_LIBC)、[`CONFIG_NATIVE_BUILD`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NATIVE_BUILD)、[`CONFIG_FORTIFY_SOURCE_COMPILE_TIME`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_FORTIFY_SOURCE_COMPILE_TIME)、[`CONFIG_FORTIFY_SOURCE_RUN_TIME`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_FORTIFY_SOURCE_RUN_TIME)。

<a id="CONFIG_COMPILER_TRACK_MACRO_EXPANSION"></a>

## 3.44 `CONFIG_COMPILER_TRACK_MACRO_EXPANSION`

**提示（Prompt）**：跟踪宏展开（Macro Expansion）。

**说明（Help）**

启用后，跟踪记号（Token）跨越宏展开过程的位置。调试较长的宏展开链时，禁用此项可能有帮助。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`Kconfig.zephyr:547`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L547)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

<a id="CONFIG_COMPILER_WARNINGS_AS_ERRORS"></a>

## 3.45 `CONFIG_COMPILER_WARNINGS_AS_ERRORS`

**提示（Prompt）**：将警告视为错误（Warnings as Errors）。

**说明（Help）**

启用工具链的“将警告视为错误”标志。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:519`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L519)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

<a id="CONFIG_CUSTOM_LINKER_SCRIPT"></a>

## 3.46 `CONFIG_CUSTOM_LINKER_SCRIPT`

**提示（Prompt）**：自定义链接脚本路径（Custom Linker Script Path）。

**说明（Help）**

指定替代开发板默认脚本的链接脚本路径。该脚本必须基于 Zephyr 提供的版本，因为内核可能要求特定布局或内存区域。应用需要向链接脚本增加节，又希望避免修改 Zephyr 提供的脚本时，此项很有用。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_HAVE_CUSTOM_LINKER_SCRIPT
```

**定义位置（Location）**：[`Kconfig.zephyr:228`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L228)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。 → 已提供自定义链接脚本（Custom Linker Script）。

**配置项引用（Symbol References）**：[`CONFIG_HAVE_CUSTOM_LINKER_SCRIPT`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_HAVE_CUSTOM_LINKER_SCRIPT)。

<a id="CONFIG_DEBUG_OPTIMIZATIONS"></a>

## 3.47 `CONFIG_DEBUG_OPTIMIZATIONS`

**提示（Prompt）**：优化调试体验（Debugging Experience）。

**说明（Help）**

独立于其他选项，将编译器优化设为 `-Og`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COMPILER_OPTIMIZATIONS>
```

**定义位置（Location）**：[`Kconfig.zephyr:487`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L487)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。 → 优化级别（Optimization Level）。

**配置项引用（Symbol References）**：[`CONFIG_COMPILER_OPTIMIZATIONS`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_COMPILER_OPTIMIZATIONS)。

<a id="CONFIG_DEPRECATED"></a>

## 3.48 `CONFIG_DEPRECATED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

被认定为已弃用（Deprecated）的特性或模块必须选择此符号。为选项增加此标记时，请遵循[API 生命周期中的弃用说明](https://docs.zephyrproject.org/latest/develop/api/api_lifecycle.html#deprecated)。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_NRFX_CLOCK_LF_CAL_ENABLED
CONFIG_NRFX_CLOCK_LF_SRC_RC
CONFIG_NRFX_CLOCK_LF_SRC_XTAL
CONFIG_NRFX_CLOCK_LF_SRC_SYNTH
CONFIG_NRFX_CLOCK_LF_SRC_LOW_SWING
CONFIG_NRFX_CLOCK_LF_SRC_FULL_SWING
CONFIG_NRFX_CLOCK_LFXO_TWO_STAGE_ENABLED
CONFIG_WIFI_NM_WPA_SUPPLICANT_WEP
CONFIG_MBEDTLS_CFG_FILE_DEPRECATED
CONFIG_MBEDTLS_USER_CONFIG_ENABLE
CONFIG_MBEDTLS_SSL_MAX_CONTENT_LEN_DEPRECATED
CONFIG_TFM_ZEPHYR_4_0_TO_4_2_COMPATIBILITY
CONFIG_MCUBOOT_BOOTUTIL_LIB_FOR_DIRECT_XIP
CONFIG_WIFI_NM_WPA_SUPPLICANT_WEP
CONFIG_NRFX_CLOCK_LF_CAL_ENABLED
CONFIG_NRFX_CLOCK_LF_SRC_RC
CONFIG_NRFX_CLOCK_LF_SRC_XTAL
CONFIG_NRFX_CLOCK_LF_SRC_SYNTH
CONFIG_NRFX_CLOCK_LF_SRC_LOW_SWING
CONFIG_NRFX_CLOCK_LF_SRC_FULL_SWING
CONFIG_NRFX_CLOCK_LFXO_TWO_STAGE_ENABLED
CONFIG_WIFI_NM_WPA_SUPPLICANT_WEP
CONFIG_MBEDTLS_CFG_FILE_DEPRECATED
CONFIG_MBEDTLS_USER_CONFIG_ENABLE
CONFIG_MBEDTLS_SSL_MAX_CONTENT_LEN_DEPRECATED
CONFIG_TFM_ZEPHYR_4_0_TO_4_2_COMPATIBILITY
CONFIG_SOC_RP2350A_HAZARD3
CONFIG_SOC_RP2350A_M33
CONFIG_SOC_RP2350B_HAZARD3
CONFIG_SOC_RP2350B_M33
CONFIG_SOC_SERIES_NRF51X
CONFIG_SOC_SERIES_NRF52X
CONFIG_SOC_SERIES_NRF53X
CONFIG_SOC_HFXO_CAP_EXTERNAL
CONFIG_SOC_HFXO_CAP_INTERNAL
CONFIG_SOC_SERIES_NRF54HX
CONFIG_SOC_SERIES_NRF54LX
CONFIG_SOC_SERIES_NRF91X
CONFIG_SOC_SERIES_NRF92X
CONFIG_NRF_PLATFORM_HALTIUM
CONFIG_NRF_PLATFORM_LUMOS
CONFIG_LITEX_CSR_DATA_WIDTH_DEPRECATED
CONFIG_SRAM_DEPRECATED_KCONFIG_SET
CONFIG_CACHE_DOUBLEMAP
CONFIG_BT_HCI_SETUP
CONFIG_CLOCK_CONTROL_NRF
CONFIG_DMA_XILINX_AXI_DMA_DISABLE_CACHE_WHEN_ACCESSING_SG_DESCRIPTORS
CONFIG_I2C_ALLOW_NO_STOP_TRANSACTIONS
CONFIG_MCUX_LPCMP
CONFIG_MCUX_LPCMP_TRIGGER
CONFIG_UART_MAX32_TX_AE_WORKAROUND
CONFIG_UART_NRFX_UARTE_ENHANCED_RX
CONFIG_UART_0_NRF_HW_ASYNC
CONFIG_UART_1_NRF_HW_ASYNC
CONFIG_UART_2_NRF_HW_ASYNC
CONFIG_UART_3_NRF_HW_ASYNC
CONFIG_UART_00_NRF_HW_ASYNC
CONFIG_UART_20_NRF_HW_ASYNC
CONFIG_UART_21_NRF_HW_ASYNC
CONFIG_UART_22_NRF_HW_ASYNC
CONFIG_UART_23_NRF_HW_ASYNC
CONFIG_UART_24_NRF_HW_ASYNC
CONFIG_UART_30_NRF_HW_ASYNC
CONFIG_UART_120_NRF_HW_ASYNC
CONFIG_UART_130_NRF_HW_ASYNC
CONFIG_UART_131_NRF_HW_ASYNC
CONFIG_UART_132_NRF_HW_ASYNC
CONFIG_UART_133_NRF_HW_ASYNC
CONFIG_UART_134_NRF_HW_ASYNC
CONFIG_UART_135_NRF_HW_ASYNC
CONFIG_UART_136_NRF_HW_ASYNC
CONFIG_UART_137_NRF_HW_ASYNC
CONFIG_SPI_SLAVE
CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_NONE
CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_COUNTER
CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_HOOKS
CONFIG_CORTEX_M_SYSTICK_RESET_BY_LPM
CONFIG_USB_DEVICE_DRIVER
CONFIG_WIFI_SIMPLELINK
CONFIG_WIFI_WINC1500
CONFIG_CPU_LOAD_METRIC
CONFIG_RING_BUFFER
CONFIG_BT_CUSTOM
CONFIG_BT_MESH_PROV_OOB_API_LEGACY
CONFIG_BT_MESH_MODEL_VND_MSG_CID_FORCE
CONFIG_BT_SIGNING
CONFIG_DEVICE_NAME_GATT_WRITABLE_NONE
CONFIG_DEVICE_NAME_GATT_WRITABLE_ENCRYPT
CONFIG_DEVICE_NAME_GATT_WRITABLE_AUTHEN
CONFIG_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN
CONFIG_FORCE_NO_ASSERT
CONFIG_ASSERT_VERBOSE
CONFIG_ASSERT_NO_FILE_INFO
CONFIG_ASSERT_NO_COND_INFO
CONFIG_ASSERT_NO_MSG_INFO
CONFIG_MCUMGR_TRANSPORT_SHELL_MTU_DEPRECATED
CONFIG_MCUMGR_TRANSPORT_UART_MTU_DEPRECATED
CONFIG_NET_L2_PTP
CONFIG_NET_ROUTING
CONFIG_NET_ROUTE_MCAST
CONFIG_NET_MCAST_ROUTE_MLD_REPORTS
CONFIG_NET_IPV6_ROUTING
CONFIG_NET_IPV4_ROUTING
CONFIG_LLMNR_RESOLVER
CONFIG_LLMNR_RESPONDER
CONFIG_XOPEN_STREAMS
CONFIG_USB_DEVICE_STACK
CONFIG_FLASH_CODE_PARTITION_USING_FIXED_PARTITIONS
CONFIG_DEPRECATION_TEST
CONFIG_LEGACY_GENERATED_INCLUDE_PATH
```

**定义位置（Location）**：[`Kconfig.zephyr:1025`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L1025)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。

**配置项引用（Symbol References）**：[`CONFIG_NRFX_CLOCK_LF_CAL_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LF_CAL_ENABLED)、[`CONFIG_NRFX_CLOCK_LF_SRC_RC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LF_SRC_RC)、[`CONFIG_NRFX_CLOCK_LF_SRC_XTAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LF_SRC_XTAL)、[`CONFIG_NRFX_CLOCK_LF_SRC_SYNTH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LF_SRC_SYNTH)、[`CONFIG_NRFX_CLOCK_LF_SRC_LOW_SWING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LF_SRC_LOW_SWING)、[`CONFIG_NRFX_CLOCK_LF_SRC_FULL_SWING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LF_SRC_FULL_SWING)、[`CONFIG_NRFX_CLOCK_LFXO_TWO_STAGE_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_CLOCK_LFXO_TWO_STAGE_ENABLED)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_WEP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_WEP)、[`CONFIG_MBEDTLS_CFG_FILE_DEPRECATED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_CFG_FILE_DEPRECATED)、[`CONFIG_MBEDTLS_USER_CONFIG_ENABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_USER_CONFIG_ENABLE)、[`CONFIG_MBEDTLS_SSL_MAX_CONTENT_LEN_DEPRECATED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBEDTLS_SSL_MAX_CONTENT_LEN_DEPRECATED)、[`CONFIG_TFM_ZEPHYR_4_0_TO_4_2_COMPATIBILITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFM_ZEPHYR_4_0_TO_4_2_COMPATIBILITY)、[`CONFIG_MCUBOOT_BOOTUTIL_LIB_FOR_DIRECT_XIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUBOOT_BOOTUTIL_LIB_FOR_DIRECT_XIP)、[`CONFIG_SOC_RP2350A_HAZARD3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350A_HAZARD3)、[`CONFIG_SOC_RP2350A_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350A_M33)、[`CONFIG_SOC_RP2350B_HAZARD3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350B_HAZARD3)、[`CONFIG_SOC_RP2350B_M33`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350B_M33)、[`CONFIG_SOC_SERIES_NRF51X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF51X)、[`CONFIG_SOC_SERIES_NRF52X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF52X)、[`CONFIG_SOC_SERIES_NRF53X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF53X)、[`CONFIG_SOC_HFXO_CAP_EXTERNAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_HFXO_CAP_EXTERNAL)、[`CONFIG_SOC_HFXO_CAP_INTERNAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_HFXO_CAP_INTERNAL)、[`CONFIG_SOC_SERIES_NRF54HX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54HX)、[`CONFIG_SOC_SERIES_NRF54LX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54LX)、[`CONFIG_SOC_SERIES_NRF91X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF91X)、[`CONFIG_SOC_SERIES_NRF92X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF92X)、[`CONFIG_NRF_PLATFORM_HALTIUM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_PLATFORM_HALTIUM)、[`CONFIG_NRF_PLATFORM_LUMOS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_PLATFORM_LUMOS)、[`CONFIG_LITEX_CSR_DATA_WIDTH_DEPRECATED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LITEX_CSR_DATA_WIDTH_DEPRECATED)、[`CONFIG_SRAM_DEPRECATED_KCONFIG_SET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SRAM_DEPRECATED_KCONFIG_SET)、[`CONFIG_CACHE_DOUBLEMAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CACHE_DOUBLEMAP)、[`CONFIG_BT_HCI_SETUP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_SETUP)、[`CONFIG_CLOCK_CONTROL_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_DMA_XILINX_AXI_DMA_DISABLE_CACHE_WHEN_ACCESSING_SG_DESCRIPTORS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA_XILINX_AXI_DMA_DISABLE_CACHE_WHEN_ACCESSING_SG_DESCRIPTORS)、[`CONFIG_I2C_ALLOW_NO_STOP_TRANSACTIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_ALLOW_NO_STOP_TRANSACTIONS)、[`CONFIG_MCUX_LPCMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUX_LPCMP)、[`CONFIG_MCUX_LPCMP_TRIGGER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUX_LPCMP_TRIGGER)、[`CONFIG_UART_MAX32_TX_AE_WORKAROUND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_MAX32_TX_AE_WORKAROUND)、[`CONFIG_UART_NRFX_UARTE_ENHANCED_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_NRFX_UARTE_ENHANCED_RX)、[`CONFIG_UART_0_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_0_NRF_HW_ASYNC)、[`CONFIG_UART_1_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_1_NRF_HW_ASYNC)、[`CONFIG_UART_2_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_2_NRF_HW_ASYNC)、[`CONFIG_UART_3_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_3_NRF_HW_ASYNC)、[`CONFIG_UART_00_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_00_NRF_HW_ASYNC)、[`CONFIG_UART_20_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_20_NRF_HW_ASYNC)、[`CONFIG_UART_21_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_21_NRF_HW_ASYNC)、[`CONFIG_UART_22_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_22_NRF_HW_ASYNC)、[`CONFIG_UART_23_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_23_NRF_HW_ASYNC)、[`CONFIG_UART_24_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_24_NRF_HW_ASYNC)、[`CONFIG_UART_30_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_30_NRF_HW_ASYNC)、[`CONFIG_UART_120_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_120_NRF_HW_ASYNC)、[`CONFIG_UART_130_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_130_NRF_HW_ASYNC)、[`CONFIG_UART_131_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_131_NRF_HW_ASYNC)、[`CONFIG_UART_132_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_132_NRF_HW_ASYNC)、[`CONFIG_UART_133_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_133_NRF_HW_ASYNC)、[`CONFIG_UART_134_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_134_NRF_HW_ASYNC)、[`CONFIG_UART_135_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_135_NRF_HW_ASYNC)、[`CONFIG_UART_136_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_136_NRF_HW_ASYNC)、[`CONFIG_UART_137_NRF_HW_ASYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_137_NRF_HW_ASYNC)、[`CONFIG_SPI_SLAVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_SLAVE)、[`CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_NONE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_NONE)、[`CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_COUNTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_COUNTER)、[`CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_HOOKS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CORTEX_M_SYSTICK_LPM_TIMER_HOOKS)、[`CONFIG_CORTEX_M_SYSTICK_RESET_BY_LPM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CORTEX_M_SYSTICK_RESET_BY_LPM)、[`CONFIG_USB_DEVICE_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_WIFI_SIMPLELINK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_SIMPLELINK)、[`CONFIG_WIFI_WINC1500`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_WINC1500)、[`CONFIG_CPU_LOAD_METRIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_LOAD_METRIC)、[`CONFIG_RING_BUFFER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RING_BUFFER)、[`CONFIG_BT_CUSTOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CUSTOM)、[`CONFIG_BT_MESH_PROV_OOB_API_LEGACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROV_OOB_API_LEGACY)、[`CONFIG_BT_MESH_MODEL_VND_MSG_CID_FORCE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_MODEL_VND_MSG_CID_FORCE)、[`CONFIG_BT_SIGNING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SIGNING)、[`CONFIG_DEVICE_NAME_GATT_WRITABLE_NONE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVICE_NAME_GATT_WRITABLE_NONE)、[`CONFIG_DEVICE_NAME_GATT_WRITABLE_ENCRYPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVICE_NAME_GATT_WRITABLE_ENCRYPT)、[`CONFIG_DEVICE_NAME_GATT_WRITABLE_AUTHEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVICE_NAME_GATT_WRITABLE_AUTHEN)、[`CONFIG_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVICE_APPEARANCE_GATT_WRITABLE_AUTHEN)、[`CONFIG_FORCE_NO_ASSERT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FORCE_NO_ASSERT)、[`CONFIG_ASSERT_VERBOSE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT_VERBOSE)、[`CONFIG_ASSERT_NO_FILE_INFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT_NO_FILE_INFO)、[`CONFIG_ASSERT_NO_COND_INFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT_NO_COND_INFO)、[`CONFIG_ASSERT_NO_MSG_INFO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ASSERT_NO_MSG_INFO)、[`CONFIG_MCUMGR_TRANSPORT_SHELL_MTU_DEPRECATED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_SHELL_MTU_DEPRECATED)、[`CONFIG_MCUMGR_TRANSPORT_UART_MTU_DEPRECATED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_TRANSPORT_UART_MTU_DEPRECATED)、[`CONFIG_NET_L2_PTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PTP)、[`CONFIG_NET_ROUTING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ROUTING)、[`CONFIG_NET_ROUTE_MCAST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ROUTE_MCAST)、[`CONFIG_NET_MCAST_ROUTE_MLD_REPORTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MCAST_ROUTE_MLD_REPORTS)、[`CONFIG_NET_IPV6_ROUTING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_ROUTING)、[`CONFIG_NET_IPV4_ROUTING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_ROUTING)、[`CONFIG_LLMNR_RESOLVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LLMNR_RESOLVER)、[`CONFIG_LLMNR_RESPONDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LLMNR_RESPONDER)、[`CONFIG_XOPEN_STREAMS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XOPEN_STREAMS)、[`CONFIG_USB_DEVICE_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK)、[`CONFIG_FLASH_CODE_PARTITION_USING_FIXED_PARTITIONS`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_FLASH_CODE_PARTITION_USING_FIXED_PARTITIONS)、[`CONFIG_DEPRECATION_TEST`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATION_TEST)、[`CONFIG_LEGACY_GENERATED_INCLUDE_PATH`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LEGACY_GENERATED_INCLUDE_PATH)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MBEDTLS_CFG_FILE_DEPRECATED`、`CONFIG_MBEDTLS_SSL_MAX_CONTENT_LEN_DEPRECATED`。

<a id="CONFIG_DEPRECATED_KCONFIGS_AS_ERRORS"></a>

## 3.49 `CONFIG_DEPRECATED_KCONFIGS_AS_ERRORS`

**提示（Prompt）**：将已弃用 Kconfig 选项视为错误（Deprecated Kconfigs as Errors）。

**说明（Help）**

构建中启用了已弃用 Kconfig 选项时，使构建系统报告失败。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_WARN_DEPRECATED
```

**定义位置（Location）**：[`Kconfig.zephyr:524`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L524)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

**配置项引用（Symbol References）**：[`CONFIG_WARN_DEPRECATED`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_WARN_DEPRECATED)。

<a id="CONFIG_DEPRECATION_TEST"></a>

## 3.50 `CONFIG_DEPRECATION_TEST`

**提示（Prompt）**：标记已弃用特性的测试（Test for Deprecated Feature）［已弃用］。

**说明（Help）**

由检查已弃用特性功能的测试选择本选项，防止使用已弃用特性被视为错误。它仅用于确保这些特性在正式移除之前仍正常工作的测试，不会阻止其他警告或错误。本 Kconfig 选项自身也已弃用，应改为将 `CONFIG_WARN_DEPRECATED` 设为 `n`。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`Kconfig.zephyr:530`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L530)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

**配置项引用（Symbol References）**：[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_EMIT_ALL_SYSCALLS"></a>

## 3.51 `CONFIG_EMIT_ALL_SYSCALLS`

**提示（Prompt）**：生成源码树中所有可能的系统调用（Syscalls）。

**说明（Help）**

要求构建系统生成源码树中发现的全部系统调用，而不仅是与已启用驱动和子系统关联的系统调用。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:1016`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L1016)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<a id="CONFIG_ENFORCE_ZEPHYR_STDINT"></a>

## 3.52 `CONFIG_ENFORCE_ZEPHYR_STDINT`

**提示（Prompt）**：强制采用 Zephyr 的 `stdint` 类型约定。

**说明（Help）**

强制采用 Zephyr 的 `stdint` 约定：`int32_t = int`、`int64_t = long long`、`intptr_t = long`，以便在 ILP32 和 LP64 架构中统一使用简短的格式化字符串长度修饰符。某些情况下无法这样做，例如链接仅提供二进制的 C++ 库，而其类型名称修饰（Type Mangling）与 Zephyr 约定不兼容，或者构建环境不允许强制该约定。此时应关闭本选项，但须注意，Zephyr 代码的参数类型验证将被跳过。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_ARCH_POSIX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`Kconfig.zephyr:1067`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L1067)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_POSIX)。

<a id="CONFIG_EXPERIMENTAL"></a>

## 3.53 `CONFIG_EXPERIMENTAL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

被认定为处于实验性实现阶段（Experimental Implementation Stage）的特性必须选择此符号。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_NM_WPA_SUPPLICANT_PRINT_PMK
CONFIG_LIBLC3_PLUS
CONFIG_LIBLC3_PLUS_HR
CONFIG_TF_PSA_CRYPTO_PQCP_MLDSA_ENABLED
CONFIG_TF_PSA_CRYPTO_PQCP_MLDSA_87_ENABLED
CONFIG_OPENTHREAD_BLE_TCAT
CONFIG_OPENTHREAD_MLE_LONG_ROUTES
CONFIG_OPENTHREAD_TIME_SYNC
CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_NM_WPA_SUPPLICANT_PRINT_PMK
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_NM_WPA_SUPPLICANT_PRINT_PMK
CONFIG_LIBLC3_PLUS
CONFIG_LIBLC3_PLUS_HR
CONFIG_TF_PSA_CRYPTO_PQCP_MLDSA_ENABLED
CONFIG_TF_PSA_CRYPTO_PQCP_MLDSA_87_ENABLED
CONFIG_OPENTHREAD_BLE_TCAT
CONFIG_OPENTHREAD_MLE_LONG_ROUTES
CONFIG_OPENTHREAD_TIME_SYNC
CONFIG_SOC_SERIES_NRF92
CONFIG_XTENSA_MPU
CONFIG_SHARED_INTERRUPTS
CONFIG_DYNAMIC_THREAD
CONFIG_TIMEOUT_BACKEND_MINHEAP
CONFIG_TIMEOUT_BACKEND_WHEEL
CONFIG_TIMEOUT_BACKEND_BUCKET
CONFIG_TIMEOUT_BACKEND_SKIPLIST
CONFIG_HW_SHADOW_STACK
CONFIG_TICKET_SPINLOCKS
CONFIG_DEVICE_MUTABLE
CONFIG_BT_H5
CONFIG_BUZZER
CONFIG_CLOCK_CONTROL_NRF_HFINT_CALIBRATION
CONFIG_COUNTER_CAPTURE
CONFIG_CRYPTO_MBEDTLS_SHIM
CONFIG_DALI
CONFIG_DMA_EMUL
CONFIG_DP_DRIVER
CONFIG_ETH_E1000_PTP_CLOCK
CONFIG_ETH_STM32_HAL_RX_THREAD_PREEMPTIVE
CONFIG_FLASH_STM32_XSPI_RAM_RELOCATION
CONFIG_ICE40_FPGA_BITBANG
CONFIG_GNSS
CONFIG_GPIO_GET_DIRECTION
CONFIG_GPIO_GET_CONFIG
CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT
CONFIG_I2C_RTIO
CONFIG_I2C_TARGET_BUFFER_MODE
CONFIG_I2C_TARGET_ALLOW_POWER_SAVING
CONFIG_I3C_RTIO
CONFIG_LIN
CONFIG_MEMC
CONFIG_MIPI_DBI
CONFIG_MIPI_DSI
CONFIG_DEVMUX
CONFIG_MM_DRV
CONFIG_MODEM_CONTEXT
CONFIG_MODEM_HL78XX
CONFIG_MSPI_STM32_CONTROLLER
CONFIG_OTP
CONFIG_PWM_EVENT
CONFIG_UART_BT
CONFIG_UART_EMUL
CONFIG_SPI_RTIO
CONFIG_SPI_PERIPHERAL
CONFIG_SPI_EXTENDED_MODES
CONFIG_SYSTEM_CLOCK_SLOPPY_IDLE
CONFIG_STM32_LPTIM_STDBY_TIMER
CONFIG_UHC_DRIVER
CONFIG_ESP32_WIFI_ENHANCED_LIGHT_SLEEP
CONFIG_NXP_88W8987
CONFIG_NXP_IW416
CONFIG_NXP_IW61X
CONFIG_NXP_88W8801
CONFIG_NXP_IW610_RD_USD
CONFIG_ZVFS
CONFIG_BT_CHANNEL_SOUNDING
CONFIG_BT_CHANNEL_SOUNDING_TEST
CONFIG_BT_HCI_ERR_TO_STR
CONFIG_BT_CONN_TX_NOTIFY_WQ
CONFIG_BT_MESH_STATISTIC
CONFIG_BT_SECURITY_ERR_TO_STR
CONFIG_BT_SMP_ERR_TO_STR
CONFIG_BT_PASSKEY_KEYPRESS
CONFIG_BT_L2CAP_SEG_RECV
CONFIG_BT_L2CAP_RECONFIGURE_EXPLICIT
CONFIG_BT_ATT_ERR_TO_STR
CONFIG_BT_EATT
CONFIG_BT_ANS
CONFIG_BT_DIS_SYSTEM_ID
CONFIG_BT_ETS
CONFIG_BT_IAS
CONFIG_BT_IAS_CLIENT
CONFIG_BT_OTS
CONFIG_BT_OTS_CLIENT
CONFIG_BT_DF
CONFIG_BT_CLASSIC
CONFIG_BT_L2CAP_CONNLESS
CONFIG_BT_L2CAP_QOS
CONFIG_BT_L2CAP_RET
CONFIG_BT_L2CAP_FC
CONFIG_BT_L2CAP_ENH_RET
CONFIG_BT_L2CAP_STREAM
CONFIG_BT_L2CAP_FCS
CONFIG_BT_L2CAP_EXT_WIN_SIZE
CONFIG_BT_RFCOMM
CONFIG_BT_HFP_HF
CONFIG_BT_HFP_AG
CONFIG_BT_AVDTP
CONFIG_BT_A2DP
CONFIG_BT_AVCTP
CONFIG_BT_AVRCP
CONFIG_BT_AVRCP_BROWSING
CONFIG_BT_AVRCP_TG_COVER_ART
CONFIG_BT_AVRCP_CT_COVER_ART
CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE_PROPERTIES
CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE
CONFIG_BT_AVRCP_CT_COVER_ART_GET_LINKED_THUMBNAIL
CONFIG_BT_DID
CONFIG_BT_HID_DEVICE
CONFIG_BT_HID_HOST
CONFIG_BT_GOEP
CONFIG_BT_BIP
CONFIG_BT_MAP
CONFIG_BT_CTLR_ADV_ISO
CONFIG_BT_CTLR_SYNC_ISO
CONFIG_BT_CTLR_SET_HOST_FEATURE
CONFIG_BT_CTLR_CENTRAL_ISO
CONFIG_BT_CTLR_PERIPHERAL_ISO
CONFIG_BT_LLL_VENDOR_NORDIC
CONFIG_BT_CTLR_ADV_DATA_CHAIN
CONFIG_BT_CTLR_DTM_HCI_DF_IQ_REPORT
CONFIG_DAP
CONFIG_GDBSTUB
CONFIG_GNSS_RTK
CONFIG_LOG_CUSTOM_HEADER
CONFIG_LOG_BACKEND_BLE
CONFIG_LORAWAN
CONFIG_MCUMGR_GRP_TRANSPORT
CONFIG_MODEM_BACKEND_UART_ASYNC_HWFC
CONFIG_MPIPE
CONFIG_NET_L2_IEEE802154_SECURITY
CONFIG_NET_IPV6_IID_STABLE
CONFIG_NET_IPV6_PE
CONFIG_NET_IPV4_NAT
CONFIG_NET_UDP_OPTIONS
CONFIG_NET_UDP_OPTIONS_DPLPMTUD
CONFIG_COAP_OVER_RELIABLE_TRANSPORT
CONFIG_COAP_OSCORE
CONFIG_MDNS_RESPONDER_PROBE
CONFIG_FTP_CLIENT
CONFIG_NET_LATMON
CONFIG_MCP_SERVER
CONFIG_NETMIDI2_HOST
CONFIG_MQTT_VERSION_5_0
CONFIG_MQTT_SN_LIB
CONFIG_PTP
CONFIG_RTP
CONFIG_TFTP_LIB
CONFIG_HTTP_SERVER
CONFIG_WEBSOCKET_CLIENT
CONFIG_LWM2M_COAP_BLOCK_TRANSFER
CONFIG_LWM2M_QUEUE_MODE_NO_MSG_BUFFERING
CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT_MULTIPLE
CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT
CONFIG_OCPP
CONFIG_QUIC
CONFIG_NET_SOCKETS_NET_MGMT
CONFIG_NET_CAPTURE_COOKED_MODE
CONFIG_NET_ZPERF_IPERF3
CONFIG_SSH_SERVER
CONFIG_SSH_CLIENT
CONFIG_WIREGUARD
CONFIG_PM_EARLY_SYSTEM_TIMER_RESUME
CONFIG_MCTP
CONFIG_SETTINGS_TFM_PSA
CONFIG_SHELL_TELNET_SUPPORT_COMMAND
CONFIG_SHELL_CUSTOM_HEADER
CONFIG_ZTEST_BENCHMARK
CONFIG_TRACING_CUSTOM
CONFIG_USB_DEVICE_AUDIO
CONFIG_USBD_VIDEO_CLASS
CONFIG_USB_HOST_STACK
CONFIG_USBIP
CONFIG_USBH_VIDEO_CLASS
CONFIG_ZBUS_PROXY_AGENT
```

**定义位置（Location）**：[`Kconfig.zephyr:1042`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L1042)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_PRINT_PMK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_PRINT_PMK)、[`CONFIG_LIBLC3_PLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIBLC3_PLUS)、[`CONFIG_LIBLC3_PLUS_HR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIBLC3_PLUS_HR)、[`CONFIG_TF_PSA_CRYPTO_PQCP_MLDSA_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TF_PSA_CRYPTO_PQCP_MLDSA_ENABLED)、[`CONFIG_TF_PSA_CRYPTO_PQCP_MLDSA_87_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TF_PSA_CRYPTO_PQCP_MLDSA_87_ENABLED)、[`CONFIG_OPENTHREAD_BLE_TCAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_BLE_TCAT)、[`CONFIG_OPENTHREAD_MLE_LONG_ROUTES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_MLE_LONG_ROUTES)、[`CONFIG_OPENTHREAD_TIME_SYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_TIME_SYNC)、[`CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_PSA_CRYPTO_DRIVERS)、[`CONFIG_SOC_SERIES_NRF92`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF92)、[`CONFIG_XTENSA_MPU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XTENSA_MPU)、[`CONFIG_SHARED_INTERRUPTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHARED_INTERRUPTS)、[`CONFIG_DYNAMIC_THREAD`](P001_kernel_配置项参考_1.md#CONFIG_DYNAMIC_THREAD)、[`CONFIG_TIMEOUT_BACKEND_MINHEAP`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_BACKEND_MINHEAP)、[`CONFIG_TIMEOUT_BACKEND_WHEEL`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_BACKEND_WHEEL)、[`CONFIG_TIMEOUT_BACKEND_BUCKET`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_BACKEND_BUCKET)、[`CONFIG_TIMEOUT_BACKEND_SKIPLIST`](P002_kernel_配置项参考_2.md#CONFIG_TIMEOUT_BACKEND_SKIPLIST)、[`CONFIG_HW_SHADOW_STACK`](P001_kernel_配置项参考_1.md#CONFIG_HW_SHADOW_STACK)、[`CONFIG_TICKET_SPINLOCKS`](P002_kernel_配置项参考_2.md#CONFIG_TICKET_SPINLOCKS)、[`CONFIG_DEVICE_MUTABLE`](P001_kernel_配置项参考_1.md#CONFIG_DEVICE_MUTABLE)、[`CONFIG_BT_H5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_H5)、[`CONFIG_BUZZER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUZZER)、[`CONFIG_CLOCK_CONTROL_NRF_HFINT_CALIBRATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_HFINT_CALIBRATION)、[`CONFIG_COUNTER_CAPTURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COUNTER_CAPTURE)、[`CONFIG_CRYPTO_MBEDTLS_SHIM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRYPTO_MBEDTLS_SHIM)、[`CONFIG_DALI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DALI)、[`CONFIG_DMA_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DMA_EMUL)、[`CONFIG_DP_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DP_DRIVER)、[`CONFIG_ETH_E1000_PTP_CLOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_E1000_PTP_CLOCK)、[`CONFIG_ETH_STM32_HAL_RX_THREAD_PREEMPTIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_STM32_HAL_RX_THREAD_PREEMPTIVE)、[`CONFIG_FLASH_STM32_XSPI_RAM_RELOCATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_STM32_XSPI_RAM_RELOCATION)、[`CONFIG_ICE40_FPGA_BITBANG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ICE40_FPGA_BITBANG)、[`CONFIG_GNSS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GNSS)、[`CONFIG_GPIO_GET_DIRECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO_GET_DIRECTION)、[`CONFIG_GPIO_GET_CONFIG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO_GET_CONFIG)、[`CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GPIO_ENABLE_DISABLE_INTERRUPT)、[`CONFIG_I2C_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_RTIO)、[`CONFIG_I2C_TARGET_BUFFER_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_TARGET_BUFFER_MODE)、[`CONFIG_I2C_TARGET_ALLOW_POWER_SAVING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I2C_TARGET_ALLOW_POWER_SAVING)、[`CONFIG_I3C_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_I3C_RTIO)、[`CONFIG_LIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LIN)、[`CONFIG_MEMC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MEMC)、[`CONFIG_MIPI_DBI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DBI)、[`CONFIG_MIPI_DSI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MIPI_DSI)、[`CONFIG_DEVMUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEVMUX)、[`CONFIG_MM_DRV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MM_DRV)、[`CONFIG_MODEM_CONTEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CONTEXT)、[`CONFIG_MODEM_HL78XX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_HL78XX)、[`CONFIG_MSPI_STM32_CONTROLLER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MSPI_STM32_CONTROLLER)、[`CONFIG_OTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OTP)、[`CONFIG_PWM_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PWM_EVENT)、[`CONFIG_UART_BT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_BT)、[`CONFIG_UART_EMUL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_EMUL)、[`CONFIG_SPI_RTIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_RTIO)、[`CONFIG_SPI_PERIPHERAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_PERIPHERAL)、[`CONFIG_SPI_EXTENDED_MODES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI_EXTENDED_MODES)、[`CONFIG_SYSTEM_CLOCK_SLOPPY_IDLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SYSTEM_CLOCK_SLOPPY_IDLE)、[`CONFIG_STM32_LPTIM_STDBY_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32_LPTIM_STDBY_TIMER)、[`CONFIG_UHC_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UHC_DRIVER)、[`CONFIG_ESP32_WIFI_ENHANCED_LIGHT_SLEEP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP32_WIFI_ENHANCED_LIGHT_SLEEP)、[`CONFIG_NXP_88W8987`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_88W8987)、[`CONFIG_NXP_IW416`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_IW416)、[`CONFIG_NXP_IW61X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_IW61X)、[`CONFIG_NXP_88W8801`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_88W8801)、[`CONFIG_NXP_IW610_RD_USD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NXP_IW610_RD_USD)、[`CONFIG_ZVFS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZVFS)、[`CONFIG_BT_CHANNEL_SOUNDING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CHANNEL_SOUNDING)、[`CONFIG_BT_CHANNEL_SOUNDING_TEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CHANNEL_SOUNDING_TEST)、[`CONFIG_BT_HCI_ERR_TO_STR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_ERR_TO_STR)、[`CONFIG_BT_CONN_TX_NOTIFY_WQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CONN_TX_NOTIFY_WQ)、[`CONFIG_BT_MESH_STATISTIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_STATISTIC)、[`CONFIG_BT_SECURITY_ERR_TO_STR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SECURITY_ERR_TO_STR)、[`CONFIG_BT_SMP_ERR_TO_STR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP_ERR_TO_STR)、[`CONFIG_BT_PASSKEY_KEYPRESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PASSKEY_KEYPRESS)、[`CONFIG_BT_L2CAP_SEG_RECV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_SEG_RECV)、[`CONFIG_BT_L2CAP_RECONFIGURE_EXPLICIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_RECONFIGURE_EXPLICIT)、[`CONFIG_BT_ATT_ERR_TO_STR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ATT_ERR_TO_STR)、[`CONFIG_BT_EATT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_EATT)、[`CONFIG_BT_ANS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ANS)、[`CONFIG_BT_DIS_SYSTEM_ID`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DIS_SYSTEM_ID)、[`CONFIG_BT_ETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ETS)、[`CONFIG_BT_IAS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_IAS)、[`CONFIG_BT_IAS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_IAS_CLIENT)、[`CONFIG_BT_OTS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OTS)、[`CONFIG_BT_OTS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_OTS_CLIENT)、[`CONFIG_BT_DF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DF)、[`CONFIG_BT_CLASSIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CLASSIC)、[`CONFIG_BT_L2CAP_CONNLESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_CONNLESS)、[`CONFIG_BT_L2CAP_QOS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_QOS)、[`CONFIG_BT_L2CAP_RET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_RET)、[`CONFIG_BT_L2CAP_FC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_FC)、[`CONFIG_BT_L2CAP_ENH_RET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_ENH_RET)、[`CONFIG_BT_L2CAP_STREAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_STREAM)、[`CONFIG_BT_L2CAP_FCS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_FCS)、[`CONFIG_BT_L2CAP_EXT_WIN_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_L2CAP_EXT_WIN_SIZE)、[`CONFIG_BT_RFCOMM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_RFCOMM)、[`CONFIG_BT_HFP_HF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_HF)、[`CONFIG_BT_HFP_AG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HFP_AG)、[`CONFIG_BT_AVDTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AVDTP)、[`CONFIG_BT_A2DP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_A2DP)、[`CONFIG_BT_AVCTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AVCTP)、[`CONFIG_BT_AVRCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AVRCP)、[`CONFIG_BT_AVRCP_BROWSING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AVRCP_BROWSING)、[`CONFIG_BT_AVRCP_TG_COVER_ART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AVRCP_TG_COVER_ART)、[`CONFIG_BT_AVRCP_CT_COVER_ART`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AVRCP_CT_COVER_ART)、[`CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE_PROPERTIES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE_PROPERTIES)、[`CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AVRCP_CT_COVER_ART_GET_IMAGE)、[`CONFIG_BT_AVRCP_CT_COVER_ART_GET_LINKED_THUMBNAIL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_AVRCP_CT_COVER_ART_GET_LINKED_THUMBNAIL)、[`CONFIG_BT_DID`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DID)、[`CONFIG_BT_HID_DEVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HID_DEVICE)、[`CONFIG_BT_HID_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HID_HOST)、[`CONFIG_BT_GOEP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_GOEP)、[`CONFIG_BT_BIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_BIP)、[`CONFIG_BT_MAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MAP)、[`CONFIG_BT_CTLR_ADV_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_ISO)、[`CONFIG_BT_CTLR_SYNC_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_ISO)、[`CONFIG_BT_CTLR_SET_HOST_FEATURE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SET_HOST_FEATURE)、[`CONFIG_BT_CTLR_CENTRAL_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CENTRAL_ISO)、[`CONFIG_BT_CTLR_PERIPHERAL_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PERIPHERAL_ISO)、[`CONFIG_BT_LLL_VENDOR_NORDIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LLL_VENDOR_NORDIC)、[`CONFIG_BT_CTLR_ADV_DATA_CHAIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_DATA_CHAIN)、[`CONFIG_BT_CTLR_DTM_HCI_DF_IQ_REPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DTM_HCI_DF_IQ_REPORT)、[`CONFIG_DAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DAP)、[`CONFIG_GDBSTUB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GDBSTUB)、[`CONFIG_GNSS_RTK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GNSS_RTK)、[`CONFIG_LOG_CUSTOM_HEADER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_CUSTOM_HEADER)、[`CONFIG_LOG_BACKEND_BLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_BACKEND_BLE)、[`CONFIG_LORAWAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LORAWAN)、[`CONFIG_MCUMGR_GRP_TRANSPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_TRANSPORT)、[`CONFIG_MODEM_BACKEND_UART_ASYNC_HWFC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_BACKEND_UART_ASYNC_HWFC)、[`CONFIG_MPIPE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE)、[`CONFIG_NET_L2_IEEE802154_SECURITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154_SECURITY)、[`CONFIG_NET_IPV6_IID_STABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_IID_STABLE)、[`CONFIG_NET_IPV6_PE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_PE)、[`CONFIG_NET_IPV4_NAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4_NAT)、[`CONFIG_NET_UDP_OPTIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP_OPTIONS)、[`CONFIG_NET_UDP_OPTIONS_DPLPMTUD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP_OPTIONS_DPLPMTUD)、[`CONFIG_COAP_OVER_RELIABLE_TRANSPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OVER_RELIABLE_TRANSPORT)、[`CONFIG_COAP_OSCORE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE)、[`CONFIG_MDNS_RESPONDER_PROBE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MDNS_RESPONDER_PROBE)、[`CONFIG_FTP_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FTP_CLIENT)、[`CONFIG_NET_LATMON`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LATMON)、[`CONFIG_MCP_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCP_SERVER)、[`CONFIG_NETMIDI2_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETMIDI2_HOST)、[`CONFIG_MQTT_VERSION_5_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MQTT_VERSION_5_0)、[`CONFIG_MQTT_SN_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MQTT_SN_LIB)、[`CONFIG_PTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP)、[`CONFIG_RTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTP)、[`CONFIG_TFTP_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFTP_LIB)、[`CONFIG_HTTP_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_SERVER)、[`CONFIG_WEBSOCKET_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WEBSOCKET_CLIENT)、[`CONFIG_LWM2M_COAP_BLOCK_TRANSFER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_COAP_BLOCK_TRANSFER)、[`CONFIG_LWM2M_QUEUE_MODE_NO_MSG_BUFFERING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_QUEUE_MODE_NO_MSG_BUFFERING)、[`CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT_MULTIPLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT_MULTIPLE)、[`CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT)、[`CONFIG_OCPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OCPP)、[`CONFIG_QUIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC)、[`CONFIG_NET_SOCKETS_NET_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_NET_MGMT)、[`CONFIG_NET_CAPTURE_COOKED_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CAPTURE_COOKED_MODE)、[`CONFIG_NET_ZPERF_IPERF3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_IPERF3)、[`CONFIG_SSH_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_SERVER)、[`CONFIG_SSH_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SSH_CLIENT)、[`CONFIG_WIREGUARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD)、[`CONFIG_PM_EARLY_SYSTEM_TIMER_RESUME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM_EARLY_SYSTEM_TIMER_RESUME)、[`CONFIG_MCTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCTP)、[`CONFIG_SETTINGS_TFM_PSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS_TFM_PSA)、[`CONFIG_SHELL_TELNET_SUPPORT_COMMAND`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_TELNET_SUPPORT_COMMAND)、[`CONFIG_SHELL_CUSTOM_HEADER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_CUSTOM_HEADER)、[`CONFIG_ZTEST_BENCHMARK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST_BENCHMARK)、[`CONFIG_TRACING_CUSTOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING_CUSTOM)、[`CONFIG_USB_DEVICE_AUDIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_AUDIO)、[`CONFIG_USBD_VIDEO_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_VIDEO_CLASS)、[`CONFIG_USB_HOST_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_HOST_STACK)、[`CONFIG_USBIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBIP)、[`CONFIG_USBH_VIDEO_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBH_VIDEO_CLASS)、[`CONFIG_ZBUS_PROXY_AGENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_PROXY_AGENT)。

<a id="CONFIG_FLASH_CODE_PARTITION_USING_FIXED_PARTITIONS"></a>

## 3.54 `CONFIG_FLASH_CODE_PARTITION_USING_FIXED_PARTITIONS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果本项被选中，说明设备使用 `fixed-partitions` 或 `fixed-subpartitions` 描述分区布局，而这已由 `zephyr,mapped-partitions` 替代。对此的支持将被移除，必须正确更新 DTS 文件；请查阅 Zephyr 4.4 迁移说明（Migration Notes）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_DT_CODE_PARTITION && (CONFIG_HAS_FLASH_LOAD_OFFSET || n)
```

**默认值（Defaults）**

```text
y if (CONFIG_XIP && n) || n
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`Kconfig.zephyr:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。 → 将应用链接到设备树中的 `/chosen/zephyr,code-partition`。

**配置项引用（Symbol References）**：[`CONFIG_USE_DT_CODE_PARTITION`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_USE_DT_CODE_PARTITION)、[`CONFIG_HAS_FLASH_LOAD_OFFSET`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_HAS_FLASH_LOAD_OFFSET)、[`CONFIG_XIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XIP)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_FLASH_LOAD_OFFSET"></a>

## 3.55 `CONFIG_FLASH_LOAD_OFFSET`

**提示（Prompt）**：内核加载偏移（Kernel Load Offset）。

**说明（Help）**

指定内核加载位置相对于闪存起点的字节偏移。将其从零改为其他值会影响 Zephyr 镜像链接，并减少应用代码可用的总闪存量。若不确定，保持默认值 0。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
!CONFIG_FLASH_USES_MAPPED_PARTITION && (CONFIG_HAS_FLASH_LOAD_OFFSET || n)
```

**默认值（Defaults）**

```text
0x0 if CONFIG_USE_DT_CODE_PARTITION
0
```

**定义位置（Location）**：[`Kconfig.zephyr:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。

**配置项引用（Symbol References）**：[`CONFIG_FLASH_USES_MAPPED_PARTITION`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_FLASH_USES_MAPPED_PARTITION)、[`CONFIG_HAS_FLASH_LOAD_OFFSET`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_HAS_FLASH_LOAD_OFFSET)、[`CONFIG_USE_DT_CODE_PARTITION`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_USE_DT_CODE_PARTITION)。

<a id="CONFIG_FLASH_LOAD_SIZE"></a>

## 3.56 `CONFIG_FLASH_LOAD_SIZE`

**提示（Prompt）**：内核加载大小（Kernel Load Size）。

**说明（Help）**

非零时，指定允许 Zephyr 镜像占用的闪存区域大小，单位为字节。为零时，镜像可占用从 `FLASH_LOAD_OFFSET` 到设备末尾的区域。若不确定，保持默认值 0。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
!CONFIG_FLASH_USES_MAPPED_PARTITION && (CONFIG_HAS_FLASH_LOAD_OFFSET || n)
```

**默认值（Defaults）**

```text
0x0 if CONFIG_USE_DT_CODE_PARTITION
0
```

**定义位置（Location）**：[`Kconfig.zephyr:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。

**配置项引用（Symbol References）**：[`CONFIG_FLASH_USES_MAPPED_PARTITION`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_FLASH_USES_MAPPED_PARTITION)、[`CONFIG_HAS_FLASH_LOAD_OFFSET`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_HAS_FLASH_LOAD_OFFSET)、[`CONFIG_USE_DT_CODE_PARTITION`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_USE_DT_CODE_PARTITION)。

<a id="CONFIG_FLASH_USES_MAPPED_PARTITION"></a>

## 3.57 `CONFIG_FLASH_USES_MAPPED_PARTITION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

临时 Kconfig 选项，用于指示底层被选中的闪存分区是否使用 `zephyr,mapped-partition` 兼容标识，以便从 `fixed-partitions` 迁移。Zephyr 构建系统之外不应依赖它，将来会移除。译注：此处单数形式的兼容标识按原文保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USE_DT_CODE_PARTITION && (CONFIG_HAS_FLASH_LOAD_OFFSET || n)
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`Kconfig.zephyr:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。 → 将应用链接到设备树中的 `/chosen/zephyr,code-partition`。

**配置项引用（Symbol References）**：[`CONFIG_USE_DT_CODE_PARTITION`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_USE_DT_CODE_PARTITION)、[`CONFIG_HAS_FLASH_LOAD_OFFSET`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_HAS_FLASH_LOAD_OFFSET)。

<a id="CONFIG_FORTIFY_SOURCE_COMPILE_TIME"></a>

## 3.58 `CONFIG_FORTIFY_SOURCE_COMPILE_TIME`

**提示（Prompt）**：编译时检测（Compile-time Detection）。

**说明（Help）**

仅启用编译时检查，不增加可执行文件大小，也不降低运行性能；检查范围限于编译时可获取的信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COMPILER_SECURITY_FORTIFY>
```

**定义位置（Location）**：[`Kconfig.zephyr:575`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L575)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。 → 检测 C 标准库调用中的缓冲区溢出（Buffer Overflow）。

**配置项引用（Symbol References）**：[`CONFIG_COMPILER_SECURITY_FORTIFY`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_COMPILER_SECURITY_FORTIFY)。

<a id="CONFIG_FORTIFY_SOURCE_NONE"></a>

## 3.59 `CONFIG_FORTIFY_SOURCE_NONE`

**提示（Prompt）**：不检测（No Detection）。

**说明（Help）**

同时禁用编译时和运行时检查。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COMPILER_SECURITY_FORTIFY>
```

**定义位置（Location）**：[`Kconfig.zephyr:570`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L570)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。 → 检测 C 标准库调用中的缓冲区溢出（Buffer Overflow）。

**配置项引用（Symbol References）**：[`CONFIG_COMPILER_SECURITY_FORTIFY`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_COMPILER_SECURITY_FORTIFY)。

<a id="CONFIG_FORTIFY_SOURCE_RUN_TIME"></a>

## 3.60 `CONFIG_FORTIFY_SOURCE_RUN_TIME`

**提示（Prompt）**：编译时与运行时检测（Compile-time and Run-time Detection）。

**说明（Help）**

同时启用编译时和运行时检查。运行时检查以增加代码为代价扩大覆盖范围，检测到缓冲区溢出时，应用会引发运行时异常（Runtime Exception）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COMPILER_SECURITY_FORTIFY>
```

**定义位置（Location）**：[`Kconfig.zephyr:583`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L583)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。 → 检测 C 标准库调用中的缓冲区溢出（Buffer Overflow）。

**配置项引用（Symbol References）**：[`CONFIG_COMPILER_SECURITY_FORTIFY`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_COMPILER_SECURITY_FORTIFY)。

<a id="CONFIG_GNU_C_EXTENSIONS"></a>

## 3.61 `CONFIG_GNU_C_EXTENSIONS`

**提示（Prompt）**：GNU C 扩展（GNU C Extensions）。

**说明（Help）**

启用 GNU C 扩展。GNU C 提供若干 ISO 标准 C 中没有的语言特性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TOOLCHAIN_SUPPORTS_GNU_EXTENSIONS
```

**被选择（Selected by）**

```text
CONFIG_XEN
```

**定义位置（Location）**：[`Kconfig.zephyr:408`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L408)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

**配置项引用（Symbol References）**：[`CONFIG_TOOLCHAIN_SUPPORTS_GNU_EXTENSIONS`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_TOOLCHAIN_SUPPORTS_GNU_EXTENSIONS)、[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)。

<a id="CONFIG_HAS_FLASH_LOAD_OFFSET"></a>

## 3.62 `CONFIG_HAS_FLASH_LOAD_OFFSET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

具有 `FLASH_LOAD_OFFSET` 和 `FLASH_LOAD_SIZE` 的目标选择本选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_RP2350A_HAZARD3_0
CONFIG_SOC_RP2350B_HAZARD3_0
CONFIG_RISCV_CORE_NORDIC_VPR
CONFIG_SOC_OPENISA_RV32M1
CONFIG_SOC_FAMILY_MAX32_RV32
CONFIG_SOC_EGIS_ET171
CONFIG_CPU_AARCH32_ARM9
CONFIG_CPU_CORTEX_M
CONFIG_CPU_AARCH32_CORTEX_R
CONFIG_CPU_AARCH32_CORTEX_A
CONFIG_CPU_CORTEX_A
CONFIG_CPU_AARCH64_CORTEX_R
CONFIG_SOC_FLASH_ITE_IT8XXX2
CONFIG_SOC_FLASH_RTS5912
```

**定义位置（Location）**：[`Kconfig.zephyr:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。

**配置项引用（Symbol References）**：[`CONFIG_SOC_RP2350A_HAZARD3_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350A_HAZARD3_0)、[`CONFIG_SOC_RP2350B_HAZARD3_0`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_RP2350B_HAZARD3_0)、[`CONFIG_RISCV_CORE_NORDIC_VPR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV_CORE_NORDIC_VPR)、[`CONFIG_SOC_OPENISA_RV32M1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_OPENISA_RV32M1)、[`CONFIG_SOC_FAMILY_MAX32_RV32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_RV32)、[`CONFIG_SOC_EGIS_ET171`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_EGIS_ET171)、[`CONFIG_CPU_AARCH32_ARM9`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH32_ARM9)、[`CONFIG_CPU_CORTEX_M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_M)、[`CONFIG_CPU_AARCH32_CORTEX_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH32_CORTEX_R)、[`CONFIG_CPU_AARCH32_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH32_CORTEX_A)、[`CONFIG_CPU_CORTEX_A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_A)、[`CONFIG_CPU_AARCH64_CORTEX_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_AARCH64_CORTEX_R)、[`CONFIG_SOC_FLASH_ITE_IT8XXX2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_ITE_IT8XXX2)、[`CONFIG_SOC_FLASH_RTS5912`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FLASH_RTS5912)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_MAX32_RV32`。

<a id="CONFIG_HAS_SRAM_OFFSET"></a>

## 3.63 `CONFIG_HAS_SRAM_OFFSET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

需要 `SRAM_OFFSET` 的目标选择本选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_X86_PC_COMPATIBLE
```

**定义位置（Location）**：[`Kconfig.zephyr:256`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L256)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。

**配置项引用（Symbol References）**：[`CONFIG_X86_PC_COMPATIBLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_X86_PC_COMPATIBLE)。

<a id="CONFIG_HAVE_CUSTOM_LINKER_SCRIPT"></a>

## 3.64 `CONFIG_HAVE_CUSTOM_LINKER_SCRIPT`

**提示（Prompt）**：已提供自定义链接脚本（Custom Linker Script）。

**说明（Help）**

如果有需要在 `CUSTOM_LINKER_SCRIPT` 中指定的自定义链接脚本（Custom Linker Script），请设置本选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING
```

**定义位置（Location）**：[`Kconfig.zephyr:222`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L222)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_MAX32_SECURE_SOC_SIGNING)。

<a id="CONFIG_IS_BOOTLOADER"></a>

## 3.65 `CONFIG_IS_BOOTLOADER`

**提示（Prompt）**：充当引导加载程序（Bootloader）。

**说明（Help）**

本选项表示 Zephyr 将作为引导加载程序（Bootloader），执行独立的 Zephyr 镜像载荷（Image Payload）。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:1088`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L1088)。

**菜单路径（Menu Path）**：顶层（Top） → 启动选项（Boot Options）。

<a id="CONFIG_KERNEL_BIN_NAME"></a>

## 3.66 `CONFIG_KERNEL_BIN_NAME`

**提示（Prompt）**：内核二进制文件名（Kernel Binary Name）。

**说明（Help）**

设置生成的内核二进制文件名称。

**类型（Type）**：字符串（String），`string`。

**默认值（Defaults）**

```text
"zephyr"
```

**定义位置（Location）**：[`Kconfig.zephyr:689`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L689)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<a id="CONFIG_KERNEL_ENTRY"></a>

## 3.67 `CONFIG_KERNEL_ENTRY`

**提示（Prompt）**：内核入口符号（Kernel Entry Symbol）。

**说明（Help）**

代码入口符号，在链接阶段设置。

**类型（Type）**：字符串（String），`string`。

**默认值（Defaults）**

```text
"__start"
```

**定义位置（Location）**：[`Kconfig.zephyr:242`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L242)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。

<a id="CONFIG_LD_LINKER_TEMPLATE"></a>

## 3.68 `CONFIG_LD_LINKER_TEMPLATE`

**提示（Prompt）**：LD 模板（LD Template）。

**说明（Help）**

使用 LD 链接脚本模板（Linker Script Templates）。模板经 C 预处理器处理，生成最终 LD 链接脚本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LD_LINKER_SCRIPT_SUPPORTED && <choice CONFIG_LINKER_SCRIPT>
```

**定义位置（Location）**：[`Kconfig.zephyr:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L202)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。 → 链接脚本（Linker Script）。

**配置项引用（Symbol References）**：[`CONFIG_LD_LINKER_SCRIPT_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LD_LINKER_SCRIPT_SUPPORTED)、[`CONFIG_LINKER_SCRIPT`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LINKER_SCRIPT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LD_LINKER_SCRIPT_SUPPORTED`。

<a id="CONFIG_LEGACY_GENERATED_INCLUDE_PATH"></a>

## 3.69 `CONFIG_LEGACY_GENERATED_INCLUDE_PATH`

**提示（Prompt）**：生成头文件的旧式包含路径（Legacy Include Path）［已弃用］。

**说明（Help）**

允许应用和库对生成的头文件使用 Zephyr 旧式包含路径，即不带 `zephyr/` 前缀的路径。现在推荐以 `<zephyr/version.h>` 包含 `version.h` 头文件。本 Kconfig 选项将在未来版本移除。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`Kconfig.zephyr:1139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L1139)。

**菜单路径（Menu Path）**：顶层（Top） → 兼容性（Compatibility）。

**配置项引用（Symbol References）**：[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_LINKER_DEVNULL_MEMORY"></a>

## 3.70 `CONFIG_LINKER_DEVNULL_MEMORY`

**提示（Prompt）**：丢弃区域（Devnull Region）。

**说明（Help）**

创建丢弃区域（Devnull Region），从最终二进制文件剔除，但在副产物 ELF 文件中保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LINKER_DEVNULL_SUPPORT
```

**被弱选择（Implied by）**

```text
CONFIG_NRF_MPCCONF_SECTION
CONFIG_NRF_PERIPHCONF_SECTION_STRIP
CONFIG_NRF_MPCCONF_SECTION
CONFIG_NRF_PERIPHCONF_SECTION_STRIP
CONFIG_LOG_FMT_SECTION_STRIP
```

**定义位置（Location）**：[`Kconfig.zephyr:352`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L352)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。

**配置项引用（Symbol References）**：[`CONFIG_LINKER_DEVNULL_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LINKER_DEVNULL_SUPPORT)、[`CONFIG_NRF_MPCCONF_SECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_MPCCONF_SECTION)、[`CONFIG_NRF_PERIPHCONF_SECTION_STRIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_PERIPHCONF_SECTION_STRIP)、[`CONFIG_LOG_FMT_SECTION_STRIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG_FMT_SECTION_STRIP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LINKER_DEVNULL_SUPPORT`。

<a id="CONFIG_LINKER_DEVNULL_MEMORY_SIZE"></a>

## 3.71 `CONFIG_LINKER_DEVNULL_MEMORY_SIZE`

**提示（Prompt）**：丢弃区域大小（Devnull Region Size）。

**说明（Help）**

可调整大小，以容纳放入该区域的全部数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LINKER_DEVNULL_MEMORY
```

**默认值（Defaults）**

```text
262144
```

**定义位置（Location）**：[`Kconfig.zephyr:359`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L359)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。 → 丢弃区域（Devnull Region）。

**配置项引用（Symbol References）**：[`CONFIG_LINKER_DEVNULL_MEMORY`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LINKER_DEVNULL_MEMORY)。

<a id="CONFIG_LINKER_ITERABLE_SUBALIGN"></a>

## 3.72 `CONFIG_LINKER_ITERABLE_SUBALIGN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

用于设置可迭代段（Iterable Sections）默认子对齐（Subalignment）的隐藏选项。

**类型（Type）**：整数（Integer），`int`。

**默认值（Defaults）**

```text
8 if CONFIG_64BIT
4
```

**定义位置（Location）**：[`Kconfig.zephyr:341`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L341)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。

**配置项引用（Symbol References）**：[`CONFIG_64BIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_64BIT)。

<a id="CONFIG_LINKER_LAST_SECTION_ID"></a>

## 3.73 `CONFIG_LINKER_LAST_SECTION_ID`

**提示（Prompt）**：末节标识符（Last Section Identifier）。

**说明（Help）**

启用后，在最后一个节中放置标识符，确保链接符号 `_flash_used` 始终正确计算，即使位置计数器（Location Counter）因对齐而增加、对齐后却未放入任何数据。注意，如果闪存已经完全用满，例如在闪存区域末尾写入了应用专用数据，再写入末节标识符可能导致 ROM 区域溢出，此时应禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM || CONFIG_ARM64 || CONFIG_RISCV
```

**默认值（Defaults）**

```text
y if !CONFIG_ARM64
```

**定义位置（Location）**：[`Kconfig.zephyr:296`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L296)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。 → 链接器节（Linker Sections）。

**配置项引用（Symbol References）**：[`CONFIG_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM)、[`CONFIG_ARM64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM64)、[`CONFIG_RISCV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RISCV)。

<a id="CONFIG_LINKER_LAST_SECTION_ID_PATTERN"></a>

## 3.74 `CONFIG_LINKER_LAST_SECTION_ID_PATTERN`

**提示（Prompt）**：末节标识符模式（Last Section Identifier Pattern）。

**说明（Help）**

填入最后一个节作为标识符的数值模式。默认值为 `0xE015`，表示最后一个节结束（End of Last Section），也可使用其他模式，但大小不得超过 4 字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_LINKER_LAST_SECTION_ID
```

**默认值（Defaults）**

```text
"0xE015E015"
```

**定义位置（Location）**：[`Kconfig.zephyr:312`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L312)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。 → 链接器节（Linker Sections）。 → 末节标识符（Last Section Identifier）。

**配置项引用（Symbol References）**：[`CONFIG_LINKER_LAST_SECTION_ID`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LINKER_LAST_SECTION_ID)。

<a id="CONFIG_LINKER_ORPHAN_CONFIGURATION"></a>

## 3.75 `CONFIG_LINKER_ORPHAN_CONFIGURATION`

**提示（Prompt）**：链接器孤立节处理（Orphan Section Handling）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
CONFIG_LINKER_ORPHAN_SECTION_WARN
```

**可选项（Choices）**

```text
CONFIG_LINKER_ORPHAN_SECTION_PLACE
CONFIG_LINKER_ORPHAN_SECTION_WARN
CONFIG_LINKER_ORPHAN_SECTION_ERROR
```

**定义位置（Location）**：[`Kconfig.zephyr:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。

**配置项引用（Symbol References）**：[`CONFIG_LINKER_ORPHAN_SECTION_WARN`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LINKER_ORPHAN_SECTION_WARN)、[`CONFIG_LINKER_ORPHAN_SECTION_PLACE`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LINKER_ORPHAN_SECTION_PLACE)、[`CONFIG_LINKER_ORPHAN_SECTION_ERROR`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LINKER_ORPHAN_SECTION_ERROR)。

<a id="CONFIG_LINKER_ORPHAN_SECTION_ERROR"></a>

## 3.76 `CONFIG_LINKER_ORPHAN_SECTION_ERROR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

发现孤立节（Orphan Section）时，链接器以错误退出。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LINKER_ORPHAN_CONFIGURATION>
```

**定义位置（Location）**：[`Kconfig.zephyr:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。 → 链接器孤立节处理（Orphan Section Handling）。

**配置项引用（Symbol References）**：[`CONFIG_LINKER_ORPHAN_CONFIGURATION`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LINKER_ORPHAN_CONFIGURATION)。

<a id="CONFIG_LINKER_ORPHAN_SECTION_PLACE"></a>

## 3.77 `CONFIG_LINKER_ORPHAN_SECTION_PLACE`

**提示（Prompt）**：放置（Place）。

**说明（Help）**

链接器自行放置孤立节（Orphan Section），不发出警告或错误。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LINKER_ORPHAN_CONFIGURATION>
```

**定义位置（Location）**：[`Kconfig.zephyr:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。 → 链接器孤立节处理（Orphan Section Handling）。

**配置项引用（Symbol References）**：[`CONFIG_LINKER_ORPHAN_CONFIGURATION`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LINKER_ORPHAN_CONFIGURATION)。

<a id="CONFIG_LINKER_ORPHAN_SECTION_WARN"></a>

## 3.78 `CONFIG_LINKER_ORPHAN_SECTION_WARN`

**提示（Prompt）**：警告（Warn）。

**说明（Help）**

链接器将孤立节（Orphan Section）放入输出，并针对这些节发出警告。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LINKER_ORPHAN_CONFIGURATION>
```

**定义位置（Location）**：[`Kconfig.zephyr:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。 → 链接器孤立节处理（Orphan Section Handling）。

**配置项引用（Symbol References）**：[`CONFIG_LINKER_ORPHAN_CONFIGURATION`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LINKER_ORPHAN_CONFIGURATION)。

<a id="CONFIG_LINKER_SCRIPT"></a>

## 3.79 `CONFIG_LINKER_SCRIPT`

**提示（Prompt）**：链接脚本（Linker Script）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
CONFIG_LD_LINKER_TEMPLATE if CONFIG_LD_LINKER_SCRIPT_SUPPORTED
```

**可选项（Choices）**

```text
CONFIG_LD_LINKER_TEMPLATE
CONFIG_CMAKE_LINKER_GENERATOR
```

**定义位置（Location）**：[`Kconfig.zephyr:198`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L198)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。

**配置项引用（Symbol References）**：[`CONFIG_LD_LINKER_TEMPLATE`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LD_LINKER_TEMPLATE)、[`CONFIG_LD_LINKER_SCRIPT_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LD_LINKER_SCRIPT_SUPPORTED)、[`CONFIG_CMAKE_LINKER_GENERATOR`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_CMAKE_LINKER_GENERATOR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LD_LINKER_SCRIPT_SUPPORTED`。

<a id="CONFIG_LINKER_SORT_BY_ALIGNMENT"></a>

## 3.80 `CONFIG_LINKER_SORT_BY_ALIGNMENT`

**提示（Prompt）**：按对齐要求排序输入节（Sort Input Sections by Alignment）。

**说明（Help）**

启用链接器标志，按对齐要求对节排序，使符号按大小递减排列，帮助减少符号之间的填充空间（Padding）。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`Kconfig.zephyr:248`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L248)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。

<a id="CONFIG_LINKER_USE_BOOT_SECTION"></a>

## 3.81 `CONFIG_LINKER_USE_BOOT_SECTION`

**提示（Prompt）**：使用启动专用链接节（Boot Linker Section）。

**说明（Help）**

启用后，将启动流程所需符号放入专门保留的另一链接节。要求架构、SoC、开发板或自定义链接脚本中存在启动节（Boot Sections）。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:274`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L274)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。 → 链接器节（Linker Sections）。

<a id="CONFIG_LINKER_USE_NO_RELAX"></a>

## 3.82 `CONFIG_LINKER_USE_NO_RELAX`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏符号，允许其他特性强制禁用链接松弛（Relaxation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_USERSPACE
```

**定义位置（Location）**：[`Kconfig.zephyr:322`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L322)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。 → 链接器节（Linker Sections）。

**配置项引用（Symbol References）**：[`CONFIG_USERSPACE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USERSPACE)。

<a id="CONFIG_LINKER_USE_ONDEMAND_SECTION"></a>

## 3.83 `CONFIG_LINKER_USE_ONDEMAND_SECTION`

**提示（Prompt）**：使用可淘汰链接节（Evictable Linker Section）。

**说明（Help）**

启用后，将可从内存淘汰的符号放入为按需符号保留的链接节。启动期间，对应内存映射为已换出（Paged Out）。要求架构、SoC、开发板或自定义链接脚本中存在按需节（On-demand Sections）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEMAND_MAPPING && !CONFIG_ARCH_MAPS_ALL_RAM
```

**定义位置（Location）**：[`Kconfig.zephyr:284`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L284)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。 → 链接器节（Linker Sections）。

**配置项引用（Symbol References）**：[`CONFIG_DEMAND_MAPPING`](P001_kernel_配置项参考_1.md#CONFIG_DEMAND_MAPPING)、[`CONFIG_ARCH_MAPS_ALL_RAM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_MAPS_ALL_RAM)。

<a id="CONFIG_LINKER_USE_RELAX"></a>

## 3.84 `CONFIG_LINKER_USE_RELAX`

**提示（Prompt）**：链接器调用寻址优化（Call Addressing Optimization）。

**说明（Help）**

链接器解析程序寻址后，本选项执行由此成为可能的全局优化，例如放宽寻址模式限制，并在输出目标文件中合成新指令。对于 ld 和 lld，启用 `--relax`。不支持此功能的平台也接受 `--relax`，但会忽略。禁用可能降低性能，因为链接器不再能将较长或低效的跳转／调用替换为更短或高效的指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LINKER_USE_NO_RELAX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`Kconfig.zephyr:327`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L327)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 链接器选项（Linker Options）。 → 链接器节（Linker Sections）。

**配置项引用（Symbol References）**：[`CONFIG_LINKER_USE_NO_RELAX`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LINKER_USE_NO_RELAX)。

<a id="CONFIG_LTO"></a>

## 3.85 `CONFIG_LTO`

**提示（Prompt）**：链接时优化（Link Time Optimization，LTO）。

**说明（Help）**

启用链接时优化（Link Time Optimization，LTO）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!(CONFIG_GEN_ISR_TABLES || CONFIG_GEN_IRQ_VECTOR_TABLE) || CONFIG_ISR_TABLES_LOCAL_DECLARATION) && !CONFIG_NATIVE_LIBRARY && !CONFIG_CODE_DATA_RELOCATION
```

**定义位置（Location）**：[`Kconfig.zephyr:503`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L503)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

**配置项引用（Symbol References）**：[`CONFIG_GEN_ISR_TABLES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GEN_ISR_TABLES)、[`CONFIG_GEN_IRQ_VECTOR_TABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GEN_IRQ_VECTOR_TABLE)、[`CONFIG_ISR_TABLES_LOCAL_DECLARATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ISR_TABLES_LOCAL_DECLARATION)、[`CONFIG_NATIVE_LIBRARY`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NATIVE_LIBRARY)、[`CONFIG_CODE_DATA_RELOCATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CODE_DATA_RELOCATION)。

<a id="CONFIG_LTO_SINGLE_THREADED"></a>

## 3.86 `CONFIG_LTO_SINGLE_THREADED`

**提示（Prompt）**：单线程链接时优化（Single-threaded LTO）。

**说明（Help）**

要求链接器使用单个线程处理链接时优化（LTO）。详情参见 [Zephyr SDK 问题 #1038](https://github.com/zephyrproject-rtos/sdk-ng/issues/1038)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LTO
```

**定义位置（Location）**：[`Kconfig.zephyr:511`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L511)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。 → 链接时优化（Link Time Optimization，LTO）。

**配置项引用（Symbol References）**：[`CONFIG_LTO`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_LTO)。

<a id="CONFIG_MAKEFILE_EXPORTS"></a>

## 3.87 `CONFIG_MAKEFILE_EXPORTS`

**提示（Prompt）**：生成名为 `Makefile.exports` 的构建元数据文件。

**说明（Help）**

生成包含构建信息的文件，供基于 Makefile 的第三方构建系统读取。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:946`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L946)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<a id="CONFIG_MISRA_SANE"></a>

## 3.88 `CONFIG_MISRA_SANE`

**提示（Prompt）**：MISRA 标准符合性特性（MISRA Standards Compliance Features）。

**说明（Help）**

使源码以“MISRA”模式构建，出于安全原因禁用 C 标准原本允许的一些特性，具体是不允许变长数组（Variable-length Array），由 GCC 强制执行。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:603`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L603)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

<a id="CONFIG_NATIVE_BUILD"></a>

## 3.89 `CONFIG_NATIVE_BUILD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

以主机系统为目标构建 Zephyr，用于调试和开发。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_NATIVE_LIBC if CONFIG_EXTERNAL_LIBC
CONFIG_NATIVE_LIBCPP if CONFIG_EXTERNAL_LIBCPP
```

**被选择（Selected by）**

```text
CONFIG_ARCH_POSIX
CONFIG_NATIVE_LIBRARY
```

**定义位置（Location）**：[`Kconfig.zephyr:434`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L434)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

**配置项引用（Symbol References）**：[`CONFIG_NATIVE_LIBC`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NATIVE_LIBC)、[`CONFIG_EXTERNAL_LIBC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EXTERNAL_LIBC)、[`CONFIG_NATIVE_LIBCPP`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NATIVE_LIBCPP)、[`CONFIG_EXTERNAL_LIBCPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EXTERNAL_LIBCPP)、[`CONFIG_ARCH_POSIX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_POSIX)、[`CONFIG_NATIVE_LIBRARY`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NATIVE_LIBRARY)。

<a id="CONFIG_NATIVE_LIBC"></a>

## 3.90 `CONFIG_NATIVE_LIBC`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Zephyr 使用主机系统的 C 标准库。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_FULL_LIBC_SUPPORTED
CONFIG_TC_PROVIDES_POSIX_C_LANG_SUPPORT_R
```

**被选择（Selected by）**

```text
CONFIG_NATIVE_BUILD
```

**定义位置（Location）**：[`Kconfig.zephyr:421`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L421)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

**配置项引用（Symbol References）**：[`CONFIG_FULL_LIBC_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FULL_LIBC_SUPPORTED)、[`CONFIG_TC_PROVIDES_POSIX_C_LANG_SUPPORT_R`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TC_PROVIDES_POSIX_C_LANG_SUPPORT_R)、[`CONFIG_NATIVE_BUILD`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NATIVE_BUILD)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_TC_PROVIDES_POSIX_C_LANG_SUPPORT_R`。

<a id="CONFIG_NATIVE_LIBCPP"></a>

## 3.91 `CONFIG_NATIVE_LIBCPP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Zephyr 使用主机系统的 C++ 标准库。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_FULL_LIBCPP_SUPPORTED
```

**被选择（Selected by）**

```text
CONFIG_NATIVE_BUILD
```

**定义位置（Location）**：[`Kconfig.zephyr:428`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L428)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

**配置项引用（Symbol References）**：[`CONFIG_FULL_LIBCPP_SUPPORTED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FULL_LIBCPP_SUPPORTED)、[`CONFIG_NATIVE_BUILD`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NATIVE_BUILD)。

<a id="CONFIG_NATIVE_LIBRARY"></a>

## 3.92 `CONFIG_NATIVE_LIBRARY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

构建为本地主机目标的预链接库（Prelinked Library），之后可将该库构建进主机可执行文件。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_NATIVE_BUILD
```

**定义位置（Location）**：[`Kconfig.zephyr:442`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L442)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。

**配置项引用（Symbol References）**：[`CONFIG_NATIVE_BUILD`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NATIVE_BUILD)。

<a id="CONFIG_NOT_SECURE"></a>

## 3.93 `CONFIG_NOT_SECURE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

特性选择此符号，以表示该特性不安全（Not Secure）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_LEGACY_CRYPTO
CONFIG_WIFI_NM_WPA_SUPPLICANT_WEP
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_PSA_WANT_ALG_MD5
CONFIG_WIFI_NM_WPA_SUPPLICANT_LEGACY_CRYPTO
CONFIG_WIFI_NM_WPA_SUPPLICANT_WEP
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_WIFI_NM_WPA_SUPPLICANT_LEGACY_CRYPTO
CONFIG_WIFI_NM_WPA_SUPPLICANT_WEP
CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE
CONFIG_PSA_WANT_ALG_MD5
CONFIG_FIDO2_UP_ALWAYS
CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_ENTRY_UID_HASH
```

**定义位置（Location）**：[`Kconfig.zephyr:1055`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L1055)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_LEGACY_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_LEGACY_CRYPTO)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_WEP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_WEP)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ENTERPRISE)、[`CONFIG_PSA_WANT_ALG_MD5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_WANT_ALG_MD5)、[`CONFIG_FIDO2_UP_ALWAYS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FIDO2_UP_ALWAYS)、[`CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_ENTRY_UID_HASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SECURE_STORAGE_ITS_TRANSFORM_AEAD_KEY_PROVIDER_ENTRY_UID_HASH)。

<a id="CONFIG_NO_OPTIMIZATIONS"></a>

## 3.94 `CONFIG_NO_OPTIMIZATIONS`

**提示（Prompt）**：不进行优化（Optimize Nothing）。

**说明（Help）**

独立于其他选项，将编译器优化设为 `-O0`。选择后，通常需要手动调整默认栈大小，以避免栈溢出（Stack Overflow）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_COMPILER_OPTIMIZATIONS>
```

**定义位置（Location）**：[`Kconfig.zephyr:493`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L493)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 编译器选项（Compiler Options）。 → 优化级别（Optimization Level）。

**配置项引用（Symbol References）**：[`CONFIG_COMPILER_OPTIMIZATIONS`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_COMPILER_OPTIMIZATIONS)。

<a id="CONFIG_NO_RUNTIME_CHECKS"></a>

## 3.95 `CONFIG_NO_RUNTIME_CHECKS`

**提示（Prompt）**：不执行运行时错误检查（No Runtime Error Checks）。

**说明（Help）**

使用 `CHECKIF()` 宏时，不进行任何运行时检查或断言。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`Kconfig.zephyr:674`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L674)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → `CHECK` 宏的错误检查行为（Error Checking Behavior）。

<a id="CONFIG_OUTPUT_DISASSEMBLE_ALL"></a>

## 3.96 `CONFIG_OUTPUT_DISASSEMBLE_ALL`

**提示（Prompt）**：反汇编所有节并包含源码，填充零。

**说明（Help）**

`.lst` 文件包含固件所有部分的完整反汇编，不限于预期包含指令的部分，也包含零值内容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OUTPUT_DISASSEMBLY
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`Kconfig.zephyr:711`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L711)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。 → 创建反汇编文件（Disassembly File）。

**配置项引用（Symbol References）**：[`CONFIG_OUTPUT_DISASSEMBLY`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_OUTPUT_DISASSEMBLY)。

<a id="CONFIG_OUTPUT_DISASSEMBLY"></a>

## 3.97 `CONFIG_OUTPUT_DISASSEMBLY`

**提示（Prompt）**：创建反汇编文件（Disassembly File）。

**说明（Help）**

创建包含固件汇编清单（Assembly Listing）的 `.lst` 文件。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`Kconfig.zephyr:706`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L706)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<a id="CONFIG_OUTPUT_DISASSEMBLY_NO_ALIASES"></a>

## 3.98 `CONFIG_OUTPUT_DISASSEMBLY_NO_ALIASES`

**提示（Prompt）**：使用原始指令助记符反汇编（Raw Instruction Mnemonics）。

**说明（Help）**

`.lst` 文件包含原始指令助记符（Instruction Mnemonic），而不是伪指令（Pseudo Instruction）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OUTPUT_DISASSEMBLY
```

**定义位置（Location）**：[`Kconfig.zephyr:730`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L730)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。 → 创建反汇编文件（Disassembly File）。

**配置项引用（Symbol References）**：[`CONFIG_OUTPUT_DISASSEMBLY`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_OUTPUT_DISASSEMBLY)。

<a id="CONFIG_OUTPUT_DISASSEMBLY_WITH_SOURCE"></a>

## 3.99 `CONFIG_OUTPUT_DISASSEMBLY_WITH_SOURCE`

**提示（Prompt）**：在输出反汇编文件中包含源码。

**说明（Help）**

`.lst` 文件也包含源码。控制是否包含源码有助于可复现构建（Reproducible Builds），因为可借此移除 `.lst` 中可能因平台而异的内容，例如由 `..` 包含路径引起的差异。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OUTPUT_DISASSEMBLY && !CONFIG_OUTPUT_DISASSEMBLE_ALL
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`Kconfig.zephyr:719`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L719)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。 → 创建反汇编文件（Disassembly File）。

**配置项引用（Symbol References）**：[`CONFIG_OUTPUT_DISASSEMBLY`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_OUTPUT_DISASSEMBLY)、[`CONFIG_OUTPUT_DISASSEMBLE_ALL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_OUTPUT_DISASSEMBLE_ALL)。

<a id="CONFIG_OUTPUT_PRINT_MEMORY_USAGE"></a>

## 3.100 `CONFIG_OUTPUT_PRINT_MEMORY_USAGE`

**提示（Prompt）**：向标准输出（stdout）打印内存用量。

**说明（Help）**

若工具链支持，本选项在链接器第一遍处理时传入 `--print-memory-region`。注意，内存区域（Memory Region）是链接脚本定义的符号概念，不一定直接对应实际物理地址空间。某些平台会执行两遍链接，因此结果不一定与最终 ELF 文件完全一致。另见 `rom_report`、`ram_report` 及 [GNU ld 的 MEMORY 文档](https://sourceware.org/binutils/docs/ld/MEMORY.html)。译注：选项名 `--print-memory-region` 按本条原文保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`Kconfig.zephyr:737`](https://github.com/zephyrproject-rtos/zephyr/blob/main/Kconfig.zephyr#L737)。

**菜单路径（Menu Path）**：顶层（Top） → 构建与链接特性（Build and Link Features）。 → 构建选项（Build Options）。

<!-- kconfig-navigation -->

[上一章](P002_kernel_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P004_Kconfig.zephyr_配置项参考_2.md)
