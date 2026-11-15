---
id: learning.zephyr-docs.kconfig-reference.page-387
title: "`subsys/mgmt`配置项参考（4/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第387章\_`subsys/mgmt`配置项参考（4/4）

本章翻译官方 Kconfig 数据库中 `subsys/mgmt` 的 30 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_OSDP_PD_ID_MODEL"></a>

## 387.1 `CONFIG_OSDP_PD_ID_MODEL`

**提示（Prompt）**：外围设备产品型号（PD Product Model Number）

**说明（Help）**

厂商产品型号，最低 8 位有效。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → 外围设备标识信息（Peripheral Device ID Information）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_ID_SERIAL_NUMBER"></a>

## 387.2 `CONFIG_OSDP_PD_ID_SERIAL_NUMBER`

**提示（Prompt）**：外围设备序列号（PD Serial Number）

**说明（Help）**

外围设备（PD）的 4 字节序列号。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
0xCAFEBABE
```

**取值范围（Ranges）**

```text
[0, 0xFFFFFFFF]
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → 外围设备标识信息（Peripheral Device ID Information）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_ID_VENDOR_CODE"></a>

## 387.3 `CONFIG_OSDP_PD_ID_VENDOR_CODE`

**提示（Prompt）**：外围设备厂商代码（PD Vendor Code）

**说明（Help）**

IEEE 分配的组织唯一标识符（OUI），最低 24 位有效。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
0x001A2B3C
```

**取值范围（Ranges）**

```text
[0, 0x00FFFFFF]
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → 外围设备标识信息（Peripheral Device ID Information）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_ID_VERSION"></a>

## 387.4 `CONFIG_OSDP_PD_ID_VERSION`

**提示（Prompt）**：外围设备产品版本（PD Product Version）

**说明（Help）**

厂商定义的产品版本，最低 8 位有效。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → 外围设备标识信息（Peripheral Device ID Information）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_POLL_RATE"></a>

## 387.5 `CONFIG_OSDP_PD_POLL_RATE`

**提示（Prompt）**：每秒发送给外围设备的 POLL 命令数量

**说明（Help）**

控制面板（CP）必须定期查询外围设备（PD），以维持连接序列并获取状态和事件。此选项定义每秒发送 `POLL` 命令的次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_MODE_CP && CONFIG_OSDP
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.cp:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.cp#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_MODE_CP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_CP)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_PD_SCBK"></a>

## 387.6 `CONFIG_OSDP_PD_SCBK`

**提示（Prompt）**：安全通道基础密钥（Secure Channel Base Key，SCBK）

**说明（Help）**

16 字节 OSDP 外围设备安全通道基础密钥（SCBK）的十六进制字符串表示。字段设为 `NONE` 时，PD 进入安装模式（Install Mode），允许控制面板（CP）用默认 SCBK 建立安全通道。使用默认密钥的安全通道建立后，CP 可发送 `KEYSET` 命令，为 PD 设置新密钥。用户必须确保 PD 仅在受控环境中的部署配置阶段（provisioning time）进入安装模式。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_SC_ENABLED && CONFIG_OSDP_MODE_PD && CONFIG_OSDP
```

**默认值（Defaults）**

```text
"NONE"
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig.pd:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig.pd#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_SC_ENABLED`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_OSDP_SC_ENABLED)、[`CONFIG_OSDP_MODE_PD`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP_MODE_PD)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_SC_ENABLED"></a>

## 387.7 `CONFIG_OSDP_SC_ENABLED`

**提示（Prompt）**：OSDP 安全通道（Secure Channel）

**说明（Help）**

