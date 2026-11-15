---
id: learning.zephyr-docs.kconfig-reference.page-385
title: "`subsys/mgmt`配置项参考（2/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第385章\_`subsys/mgmt`配置项参考（2/4）

本章翻译官方 Kconfig 数据库中 `subsys/mgmt` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH_CHUNK_SIZE"></a>

## 385.1 `CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH_CHUNK_SIZE`

**提示（Prompt）**：校验和计算缓冲区大小（Checksum calculation buffer size）

**说明（Help）**

计算文件校验和或散列（checksum/hash）时使用的缓冲区数据块大小，该缓冲区占用栈空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH && CONFIG_MCUMGR_GRP_FS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[32, 16384]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers） → MCUmgr 校验和／散列功能（Checksum/hash）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH)、[`CONFIG_MCUMGR_GRP_FS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH_SUPPORTED_CMD"></a>

## 385.2 `CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH_SUPPORTED_CMD`

**提示（Prompt）**：查询支持的散列／校验和命令

**说明（Help）**

启用“支持的散列／校验和（supported hash/checksum）”命令，返回可使用的散列及校验和类型详情。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH && CONFIG_MCUMGR_GRP_FS && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3 if CONFIG_ZCBOR_CANONICAL
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers） → MCUmgr 校验和／散列功能（Checksum/hash）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH)、[`CONFIG_MCUMGR_GRP_FS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3)、[`CONFIG_ZCBOR_CANONICAL`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR_CANONICAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3`。

<a id="CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH_SUPPORTED_MAX_TYPES"></a>

## 385.3 `CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH_SUPPORTED_MAX_TYPES`

**提示（Prompt）**：支持列表返回类型数量的预计上限

**说明（Help）**

用于定义保存所支持散列／校验和信息的 CBOR 映射。此值不影响内存分配，而是供 zcbor 根据预估大小确定映射编码方式。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH_SUPPORTED_CMD && CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH && CONFIG_MCUMGR_GRP_FS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers） → MCUmgr 校验和／散列功能（Checksum/hash） → 查询支持的散列／校验和命令

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH_SUPPORTED_CMD`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH_SUPPORTED_CMD)、[`CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH)、[`CONFIG_MCUMGR_GRP_FS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_FS_CHECKSUM_IEEE_CRC32"></a>

## 385.4 `CONFIG_MCUMGR_GRP_FS_CHECKSUM_IEEE_CRC32`

**提示（Prompt）**：IEEE CRC32 校验和支持（checksum）

**说明（Help）**

为 MCUmgr 启用 IEEE CRC32 校验和支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH && CONFIG_MCUMGR_GRP_FS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers） → MCUmgr 校验和／散列功能（Checksum/hash）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH)、[`CONFIG_MCUMGR_GRP_FS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_MCUMGR_GRP_FS_DL_CHUNK_SIZE"></a>

## 385.5 `CONFIG_MCUMGR_GRP_FS_DL_CHUNK_SIZE`

**提示（Prompt）**：文件下载数据块最大大小（Maximum chunk size）

**说明（Help）**

设置数据块大小上限。实际值会向下调整到一个可与全部必要头部一起装入 `MCUMGR_TRANSPORT_NETBUF_SIZE` 的字节数，因此可能小于配置值；发生这种情况时，编译器会发出警告。详情见 `fs_mgmt_config.h`。注意：头部大小受 `MCUMGR_GRP_FS_MAX_OFFSET_LEN` 影响。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_FS_DL_CHUNK_SIZE_LIMIT && CONFIG_MCUMGR_GRP_FS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE
```

**取值范围（Ranges）**

```text
[65, CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers） → 自定义下载文件数据块大小（chunk size）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS_DL_CHUNK_SIZE_LIMIT`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_FS_DL_CHUNK_SIZE_LIMIT)、[`CONFIG_MCUMGR_GRP_FS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE)。

<a id="CONFIG_MCUMGR_GRP_FS_DL_CHUNK_SIZE_LIMIT"></a>

## 385.6 `CONFIG_MCUMGR_GRP_FS_DL_CHUNK_SIZE_LIMIT`

**提示（Prompt）**：自定义下载文件数据块大小（chunk size）

**说明（Help）**

默认自动计算从存储读取并装入 MCUmgr 帧（frame）的文件数据块大小，使其与全部头部一起适配 `MCUMGR_TRANSPORT_NETBUF_SIZE` 大小的缓冲区。启用本项后，可设置此数据块允许的最大值。详情见 `fs_mgmt_config.h`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_FS && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK"></a>

## 385.7 `CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK`

**提示（Prompt）**：文件访问钩子（File access hooks）

**说明（Help）**

允许应用通过注册回调控制文件访问，例如文件上传和下载；每当通过文件系统管理组功能访问文件时，都会触发回调。还可按需重写或更改传入的文件路径。由于 MCUmgr 使用单一文件状态，每次文件读写过程中可能多次调用此回调。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS && CONFIG_MCUMGR_GRP_FS && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig:150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig#L150)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS)、[`CONFIG_MCUMGR_GRP_FS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_FS_FILE_AUTOMATIC_IDLE_CLOSE_TIME"></a>

## 385.8 `CONFIG_MCUMGR_GRP_FS_FILE_AUTOMATIC_IDLE_CLOSE_TIME`

**提示（Prompt）**：自动关闭文件句柄的时间（毫秒，file handle close time）

**说明（Help）**

文件上传／下载空闲达到此时间后，判定为已中止并清理文件句柄（file handle），单位为毫秒。每次文件访问都会将空闲计时重置为 `0`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_FS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
4000
```

**取值范围（Ranges）**

```text
[1, 99999999]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_FS_FILE_SEMAPHORE_TAKE_TIME"></a>

## 385.9 `CONFIG_MCUMGR_GRP_FS_FILE_SEMAPHORE_TAKE_TIME`

**提示（Prompt）**：获取文件句柄信号量的时间（毫秒）

**说明（Help）**

使用文件上传／下载命令时，获取文件句柄信号量（semaphore）的最长等待时间，单位为毫秒。无法获得时返回 `MGMT_ERR_EBUSY`。可设为 `0`，不等待锁，无法获得时立即返回。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_FS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig:160`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig#L160)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_FS_FILE_STATUS"></a>

## 385.10 `CONFIG_MCUMGR_GRP_FS_FILE_STATUS`

**提示（Prompt）**：文件状态命令（File status command）

**说明（Help）**

允许远程设备获取文件状态。当前仅在文件存在时返回其大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_FS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_FS_HASH_SHA256"></a>

## 385.11 `CONFIG_MCUMGR_GRP_FS_HASH_SHA256`

**提示（Prompt）**：SHA256 散列支持（hash support）

**说明（Help）**

为 MCUmgr 启用 SHA256 散列支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH && CONFIG_MCUMGR_GRP_FS && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_PSA_CRYPTO
CONFIG_PSA_WANT_ALG_SHA_256
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers） → MCUmgr 校验和／散列功能（Checksum/hash）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH)、[`CONFIG_MCUMGR_GRP_FS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)。

<a id="CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE"></a>

## 385.12 `CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE`

**提示（Prompt）**：允许上传／下载的最大文件大小

**说明（Help）**

允许从设备下载的最大文件大小。本项决定在 CBOR 帧中，为保存下载文件的偏移量／大小预留多少字节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_FS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE_64KB
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE_64KB
CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE_4GB
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE_64KB`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE_64KB)、[`CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE_4GB`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE_4GB)。

<a id="CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE_4GB"></a>

## 385.13 `CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE_4GB`

**提示（Prompt）**：不超过 4GB（<= 4GB）

**说明（Help）**

大小不超过 4GB 的文件，在包含文件数据块的 CBOR 帧中，需要 1～5 字节编码大小／偏移量（size/offset）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE>
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers） → 允许上传／下载的最大文件大小

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE)。

<a id="CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE_64KB"></a>

## 385.14 `CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE_64KB`

**提示（Prompt）**：不超过 64KB（<= 64KB）

**说明（Help）**

大小不超过 64KB 的文件，在包含文件数据块的 CBOR 帧中，需要 1～3 字节编码大小／偏移量（size/offset）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE>
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers） → 允许上传／下载的最大文件大小

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE)。

<a id="CONFIG_MCUMGR_GRP_FS_MAX_OFFSET_LEN"></a>

## 385.15 `CONFIG_MCUMGR_GRP_FS_MAX_OFFSET_LEN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

