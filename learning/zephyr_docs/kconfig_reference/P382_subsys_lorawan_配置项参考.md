---
id: learning.zephyr-docs.kconfig-reference.page-382
title: "`subsys/lorawan`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第382章\_`subsys/lorawan`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/lorawan` 的 38 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LORAWAN"></a>

## 382.1 `CONFIG_LORAWAN`

**提示（Prompt）**：LoRaWAN 支持【实验性 EXPERIMENTAL】

**说明（Help）**

启用 LoRaWAN 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA
```

**主动选择（Selects）**

```text
CONFIG_REQUIRES_FULL_LIBC
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/lorawan/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_LORA`](P117_drivers_lora_配置项参考.md#CONFIG_LORA)、[`CONFIG_REQUIRES_FULL_LIBC`](P198_lib_配置项参考_2.md#CONFIG_REQUIRES_FULL_LIBC)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_LORAWAN_APP_CLOCK_SYNC"></a>

## 382.2 `CONFIG_LORAWAN_APP_CLOCK_SYNC`

**提示（Prompt）**：应用层时钟同步（Application Layer Clock Synchronization）

**说明（Help）**

按照 LoRa 联盟（LoRa Alliance）的 TS003-2.0.0 启用 LoRaWAN 应用层时钟同步服务，默认使用端口 `202`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORAWAN_SERVICES && CONFIG_LORAWAN
```

**定义位置（Location）**：[`subsys/lorawan/services/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/services/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_SERVICES`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_SERVICES)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_APP_CLOCK_SYNC_PERIODICITY"></a>

## 382.3 `CONFIG_LORAWAN_APP_CLOCK_SYNC_PERIODICITY`

**提示（Prompt）**：应用层时钟同步周期（periodicity）

**说明（Help）**

时钟同步周期的初始值，单位为秒。应用服务器可远程更新此值，范围为 `128`（`0x80`）至 `4194304`（`0x400000`）。默认设置为 24 小时。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LORAWAN_APP_CLOCK_SYNC && CONFIG_LORAWAN_SERVICES && CONFIG_LORAWAN
```

**默认值（Defaults）**

```text
86400
```

**取值范围（Ranges）**

```text
[128, 4194304]
```

**定义位置（Location）**：[`subsys/lorawan/services/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/services/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend） → 应用层时钟同步（Application Layer Clock Synchronization）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_APP_CLOCK_SYNC`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_APP_CLOCK_SYNC)、[`CONFIG_LORAWAN_SERVICES`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_SERVICES)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_EMUL"></a>

## 382.4 `CONFIG_LORAWAN_EMUL`

**提示（Prompt）**：LoRaWAN 仿真器（Emulator）

**说明（Help）**

该仿真器用于 LoRaWAN 服务的单元测试，提供向 LoRaWAN 协议栈发送任意消息并通过回调接收响应的接口，无需真实 LoRa 硬件。仿真器 API 见 `include/zephyr/lorawan/emul.h`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE && CONFIG_LORAWAN
```