通过加密（encryption）与双向认证（mutual authentication）保护 OSDP 通信通道。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ENTROPY_NODE_ENABLED && CONFIG_OSDP
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CRYPTO
CONFIG_CRYPTO_MBEDTLS_SHIM
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_NODE_ENABLED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENTROPY_NODE_ENABLED)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)、[`CONFIG_CRYPTO`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO)、[`CONFIG_CRYPTO_MBEDTLS_SHIM`](P071_drivers_crypto_配置项参考.md#CONFIG_CRYPTO_MBEDTLS_SHIM)。

<a id="CONFIG_OSDP_SC_RETRY_WAIT_SEC"></a>

## 387.8 `CONFIG_OSDP_SC_RETRY_WAIT_SEC`

**提示（Prompt）**：安全通道出错后的重试等待时间（秒）

**说明（Help）**

安全通道（secure channel）失败后，在重新尝试建立之前等待的时间，单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP_SC_ENABLED && CONFIG_OSDP
```

**默认值（Defaults）**

```text
600
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP） → OSDP 安全通道（Secure Channel）

**配置项引用（Symbol References）**：[`CONFIG_OSDP_SC_ENABLED`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_OSDP_SC_ENABLED)、[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_SKIP_MARK_BYTE"></a>

## 387.9 `CONFIG_OSDP_SKIP_MARK_BYTE`

**提示（Prompt）**：跳过初始标记字节（marking byte，0xFF）

**说明（Help）**

按 OSDP 规范，通道第一个字节必须是 `0xFF` 标记字节（MARK）。但由于数据包结构定义中未说明，某些商用控制面板（CP）和外围设备（PD）不能正确处理此初始字节。此选项可完全禁用标记字节的发送和接收期待，以兼容这些不符合规范的设备。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP）

**配置项引用（Symbol References）**：[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_THREAD_STACK_SIZE"></a>

## 387.10 `CONFIG_OSDP_THREAD_STACK_SIZE`

**提示（Prompt）**：OSDP 线程栈大小（Thread stack size）

**说明（Help）**

OSDP 刷新线程（refresh thread）的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP）

**配置项引用（Symbol References）**：[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_UART_BAUD_RATE"></a>

## 387.11 `CONFIG_OSDP_UART_BAUD_RATE`

**提示（Prompt）**：OSDP UART 波特率（baud rate）

**说明（Help）**

OSDP 规定波特率可为 `9600`、`38400` 或 `115200`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP
```

**默认值（Defaults）**

```text
115200
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP）

**配置项引用（Symbol References）**：[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_OSDP_UART_BUFFER_LENGTH"></a>

## 387.12 `CONFIG_OSDP_UART_BUFFER_LENGTH`

**提示（Prompt）**：OSDP UART 缓冲区长度（buffer length）

**说明（Help）**

OSDP 接收（RX）和发送（TX）缓冲区的先进先出队列（FIFO）长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OSDP
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`subsys/mgmt/osdp/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/osdp/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 开放式受监督设备协议驱动（Open Supervised Device Protocol，OSDP）

**配置项引用（Symbol References）**：[`CONFIG_OSDP`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_OSDP)。

<a id="CONFIG_SMP_CLIENT"></a>

## 387.13 `CONFIG_SMP_CLIENT`

**提示（Prompt）**：简单管理协议客户端支持（SMP Client support）

**说明（Help）**

启用 SMP 请求生成（Request generation）和响应处理（response handling）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/smp_client/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/smp_client/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 简单管理协议客户端（SMP Client）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_SMP_CLIENT_CMD_MAX"></a>

## 387.14 `CONFIG_SMP_CLIENT_CMD_MAX`

**提示（Prompt）**：SMP 客户端最大缓冲区数量

**说明（Help）**

定义客户端能够处理的活动请求（active requests）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SMP_CLIENT || CONFIG_ZTEST) && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/smp_client/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/smp_client/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 简单管理协议客户端（SMP Client）

**配置项引用（Symbol References）**：[`CONFIG_SMP_CLIENT`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_SMP_CLIENT)、[`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_SMP_CMD_DEFAULT_LIFE_TIME"></a>

## 387.15 `CONFIG_SMP_CMD_DEFAULT_LIFE_TIME`

**提示（Prompt）**：SMP 命令生存时间（秒，command lifetime）

**说明（Help）**

定义 SMP 客户端发送请求的生存时间。当请求使用的超时值为 `0` 时，采用此配置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SMP_CLIENT || CONFIG_ZTEST) && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[2, 30]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/smp_client/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/smp_client/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 简单管理协议客户端（SMP Client）

**配置项引用（Symbol References）**：[`CONFIG_SMP_CLIENT`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_SMP_CLIENT)、[`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_SMP_CMD_RETRY_TIME"></a>

## 387.16 `CONFIG_SMP_CMD_RETRY_TIME`

**提示（Prompt）**：SMP 命令重发周期（毫秒）

**说明（Help）**

SMP 客户端重新发送命令之前，等待响应的时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_SMP_CLIENT || CONFIG_ZTEST) && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
500
```

**取值范围（Ranges）**

```text
[100, 1000]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/smp_client/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/smp_client/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 简单管理协议客户端（SMP Client）

**配置项引用（Symbol References）**：[`CONFIG_SMP_CLIENT`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_SMP_CLIENT)、[`CONFIG_ZTEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZTEST)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_UPDATEHUB"></a>

## 387.17 `CONFIG_UPDATEHUB`

**提示（Prompt）**：UpdateHub 固件空中更新支持（Firmware Over-the-Air）

**说明（Help）**

原文将 UpdateHub 描述为企业级解决方案，用于简化现场嵌入式设备的远程更新，处理固件空中更新（Firmware Over-the-Air，FOTA）发送相关的各项事务，以安全、高效为目标，让开发者专注于产品功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH && CONFIG_REBOOT && CONFIG_IMG_MANAGER && CONFIG_BOOTLOADER_MCUBOOT && CONFIG_NETWORKING && CONFIG_NET_UDP && CONFIG_NET_SOCKETS && CONFIG_COAP && CONFIG_DNS_RESOLVER && CONFIG_JSON_LIBRARY && CONFIG_HWINFO
```

**主动选择（Selects）**

```text
CONFIG_REQUIRES_FULL_LIBC
CONFIG_IMG_ENABLE_IMAGE_CHECK
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
CONFIG_PSA_CRYPTO
CONFIG_PSA_WANT_ALG_SHA_256
```

**定义位置（Location）**：[`subsys/mgmt/updatehub/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/updatehub/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_REBOOT`](P198_lib_配置项参考_2.md#CONFIG_REBOOT)、[`CONFIG_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_MANAGER)、[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_COAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP)、[`CONFIG_DNS_RESOLVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DNS_RESOLVER)、[`CONFIG_JSON_LIBRARY`](P197_lib_配置项参考_1.md#CONFIG_JSON_LIBRARY)、[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_REQUIRES_FULL_LIBC`](P198_lib_配置项参考_2.md#CONFIG_REQUIRES_FULL_LIBC)、[`CONFIG_IMG_ENABLE_IMAGE_CHECK`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_ENABLE_IMAGE_CHECK)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)。

<a id="CONFIG_UPDATEHUB_CE"></a>

## 387.18 `CONFIG_UPDATEHUB_CE`

**提示（Prompt）**：使用 UpdateHub 社区版服务器（Community Edition Server）

**说明（Help）**

允许以 UpdateHub 社区版服务器（`updatehub-ce`）替代 `updatehub.io` 企业版服务器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UPDATEHUB
```

**定义位置（Location）**：[`subsys/mgmt/updatehub/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/updatehub/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_UPDATEHUB`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_UPDATEHUB)。

<a id="CONFIG_UPDATEHUB_COAP_BLOCK_SIZE_EXP"></a>

## 387.19 `CONFIG_UPDATEHUB_COAP_BLOCK_SIZE_EXP`

**提示（Prompt）**：CoAP 最大块大小，定义为 2^(4 + EXP)

**说明（Help）**

配置数据载荷（data payload）最大大小，取值与块大小的映射如下：

| 值 | CoAP 块大小枚举 |
| --- | --- |
| 0 | `COAP_BLOCK_16` |
| 1 | `COAP_BLOCK_32` |
| 2 | `COAP_BLOCK_64` |
| 3 | `COAP_BLOCK_128` |
| 4 | `COAP_BLOCK_256` |
| 5 | `COAP_BLOCK_512` |
| 6 | `COAP_BLOCK_1024` |

此值直接映射到 `enum coap_block_size`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UPDATEHUB
```

**默认值（Defaults）**

```text
6
```

**取值范围（Ranges）**

```text
[0, 6]
```

**定义位置（Location）**：[`subsys/mgmt/updatehub/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/updatehub/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_UPDATEHUB`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_UPDATEHUB)。

<a id="CONFIG_UPDATEHUB_COAP_CONN_TIMEOUT"></a>

## 387.20 `CONFIG_UPDATEHUB_COAP_CONN_TIMEOUT`

**提示（Prompt）**：受限应用协议（CoAP）连接超时，单位秒

**说明（Help）**

设置 CoAP 连接超时值（connection timeout）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UPDATEHUB
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[1, 360]
```

**定义位置（Location）**：[`subsys/mgmt/updatehub/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/updatehub/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_UPDATEHUB`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_UPDATEHUB)。

<a id="CONFIG_UPDATEHUB_COAP_MAX_RETRY"></a>

## 387.21 `CONFIG_UPDATEHUB_COAP_MAX_RETRY`

**提示（Prompt）**：下载数据包的最大重试次数

**说明（Help）**

设置下载数据包的最大重试次数，超过后中止当前更新。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UPDATEHUB
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[3, 10]
```

**定义位置（Location）**：[`subsys/mgmt/updatehub/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/updatehub/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_UPDATEHUB`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_UPDATEHUB)。

<a id="CONFIG_UPDATEHUB_DOWNLOAD_SHA256_VERIFICATION"></a>

## 387.22 `CONFIG_UPDATEHUB_DOWNLOAD_SHA256_VERIFICATION`

**提示（Prompt）**：下载时执行 SHA-256 验证

**说明（Help）**

下载过程中对数据流执行 SHA-256 验证。注意：这只确认下载内容匹配服务器端的 SHA，不检查写入存储后的映像是否仍然有效。若要同时检查永久存储中的数据是否匹配 SHA，应选择“同时验证下载和闪存（Both download and flash verifications）”。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/mgmt/updatehub/Kconfig:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/updatehub/Kconfig#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air） → 固件验证（Firmware verification）

<a id="CONFIG_UPDATEHUB_DOWNLOAD_STORAGE_SHA256_VERIFICATION"></a>

## 387.23 `CONFIG_UPDATEHUB_DOWNLOAD_STORAGE_SHA256_VERIFICATION`

**提示（Prompt）**：同时对下载和闪存执行 SHA-256 验证

**说明（Help）**

同时对下载过程中的数据流和闪存中存储的数据流执行 SHA-256 验证。建议保持此选项启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/mgmt/updatehub/Kconfig:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/updatehub/Kconfig#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air） → 固件验证（Firmware verification）

<a id="CONFIG_UPDATEHUB_DTLS"></a>

## 387.24 `CONFIG_UPDATEHUB_DTLS`

**提示（Prompt）**：启用 CoAPS／DTLS 通信

**说明（Help）**

在 UpdateHub 客户端与服务器之间启用数据报传输层安全协议（DTLS）通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UPDATEHUB
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS
CONFIG_MBEDTLS_ENABLE_HEAP
CONFIG_NET_SOCKETS_SOCKOPT_TLS
CONFIG_NET_SOCKETS_ENABLE_DTLS
```

**定义位置（Location）**：[`subsys/mgmt/updatehub/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/updatehub/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_UPDATEHUB`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_UPDATEHUB)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_ENABLE_HEAP`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_ENABLE_HEAP)、[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SOCKOPT_TLS)、[`CONFIG_NET_SOCKETS_ENABLE_DTLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_ENABLE_DTLS)。

<a id="CONFIG_UPDATEHUB_POLL_INTERVAL"></a>

## 387.25 `CONFIG_UPDATEHUB_POLL_INTERVAL`

**提示（Prompt）**：轮询间隔（分钟，poll interval）

**说明（Help）**

设置轮询 UpdateHub 更新服务器的间隔，范围为 0 至 43200 分钟，即 30 天。译注：原文写作 “zero and 43200”，此处按区间上下限表达。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UPDATEHUB
```

**默认值（Defaults）**

```text
1440
```

**取值范围（Ranges）**

```text
[0, 43200]
```

**定义位置（Location）**：[`subsys/mgmt/updatehub/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/updatehub/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_UPDATEHUB`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_UPDATEHUB)。

<a id="CONFIG_UPDATEHUB_PRODUCT_UID"></a>

## 387.26 `CONFIG_UPDATEHUB_PRODUCT_UID`

**提示（Prompt）**：产品唯一标识符（Product Unique Identifier，UID）

**说明（Help）**

与 UpdateHub 服务器通信时使用的产品唯一标识符（UID）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_UPDATEHUB
```

**定义位置（Location）**：[`subsys/mgmt/updatehub/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/updatehub/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_UPDATEHUB`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_UPDATEHUB)。

<a id="CONFIG_UPDATEHUB_SERVER"></a>

## 387.27 `CONFIG_UPDATEHUB_SERVER`

**提示（Prompt）**：用户指定的 updatehub-ce-server 地址

**说明（Help）**

此配置提供默认地址。若需使用其他地址，必须通过 UpdateHub 命令行（shell）设置。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_UPDATEHUB_CE && CONFIG_UPDATEHUB
```

**定义位置（Location）**：[`subsys/mgmt/updatehub/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/updatehub/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air） → 使用 UpdateHub 社区版服务器（Community Edition Server）

**配置项引用（Symbol References）**：[`CONFIG_UPDATEHUB_CE`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_UPDATEHUB_CE)、[`CONFIG_UPDATEHUB`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_UPDATEHUB)。

<a id="CONFIG_UPDATEHUB_SHELL"></a>

## 387.28 `CONFIG_UPDATEHUB_SHELL`

**提示（Prompt）**：UpdateHub 命令行工具（shell utilities）

**说明（Help）**

启用提供 UpdateHub 命令的命令行模块（shell module）。译注：原文在 “like” 后结束，未给出后续命令示例。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_UPDATEHUB
```

**主动选择（Selects）**

```text
CONFIG_KERNEL_SHELL
```

**定义位置（Location）**：[`subsys/mgmt/updatehub/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/updatehub/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_UPDATEHUB`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_UPDATEHUB)、[`CONFIG_KERNEL_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_KERNEL_SHELL)。

<a id="CONFIG_UPDATEHUB_STORAGE_SHA256_VERIFICATION"></a>

## 387.29 `CONFIG_UPDATEHUB_STORAGE_SHA256_VERIFICATION`

**提示（Prompt）**：从闪存执行 SHA-256 验证

**说明（Help）**

验证已存储的数据流。启用后，从存储中回读数据并进行 SHA 验证，确保数据已正确写入。若需同时确认下载数据流匹配 SHA，应选择“同时验证下载和闪存（Both download and flash verifications）”。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/mgmt/updatehub/Kconfig:130`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/updatehub/Kconfig#L130)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air） → 固件验证（Firmware verification）

<a id="CONFIG_UPDATEHUB_SUPPORTED_HARDWARE_MAX"></a>

## 387.30 `CONFIG_UPDATEHUB_SUPPORTED_HARDWARE_MAX`

**提示（Prompt）**：支持的硬件数量上限（Max number of supported hardware）

**说明（Help）**

配置同一映像支持的最大硬件数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_UPDATEHUB
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 100]
```

**定义位置（Location）**：[`subsys/mgmt/updatehub/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/updatehub/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_UPDATEHUB`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_UPDATEHUB)。

<!-- kconfig-navigation -->

[上一章](P386_subsys_mgmt_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P388_subsys_modbus_配置项参考.md)