包含下载文件数据块的 CBOR 帧中，编码后偏移量／大小字段的最大字节长度。它决定头部字段大小，从而影响下载缓冲区可容纳的数据量。

注意：此选项有意隐藏，因为它应根据 `MCUMGR_GRP_FS_MAX_FILE_SIZE` 菜单的选择，从有限的允许值集合中赋值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_FS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
3 if CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE_64KB
5 if CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE_4GB
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE_64KB`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE_64KB)、[`CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE_4GB`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_FS_MAX_FILE_SIZE_4GB)。

<a id="CONFIG_MCUMGR_GRP_FS_PATH_LEN"></a>

## 385.16 `CONFIG_MCUMGR_GRP_FS_PATH_LEN`

**提示（Prompt）**：文件路径最大长度（Maximum file path length）

**说明（Help）**

限制文件操作的最大路径长度，单位为字节。处理文件上传和下载命令期间，会在栈上分配此大小的缓冲区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_FS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig:143`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig#L143)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_IMG"></a>

## 385.17 `CONFIG_MCUMGR_GRP_IMG`

**提示（Prompt）**：MCUmgr 映像管理处理程序（image management handlers）

**说明（Help）**

启用 MCUmgr 映像管理处理程序（image management handlers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH && CONFIG_IMG_MANAGER && !CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP && (CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE >= 104 || !CONFIG_MCUMGR_TRANSPORT_UART) && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2
CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3 if CONFIG_ZCBOR_CANONICAL
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_MANAGER)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_SINGLE_APP)、[`CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_NETBUF_SIZE)、[`CONFIG_MCUMGR_TRANSPORT_UART`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UART)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3)、[`CONFIG_ZCBOR_CANONICAL`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR_CANONICAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`、`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3`。

<a id="CONFIG_MCUMGR_GRP_IMG_ALLOW_CONFIRM_NON_ACTIVE_IMAGE_ANY"></a>

## 385.18 `CONFIG_MCUMGR_GRP_IMG_ALLOW_CONFIRM_NON_ACTIVE_IMAGE_ANY`

**提示（Prompt）**：允许确认非活动映像的槽位（non-active image slots）

**说明（Help）**

允许确认非活动映像的任意槽位（slot）。通常不应通过 MCUmgr 命令确认非活动映像的槽位，以免确认了损坏且可能无法在其他槽位启动的映像；应由应用提供测试并确认映像的机制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER && CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_GRP_IMG_ALLOW_CONFIRM_NON_ACTIVE_IMAGE_SECONDARY
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER)、[`CONFIG_MCUMGR_GRP_IMG`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_IMG_ALLOW_CONFIRM_NON_ACTIVE_IMAGE_SECONDARY`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG_ALLOW_CONFIRM_NON_ACTIVE_IMAGE_SECONDARY)。

<a id="CONFIG_MCUMGR_GRP_IMG_ALLOW_CONFIRM_NON_ACTIVE_IMAGE_SECONDARY"></a>

## 385.19 `CONFIG_MCUMGR_GRP_IMG_ALLOW_CONFIRM_NON_ACTIVE_IMAGE_SECONDARY`

**提示（Prompt）**：允许确认非活动映像的次槽位（secondary slot）

**说明（Help）**

允许确认非活动映像的次槽位，即非活动槽位（secondary/non-active slot）。通常不应通过 MCUmgr 命令确认非活动映像的槽位，以免确认了损坏且可能无法在其他槽位启动的映像；应由应用提供测试并确认映像的机制。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER && CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_MCUMGR_GRP_IMG_ALLOW_CONFIRM_NON_ACTIVE_IMAGE_ANY
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER)、[`CONFIG_MCUMGR_GRP_IMG`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_IMG_ALLOW_CONFIRM_NON_ACTIVE_IMAGE_ANY`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG_ALLOW_CONFIRM_NON_ACTIVE_IMAGE_ANY)。

<a id="CONFIG_MCUMGR_GRP_IMG_ALLOW_CONFIRM_NON_ACTIVE_SLOT"></a>

## 385.20 `CONFIG_MCUMGR_GRP_IMG_ALLOW_CONFIRM_NON_ACTIVE_SLOT`

**提示（Prompt）**：允许确认任意映像的非活动槽位

**说明（Help）**

允许确认任意映像的非活动槽位（non-active slot）。通常不应通过 MCUmgr 命令确认任何槽位，以免确认了损坏且未验证能够正确启动的映像。仅覆盖模式（overwrite only mode）下始终启用此项，因为更新是永久性的，而使用确认标志（confirm flag）正是该模式预期的更新方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT || CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT || CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_SCRATCH || CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_MOVE || CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_OFFSET || CONFIG_MCUBOOT_BOOTLOADER_MODE_OVERWRITE_ONLY) && CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_RAM_LOAD_WITH_REVERT)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_SCRATCH`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_SCRATCH)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_MOVE`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_MOVE)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_OFFSET`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_SWAP_USING_OFFSET)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_OVERWRITE_ONLY`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_OVERWRITE_ONLY)、[`CONFIG_MCUMGR_GRP_IMG`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_IMG_ALLOW_ERASE_PENDING"></a>

## 385.21 `CONFIG_MCUMGR_GRP_IMG_ALLOW_ERASE_PENDING`

**提示（Prompt）**：允许擦除待切换槽位（pending slot）

**说明（Help）**

允许擦除标记为测试（test）或已确认（confirmed）的次槽位。即使槽位已设置为下次启动使用，只要设备尚未复位、槽位尚未交换（swapped），仍可擦除。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP && CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP)、[`CONFIG_MCUMGR_GRP_IMG`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_IMG_CLIENT"></a>

## 385.22 `CONFIG_MCUMGR_GRP_IMG_CLIENT`

**提示（Prompt）**：MCUmgr 映像管理客户端处理程序（client handlers）

**说明（Help）**

启用 MCUmgr 映像管理客户端处理程序（client handlers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SMP_CLIENT && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MCUBOOT_BOOTUTIL_LIB
CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt_client/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt_client/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers）

**配置项引用（Symbol References）**：[`CONFIG_SMP_CLIENT`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_SMP_CLIENT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUBOOT_BOOTUTIL_LIB`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTUTIL_LIB)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3`。

<a id="CONFIG_MCUMGR_GRP_IMG_DIRECT_UPLOAD"></a>

## 385.23 `CONFIG_MCUMGR_GRP_IMG_DIRECT_UPLOAD`

**提示（Prompt）**：允许直接上传映像（direct image upload）

**说明（Help）**

允许将映像直接上传到选定映像分区。这会改变 MCUmgr 对“映像（image）”的理解：通常 MCUmgr 只知道一个映像，允许上传到它的第一个槽位；此时一个映像包含两个槽位，在 Zephyr 中对应两个 DTS 映像。直接上传模式则将每个 DTS 定义的映像都视为直接上传目标，因此可以使用两个以上目标，原文时点为 `4` 个。

注意：直接上传模式下，映像编号整体加 `1`。未选择映像时，默认上传到通常操作中代表次槽位（secondary slot）的映像。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER && CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_FIRMWARE_UPDATER)、[`CONFIG_MCUMGR_GRP_IMG`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_IMG_FLASH_OPERATION_TIMEOUT"></a>

## 385.24 `CONFIG_MCUMGR_GRP_IMG_FLASH_OPERATION_TIMEOUT`

**提示（Prompt）**：MCUmgr 复位或上传命令超时（timeout）

**说明（Help）**

平台需要不同等待时间时，更改默认值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_IMG_CLIENT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
15
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt_client/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt_client/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理客户端处理程序（client handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG_CLIENT`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG_CLIENT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_IMG_FRUGAL_LIST"></a>

## 385.25 `CONFIG_MCUMGR_GRP_IMG_FRUGAL_LIST`

**提示（Prompt）**：在状态列表中省略零、空值或 false

**说明（Help）**

设备返回的状态列表（status list）只填充非零、非空或为 true 的数据。可略微减少返回字节数，但客户端软件必须支持为省略字段使用默认值。原文指出，此功能可与 Go 版本的 `mcumgr-cli` 应用正确配合。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_IMG_IMAGE_SLOT_STATE_HOOK"></a>

## 385.26 `CONFIG_MCUMGR_GRP_IMG_IMAGE_SLOT_STATE_HOOK`

**提示（Prompt）**：映像槽位状态钩子（Image slot state hook）

**说明（Help）**

允许应用向映像槽位状态命令的响应添加额外字段（fields）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS && CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:205`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L205)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS)、[`CONFIG_MCUMGR_GRP_IMG`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_IMG_IMAGE_SLOT_STATE_STATES"></a>

## 385.27 `CONFIG_MCUMGR_GRP_IMG_IMAGE_SLOT_STATE_STATES`

**提示（Prompt）**：每组条目数量的预计上限（Predicted maximum number）

**说明（Help）**

用于定义保存组数据的 CBOR 映射。此值不影响内存分配，而是供 zcbor 根据预估大小确定映射编码方式。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
15
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:212`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L212)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers） → 映像槽位状态钩子（Image slot state hook）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_IMG_MUTEX"></a>

## 385.28 `CONFIG_MCUMGR_GRP_IMG_MUTEX`

**提示（Prompt）**：互斥锁保护（Mutex locking）

**说明（Help）**

启用互斥锁（mutex）保护映像组对象访问，避免并发线程，例如多个传输通道，访问时出现问题。同时在映像管理组头文件中公开 `img_mgmt_reset_upload()`，应用可用它重置映像管理状态；存在多种固件更新加载方式时尤其有用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_IMG_REJECT_DIRECT_XIP_MISMATCHED_SLOT"></a>

## 385.29 `CONFIG_MCUMGR_GRP_IMG_REJECT_DIRECT_XIP_MISMATCHED_SLOT`

**提示（Prompt）**：拒绝地址不匹配的直接就地执行应用（Direct-XIP）

**说明（Help）**

启用后，上传时 MCUmgr 比较应用基地址（base address）；该地址由 imgtool 编码到 `.bin` 文件头中。若二进制文件无法从可用的直接就地执行（Direct-XIP）地址启动，则拒绝上传。可通过 imgtool 的 `--rom-fixed` 命令行选项设置映像头中的基地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP || CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT) && CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT)、[`CONFIG_MCUMGR_GRP_IMG`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_IMG_SLOT_INFO"></a>

## 385.30 `CONFIG_MCUMGR_GRP_IMG_SLOT_INFO`

**提示（Prompt）**：槽位信息（Slot info）

**说明（Help）**

启用槽位信息功能，返回应用可见的全部映像与槽位（images and slots）信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y if CONFIG_MCUMGR_GRP_IMG_UPDATABLE_IMAGE_NUMBER > 1
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L221)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_IMG_UPDATABLE_IMAGE_NUMBER`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG_UPDATABLE_IMAGE_NUMBER)。

