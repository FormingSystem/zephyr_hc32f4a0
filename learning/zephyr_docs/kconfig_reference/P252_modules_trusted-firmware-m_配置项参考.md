---
id: learning.zephyr-docs.kconfig-reference.page-252
title: "`modules/trusted-firmware-m`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第252章\_`modules/trusted-firmware-m`配置项参考

本章翻译官方 Kconfig 数据库中 `modules/trusted-firmware-m` 的 99 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BUILD_WITH_TFM"></a>

## 252.1 `CONFIG_BUILD_WITH_TFM`

原库同名定义共 3 条；本项为数据库第 3447 条记录，各定义分别保留。

**提示（Prompt）**：构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**说明（Help）**

启用后，此选项指示 Zephyr 构建过程在生成 Zephyr 镜像的同时，额外生成用于安全执行环境（Secure Execution Environment）的 TF-M 镜像。Zephyr 镜像本身将在非安全处理环境（Non-Secure Processing Environment）中执行。对 `TRUSTED_EXECUTION_NONSECURE` 的必要依赖可确保 Zephyr 镜像作为非安全镜像构建。在正常 Zephyr 构建过程中，会生成 TF-M 和 Zephyr 两个镜像，以及连接两者的跳板目标文件（veneer object file）。

注意：

- 使用带 `/ns` 的 `BOARD` 变体构建，例如 `mps2/an521/cpu0/ns`，可确保启用 `CONFIG_TRUSTED_EXECUTION_NONSECURE`。
- 默认允许 Zephyr 可抢占线程（preemptible thread）在执行安全函数调用（secure function call）期间被抢占。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRUSTED_EXECUTION_NONSECURE && CONFIG_TFM_BOARD != "" && CONFIG_ARM_TRUSTZONE_M
```

**主动选择（Selects）**

```text
CONFIG_BUILD_OUTPUT_HEX
```

**弱选择（Implies）**

```text
CONFIG_INIT_ARCH_HW_AT_BOOT
CONFIG_ARM_NONSECURE_PREEMPTIBLE_SECURE_CALLS
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_TRUSTED_EXECUTION_NONSECURE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_TRUSTED_EXECUTION_NONSECURE)、[`CONFIG_TFM_BOARD`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BOARD)、[`CONFIG_ARM_TRUSTZONE_M`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_TRUSTZONE_M)、[`CONFIG_BUILD_OUTPUT_HEX`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BUILD_OUTPUT_HEX)、[`CONFIG_INIT_ARCH_HW_AT_BOOT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_INIT_ARCH_HW_AT_BOOT)、[`CONFIG_ARM_NONSECURE_PREEMPTIBLE_SECURE_CALLS`](P029_arch_arm_配置项参考_1.md#CONFIG_ARM_NONSECURE_PREEMPTIBLE_SECURE_CALLS)。

<a id="CONFIG_ROM_START_OFFSET"></a>

## 252.2 `CONFIG_ROM_START_OFFSET`

原库同名定义共 2 条；本项为数据库第 16259 条记录，各定义分别保留。

**提示（Prompt）**：在非安全镜像中为 BL2 头部预留空间的 ROM 起始偏移（ROM Start Offset）

**说明（Help）**

TF-M 中的 BL2 头部（header）大小默认为 `0x400`。如果 TF-M 改用其他 BL2 头部大小，则需要更新 `ROM_START_OFFSET`。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_BL2 && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
0x400
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:532`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L532)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_BL2`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_BL1"></a>

## 252.3 `CONFIG_TFM_BL1`

**提示（Prompt）**：将 BL1 添加到 TFM（Add BL1 to TFM）

**说明（Help）**

TFM 设计为可在特定配置中与 BL1 一同运行。此配置将 BL1 加入构建，并通过 TFM 构建系统构建它。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:235`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L235)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_BL2"></a>

## 252.4 `CONFIG_TFM_BL2`

**提示（Prompt）**：将 MCUboot 添加到 TFM（Add MCUboot to TFM）

**说明（Help）**

TFM 设计为可在特定配置中与 MCUboot 一同运行。此配置将 MCUboot 加入构建，并通过 TFM 构建系统构建它。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_TFM_BL2_NOT_SUPPORTED && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:241`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L241)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_BL2_NOT_SUPPORTED`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2_NOT_SUPPORTED)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_BL2_LOG_LEVEL"></a>

## 252.5 `CONFIG_TFM_BL2_LOG_LEVEL`

**提示（Prompt）**：BL2 日志级别（Log Level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_BL2 && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
CONFIG_TFM_BL2_LOG_LEVEL_INFO
```

**可选项（Choices）**

```text
CONFIG_TFM_BL2_LOG_LEVEL_DEBUG
CONFIG_TFM_BL2_LOG_LEVEL_INFO
CONFIG_TFM_BL2_LOG_LEVEL_WARNING
CONFIG_TFM_BL2_LOG_LEVEL_ERROR
CONFIG_TFM_BL2_LOG_LEVEL_OFF
CONFIG_TFM_BL2_LOG_LEVEL_DEBUG
CONFIG_TFM_BL2_LOG_LEVEL_INFO
CONFIG_TFM_BL2_LOG_LEVEL_WARNING
CONFIG_TFM_BL2_LOG_LEVEL_ERROR
CONFIG_TFM_BL2_LOG_LEVEL_OFF
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:540`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L540)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_BL2`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_BL2_LOG_LEVEL_INFO`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2_LOG_LEVEL_INFO)、[`CONFIG_TFM_BL2_LOG_LEVEL_DEBUG`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2_LOG_LEVEL_DEBUG)、[`CONFIG_TFM_BL2_LOG_LEVEL_WARNING`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2_LOG_LEVEL_WARNING)、[`CONFIG_TFM_BL2_LOG_LEVEL_ERROR`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2_LOG_LEVEL_ERROR)、[`CONFIG_TFM_BL2_LOG_LEVEL_OFF`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2_LOG_LEVEL_OFF)。

<a id="CONFIG_TFM_BL2_LOG_LEVEL_DEBUG"></a>

## 252.6 `CONFIG_TFM_BL2_LOG_LEVEL_DEBUG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_BL2_LOG_LEVEL>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:543`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L543)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → BL2 日志级别（Log Level）

**配置项引用（Symbol References）**：[`CONFIG_TFM_BL2_LOG_LEVEL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2_LOG_LEVEL)。

<a id="CONFIG_TFM_BL2_LOG_LEVEL_ERROR"></a>

## 252.7 `CONFIG_TFM_BL2_LOG_LEVEL_ERROR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_BL2_LOG_LEVEL>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:549`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L549)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → BL2 日志级别（Log Level）

**配置项引用（Symbol References）**：[`CONFIG_TFM_BL2_LOG_LEVEL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2_LOG_LEVEL)。

<a id="CONFIG_TFM_BL2_LOG_LEVEL_INFO"></a>

## 252.8 `CONFIG_TFM_BL2_LOG_LEVEL_INFO`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_BL2_LOG_LEVEL>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:545`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L545)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → BL2 日志级别（Log Level）

**配置项引用（Symbol References）**：[`CONFIG_TFM_BL2_LOG_LEVEL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2_LOG_LEVEL)。

<a id="CONFIG_TFM_BL2_LOG_LEVEL_OFF"></a>

## 252.9 `CONFIG_TFM_BL2_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_BL2_LOG_LEVEL>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:551`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L551)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → BL2 日志级别（Log Level）

**配置项引用（Symbol References）**：[`CONFIG_TFM_BL2_LOG_LEVEL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2_LOG_LEVEL)。

<a id="CONFIG_TFM_BL2_LOG_LEVEL_WARNING"></a>

## 252.10 `CONFIG_TFM_BL2_LOG_LEVEL_WARNING`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_BL2_LOG_LEVEL>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:547`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L547)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → BL2 日志级别（Log Level）

**配置项引用（Symbol References）**：[`CONFIG_TFM_BL2_LOG_LEVEL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2_LOG_LEVEL)。

<a id="CONFIG_TFM_BL2_NOT_SUPPORTED"></a>

## 252.11 `CONFIG_TFM_BL2_NOT_SUPPORTED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，用于标记不支持 BL2，即 TF-M 中包含的 MCUBoot。不使用 BL2 的平台应选择此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:214`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L214)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_BL2_SIGNING_KEY_PATH"></a>

## 252.12 `CONFIG_TFM_BL2_SIGNING_KEY_PATH`

**提示（Prompt）**：用于签署 BL2 固件镜像的私钥路径（private key path）

**说明（Help）**

二进制 BL2 签名私钥（signing private key）的路径。如果针对该开发板的 TF-M 配置未修改此值，则默认为 `$(ZEPHYR_TRUSTED_FIRMWARE_M_MODULE_DIR)/bl1/bl1_2/bl1_dummy_rotpk`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_BL1 && CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:311`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L311)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_BL1`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL1)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_BOARD"></a>

## 252.13 `CONFIG_TFM_BOARD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

构建 TFM 所用的开发板名称（board name）。与 TFM 一同构建，要求 TFM 已移植到对应开发板／片上系统（SoC）。

**类型（Type）**：字符串（String），`string`。

**默认值（Defaults）**

