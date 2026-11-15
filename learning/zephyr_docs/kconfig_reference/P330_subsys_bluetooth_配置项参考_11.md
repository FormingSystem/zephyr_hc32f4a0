---
id: learning.zephyr-docs.kconfig-reference.page-330
title: "`subsys/bluetooth`配置项参考（11/13）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第330章\_`subsys/bluetooth`配置项参考（11/13）

本章翻译官方 Kconfig 数据库中 `subsys/bluetooth` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_MPL_ICON_URL"></a>

## 330.1 `CONFIG_BT_MPL_ICON_URL`

**提示（Prompt）**：媒体播放器图标 URL（Media player Icon URL）

**说明（Help）**

设置媒体播放器图标（Media Player Icon）的 URL。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MPL && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
"http://server.some.where/path/icon.png"
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mpl:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mpl#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体播放器支持（Support for media player）

**配置项引用（Symbol References）**：[`CONFIG_BT_MPL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MPL)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MPL_ICON_URL_MAX"></a>

## 330.2 `CONFIG_BT_MPL_ICON_URL_MAX`

**提示（Prompt）**：媒体播放器图标 URL 最大长度（Max length of media player icon URL）

**说明（Help）**

设置媒体播放器图标 URL（media player icon URL）的最大字节数，包括空终止符（null termination）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MPL && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
40
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mpl:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mpl#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体播放器支持（Support for media player）

**配置项引用（Symbol References）**：[`CONFIG_BT_MPL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MPL)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MPL_MAX_OBJ_SIZE"></a>

## 330.3 `CONFIG_BT_MPL_MAX_OBJ_SIZE`

**提示（Prompt）**：存储对象内容的总内存大小（Total memory size for object content）

**说明（Help）**

设置存储对象内容（object content）的总内存大小，单位为八位字节（octets）。它决定总内存池缓冲区大小，发送对象内容时从该池分配内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MPL_OBJECTS && CONFIG_BT_MPL && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
127
```

**取值范围（Ranges）**

```text
[0, 65536]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mpl:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mpl#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体播放器支持（Support for media player） → 媒体播放器对象支持（Support for media player objects）

**配置项引用（Symbol References）**：[`CONFIG_BT_MPL_OBJECTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_MPL_OBJECTS)、[`CONFIG_BT_MPL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MPL)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MPL_MEDIA_PLAYER_NAME"></a>

## 330.4 `CONFIG_BT_MPL_MEDIA_PLAYER_NAME`

**提示（Prompt）**：媒体播放器名称（Media Player Name）

**说明（Help）**

设置媒体播放器名称（media player name）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MPL && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
"Player0"
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mpl:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mpl#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体播放器支持（Support for media player）

**配置项引用（Symbol References）**：[`CONFIG_BT_MPL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MPL)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MPL_MEDIA_PLAYER_NAME_MAX"></a>

## 330.5 `CONFIG_BT_MPL_MEDIA_PLAYER_NAME_MAX`

**提示（Prompt）**：媒体播放器名称最大长度（Max length of media player name）

**说明（Help）**

设置媒体播放器名称（media player name）的最大字节数，包括空终止符（null termination）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MPL && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mpl:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mpl#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体播放器支持（Support for media player）

**配置项引用（Symbol References）**：[`CONFIG_BT_MPL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MPL)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MPL_OBJECTS"></a>

## 330.6 `CONFIG_BT_MPL_OBJECTS`

**提示（Prompt）**：媒体播放器对象支持（Support for media player objects）

**说明（Help）**

启用媒体播放器对象（media player objects）支持。对象用于提供或获取更多信息，例如媒体曲目信息；需要对象传输服务（Object Transfer Service）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OTS && CONFIG_BT_MCS && CONFIG_BT_MPL && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mpl:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mpl#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体播放器支持（Support for media player）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS)、[`CONFIG_BT_MCS`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCS)、[`CONFIG_BT_MPL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MPL)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MPL_SEGMENT_NAME_MAX"></a>

## 330.7 `CONFIG_BT_MPL_SEGMENT_NAME_MAX`

**提示（Prompt）**：曲目分段名称最大长度（Max length of name of a track segment）

**说明（Help）**

设置媒体播放器中任意曲目分段名称（track segment name）的最大字节数，包括空终止符（null termination）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MPL && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
25
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mpl:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mpl#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体播放器支持（Support for media player）

**配置项引用（Symbol References）**：[`CONFIG_BT_MPL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MPL)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MPL_TRACK_MAX_SIZE"></a>

## 330.8 `CONFIG_BT_MPL_TRACK_MAX_SIZE`

**提示（Prompt）**：曲目对象最大大小（Maximum size for a track object）

**说明（Help）**

设置曲目对象（track object）的最大大小，单位为八位字节（octets）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MPL_OBJECTS && CONFIG_BT_MPL && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
127
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mpl:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mpl#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体播放器支持（Support for media player） → 媒体播放器对象支持（Support for media player objects）

**配置项引用（Symbol References）**：[`CONFIG_BT_MPL_OBJECTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_MPL_OBJECTS)、[`CONFIG_BT_MPL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MPL)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_MPL_TRACK_TITLE_MAX"></a>

## 330.9 `CONFIG_BT_MPL_TRACK_TITLE_MAX`

**提示（Prompt）**：曲目标题最大长度（Max length of the title of a track）

**说明（Help）**

设置媒体播放器中任意曲目标题（track title）的最大字节数，包括空终止符（null termination）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_MPL && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
40
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.mpl:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.mpl#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 媒体播放器支持（Support for media player）

**配置项引用（Symbol References）**：[`CONFIG_BT_MPL`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MPL)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_OBEX_AUTH"></a>

## 330.10 `CONFIG_BT_OBEX_AUTH`

**提示（Prompt）**：蓝牙 OBEX 认证支持（Bluetooth OBEX Authentication support）

**说明（Help）**

启用对象交换协议（OBEX）认证功能。OBEX 认证使用 MD5，其密码学安全性较弱，只能提供有限的安全保护。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GOEP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_PSA_WANT_ALG_MD5
CONFIG_MBEDTLS
```

**被选择（Selected by）**

```text
CONFIG_BT_PBAP
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:750`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L750)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → 蓝牙通用对象交换配置文件（Bluetooth GOEP Profile）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_GOEP`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_GOEP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_PSA_WANT_ALG_MD5`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_MD5)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_BT_PBAP`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBAP)。

<a id="CONFIG_BT_OBEX_AUTH_PWD_LEN"></a>

## 330.11 `CONFIG_BT_OBEX_AUTH_PWD_LEN`

**提示（Prompt）**：OBEX 认证密码最大长度（Maximum OBEX Authentication Password Length）

**说明（Help）**

设置 OBEX 认证密码（authentication password）的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBEX_AUTH && CONFIG_BT_GOEP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:759`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L759)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → 蓝牙通用对象交换配置文件（Bluetooth GOEP Profile）[实验性，EXPERIMENTAL] → 蓝牙 OBEX 认证支持（Bluetooth OBEX Authentication support）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBEX_AUTH`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OBEX_AUTH)、[`CONFIG_BT_GOEP`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_GOEP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_OBSERVER"></a>

## 330.12 `CONFIG_BT_OBSERVER`

**提示（Prompt）**：观察者角色支持（Observer Role support）

**说明（Help）**

选择此项以支持低功耗蓝牙观察者角色（LE Observer role）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_CENTRAL
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)。

<a id="CONFIG_BT_OEBX_RSP_CODE_TO_STR"></a>

## 330.13 `CONFIG_BT_OEBX_RSP_CODE_TO_STR`

**提示（Prompt）**：以字符串打印 OBEX 响应码（OBEX response codes as strings）

**说明（Help）**

启用以字符串形式打印 OBEX 响应码（response codes）的功能。详情参见 `bt_obex_rsp_code_to_str()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GOEP && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:743`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L743)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → 蓝牙通用对象交换配置文件（Bluetooth GOEP Profile）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_GOEP`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_GOEP)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_OOB_DATA_FIXED"></a>

## 330.14 `CONFIG_BT_OOB_DATA_FIXED`

**提示（Prompt）**：LESC 带外配对使用固定随机数（fixed random number for LESC OOB pairing）