<a id="CONFIG_MCUMGR_GRP_IMG_SLOT_INFO_HOOKS"></a>

## 385.31 `CONFIG_MCUMGR_GRP_IMG_SLOT_INFO_HOOKS`

**提示（Prompt）**：槽位信息钩子（Slot info hooks）

**说明（Help）**

启用槽位信息函数钩子（hooks），以向响应添加额外信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_IMG_SLOT_INFO && CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS && CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:228`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L228)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers） → 槽位信息（Slot info）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG_SLOT_INFO`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG_SLOT_INFO)、[`CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS)、[`CONFIG_MCUMGR_GRP_IMG`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS"></a>

## 385.32 `CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS`

**提示（Prompt）**：状态钩子（Status hooks）

**说明（Help）**

启用设备固件更新（DFU）状态钩子，供应用监视 DFU 上传。注意，这些钩子仅用于状态检查；若需检查文件上传内容或阻止上传，必须使用 `CONFIG_MCUMGR_GRP_IMG_UPLOAD_CHECK_HOOK`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS && CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:156`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L156)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS)、[`CONFIG_MCUMGR_GRP_IMG`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_BOOTLOADER_INFO"></a>

## 385.33 `CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_BOOTLOADER_INFO`

**提示（Prompt）**：通过保留存储中的引导加载程序信息（retention bootloader info）

**说明（Help）**

从保留存储子系统（retention subsystem）的引导加载程序信息模块获取最大映像大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RETENTION_BOOTLOADER_INFO_OUTPUT_FUNCTION && <choice CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_CHECK>
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:197`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L197)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers） → 映像大小检查中的额外开销（Image size check overhead）

**配置项引用（Symbol References）**：[`CONFIG_RETENTION_BOOTLOADER_INFO_OUTPUT_FUNCTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RETENTION_BOOTLOADER_INFO_OUTPUT_FUNCTION)、[`CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_CHECK`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_CHECK)。

<a id="CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_CHECK"></a>

## 385.34 `CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_CHECK`

**提示（Prompt）**：映像大小检查中的额外开销（Image size check overhead）

**说明（Help）**

MCUboot 映像必须限制在引导加载程序能够交换的最大大小以内。确定此大小需要 MCUboot 配置的额外信息，否则可能上传过大、无法交换的映像。本项选择获取该信息的方法。

注意：选择任何非禁用选项，都会阻止上传已填充且已确认（padded and confirmed）的映像；若需支持此类映像，应保持禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_DISABLED
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_DISABLED
CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_SYSBUILD
CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_BOOTLOADER_INFO
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L173)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_DISABLED`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_DISABLED)、[`CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_SYSBUILD`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_SYSBUILD)、[`CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_BOOTLOADER_INFO`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_BOOTLOADER_INFO)。

<a id="CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_DISABLED"></a>

## 385.35 `CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_DISABLED`

**提示（Prompt）**：禁用（Disabled）

**说明（Help）**

检查最大文件大小时，不考虑 MCUboot 配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_CHECK>
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:186`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L186)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers） → 映像大小检查中的额外开销（Image size check overhead）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_CHECK`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_CHECK)。

<a id="CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_SYSBUILD"></a>

## 385.36 `CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_SYSBUILD`

**提示（Prompt）**：通过系统构建（Sysbuild）从 MCUboot 配置获取

**说明（Help）**

使用系统构建（Sysbuild）映像配置阶段计算的映像额外开销大小（image overhead size）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_ROM_END_OFFSET > 0 || CONFIG_MCUBOOT_UPDATE_FOOTER_SIZE > 0) && <choice CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_CHECK>
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:191`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L191)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers） → 映像大小检查中的额外开销（Image size check overhead）