```text
"adi/max32657" if BOARD_MAX32657EVKIT_MAX32657_NS || BOARD_MAX32658EVKIT_MAX32658_NS
"arm/mps2/an521" if BOARD_MPS2_AN521_CPU0_NS
"nxp/frdmmcxn947" if BOARD_FRDM_MCXN947_MCXN947_CPU0_NS
"nxp/frdmmcxa577" if BOARD_FRDM_MCXA577_MCXA577_NS
"arm/mps3/corstone300/fvp" if BOARD_MPS3_CORSTONE300_FVP_NS
"arm/mps3/corstone300/an547" if BOARD_MPS3_CORSTONE300_AN547_NS
"arm/mps3/corstone300/an552" if BOARD_MPS3_CORSTONE300_AN552_NS
"arm/mps3/corstone310/an555" if BOARD_MPS3_CORSTONE310_AN555_NS
"arm/mps3/corstone310/fvp" if BOARD_MPS3_CORSTONE310_FVP_NS
"arm/mps4/corstone315" if BOARD_MPS4_CORSTONE315_FVP_NS
"arm/mps4/corstone320" if BOARD_MPS4_CORSTONE320_FVP_NS
"arm/musca_b1" if CONFIG_BOARD_V2M_MUSCA_B1
"arm/musca_s1" if CONFIG_BOARD_V2M_MUSCA_S1
"infineon/pse84" if BOARD_KIT_PSE84_EVAL_PSE846GPS2DBZC4A_M33_NS
"infineon/pse84" if BOARD_KIT_PSE84_AI_PSE846GPS2DBZC4A_M33_NS
"nxp/lpcxpresso55s69" if BOARD_LPCXPRESSO55S69_LPC55S69_CPU0_NS
"stm/b_u585i_iot02a" if CONFIG_BOARD_B_U585I_IOT02A
"stm/nucleo_l552ze_q" if CONFIG_BOARD_NUCLEO_L552ZE_Q
"stm/nucleo_u3c5zi_q" if CONFIG_BOARD_NUCLEO_U3C5ZI_Q
"stm/stm32h573i_dk" if CONFIG_BOARD_STM32H573I_DK
"stm/stm32l562e_dk" if CONFIG_BOARD_STM32L562E_DK
"stm/stm32wba65i_dk" if CONFIG_BOARD_NUCLEO_WBA65RI || CONFIG_BOARD_STM32WBA65I_DK1
"modules/trusted-firmware-m/nordic/nrf9160" if CONFIG_SOC_NRF9160
"modules/trusted-firmware-m/nordic/nrf9120" if CONFIG_SOC_NRF9120
"modules/trusted-firmware-m/nordic/nrf5340_cpuapp" if CONFIG_SOC_NRF5340_CPUAPP
"modules/trusted-firmware-m/nordic/nrf54l15_cpuapp" if CONFIG_SOC_NRF54L15_CPUAPP
"modules/trusted-firmware-m/nordic/nrf54l10_cpuapp" if CONFIG_SOC_NRF54L10_CPUAPP
"modules/trusted-firmware-m/nordic/nrf54lm20a_cpuapp" if CONFIG_SOC_NRF54LM20A_CPUAPP
"modules/trusted-firmware-m/nordic/nrf7120_cpuapp" if CONFIG_SOC_NRF7120_ENGA_CPUAPP
"modules/trusted-firmware-m/nordic/nrf7120e_cpuapp" if CONFIG_SOC_NRF7120E_ENGA_CPUAPP
"modules/trusted-firmware-m/nordic/nrf54lm20b_cpuapp" if CONFIG_SOC_NRF54LM20B_CPUAPP
"modules/trusted-firmware-m/nordic/nrf54lv10a_cpuapp" if CONFIG_SOC_NRF54LV10A_CPUAPP
```

> 译注：本字段中由上游构建环境展开的路径已改为相对表示，起点为Zephyr 源码根目录。仅去除构建机目录前缀，路径其余部分、宏引用和条件保持原样；实际配置值仍由原构建系统解析。

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_V2M_MUSCA_B1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_V2M_MUSCA_B1)、[`CONFIG_BOARD_V2M_MUSCA_S1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_V2M_MUSCA_S1)、[`CONFIG_BOARD_B_U585I_IOT02A`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_B_U585I_IOT02A)、[`CONFIG_BOARD_NUCLEO_L552ZE_Q`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NUCLEO_L552ZE_Q)、[`CONFIG_BOARD_NUCLEO_U3C5ZI_Q`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NUCLEO_U3C5ZI_Q)、[`CONFIG_BOARD_STM32H573I_DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_STM32H573I_DK)、[`CONFIG_BOARD_STM32L562E_DK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_STM32L562E_DK)、[`CONFIG_BOARD_NUCLEO_WBA65RI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_NUCLEO_WBA65RI)、[`CONFIG_BOARD_STM32WBA65I_DK1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BOARD_STM32WBA65I_DK1)、[`CONFIG_SOC_NRF9160`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9160)、[`CONFIG_SOC_NRF9120`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF9120)、[`CONFIG_SOC_NRF5340_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF5340_CPUAPP)、[`CONFIG_SOC_NRF54L15_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L15_CPUAPP)、[`CONFIG_SOC_NRF54L10_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L10_CPUAPP)、[`CONFIG_SOC_NRF54LM20A_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54LM20A_CPUAPP)、[`CONFIG_SOC_NRF7120_ENGA_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF7120_ENGA_CPUAPP)、[`CONFIG_SOC_NRF7120E_ENGA_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF7120E_ENGA_CPUAPP)、[`CONFIG_SOC_NRF54LM20B_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54LM20B_CPUAPP)、[`CONFIG_SOC_NRF54LV10A_CPUAPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54LV10A_CPUAPP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BOARD_V2M_MUSCA_B1`、`CONFIG_BOARD_V2M_MUSCA_S1`、`CONFIG_BOARD_B_U585I_IOT02A`、`CONFIG_BOARD_NUCLEO_L552ZE_Q`、`CONFIG_BOARD_NUCLEO_U3C5ZI_Q`、`CONFIG_BOARD_STM32H573I_DK`、`CONFIG_BOARD_STM32L562E_DK`、`CONFIG_BOARD_NUCLEO_WBA65RI`、`CONFIG_BOARD_STM32WBA65I_DK1`、`CONFIG_SOC_NRF9160`、`CONFIG_SOC_NRF9120`、`CONFIG_SOC_NRF5340_CPUAPP`。

<a id="CONFIG_TFM_CMAKE_BUILD_TYPE"></a>

## 252.14 `CONFIG_TFM_CMAKE_BUILD_TYPE`

**提示（Prompt）**：TFM 的构建类型（build type）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
CONFIG_TFM_CMAKE_BUILD_TYPE_RELEASE if CONFIG_SPEED_OPTIMIZATIONS && CONFIG_BUILD_OUTPUT_STRIPPED
CONFIG_TFM_CMAKE_BUILD_TYPE_MINSIZEREL if CONFIG_SIZE_OPTIMIZATIONS || CONFIG_SIZE_OPTIMIZATIONS_AGGRESSIVE
CONFIG_TFM_CMAKE_BUILD_TYPE_DEBUG if CONFIG_DEBUG_OPTIMIZATIONS
CONFIG_TFM_CMAKE_BUILD_TYPE_RELWITHDEBINFO
```

**可选项（Choices）**

```text
CONFIG_TFM_CMAKE_BUILD_TYPE_RELEASE
CONFIG_TFM_CMAKE_BUILD_TYPE_RELWITHDEBINFO
CONFIG_TFM_CMAKE_BUILD_TYPE_MINSIZEREL
CONFIG_TFM_CMAKE_BUILD_TYPE_DEBUG
CONFIG_TFM_CMAKE_BUILD_TYPE_RELEASE
CONFIG_TFM_CMAKE_BUILD_TYPE_RELWITHDEBINFO
CONFIG_TFM_CMAKE_BUILD_TYPE_MINSIZEREL
CONFIG_TFM_CMAKE_BUILD_TYPE_DEBUG
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_CMAKE_BUILD_TYPE_RELEASE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_CMAKE_BUILD_TYPE_RELEASE)、[`CONFIG_SPEED_OPTIMIZATIONS`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_SPEED_OPTIMIZATIONS)、[`CONFIG_BUILD_OUTPUT_STRIPPED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BUILD_OUTPUT_STRIPPED)、[`CONFIG_TFM_CMAKE_BUILD_TYPE_MINSIZEREL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_CMAKE_BUILD_TYPE_MINSIZEREL)、[`CONFIG_SIZE_OPTIMIZATIONS`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_SIZE_OPTIMIZATIONS)、[`CONFIG_SIZE_OPTIMIZATIONS_AGGRESSIVE`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_SIZE_OPTIMIZATIONS_AGGRESSIVE)、[`CONFIG_TFM_CMAKE_BUILD_TYPE_DEBUG`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_CMAKE_BUILD_TYPE_DEBUG)、[`CONFIG_DEBUG_OPTIMIZATIONS`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEBUG_OPTIMIZATIONS)、[`CONFIG_TFM_CMAKE_BUILD_TYPE_RELWITHDEBINFO`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_CMAKE_BUILD_TYPE_RELWITHDEBINFO)。

<a id="CONFIG_TFM_CMAKE_BUILD_TYPE_DEBUG"></a>

## 252.15 `CONFIG_TFM_CMAKE_BUILD_TYPE_DEBUG`

**提示（Prompt）**：调试构建（Debug build）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_CMAKE_BUILD_TYPE>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → TFM 的构建类型（build type）

**配置项引用（Symbol References）**：[`CONFIG_TFM_CMAKE_BUILD_TYPE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_CMAKE_BUILD_TYPE)。

<a id="CONFIG_TFM_CMAKE_BUILD_TYPE_MINSIZEREL"></a>

## 252.16 `CONFIG_TFM_CMAKE_BUILD_TYPE_MINSIZEREL`

**提示（Prompt）**：为大小优化的发布构建（Release build, optimized for size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_CMAKE_BUILD_TYPE>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → TFM 的构建类型（build type）

**配置项引用（Symbol References）**：[`CONFIG_TFM_CMAKE_BUILD_TYPE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_CMAKE_BUILD_TYPE)。

<a id="CONFIG_TFM_CMAKE_BUILD_TYPE_RELEASE"></a>

## 252.17 `CONFIG_TFM_CMAKE_BUILD_TYPE_RELEASE`

**提示（Prompt）**：发布构建（Release build）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_CMAKE_BUILD_TYPE>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → TFM 的构建类型（build type）