**说明（Help）**

启用后，应用可使用由固定随机数（random number）和确认值（confirm value）组成的带外数据（OOB data），执行低功耗安全连接（LESC）配对。警告：此选项在映像中保存硬编码的带外值。强烈不建议在生产环境使用此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TESTING && CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:778`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L778)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_TESTING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TESTING)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_OTS"></a>

## 330.15 `CONFIG_BT_OTS`

**提示（Prompt）**：对象传输服务（Object Transfer Service，OTS）[实验性，EXPERIMENTAL]

**说明（Help）**

启用对象传输服务（Object Transfer Service）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_L2CAP_DYNAMIC_CHANNEL
CONFIG_BT_GATT_DYNAMIC_DB
CONFIG_BT_SMP
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ots/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ots/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_L2CAP_DYNAMIC_CHANNEL`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_L2CAP_DYNAMIC_CHANNEL)、[`CONFIG_BT_GATT_DYNAMIC_DB`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_DYNAMIC_DB)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_OTS_CLIENT"></a>

## 330.16 `CONFIG_BT_OTS_CLIENT`

**提示（Prompt）**：对象传输服务客户端（Object Transfer Service Client）[实验性，EXPERIMENTAL]

**说明（Help）**

启用对象传输服务客户端（Object Transfer Service Client）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_L2CAP_DYNAMIC_CHANNEL
CONFIG_BT_GATT_CLIENT
CONFIG_BT_GATT_AUTO_DISCOVER_CCC
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ots/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ots/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_L2CAP_DYNAMIC_CHANNEL`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_L2CAP_DYNAMIC_CHANNEL)、[`CONFIG_BT_GATT_CLIENT`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_CLIENT)、[`CONFIG_BT_GATT_AUTO_DISCOVER_CCC`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_AUTO_DISCOVER_CCC)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_OTS_DIR_LIST_OBJ"></a>

## 330.17 `CONFIG_BT_OTS_DIR_LIST_OBJ`

**提示（Prompt）**：目录列表对象（Directory Listing Object）

**说明（Help）**

启用目录列表对象（Directory Listing Object），它包含所有其他对象的全部元数据，便于向客户端公开。启用后会占用 `BT_OTS_MAX_OBJ_CNT` 指定数量中的一个对象名额。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OTS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ots/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ots/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → 对象传输服务（Object Transfer Service，OTS）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_OTS_DIR_LIST_OBJ_NAME"></a>

## 330.18 `CONFIG_BT_OTS_DIR_LIST_OBJ_NAME`

**提示（Prompt）**：目录列表对象的对象名称（object name of the Directory Listing Object）

**说明（Help）**

客户端读取目录列表对象（Directory Listing Object）时获得的名称。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OTS_DIR_LIST_OBJ && CONFIG_BT_OTS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
"Directory"
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ots/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ots/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → 对象传输服务（Object Transfer Service，OTS）[实验性，EXPERIMENTAL] → 目录列表对象（Directory Listing Object）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS_DIR_LIST_OBJ`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS_DIR_LIST_OBJ)、[`CONFIG_BT_OTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_OTS_L2CAP_CHAN_RX_MTU"></a>

## 330.19 `CONFIG_BT_OTS_L2CAP_CHAN_RX_MTU`

**提示（Prompt）**：对象传输信道接收 MTU 大小（RX MTU for Object Transfer Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_OTS || CONFIG_BT_OTS_CLIENT) && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_BUF_ACL_RX_SIZE
```

**取值范围（Ranges）**

```text
[21, CONFIG_BT_BUF_ACL_RX_SIZE]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ots/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ots/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS)、[`CONFIG_BT_OTS_CLIENT`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS_CLIENT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BUF_ACL_RX_SIZE`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BUF_ACL_RX_SIZE)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_OTS_L2CAP_CHAN_TX_MTU"></a>

## 330.20 `CONFIG_BT_OTS_L2CAP_CHAN_TX_MTU`

**提示（Prompt）**：对象传输信道发送 MTU 大小（TX MTU for Object Transfer Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_OTS || CONFIG_BT_OTS_CLIENT) && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[21, 65533]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ots/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ots/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS)、[`CONFIG_BT_OTS_CLIENT`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS_CLIENT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_OTS_MAX_INST_CNT"></a>

## 330.21 `CONFIG_BT_OTS_MAX_INST_CNT`

**提示（Prompt）**：可用对象传输服务实例最大数量（available OTS instances）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OTS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 1] if !CONFIG_BT_OTS_SECONDARY_SVC
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ots/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ots/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → 对象传输服务（Object Transfer Service，OTS）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_OTS_SECONDARY_SVC`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS_SECONDARY_SVC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_OTS_MAX_OBJ_CNT"></a>

## 330.22 `CONFIG_BT_OTS_MAX_OBJ_CNT`

**提示（Prompt）**：每个服务实例可存储的最大对象数量（objects per service instance）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_OTS || CONFIG_BT_OTS_CLIENT) && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 281474976710400]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ots/Kconfig:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ots/Kconfig#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS)、[`CONFIG_BT_OTS_CLIENT`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS_CLIENT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_OTS_OACP_CHECKSUM_SUPPORT"></a>

## 330.23 `CONFIG_BT_OTS_OACP_CHECKSUM_SUPPORT`

**提示（Prompt）**：支持对象操作控制点计算校验和操作（OACP Calculate Checksum）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OTS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**弱选择（Implies）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ots/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ots/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → 对象传输服务（Object Transfer Service，OTS）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_OTS_OACP_CREATE_SUPPORT"></a>

## 330.24 `CONFIG_BT_OTS_OACP_CREATE_SUPPORT`

**提示（Prompt）**：支持对象操作控制点创建操作（OACP Create Operation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OTS_OACP_WRITE_SUPPORT && CONFIG_BT_OTS_OBJ_NAME_WRITE_SUPPORT && CONFIG_BT_OTS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ots/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ots/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → 对象传输服务（Object Transfer Service，OTS）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS_OACP_WRITE_SUPPORT`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS_OACP_WRITE_SUPPORT)、[`CONFIG_BT_OTS_OBJ_NAME_WRITE_SUPPORT`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS_OBJ_NAME_WRITE_SUPPORT)、[`CONFIG_BT_OTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_OTS_OACP_DELETE_SUPPORT"></a>

## 330.25 `CONFIG_BT_OTS_OACP_DELETE_SUPPORT`

**提示（Prompt）**：支持对象操作控制点删除操作（OACP Delete Operation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OTS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ots/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ots/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → 对象传输服务（Object Transfer Service，OTS）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_OTS_OACP_PATCH_SUPPORT"></a>

## 330.26 `CONFIG_BT_OTS_OACP_PATCH_SUPPORT`

**提示（Prompt）**：支持对象补丁更新（patching of objects）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OTS_OACP_WRITE_SUPPORT && CONFIG_BT_OTS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ots/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ots/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → 对象传输服务（Object Transfer Service，OTS）[实验性，EXPERIMENTAL] → 支持对象操作控制点写操作（OACP Write Operation）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS_OACP_WRITE_SUPPORT`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS_OACP_WRITE_SUPPORT)、[`CONFIG_BT_OTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_OTS_OACP_READ_SUPPORT"></a>

## 330.27 `CONFIG_BT_OTS_OACP_READ_SUPPORT`

**提示（Prompt）**：支持对象操作控制点读操作（OACP Read Operation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OTS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ots/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ots/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → 对象传输服务（Object Transfer Service，OTS）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_OTS_OACP_WRITE_SUPPORT"></a>

## 330.28 `CONFIG_BT_OTS_OACP_WRITE_SUPPORT`

**提示（Prompt）**：支持对象操作控制点写操作（OACP Write Operation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OTS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ots/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ots/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → 对象传输服务（Object Transfer Service，OTS）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_OTS_OBJ_MAX_NAME_LEN"></a>

## 330.29 `CONFIG_BT_OTS_OBJ_MAX_NAME_LEN`

**提示（Prompt）**：对象名称最大长度（Maximum object name length）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_OTS || CONFIG_BT_OTS_CLIENT) && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
120
```

**取值范围（Ranges）**

```text
[1, 120]
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ots/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ots/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services）

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS)、[`CONFIG_BT_OTS_CLIENT`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS_CLIENT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_OTS_OBJ_NAME_WRITE_SUPPORT"></a>

## 330.30 `CONFIG_BT_OTS_OBJ_NAME_WRITE_SUPPORT`

**提示（Prompt）**：支持对象名称写入（object name write）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OTS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ots/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ots/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → 对象传输服务（Object Transfer Service，OTS）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_OTS_OLCP_GO_TO_SUPPORT"></a>

## 330.31 `CONFIG_BT_OTS_OLCP_GO_TO_SUPPORT`

**提示（Prompt）**：支持对象列表控制点跳转操作（OLCP Go To Operation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OTS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ots/Kconfig:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ots/Kconfig#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → 对象传输服务（Object Transfer Service，OTS）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_OTS_SECONDARY_SVC"></a>

## 330.32 `CONFIG_BT_OTS_SECONDARY_SVC`

**提示（Prompt）**：将对象传输服务注册为次服务（Register OTS as Secondary Service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OTS && CONFIG_BT_CONN && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../services/ots/Kconfig:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../services/ots/Kconfig#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → GATT 服务（GATT Services） → 对象传输服务（Object Transfer Service，OTS）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_OTS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_PACS_SUPPORTED_CONTEXT_NOTIFIABLE"></a>

## 330.33 `CONFIG_BT_PACS_SUPPORTED_CONTEXT_NOTIFIABLE`

**提示（Prompt）**：支持的音频上下文通知支持（Supported Audio Context Notifiable Support）

**说明（Help）**

允许在“支持的音频上下文”特征（Supported Audio Contexts Characteristic）发生变化时通知客户端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PACS && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.pacs:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.pacs#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 已发布音频能力选项（Published Audio Capabilities，PAC options）

**配置项引用（Symbol References）**：[`CONFIG_BT_PACS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PACS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_PACS`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_PAC_SNK"></a>

## 330.34 `CONFIG_BT_PAC_SNK`

**提示（Prompt）**：接收端 PAC 特征支持（Sink PAC Characteristic Support）

**说明（Help）**

启用接收端已发布音频能力（Sink Published Audio Capabilities）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_DYNAMIC_DB && CONFIG_BT_SMP && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_BAP_UNICAST_SERVER
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.pacs:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.pacs#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 已发布音频能力选项（Published Audio Capabilities，PAC options）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_DYNAMIC_DB`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_DYNAMIC_DB)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BAP_UNICAST_SERVER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAP_UNICAST_SERVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_PAC_SNK_LOC"></a>