**配置项引用（Symbol References）**：[`CONFIG_ROM_END_OFFSET`](P004_Kconfig.zephyr_配置项参考_2.md#CONFIG_ROM_END_OFFSET)、[`CONFIG_MCUBOOT_UPDATE_FOOTER_SIZE`](P339_subsys_dfu_配置项参考.md#CONFIG_MCUBOOT_UPDATE_FOOTER_SIZE)、[`CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_CHECK`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG_TOO_LARGE_CHECK)。

<a id="CONFIG_MCUMGR_GRP_IMG_UPDATABLE_IMAGE_NUMBER"></a>

## 385.37 `CONFIG_MCUMGR_GRP_IMG_UPDATABLE_IMAGE_NUMBER`

**提示（Prompt）**：支持的映像数量（Number of supported images）

**说明（Help）**

设置支持的应用映像数量，每个映像是一对主槽位与次槽位（primary/secondary slots）。设为 `2` 时，要求 `MCUMGR_TRANSPORT_NETBUF_SIZE` 至少为 512 字节。

注意：即便采用 Zephyr 构建，MCUboot 配置中的 `UPDATEABLE_IMAGE_NUMBER` 也必须设为相同值，因为 MCUmgr 使用 `boot_util`，而该配置决定此库支持的映像数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_UPDATEABLE_IMAGE_NUMBER
```

**取值范围（Ranges）**

```text
[1, 3]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_UPDATEABLE_IMAGE_NUMBER`](P339_subsys_dfu_配置项参考.md#CONFIG_UPDATEABLE_IMAGE_NUMBER)。

<a id="CONFIG_MCUMGR_GRP_IMG_UPLOAD_CHECK_HOOK"></a>

## 385.38 `CONFIG_MCUMGR_GRP_IMG_UPLOAD_CHECK_HOOK`

**提示（Prompt）**：上传检查钩子（Upload check hook）

**说明（Help）**

启用上传检查钩子，将映像上传请求发送给已注册回调，让用户应用决定接受还是拒绝上传。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS && CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS)、[`CONFIG_MCUMGR_GRP_IMG`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_IMG_UPLOAD_DATA_ALIGNMENT_SIZE"></a>

## 385.39 `CONFIG_MCUMGR_GRP_IMG_UPLOAD_DATA_ALIGNMENT_SIZE`

**提示（Prompt）**：MCUmgr 上传数据对齐大小（data alignment size）

**说明（Help）**

平台需要不同数据对齐（data alignment）时，更改默认值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_IMG_CLIENT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt_client/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt_client/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理客户端处理程序（client handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG_CLIENT`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG_CLIENT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_IMG_USE_HEAP_FOR_FLASH_IMG_CONTEXT"></a>

## 385.40 `CONFIG_MCUMGR_GRP_IMG_USE_HEAP_FOR_FLASH_IMG_CONTEXT`

**提示（Prompt）**：使用堆内存池分配闪存映像 DFU 上下文

**说明（Help）**

使用堆（heap）分配闪存映像上传上下文，否则使用静态变量。`MCUMGR_GRP_IMG_MANAGER` 使用该上下文缓冲映像写入；对象较大，主要由 `CONFIG_IMG_BLOCK_BUF_SIZE` 大小的映像写入缓冲区，以及 `struct flash_img_context` 中保存状态信息的其他字段构成。禁用此项会增加静态 RAM 使用量。

启用时，应通过测试确认堆有足够空间分配该上下文，否则无法执行设备固件更新（DFU）。应用运行造成堆空间紧张时，也可能分配失败，应用同样需要处理这种情况。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HEAP_MEM_POOL_SIZE > 0 && CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers）

**配置项引用（Symbol References）**：[`CONFIG_HEAP_MEM_POOL_SIZE`](P001_kernel_配置项参考_1.md#CONFIG_HEAP_MEM_POOL_SIZE)、[`CONFIG_MCUMGR_GRP_IMG`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_IMG_VERBOSE_ERR"></a>

## 385.41 `CONFIG_MCUMGR_GRP_IMG_VERBOSE_ERR`

**提示（Prompt）**：上传应用映像时返回详细错误响应（Verbose error responses）

**说明（Help）**

在有相应说明时，为简单管理协议（SMP）响应添加 `rsn` 键，解释非零 `rc` 代码。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_SMP_VERBOSE_ERR_RESPONSE
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_SMP_VERBOSE_ERR_RESPONSE`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_SMP_VERBOSE_ERR_RESPONSE)。

<a id="CONFIG_MCUMGR_GRP_IMG_VERSION_CMP_USE_BUILD_NUMBER"></a>

## 385.42 `CONFIG_MCUMGR_GRP_IMG_VERSION_CMP_USE_BUILD_NUMBER`

**提示（Prompt）**：比较映像版本时使用构建号（build number）

**说明（Help）**

默认只比较主版本号（major）、次版本号（minor）和修订号（revision）。启用后，比较时也考虑构建号（build number）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig:142`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/img_mgmt/Kconfig#L142)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS"></a>

## 385.43 `CONFIG_MCUMGR_GRP_OS`

**提示（Prompt）**：MCUmgr 操作系统管理处理程序（OS management handlers）

**说明（Help）**

启用 MCUmgr 操作系统管理处理程序（OS management handlers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**弱选择（Implies）**

```text
CONFIG_REBOOT
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_REBOOT`](P198_lib_配置项参考_2.md#CONFIG_REBOOT)。

<a id="CONFIG_MCUMGR_GRP_OS_BOOTLOADER_INFO"></a>

## 385.44 `CONFIG_MCUMGR_GRP_OS_BOOTLOADER_INFO`

**提示（Prompt）**：引导加载程序信息（Bootloader information）

**说明（Help）**

允许通过 MCUmgr 查询设备使用的引导加载程序（bootloader）及其各种参数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:217`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L217)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS_BOOTLOADER_INFO_HOOK"></a>

## 385.45 `CONFIG_MCUMGR_GRP_OS_BOOTLOADER_INFO_HOOK`

**提示（Prompt）**：引导加载程序信息钩子（Bootloader info hooks）

**说明（Help）**

通过已注册回调，向引导加载程序信息命令添加自定义响应。可向回调提供的结构体追加数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS && CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:223`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L223)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS)、[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS_CLIENT"></a>

## 385.46 `CONFIG_MCUMGR_GRP_OS_CLIENT`

**提示（Prompt）**：MCUmgr 操作系统管理的客户端请求与响应处理程序（request and response handlers）

**说明（Help）**

启用 MCUmgr 操作系统管理的客户端请求和响应处理程序（request and response handlers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SMP_CLIENT && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt_client/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt_client/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers）

**配置项引用（Symbol References）**：[`CONFIG_SMP_CLIENT`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_SMP_CLIENT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3`。

<a id="CONFIG_MCUMGR_GRP_OS_CLIENT_ECHO"></a>

## 385.47 `CONFIG_MCUMGR_GRP_OS_CLIENT_ECHO`

**提示（Prompt）**：支持回显命令请求（echo command request）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_OS_CLIENT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt_client/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt_client/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理的客户端请求与响应处理程序（request and response handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_CLIENT`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_CLIENT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS_CLIENT_RESET"></a>

## 385.48 `CONFIG_MCUMGR_GRP_OS_CLIENT_RESET`

**提示（Prompt）**：支持复位命令请求（reset command request）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_OS_CLIENT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt_client/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt_client/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理的客户端请求与响应处理程序（request and response handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_CLIENT`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_CLIENT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS_DATETIME"></a>

## 385.49 `CONFIG_MCUMGR_GRP_OS_DATETIME`

**提示（Prompt）**：支持日期时间命令（datetime command）

**说明（Help）**

支持获取和设置日期时间（datetime get/set），使用别名为 `rtc` 的设备作为时间源（timesource），从中读取或向其写入当前时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`。

<a id="CONFIG_MCUMGR_GRP_OS_DATETIME_HOOK"></a>

## 385.50 `CONFIG_MCUMGR_GRP_OS_DATETIME_HOOK`

**提示（Prompt）**：日期时间钩子（Datetime hook）

**说明（Help）**

允许应用控制通过 MCUmgr 发出的日期时间设置／获取命令，并在这些命令发出时接收通知。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_OS_DATETIME && CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS && CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:171`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L171)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → 支持日期时间命令（datetime command）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_DATETIME`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_DATETIME)、[`CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS)、[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS_DATETIME_MS"></a>

## 385.51 `CONFIG_MCUMGR_GRP_OS_DATETIME_MS`

**提示（Prompt）**：日期时间命令支持毫秒字段（millisecond field）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_OS_DATETIME && CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:167`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L167)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → 支持日期时间命令（datetime command）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_DATETIME`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_DATETIME)、[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS_ECHO"></a>

## 385.52 `CONFIG_MCUMGR_GRP_OS_ECHO`

**提示（Prompt）**：支持回显命令（echo command）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`。

<a id="CONFIG_MCUMGR_GRP_OS_INFO"></a>

## 385.53 `CONFIG_MCUMGR_GRP_OS_INFO`

**提示（Prompt）**：支持信息命令（info command）

**说明（Help）**

可像 Unix/Linux 的 `uname` 命令一样，获取系统信息，包括内核版本、处理器体系结构和开发板名称。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:182`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L182)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS_INFO_BUILD_DATE_TIME"></a>

## 385.54 `CONFIG_MCUMGR_GRP_OS_INFO_BUILD_DATE_TIME`

**提示（Prompt）**：显示构建日期和时间（build date and time）

**说明（Help）**

允许使用 `info` 命令的格式选项 `b` 返回固件构建日期和时间；使用 `a` 获取全部响应时也会返回。注意：这会将构建日期／时间嵌入输出固件映像，破坏固件的可复现构建（reproducible builds）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_OS_INFO && CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:206`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L206)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → 支持信息命令（info command）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_INFO`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_INFO)、[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS_INFO_CUSTOM_HOOKS"></a>

## 385.55 `CONFIG_MCUMGR_GRP_OS_INFO_CUSTOM_HOOKS`

**提示（Prompt）**：自定义信息钩子（Custom info hooks）

**说明（Help）**

通过已注册回调，为 `info` 命令添加自定义命令／字符处理。可向回调提供的结构体追加数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS && CONFIG_MCUMGR_GRP_OS_INFO && CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:199`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L199)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → 支持信息命令（info command）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS)、[`CONFIG_MCUMGR_GRP_OS_INFO`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_INFO)、[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS_INFO_MAX_RESPONSE_SIZE"></a>

## 385.56 `CONFIG_MCUMGR_GRP_OS_INFO_MAX_RESPONSE_SIZE`

**提示（Prompt）**：info 命令响应最大大小（Maximum response size）

**说明（Help）**

`info` 命令响应的最大大小。会使用此大小的栈缓冲区存储数据。若输出响应过大，则响应中不包含输出内容，仅返回内存错误结果码 `rc`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_OS_INFO && CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[32, 512]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:190`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L190)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → 支持信息命令（info command）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_INFO`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_INFO)、[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS_MCUMGR_PARAMS"></a>

## 385.57 `CONFIG_MCUMGR_GRP_OS_MCUMGR_PARAMS`

**提示（Prompt）**：MCUmgr 参数获取命令（Parameters retrieval command）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L179)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS_MPSTAT"></a>