**配置项引用（Symbol References）**：[`CONFIG_TFM_CMAKE_BUILD_TYPE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_CMAKE_BUILD_TYPE)。

<a id="CONFIG_TFM_CMAKE_BUILD_TYPE_RELWITHDEBINFO"></a>

## 252.18 `CONFIG_TFM_CMAKE_BUILD_TYPE_RELWITHDEBINFO`

**提示（Prompt）**：带调试信息的发布构建（Release build with Debug info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_CMAKE_BUILD_TYPE>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → TFM 的构建类型（build type）

**配置项引用（Symbol References）**：[`CONFIG_TFM_CMAKE_BUILD_TYPE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_CMAKE_BUILD_TYPE)。

<a id="CONFIG_TFM_CONNECTION_BASED_SERVICE_API"></a>

## 252.19 `CONFIG_TFM_CONNECTION_BASED_SERVICE_API`

**提示（Prompt）**：TF-M 使用基于连接的服务 API（connection based service APIs）

**说明（Help）**

TF-M 构建系统会生成用于访问基于连接的服务（connection based service）的接口源文件。当 TF-M 服务模型需要该源文件时，选择此选项。注意：这是 TF-M 构建系统自动生成的配置。如果 TF-M 构建系统未启用此选项，就会导致编译错误。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:297`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L297)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_CRYPTO_AEAD_MODULE_ENABLED"></a>

## 252.20 `CONFIG_TFM_CRYPTO_AEAD_MODULE_ENABLED`

**提示（Prompt）**：带关联数据的认证加密模块（AEAD crypto module）

**说明（Help）**

在加密分区（crypto partition）中启用带关联数据的认证加密模块（AEAD）。如果不使用 `crypto_aead.c` 提供的功能，请取消此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_PARTITION_CRYPTO && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.crypto:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.crypto#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_CRYPTO`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_CRYPTO)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_CRYPTO_ASYM_ENCRYPT_MODULE_ENABLED"></a>

## 252.21 `CONFIG_TFM_CRYPTO_ASYM_ENCRYPT_MODULE_ENABLED`

**提示（Prompt）**：非对称加密模块（ASYM ENCRYPT crypto module）

**说明（Help）**

在加密分区（crypto partition）中启用非对称加密模块（ASYM ENCRYPT）。如果不使用 `crypto_asymmetric.c` 提供的加密功能，请取消此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_PARTITION_CRYPTO && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.crypto:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.crypto#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_CRYPTO`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_CRYPTO)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_CRYPTO_ASYM_SIGN_MODULE_ENABLED"></a>

## 252.22 `CONFIG_TFM_CRYPTO_ASYM_SIGN_MODULE_ENABLED`

**提示（Prompt）**：非对称签名模块（ASYM SIGN crypto module）

**说明（Help）**

在加密分区（crypto partition）中启用非对称签名模块（ASYM SIGN）。如果不使用 `crypto_asymmetric.c` 提供的签名功能，请取消此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_PARTITION_CRYPTO && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.crypto:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.crypto#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_CRYPTO`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_CRYPTO)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_CRYPTO_CIPHER_MODULE_ENABLED"></a>

## 252.23 `CONFIG_TFM_CRYPTO_CIPHER_MODULE_ENABLED`

**提示（Prompt）**：密码运算模块（CIPHER crypto module）

**说明（Help）**

在加密分区（crypto partition）中启用密码运算模块（CIPHER）。如果不使用 `crypto_cipher.c` 提供的功能，请取消此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_PARTITION_CRYPTO && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.crypto:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.crypto#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_CRYPTO`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_CRYPTO)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_CRYPTO_HASH_MODULE_ENABLED"></a>

## 252.24 `CONFIG_TFM_CRYPTO_HASH_MODULE_ENABLED`

**提示（Prompt）**：哈希加密模块（HASH crypto module）

**说明（Help）**

在加密分区（crypto partition）中启用哈希模块（HASH）。如果不使用 `crypto_hash.c` 提供的功能，请取消此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_PARTITION_CRYPTO && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.crypto:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.crypto#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_CRYPTO`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_CRYPTO)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_CRYPTO_KEY_DERIVATION_MODULE_ENABLED"></a>

## 252.25 `CONFIG_TFM_CRYPTO_KEY_DERIVATION_MODULE_ENABLED`

**提示（Prompt）**：密钥派生加密模块（KEY DERIVATION crypto module）

**说明（Help）**

在加密分区（crypto partition）中启用密钥派生模块（KEY_DERIVATION）。如果不使用 `crypto_key_derivation.c` 提供的功能，请取消此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_PARTITION_CRYPTO && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.crypto:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.crypto#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_CRYPTO`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_CRYPTO)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_CRYPTO_KEY_MODULE_ENABLED"></a>

## 252.26 `CONFIG_TFM_CRYPTO_KEY_MODULE_ENABLED`

**提示（Prompt）**：密钥加密模块（KEY crypto module）

**说明（Help）**

在加密分区（crypto partition）中启用密钥模块（KEY）。如果不使用 `crypto_key_management.c` 提供的功能，请取消此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_PARTITION_CRYPTO && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.crypto:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.crypto#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_CRYPTO`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_CRYPTO)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_CRYPTO_MAC_MODULE_ENABLED"></a>

## 252.27 `CONFIG_TFM_CRYPTO_MAC_MODULE_ENABLED`

**提示（Prompt）**：消息认证码加密模块（MAC crypto module）

**说明（Help）**

在加密分区（crypto partition）中启用消息认证码模块（MAC）。如果不使用 `crypto_mac.c` 提供的功能，请取消此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_PARTITION_CRYPTO && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.crypto:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.crypto#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_CRYPTO`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_CRYPTO)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_CRYPTO_RNG_MODULE_ENABLED"></a>

## 252.28 `CONFIG_TFM_CRYPTO_RNG_MODULE_ENABLED`

**提示（Prompt）**：随机数生成器加密模块（Random number generator crypto module）

**说明（Help）**

在加密分区（crypto partition）中启用随机数生成器模块（random number generator）。如果不使用 `psa_generate_random`，请取消此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_PARTITION_CRYPTO && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.crypto:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.crypto#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_CRYPTO`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_CRYPTO)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_DUMMY_PROVISIONING"></a>

## 252.29 `CONFIG_TFM_DUMMY_PROVISIONING`

**提示（Prompt）**：使用虚拟值进行预配，不得用于生产（Provision with dummy values）

**说明（Help）**

启用此选项时（默认启用），会预配一组虚拟密钥／数据（dummy keys / data）。虚拟初始证明密钥（IAK）与 TF-M 测试所检查的 IAK 匹配，虚拟 bl2 根信任公钥（ROTPK）与默认使用的虚拟 bl2 密钥匹配。由于这些密钥不安全，此选项绝对不得用于生产硬件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_TFM_INITIAL_ATTESTATION_KEY
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:195`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L195)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_INITIAL_ATTESTATION_KEY`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_INITIAL_ATTESTATION_KEY)。

<a id="CONFIG_TFM_EXCEPTION_INFO_DUMP"></a>

## 252.30 `CONFIG_TFM_EXCEPTION_INFO_DUMP`

**提示（Prompt）**：TF-M 异常信息转储（exception info dump）

**说明（Help）**

安全固件发生致命错误（fatal error）时，捕获有关异常（exception）的信息。如果安全分区管理器（SPM）的日志级别允许，则打印这些信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:596`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L596)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_FLASH_MERGED_BINARY"></a>

## 252.31 `CONFIG_TFM_FLASH_MERGED_BINARY`

原库同名定义共 2 条；本项为数据库第 18923 条记录，各定义分别保留。

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此选项指示 `west flash` 烧录组合后的二进制文件（combined / merged binary）。它包含 TF-M 安全固件镜像、可选的 BL2 镜像（启用了 `TFM_BL2` 构建时），以及非安全应用固件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:559`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L559)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_IMAGE_SECURITY_COUNTER"></a>

## 252.32 `CONFIG_TFM_IMAGE_SECURITY_COUNTER`

**提示（Prompt）**：用于硬件回滚保护的安全计数器值（security counter value）

**说明（Help）**

TFM 默认启用硬件回滚保护（hardware rollback protection），这要求在镜像尾部（image trailer）嵌入安全计数器（security counter）。根据 `mcuboot/docs/design.md` 中的“基于硬件的降级防护”（Hardware-based downgrade prevention）说明，并不需要在每次固件更新时都递增此值；但只有递增此值时，硬件回滚保护才会生效。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_BL2 && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 1024]
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:322`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L322)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_BL2`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_IMAGE_VERSION_NS"></a>

## 252.33 `CONFIG_TFM_IMAGE_VERSION_NS`

**提示（Prompt）**：非安全镜像版本（Version of the Non-Secure Image）

**说明（Help）**

非安全镜像（non-secure image）的版本。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
"" if "" != "" && CONFIG_TFM_MCUBOOT_IMAGE_NUMBER = 2
"0.0.0+0"
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:228`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L228)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_MCUBOOT_IMAGE_NUMBER`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_MCUBOOT_IMAGE_NUMBER)。

<a id="CONFIG_TFM_IMAGE_VERSION_S"></a>

## 252.34 `CONFIG_TFM_IMAGE_VERSION_S`

**提示（Prompt）**：安全镜像版本（Version of the Secure Image）

**说明（Help）**

安全镜像（secure image）的版本。对于合并安全与非安全镜像的构建（`TFM_MCUBOOT_IMAGE_NUMBER == 1`），也使用此版本。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
"" if "" != "" && CONFIG_TFM_MCUBOOT_IMAGE_NUMBER = 1
"0.0.0+0"
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:220`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L220)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_MCUBOOT_IMAGE_NUMBER`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_MCUBOOT_IMAGE_NUMBER)。

<a id="CONFIG_TFM_INITIAL_ATTESTATION_KEY"></a>