## 330.35 `CONFIG_BT_PAC_SNK_LOC`

**提示（Prompt）**：接收端 PAC 位置支持（Sink PAC Location Support）

**说明（Help）**

启用接收端 PAC 位置特征（Sink PAC Location Characteristic）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PAC_SNK && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.pacs:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.pacs#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 已发布音频能力选项（Published Audio Capabilities，PAC options） → 接收端 PAC 特征支持（Sink PAC Characteristic Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_PAC_SNK`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PAC_SNK)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_PAC_SNK_LOC_NOTIFIABLE"></a>

## 330.36 `CONFIG_BT_PAC_SNK_LOC_NOTIFIABLE`

**提示（Prompt）**：接收端音频位置通知支持（Sink Audio Location Notifiable Support）

**说明（Help）**

允许在接收端音频位置特征（Sink Audio Location Characteristic）变化时通知客户端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PAC_SNK_LOC && CONFIG_BT_PAC_SNK && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.pacs:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.pacs#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 已发布音频能力选项（Published Audio Capabilities，PAC options） → 接收端 PAC 特征支持（Sink PAC Characteristic Support） → 接收端 PAC 位置支持（Sink PAC Location Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_PAC_SNK_LOC`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PAC_SNK_LOC)、[`CONFIG_BT_PAC_SNK`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PAC_SNK)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_PAC_SNK_LOC_WRITEABLE"></a>

## 330.37 `CONFIG_BT_PAC_SNK_LOC_WRITEABLE`

**提示（Prompt）**：接收端 PAC 位置可写支持（Sink PAC Location Writable Support）

**说明（Help）**

允许客户端写入接收端 PAC 位置特征（Sink PAC Location Characteristic）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PAC_SNK_LOC && CONFIG_BT_PAC_SNK && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.pacs:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.pacs#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 已发布音频能力选项（Published Audio Capabilities，PAC options） → 接收端 PAC 特征支持（Sink PAC Characteristic Support） → 接收端 PAC 位置支持（Sink PAC Location Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_PAC_SNK_LOC`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PAC_SNK_LOC)、[`CONFIG_BT_PAC_SNK`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PAC_SNK)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_PAC_SNK_NOTIFIABLE"></a>

## 330.38 `CONFIG_BT_PAC_SNK_NOTIFIABLE`

**提示（Prompt）**：接收端 PAC 通知支持（Sink PAC Notifiable Support）

**说明（Help）**

允许在接收端 PAC 特征（Sink PAC Characteristic）变化时通知客户端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PAC_SNK && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.pacs:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.pacs#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 已发布音频能力选项（Published Audio Capabilities，PAC options） → 接收端 PAC 特征支持（Sink PAC Characteristic Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_PAC_SNK`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PAC_SNK)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_PAC_SRC"></a>

## 330.39 `CONFIG_BT_PAC_SRC`

**提示（Prompt）**：发送端 PAC 特征支持（Source PAC Characteristic Support）

**说明（Help）**

启用发送端已发布音频能力（Source Published Audio Capabilities）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GATT_DYNAMIC_DB && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_BAP_UNICAST_SERVER
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.pacs:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.pacs#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 已发布音频能力选项（Published Audio Capabilities，PAC options）

**配置项引用（Symbol References）**：[`CONFIG_BT_GATT_DYNAMIC_DB`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GATT_DYNAMIC_DB)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BAP_UNICAST_SERVER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BAP_UNICAST_SERVER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_PAC_SRC_LOC"></a>

## 330.40 `CONFIG_BT_PAC_SRC_LOC`

**提示（Prompt）**：发送端 PAC 位置支持（Source PAC Location Support）

**说明（Help）**

启用发送端 PAC 位置特征（Source PAC Location Characteristic）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PAC_SRC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.pacs:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.pacs#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 已发布音频能力选项（Published Audio Capabilities，PAC options） → 发送端 PAC 特征支持（Source PAC Characteristic Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_PAC_SRC`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PAC_SRC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_PAC_SRC_LOC_NOTIFIABLE"></a>

## 330.41 `CONFIG_BT_PAC_SRC_LOC_NOTIFIABLE`

**提示（Prompt）**：发送端音频位置通知支持（Source Audio Location Notifiable Support）

**说明（Help）**

允许在发送端音频位置特征（Source Audio Location Characteristic）变化时通知客户端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PAC_SRC_LOC && CONFIG_BT_PAC_SRC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.pacs:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.pacs#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 已发布音频能力选项（Published Audio Capabilities，PAC options） → 发送端 PAC 特征支持（Source PAC Characteristic Support） → 发送端 PAC 位置支持（Source PAC Location Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_PAC_SRC_LOC`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PAC_SRC_LOC)、[`CONFIG_BT_PAC_SRC`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PAC_SRC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_PAC_SRC_LOC_WRITEABLE"></a>

## 330.42 `CONFIG_BT_PAC_SRC_LOC_WRITEABLE`

**提示（Prompt）**：发送端 PAC 位置可写支持（Source PAC Location Writable Support）

**说明（Help）**

允许客户端写入发送端 PAC 位置特征（Source PAC Location Characteristic）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PAC_SRC_LOC && CONFIG_BT_PAC_SRC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.pacs:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.pacs#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 已发布音频能力选项（Published Audio Capabilities，PAC options） → 发送端 PAC 特征支持（Source PAC Characteristic Support） → 发送端 PAC 位置支持（Source PAC Location Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_PAC_SRC_LOC`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PAC_SRC_LOC)、[`CONFIG_BT_PAC_SRC`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PAC_SRC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_PAC_SRC_NOTIFIABLE"></a>

## 330.43 `CONFIG_BT_PAC_SRC_NOTIFIABLE`

**提示（Prompt）**：发送端 PAC 通知支持（Source PAC Notifiable Support）