## 385.58 `CONFIG_MCUMGR_GRP_OS_MPSTAT`

**提示（Prompt）**：支持内存池统计命令（memory pool statistics command）

**说明（Help）**

内存池统计命令 `mpstat` 列出设备上的各个堆内存池，包括大小、空闲空间，以及空闲空间的最小值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SYS_HEAP_RUNTIME_STATS && CONFIG_SYS_HEAP_ARRAY_SIZE > 0 && CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_2
CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3 if CONFIG_ZCBOR_CANONICAL
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:133`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L133)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers）

**配置项引用（Symbol References）**：[`CONFIG_SYS_HEAP_RUNTIME_STATS`](P199_lib_配置项参考_3.md#CONFIG_SYS_HEAP_RUNTIME_STATS)、[`CONFIG_SYS_HEAP_ARRAY_SIZE`](P198_lib_配置项参考_2.md#CONFIG_SYS_HEAP_ARRAY_SIZE)、[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_2)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3)、[`CONFIG_ZCBOR_CANONICAL`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR_CANONICAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_2`、`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3`。

<a id="CONFIG_MCUMGR_GRP_OS_MPSTAT_ONLY_SUPPORTED_STATS"></a>

## 385.59 `CONFIG_MCUMGR_GRP_OS_MPSTAT_ONLY_SUPPORTED_STATS`

**提示（Prompt）**：仅发送 Zephyr 收集的数据

**说明（Help）**