## 252.35 `CONFIG_TFM_INITIAL_ATTESTATION_KEY`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，表示 TF-M 平台具有初始证明密钥（initial attestation key）；这是初始证明分区（Initial Attestation partition）的必要条件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**被选择（Selected by）**

```text
CONFIG_TFM_DUMMY_PROVISIONING
CONFIG_TFM_DUMMY_PROVISIONING
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:207`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L207)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_DUMMY_PROVISIONING`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_DUMMY_PROVISIONING)。

<a id="CONFIG_TFM_INSTALL_TF_PSA_CRYPTO_HEADERS"></a>

## 252.36 `CONFIG_TFM_INSTALL_TF_PSA_CRYPTO_HEADERS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏符号，表示 Zephyr 镜像使用的 TF-PSA-Crypto 头文件（`psa/crypto.h` 及相关文件）由 TF-M 安装，并与其配套的 TF-PSA-Crypto 配置头文件一同使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_PARTITION_CRYPTO && !CONFIG_MBEDTLS && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:288`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L288)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_CRYPTO`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_CRYPTO)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_IPC"></a>

## 252.37 `CONFIG_TFM_IPC`

**提示（Prompt）**：进程间通信模型（IPC Model）

**说明（Help）**

使用进程间通信模型（IPC Model）作为 PSA API 的安全分区管理器（SPM）后端。IPC 模型支持 IPC 和安全函数（SFN）分区模型，以及隔离级别 1、2、3。此模型中，每个安全分区（Secure Partition）可以按任意顺序处理信号，并可在继续处理其他信号的同时延后响应某条消息。IPC 模型符合面向 M 的 PSA 固件框架（PSA Firmware Framework for M，FF-M）v1.1。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_MODEL>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:466`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L466)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → TF-M 固件框架模型（Firmware Framework model）

**配置项引用（Symbol References）**：[`CONFIG_TFM_MODEL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_MODEL)。

<a id="CONFIG_TFM_ISOLATION_LEVEL"></a>

## 252.38 `CONFIG_TFM_ISOLATION_LEVEL`

**提示（Prompt）**：隔离级别设置（Isolation level setting）

**说明（Help）**

手动设置所需的 TFM 隔离级别（isolation level）。可选值为 1、2、3；默认值由构建配置设置。提供 TF-M 配置档（Profile）选项时，不允许手动设置隔离级别，因为它由配置档决定。由于隔离级别 2 和 3 需要 PSA_API（`TFM_IPC`）支持，因此未启用 `TFM_IPC` 时强制使用级别 1。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
1 if CONFIG_TFM_PROFILE_TYPE_SMALL || !CONFIG_TFM_IPC
2 if CONFIG_TFM_PROFILE_TYPE_MEDIUM
3 if CONFIG_TFM_PROFILE_TYPE_LARGE
```

**取值范围（Ranges）**

```text
[1, 3]
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_PROFILE_TYPE_SMALL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PROFILE_TYPE_SMALL)、[`CONFIG_TFM_IPC`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_IPC)、[`CONFIG_TFM_PROFILE_TYPE_MEDIUM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PROFILE_TYPE_MEDIUM)、[`CONFIG_TFM_PROFILE_TYPE_LARGE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PROFILE_TYPE_LARGE)。

<a id="CONFIG_TFM_ITS_MAX_ASSET_SIZE"></a>

## 252.39 `CONFIG_TFM_ITS_MAX_ASSET_SIZE`

**提示（Prompt）**：内部可信存储资产的最大大小（Maximum Internal Trusted Storage asset size）

**说明（Help）**

存入内部可信存储（Internal Trusted Storage，ITS）的单个资产（asset）的最大大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_ITS_MAX_ASSET_SIZE_OVERRIDE && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L178)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → 覆盖内部可信存储资产的最大大小（Override maximum asset size）

**配置项引用（Symbol References）**：[`CONFIG_TFM_ITS_MAX_ASSET_SIZE_OVERRIDE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_ITS_MAX_ASSET_SIZE_OVERRIDE)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_ITS_MAX_ASSET_SIZE_OVERRIDE"></a>

## 252.40 `CONFIG_TFM_ITS_MAX_ASSET_SIZE_OVERRIDE`

**提示（Prompt）**：覆盖内部可信存储资产的最大大小（Override maximum asset size）

**说明（Help）**

使用 `TFM_ITS_MAX_ASSET_SIZE` 覆盖平台默认的内部可信存储（Internal Trusted Storage，ITS）单个资产最大大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_ITS_NUM_ASSETS"></a>

## 252.41 `CONFIG_TFM_ITS_NUM_ASSETS`

**提示（Prompt）**：内部可信存储资产的最大数量（Maximum number of Internal Trusted Storage assets）

**说明（Help）**

存入内部可信存储（Internal Trusted Storage，ITS）的资产（asset）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_ITS_NUM_ASSETS_OVERRIDE && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:165`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L165)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → 覆盖内部可信存储资产的最大数量（Override maximum number of assets）

**配置项引用（Symbol References）**：[`CONFIG_TFM_ITS_NUM_ASSETS_OVERRIDE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_ITS_NUM_ASSETS_OVERRIDE)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_ITS_NUM_ASSETS_OVERRIDE"></a>

## 252.42 `CONFIG_TFM_ITS_NUM_ASSETS_OVERRIDE`

**提示（Prompt）**：覆盖内部可信存储资产的最大数量（Override maximum number of assets）

**说明（Help）**

使用 `TFM_ITS_NUM_ASSETS` 覆盖平台默认的内部可信存储（Internal Trusted Storage，ITS）资产最大数量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:159`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L159)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_KEY_FILE_NS"></a>

## 252.43 `CONFIG_TFM_KEY_FILE_NS`

**提示（Prompt）**：用于签署非安全固件镜像的私钥路径（private key path）

**说明（Help）**

包含私钥的 `.pem` 文件的路径和文件名；BL2 引导加载程序（bootloader）签署非安全固件镜像时应使用该私钥。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_BL2 && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
"modules/tee/tf-m/trusted-firmware-m/bl2/ext/mcuboot/root-${CONFIG_TFM_MCUBOOT_SIGNATURE_TYPE}_1.pem"
```

> 译注：本字段中由上游构建环境展开的路径已改为相对表示，起点为west 工作区顶层目录。仅去除构建机目录前缀，路径其余部分、宏引用和条件保持原样；实际配置值仍由原构建系统解析。

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:347`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L347)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_BL2`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_KEY_FILE_S"></a>

## 252.44 `CONFIG_TFM_KEY_FILE_S`

**提示（Prompt）**：用于签署安全固件镜像的私钥路径（private key path）

**说明（Help）**

包含私钥的 `.pem` 文件的路径和文件名；BL2 引导加载程序（bootloader）签署安全固件镜像时应使用该私钥。合并安全与非安全镜像的构建（`TFM_MCUBOOT_IMAGE_NUMBER == 1`）也使用此密钥文件。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_BL2 && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
"modules/tee/tf-m/trusted-firmware-m/bl2/ext/mcuboot/root-${CONFIG_TFM_MCUBOOT_SIGNATURE_TYPE}.pem"
```

> 译注：本字段中由上游构建环境展开的路径已改为相对表示，起点为west 工作区顶层目录。仅去除构建机目录前缀，路径其余部分、宏引用和条件保持原样；实际配置值仍由原构建系统解析。

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:338`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L338)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_BL2`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_LOG_LEVEL_SILENCE"></a>

## 252.45 `CONFIG_TFM_LOG_LEVEL_SILENCE`

原库同名定义共 2 条；本项为数据库第 18938 条记录，各定义分别保留。

**提示（Prompt）**：TF-M 禁用安全侧日志（Disable secure logging）

**说明（Help）**

将所有 TF-M 模块（SPM、分区等）的日志级别设为静默（silence）。在某些平台上，这会从安全域（secure domain）释放 UART，并减少 UART 驱动占用的 Flash 空间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:567`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L567)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_MCUBOOT_DATA_SHARING"></a>

## 252.46 `CONFIG_TFM_MCUBOOT_DATA_SHARING`

**提示（Prompt）**：在 TF-M 与 MCUBoot 之间共享应用专用数据（app-specific data）

**说明（Help）**

添加应用专用数据共享，使用与度量启动（measured boot）相同的共享数据区域（shared data area）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_BL2 && CONFIG_BUILD_WITH_TFM
```

**被选择（Selected by）**

```text
CONFIG_TFM_PARTITION_FIRMWARE_UPDATE
CONFIG_TFM_PARTITION_FIRMWARE_UPDATE
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:450`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L450)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_BL2`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_PARTITION_FIRMWARE_UPDATE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_FIRMWARE_UPDATE)。

<a id="CONFIG_TFM_MCUBOOT_ENCRYPTION"></a>

## 252.47 `CONFIG_TFM_MCUBOOT_ENCRYPTION`

**提示（Prompt）**：BL2 中的镜像加密（Image encryption in BL2）

**说明（Help）**

在 MCUboot（BL2）中启用加密镜像支持（encrypted images），对应 TF-M 的 `MCUBOOT_ENC_IMAGES` 选项。只有更新镜像（`*_signed_encrypted.bin`）会被加密。BL2 在将镜像从次槽位（secondary slot）移动到主槽位（primary slot）时解密，因此烧录到主槽位的镜像保持未加密状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_BL2 && CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:369`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L369)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_BL2`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_MCUBOOT_ENCRYPTION_KEY_FILE"></a>

## 252.48 `CONFIG_TFM_MCUBOOT_ENCRYPTION_KEY_FILE`

**提示（Prompt）**：用于加密固件镜像的私钥路径（private key path）

**说明（Help）**

用于加密安全与非安全固件镜像的密钥文件路径和文件名。对于 RSA-OAEP，此文件是 RSA 私钥：它嵌入 BL2 中，用于解封装 AES 密钥；加密镜像时则使用对应公钥封装该 AES 密钥。此项对应 TF-M 的 `MCUBOOT_KEY_ENC` 选项。默认值是公开已知的 MCUboot 测试密钥，不提供保密性（confidentiality）。生产环境应使用自己的私钥。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_MCUBOOT_ENCRYPTION && CONFIG_TFM_BL2 && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
"bootloader/mcuboot/enc-rsa2048-priv.pem" if CONFIG_TFM_MCUBOOT_ENCRYPTION_RSA_OAEP
```

