---
id: learning.zephyr-docs.kconfig-reference.page-319
title: "`subsys/bindesc`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第319章\_`subsys/bindesc`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/bindesc` 的 43 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BINDESC"></a>

## 319.1 `CONFIG_BINDESC`

**提示（Prompt）**：二进制描述符（Binary Descriptors）

**说明（Help）**

二进制描述符（Binary Descriptors）：可在可执行映像之外访问的常量数据

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_SUPPORTS_ROM_START || CONFIG_ARCH_POSIX
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_SUPPORTS_ROM_START`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_SUPPORTS_ROM_START)、[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_SUPPORTS_ROM_START`。

<a id="CONFIG_BINDESC_APP_BUILD_VERSION"></a>

## 319.2 `CONFIG_BINDESC_APP_BUILD_VERSION`

**提示（Prompt）**：应用 Git 引用（App git reference）

**说明（Help）**

应用程序的 Git 引用（git reference），例如 `"v3.3.0-18-g2c85d9224fca"`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_VERSION && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.version:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.version#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 版本二进制描述符（Version binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_VERSION`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_VERSION)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_APP_VERSION_MAJOR"></a>

## 319.3 `CONFIG_BINDESC_APP_VERSION_MAJOR`

**提示（Prompt）**：应用主版本号（App version major）

**说明（Help）**

应用程序的主版本号（major version number），例如 `1.0.0` 中的 `1`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_VERSION && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.version:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.version#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 版本二进制描述符（Version binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_VERSION`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_VERSION)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_APP_VERSION_MINOR"></a>

## 319.4 `CONFIG_BINDESC_APP_VERSION_MINOR`

**提示（Prompt）**：应用次版本号（App version minor）

**说明（Help）**

应用程序的次版本号（minor version number），例如 `1.0.0` 中的 `0`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_VERSION && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.version:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.version#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 版本二进制描述符（Version binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_VERSION`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_VERSION)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_APP_VERSION_NUMBER"></a>

## 319.5 `CONFIG_BINDESC_APP_VERSION_NUMBER`

**提示（Prompt）**：应用版本数值（App version number）

**说明（Help）**

应用版本的数值表示；原文称其为二进制编码的十进制数（binary coded decimal），计算公式为 `(major << 16 | minor << 8 | patchlevel)`。例如，`1.0.0` 表示为 `0x10000`。

译注：这里保留原文术语；给出的公式实际按位拼接各版本分量，不应将其理解为逐十进制数字编码的常规 BCD。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_VERSION && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.version:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.version#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 版本二进制描述符（Version binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_VERSION`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_VERSION)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_APP_VERSION_PATCHLEVEL"></a>

## 319.6 `CONFIG_BINDESC_APP_VERSION_PATCHLEVEL`

**提示（Prompt）**：应用补丁版本号（App version patchlevel）

**说明（Help）**

应用程序的补丁版本号（patchlevel version number），例如 `1.0.0` 中的 `0`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_VERSION && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.version:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.version#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 版本二进制描述符（Version binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_VERSION`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_VERSION)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_APP_VERSION_STRING"></a>

## 319.7 `CONFIG_BINDESC_APP_VERSION_STRING`

**提示（Prompt）**：应用版本字符串（App version string）

**说明（Help）**

应用程序的版本字符串（version string），例如 `"1.0.0"`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_VERSION && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.version:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.version#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 版本二进制描述符（Version binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_VERSION`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_VERSION)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_BUILD_DATE_STRING"></a>

## 319.8 `CONFIG_BINDESC_BUILD_DATE_STRING`

**提示（Prompt）**：字符串形式的构建日期（Build date as string）

**说明（Help）**

字符串形式的编译日期（date of compilation），例如 `"2023-09-29"`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_BUILD_TIME && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.build_time:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.build_time#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 构建时间二进制描述符（Build Time binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_BUILD_TIME`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_BUILD_TIME)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_BUILD_DATE_STRING_FORMAT"></a>

## 319.9 `CONFIG_BINDESC_BUILD_DATE_STRING_FORMAT`

**提示（Prompt）**：日期格式（Date format）

**说明（Help）**

构建日期字符串（build date string）的格式。该值传递给 CMake 的 `string(TIMESTAMP ...)` 函数；不同格式的详细说明请参阅 `string` 的文档。尝试复现映像（reproduce an image）时，也可用它指定一个固定时间。例如，将格式设为 `"2023-02-05"`，无论实际构建时间是什么，构建时间都会设为该值。默认格式示例：`2023-02-05`。注意：默认格式符合 ISO-8601。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_BUILD_TIME && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**默认值（Defaults）**