**说明（Help）**

允许在发送端 PAC 特征（Source PAC Characteristic）变化时通知客户端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PAC_SRC && CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.pacs:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.pacs#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support） → 已发布音频能力选项（Published Audio Capabilities，PAC options） → 发送端 PAC 特征支持（Source PAC Characteristic Support）

**配置项引用（Symbol References）**：[`CONFIG_BT_PAC_SRC`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PAC_SRC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_PAGE_TIMEOUT"></a>

## 330.44 `CONFIG_BT_PAGE_TIMEOUT`

**提示（Prompt）**：蓝牙寻呼超时（Bluetooth Page Timeout）

**说明（Help）**

设置寻呼超时（page timeout）值，按 `(N * 0.625) ms` 选择。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0x2000
```

**取值范围（Ranges）**

```text
[0x0001, 0xffff]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:676`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L676)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PASSKEY_KEYPRESS"></a>

## 330.45 `CONFIG_BT_PASSKEY_KEYPRESS`

**提示（Prompt）**：通行密钥按键通知支持（Passkey Keypress Notification）[实验性，EXPERIMENTAL]

**说明（Help）**

允许在配对的通行密钥输入（Passkey Entry）期间，接收和发送按键通知（Keypress Notifications）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:451`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L451)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_PATH_LOSS_MONITORING"></a>

## 330.46 `CONFIG_BT_PATH_LOSS_MONITORING`

**提示（Prompt）**：低功耗蓝牙路径损耗监测（LE Path Loss Monitoring）

**说明（Help）**

启用低功耗蓝牙路径损耗监测（LE Path Loss Monitoring）功能支持，其定义见蓝牙核心规范（Bluetooth Core specification）Version 5.4，Vol 6, Part B, Section 4.6.32。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_LE_PATH_LOSS_MONITORING_SUPPORT) && CONFIG_BT_CONN && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L211)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_LE_PATH_LOSS_MONITORING_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_LE_PATH_LOSS_MONITORING_SUPPORT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_LE_PATH_LOSS_MONITORING_SUPPORT`。

<a id="CONFIG_BT_PBAP"></a>

## 330.47 `CONFIG_BT_PBAP`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用电话簿访问配置文件（PBAP profile）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_GOEP
CONFIG_BT_OBEX_AUTH
```

**被选择（Selected by）**

```text
CONFIG_BT_PBAP_PSE
CONFIG_BT_PBAP_PCE
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:776`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L776)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_GOEP`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_GOEP)、[`CONFIG_BT_OBEX_AUTH`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OBEX_AUTH)、[`CONFIG_BT_PBAP_PSE`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBAP_PSE)、[`CONFIG_BT_PBAP_PCE`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBAP_PCE)。

<a id="CONFIG_BT_PBAP_PCE"></a>

## 330.48 `CONFIG_BT_PBAP_PCE`

**提示（Prompt）**：蓝牙电话簿访问配置文件客户端（Bluetooth PBAP Profile Client）[实验性，EXPERIMENTAL]

**说明（Help）**

启用电话簿客户端设备（Phone Book Client Equipment，PCE）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_PBAP
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:789`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L789)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_PBAP`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBAP)。

<a id="CONFIG_BT_PBAP_PSE"></a>

## 330.49 `CONFIG_BT_PBAP_PSE`

**提示（Prompt）**：蓝牙电话簿访问配置文件服务器（Bluetooth PBAP Profile Server）[实验性，EXPERIMENTAL]

**说明（Help）**

启用电话簿服务器设备（Phone Book Server Equipment，PSE）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_PBAP
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:783`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L783)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_PBAP`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBAP)。

<a id="CONFIG_BT_PBAP_PSE_BROWSING"></a>

## 330.50 `CONFIG_BT_PBAP_PSE_BROWSING`

**提示（Prompt）**：PBAP 服务器设备浏览功能（PBAP PSE Browsing feature）

**说明（Help）**

在 PSE 上启用电话簿浏览（phone book browsing）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PBAP_PSE && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:803`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L803)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_PSE`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBAP_PSE)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PBAP_PSE_CONTACT_REFERENCING"></a>

## 330.51 `CONFIG_BT_PBAP_PSE_CONTACT_REFERENCING`

**提示（Prompt）**：PBAP 服务器设备联系人引用功能（PBAP PSE Contact Referencing feature）

**说明（Help）**

在 PSE 上启用联系人引用处理（contact reference handling）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PBAP_PSE && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:845`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L845)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_PSE`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBAP_PSE)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PBAP_PSE_DATABASE_IDENTIFIER"></a>

## 330.52 `CONFIG_BT_PBAP_PSE_DATABASE_IDENTIFIER`

**提示（Prompt）**：PBAP 服务器设备数据库标识符功能（PBAP PSE Database Identifier feature）

**说明（Help）**

在 PSE 上启用数据库变更跟踪（database change tracking）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PBAP_PSE && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:809`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L809)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_PSE`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBAP_PSE)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PBAP_PSE_DEFAULT_CONTACT_IMAGE"></a>

## 330.53 `CONFIG_BT_PBAP_PSE_DEFAULT_CONTACT_IMAGE`

**提示（Prompt）**：PBAP 服务器设备默认联系人图像功能（PBAP PSE Default Contact Image feature）

**说明（Help）**

在 PSE 上启用默认联系人图像（default contact images）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PBAP_PSE && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:851`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L851)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_PSE`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBAP_PSE)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PBAP_PSE_DOWNLOAD"></a>

## 330.54 `CONFIG_BT_PBAP_PSE_DOWNLOAD`

**提示（Prompt）**：PBAP 服务器设备下载功能（PBAP PSE Download feature）

**说明（Help）**

在 PSE 上启用电话簿下载（phone book download）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PBAP_PSE && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:797`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L797)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_PSE`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBAP_PSE)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PBAP_PSE_ENHANCED_MISSED_CALLS"></a>

## 330.55 `CONFIG_BT_PBAP_PSE_ENHANCED_MISSED_CALLS`

**提示（Prompt）**：PBAP 服务器设备增强未接来电功能（PBAP PSE Enhanced Missed Calls feature）

**说明（Help）**

在 PSE 上启用增强未接来电处理（enhanced missed call handling）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PBAP_PSE && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:827`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L827)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_PSE`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBAP_PSE)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PBAP_PSE_FOLDER_VERSION_COUNTERS"></a>

## 330.56 `CONFIG_BT_PBAP_PSE_FOLDER_VERSION_COUNTERS`

**提示（Prompt）**：PBAP 服务器设备文件夹版本计数器功能（PBAP PSE Folder Version Counters feature）

**说明（Help）**

在 PSE 上启用文件夹版本跟踪（folder version tracking）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PBAP_PSE && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:815`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L815)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_PSE`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBAP_PSE)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PBAP_PSE_REPOSITORY_FAVORITES"></a>

## 330.57 `CONFIG_BT_PBAP_PSE_REPOSITORY_FAVORITES`

**提示（Prompt）**：PBAP 服务器设备收藏夹存储库（PBAP PSE Favorites Repository）

**说明（Help）**

在 PSE 上启用收藏夹存储库（favorites repository）支持，包括收藏联系人（favorite contacts）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PBAP_PSE && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:878`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L878)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_PSE`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBAP_PSE)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PBAP_PSE_REPOSITORY_LOCAL_PHONE_BOOK"></a>

## 330.58 `CONFIG_BT_PBAP_PSE_REPOSITORY_LOCAL_PHONE_BOOK`

**提示（Prompt）**：PBAP 服务器设备本地电话簿存储库（PBAP PSE Local phonebook Repository）

**说明（Help）**

在 PSE 上启用本地电话簿存储库（local phone book repository）支持，包括设备本地内存中保存的联系人。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PBAP_PSE && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:857`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L857)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_PSE`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBAP_PSE)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PBAP_PSE_REPOSITORY_SIM"></a>

## 330.59 `CONFIG_BT_PBAP_PSE_REPOSITORY_SIM`

**提示（Prompt）**：PBAP 服务器设备 SIM 存储库（PBAP PSE SIM Repository）

**说明（Help）**

在 PSE 上启用 SIM 卡电话簿存储库（SIM card phone book repository）支持，包括 SIM 卡上保存的联系人。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PBAP_PSE && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:864`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L864)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_PSE`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBAP_PSE)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PBAP_PSE_REPOSITORY_SPEED_DIAL"></a>

## 330.60 `CONFIG_BT_PBAP_PSE_REPOSITORY_SPEED_DIAL`

**提示（Prompt）**：PBAP 服务器设备快速拨号存储库（PBAP PSE Speed Dial Repository）

**说明（Help）**

在 PSE 上启用快速拨号存储库（speed dial repository）支持，包括快速拨号条目。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PBAP_PSE && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:871`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L871)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_PSE`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBAP_PSE)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PBAP_PSE_UCI_VCARD_PROPERTY"></a>

## 330.61 `CONFIG_BT_PBAP_PSE_UCI_VCARD_PROPERTY`

**提示（Prompt）**：PBAP 服务器设备 UCI vCard 属性功能（PBAP PSE UCI vCard Property feature）

**说明（Help）**

在 PSE 上启用唯一联系人标识符（Unique Contact Identifier）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PBAP_PSE && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:833`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L833)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_PSE`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBAP_PSE)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PBAP_PSE_UID_VCARD_PROPERTY"></a>

## 330.62 `CONFIG_BT_PBAP_PSE_UID_VCARD_PROPERTY`

**提示（Prompt）**：PBAP 服务器设备 UID vCard 属性功能（PBAP PSE UID vCard Property feature）

**说明（Help）**

在 PSE 上启用 vCard UID 属性（property）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PBAP_PSE && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:839`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L839)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_PSE`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBAP_PSE)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PBAP_PSE_VCARD_SELECTOR"></a>

## 330.63 `CONFIG_BT_PBAP_PSE_VCARD_SELECTOR`

**提示（Prompt）**：PBAP 服务器设备 vCard 选择器功能（PBAP PSE vCard Selector feature）

**说明（Help）**

在电话簿服务器设备（PSE）上启用 vCard 属性过滤（property filtering）功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PBAP_PSE && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:821`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L821)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_PBAP_PSE`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PBAP_PSE)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PBP"></a>

## 330.64 `CONFIG_BT_PBP`

**提示（Prompt）**：公共广播配置文件（Public Broadcast Profile）

**说明（Help）**

启用后将启用公共广播配置文件（PBP）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_AUDIO && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/../audio/Kconfig.pbp:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/../audio/Kconfig.pbp#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 蓝牙音频支持（Bluetooth Audio support）

**配置项引用（Symbol References）**：[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_PERIPHERAL"></a>

## 330.65 `CONFIG_BT_PERIPHERAL`

原库同名定义共 2 条；本项为数据库第 3118 条记录，各定义分别保留。

**提示（Prompt）**：外设角色支持（Peripheral Role support）

**说明（Help）**

选择此项以支持低功耗蓝牙外设角色（LE Peripheral role）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_HCI_RAW
```