> 译注：本字段中由上游构建环境展开的路径已改为相对表示，起点为west 工作区顶层目录。仅去除构建机目录前缀，路径其余部分、宏引用和条件保持原样；实际配置值仍由原构建系统解析。

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:404`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L404)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → BL2 中的镜像加密（Image encryption in BL2）

**配置项引用（Symbol References）**：[`CONFIG_TFM_MCUBOOT_ENCRYPTION`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_MCUBOOT_ENCRYPTION)、[`CONFIG_TFM_BL2`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_MCUBOOT_ENCRYPTION_RSA_OAEP`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_MCUBOOT_ENCRYPTION_RSA_OAEP)。

<a id="CONFIG_TFM_MCUBOOT_ENCRYPTION_KEY_LEN"></a>

## 252.49 `CONFIG_TFM_MCUBOOT_ENCRYPTION_KEY_LEN`

**提示（Prompt）**：镜像加密 AES 密钥长度（Image encryption AES key length）

**说明（Help）**

用于加密镜像载荷（image payload）的 AES 密钥长度，单位为位。有效值为 128 和 256，对应 TF-M 的 `MCUBOOT_ENC_KEY_LEN` 选项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_MCUBOOT_ENCRYPTION && CONFIG_TFM_BL2 && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:396`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L396)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → BL2 中的镜像加密（Image encryption in BL2）

**配置项引用（Symbol References）**：[`CONFIG_TFM_MCUBOOT_ENCRYPTION`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_MCUBOOT_ENCRYPTION)、[`CONFIG_TFM_BL2`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_MCUBOOT_ENCRYPTION_KEY_WRAP_SCHEME"></a>

## 252.50 `CONFIG_TFM_MCUBOOT_ENCRYPTION_KEY_WRAP_SCHEME`

**提示（Prompt）**：镜像加密密钥封装方案（Image encryption key-wrapping scheme）

**说明（Help）**

选择用于封装每个镜像 AES 密钥的算法（key-wrapping algorithm）；该密钥存储在镜像的类型－长度－值区域（TLV area）中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_MCUBOOT_ENCRYPTION && CONFIG_TFM_BL2 && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
CONFIG_TFM_MCUBOOT_ENCRYPTION_RSA_OAEP
```

**可选项（Choices）**

```text
CONFIG_TFM_MCUBOOT_ENCRYPTION_RSA_OAEP
CONFIG_TFM_MCUBOOT_ENCRYPTION_RSA_OAEP
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:381`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L381)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → BL2 中的镜像加密（Image encryption in BL2）

**配置项引用（Symbol References）**：[`CONFIG_TFM_MCUBOOT_ENCRYPTION`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_MCUBOOT_ENCRYPTION)、[`CONFIG_TFM_BL2`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_MCUBOOT_ENCRYPTION_RSA_OAEP`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_MCUBOOT_ENCRYPTION_RSA_OAEP)。

<a id="CONFIG_TFM_MCUBOOT_ENCRYPTION_RSA_OAEP"></a>

## 252.51 `CONFIG_TFM_MCUBOOT_ENCRYPTION_RSA_OAEP`

**提示（Prompt）**：RSA 最优非对称加密填充（RSA-OAEP）

**说明（Help）**

使用 RSA-OAEP 封装 AES 密钥，对应 TF-M 的 `MCUBOOT_ENCRYPT_RSA` 选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_MCUBOOT_ENCRYPTION_KEY_WRAP_SCHEME>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:388`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L388)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → BL2 中的镜像加密（Image encryption in BL2） → 镜像加密密钥封装方案（Image encryption key-wrapping scheme）

**配置项引用（Symbol References）**：[`CONFIG_TFM_MCUBOOT_ENCRYPTION_KEY_WRAP_SCHEME`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_MCUBOOT_ENCRYPTION_KEY_WRAP_SCHEME)。

<a id="CONFIG_TFM_MCUBOOT_IMAGE_NUMBER"></a>

## 252.52 `CONFIG_TFM_MCUBOOT_IMAGE_NUMBER`

**提示（Prompt）**：TFM 与应用的固件更新粒度（Granularity of FW updates）

**说明（Help）**

引导加载程序（bootloader）查看 TFM 和应用时将其视为几个镜像。此值为 1 时，安全侧（S）与非安全侧（NS）视为一个镜像，必须在一次原子操作（atomic operation）中更新。此值为 2 时，两者分开，在满足依赖要求时可以独立更新。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_BL2 && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 2]
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:419`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L419)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_BL2`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_MCUBOOT_SIGNATURE_TYPE"></a>

## 252.53 `CONFIG_TFM_MCUBOOT_SIGNATURE_TYPE`

**提示（Prompt）**：用于签署安全与非安全固件镜像的签名类型（signature type）

**说明（Help）**

可选类型为 RSA-2048、RSA-3072、EC-P256、EC-P384。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_BL2 && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
"EC-P256"
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:332`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L332)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_BL2`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_MODEL"></a>

## 252.54 `CONFIG_TFM_MODEL`

**提示（Prompt）**：TF-M 固件框架模型（Firmware Framework model）

**说明（Help）**

面向 M 的固件框架（Firmware Framework M，FF-M）为安全分区（Secure Partition）提供不同的编程模型（programming model）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
CONFIG_TFM_SFN if CONFIG_TFM_PROFILE_TYPE_SMALL
CONFIG_TFM_IPC
```

**可选项（Choices）**

```text
CONFIG_TFM_IPC
CONFIG_TFM_SFN
CONFIG_TFM_IPC
CONFIG_TFM_SFN
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:458`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L458)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_SFN`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_SFN)、[`CONFIG_TFM_PROFILE_TYPE_SMALL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PROFILE_TYPE_SMALL)、[`CONFIG_TFM_IPC`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_IPC)。

<a id="CONFIG_TFM_PARTITION_CRYPTO"></a>

## 252.55 `CONFIG_TFM_PARTITION_CRYPTO`

**提示（Prompt）**：安全分区“加密”（Secure partition 'Crypto'）

**说明（Help）**

设置此选项会将 `-DTFM_PARTITION_CRYPTO` 传给 TF-M 构建系统。关于此参数的详细信息，请查看 trusted-firmware-m 仓库中的 `config_default.cmake`。各个 `TFM_PARTITION_*` 选项之间的依赖均由该仓库中的构建系统处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_PSA_CRYPTO_PROVIDER_TFM
CONFIG_PSA_CRYPTO_PROVIDER_TFM
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.partitions:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.partitions#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_PSA_CRYPTO_PROVIDER_TFM`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO_PROVIDER_TFM)。

<a id="CONFIG_TFM_PARTITION_FIRMWARE_UPDATE"></a>

## 252.56 `CONFIG_TFM_PARTITION_FIRMWARE_UPDATE`

**提示（Prompt）**：包含安全分区“固件更新”（Firmware Update）

**说明（Help）**

设置此选项会将 `-DTFM_PARTITION_FIRMWARE_UPDATE` 传给 TF-M 构建系统。关于此参数的详细信息，请查看 trusted-firmware-m 仓库中的 `config_default.cmake`。各个 `TFM_PARTITION_*` 选项之间的依赖均由该仓库中的构建系统处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_PARTITION_FIRMWARE_UPDATE_SUPPORTED && CONFIG_BUILD_WITH_TFM
```

**主动选择（Selects）**

```text
CONFIG_TFM_MCUBOOT_DATA_SHARING
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.partitions:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.partitions#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_FIRMWARE_UPDATE_SUPPORTED`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_FIRMWARE_UPDATE_SUPPORTED)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_MCUBOOT_DATA_SHARING`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_MCUBOOT_DATA_SHARING)。

<a id="CONFIG_TFM_PARTITION_FIRMWARE_UPDATE_SUPPORTED"></a>

## 252.57 `CONFIG_TFM_PARTITION_FIRMWARE_UPDATE_SUPPORTED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示开发板支持固件更新分区（Firmware Update partition）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.partitions:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.partitions#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_PARTITION_INITIAL_ATTESTATION"></a>

## 252.58 `CONFIG_TFM_PARTITION_INITIAL_ATTESTATION`

**提示（Prompt）**：安全分区“初始证明”（Secure partition 'Initial Attestation'）

**说明（Help）**

设置此选项会将 `-DTFM_PARTITION_INITIAL_ATTESTATION` 传给 TF-M 构建系统。关于此参数的详细信息，请查看 trusted-firmware-m 仓库中的 `config_default.cmake`。各个 `TFM_PARTITION_*` 选项之间的依赖均由该仓库中的构建系统处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_PARTITION_CRYPTO && CONFIG_TFM_INITIAL_ATTESTATION_KEY && CONFIG_BUILD_WITH_TFM
```

**被选择（Selected by）**

```text
CONFIG_TFM_PSA_TEST_INITIAL_ATTESTATION
CONFIG_TFM_PSA_TEST_INITIAL_ATTESTATION
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.partitions:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.partitions#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → 安全分区“加密”（Secure partition 'Crypto'）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_CRYPTO`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_CRYPTO)、[`CONFIG_TFM_INITIAL_ATTESTATION_KEY`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_INITIAL_ATTESTATION_KEY)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_PSA_TEST_INITIAL_ATTESTATION`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PSA_TEST_INITIAL_ATTESTATION)。

<a id="CONFIG_TFM_PARTITION_INTERNAL_TRUSTED_STORAGE"></a>