```text
"%Y-%m-%d"
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.build_time:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.build_time#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 构建时间二进制描述符（Build Time binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_BUILD_TIME`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_BUILD_TIME)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_BUILD_DATE_TIME_STRING"></a>

## 319.10 `CONFIG_BINDESC_BUILD_DATE_TIME_STRING`

**提示（Prompt）**：字符串形式的构建日期与时间（Build date and time as string）

**说明（Help）**

字符串形式的编译日期与时间（date and time of compilation），例如 `"2023-09-29T17:43:14+0000"`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_BUILD_TIME && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.build_time:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.build_time#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 构建时间二进制描述符（Build Time binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_BUILD_TIME`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_BUILD_TIME)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_BUILD_DATE_TIME_STRING_FORMAT"></a>

## 319.11 `CONFIG_BINDESC_BUILD_DATE_TIME_STRING_FORMAT`

**提示（Prompt）**：日期时间格式（Date-Time format）

**说明（Help）**

构建时间字符串（build time string）的格式。该值传递给 CMake 的 `string(TIMESTAMP ...)` 函数；不同格式的详细说明请参阅 `string` 的文档。尝试复现映像（reproduce an image）时，也可用它指定一个固定时间。例如，将格式设为 `"2023-02-05T00:07:04+0000"`，无论实际构建时间是什么，构建时间都会设为该值。如果启用了 `BINDESC_BUILD_TIME_USE_LOCAL_TIME`，时间采用本地时间（local time），否则采用协调世界时（UTC）。默认格式示例：`2023-09-29T17:43:14+0000`。注意：默认格式符合 ISO-8601。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_BUILD_TIME && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**默认值（Defaults）**

```text
"%Y-%m-%dT%H:%M:%S%z"
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.build_time:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.build_time#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 构建时间二进制描述符（Build Time binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_BUILD_TIME`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_BUILD_TIME)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_BUILD_TIME_ALWAYS_REBUILD"></a>

## 319.12 `CONFIG_BINDESC_BUILD_TIME_ALWAYS_REBUILD`

**提示（Prompt）**：始终重新构建（Always rebuild）

**说明（Help）**

启用后，包含构建时间定义（build time definitions）的文件始终重新构建。这样能让时间戳（timestamp）始终准确，但构建耗时也会稍有增加。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_BUILD_TIME && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.build_time:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.build_time#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 构建时间二进制描述符（Build Time binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_BUILD_TIME`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_BUILD_TIME)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_BUILD_TIME_DAY"></a>

## 319.13 `CONFIG_BINDESC_BUILD_TIME_DAY`

**提示（Prompt）**：构建日（Day of build）

**说明（Help）**

映像编译日期在当月中的日数（day of the month），例如 `9`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_BUILD_TIME && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.build_time:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.build_time#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 构建时间二进制描述符（Build Time binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_BUILD_TIME`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_BUILD_TIME)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_BUILD_TIME_HOUR"></a>

## 319.14 `CONFIG_BINDESC_BUILD_TIME_HOUR`

**提示（Prompt）**：构建小时（Hour of build）

**说明（Help）**

映像编译时刻在当天中的小时数（hour of the day），例如 `13:34:52` 中的 `13`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_BUILD_TIME && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.build_time:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.build_time#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 构建时间二进制描述符（Build Time binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_BUILD_TIME`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_BUILD_TIME)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_BUILD_TIME_MINUTE"></a>

## 319.15 `CONFIG_BINDESC_BUILD_TIME_MINUTE`

**提示（Prompt）**：构建分钟（Minute of build）

**说明（Help）**

映像编译时刻的分钟数（minute），例如 `13:34:52` 中的 `34`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_BUILD_TIME && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.build_time:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.build_time#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 构建时间二进制描述符（Build Time binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_BUILD_TIME`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_BUILD_TIME)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_BUILD_TIME_MONTH"></a>

## 319.16 `CONFIG_BINDESC_BUILD_TIME_MONTH`

**提示（Prompt）**：构建月份（Month of build）

**说明（Help）**

映像编译日期的月份（month），例如 `5`（五月，May）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_BUILD_TIME && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.build_time:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.build_time#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 构建时间二进制描述符（Build Time binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_BUILD_TIME`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_BUILD_TIME)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_BUILD_TIME_SECOND"></a>