响应不包含 Zephyr 不支持的 `blksiz` 字段，该字段的值为 `1`。若客户端软件能够处理每个内存池均缺少 `blksiz` 的 `mpstat` 响应，可启用本项，略微减小代码大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_OS_MPSTAT && CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:143`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L143)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → 支持内存池统计命令（memory pool statistics command）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_MPSTAT`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_MPSTAT)、[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS_RESET_BOOT_MODE"></a>

## 385.60 `CONFIG_MCUMGR_GRP_OS_RESET_BOOT_MODE`

**提示（Prompt）**：启动模式（Boot mode）

**说明（Help）**

允许应用通过保留存储启动模式模块（retention boot mode module）设置启动模式，以启动其他映像，例如作为引导加载程序的一部分。通过复位命令中的可选字段指定启动模式值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RETENTION_BOOT_MODE && CONFIG_REBOOT && CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers）

**配置项引用（Symbol References）**：[`CONFIG_RETENTION_BOOT_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RETENTION_BOOT_MODE)、[`CONFIG_REBOOT`](P198_lib_配置项参考_2.md#CONFIG_REBOOT)、[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS_RESET_HOOK"></a>

## 385.61 `CONFIG_MCUMGR_GRP_OS_RESET_HOOK`

**提示（Prompt）**：复位钩子（Reset hook）

**说明（Help）**

允许应用控制 MCUmgr 复位命令，并在收到命令时接收通知。禁用时，模块收到命令后直接重启，不发出通知。启用并注册处理程序（handler）后，会通知应用收到复位命令，允许其先执行必要操作，再接受或拒绝复位请求。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS && CONFIG_REBOOT && CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS)、[`CONFIG_REBOOT`](P198_lib_配置项参考_2.md#CONFIG_REBOOT)、[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS_RESET_MS"></a>

## 385.62 `CONFIG_MCUMGR_GRP_OS_RESET_MS`

**提示（Prompt）**：执行复位命令前的延迟（毫秒）

**说明（Help）**

收到复位命令后，系统等待此时间再复位，单位为毫秒，以便 MCUmgr 响应有时间完成发送。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MULTITHREADING && CONFIG_REBOOT && CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
250
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MULTITHREADING`](P001_kernel_配置项参考_1.md#CONFIG_MULTITHREADING)、[`CONFIG_REBOOT`](P198_lib_配置项参考_2.md#CONFIG_REBOOT)、[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS_TASKSTAT"></a>

## 385.63 `CONFIG_MCUMGR_GRP_OS_TASKSTAT`

**提示（Prompt）**：支持任务状态命令（taskstat command）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_MONITOR && CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3 if CONFIG_ZCBOR_CANONICAL
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_MONITOR`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MONITOR)、[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3)、[`CONFIG_ZCBOR_CANONICAL`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR_CANONICAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3`。

<a id="CONFIG_MCUMGR_GRP_OS_TASKSTAT_MAX_NUM_THREADS"></a>

## 385.64 `CONFIG_MCUMGR_GRP_OS_TASKSTAT_MAX_NUM_THREADS`

**提示（Prompt）**：taskstat 列表返回线程数量的预计上限

**说明（Help）**

用于定义保存线程信息的 CBOR 映射。此值不影响内存分配，而是供 zcbor 根据预估大小确定映射编码方式。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_OS_TASKSTAT && CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → 支持任务状态命令（taskstat command）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_TASKSTAT`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_TASKSTAT)、[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS_TASKSTAT_ONLY_SUPPORTED_STATS"></a>

## 385.65 `CONFIG_MCUMGR_GRP_OS_TASKSTAT_ONLY_SUPPORTED_STATS`

**提示（Prompt）**：仅发送 Zephyr 收集的数据

**说明（Help）**

响应不包含 Zephyr 未收集统计数据的字段。若客户端能够处理每个任务均缺少 `runtime`、`cswcnt`、`last_checkin` 和 `next_checkin` 映射条目的 `taskstat` 响应，可启用本项，略微减小代码大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_OS_TASKSTAT && CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → 支持任务状态命令（taskstat command）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_TASKSTAT`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_TASKSTAT)、[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS_TASKSTAT_SIGNED_PRIORITY"></a>

## 385.66 `CONFIG_MCUMGR_GRP_OS_TASKSTAT_SIGNED_PRIORITY`

**提示（Prompt）**：有符号优先级（Signed priorities）

**说明（Help）**

Zephyr 的线程优先级类型为 `int8_t`，但 `taskstat` 响应默认将其编码为无符号整数。启用后，响应使用有符号整数表示优先级，更符合 Zephyr 的习惯。若客户端无法正确解码和接受有符号优先级，则禁用本项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_OS_TASKSTAT && CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → 支持任务状态命令（taskstat command）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_TASKSTAT`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_TASKSTAT)、[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS_TASKSTAT_STACK_INFO"></a>

## 385.67 `CONFIG_MCUMGR_GRP_OS_TASKSTAT_STACK_INFO`

**提示（Prompt）**：在 taskstat 响应中包含栈信息（stack info）

**说明（Help）**

在 `taskstat` 命令响应中加入栈信息；选择 `THREAD_STACK_INFO` 时默认启用。仅在客户端能够处理缺少 `stksiz` 和 `stkuse` 字段的响应时才禁用。禁用 `THREAD_STACK_INFO` 时，也适合禁用本项，以免仅为填满响应字段而发送全零栈信息，同时可略微减小代码大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_STACK_INFO && CONFIG_MCUMGR_GRP_OS_TASKSTAT && CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L120)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → 支持任务状态命令（taskstat command）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)、[`CONFIG_MCUMGR_GRP_OS_TASKSTAT`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_TASKSTAT)、[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_OS_TASKSTAT_THREAD_NAME_CHOICE"></a>

## 385.68 `CONFIG_MCUMGR_GRP_OS_TASKSTAT_THREAD_NAME_CHOICE`

**提示（Prompt）**：taskstat 中用作线程名称的特征（Characteristic）

**说明（Help）**

选择 `taskstat` 响应中用作线程名称的内容。禁用 `THREAD_NAME` 时，默认使用线程优先级（thread priority）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_OS_TASKSTAT && CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_GRP_OS_TASKSTAT_USE_THREAD_NAME_FOR_NAME if CONFIG_THREAD_NAME
CONFIG_MCUMGR_GRP_OS_TASKSTAT_USE_THREAD_PRIO_FOR_NAME
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_GRP_OS_TASKSTAT_USE_THREAD_NAME_FOR_NAME
CONFIG_MCUMGR_GRP_OS_TASKSTAT_USE_THREAD_IDX_FOR_NAME
CONFIG_MCUMGR_GRP_OS_TASKSTAT_USE_THREAD_PRIO_FOR_NAME
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → 支持任务状态命令（taskstat command）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_TASKSTAT`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_TASKSTAT)、[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_OS_TASKSTAT_USE_THREAD_NAME_FOR_NAME`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_TASKSTAT_USE_THREAD_NAME_FOR_NAME)、[`CONFIG_THREAD_NAME`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_NAME)、[`CONFIG_MCUMGR_GRP_OS_TASKSTAT_USE_THREAD_PRIO_FOR_NAME`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_TASKSTAT_USE_THREAD_PRIO_FOR_NAME)、[`CONFIG_MCUMGR_GRP_OS_TASKSTAT_USE_THREAD_IDX_FOR_NAME`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_TASKSTAT_USE_THREAD_IDX_FOR_NAME)。

<a id="CONFIG_MCUMGR_GRP_OS_TASKSTAT_THREAD_NAME_LEN"></a>

## 385.69 `CONFIG_MCUMGR_GRP_OS_TASKSTAT_THREAD_NAME_LEN`

**提示（Prompt）**：响应中返回的线程名称长度

**说明（Help）**

`taskstat` 命令响应中线程名称字符串的长度。启用 `THREAD_NAME` 时，默认为 `THREAD_MAX_NAME_LEN`；禁用时，根据有符号整数形式的线程优先级生成名称，本项控制使用多少位数字，并应计入可能出现的负号 `-`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_OS_TASKSTAT && CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_THREAD_MAX_NAME_LEN if CONFIG_THREAD_NAME
5 if !CONFIG_THREAD_NAME
```

**取值范围（Ranges）**

```text
[3, CONFIG_THREAD_MAX_NAME_LEN] if CONFIG_THREAD_NAME
[3, 6] if !CONFIG_THREAD_NAME
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → 支持任务状态命令（taskstat command）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_TASKSTAT`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_TASKSTAT)、[`CONFIG_MCUMGR_GRP_OS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_THREAD_MAX_NAME_LEN`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_MAX_NAME_LEN)、[`CONFIG_THREAD_NAME`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_NAME)。

<a id="CONFIG_MCUMGR_GRP_OS_TASKSTAT_USE_THREAD_IDX_FOR_NAME"></a>

## 385.70 `CONFIG_MCUMGR_GRP_OS_TASKSTAT_USE_THREAD_IDX_FOR_NAME`

**提示（Prompt）**：线程索引（Thread index）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_OS_TASKSTAT_THREAD_NAME_CHOICE>
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → 支持任务状态命令（taskstat command） → taskstat 中用作线程名称的特征（Characteristic）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_TASKSTAT_THREAD_NAME_CHOICE`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_TASKSTAT_THREAD_NAME_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_OS_TASKSTAT_USE_THREAD_NAME_FOR_NAME"></a>

## 385.71 `CONFIG_MCUMGR_GRP_OS_TASKSTAT_USE_THREAD_NAME_FOR_NAME`

**提示（Prompt）**：线程名称（Thread Name）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_THREAD_NAME && <choice CONFIG_MCUMGR_GRP_OS_TASKSTAT_THREAD_NAME_CHOICE>
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → 支持任务状态命令（taskstat command） → taskstat 中用作线程名称的特征（Characteristic）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_NAME`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_NAME)、[`CONFIG_MCUMGR_GRP_OS_TASKSTAT_THREAD_NAME_CHOICE`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_TASKSTAT_THREAD_NAME_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_OS_TASKSTAT_USE_THREAD_PRIO_FOR_NAME"></a>

## 385.72 `CONFIG_MCUMGR_GRP_OS_TASKSTAT_USE_THREAD_PRIO_FOR_NAME`

**提示（Prompt）**：线程优先级（Thread Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_OS_TASKSTAT_THREAD_NAME_CHOICE>
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/os_mgmt/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → 支持任务状态命令（taskstat command） → taskstat 中用作线程名称的特征（Characteristic）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_TASKSTAT_THREAD_NAME_CHOICE`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_OS_TASKSTAT_THREAD_NAME_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_SETTINGS"></a>

## 385.73 `CONFIG_MCUMGR_GRP_SETTINGS`

**提示（Prompt）**：MCUmgr 设置管理处理程序（settings management handlers）

**说明（Help）**

启用 MCUmgr 设置操作处理程序（settings manipulation handlers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS && CONFIG_SETTINGS_RUNTIME && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2
CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_2 if CONFIG_ZCBOR_CANONICAL
CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_1
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/settings_mgmt/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/settings_mgmt/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS)、[`CONFIG_SETTINGS_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS_RUNTIME)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_2)、[`CONFIG_ZCBOR_CANONICAL`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR_CANONICAL)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_1`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_1)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`、`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_2`、`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_1`。

<a id="CONFIG_MCUMGR_GRP_SETTINGS_ACCESS_HOOK"></a>

## 385.74 `CONFIG_MCUMGR_GRP_SETTINGS_ACCESS_HOOK`

**提示（Prompt）**：设置访问钩子（Settings access hook）

**说明（Help）**

允许应用通过注册回调控制设置管理访问；每次尝试读取或写入设置（settings）时，都会触发该回调。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS && CONFIG_MCUMGR_GRP_SETTINGS && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/settings_mgmt/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/settings_mgmt/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 设置管理处理程序（settings management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS)、[`CONFIG_MCUMGR_GRP_SETTINGS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_SETTINGS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE"></a>

## 385.75 `CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE`

**提示（Prompt）**：缓冲区类型（Buffer type）

**说明（Help）**

选择处理请求时所需的变量使用栈（stack）还是堆（heap）存储。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_SETTINGS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE_STACK
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE_STACK
CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE_HEAP
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/settings_mgmt/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/settings_mgmt/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 设置管理处理程序（settings management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_SETTINGS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_SETTINGS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE_STACK`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE_STACK)、[`CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE_HEAP`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE_HEAP)。