## 252.59 `CONFIG_TFM_PARTITION_INTERNAL_TRUSTED_STORAGE`

**提示（Prompt）**：安全分区“内部可信存储”（Secure partition 'Internal Trusted Storage'）

**说明（Help）**

设置此选项会将 `-DTFM_PARTITION_INTERNAL_TRUSTED_STORAGE` 传给 TF-M 构建系统。关于此参数的详细信息，请查看 trusted-firmware-m 仓库中的 `config_default.cmake`。各个 `TFM_PARTITION_*` 选项之间的依赖均由该仓库中的构建系统处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.partitions:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.partitions#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_PARTITION_LOG_LEVEL"></a>

## 252.60 `CONFIG_TFM_PARTITION_LOG_LEVEL`

**提示（Prompt）**：TF-M 分区日志级别（Partition Log Level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
CONFIG_TFM_PARTITION_LOG_LEVEL_INFO
```

**可选项（Choices）**

```text
CONFIG_TFM_PARTITION_LOG_LEVEL_DEBUG
CONFIG_TFM_PARTITION_LOG_LEVEL_INFO
CONFIG_TFM_PARTITION_LOG_LEVEL_ERROR
CONFIG_TFM_PARTITION_LOG_LEVEL_SILENCE
CONFIG_TFM_PARTITION_LOG_LEVEL_DEBUG
CONFIG_TFM_PARTITION_LOG_LEVEL_INFO
CONFIG_TFM_PARTITION_LOG_LEVEL_ERROR
CONFIG_TFM_PARTITION_LOG_LEVEL_SILENCE
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.partitions:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.partitions#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_PARTITION_LOG_LEVEL_INFO`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_LOG_LEVEL_INFO)、[`CONFIG_TFM_PARTITION_LOG_LEVEL_DEBUG`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_LOG_LEVEL_DEBUG)、[`CONFIG_TFM_PARTITION_LOG_LEVEL_ERROR`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_LOG_LEVEL_ERROR)、[`CONFIG_TFM_PARTITION_LOG_LEVEL_SILENCE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_LOG_LEVEL_SILENCE)。

<a id="CONFIG_TFM_PARTITION_LOG_LEVEL_DEBUG"></a>

## 252.61 `CONFIG_TFM_PARTITION_LOG_LEVEL_DEBUG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_PARTITION_LOG_LEVEL>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.partitions:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.partitions#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → TF-M 分区日志级别（Partition Log Level）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_LOG_LEVEL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_LOG_LEVEL)。

<a id="CONFIG_TFM_PARTITION_LOG_LEVEL_ERROR"></a>

## 252.62 `CONFIG_TFM_PARTITION_LOG_LEVEL_ERROR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_PARTITION_LOG_LEVEL>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.partitions:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.partitions#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → TF-M 分区日志级别（Partition Log Level）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_LOG_LEVEL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_LOG_LEVEL)。

<a id="CONFIG_TFM_PARTITION_LOG_LEVEL_INFO"></a>

## 252.63 `CONFIG_TFM_PARTITION_LOG_LEVEL_INFO`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_PARTITION_LOG_LEVEL>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.partitions:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.partitions#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → TF-M 分区日志级别（Partition Log Level）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_LOG_LEVEL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_LOG_LEVEL)。

<a id="CONFIG_TFM_PARTITION_LOG_LEVEL_SILENCE"></a>

## 252.64 `CONFIG_TFM_PARTITION_LOG_LEVEL_SILENCE`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_PARTITION_LOG_LEVEL>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.partitions:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.partitions#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → TF-M 分区日志级别（Partition Log Level）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_LOG_LEVEL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_LOG_LEVEL)。

<a id="CONFIG_TFM_PARTITION_PLATFORM"></a>

## 252.65 `CONFIG_TFM_PARTITION_PLATFORM`

**提示（Prompt）**：安全分区“平台”（Secure partition 'Platform'）

**说明（Help）**

设置此选项会将 `-DTFM_PARTITION_PLATFORM` 传给 TF-M 构建系统。关于此参数的详细信息，请查看 trusted-firmware-m 仓库中的 `config_default.cmake`。各个 `TFM_PARTITION_*` 选项之间的依赖均由该仓库中的构建系统处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.partitions:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.partitions#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_PARTITION_PLATFORM_CUSTOM_REBOOT"></a>

## 252.66 `CONFIG_TFM_PARTITION_PLATFORM_CUSTOM_REBOOT`

**提示（Prompt）**：使用自定义重启处理函数（custom reboot handler）

**说明（Help）**

不包含 Zephyr 默认的 TF-M 平台复位服务调用实现。应用必须改为覆盖 `sys_arch_reset()` 的 ARM 弱实现（weak implementation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_PARTITION_PLATFORM && CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:186`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L186)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_PLATFORM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_PLATFORM)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_PARTITION_PROTECTED_STORAGE"></a>

## 252.67 `CONFIG_TFM_PARTITION_PROTECTED_STORAGE`

**提示（Prompt）**：安全分区“受保护存储”（Secure partition 'Protected Storage'）

**说明（Help）**

设置此选项会将 `-DTFM_PARTITION_PROTECTED_STORAGE` 传给 TF-M 构建系统。关于此参数的详细信息，请查看 trusted-firmware-m 仓库中的 `config_default.cmake`。各个 `TFM_PARTITION_*` 选项之间的依赖均由该仓库中的构建系统处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_PARTITION_PLATFORM && CONFIG_TFM_PARTITION_INTERNAL_TRUSTED_STORAGE && CONFIG_TFM_PARTITION_CRYPTO && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.partitions:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.partitions#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_PLATFORM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_PLATFORM)、[`CONFIG_TFM_PARTITION_INTERNAL_TRUSTED_STORAGE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_INTERNAL_TRUSTED_STORAGE)、[`CONFIG_TFM_PARTITION_CRYPTO`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_CRYPTO)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_PLATFORM_HANDLES_MERGE"></a>

## 252.68 `CONFIG_TFM_PLATFORM_HANDLES_MERGE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

由自行对 TF-M 安全和非安全镜像进行后处理（例如额外签名）、并自行生成合并镜像的平台（SoC／开发板）选择；此类平台不依赖 TF-M 模块默认执行的安全／非安全镜像合并。这是没有提示文字（prompt）的内部符号，不供用户设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_PROFILE"></a>

## 252.69 `CONFIG_TFM_PROFILE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

构建 `tfm_s` 镜像使用的配置档（build profile）。可选值为 `profile_large`、`profile_medium`、`profile_small`。默认配置档不需要设置此配置。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
"profile_small" if CONFIG_TFM_PROFILE_TYPE_SMALL
"profile_medium" if CONFIG_TFM_PROFILE_TYPE_MEDIUM
"profile_medium_arotless" if CONFIG_TFM_PROFILE_TYPE_AROTLESS
"profile_large" if CONFIG_TFM_PROFILE_TYPE_LARGE
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_PROFILE_TYPE_SMALL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PROFILE_TYPE_SMALL)、[`CONFIG_TFM_PROFILE_TYPE_MEDIUM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PROFILE_TYPE_MEDIUM)、[`CONFIG_TFM_PROFILE_TYPE_AROTLESS`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PROFILE_TYPE_AROTLESS)、[`CONFIG_TFM_PROFILE_TYPE_LARGE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PROFILE_TYPE_LARGE)。

<a id="CONFIG_TFM_PROFILE_TYPE"></a>

## 252.70 `CONFIG_TFM_PROFILE_TYPE`

**提示（Prompt）**：TF-M 构建配置档（build profile）

**说明（Help）**

选择 TF-M 构建配置档（build profile）。可以为空（未设置）、small、medium 或 large。某些配置档类型会启用其他 TF-M 配置选项，即 IPC 模型和隔离级别（isolation level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
CONFIG_TFM_PROFILE_TYPE_NOT_SET
```

**可选项（Choices）**

```text
CONFIG_TFM_PROFILE_TYPE_NOT_SET
CONFIG_TFM_PROFILE_TYPE_SMALL
CONFIG_TFM_PROFILE_TYPE_MEDIUM
CONFIG_TFM_PROFILE_TYPE_AROTLESS
CONFIG_TFM_PROFILE_TYPE_LARGE
CONFIG_TFM_PROFILE_TYPE_NOT_SET
CONFIG_TFM_PROFILE_TYPE_SMALL
CONFIG_TFM_PROFILE_TYPE_MEDIUM
CONFIG_TFM_PROFILE_TYPE_AROTLESS
CONFIG_TFM_PROFILE_TYPE_LARGE
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_PROFILE_TYPE_NOT_SET`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PROFILE_TYPE_NOT_SET)、[`CONFIG_TFM_PROFILE_TYPE_SMALL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PROFILE_TYPE_SMALL)、[`CONFIG_TFM_PROFILE_TYPE_MEDIUM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PROFILE_TYPE_MEDIUM)、[`CONFIG_TFM_PROFILE_TYPE_AROTLESS`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PROFILE_TYPE_AROTLESS)、[`CONFIG_TFM_PROFILE_TYPE_LARGE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PROFILE_TYPE_LARGE)。

<a id="CONFIG_TFM_PROFILE_TYPE_AROTLESS"></a>

## 252.71 `CONFIG_TFM_PROFILE_TYPE_AROTLESS`

**提示（Prompt）**：TF-M 构建配置档：无应用信任根（ARoT-less）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_PROFILE_TYPE>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → TF-M 构建配置档（build profile）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PROFILE_TYPE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PROFILE_TYPE)。

<a id="CONFIG_TFM_PROFILE_TYPE_LARGE"></a>

## 252.72 `CONFIG_TFM_PROFILE_TYPE_LARGE`

**提示（Prompt）**：TF-M 构建配置档：大型（large）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_PROFILE_TYPE>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → TF-M 构建配置档（build profile）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PROFILE_TYPE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PROFILE_TYPE)。