## 319.17 `CONFIG_BINDESC_BUILD_TIME_SECOND`

**提示（Prompt）**：构建秒数（Second of build）

**说明（Help）**

映像编译时刻的秒数（second），例如 `13:34:52` 中的 `52`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_BUILD_TIME && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.build_time:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.build_time#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 构建时间二进制描述符（Build Time binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_BUILD_TIME`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_BUILD_TIME)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_BUILD_TIME_STRING"></a>

## 319.18 `CONFIG_BINDESC_BUILD_TIME_STRING`

**提示（Prompt）**：字符串形式的构建时间（Build time as string）

**说明（Help）**

字符串形式的编译时间（time of compilation），例如 `"T17:43:14+0000"`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_BUILD_TIME && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.build_time:71`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.build_time#L71)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 构建时间二进制描述符（Build Time binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_BUILD_TIME`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_BUILD_TIME)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_BUILD_TIME_STRING_FORMAT"></a>

## 319.19 `CONFIG_BINDESC_BUILD_TIME_STRING_FORMAT`

**提示（Prompt）**：时间格式（Time format）

**说明（Help）**

构建时间字符串（build time string）的格式。该值传递给 CMake 的 `string(TIMESTAMP ...)` 函数；不同格式的详细说明请参阅 `string` 的文档。尝试复现映像（reproduce an image）时，也可用它指定一个固定时间。例如，将格式设为 `"T00:07:04+0000"`，无论实际构建时间是什么，构建时间都会设为该值。默认格式示例：`T00:07:04+0000`。注意：默认格式符合 ISO-8601。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_BUILD_TIME && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**默认值（Defaults）**

```text
"T%H:%M:%S%z"
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.build_time:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.build_time#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 构建时间二进制描述符（Build Time binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_BUILD_TIME`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_BUILD_TIME)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_BUILD_TIME_UNIX"></a>

## 319.20 `CONFIG_BINDESC_BUILD_TIME_UNIX`

**提示（Prompt）**：UNIX 时间形式的构建时间（Build time as UNIX time）

**说明（Help）**

映像编译时的 UNIX 时间（UNIX time）。这是一个整数，表示自 1970 年 1 月 1 日午夜起经过的秒数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_BUILD_TIME && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.build_time:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.build_time#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 构建时间二进制描述符（Build Time binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_BUILD_TIME`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_BUILD_TIME)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_BUILD_TIME_USE_LOCAL_TIME"></a>

## 319.21 `CONFIG_BINDESC_BUILD_TIME_USE_LOCAL_TIME`

**提示（Prompt）**：使用本地时间（Use local time）

**说明（Help）**

启用后，描述符（descriptors）中的构建时间使用本地时间（local time），而非协调世界时（UTC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_BUILD_TIME && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.build_time:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.build_time#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 构建时间二进制描述符（Build Time binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_BUILD_TIME`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_BUILD_TIME)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_BUILD_TIME_YEAR"></a>

## 319.22 `CONFIG_BINDESC_BUILD_TIME_YEAR`

**提示（Prompt）**：构建年份（Year of build）

**说明（Help）**

映像编译日期的年份（year），例如 `2023`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_BUILD_TIME && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.build_time:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.build_time#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 构建时间二进制描述符（Build Time binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_BUILD_TIME`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_BUILD_TIME)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_CXX_COMPILER_NAME"></a>

## 319.23 `CONFIG_BINDESC_CXX_COMPILER_NAME`

**提示（Prompt）**：C++ 编译器名称（C++ compiler name）

**说明（Help）**

C++ 编译器（C++ compiler）的名称，例如 `"GNU"`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_HOST_INFO && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.host_info:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.host_info#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 主机信息二进制描述符（Host info binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_HOST_INFO`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_HOST_INFO)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_CXX_COMPILER_VERSION"></a>

## 319.24 `CONFIG_BINDESC_CXX_COMPILER_VERSION`

**提示（Prompt）**：C++ 编译器版本（C++ compiler version）

**说明（Help）**

C++ 编译器（C++ compiler）的版本，例如 `"12.3.0"`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_HOST_INFO && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.host_info:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.host_info#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 主机信息二进制描述符（Host info binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_HOST_INFO`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_HOST_INFO)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_C_COMPILER_NAME"></a>

## 319.25 `CONFIG_BINDESC_C_COMPILER_NAME`

**提示（Prompt）**：C 编译器名称（C compiler name）