<a id="CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE_HEAP"></a>

## 385.76 `CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE_HEAP`

**提示（Prompt）**：堆，动态大小（Heap, dynamic size）

**说明（Help）**

通过 `k_malloc` 动态分配堆内存。若可用堆内存不足以完成分配，则拒绝请求。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HEAP_MEM_POOL_SIZE > 0 && <choice CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE>
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/settings_mgmt/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/settings_mgmt/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 设置管理处理程序（settings management handlers） → 缓冲区类型（Buffer type）

**配置项引用（Symbol References）**：[`CONFIG_HEAP_MEM_POOL_SIZE`](P001_kernel_配置项参考_1.md#CONFIG_HEAP_MEM_POOL_SIZE)、[`CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE)。

<a id="CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE_STACK"></a>

## 385.77 `CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE_STACK`

**提示（Prompt）**：栈，固定大小（Stack, fixed size）

**说明（Help）**

使用固定大小的栈缓冲区，拒绝超出其长度的用户输入值。仅参数存储的栈占用就为 `MCUMGR_GRP_SETTINGS_NAME_LEN + MCUMGR_GRP_SETTINGS_VALUE_LEN`，因此应相应设置 MCUmgr 栈大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE>
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/settings_mgmt/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/settings_mgmt/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 设置管理处理程序（settings management handlers） → 缓冲区类型（Buffer type）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_SETTINGS_BUFFER_TYPE)。

<a id="CONFIG_MCUMGR_GRP_SETTINGS_NAME_LEN"></a>

## 385.78 `CONFIG_MCUMGR_GRP_SETTINGS_NAME_LEN`

**提示（Prompt）**：设置名称最大长度（Maximum setting name length）

**说明（Help）**

待查找键（key）的最大长度。变量放在栈上时，此值为其大小；放在堆上时，此值为可分配的最大大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_SETTINGS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/settings_mgmt/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/settings_mgmt/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 设置管理处理程序（settings management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_SETTINGS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_SETTINGS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_SETTINGS_VALUE_LEN"></a>

## 385.79 `CONFIG_MCUMGR_GRP_SETTINGS_VALUE_LEN`

**提示（Prompt）**：设置值最大长度（Maximum setting value length）

**说明（Help）**

待读取值（value）的最大长度。变量放在栈上时，此值为其大小；放在堆上时，此值为实际分配大小，因为设置子系统（settings）不支持在查找之前先获取值的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_SETTINGS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/settings_mgmt/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/settings_mgmt/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 设置管理处理程序（settings management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_SETTINGS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_SETTINGS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_SHELL"></a>

## 385.80 `CONFIG_MCUMGR_GRP_SHELL`

**提示（Prompt）**：MCUmgr 命令行管理处理程序（shell management handlers）

**说明（Help）**

启用 MCUmgr 命令行管理处理程序（shell management handlers）。处理程序使用虚拟后端（dummy backend）执行命令，将输出捕获到内部内存缓冲区，因此不会与用户操作范围以外的物理接口交互。其他命令行后端可与其配合使用，互不干扰。

`CONFIG_SHELL_BACKEND_DUMMY_BUF_SIZE` 决定可返回的命令输出字符数；输出被截断时，请增大该值，并相应设置 `MCUMGR_TRANSPORT_NETBUF_SIZE`。注意，接受的命令最大长度由 `CONFIG_SHELL_CMD_BUFF_SIZE` 决定，MCUmgr 会在栈上分配命令缓冲区。因此，启用 `MCUMGR_GRP_SHELL` 或更改 `CONFIG_SHELL_CMD_BUFF_SIZE`，都可能提高栈大小要求。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_SHELL_BACKEND_DUMMY && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/shell_mgmt/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/shell_mgmt/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_SHELL_BACKEND_DUMMY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_DUMMY)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`。

<a id="CONFIG_MCUMGR_GRP_SHELL_LEGACY_RC_RETURN_CODE"></a>

## 385.81 `CONFIG_MCUMGR_GRP_SHELL_LEGACY_RC_RETURN_CODE`

**提示（Prompt）**：旧版行为：用 rc 字段返回命令行函数返回码

**说明（Help）**

启用后恢复旧版行为：将命令行返回码错误地放入原本用于简单管理协议（SMP）处理错误的 `rc` 字段。禁用时，新增 `ret` 字段保存命令行命令退出码，而 `rc` 用于 SMP 处理错误码。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_SHELL && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/shell_mgmt/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/shell_mgmt/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 命令行管理处理程序（shell management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_SHELL`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_SHELL)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_STAT"></a>

## 385.82 `CONFIG_MCUMGR_GRP_STAT`

**提示（Prompt）**：MCUmgr 统计管理处理程序（statistics management handlers）

**说明（Help）**

启用 MCUmgr 统计管理处理程序（statistics management handlers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STATS && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2
CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3 if CONFIG_ZCBOR_CANONICAL
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/stat_mgmt/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/stat_mgmt/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers）

**配置项引用（Symbol References）**：[`CONFIG_STATS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STATS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3)、[`CONFIG_ZCBOR_CANONICAL`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR_CANONICAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`、`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3`。

<a id="CONFIG_MCUMGR_GRP_STAT_MAX_NAME_LEN"></a>

## 385.83 `CONFIG_MCUMGR_GRP_STAT_MAX_NAME_LEN`

**提示（Prompt）**：统计组名称最大长度（stat group name length）

**说明（Help）**

以字节为单位限制 MCUmgr 请求中的统计组名称长度。处理所有统计读取命令时，在栈上分配此大小的组名称缓冲区。若组名称超过此限制，就无法通过 `stat show` 命令获取其值。对于统计名称 `s_name` 和 `snm_name`，本项也是编码到 CBOR 时允许的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_STAT && CONFIG_MCUMGR_GRP_STAT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/stat_mgmt/Kconfig:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/stat_mgmt/Kconfig#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 统计管理处理程序（statistics management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_STAT`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_STAT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_TRANSPORT"></a>

## 385.84 `CONFIG_MCUMGR_GRP_TRANSPORT`

**提示（Prompt）**：MCUmgr 传输管理处理程序（transport management handlers）【实验性 EXPERIMENTAL】

**说明（Help）**

启用 MCUmgr 传输管理处理程序（transport management handlers）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2
CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3 if CONFIG_ZCBOR_CANONICAL
CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_2
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/transport_mgmt/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/transport_mgmt/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3)、[`CONFIG_ZCBOR_CANONICAL`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR_CANONICAL)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_2)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`、`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_3`、`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVEL_2`。

<a id="CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_FUNCTION"></a>

## 385.85 `CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_FUNCTION`

**提示（Prompt）**：从自定义函数获取（custom function）

**说明（Help）**

使用函数返回值设置传输组 ID（transport group ID），该 ID 可由应用或设备自定义。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_TYPE>
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/transport_mgmt/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/transport_mgmt/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 传输管理处理程序（transport management handlers）【实验性 EXPERIMENTAL】 → 组 ID 类型（Group ID type）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_TYPE`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_TYPE)。

<a id="CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_VALUE"></a>

## 385.86 `CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_VALUE`

**提示（Prompt）**：指定自定义值（custom value）

**说明（Help）**

使用 Kconfig 值设置传输组 ID（transport group ID），该 ID 可由应用或设备自定义。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_TYPE>
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/transport_mgmt/Kconfig:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/transport_mgmt/Kconfig#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 传输管理处理程序（transport management handlers）【实验性 EXPERIMENTAL】 → 组 ID 类型（Group ID type）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_TYPE`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_TYPE)。

<a id="CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_VALUE_GROUP_ID"></a>

## 385.87 `CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_VALUE_GROUP_ID`

**提示（Prompt）**：组 ID（Group ID）

**说明（Help）**

