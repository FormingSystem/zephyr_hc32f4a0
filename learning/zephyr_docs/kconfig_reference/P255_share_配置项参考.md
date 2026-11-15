---
id: learning.zephyr-docs.kconfig-reference.page-255
title: "`share`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第255章\_`share`配置项参考

本章翻译官方 Kconfig 数据库中 `share` 的 45 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="SB_CONFIG_BOARD"></a>

## 255.1 `SB_CONFIG_BOARD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

保存开发板名称（Board Name），用于定位源码树中与开发板相关的文件，位于 `boards/` 下。查找 `linker.ld` 时先查开发板目录；如果未找到，则在 `soc/<arch>/<family>/<series>` 中查找链接器文件（Linker File）。

**类型（Type）**：字符串（String），`string`。

**默认值（Defaults）**

```text
"boards"
```

**定义位置（Location）**：[`share/sysbuild/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="SB_CONFIG_BOARD_DEPRECATED_RELEASE"></a>

## 255.2 `SB_CONFIG_BOARD_DEPRECATED_RELEASE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项在开发板配置中设置，表示将在哪个 Zephyr 发行版中删除该开发板配置。设置后，为该开发板进行的任何构建都会生成醒目的弃用警告（deprecation warning）。

**类型（Type）**：字符串（String），`string`。

**定义位置（Location）**：[`share/sysbuild/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="SB_CONFIG_BOARD_REVISION"></a>

## 255.3 `SB_CONFIG_BOARD_REVISION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果 `BOARD` 设置了修订版字段（revision field），此值就是该修订版，否则为空字符串。例如，`BOARD` 为 `plank@foo` 时，此选项为 `foo`；`BOARD` 为 `plank` 时，此选项为空字符串。

**类型（Type）**：字符串（String），`string`。

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`share/sysbuild/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="SB_CONFIG_BOOTLOADER"></a>

## 255.4 `SB_CONFIG_BOOTLOADER`

**提示（Prompt）**：引导加载程序支持（Bootloader support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
SB_CONFIG_SUPPORT_BOOTLOADER
```

**默认值（Defaults）**

```text
SB_CONFIG_BOOTLOADER_NONE
```

**可选项（Choices）**

```text
SB_CONFIG_BOOTLOADER_NONE
SB_CONFIG_BOOTLOADER_MCUBOOT
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SUPPORT_BOOTLOADER`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SUPPORT_BOOTLOADER)、[`SB_CONFIG_BOOTLOADER_NONE`](P255_share_配置项参考.md#SB_CONFIG_BOOTLOADER_NONE)、[`SB_CONFIG_BOOTLOADER_MCUBOOT`](P255_share_配置项参考.md#SB_CONFIG_BOOTLOADER_MCUBOOT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SUPPORT_BOOTLOADER`。

<a id="SB_CONFIG_BOOTLOADER_MCUBOOT"></a>

## 255.5 `SB_CONFIG_BOOTLOADER_MCUBOOT`

**提示（Prompt）**：MCUboot 引导加载程序（MCUboot bootloader）

**说明（Help）**

包含 MCUboot 的 Zephyr 移植版，作为要使用的引导加载程序（bootloader）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
SB_CONFIG_SUPPORT_BOOTLOADER_MCUBOOT_ZEPHYR && <choice SB_CONFIG_BOOTLOADER>
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 引导加载程序支持（Bootloader support）

**配置项引用（Symbol References）**：[`SB_CONFIG_SUPPORT_BOOTLOADER_MCUBOOT_ZEPHYR`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SUPPORT_BOOTLOADER_MCUBOOT_ZEPHYR)、[`SB_CONFIG_BOOTLOADER`](P255_share_配置项参考.md#SB_CONFIG_BOOTLOADER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SUPPORT_BOOTLOADER_MCUBOOT_ZEPHYR`。

<a id="SB_CONFIG_BOOTLOADER_NONE"></a>

## 255.6 `SB_CONFIG_BOOTLOADER_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**

构建中不包含引导加载程序（bootloader）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice SB_CONFIG_BOOTLOADER>
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 引导加载程序支持（Bootloader support）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOOTLOADER`](P255_share_配置项参考.md#SB_CONFIG_BOOTLOADER)。

<a id="SB_CONFIG_BOOT_ENCRYPTION"></a>

## 255.7 `SB_CONFIG_BOOT_ENCRYPTION`

**提示（Prompt）**：加密镜像支持（Encrypted image support）

**说明（Help）**

支持加密镜像（encrypted images）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
SB_CONFIG_SUPPORT_BOOT_ENCRYPTION && SB_CONFIG_BOOTLOADER_MCUBOOT
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L221)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_SUPPORT_BOOT_ENCRYPTION`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SUPPORT_BOOT_ENCRYPTION)、[`SB_CONFIG_BOOTLOADER_MCUBOOT`](P255_share_配置项参考.md#SB_CONFIG_BOOTLOADER_MCUBOOT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SUPPORT_BOOT_ENCRYPTION`。

<a id="SB_CONFIG_BOOT_ENCRYPTION_ALG"></a>

## 255.8 `SB_CONFIG_BOOT_ENCRYPTION_ALG`

**提示（Prompt）**：用于镜像加密的算法（image encryption algorithm）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
SB_CONFIG_BOOT_ENCRYPTION && SB_CONFIG_BOOTLOADER_MCUBOOT
```

**默认值（Defaults）**

```text
SB_CONFIG_BOOT_ENCRYPTION_ALG_AES_128
```

**可选项（Choices）**

```text
SB_CONFIG_BOOT_ENCRYPTION_ALG_AES_128
SB_CONFIG_BOOT_ENCRYPTION_ALG_AES_256
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L239)。

**菜单路径（Menu Path）**：顶层（Top） → 加密镜像支持（Encrypted image support）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOOT_ENCRYPTION`](P255_share_配置项参考.md#SB_CONFIG_BOOT_ENCRYPTION)、[`SB_CONFIG_BOOTLOADER_MCUBOOT`](P255_share_配置项参考.md#SB_CONFIG_BOOTLOADER_MCUBOOT)、[`SB_CONFIG_BOOT_ENCRYPTION_ALG_AES_128`](P255_share_配置项参考.md#SB_CONFIG_BOOT_ENCRYPTION_ALG_AES_128)、[`SB_CONFIG_BOOT_ENCRYPTION_ALG_AES_256`](P255_share_配置项参考.md#SB_CONFIG_BOOT_ENCRYPTION_ALG_AES_256)。

<a id="SB_CONFIG_BOOT_ENCRYPTION_ALG_AES_128"></a>

## 255.9 `SB_CONFIG_BOOT_ENCRYPTION_ALG_AES_128`

**提示（Prompt）**：使用 AES-128 加密镜像

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice SB_CONFIG_BOOT_ENCRYPTION_ALG>
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:243`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L243)。

**菜单路径（Menu Path）**：顶层（Top） → 加密镜像支持（Encrypted image support） → 用于镜像加密的算法（image encryption algorithm）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOOT_ENCRYPTION_ALG`](P255_share_配置项参考.md#SB_CONFIG_BOOT_ENCRYPTION_ALG)。

<a id="SB_CONFIG_BOOT_ENCRYPTION_ALG_AES_256"></a>

## 255.10 `SB_CONFIG_BOOT_ENCRYPTION_ALG_AES_256`

**提示（Prompt）**：使用 AES-256 加密镜像

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice SB_CONFIG_BOOT_ENCRYPTION_ALG>
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:246`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L246)。