**定义位置（Location）**：[`subsys/lorawan/emul/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/emul/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_FRAG_TRANSPORT"></a>

## 382.5 `CONFIG_LORAWAN_FRAG_TRANSPORT`

**提示（Prompt）**：分片数据块传输（Fragmented Data Block Transport）

**说明（Help）**

按照 LoRa 联盟（LoRa Alliance）发布的 TS004-1.0.0，启用 LoRaWAN 分片数据块传输服务，默认使用端口 `201`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MAP && CONFIG_FLASH_PAGE_LAYOUT && CONFIG_IMG_MANAGER && CONFIG_LITTLE_ENDIAN && CONFIG_LORAWAN_SERVICES && CONFIG_LORAWAN
```

**定义位置（Location）**：[`subsys/lorawan/services/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/services/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MAP)、[`CONFIG_FLASH_PAGE_LAYOUT`](P093_drivers_flash_配置项参考_2.md#CONFIG_FLASH_PAGE_LAYOUT)、[`CONFIG_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_MANAGER)、[`CONFIG_LITTLE_ENDIAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LITTLE_ENDIAN)、[`CONFIG_LORAWAN_SERVICES`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_SERVICES)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_LITTLE_ENDIAN`。

<a id="CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER"></a>

## 382.6 `CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER`

**提示（Prompt）**：分片数据块传输解码器实现（decoder implementation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORAWAN_FRAG_TRANSPORT && CONFIG_LORAWAN_SERVICES && CONFIG_LORAWAN
```

**默认值（Defaults）**

```text
CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER_SEMTECH if CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE
CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER_LOWMEM
```

**可选项（Choices）**

```text
CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER_SEMTECH
CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER_LOWMEM
```

**定义位置（Location）**：[`subsys/lorawan/services/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/services/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend） → 分片数据块传输（Fragmented Data Block Transport）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_FRAG_TRANSPORT`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_FRAG_TRANSPORT)、[`CONFIG_LORAWAN_SERVICES`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_SERVICES)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)、[`CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER_SEMTECH`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER_SEMTECH)、[`CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE)、[`CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER_LOWMEM`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER_LOWMEM)。

<a id="CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER_LOWMEM"></a>

## 382.7 `CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER_LOWMEM`

**提示（Prompt）**：低内存占用算法（Low Memory Footprint Algorithm）

**说明（Help）**

降低 RAM 占用的替代实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER>
```

**定义位置（Location）**：[`subsys/lorawan/services/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/services/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend） → 分片数据块传输（Fragmented Data Block Transport） → 分片数据块传输解码器实现（decoder implementation）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER)。

<a id="CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER_SEMTECH"></a>

## 382.8 `CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER_SEMTECH`

**提示（Prompt）**：Semtech 实现

**说明（Help）**

来自 LoRaMAC-node 的默认解码器（decoder）实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE && <choice CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER>
```

**定义位置（Location）**：[`subsys/lorawan/services/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/services/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend） → 分片数据块传输（Fragmented Data Block Transport） → 分片数据块传输解码器实现（decoder implementation）

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE)、[`CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_FRAG_TRANSPORT_DECODER)。

<a id="CONFIG_LORAWAN_FRAG_TRANSPORT_IMAGE_SIZE"></a>

## 382.9 `CONFIG_LORAWAN_FRAG_TRANSPORT_IMAGE_SIZE`

**提示（Prompt）**：固件映像总大小（firmware image）

**说明（Help）**

应用固件映像所在闪存分区的大小，单位为字节。需要传输的最少分片数根据此值除以分片大小计算。本设置对 RAM 使用量有显著影响。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LORAWAN_FRAG_TRANSPORT && CONFIG_LORAWAN_SERVICES && CONFIG_LORAWAN
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/lorawan/services/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/services/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend） → 分片数据块传输（Fragmented Data Block Transport）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_FRAG_TRANSPORT`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_FRAG_TRANSPORT)、[`CONFIG_LORAWAN_SERVICES`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_SERVICES)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_FRAG_TRANSPORT_MAX_FRAG_SIZE"></a>

## 382.10 `CONFIG_LORAWAN_FRAG_TRANSPORT_MAX_FRAG_SIZE`

**提示（Prompt）**：传输分片最大大小（Maximum size of transported fragments）

**说明（Help）**

固件空中升级（FUOTA）过程中，分片数据块传输会话内单个分片的最大大小，由服务器端选择。分片必须装入 LoRaWAN 载荷（payload），根据区域及频率设置，载荷最大可为 242 字节，其中 3 字节用于协议信息。某些微控制器，例如 STM32WL，要求分片大小为 8 的整数倍，详情参见闪存驱动。