**主动选择（Selects）**

```text
CONFIG_BT_BROADCASTER
CONFIG_BT_CONN
```

**被选择（Selected by）**

```text
CONFIG_BT_CLASSIC
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI_RAW)、[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)。

<a id="CONFIG_BT_PERIPHERAL_PREF_LATENCY"></a>

## 330.66 `CONFIG_BT_PERIPHERAL_PREF_LATENCY`

**提示（Prompt）**：外设首选外设延迟，以连接间隔数表示（preferred peripheral latency in Connection Intervals）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GAP_PERIPHERAL_PREF_PARAMS && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 499] if !CONFIG_BT_CONN_PARAM_ANY
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:257`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L257)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options） → 配置外设首选连接参数（Configure peripheral preferred connection parameters）

**配置项引用（Symbol References）**：[`CONFIG_BT_GAP_PERIPHERAL_PREF_PARAMS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GAP_PERIPHERAL_PREF_PARAMS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CONN_PARAM_ANY`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN_PARAM_ANY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_PERIPHERAL_PREF_MAX_INT"></a>

## 330.67 `CONFIG_BT_PERIPHERAL_PREF_MAX_INT`

**提示（Prompt）**：外设首选最大连接间隔，以 1.25ms 为单位（preferred maximum connection interval）

**说明（Help）**

`3200` 到 `65534` 范围无效；`65535` 表示不指定具体值（no specific value）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GAP_PERIPHERAL_PREF_PARAMS && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
40
```

**取值范围（Ranges）**

```text
[6, 65535] if !CONFIG_BT_CONN_PARAM_ANY
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:250`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L250)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options） → 配置外设首选连接参数（Configure peripheral preferred connection parameters）

**配置项引用（Symbol References）**：[`CONFIG_BT_GAP_PERIPHERAL_PREF_PARAMS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GAP_PERIPHERAL_PREF_PARAMS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CONN_PARAM_ANY`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN_PARAM_ANY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_PERIPHERAL_PREF_MIN_INT"></a>

## 330.68 `CONFIG_BT_PERIPHERAL_PREF_MIN_INT`

**提示（Prompt）**：外设首选最小连接间隔，以 1.25ms 为单位（preferred minimum connection interval）

**说明（Help）**

`3200` 到 `65534` 范围无效；`65535` 表示不指定具体值（no specific value）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GAP_PERIPHERAL_PREF_PARAMS && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
24
```

**取值范围（Ranges）**

```text
[6, 65535] if !CONFIG_BT_CONN_PARAM_ANY
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:243`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L243)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options） → 配置外设首选连接参数（Configure peripheral preferred connection parameters）

**配置项引用（Symbol References）**：[`CONFIG_BT_GAP_PERIPHERAL_PREF_PARAMS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GAP_PERIPHERAL_PREF_PARAMS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CONN_PARAM_ANY`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN_PARAM_ANY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_PERIPHERAL_PREF_TIMEOUT"></a>

## 330.69 `CONFIG_BT_PERIPHERAL_PREF_TIMEOUT`

**提示（Prompt）**：外设首选监督超时，以 10ms 为单位（preferred supervision timeout）

**说明（Help）**

用户负责提供满足最小值要求的有效超时：以毫秒表示时，必须大于 `(1+ Conn_Latency) * Conn_Interval_Max * 2`，其中 `Conn_Interval_Max` 也以毫秒表示。`3200` 到 `65534` 范围无效；`65535` 表示不指定具体值（no specific value）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_GAP_PERIPHERAL_PREF_PARAMS && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
42
```

**取值范围（Ranges）**

```text
[10, 65535] if !CONFIG_BT_CONN_PARAM_ANY
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig.gatt:262`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig.gatt#L262)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → ATT 和 GATT 选项（ATT and GATT Options） → 配置外设首选连接参数（Configure peripheral preferred connection parameters）

**配置项引用（Symbol References）**：[`CONFIG_BT_GAP_PERIPHERAL_PREF_PARAMS`](P325_subsys_bluetooth_配置项参考_6.md#CONFIG_BT_GAP_PERIPHERAL_PREF_PARAMS)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_CONN_PARAM_ANY`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN_PARAM_ANY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_PER_ADV"></a>

## 330.70 `CONFIG_BT_PER_ADV`

**提示（Prompt）**：周期性广播与扫描支持（Periodic Advertising and Scanning support）

**说明（Help）**

启用周期性广播 API（Periodic Advertising API）支持，使设备能够以确定的时间间隔周期性发送广播数据。扫描器可同步到这些周期性广播，从而周期性获取数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_EXT_ADV && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_ISO_BROADCASTER
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig.adv:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig.adv#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 扩展广播与扫描支持（Extended Advertising and Scanning support）

**配置项引用（Symbol References）**：[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_BROADCASTER`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_ISO_BROADCASTER)。

<a id="CONFIG_BT_PER_ADV_RSP"></a>

## 330.71 `CONFIG_BT_PER_ADV_RSP`

**提示（Prompt）**：带响应周期性广播支持（Periodic Advertising with Responses support）

**说明（Help）**

启用带响应周期性广播 API（Periodic Advertising with Responses API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PER_ADV && CONFIG_BT_EXT_ADV && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig.adv:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig.adv#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 扩展广播与扫描支持（Extended Advertising and Scanning support） → 周期性广播与扫描支持（Periodic Advertising and Scanning support）

**配置项引用（Symbol References）**：[`CONFIG_BT_PER_ADV`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PER_ADV)、[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PER_ADV_RSP_REASSEMBLY"></a>

## 330.72 `CONFIG_BT_PER_ADV_RSP_REASSEMBLY`

**提示（Prompt）**：重组已分片的 PAwR 响应报告（Reassembly of fragmented PAwR response reports）

**说明（Help）**

重组控制器分散在多个 HCI 事件中交付的带响应周期性广播（PAwR）响应报告，代价是每个广播集合需要一个重组缓冲区（reassembly buffer）。禁用时，已分片响应会被丢弃。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PER_ADV_RSP && CONFIG_BT_EXT_ADV && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig.adv:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig.adv#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 扩展广播与扫描支持（Extended Advertising and Scanning support） → 周期性广播与扫描支持（Periodic Advertising and Scanning support） → 带响应周期性广播支持（Periodic Advertising with Responses support）

**配置项引用（Symbol References）**：[`CONFIG_BT_PER_ADV_RSP`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PER_ADV_RSP)、[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PER_ADV_SYNC"></a>

## 330.73 `CONFIG_BT_PER_ADV_SYNC`

**提示（Prompt）**：周期性广播同步支持（Periodic advertising sync support）

**说明（Help）**

启用周期性广播同步 API（Periodic Advertising Sync API）支持。与周期性广播者同步后，设备可采用无连接方式，周期性并按确定时序从该设备接收数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBSERVER && CONFIG_BT_EXT_ADV && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_ISO_SYNC_RECEIVER
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig.adv:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig.adv#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 扩展广播与扫描支持（Extended Advertising and Scanning support）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OBSERVER)、[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_SYNC_RECEIVER`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_ISO_SYNC_RECEIVER)。

<a id="CONFIG_BT_PER_ADV_SYNC_BUF_SIZE"></a>

## 330.74 `CONFIG_BT_PER_ADV_SYNC_BUF_SIZE`

**提示（Prompt）**：周期性广播报告最大大小（Maximum periodic advertising report size）

**说明（Help）**

已分片周期性广播报告（fragmented periodic advertising report）的最大大小。如果控制器提供的报告经过分片且超过此缓冲区大小，数据会被丢弃。未分片报告按接收到的内容直接转发。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PER_ADV_SYNC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 1650]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:1096`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L1096)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_PER_ADV_SYNC`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PER_ADV_SYNC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PER_ADV_SYNC_MAX"></a>