**菜单路径（Menu Path）**：顶层（Top） → 加密镜像支持（Encrypted image support） → 用于镜像加密的算法（image encryption algorithm）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOOT_ENCRYPTION_ALG`](P255_share_配置项参考.md#SB_CONFIG_BOOT_ENCRYPTION_ALG)。

<a id="SB_CONFIG_BOOT_ENCRYPTION_KEY_FILE"></a>

## 255.11 `SB_CONFIG_BOOT_ENCRYPTION_KEY_FILE`

**提示（Prompt）**：加密 PEM 密钥文件（Encryption PEM key file）

**说明（Help）**

供 MCUBoot 使用的加密密钥文件（encryption key file）的绝对路径。译注：这里保留的是配置接口对路径的要求；文档中的默认路径按明确标注的起点以相对形式展示，不绑定任何读者的仓库位置。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
SB_CONFIG_BOOT_ENCRYPTION && SB_CONFIG_BOOTLOADER_MCUBOOT
```

**默认值（Defaults）**

```text
"bootloader/mcuboot/enc-ec256-priv.pem" if SB_CONFIG_BOOT_SIGNATURE_TYPE_ECDSA_P256
"bootloader/mcuboot/enc-x25519-priv.pem" if SB_CONFIG_BOOT_SIGNATURE_TYPE_ED25519
"bootloader/mcuboot/enc-rsa2048-priv.pem" if SB_CONFIG_BOOT_SIGNATURE_TYPE_RSA
""
```