**说明（Help）**

C 编译器（C compiler）的名称，例如 `"GNU"`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_HOST_INFO && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.host_info:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.host_info#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 主机信息二进制描述符（Host info binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_HOST_INFO`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_HOST_INFO)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_C_COMPILER_VERSION"></a>

## 319.26 `CONFIG_BINDESC_C_COMPILER_VERSION`

**提示（Prompt）**：C 编译器版本（C compiler version）

**说明（Help）**

C 编译器（C compiler）的版本，例如 `"12.3.0"`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_HOST_INFO && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.host_info:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.host_info#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 主机信息二进制描述符（Host info binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_HOST_INFO`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_HOST_INFO)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_DEFINE"></a>

## 319.27 `CONFIG_BINDESC_DEFINE`

**提示（Prompt）**：二进制描述符定义（Binary Descriptors Define）

**说明（Help）**

允许应用定义自己的二进制描述符（binary descriptors）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_DEFINE_BUILD_TIME"></a>

## 319.28 `CONFIG_BINDESC_DEFINE_BUILD_TIME`

**提示（Prompt）**：构建时间二进制描述符（Build Time binary descriptors）

**说明（Help）**

添加构建时间二进制描述符（build time binary descriptors）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.build_time:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.build_time#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_DEFINE_HOST_INFO"></a>

## 319.29 `CONFIG_BINDESC_DEFINE_HOST_INFO`

**提示（Prompt）**：主机信息二进制描述符（Host info binary descriptors）

**说明（Help）**

添加主机信息二进制描述符（host info binary descriptors）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.host_info:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.host_info#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_DEFINE_MAX_DATA_SIZE"></a>

## 319.30 `CONFIG_BINDESC_DEFINE_MAX_DATA_SIZE`

**提示（Prompt）**：二进制描述符最大数据大小（Bindesc max data size）

**说明（Help）**

确定二进制描述符（binary descriptor）数据的最大大小。理论上限为 `uint16_t` 的最大值（`65535`）；实践中建议设置为远小于此上限的值，以便更容易处理数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[4, 65535]
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_DEFINE_VERSION"></a>

## 319.31 `CONFIG_BINDESC_DEFINE_VERSION`

**提示（Prompt）**：版本二进制描述符（Version binary descriptors）

**说明（Help）**

添加版本二进制描述符（version binary descriptors）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.version:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.version#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_HOST_NAME"></a>

## 319.32 `CONFIG_BINDESC_HOST_NAME`

**提示（Prompt）**：主机名称（Host name）

**说明（Help）**

编译映像所用主机（host）的名称。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_HOST_INFO && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.host_info:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.host_info#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 主机信息二进制描述符（Host info binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_HOST_INFO`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_HOST_INFO)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_KERNEL_BUILD_VERSION"></a>

## 319.33 `CONFIG_BINDESC_KERNEL_BUILD_VERSION`

**提示（Prompt）**：内核 Git 引用（Kernel git reference）

**说明（Help）**

内核的 Git 引用（git reference），例如 `"v3.3.0-18-g2c85d9224fca"`；也可在构建时覆盖，参见 `BUILD_VERSION`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_VERSION && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.version:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.version#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 版本二进制描述符（Version binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_VERSION`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_VERSION)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_KERNEL_VERSION_MAJOR"></a>

## 319.34 `CONFIG_BINDESC_KERNEL_VERSION_MAJOR`

**提示（Prompt）**：内核主版本号（Kernel version major）

**说明（Help）**

主版本号（major version number），例如 `3.4.0` 中的 `3`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_VERSION && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.version:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.version#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 版本二进制描述符（Version binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_VERSION`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_VERSION)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_KERNEL_VERSION_MINOR"></a>

## 319.35 `CONFIG_BINDESC_KERNEL_VERSION_MINOR`

**提示（Prompt）**：内核次版本号（Kernel version minor）

**说明（Help）**

次版本号（minor version number），例如 `3.4.0` 中的 `4`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_VERSION && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.version:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.version#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 版本二进制描述符（Version binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_VERSION`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_VERSION)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_KERNEL_VERSION_NUMBER"></a>

## 319.36 `CONFIG_BINDESC_KERNEL_VERSION_NUMBER`

**提示（Prompt）**：内核版本数值（Kernel version number）

**说明（Help）**

内核版本的数值表示；原文称其为二进制编码的十进制数（binary coded decimal），计算公式为 `(major << 16 | minor << 8 | patchlevel)`。例如，`3.4.0` 表示为 `0x30400`。