## 330.75 `CONFIG_BT_PER_ADV_SYNC_MAX`

**提示（Prompt）**：最大同时周期性广播同步数量（simultaneous periodic advertising syncs）

**说明（Help）**

支持同时存在的周期性广播同步（periodic advertising syncs）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PER_ADV_SYNC && CONFIG_BT_EXT_ADV && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig.adv:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig.adv#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 扩展广播与扫描支持（Extended Advertising and Scanning support）

**配置项引用（Symbol References）**：[`CONFIG_BT_PER_ADV_SYNC`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PER_ADV_SYNC)、[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PER_ADV_SYNC_RSP"></a>

## 330.76 `CONFIG_BT_PER_ADV_SYNC_RSP`

**提示（Prompt）**：带响应周期性广播同步支持（Periodic Advertising with Responses sync support）

**说明（Help）**

启用带响应周期性广播同步 API（Periodic Advertising with Responses Sync API）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_OBSERVER && CONFIG_BT_EXT_ADV && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig.adv:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig.adv#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 扩展广播与扫描支持（Extended Advertising and Scanning support）

**配置项引用（Symbol References）**：[`CONFIG_BT_OBSERVER`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OBSERVER)、[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PER_ADV_SYNC_TRANSFER_RECEIVER"></a>

## 330.77 `CONFIG_BT_PER_ADV_SYNC_TRANSFER_RECEIVER`

**提示（Prompt）**：周期性广播同步传输接收方（Periodic Advertising Sync Transfer receiver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PER_ADV_SYNC && CONFIG_BT_CONN && (!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT) && CONFIG_BT_CONN && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L189)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_PER_ADV_SYNC`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PER_ADV_SYNC)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT`。

<a id="CONFIG_BT_PER_ADV_SYNC_TRANSFER_SENDER"></a>

## 330.78 `CONFIG_BT_PER_ADV_SYNC_TRANSFER_SENDER`

**提示（Prompt）**：周期性广播同步传输发送方（Periodic Advertising Sync Transfer sender）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_PER_ADV_SYNC || CONFIG_BT_PER_ADV) && CONFIG_BT_CONN && (!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT) && CONFIG_BT_CONN && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L193)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_PER_ADV_SYNC`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PER_ADV_SYNC)、[`CONFIG_BT_PER_ADV`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PER_ADV)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT`。

<a id="CONFIG_BT_PHY_UPDATE"></a>

## 330.79 `CONFIG_BT_PHY_UPDATE`

**提示（Prompt）**：物理层更新（PHY Update）

**说明（Help）**

启用蓝牙 5.0 物理层更新过程（PHY Update Procedure）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT) && CONFIG_BT_CONN && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L175)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT`。

<a id="CONFIG_BT_POWER_MODE_CONTROL"></a>

## 330.80 `CONFIG_BT_POWER_MODE_CONTROL`

**提示（Prompt）**：蓝牙功耗模式控制，活动／嗅探（Bluetooth Power Mode Control, Active/Sniff）

**说明（Help）**

启用功耗模式控制（power mode control）功能，允许应用控制蓝牙控制器的功耗模式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:698`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L698)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_BT_PRIVACY"></a>

## 330.81 `CONFIG_BT_PRIVACY`

原库同名定义共 2 条；本项为数据库第 3135 条记录，各定义分别保留。

**提示（Prompt）**：设备隐私（Device privacy）

**说明（Help）**

为本地设备启用隐私（privacy），使设备默认使用可解析私有地址（Resolvable Private Addresses，RPAs）。注意：作为定向广播者（directed advertiser）或向定向广播者建立连接，只有控制器也支持隐私时才可行。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:458`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L458)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_PRIVACY_RANDOMIZE_IR"></a>

## 330.82 `CONFIG_BT_PRIVACY_RANDOMIZE_IR`

**提示（Prompt）**：为回退身份随机化身份根（Randomize identity root for fallback identities）

**说明（Help）**

启用后，主机（Host）忽略控制器提供的身份根（identity roots，IR），改用 `bt_rand` 生成身份解析密钥（identity resolving keys，IRK），并保存到设置子系统（settings subsystem）。这可能增加启动时间：硬件随机数生成器（RNG）可能需要时间生成熵，并阻塞蓝牙初始化。

此选项提高隐私性的原因如下。IR 决定身份的 IRK。IRK 既用于生成，也用于解析和识别该身份的私有地址；它是与绑定到该身份的对端共享的秘密。攻击者如果窃取了 IRK，或曾经绑定并保留了 IRK，即使本地后来删除绑定，仍能一直解析由该 IRK 生成的地址。

理想情况下，删除身份也应删除 IRK，从而对之前绑定过的对端重新获得匿名性。但未设置此配置时，并不总能做到。例如，恢复出厂设置即使清空了设置子系统数据，也可能不影响控制器提供的 IR。如果再次使用这些 IR，设备跨越恢复出厂设置后仍可能被跟踪。

要获得最佳隐私性，每个绑定应使用新的 IRK，也就是新的身份。但这样自然也使该身份的广播只能被那一个绑定设备识别。

此设置的具体作用如下：

- 在调用 `bt_enable()` 之后，如果应用在调用 `settings_load()`／`settings_load_subtree("bt")` 前未设置身份，主机会自动尝试从设置子系统加载已保存身份；如果没有，则建立默认身份 `BT_ID_DEFAULT`。
- 如果控制器具有公共地址（`HCI_Read_BD_ADDR`），该地址成为默认身份地址。主机默认尝试通过 Zephyr HCI `Read_Key_Hierarchy_Roots` 从控制器取得该身份的 IR；设置此配置后，改为随机化 IR。
- 如果控制器没有公共地址，主机尝试使用控制器的静态地址信息（Zephyr HCI `Read_Static_Addresses`）作为默认身份来源，为返回的每个条目建立一个身份。设置此配置后，该过程中的 IR 均被随机化。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PRIVACY && CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_SETTINGS
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:468`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L468)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support） → 设备隐私（Device privacy）