本设置对 RAM 使用量有显著影响。若已知确切分片大小，将 MIN 和 MAX 配置均设为该值，可减少内存消耗。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LORAWAN_FRAG_TRANSPORT && CONFIG_LORAWAN_SERVICES && CONFIG_LORAWAN
```

**默认值（Defaults）**

```text
232
```

**取值范围（Ranges）**

```text
[1, 239]
```

**定义位置（Location）**：[`subsys/lorawan/services/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/services/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend） → 分片数据块传输（Fragmented Data Block Transport）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_FRAG_TRANSPORT`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_FRAG_TRANSPORT)、[`CONFIG_LORAWAN_SERVICES`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_SERVICES)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_FRAG_TRANSPORT_MAX_REDUNDANCY"></a>

## 382.11 `CONFIG_LORAWAN_FRAG_TRANSPORT_MAX_REDUNDANCY`

**提示（Prompt）**：冗余分片百分比（Percentage of redundant fragments）

**说明（Help）**

内置前向纠错（Forward Error Correction，FEC）机制允许利用服务器在全部数据包发送完之后追加的冗余包，重建丢失的数据包。本参数指定仍应能够重建完整固件映像的最大丢包比例，以百分比表示。本设置对 RAM 使用量有显著影响。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LORAWAN_FRAG_TRANSPORT && CONFIG_LORAWAN_SERVICES && CONFIG_LORAWAN
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[1, 100]
```

**定义位置（Location）**：[`subsys/lorawan/services/Kconfig:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/services/Kconfig#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend） → 分片数据块传输（Fragmented Data Block Transport）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_FRAG_TRANSPORT`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_FRAG_TRANSPORT)、[`CONFIG_LORAWAN_SERVICES`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_SERVICES)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_FRAG_TRANSPORT_MIN_FRAG_SIZE"></a>

## 382.12 `CONFIG_LORAWAN_FRAG_TRANSPORT_MIN_FRAG_SIZE`

**提示（Prompt）**：传输分片最小大小（Minimum size of transported fragments）

**说明（Help）**

固件空中升级（FUOTA）过程中，分片数据块传输会话内单个分片的最小大小，由服务器端选择。分片必须装入 LoRaWAN 载荷（payload），根据区域及频率设置，载荷最大可为 242 字节，其中 3 字节用于协议信息。某些微控制器，例如 STM32WL，要求分片大小为 8 的整数倍，详情参见闪存驱动。