> 译注：本字段中由上游构建环境展开的路径已改为相对表示，起点为west 工作区顶层目录。仅去除构建机目录前缀，路径其余部分、宏引用和条件保持原样；实际配置值仍由原构建系统解析。

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:227`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L227)。

**菜单路径（Menu Path）**：顶层（Top） → 加密镜像支持（Encrypted image support）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOOT_ENCRYPTION`](P255_share_配置项参考.md#SB_CONFIG_BOOT_ENCRYPTION)、[`SB_CONFIG_BOOTLOADER_MCUBOOT`](P255_share_配置项参考.md#SB_CONFIG_BOOTLOADER_MCUBOOT)、[`SB_CONFIG_BOOT_SIGNATURE_TYPE_ECDSA_P256`](P255_share_配置项参考.md#SB_CONFIG_BOOT_SIGNATURE_TYPE_ECDSA_P256)、[`SB_CONFIG_BOOT_SIGNATURE_TYPE_ED25519`](P255_share_配置项参考.md#SB_CONFIG_BOOT_SIGNATURE_TYPE_ED25519)、[`SB_CONFIG_BOOT_SIGNATURE_TYPE_RSA`](P255_share_配置项参考.md#SB_CONFIG_BOOT_SIGNATURE_TYPE_RSA)。

<a id="SB_CONFIG_BOOT_SIGNATURE_KEY_FILE"></a>

## 255.12 `SB_CONFIG_BOOT_SIGNATURE_KEY_FILE`

**提示（Prompt）**：签名 PEM 密钥文件，或以逗号分隔的文件列表（Signing PEM key files）

**说明（Help）**

签名密钥文件的路径，也可以是以逗号分隔的密钥文件列表，以便在引导加载程序（bootloader）中嵌入多个验证密钥（verification key）；使用其中任何一个密钥签署的镜像都会被接受。第一项还用于为应用签名；后续各项仅用于验证，必须是相同签名类型、仅含公钥的 PEM 文件（public-only PEM）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
SB_CONFIG_BOOTLOADER_MCUBOOT
```

**默认值（Defaults）**

```text
"bootloader/mcuboot/root-ec-p256.pem" if SB_CONFIG_BOOT_SIGNATURE_TYPE_ECDSA_P256
"bootloader/mcuboot/root-ed25519.pem" if SB_CONFIG_BOOT_SIGNATURE_TYPE_ED25519
"bootloader/mcuboot/root-rsa-2048.pem" if SB_CONFIG_BOOT_SIGNATURE_TYPE_RSA
""
```

> 译注：本字段中由上游构建环境展开的路径已改为相对表示，起点为west 工作区顶层目录。仅去除构建机目录前缀，路径其余部分、宏引用和条件保持原样；实际配置值仍由原构建系统解析。

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:203`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L203)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOOTLOADER_MCUBOOT`](P255_share_配置项参考.md#SB_CONFIG_BOOTLOADER_MCUBOOT)、[`SB_CONFIG_BOOT_SIGNATURE_TYPE_ECDSA_P256`](P255_share_配置项参考.md#SB_CONFIG_BOOT_SIGNATURE_TYPE_ECDSA_P256)、[`SB_CONFIG_BOOT_SIGNATURE_TYPE_ED25519`](P255_share_配置项参考.md#SB_CONFIG_BOOT_SIGNATURE_TYPE_ED25519)、[`SB_CONFIG_BOOT_SIGNATURE_TYPE_RSA`](P255_share_配置项参考.md#SB_CONFIG_BOOT_SIGNATURE_TYPE_RSA)。

<a id="SB_CONFIG_BOOT_SIGNATURE_TYPE"></a>

## 255.13 `SB_CONFIG_BOOT_SIGNATURE_TYPE`

**提示（Prompt）**：签名类型（Signature type）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
SB_CONFIG_BOOTLOADER_MCUBOOT
```

**默认值（Defaults）**

```text
SB_CONFIG_BOOT_SIGNATURE_TYPE_RSA
```

**可选项（Choices）**

```text
SB_CONFIG_BOOT_SIGNATURE_TYPE_NONE
SB_CONFIG_BOOT_SIGNATURE_TYPE_RSA
SB_CONFIG_BOOT_SIGNATURE_TYPE_ECDSA_P256
SB_CONFIG_BOOT_SIGNATURE_TYPE_ED25519
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:185`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L185)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOOTLOADER_MCUBOOT`](P255_share_配置项参考.md#SB_CONFIG_BOOTLOADER_MCUBOOT)、[`SB_CONFIG_BOOT_SIGNATURE_TYPE_RSA`](P255_share_配置项参考.md#SB_CONFIG_BOOT_SIGNATURE_TYPE_RSA)、[`SB_CONFIG_BOOT_SIGNATURE_TYPE_NONE`](P255_share_配置项参考.md#SB_CONFIG_BOOT_SIGNATURE_TYPE_NONE)、[`SB_CONFIG_BOOT_SIGNATURE_TYPE_ECDSA_P256`](P255_share_配置项参考.md#SB_CONFIG_BOOT_SIGNATURE_TYPE_ECDSA_P256)、[`SB_CONFIG_BOOT_SIGNATURE_TYPE_ED25519`](P255_share_配置项参考.md#SB_CONFIG_BOOT_SIGNATURE_TYPE_ED25519)。

<a id="SB_CONFIG_BOOT_SIGNATURE_TYPE_ECDSA_P256"></a>

## 255.14 `SB_CONFIG_BOOT_SIGNATURE_TYPE_ECDSA_P256`

**提示（Prompt）**：采用 P-256 曲线的椭圆曲线数字签名（Elliptic curve digital signatures）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice SB_CONFIG_BOOT_SIGNATURE_TYPE>
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:195`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L195)。

**菜单路径（Menu Path）**：顶层（Top） → 签名类型（Signature type）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOOT_SIGNATURE_TYPE`](P255_share_配置项参考.md#SB_CONFIG_BOOT_SIGNATURE_TYPE)。

<a id="SB_CONFIG_BOOT_SIGNATURE_TYPE_ED25519"></a>

## 255.15 `SB_CONFIG_BOOT_SIGNATURE_TYPE_ED25519`

**提示（Prompt）**：采用 ed25519 的爱德华兹曲线数字签名（Edwards curve digital signatures）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice SB_CONFIG_BOOT_SIGNATURE_TYPE>
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:198`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L198)。