**配置项引用（Symbol References）**：[`CONFIG_BT_PRIVACY`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PRIVACY)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_SETTINGS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_SETTINGS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_REMOTE_INFO"></a>

## 330.83 `CONFIG_BT_REMOTE_INFO`

**提示（Prompt）**：应用访问远端信息（Application access to remote information）

**说明（Help）**

允许应用访问协议栈中可用的远端信息（remote information）。连接建立后会获取这些信息，并在可用时通过连接回调 `remote_info_available` 通知应用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:416`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L416)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_REMOTE_VERSION"></a>

## 330.84 `CONFIG_BT_REMOTE_VERSION`

**提示（Prompt）**：允许获取远端版本（Allow fetching of remote version）

**说明（Help）**

启用后，可在控制器与主机中通过 `bt_conn_get_remote_info()` 访问远端版本（remote version），相关字段位于 `bt_conn_remote_info` 结构体中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_HCI_RAW
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI_RAW)。

<a id="CONFIG_BT_RFCOMM"></a>

## 330.85 `CONFIG_BT_RFCOMM`

**提示（Prompt）**：蓝牙 RFCOMM 协议支持（Bluetooth RFCOMM protocol support）[实验性，EXPERIMENTAL]

**说明（Help）**

启用蓝牙 RFCOMM 支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**被选择（Selected by）**

```text
CONFIG_BT_HFP_HF
CONFIG_BT_HFP_AG
CONFIG_BT_GOEP
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_BT_HFP_HF`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_HF)、[`CONFIG_BT_HFP_AG`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HFP_AG)、[`CONFIG_BT_GOEP`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_GOEP)。

<a id="CONFIG_BT_RFCOMM_L2CAP_MTU"></a>

## 330.86 `CONFIG_BT_RFCOMM_L2CAP_MTU`

**提示（Prompt）**：RFCOMM 帧的 L2CAP MTU（L2CAP MTU for RFCOMM frames）

**说明（Help）**

RFCOMM 帧所用 L2CAP PDU 的最大大小。接收 MTU（RX MTU）会被截减，为 L2CAP PDU 头（header）留出空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_RFCOMM && CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_BUF_ACL_RX_SIZE
```

**取值范围（Ranges）**

```text
[23, 32767]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:170`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L170)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL] → 蓝牙 RFCOMM 协议支持（Bluetooth RFCOMM protocol support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_RFCOMM`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_RFCOMM)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BUF_ACL_RX_SIZE`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BUF_ACL_RX_SIZE)。

<a id="CONFIG_BT_RFCOMM_TX_MAX"></a>

## 330.87 `CONFIG_BT_RFCOMM_TX_MAX`

**提示（Prompt）**：RFCOMM 待处理发送缓冲区最大数量（pending TX buffers for RFCOMM）

**说明（Help）**

具有关联发送缓冲区（sending buf）的待处理发送缓冲区（pending TX buffers）最大数量。通常可保留默认值，其值等于协议栈内部池（stack-internal pool）的会话数量（sessions）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_BUF_ACL_TX_COUNT
```

**取值范围（Ranges）**

```text
[CONFIG_BT_BUF_ACL_TX_COUNT, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/host/./classic/Kconfig:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/./classic/Kconfig#L179)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 经典蓝牙选项（Bluetooth Classic Options） → 蓝牙基本速率／增强数据速率支持（Bluetooth BR/EDR support）[实验性，EXPERIMENTAL]

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_BUF_ACL_TX_COUNT`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BUF_ACL_TX_COUNT)。

<a id="CONFIG_BT_RPA_SHARING"></a>

## 330.88 `CONFIG_BT_RPA_SHARING`

**提示（Prompt）**：广播集合之间共享可解析私有地址（Share the Resolvable Private Address）

**说明（Help）**

使关联到同一蓝牙身份（Bluetooth identity）的广播集合在一个轮换周期（rotation period）内使用相同的可解析私有地址（RPA）。RPA 超时后生成新地址，并在下一个轮换周期继续由这些集合共享。禁用时，同一周期内各广播集合生成的 RPA 彼此不同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PRIVACY && CONFIG_BT_EXT_ADV && CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:540`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L540)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support） → 设备隐私（Device privacy）

**配置项引用（Symbol References）**：[`CONFIG_BT_PRIVACY`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PRIVACY)、[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_RPA_TIMEOUT"></a>

## 330.89 `CONFIG_BT_RPA_TIMEOUT`

**提示（Prompt）**：可解析私有地址超时（Resolvable Private Address timeout）

**说明（Help）**

定义可解析私有地址（RPA）的轮换频率，值以秒表示，默认为 `900` 秒，即 `15` 分钟。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PRIVACY && CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
900
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:524`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L524)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support） → 设备隐私（Device privacy）

**配置项引用（Symbol References）**：[`CONFIG_BT_PRIVACY`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PRIVACY)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_RPA_TIMEOUT_DYNAMIC"></a>

## 330.90 `CONFIG_BT_RPA_TIMEOUT_DYNAMIC`

**提示（Prompt）**：支持运行时设置可解析私有地址超时（RPA timeout at runtime）

**说明（Help）**

允许用户通过专用 API 覆盖可解析私有地址（Resolvable Private Address）的默认超时值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PRIVACY && CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:533`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L533)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support） → 设备隐私（Device privacy）

**配置项引用（Symbol References）**：[`CONFIG_BT_PRIVACY`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PRIVACY)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_RX_STACK_SIZE"></a>

## 330.91 `CONFIG_BT_RX_STACK_SIZE`

**提示（Prompt）**：蓝牙工作队列栈大小（Size of the Bluetooth workqueue stack）

**说明（Help）**

蓝牙工作队列（Bluetooth workqueue）的栈大小。主机在该线程中处理接收数据并运行延后工作（deferred work），应用从协议栈内部上下文获得的大多数回调也在此线程执行。默认值足以支持基本操作；若应用回调需要额外栈空间，可增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
768 if CONFIG_BT_HCI_RAW
3092 if CONFIG_BT_MESH_GATT_CLIENT
2800 if CONFIG_BT_MESH_PB_GATT
2600 if CONFIG_BT_MESH
2048 if CONFIG_BT_AUDIO
1200
```

**其他位置的默认值（Other Defaults）**

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
4096 if CONFIG_LIBLC3
```

来源：[`boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/nxp_m2_wifi_bt/Kconfig.defconfig)。

```text
2800 if (CONFIG_BT_SETTINGS || CONFIG_BT_SMP) && !CONFIG_BT_MESH_GATT_CLIENT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_HCI_RAW`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI_RAW)、[`CONFIG_BT_MESH_GATT_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_GATT_CLIENT)、[`CONFIG_BT_MESH_PB_GATT`](P329_subsys_bluetooth_配置项参考_10.md#CONFIG_BT_MESH_PB_GATT)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_LIBLC3`](P236_modules_liblc3_配置项参考.md#CONFIG_LIBLC3)、[`CONFIG_BT_SETTINGS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_SETTINGS)、[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_MESH_GATT_CLIENT`。

<a id="CONFIG_BT_RX_USER_PDU_LEN"></a>

## 330.92 `CONFIG_BT_RX_USER_PDU_LEN`

**提示（Prompt）**：支持的最大专有 PDU 缓冲区长度（Maximum supported proprietary PDU buffer length）

**说明（Help）**

每个专有 PDU（proprietary PDU）的最大数据大小，包括链路层头（link layer header）和有效载荷（payload），不计入 HCI 事件头，因为假定这些 PDU 不通过 HCI 传送。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CTLR_USER_EXT && CONFIG_BT_LL_SW_SPLIT && CONFIG_HAS_BT_CTLR && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[2, 255]
```

**定义位置（Location）**：[`subsys/bluetooth/controller/Kconfig.ll_sw_split:1421`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/controller/Kconfig.ll_sw_split#L1421)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 高级功能（Advanced features） → 控制器中的专有扩展（Proprietary extensions in Controller）

**配置项引用（Symbol References）**：[`CONFIG_BT_CTLR_USER_EXT`](P324_subsys_bluetooth_配置项参考_5.md#CONFIG_BT_CTLR_USER_EXT)、[`CONFIG_BT_LL_SW_SPLIT`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_LL_SW_SPLIT)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`。

<a id="CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL"></a>

## 330.93 `CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL`

**提示（Prompt）**：允许并发扫描与发起连接（concurrent scanning and initiating）

**说明（Help）**

允许扫描与发起连接并行进行，使应用无需停止扫描器即可向对端设备发起连接。如果禁用隐私（privacy），扫描器使用其身份地址（identity address）。此功能仅在使用扩展广播 HCI 命令时可用，以避免使用广播者时性能下降。启用此功能后，不支持带超时的扫描（scanning with a timeout）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CENTRAL && CONFIG_BT_OBSERVER && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_BT_EXT_ADV if CONFIG_BT_BROADCASTER
CONFIG_BT_SCAN_WITH_IDENTITY if !CONFIG_BT_PRIVACY
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:919`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L919)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)、[`CONFIG_BT_OBSERVER`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OBSERVER)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_BROADCASTER`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_BROADCASTER)、[`CONFIG_BT_SCAN_WITH_IDENTITY`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_SCAN_WITH_IDENTITY)、[`CONFIG_BT_PRIVACY`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PRIVACY)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SCAN_EXT_FILTER_POLICY"></a>