传输管理组（transport management group）使用的组索引（group index）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_VALUE && <choice CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_TYPE>
```

**取值范围（Ranges）**

```text
[64, 65535]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/transport_mgmt/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/transport_mgmt/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 传输管理处理程序（transport management handlers）【实验性 EXPERIMENTAL】 → 组 ID 类型（Group ID type） → 指定自定义值（custom value）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_VALUE`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_VALUE)、[`CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_TYPE`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_TYPE)。

<a id="CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_DEFAULT"></a>

## 385.88 `CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用全局默认传输组 ID（transport group ID），具有通用兼容性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_TYPE>
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/transport_mgmt/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/transport_mgmt/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 传输管理处理程序（transport management handlers）【实验性 EXPERIMENTAL】 → 组 ID 类型（Group ID type）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_TYPE`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_TYPE)。

<a id="CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_TYPE"></a>

## 385.89 `CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_TYPE`

**提示（Prompt）**：组 ID 类型（Group ID type）

**说明（Help）**

指定 MCUmgr 命令组 ID（command group ID）的定义方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_TRANSPORT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_DEFAULT
CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_VALUE
CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_FUNCTION
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/transport_mgmt/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/transport_mgmt/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 传输管理处理程序（transport management handlers）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_TRANSPORT`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_TRANSPORT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_DEFAULT`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_DEFAULT)、[`CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_VALUE`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_VALUE)、[`CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_FUNCTION`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_TRANSPORT_GROUP_ID_CUSTOM_FUNCTION)。

<a id="CONFIG_MCUMGR_GRP_TRANSPORT_INFO_FUNCTIONS"></a>

## 385.90 `CONFIG_MCUMGR_GRP_TRANSPORT_INFO_FUNCTIONS`

**提示（Prompt）**：信息函数（Info functions）

**说明（Help）**

禁用后移除信息函数，可在传输布局（transport layout）固定或已知的设备上节省资源。但这会使实现不再符合传输管理组规范，因此只有使用自定义组 ID 时才允许禁用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_TRANSPORT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/transport_mgmt/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/transport_mgmt/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 传输管理处理程序（transport management handlers）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_TRANSPORT`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_TRANSPORT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_TRANSPORT_LOCKING"></a>

## 385.91 `CONFIG_MCUMGR_GRP_TRANSPORT_LOCKING`

**提示（Prompt）**：信号量锁定（Semaphore locking）

**说明（Help）**

启用后，通过信号量（semaphore）防止桥接变量（bridge variables）被并发访问。确定不会并发使用这些资源的系统可禁用，以减少资源占用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_TRANSPORT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/transport_mgmt/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/transport_mgmt/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 传输管理处理程序（transport management handlers）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_TRANSPORT`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_TRANSPORT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_TRANSPORT_MAX_BRIDGES"></a>

## 385.92 `CONFIG_MCUMGR_GRP_TRANSPORT_MAX_BRIDGES`

**提示（Prompt）**：最大桥接数量（Maximum bridges）

**说明（Help）**

支持的并发桥接数量上限。注意，这是桥接基础设施本身的限制，具体传输实现的并发桥接上限可能更低。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_TRANSPORT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 128]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/transport_mgmt/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/transport_mgmt/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 传输管理处理程序（transport management handlers）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_TRANSPORT`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_TRANSPORT)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_ZBASIC"></a>

## 385.93 `CONFIG_MCUMGR_GRP_ZBASIC`

**提示（Prompt）**：Zephyr 专用基础命令组（basic group of commands）

**说明（Help）**

允许 MCUmgr 处理 Zephyr 专用命令组（groups）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/zephyr_basic/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/zephyr_basic/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_ZBASIC_STORAGE_ERASE"></a>

## 385.94 `CONFIG_MCUMGR_GRP_ZBASIC_STORAGE_ERASE`

**提示（Prompt）**：存储擦除命令（Storage erase command）

**说明（Help）**

启用用于擦除存储分区（storage partition）的命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH_MAP && CONFIG_MCUMGR_GRP_ZBASIC && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/zephyr_basic/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/zephyr_basic/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → Zephyr 专用基础命令组（basic group of commands）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_MAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MAP)、[`CONFIG_MCUMGR_GRP_ZBASIC`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_GRP_ZBASIC)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_MGMT_CUSTOM_PAYLOAD"></a>

## 385.95 `CONFIG_MCUMGR_MGMT_CUSTOM_PAYLOAD`

**提示（Prompt）**：MCUmgr 自定义载荷（custom payload）

**说明（Help）**

启用后，用户可通过 `mgmt_handler` 的 `custom_payload` 字段，跳过 `smp_handle_single_payload` 中 CBOR 起始和结束字节的生成，改用用户定义的简单管理协议（SMP）消息载荷。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/mgmt/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/mgmt/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_MGMT_HANDLER_USER_DATA"></a>

## 385.96 `CONFIG_MCUMGR_MGMT_HANDLER_USER_DATA`

**提示（Prompt）**：MCUmgr 管理处理程序的用户数据支持（user data）

**说明（Help）**

在 `struct mgmt_handler` 中增加字段，使用户能够在调用所定义的处理程序时传入 `user_data`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/mgmt/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/mgmt/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS"></a>

## 385.97 `CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS`

**提示（Prompt）**：MCUmgr 通知钩子支持（notification hook）

**说明（Help）**

启用后，应用或其他代码可注册 MCUmgr 事件通知（event notifications），在相应事件发生时获得回调。本项仅启用基础通知机制，本身不启用具体通知；具体通知需选择其他 Kconfig 选项。

代码中需调用 `mgmt_callback_register()`，提供回调函数和希望接收的事件。可注册多个处理程序，事件发生时会全部调用。某些回调可向调用方返回状态，以接受或拒绝当前操作：返回 `false` 表示应拒绝请求；对于仅告知信息或允许操作的情形，所有已注册通知处理程序都必须返回 `true`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/mgmt/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/mgmt/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_SMP_CBOR_MAX_DECODING_LEVELS"></a>

## 385.98 `CONFIG_MCUMGR_SMP_CBOR_MAX_DECODING_LEVELS`

**提示（Prompt）**：SMP 解码允许的映射／列表嵌套层数

**说明（Help）**

不同命令组解码时允许的最大映射／列表嵌套层数（map/list encapsulations）。不提供 CBOR 编码载荷的 SMP 命令／组无此要求；提供 CBOR 载荷的命令至少需要 1 层，每增加一层映射或列表封装，再增加一层。例如，命令接受参数映射作为载荷时，需要 2 层。

此值对应 zcbor 备份状态（backup states）数量，每增加 `1`，`cbor_nb_reader` 结构体就增加一个 `zcbor_state_t` 的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVELS
```

**取值范围（Ranges）**

```text
[CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVELS, 15]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/smp/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/smp/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVELS`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVELS)。

<a id="CONFIG_MCUMGR_SMP_CBOR_MAX_ENCODING_LEVELS"></a>

## 385.99 `CONFIG_MCUMGR_SMP_CBOR_MAX_ENCODING_LEVELS`

**提示（Prompt）**：SMP 编码允许的映射／列表嵌套层数

**说明（Help）**

不同命令组编码时允许的最大映射／列表嵌套层数（map/list encapsulations）。此值对应 zcbor 备份状态数量，每增加 `1`，`cbor_nb_writer` 结构体就增加一个 `zcbor_state_t` 的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVELS
```

**取值范围（Ranges）**

```text
[CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVELS, 15]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/smp/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/smp/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVELS`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_SMP_CBOR_MIN_ENCODING_LEVELS)。

<a id="CONFIG_MCUMGR_SMP_CBOR_MAX_MAIN_MAP_ENTRIES"></a>

## 385.100 `CONFIG_MCUMGR_SMP_CBOR_MAX_MAIN_MAP_ENTRIES`

**提示（Prompt）**：主响应映射条目数量的预计上限

**说明（Help）**

包含响应全部内容的主映射（main response map）中，预计条目数量的上限。zcbor 使用此值预测所需映射编码，不影响内存分配或使用量。内置命令处理程序很少直接向主映射加入大量数据，通常创建子映射，因此默认值适用。如果应用直接向主映射添加字段而不另行封装，并开始出现编码失败，可能需要增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
15
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/smp/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/smp/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<!-- kconfig-navigation -->

[上一章](P384_subsys_mgmt_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P386_subsys_mgmt_配置项参考_3.md)