<a id="CONFIG_TFM_PROFILE_TYPE_MEDIUM"></a>

## 252.73 `CONFIG_TFM_PROFILE_TYPE_MEDIUM`

**提示（Prompt）**：TF-M 构建配置档：中型（medium）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_PROFILE_TYPE>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → TF-M 构建配置档（build profile）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PROFILE_TYPE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PROFILE_TYPE)。

<a id="CONFIG_TFM_PROFILE_TYPE_NOT_SET"></a>

## 252.74 `CONFIG_TFM_PROFILE_TYPE_NOT_SET`

**提示（Prompt）**：TF-M 构建配置档：未设置，基础配置（not set, base）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_PROFILE_TYPE>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → TF-M 构建配置档（build profile）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PROFILE_TYPE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PROFILE_TYPE)。

<a id="CONFIG_TFM_PROFILE_TYPE_SMALL"></a>

## 252.75 `CONFIG_TFM_PROFILE_TYPE_SMALL`

**提示（Prompt）**：TF-M 构建配置档：小型（small）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_PROFILE_TYPE>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → TF-M 构建配置档（build profile）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PROFILE_TYPE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PROFILE_TYPE)。

<a id="CONFIG_TFM_PSA_TEST"></a>

## 252.76 `CONFIG_TFM_PSA_TEST`

**提示（Prompt）**：启用 PSA 测试套件（PSA test suite）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
CONFIG_TFM_PSA_TEST_NONE
```

**可选项（Choices）**

```text
CONFIG_TFM_PSA_TEST_CRYPTO
CONFIG_TFM_PSA_TEST_PROTECTED_STORAGE
CONFIG_TFM_PSA_TEST_INTERNAL_TRUSTED_STORAGE
CONFIG_TFM_PSA_TEST_STORAGE
CONFIG_TFM_PSA_TEST_INITIAL_ATTESTATION
CONFIG_TFM_PSA_TEST_NONE
CONFIG_TFM_PSA_TEST_CRYPTO
CONFIG_TFM_PSA_TEST_PROTECTED_STORAGE
CONFIG_TFM_PSA_TEST_INTERNAL_TRUSTED_STORAGE
CONFIG_TFM_PSA_TEST_STORAGE
CONFIG_TFM_PSA_TEST_INITIAL_ATTESTATION
CONFIG_TFM_PSA_TEST_NONE
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:494`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L494)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_PSA_TEST_NONE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PSA_TEST_NONE)、[`CONFIG_TFM_PSA_TEST_CRYPTO`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PSA_TEST_CRYPTO)、[`CONFIG_TFM_PSA_TEST_PROTECTED_STORAGE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PSA_TEST_PROTECTED_STORAGE)、[`CONFIG_TFM_PSA_TEST_INTERNAL_TRUSTED_STORAGE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PSA_TEST_INTERNAL_TRUSTED_STORAGE)、[`CONFIG_TFM_PSA_TEST_STORAGE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PSA_TEST_STORAGE)、[`CONFIG_TFM_PSA_TEST_INITIAL_ATTESTATION`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PSA_TEST_INITIAL_ATTESTATION)。

<a id="CONFIG_TFM_PSA_TEST_CRYPTO"></a>

## 252.77 `CONFIG_TFM_PSA_TEST_CRYPTO`

**提示（Prompt）**：加密测试（Crypto tests）

**说明（Help）**

启用 PSA 加密测试套件（PSA Crypto test suite）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_PSA_TEST>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:498`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L498)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → 启用 PSA 测试套件（PSA test suite）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PSA_TEST`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PSA_TEST)。

<a id="CONFIG_TFM_PSA_TEST_INITIAL_ATTESTATION"></a>

## 252.78 `CONFIG_TFM_PSA_TEST_INITIAL_ATTESTATION`

**提示（Prompt）**：初始证明测试（Initial attestation tests）

**说明（Help）**

启用 PSA 初始证明测试套件（Initial Attestation test suite）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_PSA_TEST>
```

**主动选择（Selects）**

```text
CONFIG_TFM_PARTITION_INITIAL_ATTESTATION
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:519`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L519)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → 启用 PSA 测试套件（PSA test suite）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PSA_TEST`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PSA_TEST)、[`CONFIG_TFM_PARTITION_INITIAL_ATTESTATION`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_INITIAL_ATTESTATION)。

<a id="CONFIG_TFM_PSA_TEST_INTERNAL_TRUSTED_STORAGE"></a>

## 252.79 `CONFIG_TFM_PSA_TEST_INTERNAL_TRUSTED_STORAGE`

**提示（Prompt）**：内部可信存储测试（Internal Trusted Storage tests）

**说明（Help）**

启用 PSA 内部可信存储测试套件（Internal Trusted Storage test suite）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_PSA_TEST>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:508`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L508)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → 启用 PSA 测试套件（PSA test suite）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PSA_TEST`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PSA_TEST)。

<a id="CONFIG_TFM_PSA_TEST_NONE"></a>

## 252.80 `CONFIG_TFM_PSA_TEST_NONE`

**提示（Prompt）**：不使用 PSA 测试套件（No PSA test suite）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_PSA_TEST>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:525`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L525)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → 启用 PSA 测试套件（PSA test suite）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PSA_TEST`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PSA_TEST)。

<a id="CONFIG_TFM_PSA_TEST_PROTECTED_STORAGE"></a>

## 252.81 `CONFIG_TFM_PSA_TEST_PROTECTED_STORAGE`

**提示（Prompt）**：存储测试（Storage tests）

**说明（Help）**

启用 PSA 受保护存储测试套件（Protected Storage test suite）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_PSA_TEST>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:503`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L503)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → 启用 PSA 测试套件（PSA test suite）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PSA_TEST`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PSA_TEST)。

<a id="CONFIG_TFM_PSA_TEST_STORAGE"></a>

## 252.82 `CONFIG_TFM_PSA_TEST_STORAGE`

**提示（Prompt）**：存储测试（Storage tests）

**说明（Help）**

启用 PSA 存储测试套件（Storage test suite），它结合了受保护存储（protected storage）和内部可信存储（internal trusted storage）测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_PSA_TEST>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:513`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L513)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → 启用 PSA 测试套件（PSA test suite）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PSA_TEST`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PSA_TEST)。

<a id="CONFIG_TFM_PS_ROLLBACK_PROTECTION"></a>

## 252.83 `CONFIG_TFM_PS_ROLLBACK_PROTECTION`

**提示（Prompt）**：回滚保护（Rollback protection）

**说明（Help）**

为受保护存储分区（Protected Storage partition）启用回滚保护（rollback protection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_PARTITION_PROTECTED_STORAGE && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm.ps:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm.ps#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_PROTECTED_STORAGE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_PROTECTED_STORAGE)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_PUBLIC_KEY_FORMAT"></a>

## 252.84 `CONFIG_TFM_PUBLIC_KEY_FORMAT`

**提示（Prompt）**：BL2 中的公钥存储格式（Public key storing format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_BL2 && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
CONFIG_TFM_PUBLIC_KEY_FORMAT_FULL
```

**可选项（Choices）**

```text
CONFIG_TFM_PUBLIC_KEY_FORMAT_FULL
CONFIG_TFM_PUBLIC_KEY_FORMAT_HASH
CONFIG_TFM_PUBLIC_KEY_FORMAT_FULL
CONFIG_TFM_PUBLIC_KEY_FORMAT_HASH
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:355`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L355)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_BL2`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_PUBLIC_KEY_FORMAT_FULL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PUBLIC_KEY_FORMAT_FULL)、[`CONFIG_TFM_PUBLIC_KEY_FORMAT_HASH`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PUBLIC_KEY_FORMAT_HASH)。

<a id="CONFIG_TFM_PUBLIC_KEY_FORMAT_FULL"></a>

## 252.85 `CONFIG_TFM_PUBLIC_KEY_FORMAT_FULL`

**提示（Prompt）**：完整（Full）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_PUBLIC_KEY_FORMAT>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:359`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L359)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → BL2 中的公钥存储格式（Public key storing format）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PUBLIC_KEY_FORMAT`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PUBLIC_KEY_FORMAT)。

<a id="CONFIG_TFM_PUBLIC_KEY_FORMAT_HASH"></a>

## 252.86 `CONFIG_TFM_PUBLIC_KEY_FORMAT_HASH`

**提示（Prompt）**：哈希（Hash）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_PUBLIC_KEY_FORMAT>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:363`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L363)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → BL2 中的公钥存储格式（Public key storing format）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PUBLIC_KEY_FORMAT`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PUBLIC_KEY_FORMAT)。

<a id="CONFIG_TFM_QCBOR_PATH"></a>

## 252.87 `CONFIG_TFM_QCBOR_PATH`

**提示（Prompt）**：QCBOR 路径，或设为 DOWNLOAD 以自动获取（Path or DOWNLOAD）

**说明（Help）**