**菜单路径（Menu Path）**：顶层（Top） → 签名类型（Signature type）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOOT_SIGNATURE_TYPE`](P255_share_配置项参考.md#SB_CONFIG_BOOT_SIGNATURE_TYPE)。

<a id="SB_CONFIG_BOOT_SIGNATURE_TYPE_NONE"></a>

## 255.16 `SB_CONFIG_BOOT_SIGNATURE_TYPE_NONE`

**提示（Prompt）**：无签名，仅使用哈希检查（No signature; hash check only）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice SB_CONFIG_BOOT_SIGNATURE_TYPE>
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L189)。

**菜单路径（Menu Path）**：顶层（Top） → 签名类型（Signature type）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOOT_SIGNATURE_TYPE`](P255_share_配置项参考.md#SB_CONFIG_BOOT_SIGNATURE_TYPE)。

<a id="SB_CONFIG_BOOT_SIGNATURE_TYPE_RSA"></a>

## 255.17 `SB_CONFIG_BOOT_SIGNATURE_TYPE_RSA`

**提示（Prompt）**：RSA 签名（RSA signatures）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice SB_CONFIG_BOOT_SIGNATURE_TYPE>
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:192`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L192)。

**菜单路径（Menu Path）**：顶层（Top） → 签名类型（Signature type）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOOT_SIGNATURE_TYPE`](P255_share_配置项参考.md#SB_CONFIG_BOOT_SIGNATURE_TYPE)。

<a id="SB_CONFIG_COMPILER_WARNINGS_AS_ERRORS"></a>

## 255.18 `SB_CONFIG_COMPILER_WARNINGS_AS_ERRORS`

**提示（Prompt）**：将警告视为错误（Warnings as Errors）。

**说明（Help）**

设置后，为所有镜像启用将警告视为错误的工具链标志（warning as error）。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`share/sysbuild/build/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/build/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 构建选项（Build options）

<a id="SB_CONFIG_DEPRECATED"></a>

## 255.19 `SB_CONFIG_DEPRECATED`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果某个功能或模块已被视为弃用（deprecated），则它必须选择此符号。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`share/sysbuild/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="SB_CONFIG_DEPRECATED_KCONFIGS_AS_ERRORS"></a>

## 255.20 `SB_CONFIG_DEPRECATED_KCONFIGS_AS_ERRORS`

**提示（Prompt）**：将已弃用 Kconfig 选项视为错误（Deprecated Kconfigs as Errors）。

**说明（Help）**

若构建启用了已弃用的 Kconfig 项（deprecated Kconfigs），将使构建系统报错失败。启用此选项时，也会将其传播到所有镜像。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
SB_CONFIG_WARN_DEPRECATED
```

**定义位置（Location）**：[`share/sysbuild/build/Kconfig:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/build/Kconfig#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 构建选项（Build options）

**配置项引用（Symbol References）**：[`SB_CONFIG_WARN_DEPRECATED`](P255_share_配置项参考.md#SB_CONFIG_WARN_DEPRECATED)。

<a id="SB_CONFIG_EXPERIMENTAL"></a>

## 255.21 `SB_CONFIG_EXPERIMENTAL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

被认定为处于实验性实现阶段（Experimental Implementation Stage）的特性必须选择此符号。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
SB_CONFIG_MCUBOOT_DIRECT_XIP_GENERATE_VARIANT
```

**定义位置（Location）**：[`share/sysbuild/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_MCUBOOT_DIRECT_XIP_GENERATE_VARIANT`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_DIRECT_XIP_GENERATE_VARIANT)。

<a id="SB_CONFIG_FIRMWARE_LOADER"></a>

## 255.22 `SB_CONFIG_FIRMWARE_LOADER`

**提示（Prompt）**：固件加载器镜像（Firmware loader image）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
SB_CONFIG_MCUBOOT_MODE_FIRMWARE_UPDATER
```

**默认值（Defaults）**

```text
SB_CONFIG_FIRMWARE_LOADER_IMAGE_NONE
```

**可选项（Choices）**

```text
SB_CONFIG_FIRMWARE_LOADER_IMAGE_NONE
SB_CONFIG_FIRMWARE_LOADER_IMAGE_SMP_SVR
```

**定义位置（Location）**：[`share/sysbuild/images/firmware_loader/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/firmware_loader/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_MCUBOOT_MODE_FIRMWARE_UPDATER`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE_FIRMWARE_UPDATER)、[`SB_CONFIG_FIRMWARE_LOADER_IMAGE_NONE`](P255_share_配置项参考.md#SB_CONFIG_FIRMWARE_LOADER_IMAGE_NONE)、[`SB_CONFIG_FIRMWARE_LOADER_IMAGE_SMP_SVR`](P255_share_配置项参考.md#SB_CONFIG_FIRMWARE_LOADER_IMAGE_SMP_SVR)。

<a id="SB_CONFIG_FIRMWARE_LOADER_IMAGE_NAME"></a>

## 255.23 `SB_CONFIG_FIRMWARE_LOADER_IMAGE_NAME`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

固件加载器镜像的名称（Name of firmware loader image）。

**类型（Type）**：字符串（String），`string`。

**默认值（Defaults）**

```text
"smp_svr" if SB_CONFIG_FIRMWARE_LOADER_IMAGE_SMP_SVR
```

**定义位置（Location）**：[`share/sysbuild/images/firmware_loader/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/firmware_loader/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_FIRMWARE_LOADER_IMAGE_SMP_SVR`](P255_share_配置项参考.md#SB_CONFIG_FIRMWARE_LOADER_IMAGE_SMP_SVR)。

<a id="SB_CONFIG_FIRMWARE_LOADER_IMAGE_NONE"></a>

## 255.24 `SB_CONFIG_FIRMWARE_LOADER_IMAGE_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**

构建中不包含固件加载器镜像（firmware loader image）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice SB_CONFIG_FIRMWARE_LOADER>
```

**定义位置（Location）**：[`share/sysbuild/images/firmware_loader/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/firmware_loader/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 固件加载器镜像（Firmware loader image）

**配置项引用（Symbol References）**：[`SB_CONFIG_FIRMWARE_LOADER`](P255_share_配置项参考.md#SB_CONFIG_FIRMWARE_LOADER)。

<a id="SB_CONFIG_FIRMWARE_LOADER_IMAGE_PATH"></a>

## 255.25 `SB_CONFIG_FIRMWARE_LOADER_IMAGE_PATH`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

固件加载器镜像的源码目录（Source directory）。

**类型（Type）**：字符串（String），`string`。

**默认值（Defaults）**

```text
"samples/subsys/mgmt/mcumgr/smp_svr" if SB_CONFIG_FIRMWARE_LOADER_IMAGE_SMP_SVR
```

> 译注：本字段中由上游构建环境展开的路径已改为相对表示，起点为Zephyr 源码根目录。仅去除构建机目录前缀，路径其余部分、宏引用和条件保持原样；实际配置值仍由原构建系统解析。

**定义位置（Location）**：[`share/sysbuild/images/firmware_loader/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/firmware_loader/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_FIRMWARE_LOADER_IMAGE_SMP_SVR`](P255_share_配置项参考.md#SB_CONFIG_FIRMWARE_LOADER_IMAGE_SMP_SVR)。

<a id="SB_CONFIG_FIRMWARE_LOADER_IMAGE_SMP_SVR"></a>

## 255.26 `SB_CONFIG_FIRMWARE_LOADER_IMAGE_SMP_SVR`

**提示（Prompt）**：smp_svr 示例（sample）

**说明（Help）**

包含 MCUmgr 的 `smp_svr` 示例，作为要使用的固件加载器镜像（firmware loader image）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
SB_CONFIG_SUPPORT_FIRMWARE_LOADER_SMP_SVR && <choice SB_CONFIG_FIRMWARE_LOADER>
```

**定义位置（Location）**：[`share/sysbuild/images/firmware_loader/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/firmware_loader/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 固件加载器镜像（Firmware loader image）

**配置项引用（Symbol References）**：[`SB_CONFIG_SUPPORT_FIRMWARE_LOADER_SMP_SVR`](https://docs.zephyrproject.org/latest/kconfig.html#SB_CONFIG_SUPPORT_FIRMWARE_LOADER_SMP_SVR)、[`SB_CONFIG_FIRMWARE_LOADER`](P255_share_配置项参考.md#SB_CONFIG_FIRMWARE_LOADER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`SB_CONFIG_SUPPORT_FIRMWARE_LOADER_SMP_SVR`。

<a id="SB_CONFIG_MCUBOOT_DIRECT_XIP_GENERATE_VARIANT"></a>

## 255.27 `SB_CONFIG_MCUBOOT_DIRECT_XIP_GENERATE_VARIANT`

**提示（Prompt）**：生成槽位 1 变体镜像（Generate slot 1 variant image）［实验性，EXPERIMENTAL］

**说明（Help）**

为备用分区 `slot1_partition` 生成一个可用于固件更新的镜像。此镜像应用与主镜像相同的配置选项，并增加一个设备树覆盖文件（DTS overlay），将选定的 Flash 分区改为 `slot1_partition`；镜像名称为 `<app>_slot_1_variant`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(SB_CONFIG_MCUBOOT_MODE_DIRECT_XIP || SB_CONFIG_MCUBOOT_MODE_DIRECT_XIP_WITH_REVERT) && SB_CONFIG_BOOTLOADER_MCUBOOT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
SB_CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:159`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L159)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_MCUBOOT_MODE_DIRECT_XIP`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE_DIRECT_XIP)、[`SB_CONFIG_MCUBOOT_MODE_DIRECT_XIP_WITH_REVERT`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE_DIRECT_XIP_WITH_REVERT)、[`SB_CONFIG_BOOTLOADER_MCUBOOT`](P255_share_配置项参考.md#SB_CONFIG_BOOTLOADER_MCUBOOT)、[`SB_CONFIG_EXPERIMENTAL`](P255_share_配置项参考.md#SB_CONFIG_EXPERIMENTAL)。

<a id="SB_CONFIG_MCUBOOT_MODE"></a>

## 255.28 `SB_CONFIG_MCUBOOT_MODE`

**提示（Prompt）**：工作模式（Mode of operation）

**说明（Help）**

MCUboot 的工作模式（operating mode）；此设置也会传播到应用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
SB_CONFIG_BOOTLOADER_MCUBOOT
```

**默认值（Defaults）**

```text
SB_CONFIG_MCUBOOT_MODE_SWAP_USING_OFFSET
```

**可选项（Choices）**

```text
SB_CONFIG_MCUBOOT_MODE_SINGLE_APP
SB_CONFIG_MCUBOOT_MODE_SWAP_USING_OFFSET
SB_CONFIG_MCUBOOT_MODE_SWAP_USING_MOVE
SB_CONFIG_MCUBOOT_MODE_SWAP_SCRATCH
SB_CONFIG_MCUBOOT_MODE_OVERWRITE_ONLY
SB_CONFIG_MCUBOOT_MODE_DIRECT_XIP
SB_CONFIG_MCUBOOT_MODE_DIRECT_XIP_WITH_REVERT
SB_CONFIG_MCUBOOT_MODE_RAM_LOAD
SB_CONFIG_MCUBOOT_MODE_RAM_LOAD_WITH_REVERT
SB_CONFIG_MCUBOOT_MODE_FIRMWARE_UPDATER
SB_CONFIG_MCUBOOT_MODE_SINGLE_APP_RAM_LOAD
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_BOOTLOADER_MCUBOOT`](P255_share_配置项参考.md#SB_CONFIG_BOOTLOADER_MCUBOOT)、[`SB_CONFIG_MCUBOOT_MODE_SWAP_USING_OFFSET`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE_SWAP_USING_OFFSET)、[`SB_CONFIG_MCUBOOT_MODE_SINGLE_APP`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE_SINGLE_APP)、[`SB_CONFIG_MCUBOOT_MODE_SWAP_USING_MOVE`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE_SWAP_USING_MOVE)、[`SB_CONFIG_MCUBOOT_MODE_SWAP_SCRATCH`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE_SWAP_SCRATCH)、[`SB_CONFIG_MCUBOOT_MODE_OVERWRITE_ONLY`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE_OVERWRITE_ONLY)、[`SB_CONFIG_MCUBOOT_MODE_DIRECT_XIP`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE_DIRECT_XIP)、[`SB_CONFIG_MCUBOOT_MODE_DIRECT_XIP_WITH_REVERT`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE_DIRECT_XIP_WITH_REVERT)、[`SB_CONFIG_MCUBOOT_MODE_RAM_LOAD`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE_RAM_LOAD)、[`SB_CONFIG_MCUBOOT_MODE_RAM_LOAD_WITH_REVERT`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE_RAM_LOAD_WITH_REVERT)、[`SB_CONFIG_MCUBOOT_MODE_FIRMWARE_UPDATER`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE_FIRMWARE_UPDATER)、[`SB_CONFIG_MCUBOOT_MODE_SINGLE_APP_RAM_LOAD`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE_SINGLE_APP_RAM_LOAD)。

<a id="SB_CONFIG_MCUBOOT_MODE_DIRECT_XIP"></a>

## 255.29 `SB_CONFIG_MCUBOOT_MODE_DIRECT_XIP`

**提示（Prompt）**：直接原地执行（DirectXIP）

**说明（Help）**

MCUboot 要求设备树（DT）中存在 `slot0_partition` 和 `slot1_partition`。此模式下，MCUboot 可以从任一分区启动，并选择应用镜像版本较高的分区。通常比较的是主版本号、次版本号和补丁号三元组（`major.minor.patch`）；若同时在 MCUboot 中选择了 `BOOT_VERSION_CMP_USE_BUILD_NUMBER`，则还会比较构建号（build number）。此选项会自动选择 `MCUBOOT_BOOTLOADER_NO_DOWNGRADE`，因为无法交换回更旧版本的应用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice SB_CONFIG_MCUBOOT_MODE>
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 工作模式（Mode of operation）

**配置项引用（Symbol References）**：[`SB_CONFIG_MCUBOOT_MODE`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE)。

<a id="SB_CONFIG_MCUBOOT_MODE_DIRECT_XIP_WITH_REVERT"></a>

## 255.30 `SB_CONFIG_MCUBOOT_MODE_DIRECT_XIP_WITH_REVERT`

**提示（Prompt）**：支持恢复的直接原地执行（DirectXIP with revert）

**说明（Help）**

MCUboot 要求设备树（DT）中存在 `slot0_partition` 和 `slot1_partition`。此模式下，只要应用被标记为下次启动时进行测试或永久启动，MCUboot 就会从任一槽位中选择版本更高的应用启动。标记为测试的应用必须在首次启动时自我确认（confirm），否则会被移除，MCUboot 将回退到先前获准的应用。此模式不允许自由切换应用版本：一旦较高版本获准，就不能再选择较低版本启动。由于无法对正在运行的应用降级，此模式选择 `MCUBOOT_BOOTLOADER_NO_DOWNGRADE`；但要注意，若较高版本应用未被确认，MCUboot 仍可能回退到较低版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice SB_CONFIG_MCUBOOT_MODE>
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 工作模式（Mode of operation）

**配置项引用（Symbol References）**：[`SB_CONFIG_MCUBOOT_MODE`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE)。

<a id="SB_CONFIG_MCUBOOT_MODE_FIRMWARE_UPDATER"></a>

## 255.31 `SB_CONFIG_MCUBOOT_MODE_FIRMWARE_UPDATER`

**提示（Prompt）**：固件更新程序（Firmware updater）

**说明（Help）**

MCUboot 仅从 `slot0_partition` 启动主应用，但定义了进入 `slot1_partition` 的入口机制（entrance mechanism）。后者是专用的固件更新应用（firmware updater application），用于更新 `slot0_partition` 中的应用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice SB_CONFIG_MCUBOOT_MODE>
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 工作模式（Mode of operation）

**配置项引用（Symbol References）**：[`SB_CONFIG_MCUBOOT_MODE`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE)。

<a id="SB_CONFIG_MCUBOOT_MODE_FIRMWARE_UPDATER_BOOT_MODE_ENTRANCE"></a>

## 255.32 `SB_CONFIG_MCUBOOT_MODE_FIRMWARE_UPDATER_BOOT_MODE_ENTRANCE`

**提示（Prompt）**：通过保留启动模式进入固件更新程序（Firmware updater retention boot mode entrance）

**说明（Help）**

在 MCUboot 和主应用中启用保留内存（retained memory）、保留机制（retention）以及启动模式模块（boot mode module），以便强制启动固件加载器应用镜像。这要求正确配置 `zephyr,boot-mode` chosen 节点。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
SB_CONFIG_MCUBOOT_MODE_FIRMWARE_UPDATER && SB_CONFIG_BOOTLOADER_MCUBOOT
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:170`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L170)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_MCUBOOT_MODE_FIRMWARE_UPDATER`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE_FIRMWARE_UPDATER)、[`SB_CONFIG_BOOTLOADER_MCUBOOT`](P255_share_配置项参考.md#SB_CONFIG_BOOTLOADER_MCUBOOT)。

<a id="SB_CONFIG_MCUBOOT_MODE_OVERWRITE_ONLY"></a>

## 255.33 `SB_CONFIG_MCUBOOT_MODE_OVERWRITE_ONLY`

**提示（Prompt）**：覆盖（Overwrite）

**说明（Help）**

MCUboot 使用镜像次槽位（secondary slot）的内容覆盖主槽位（primary slot）。此模式不保留次槽位中的上一版本，因此无法回退。它支持 `MCUBOOT_BOOTLOADER_NO_DOWNGRADE`；启用防降级后，只有次槽位版本高于主槽位版本时才会覆盖。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice SB_CONFIG_MCUBOOT_MODE>
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 工作模式（Mode of operation）

**配置项引用（Symbol References）**：[`SB_CONFIG_MCUBOOT_MODE`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE)。

<a id="SB_CONFIG_MCUBOOT_MODE_RAM_LOAD"></a>

## 255.34 `SB_CONFIG_MCUBOOT_MODE_RAM_LOAD`

**提示（Prompt）**：加载到 RAM（RAM load）

**说明（Help）**

MCUboot 要求设备树（DT）中存在 `slot0_partition` 和 `slot1_partition`。此模式下，MCUboot 会选择版本号较高的镜像，将其复制到 RAM，并从 RAM 开始执行。镜像必须链接为从 RAM 执行；复制目标地址由运行 imgtool 时的 `load-addr` 参数指定。注意：此模式下，必须为引导加载程序（bootloader）分配应用不使用的 RAM，使引导加载程序在应用启动完成之前能够正常运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice SB_CONFIG_MCUBOOT_MODE>
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 工作模式（Mode of operation）

**配置项引用（Symbol References）**：[`SB_CONFIG_MCUBOOT_MODE`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE)。

<a id="SB_CONFIG_MCUBOOT_MODE_RAM_LOAD_WITH_REVERT"></a>

## 255.35 `SB_CONFIG_MCUBOOT_MODE_RAM_LOAD_WITH_REVERT`

**提示（Prompt）**：支持恢复的 RAM 加载（RAM load with revert）

**说明（Help）**

MCUboot 要求设备树（DT）中存在 `slot0_partition` 和 `slot1_partition`。此模式下，MCUboot 会选择版本号较高的镜像，将其复制到 RAM，并从 RAM 开始执行。只有镜像被标记为下次进行测试启动（test）或永久启动（permanent）时，MCUBoot 才会启动它。若应用被标记为测试，则必须在首次启动时确认自身（confirm itself）；否则会被移除，MCUboot 将恢复启动先前已批准的应用。镜像必须链接为从 RAM 执行；复制目标地址由运行 imgtool 时的 `load-addr` 参数指定。注意：此模式下，必须为引导加载程序（bootloader）分配应用不使用的 RAM，使引导加载程序在应用启动完成之前能够正常运行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice SB_CONFIG_MCUBOOT_MODE>
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 工作模式（Mode of operation）

**配置项引用（Symbol References）**：[`SB_CONFIG_MCUBOOT_MODE`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE)。

<a id="SB_CONFIG_MCUBOOT_MODE_SINGLE_APP"></a>

## 255.36 `SB_CONFIG_MCUBOOT_MODE_SINGLE_APP`

**提示（Prompt）**：单槽位（Single slot）

**说明（Help）**

MCUboot 仅启动位于 `slot0_partition` 的应用，不关心其他槽位。此模式下，应用无法通过设备固件升级（DFU）将自身更新写入次槽位，所有更新都必须通过 MCUboot 串行恢复（serial recovery）完成。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice SB_CONFIG_MCUBOOT_MODE>
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 工作模式（Mode of operation）

**配置项引用（Symbol References）**：[`SB_CONFIG_MCUBOOT_MODE`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE)。

<a id="SB_CONFIG_MCUBOOT_MODE_SINGLE_APP_RAM_LOAD"></a>

## 255.37 `SB_CONFIG_MCUBOOT_MODE_SINGLE_APP_RAM_LOAD`

**提示（Prompt）**：单应用 RAM 加载模式（Single app RAM load mode）

**说明（Help）**

MCUboot 可从任意位置将镜像加载到 RAM。此模式下，它将镜像复制到 RAM 并从 RAM 开始执行。镜像必须链接为从 RAM 执行，复制目标地址在运行 `imgtool` 时通过 `load-addr` 参数指定。虽然不直接使用 `slot0_partition`，但仍必须在设备树（DT）中定义该分区，因为需要用它获取待加载镜像大小的信息。由于无法换回较旧版本的应用，此选项自动选择 `MCUBOOT_BOOTLOADER_NO_DOWNGRADE`。事实上，此模式不支持任何交换操作（swap operations）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice SB_CONFIG_MCUBOOT_MODE>
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 工作模式（Mode of operation）

**配置项引用（Symbol References）**：[`SB_CONFIG_MCUBOOT_MODE`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE)。

<a id="SB_CONFIG_MCUBOOT_MODE_SWAP_SCRATCH"></a>

## 255.38 `SB_CONFIG_MCUBOOT_MODE_SWAP_SCRATCH`

**提示（Prompt）**：使用暂存区交换（Swap using scratch）

**说明（Help）**

MCUboot 要求设备树（DT）中存在 `slot0_partition`、`slot1_partition` 和 `scratch_partition`，应用从 `slot0_partition` 启动。此模式下，MCUboot 将应用从次槽位（secondary slot）交换到主槽位（primary slot）时，使用 `scratch_partition` 作为临时存储。如果构建 MCUboot 时启用了 `MCUBOOT_DOWNGRADE_PREVENTION`，主应用也应选择 `MCUBOOT_BOOTLOADER_NO_DOWNGRADE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice SB_CONFIG_MCUBOOT_MODE>
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 工作模式（Mode of operation）

**配置项引用（Symbol References）**：[`SB_CONFIG_MCUBOOT_MODE`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE)。

<a id="SB_CONFIG_MCUBOOT_MODE_SWAP_USING_MOVE"></a>

## 255.39 `SB_CONFIG_MCUBOOT_MODE_SWAP_USING_MOVE`

**提示（Prompt）**：使用移动方式交换（Swap using move）

**说明（Help）**

MCUboot 要求设备树（DT）中存在 `slot0_partition` 和 `slot1_partition`，应用从 `slot0_partition` 启动。如果构建 MCUboot 时启用了 `MCUBOOT_DOWNGRADE_PREVENTION`，主应用也应选择 `MCUBOOT_BOOTLOADER_NO_DOWNGRADE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice SB_CONFIG_MCUBOOT_MODE>
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 工作模式（Mode of operation）

**配置项引用（Symbol References）**：[`SB_CONFIG_MCUBOOT_MODE`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE)。

<a id="SB_CONFIG_MCUBOOT_MODE_SWAP_USING_OFFSET"></a>

## 255.40 `SB_CONFIG_MCUBOOT_MODE_SWAP_USING_OFFSET`

**提示（Prompt）**：使用偏移方式交换（Swap using offset）

**说明（Help）**

MCUboot 要求设备树（DT）中存在 `slot0_partition` 和 `slot1_partition`，应用从 `slot0_partition` 启动。如果构建 MCUboot 时启用了 `MCUBOOT_DOWNGRADE_PREVENTION`，主应用也应选择 `MCUBOOT_BOOTLOADER_NO_DOWNGRADE`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice SB_CONFIG_MCUBOOT_MODE>
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 工作模式（Mode of operation）

**配置项引用（Symbol References）**：[`SB_CONFIG_MCUBOOT_MODE`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE)。

<a id="SB_CONFIG_MCUBOOT_RAMLOAD_ALLOW_XIP"></a>

## 255.41 `SB_CONFIG_MCUBOOT_RAMLOAD_ALLOW_XIP`

**提示（Prompt）**：使用 RAM 加载时允许原地执行（Allow XIP when using RAM load）

**说明（Help）**

使用 MCUboot RAM 加载模式（RAM Load mode）时，允许应用从最初加载到的 RAM 中原地执行（XIP）。如果应用链接为在与数据 RAM 分离的指令 RAM 中执行，这会很有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(SB_CONFIG_MCUBOOT_MODE_RAM_LOAD || SB_CONFIG_MCUBOOT_MODE_RAM_LOAD_WITH_REVERT) && SB_CONFIG_BOOTLOADER_MCUBOOT
```

**定义位置（Location）**：[`share/sysbuild/images/bootloader/Kconfig:151`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/images/bootloader/Kconfig#L151)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`SB_CONFIG_MCUBOOT_MODE_RAM_LOAD`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE_RAM_LOAD)、[`SB_CONFIG_MCUBOOT_MODE_RAM_LOAD_WITH_REVERT`](P255_share_配置项参考.md#SB_CONFIG_MCUBOOT_MODE_RAM_LOAD_WITH_REVERT)、[`SB_CONFIG_BOOTLOADER_MCUBOOT`](P255_share_配置项参考.md#SB_CONFIG_BOOTLOADER_MCUBOOT)。

<a id="SB_CONFIG_MERGED_HEX_FILES"></a>

## 255.42 `SB_CONFIG_MERGED_HEX_FILES`

**提示（Prompt）**：创建合并的 hex 文件（merged hex files）

**说明（Help）**

启用此选项后，会为每个不同的开发板目标（board target）创建一个合并 hex 文件，将所有 hex 输出文件的数据合并到单个文件中，命名为 `merged_<NORMALIZED_BOARD_TARGET>.hex`。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`share/sysbuild/build/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/build/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 构建选项（Build options）

<a id="SB_CONFIG_NOT_SECURE"></a>

## 255.43 `SB_CONFIG_NOT_SECURE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

特性选择此符号，以表示该特性不安全（Not Secure）。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`share/sysbuild/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="SB_CONFIG_WARN_DEPRECATED"></a>

## 255.44 `SB_CONFIG_WARN_DEPRECATED`

**提示（Prompt）**：对已弃用功能的使用发出警告（Deprecated Usage）。

**说明（Help）**

解析 Kconfig 树时，如果启用了任何已弃用功能（deprecated features），则打印警告。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`share/sysbuild/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="SB_CONFIG_WARN_EXPERIMENTAL"></a>

## 255.45 `SB_CONFIG_WARN_EXPERIMENTAL`

**提示（Prompt）**：对实验性功能的使用发出警告（Experimental Usage）。

**说明（Help）**

解析 Kconfig 树时，若启用了任何实验性特性，则打印警告。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`share/sysbuild/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/sysbuild/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top）

<!-- kconfig-navigation -->

[上一章](P254_modules_zcbor_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P256_soc_Kconfig_配置项参考.md)