本设置对 RAM 使用量有显著影响。若已知确切分片大小，将 MIN 和 MAX 配置均设为该值，可减少内存消耗。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LORAWAN_FRAG_TRANSPORT && CONFIG_LORAWAN_SERVICES && CONFIG_LORAWAN
```

**默认值（Defaults）**

```text
48
```

**取值范围（Ranges）**

```text
[1, 239]
```

**定义位置（Location）**：[`subsys/lorawan/services/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/services/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend） → 分片数据块传输（Fragmented Data Block Transport）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_FRAG_TRANSPORT`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_FRAG_TRANSPORT)、[`CONFIG_LORAWAN_SERVICES`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_SERVICES)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_LORAMAC_NODE"></a>

## 382.13 `CONFIG_LORAWAN_LORAMAC_NODE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏配置（hidden config），用于启用 loramac-node 后端专用选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE && CONFIG_LORAWAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_SEMTECH_LORAMAC
```

**弱选择（Implies）**

```text
CONFIG_HAS_SEMTECH_SOFT_SE
```

**定义位置（Location）**：[`subsys/lorawan/loramac-node/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/loramac-node/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)、[`CONFIG_HAS_SEMTECH_LORAMAC`](P239_modules_loramac-node_配置项参考.md#CONFIG_HAS_SEMTECH_LORAMAC)、[`CONFIG_HAS_SEMTECH_SOFT_SE`](P239_modules_loramac-node_配置项参考.md#CONFIG_HAS_SEMTECH_SOFT_SE)。

<a id="CONFIG_LORAWAN_NATIVE"></a>

## 382.14 `CONFIG_LORAWAN_NATIVE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏配置（hidden config），用于启用原生 LoRaWAN 后端（native backend）专用选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_MODULE_BACKEND_NATIVE && CONFIG_LORAWAN
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PSA_CRYPTO
CONFIG_PSA_WANT_ALG_CMAC
CONFIG_PSA_WANT_ALG_ECB_NO_PADDING
CONFIG_PSA_WANT_KEY_TYPE_AES
```

**定义位置（Location）**：[`subsys/lorawan/native/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/native/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_WANT_ALG_CMAC`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_CMAC)、[`CONFIG_PSA_WANT_ALG_ECB_NO_PADDING`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_ECB_NO_PADDING)、[`CONFIG_PSA_WANT_KEY_TYPE_AES`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_KEY_TYPE_AES)。

<a id="CONFIG_LORAWAN_NATIVE_DUTY_CYCLE"></a>

## 382.15 `CONFIG_LORAWAN_NATIVE_DUTY_CYCLE`

**提示（Prompt）**：强制执行区域占空比限制（regional duty cycle limits）

**说明（Help）**

按 ETSI 法规要求，例如 EU868，启用逐子频段（sub-band）占空比限制。启用后，协议栈跟踪每个子频段的空中传输时间（on-air time），并阻止尚未满足停发时间（off-time）的信道发送。测试时，或占空比限制由外部机制负责时，可禁用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_MODULE_BACKEND_NATIVE && CONFIG_LORAWAN
```

**定义位置（Location）**：[`subsys/lorawan/native/region/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/native/region/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_NATIVE_ENGINE_PRIORITY"></a>

## 382.16 `CONFIG_LORAWAN_NATIVE_ENGINE_PRIORITY`

**提示（Prompt）**：引擎线程优先级（Engine thread priority）

**说明（Help）**

原生 LoRaWAN 引擎线程（engine thread）的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_MODULE_BACKEND_NATIVE && CONFIG_LORAWAN
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/lorawan/native/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/native/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_NATIVE_ENGINE_STACK_SIZE"></a>

## 382.17 `CONFIG_LORAWAN_NATIVE_ENGINE_STACK_SIZE`

**提示（Prompt）**：引擎线程栈大小（Engine thread stack size）

**说明（Help）**

原生 LoRaWAN 引擎线程（engine thread）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_MODULE_BACKEND_NATIVE && CONFIG_LORAWAN
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`subsys/lorawan/native/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/native/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_NATIVE_MAX_CHANNELS"></a>

## 382.18 `CONFIG_LORAWAN_NATIVE_MAX_CHANNELS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

确定每个会话的信道表大小，不供用户调整，由所选区域（regions）决定。所译快照仅实现 EU868，采用 16 信道方案。支持更大信道方案的区域加入时，将通过 `default N if LORAWAN_REGION_X` 配置行扩展此项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_MODULE_BACKEND_NATIVE && CONFIG_LORAWAN
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/lorawan/native/region/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/native/region/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_NATIVE_PUBLIC_NETWORK"></a>

## 382.19 `CONFIG_LORAWAN_NATIVE_PUBLIC_NETWORK`

**提示（Prompt）**：LoRaWAN 公共网络（Public Network）

**说明（Help）**

使用公共 LoRaWAN 网络时启用，使用私有 LoRaWAN 网络时禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_MODULE_BACKEND_NATIVE && CONFIG_LORAWAN
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/lorawan/native/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/native/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_NVM"></a>

## 382.20 `CONFIG_LORAWAN_NVM`

**提示（Prompt）**：LoRaWAN 非易失性存储（NVM）后端

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORAWAN
```

**默认值（Defaults）**

```text
CONFIG_LORAWAN_NVM_SETTINGS if CONFIG_SETTINGS
CONFIG_LORAWAN_NVM_NONE
```

**可选项（Choices）**

```text
CONFIG_LORAWAN_NVM_NONE
CONFIG_LORAWAN_NVM_SETTINGS
```

**定义位置（Location）**：[`subsys/lorawan/nvm/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/nvm/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)、[`CONFIG_LORAWAN_NVM_SETTINGS`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_NVM_SETTINGS)、[`CONFIG_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS)、[`CONFIG_LORAWAN_NVM_NONE`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_NVM_NONE)。

<a id="CONFIG_LORAWAN_NVM_NONE"></a>

## 382.21 `CONFIG_LORAWAN_NVM_NONE`

**提示（Prompt）**：LoRaWAN 不使用 NVM 后端

**说明（Help）**

使用此配置时，每次发送空中激活（OTAA）入网请求时，应用都负责存储并恢复 `DevNonce` 值。该值应直接用于入网配置（join configuration）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LORAWAN_NVM>
```

**定义位置（Location）**：[`subsys/lorawan/nvm/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/nvm/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 非易失性存储（NVM）后端

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_NVM`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_NVM)。

<a id="CONFIG_LORAWAN_NVM_SETTINGS"></a>

## 382.22 `CONFIG_LORAWAN_NVM_SETTINGS`

**提示（Prompt）**：基于设置子系统的非易失性存储（Settings based NVM）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS && CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE && <choice CONFIG_LORAWAN_NVM>
```

**定义位置（Location）**：[`subsys/lorawan/nvm/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/nvm/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 非易失性存储（NVM）后端

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS)、[`CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE)、[`CONFIG_LORAWAN_NVM`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_NVM)。

<a id="CONFIG_LORAWAN_PUBLIC_NETWORK"></a>

## 382.23 `CONFIG_LORAWAN_PUBLIC_NETWORK`

**提示（Prompt）**：LoRaWAN 公共网络（Public Network）

**说明（Help）**

使用公共 LoRaWAN 网络时启用，使用私有 LoRaWAN 网络时禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE && CONFIG_LORAWAN
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/lorawan/loramac-node/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/loramac-node/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_REGION_AS923"></a>

## 382.24 `CONFIG_LORAWAN_REGION_AS923`

**提示（Prompt）**：亚洲 923 MHz 频段（Asia frequency band）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LORA_MODULE_BACKEND_NATIVE && CONFIG_LORAWAN
```

**定义位置（Location）**：[`subsys/lorawan/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 区域（Regions）

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_REGION_AU915"></a>

## 382.25 `CONFIG_LORAWAN_REGION_AU915`

**提示（Prompt）**：澳大利亚 915 MHz 频段（Australia frequency band）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LORA_MODULE_BACKEND_NATIVE && CONFIG_LORAWAN
```

**定义位置（Location）**：[`subsys/lorawan/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 区域（Regions）

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_REGION_CN470"></a>

## 382.26 `CONFIG_LORAWAN_REGION_CN470`

**提示（Prompt）**：中国 470 MHz 频段（China frequency band）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LORA_MODULE_BACKEND_NATIVE && CONFIG_LORAWAN
```

**定义位置（Location）**：[`subsys/lorawan/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 区域（Regions）

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_REGION_CN779"></a>

## 382.27 `CONFIG_LORAWAN_REGION_CN779`

**提示（Prompt）**：中国 779 MHz 频段（China frequency band）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LORA_MODULE_BACKEND_NATIVE && CONFIG_LORAWAN
```

**定义位置（Location）**：[`subsys/lorawan/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 区域（Regions）

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_REGION_EU433"></a>

## 382.28 `CONFIG_LORAWAN_REGION_EU433`

**提示（Prompt）**：欧洲 433 MHz 频段（Europe frequency band）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LORA_MODULE_BACKEND_NATIVE && CONFIG_LORAWAN
```

**定义位置（Location）**：[`subsys/lorawan/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 区域（Regions）

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_REGION_EU868"></a>

## 382.29 `CONFIG_LORAWAN_REGION_EU868`

**提示（Prompt）**：欧洲 868 MHz 频段（Europe frequency band）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORAWAN
```

**定义位置（Location）**：[`subsys/lorawan/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 区域（Regions）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_REGION_IN865"></a>

## 382.30 `CONFIG_LORAWAN_REGION_IN865`

**提示（Prompt）**：印度 865 MHz 频段（India frequency band）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LORA_MODULE_BACKEND_NATIVE && CONFIG_LORAWAN
```

**定义位置（Location）**：[`subsys/lorawan/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 区域（Regions）

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_REGION_KR920"></a>

## 382.31 `CONFIG_LORAWAN_REGION_KR920`

**提示（Prompt）**：韩国 920 MHz 频段（South Korea frequency band）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LORA_MODULE_BACKEND_NATIVE && CONFIG_LORAWAN
```

**定义位置（Location）**：[`subsys/lorawan/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 区域（Regions）

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_REGION_RU864"></a>

## 382.32 `CONFIG_LORAWAN_REGION_RU864`

**提示（Prompt）**：俄罗斯 864 MHz 频段（Russia frequency band）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LORA_MODULE_BACKEND_NATIVE && CONFIG_LORAWAN
```

**定义位置（Location）**：[`subsys/lorawan/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 区域（Regions）

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_REGION_US915"></a>

## 382.33 `CONFIG_LORAWAN_REGION_US915`

**提示（Prompt）**：北美洲 915 MHz 频段（North America frequency band）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LORA_MODULE_BACKEND_NATIVE && CONFIG_LORAWAN
```

**定义位置（Location）**：[`subsys/lorawan/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 区域（Regions）

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_NATIVE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_NATIVE)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_REMOTE_MULTICAST"></a>

## 382.34 `CONFIG_LORAWAN_REMOTE_MULTICAST`

**提示（Prompt）**：远程组播设置（Remote Multicast Setup）

**说明（Help）**

按照 LoRa 联盟（LoRa Alliance）发布的 TS005-1.0.0，启用 LoRaWAN 远程组播设置服务。该服务自动在后台运行，负责交换组播会话密钥（multicast session keys）并建立 C 类会话（class C session）。交换的密钥保存在非易失性存储器中，默认使用端口 `200`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORAWAN_APP_CLOCK_SYNC && !CONFIG_LORAWAN_NVM_NONE && CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE && CONFIG_LORAWAN_SERVICES && CONFIG_LORAWAN
```

**定义位置（Location）**：[`subsys/lorawan/services/Kconfig:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/services/Kconfig#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_APP_CLOCK_SYNC`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_APP_CLOCK_SYNC)、[`CONFIG_LORAWAN_NVM_NONE`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_NVM_NONE)、[`CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE)、[`CONFIG_LORAWAN_SERVICES`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_SERVICES)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_SERVICES"></a>

## 382.35 `CONFIG_LORAWAN_SERVICES`

**提示（Prompt）**：LoRaWAN 服务后端（Services backend）

**说明（Help）**

启用 LoRaWAN 后台服务，例如固件空中升级（FUOTA）所用服务。这些服务使用专用线程和工作队列（work queue）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LORAWAN && CONFIG_LORAWAN
```

**主动选择（Selects）**

```text
CONFIG_ENTROPY_GENERATOR
```

**定义位置（Location）**：[`subsys/lorawan/services/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/services/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_LORAWAN_SERVICES_THREAD_PRIORITY"></a>

## 382.36 `CONFIG_LORAWAN_SERVICES_THREAD_PRIORITY`

**提示（Prompt）**：服务线程优先级（Services thread priority）

**说明（Help）**

运行 LoRaWAN 后台服务的线程优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LORAWAN_SERVICES && CONFIG_LORAWAN
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/lorawan/services/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/services/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_SERVICES`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_SERVICES)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_SERVICES_THREAD_STACK_SIZE"></a>

## 382.37 `CONFIG_LORAWAN_SERVICES_THREAD_STACK_SIZE`

**提示（Prompt）**：服务线程栈大小（Services thread stack size）

**说明（Help）**

运行 LoRaWAN 后台服务的线程栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LORAWAN_SERVICES && CONFIG_LORAWAN
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`subsys/lorawan/services/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/services/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】 → LoRaWAN 服务后端（Services backend）

**配置项引用（Symbol References）**：[`CONFIG_LORAWAN_SERVICES`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN_SERVICES)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<a id="CONFIG_LORAWAN_SYSTEM_MAX_RX_ERROR"></a>

## 382.38 `CONFIG_LORAWAN_SYSTEM_MAX_RX_ERROR`

**提示（Prompt）**：LoRaWAN 系统最大接收误差（System Max Rx Error）

**说明（Help）**

系统最大接收定时误差（Max Rx timing error），单位为毫秒，供 LoRaWAN 协议栈计算 RX1／RX2 接收窗口时序。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE && CONFIG_LORAWAN
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`subsys/lorawan/loramac-node/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/lorawan/loramac-node/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → LoRaWAN 支持【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE`](P117_drivers_lora_配置项参考.md#CONFIG_LORA_MODULE_BACKEND_LORAMAC_NODE)、[`CONFIG_LORAWAN`](P382_subsys_lorawan_配置项参考.md#CONFIG_LORAWAN)。

<!-- kconfig-navigation -->

[上一章](P381_subsys_logging_配置项参考_30.md) · [返回大纲](大纲.md) · [下一章](P383_subsys_mem_mgmt_配置项参考.md)