## 330.94 `CONFIG_BT_SCAN_EXT_FILTER_POLICY`

**提示（Prompt）**：扩展扫描器过滤策略（Extended scanner filter policies）

**说明（Help）**

启用 `BT_LE_SCAN_OPT_EXT_FILTER_POLICY` 扫描选项支持。扩展扫描器过滤策略（Extended Scanner Filter Policies）允许控制器报告以下定向广播：其目标地址为控制器无法解析的可解析私有地址（RPA），而不是丢弃这些广播。应用因此可发现向本地设备无法解析的身份发送定向广播的对端。

此选项启用 `LE Directed Advertising Report` 事件，以在使用传统扫描命令时报告这些广播；要求控制器支持扩展扫描器过滤策略。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_EXT_SCAN_FP) && CONFIG_BT_OBSERVER && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:888`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L888)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_EXT_SCAN_FP`](P323_subsys_bluetooth_配置项参考_4.md#CONFIG_BT_CTLR_EXT_SCAN_FP)、[`CONFIG_BT_OBSERVER`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OBSERVER)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SCAN_WITH_IDENTITY"></a>

## 330.95 `CONFIG_BT_SCAN_WITH_IDENTITY`

**提示（Prompt）**：使用本地身份地址执行主动扫描（active scanning using local identity address）

**说明（Help）**

如果希望以本地身份地址（local identity address）作为扫描器地址进行主动扫描（active scanning），启用此项。默认情况下，为避免泄露本地身份信息，协议栈始终使用不可解析私有地址（Non-Resolvable Private Address，NRPA）。原文接着指出，不以身份地址扫描时，扫描器会接收针对本地身份的定向广播报告；如果需要此使用场景，应启用本选项。

译注：原文使用 `By not scanning with the identity address`，但前后又要求启用身份地址扫描，表述存在矛盾。此处保留并指出，不替换成推测的行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_BT_PRIVACY && (CONFIG_BT_CENTRAL || CONFIG_BT_OBSERVER) && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**被选择（Selected by）**

```text
CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:907`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L907)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_BT_PRIVACY`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_PRIVACY)、[`CONFIG_BT_CENTRAL`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_CENTRAL)、[`CONFIG_BT_OBSERVER`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OBSERVER)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SCA_UPDATE"></a>

## 330.96 `CONFIG_BT_SCA_UPDATE`

**提示（Prompt）**：睡眠时钟精度更新（Sleep Clock Accuracy Update）

**说明（Help）**

启用蓝牙 5.1 睡眠时钟精度更新过程（Sleep Clock Accuracy Update Procedure）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_HAS_BT_CTLR || CONFIG_BT_CTLR_SCA_UPDATE_SUPPORT) && CONFIG_BT_CONN && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y if CONFIG_BT_ISO_PERIPHERAL || CONFIG_BT_ISO_CENTRAL
```

**定义位置（Location）**：[`subsys/bluetooth/Kconfig:197`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/Kconfig#L197)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth）

**配置项引用（Symbol References）**：[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_SCA_UPDATE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SCA_UPDATE_SUPPORT)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_PERIPHERAL`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_ISO_PERIPHERAL)、[`CONFIG_BT_ISO_CENTRAL`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_ISO_CENTRAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_SCA_UPDATE_SUPPORT`。

<a id="CONFIG_BT_SECURITY_ERR_TO_STR"></a>

## 330.97 `CONFIG_BT_SECURITY_ERR_TO_STR`

**提示（Prompt）**：以字符串打印安全错误码（security error codes as strings）[实验性，EXPERIMENTAL]

**说明（Help）**

启用以字符串形式打印安全错误码（security error codes）的功能。详情参见 `bt_security_err_to_str()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SMP && CONFIG_BT_CONN && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:435`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L435)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 安全管理协议支持（Security Manager Protocol support）

**配置项引用（Symbol References）**：[`CONFIG_BT_SMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SMP)、[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SETTINGS"></a>

## 330.98 `CONFIG_BT_SETTINGS`

**提示（Prompt）**：持久化保存蓝牙状态与配置（Store Bluetooth state and configuration persistently）

**说明（Help）**

选择后，蓝牙协议栈负责在 Flash 中持久化保存并恢复蓝牙状态，例如配对密钥（pairing keys），以及配置。启用后，应用必须在完成所有必要初始化，例如调用 `bt_enable` 之后，调用 `settings_load()`。

将 `settings_load()` 留给协议栈外部调用，是因为其他子系统也可能使用设置 API；一次加载全部设置，比各子系统分别加载更高效。

警告：蓝牙主机要求设置后端（settings backend）按句柄顺序（handle order）加载设置项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**主动选择（Selects）**

```text
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
```

**被选择（Selected by）**

```text
CONFIG_BT_PRIVACY_RANDOMIZE_IR
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:187`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L187)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)、[`CONFIG_BT_PRIVACY_RANDOMIZE_IR`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_PRIVACY_RANDOMIZE_IR)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SETTINGS_CCC_LAZY_LOADING"></a>

## 330.99 `CONFIG_BT_SETTINGS_CCC_LAZY_LOADING`

**提示（Prompt）**：对端连接时从设置中加载 CCC 值（Load CCC values when peer connects）

**说明（Help）**

已绑定设备连接后，立即加载客户端配置特征设置（Client Configuration Characteristic setting）。禁用会增加内存用量，因为调用 `settings_load` 时会加载所有已绑定设备的 CCC 值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CONN && CONFIG_BT_SETTINGS && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:208`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L208)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 持久化保存蓝牙状态与配置（Store Bluetooth state and configuration persistently）

**配置项引用（Symbol References）**：[`CONFIG_BT_CONN`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CONN)、[`CONFIG_BT_SETTINGS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_SETTINGS)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<a id="CONFIG_BT_SETTINGS_CCC_STORE_MAX"></a>

## 330.100 `CONFIG_BT_SETTINGS_CCC_STORE_MAX`

**提示（Prompt）**：客户端特征配置最大数量（Client Characteristic Configuration，CCC）

**说明（Help）**

定义协议栈能够处理的客户端特征配置（Client Characteristic Configuration，CCC）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SETTINGS && CONFIG_BT_HCI_HOST && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
48
```

**取值范围（Ranges）**

```text
[1, 96]
```

**定义位置（Location）**：[`subsys/bluetooth/host/Kconfig:263`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bluetooth/host/Kconfig#L263)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙主机（Bluetooth Host） → 持久化保存蓝牙状态与配置（Store Bluetooth state and configuration persistently）

**配置项引用（Symbol References）**：[`CONFIG_BT_SETTINGS`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_SETTINGS)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`。

<!-- kconfig-navigation -->

[上一章](P329_subsys_bluetooth_配置项参考_10.md) · [返回大纲](大纲.md) · [下一章](P331_subsys_bluetooth_配置项参考_12.md)
