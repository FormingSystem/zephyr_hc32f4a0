---
id: learning.zephyr-docs.cmake-reference.module.sysbuild_extensions
title: sysbuild_extensions
kind: reference
status: maintained
domains: [zephyr, cmake]
source_url: https://docs.zephyrproject.org/latest/build/cmake-ref/module/sysbuild_extensions.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_sysbuild_extensions

原文：[sysbuild_extensions](https://docs.zephyrproject.org/latest/build/cmake-ref/module/sysbuild_extensions.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

<a id="module:sysbuild_extensions"></a>

本模块提供 Sysbuild 的 CMake 扩展命令（Extension Command），用于描述 Sysbuild 配置：哪些镜像（Image）参与构建、如何配置这些镜像，以及配置和烧录它们的顺序。

参与 Sysbuild 构建的任何应用或 Zephyr 模块，都可以在其 `sysbuild.cmake` 文件中使用下列命令。此处未记录的命令供 Sysbuild 自身使用，可能不经提前通知就被删除、重命名或改变用途。

## 10.1\_为镜像设置Kconfig值（Setting Kconfig Values on an Image）

> 译注：官方页面在此使用上述标题，但下面先介绍读取变量、添加镜像和设置缓存的命令；具体的 Kconfig 写入命令列在后面的同名小节中。这里保留原文的组织顺序。

<a id="command:sysbuild-get"></a>

### 10.1.1\_sysbuild_get

`sysbuild_get(<variable> IMAGE <image> [VAR <image-variable>] <KCONFIG|CACHE>)`

从镜像读取 CMake 缓存变量（Cache Variable）或 Kconfig 设置。只有镜像配置完成后，Sysbuild 才能读取它，例如在 Sysbuild 模块的 CMake 后置钩子（Post-CMake Hook）中读取。

若给出 `VAR`，使用该参数指定的名称查找；若未给出，则用 `<variable>` 同时作为查找名称和返回值变量。结果返回到 `<variable>`。

| 参数 | 含义 |
| --- | --- |
| `<variable>` | 返回值变量；未提供 `VAR` 时，也作为查找变量 |
| `IMAGE <image>` | 要从中读取变量的镜像名称 |
| `VAR <image-variable>` | 要查找的变量名称 |
| `KCONFIG` | 表示读取 Kconfig 设置的标志 |
| `CACHE` | 表示读取 CMake 缓存变量的标志 |

示例依次从 `my_sample` 的 CMake 缓存读取 `PROJECT_NAME` 到同名变量、读取同一项到 `my_sample_PROJECT_NAME`，以及读取 Kconfig 设置 `CONFIG_FOO`：

```cmake
# Look up PROJECT_NAME from the CMake cache of `my_sample` and return it
# in the local variable `PROJECT_NAME`.
sysbuild_get(PROJECT_NAME IMAGE my_sample CACHE)

# Same lookup, but returned in `my_sample_PROJECT_NAME`.
sysbuild_get(my_sample_PROJECT_NAME IMAGE my_sample VAR PROJECT_NAME CACHE)

# Look up the Kconfig setting CONFIG_FOO of `my_sample`.
sysbuild_get(my_sample_CONFIG_FOO IMAGE my_sample VAR CONFIG_FOO KCONFIG)
```

<a id="command:externalzephyrproject-add-application"></a>

### 10.1.2\_ExternalZephyrProject_Add

`ExternalZephyrProject_Add(APPLICATION <name> SOURCE_DIR <dir> [BOARD <board> [BOARD_REVISION <revision>]] [APP_TYPE <MAIN|BOOTLOADER|FIRMWARE_LOADER>] [BUILD_ONLY <bool>] )`

将一个基于 Zephyr 的构建系统纳入多镜像构建系统（Multi-image Build System）。

- `APPLICATION <name>`：应用名称，也用作应用的构建文件夹名称。
- `SOURCE_DIR <dir>`：应用源目录。
- `BOARD <board>`：应用构建使用 `<board>`，替代用户定义的 `BOARD`。
- `BOARD_REVISION <revision>`：应用使用 `<board>` 的 `<revision>` 修订版；仅在同时提供 `BOARD` 时有效。
- `APP_TYPE <MAIN|BOOTLOADER|FIRMWARE_LOADER>`：应用类型。
- `BUILD_ONLY <bool>`：将应用标为仅构建（Build-only）。若 `<bool>` 求值为真，此应用不参与烧录和调试。

应用类型的含义如下：

- `MAIN`：主应用。除多镜像构建标志外，用户定义的设置应原样传给它。例如，`-DCONF_FILE=<files>` 会不作修改地传给主应用。
- `BOOTLOADER`：引导加载程序（Bootloader）。
- `FIRMWARE_LOADER`：MCUboot 的固件加载器镜像（Firmware Loader Image）。

完整示例见“向 Sysbuild 添加 Zephyr 应用”（Adding Zephyr Applications to Sysbuild）。

<a id="command:externalzephyrvariantproject-add-application"></a>

### 10.1.3\_ExternalZephyrVariantProject_Add

`ExternalZephyrVariantProject_Add(APPLICATION <name> SOURCE_APP <name> [SNIPPET <snippet>] [EXTRA_DTC_OVERLAY_FILE <file>] [EXTRA_CONF_FILE <file>] [BUILD_ONLY <bool>] )`

复制一个已有的 Zephyr 构建系统，施加指定修改后加入多镜像构建系统。它不会创建 `ExternalZephyrProject_Add()` 添加的额外构建目标，例如 `<app>_menuconfig`。

**注意：**必须为变体镜像（Variant Image）添加 `CONF_FILE`、`EXTRA_CONF_FILE`、`EXTRA_DTC_OVERLAY_FILE` 或 `SNIPPET` 中的一项；否则镜像无效，配置镜像时会产生致命错误（Fatal Error）。

| 参数 | 含义 |
| --- | --- |
| `APPLICATION <name>` | 应用名称，也用作应用构建文件夹名称 |
| `SOURCE_APP <name>` | 要复制的已有镜像名称 |
| `SNIPPET <snippet>` | 默认应用到变体镜像的配置片段（Snippet）列表 |
| `EXTRA_DTC_OVERLAY_FILE <file>` | 默认应用到变体镜像的额外设备树覆盖文件（Devicetree Overlay File）列表 |
| `EXTRA_CONF_FILE <file>` | 默认应用到变体镜像的额外 Kconfig 配置片段（Kconfig Fragment）列表 |
| `BUILD_ONLY <bool>` | 仅构建标志；求值为真时，应用不参与烧录和调试 |

<a id="command:sysbuild-cache-set-var"></a>

### 10.1.4\_sysbuild_cache_set

`sysbuild_cache_set(VAR <variable> [APPEND [REMOVE_DUPLICATES]] <value>)`

设置 Sysbuild 缓存变量，使镜像能够访问它。结果返回到 `<variable>`。

- `VAR <variable>`：CMake 缓存中的变量名称。
- `APPEND`：若指定，以列表形式将给定数据追加到已有值。
- `REMOVE_DUPLICATES`：若指定，在保存到缓存之前移除列表中的重复条目。
- `<value>`：要设置或更新的值。

示例向 CMake 缓存的 `ATTRIBUTES` 列表添加 `battery`，并移除重复条目：

```cmake
# Add `battery` to the `ATTRIBUTES` list in the CMake cache, removing
# any duplicates from the list.
sysbuild_cache_set(VAR ATTRIBUTES APPEND REMOVE_DUPLICATES battery)
```

## 10.2\_为镜像设置Kconfig值（Setting Kconfig Values on an Image）

下列命令向 `<image>` 添加一行 Kconfig 配置片段，是 `sysbuild.cmake` 配置其所添加镜像的受支持方式。

收集的片段作为强制输入配置（Forced Input Configuration）传给镜像，因此最后应用，优先于镜像自身的 Kconfig 片段。它们与 `SB_CONFIG_` 选项的关系见“Kconfig 命名空间”（Kconfig Namespacing）。

<a id="command:set-config-bool"></a>

### 10.2.1\_set_config_bool

`set_config_bool(<image> <setting> <value>)`

若 `<value>` 求值为真，将布尔 Kconfig 选项设为 `y`，否则设为 `n`。

<a id="command:set-config-string"></a>

### 10.2.2\_set_config_string

`set_config_string(<image> <setting> <value>)`

将字符串 Kconfig 选项设为 `<value>`。

<a id="command:set-config-int"></a>

### 10.2.3\_set_config_int

`set_config_int(<image> <setting> <value>)`

将整数或十六进制（`int` 或 `hex`）Kconfig 选项设为 `<value>`。

以下示例分别设置主镜像的 MCUboot 引导选项、签名密钥文件，以及 `mcuboot` 镜像的最大日志级别：

```cmake
set_config_bool(${DEFAULT_IMAGE} CONFIG_BOOTLOADER_MCUBOOT y)
set_config_string(${DEFAULT_IMAGE} CONFIG_MCUBOOT_SIGNATURE_KEY_FILE "${keyfile}")
set_config_int(mcuboot CONFIG_LOG_MAX_LEVEL 2)
```

## 10.3\_递归添加与依赖顺序

<a id="command:sysbuild-add-subdirectory"></a>

### 10.3.1\_sysbuild_add_subdirectory

`sysbuild_add_subdirectory(<source_dir> [<binary_dir>])`

添加子目录，并递归处理它所添加的 Sysbuild 镜像。此命令扩展 `add_subdirectory`，对通过 `<source_dir>` 添加的镜像进行额外的递归处理。

退出 `<source_dir>` 后，命令检查截至此时已添加的每个镜像；若找到其 `sysbuild.cmake`，则用 `include()` 加载。如果此时又添加了更多镜像，也加载这些镜像的 `sysbuild.cmake`，依此继续，直到所有预期镜像均已添加才返回。

<a id="command:sysbuild-add-dependencies"></a>

### 10.3.2\_sysbuild_add_dependencies

`sysbuild_add_dependencies(<CONFIGURE | FLASH> <image> [<image-dependency> ...])`

使一个镜像在配置或烧录顺序上依赖其他镜像。每个 `<image-dependency>` 都排在 `<image>` 之前。

- `CONFIGURE`：添加 CMake 配置依赖（Configuration Dependency），决定镜像配置顺序。
- `FLASH`：添加烧录依赖（Flashing Dependency），决定全部镜像在 `domains.yaml` 中出现的顺序。

完整示例见“添加 Zephyr 应用之间的依赖”（Adding Dependencies among Zephyr Applications）。

<a id="command:sysbuild-images-order"></a>

### 10.3.3\_sysbuild_images_order

`sysbuild_images_order(<variable> <CONFIGURE | FLASH> IMAGES <images>)`

对给定的 `<images>` 排序，使其满足通过 `sysbuild_add_dependencies()` 指定的依赖关系。结果返回到 `<variable>`。

## 10.4\_原文相关链接

- [sysbuild](https://docs.zephyrproject.org/latest/build/sysbuild/index.html#sysbuild)
- [sysbuild-module-integration](https://docs.zephyrproject.org/latest/develop/modules.html#sysbuild-module-integration)
- [variable:BOARD](P027_BOARD.md#variable:BOARD)
- [sysbuild-zephyr-application](https://docs.zephyrproject.org/latest/build/sysbuild/index.html#sysbuild-zephyr-application)
- [variable:CONF_FILE](P035_CONF_FILE.md#variable:CONF_FILE)
- [variable:EXTRA_CONF_FILE](P039_EXTRA_CONF_FILE.md#variable:EXTRA_CONF_FILE)
- [variable:EXTRA_DTC_OVERLAY_FILE](P040_EXTRA_DTC_OVERLAY_FILE.md#variable:EXTRA_DTC_OVERLAY_FILE)
- [sysbuild-kconfig-namespacing](https://docs.zephyrproject.org/latest/build/sysbuild/index.html#sysbuild-kconfig-namespacing)
- [command:add_subdirectory](https://cmake.org/cmake/help/latest/command/add_subdirectory.html#command:add_subdirectory)
- [command:include](https://cmake.org/cmake/help/latest/command/include.html#command:include)
- [sysbuild-zephyr-application-dependencies](https://docs.zephyrproject.org/latest/build/sysbuild/index.html#sysbuild-zephyr-application-dependencies)

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：kconfig](P009_kconfig.md) · [本模块主线目录](../reading/cmake_reference.md) · [全部主线](../reading/README.md) · [下一篇：sysbuild_kconfig](P011_sysbuild_kconfig.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P009_kconfig.md) · [返回大纲](大纲.md) · [下一章](P011_sysbuild_kconfig.md)

</details>

<!-- reading-navigation:end -->