用于 TF-M 构建的 QCBOR 路径。由于该库存在许可问题，Zephyr 不附带该库。若应用仍希望使用，可以指向自行检出的该库副本，或设为 `DOWNLOAD`，允许 TF-M 构建系统自动下载。译注：关于许可和随附状态的表述来自本次 Zephyr 官方文档快照。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_PARTITION_INITIAL_ATTESTATION && CONFIG_TFM_BL2 && CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:431`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L431)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_INITIAL_ATTESTATION`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_INITIAL_ATTESTATION)、[`CONFIG_TFM_BL2`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_SECURE_UART"></a>

## 252.88 `CONFIG_TFM_SECURE_UART`

**提示（Prompt）**：TF-M 将 UART 实例配置为安全外设（secure peripheral）

**说明（Help）**

将 UART 实例配置为安全外设（secure peripheral），用于 TF-M 日志。这会使非安全应用无法使用该 UART 实例。选择此选项时，需要在非安全应用中禁用对应 UART 实例的设备树节点（device tree node）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_FAMILY_NORDIC_NRF && !CONFIG_TFM_LOG_LEVEL_SILENCE
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:587`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L587)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_TFM_LOG_LEVEL_SILENCE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_LOG_LEVEL_SILENCE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_TFM_SFN"></a>

## 252.89 `CONFIG_TFM_SFN`

**提示（Prompt）**：安全函数模型（SFN model）

**说明（Help）**

使用安全函数模型（SFN Model）作为 PSA API 的安全分区管理器（SPM）后端。SFN 模型支持 SFN 分区模型和隔离级别 1。在此模型中，每个安全分区（Secure Partition）由一组实现安全服务的回调函数组成。SFN 模型符合面向 M 的 PSA 固件框架（PSA Firmware Framework for M，FF-M）v1.1。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_MODEL>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:480`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L480)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → TF-M 固件框架模型（Firmware Framework model）

**配置项引用（Symbol References）**：[`CONFIG_TFM_MODEL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_MODEL)。

<a id="CONFIG_TFM_SPM_LOG_LEVEL"></a>

## 252.90 `CONFIG_TFM_SPM_LOG_LEVEL`

**提示（Prompt）**：TF-M 安全分区管理器日志级别（SPM Log Level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
CONFIG_TFM_SPM_LOG_LEVEL_INFO
```

**可选项（Choices）**

```text
CONFIG_TFM_SPM_LOG_LEVEL_DEBUG
CONFIG_TFM_SPM_LOG_LEVEL_INFO
CONFIG_TFM_SPM_LOG_LEVEL_ERROR
CONFIG_TFM_SPM_LOG_LEVEL_SILENCE
CONFIG_TFM_SPM_LOG_LEVEL_DEBUG
CONFIG_TFM_SPM_LOG_LEVEL_INFO
CONFIG_TFM_SPM_LOG_LEVEL_ERROR
CONFIG_TFM_SPM_LOG_LEVEL_SILENCE
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:574`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L574)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_SPM_LOG_LEVEL_INFO`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_SPM_LOG_LEVEL_INFO)、[`CONFIG_TFM_SPM_LOG_LEVEL_DEBUG`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_SPM_LOG_LEVEL_DEBUG)、[`CONFIG_TFM_SPM_LOG_LEVEL_ERROR`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_SPM_LOG_LEVEL_ERROR)、[`CONFIG_TFM_SPM_LOG_LEVEL_SILENCE`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_SPM_LOG_LEVEL_SILENCE)。

<a id="CONFIG_TFM_SPM_LOG_LEVEL_DEBUG"></a>

## 252.91 `CONFIG_TFM_SPM_LOG_LEVEL_DEBUG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_SPM_LOG_LEVEL>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:577`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L577)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → TF-M 安全分区管理器日志级别（SPM Log Level）

**配置项引用（Symbol References）**：[`CONFIG_TFM_SPM_LOG_LEVEL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_SPM_LOG_LEVEL)。

<a id="CONFIG_TFM_SPM_LOG_LEVEL_ERROR"></a>

## 252.92 `CONFIG_TFM_SPM_LOG_LEVEL_ERROR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_SPM_LOG_LEVEL>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:581`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L581)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → TF-M 安全分区管理器日志级别（SPM Log Level）

**配置项引用（Symbol References）**：[`CONFIG_TFM_SPM_LOG_LEVEL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_SPM_LOG_LEVEL)。

<a id="CONFIG_TFM_SPM_LOG_LEVEL_INFO"></a>

## 252.93 `CONFIG_TFM_SPM_LOG_LEVEL_INFO`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_SPM_LOG_LEVEL>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:579`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L579)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → TF-M 安全分区管理器日志级别（SPM Log Level）

**配置项引用（Symbol References）**：[`CONFIG_TFM_SPM_LOG_LEVEL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_SPM_LOG_LEVEL)。

<a id="CONFIG_TFM_SPM_LOG_LEVEL_SILENCE"></a>

## 252.94 `CONFIG_TFM_SPM_LOG_LEVEL_SILENCE`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TFM_SPM_LOG_LEVEL>
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:583`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L583)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → TF-M 安全分区管理器日志级别（SPM Log Level）

**配置项引用（Symbol References）**：[`CONFIG_TFM_SPM_LOG_LEVEL`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_SPM_LOG_LEVEL)。

<a id="CONFIG_TFM_STM32_FLASH_LAYOUT_BEGIN_OFFSET"></a>

## 252.95 `CONFIG_TFM_STM32_FLASH_LAYOUT_BEGIN_OFFSET`

**提示（Prompt）**：Flash 布局起始处的偏移空隙（Offset gap）

**说明（Help）**

在 STM32 平台 Flash 布局的起始处设置一个偏移，TF-M 资源位置从该偏移之后开始。平台出于自身需要使用这段空隙，例如使用 TF-M 外部的引导加载程序（bootloader）时。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_FAMILY_STM32 && CONFIG_BUILD_WITH_TFM
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:603`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L603)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_TFM_T_COSE_PATH"></a>

## 252.96 `CONFIG_TFM_T_COSE_PATH`

**提示（Prompt）**：t_cose 路径，或设为 DOWNLOAD 以自动获取（Path or DOWNLOAD）

**说明（Help）**

用于 TF-M 构建的 t_cose 路径。Zephyr 不附带此库。若应用仍希望使用，可以指向自行检出的该库副本，或设为 `DOWNLOAD`，允许 TF-M 构建系统自动下载。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_PARTITION_INITIAL_ATTESTATION && CONFIG_TFM_BL2 && CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:440`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L440)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_TFM_PARTITION_INITIAL_ATTESTATION`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_PARTITION_INITIAL_ATTESTATION)、[`CONFIG_TFM_BL2`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_USE_NS_APP"></a>

## 252.97 `CONFIG_TFM_USE_NS_APP`

**提示（Prompt）**：使用 TF-M 非安全应用（Non-Secure application）

**说明（Help）**

TF-M 构建系统可以生成多个可执行文件，其中主要文件是 TF-M 安全固件。也可以选择构建 TF-M 非安全应用（non-secure application）。通常不使用 TF-M 非安全应用，因为 Zephyr 应用就是非安全应用。启用此选项后，情况反过来：使用 TF-M 非安全应用，替代 Zephyr 非安全应用。此选项仅用于测试，因为这是在 Zephyr 构建系统中集成并运行 TF-M 回归测试（regression tests）的最简便方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_WITH_TFM
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:273`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L273)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)。

<a id="CONFIG_TFM_ZEPHYR_4_0_TO_4_2_COMPATIBILITY"></a>

## 252.98 `CONFIG_TFM_ZEPHYR_4_0_TO_4_2_COMPATIBILITY`

**提示（Prompt）**：支持升级最初烧录 Zephyr v4.2 的设备（upgrading devices originally flashed with Zephyr v4.2）［已弃用，DEPRECATED］

**说明（Help）**

此选项已弃用（deprecated），请改用 `TFM_ZEPHYR_4_2_COMPATIBILITY`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_BL2 && CONFIG_BUILD_WITH_TFM
```

**主动选择（Selects）**

```text
CONFIG_TFM_ZEPHYR_4_2_COMPATIBILITY
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:265`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L265)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → 将 MCUboot 添加到 TFM（Add MCUboot to TFM）

**配置项引用（Symbol References）**：[`CONFIG_TFM_BL2`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_ZEPHYR_4_2_COMPATIBILITY`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_ZEPHYR_4_2_COMPATIBILITY)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_TFM_ZEPHYR_4_2_COMPATIBILITY"></a>

## 252.99 `CONFIG_TFM_ZEPHYR_4_2_COMPATIBILITY`

**提示（Prompt）**：支持升级最初烧录 Zephyr v4.2 的设备（upgrading devices originally flashed with Zephyr v4.2）

**说明（Help）**

Zephyr v4.2 所包含的 TF-M 版本（v2.2.0）将一个预配结构字段（provisioning structure field）`profile_definition` 的大小从 32 字节改为 48 字节。Zephyr v4.3 所包含的 TF-M 版本撤销了这项修改；但结构大小变化会使最初烧录 Zephyr v4.2 的设备无法进行空中升级（OTA upgrade），并导致设备失效（bricks devices）。此选项在 TF-M 中设置 `PROFILE_DEFINITION_LARGE` 宏定义，将该结构字段恢复为 48 字节。必须仅对最初使用 Zephyr v4.2 发行版烧录的应用设置此项。所有后续升级都必须保持此项启用。译注：版本和兼容性要求均按本次官方文档快照保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TFM_BL2 && CONFIG_BUILD_WITH_TFM
```

**被选择（Selected by）**

```text
CONFIG_TFM_ZEPHYR_4_0_TO_4_2_COMPATIBILITY
CONFIG_TFM_ZEPHYR_4_0_TO_4_2_COMPATIBILITY
```

**定义位置（Location）**：[`modules/trusted-firmware-m/Kconfig.tfm:249`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/trusted-firmware-m/Kconfig.tfm#L249)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → trusted-firmware-m（模块路径 `modules/tee/tf-m/trusted-firmware-m`，相对于 west 工作区顶层目录） → 构建时使用 TF-M 作为安全执行环境（Secure Execution Environment） → 将 MCUboot 添加到 TFM（Add MCUboot to TFM）

**配置项引用（Symbol References）**：[`CONFIG_TFM_BL2`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2)、[`CONFIG_BUILD_WITH_TFM`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_BUILD_WITH_TFM)、[`CONFIG_TFM_ZEPHYR_4_0_TO_4_2_COMPATIBILITY`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_ZEPHYR_4_0_TO_4_2_COMPATIBILITY)。

<!-- kconfig-navigation -->

[上一章](P251_modules_trusted-firmware-a_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P253_modules_uoscore-uedhoc_配置项参考.md)