译注：这里保留原文术语；给出的公式实际按位拼接各版本分量，不应将其理解为逐十进制数字编码的常规 BCD。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_VERSION && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.version:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.version#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 版本二进制描述符（Version binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_VERSION`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_VERSION)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_KERNEL_VERSION_PATCHLEVEL"></a>

## 319.37 `CONFIG_BINDESC_KERNEL_VERSION_PATCHLEVEL`

**提示（Prompt）**：内核补丁版本号（Kernel version patchlevel）

**说明（Help）**

补丁版本号（patchlevel version number），例如 `3.4.0` 中的 `0`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_VERSION && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.version:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.version#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 版本二进制描述符（Version binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_VERSION`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_VERSION)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_KERNEL_VERSION_STRING"></a>

## 319.38 `CONFIG_BINDESC_KERNEL_VERSION_STRING`

**提示（Prompt）**：内核版本字符串（Kernel version string）

**说明（Help）**

内核版本字符串（kernel version string），例如 `"3.4.0"`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_DEFINE_VERSION && CONFIG_BINDESC_DEFINE && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig.version:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig.version#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 二进制描述符定义（Binary Descriptors Define） → 版本二进制描述符（Version binary descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_DEFINE_VERSION`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE_VERSION)、[`CONFIG_BINDESC_DEFINE`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_DEFINE)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_READ"></a>

## 319.39 `CONFIG_BINDESC_READ`

**提示（Prompt）**：读取二进制描述符（Binary Descriptors Read）

**说明（Help）**

允许应用读取另一个映像（image）的二进制描述符（binary descriptors）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_READ_FLASH"></a>

## 319.40 `CONFIG_BINDESC_READ_FLASH`

**提示（Prompt）**：从 Flash 读取二进制描述符（Bindesc read from flash）

**说明（Help）**

允许从非内存映射闪存（non memory mapped flash，例如外部 Flash）读取并解析二进制描述符（binary descriptors）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_READ && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 读取二进制描述符（Binary Descriptors Read）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_READ`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_READ)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_READ_FLASH_MAX_DATA_SIZE"></a>

## 319.41 `CONFIG_BINDESC_READ_FLASH_MAX_DATA_SIZE`

**提示（Prompt）**：从 Flash 读取二进制描述符时的最大数据大小（Bindesc read flash max data size）

**说明（Help）**

预期的描述符数据最大大小。应将其设为被读取映像采用的 `BINDESC_DEFINE_MAX_DATA_SIZE` 值。任何超过此大小的描述符（descriptor）都会被忽略。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_READ_FLASH && CONFIG_BINDESC_READ && CONFIG_BINDESC
```

**默认值（Defaults）**

```text
128
```

**取值范围（Ranges）**

```text
[4, 65535]
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 读取二进制描述符（Binary Descriptors Read） → 从 Flash 读取二进制描述符（Bindesc read from flash）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_READ_FLASH`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_READ_FLASH)、[`CONFIG_BINDESC_READ`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_READ)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_READ_MEMORY_MAPPED_FLASH"></a>

## 319.42 `CONFIG_BINDESC_READ_MEMORY_MAPPED_FLASH`

**提示（Prompt）**：从内存映射 Flash 读取二进制描述符（Bindesc read from memory mapped flash）

**说明（Help）**

允许从内存映射闪存（memory mapped flash）读取并解析二进制描述符（binary descriptors）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_READ && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 读取二进制描述符（Binary Descriptors Read）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_READ`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_READ)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<a id="CONFIG_BINDESC_READ_RAM"></a>

## 319.43 `CONFIG_BINDESC_READ_RAM`

**提示（Prompt）**：从 RAM 读取二进制描述符（Bindesc read from RAM）

**说明（Help）**

允许从随机存取存储器（RAM）读取并解析二进制描述符（binary descriptors）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BINDESC_READ && CONFIG_BINDESC
```

**定义位置（Location）**：[`subsys/bindesc/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/bindesc/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 二进制描述符（Binary Descriptors） → 读取二进制描述符（Binary Descriptors Read）

**配置项引用（Symbol References）**：[`CONFIG_BINDESC_READ`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC_READ)、[`CONFIG_BINDESC`](P319_subsys_bindesc_配置项参考.md#CONFIG_BINDESC)。

<!-- kconfig-navigation -->

[上一章](P318_subsys_authentication_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P320_subsys_bluetooth_配置项参考_1.md)
