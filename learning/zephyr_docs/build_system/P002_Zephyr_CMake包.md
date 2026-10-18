---
id: learning.zephyr-docs.build_system.cmake-package
title: Zephyr_CMake包
kind: reference
status: maintained
domains: [zephyr, build_system]
source_url: https://docs.zephyrproject.org/latest/build/zephyr_cmake_package.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第2章\_Zephyr_CMake包

原文：[Zephyr CMake Package](https://docs.zephyrproject.org/latest/build/zephyr_cmake_package.html)。读取日期：2026-10-12，`latest`。

**Zephyr CMake包（Zephyr CMake Package）**提供创建 Zephyr 应用的便捷入口，使 CMake 能自动选择用于构建应用的 Zephyr 安装。无论应用位于 Zephyr 仓库内、同一工作区内，还是独立于工作区之外，都可使用这一机制。三类应用的含义见[应用开发](../application/P001_应用开发.md)。

开发者在应用 `CMakeLists.txt` 开头写入 `find_package(Zephyr)`，即可让 CMake 查找并接入 Zephyr。原文要求先把所用 Zephyr 导出到 **CMake用户包注册表（CMake User Package Registry）**，即在当前用户的注册信息中建立到这套 Zephyr 安装的引用。

> 译注：这里的“包”是 CMake 能识别的配置入口，不是安装编译器的 SDK 压缩包；“导出”建立引用，不复制 Zephyr 源码，也不构建固件。显式环境提示及其他查找方式见后文，不能把包导出误认为每次构建都要重复执行的步骤。

## 2.1\_用户包注册位置

原文按系统列出的登记位置如下。Windows 的 `HKEY_CURRENT_USER` 表示当前用户注册表配置单元：

| 系统 | 登记位置及含义 |
| --- | --- |
| Ubuntu及其他Linux | 当前用户主目录下的 `.cmake/packages/Zephyr`，原写法为 `~/.cmake/packages/Zephyr`。 |
| macOS | 当前用户主目录下的 `.cmake/packages/Zephyr`，原写法同上。 |
| Windows | 当前用户注册表键 `HKEY_CURRENT_USER\Software\Kitware\CMake\Packages\Zephyr`。它是注册表位置，不是待创建的磁盘目录。 |

Zephyr CMake 包使 CMake 能自动找到 **Zephyr源码根（Zephyr Base）**。可导出一套或多套 Zephyr。开发、测试独立应用，或使用厂商派生版本的工作区应用时，多套登记很有用。具体注册表机制见 [CMake用户包注册表](https://cmake.org/cmake/help/latest/manual/cmake-packages.7.html#user-package-registry)。

## 2.2\_通过west导出

使用 west 安装 Zephyr 时，推荐通过 `west zephyr-export` 导出。该命令来自 Zephyr 提供的 west 扩展，应在能够发现当前 Zephyr 工作区的环境中运行。取得源码的官方说明见[入门指南](../getting_started/P002_入门指南.md)。

> 译注：该操作登记当前安装供以后查找，不是把另一套源码同步进当前仓库。若已有实验工作区，先核对当前工作区和 Zephyr 根，不为使用本页而重新初始化 west。

## 2.3\_不通过west导出

也可直接运行官方 CMake 脚本；`<PATH-TO-ZEPHYR>` 是目标 Zephyr 根目录路径占位符：

```sh
cmake -P <PATH-TO-ZEPHYR>/share/zephyr-package/cmake/zephyr_export.cmake
```

将 `<PATH-TO-ZEPHYR>` 替换为从当前终端工作目录到目标 Zephyr 根的正确路径。该命令把这套 Zephyr 加入 CMake 用户包注册表。`-P` 表示执行 CMake 脚本，不是配置应用源码目录。

## 2.4\_显式提供Zephyr根环境设置

查找机制允许使用环境变量显式指定 Zephyr 根。在应用 `CMakeLists.txt` 中使用：

```cmake
find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
```

这指示 CMake 先根据环境变量 `ZEPHYR_BASE` 查找，再使用正常搜索路径。`REQUIRED` 表示必须找到包，`HINTS` 提供搜索提示，`$ENV{ZEPHYR_BASE}` 读取环境变量值。变量的作用域与设置方式见[环境变量](https://docs.zephyrproject.org/latest/develop/env_vars.html#envvar-ZEPHYR_BASE)。

> 译注：应在实际调用 CMake 的终端中设置变量，并确认该终端所见值指向所需源码根。它与构建目录中已保存的 CMake 缓存不是同一层设置；已有缓存的处理见下一节。

## 2.5\_Zephyr包搜索顺序

不使用上节环境提示时，按以下应用位置选择匹配安装。

### 2.5.1\_仓库内应用

**Zephyr仓库应用（Zephyr Repository Application）**使用它所在的 Zephyr。例如：

```text
<projects>/zephyr-workspace/zephyr
└── samples
    └── hello_world
```

这里的示例应用 `hello_world` 使用 `<projects>/zephyr-workspace/zephyr`。

### 2.5.2\_工作区应用

**Zephyr工作区应用（Zephyr Workspace Application）**使用同一工作区内的 Zephyr。例如：

```text
<projects>/zephyr-workspace
├── zephyr
├── ...
└── my_applications
     └── my_first_app
```

示例应用 `my_first_app` 使用 `<projects>/zephyr-workspace/zephyr`，因为二者共享工作区。

> 原文注意：通过 west 安装工作区时，工作区根与 `west topdir` 输出一致。

### 2.5.3\_独立应用

**Zephyr独立应用（Zephyr Freestanding Application）**使用 CMake 用户包注册表中的 Zephyr。原文例子：

```text
<projects>/zephyr-workspace-1
└── zephyr                       (Not exported to CMake)

<projects>/zephyr-workspace-2
└── zephyr                       (Exported to CMake)

<home>/app
├── CMakeLists.txt
├── prj.conf
└── src
    └── main.c
```

其中只有 `zephyr-workspace-2/zephyr` 已导出到 CMake，`zephyr-workspace-1/zephyr` 没有导出，因此独立应用 `<home>/app` 使用第二套。

若要改用第一套测试，可以在运行 CMake 前，把 `ZEPHYR_BASE` 设置为 `<projects>/zephyr-workspace-1/zephyr`，并使用上一节带环境提示的查找方式。

> 原文注意：第一次 CMake 配置选中的 Zephyr 包会用于后续构建。要换包，例如通过新的 `ZEPHYR_BASE` 测试另一套源码，必须先进行 **pristine构建（Pristine Build，清理旧配置后重新生成构建）**。详情见[重新构建应用](https://docs.zephyrproject.org/latest/develop/application/index.html#application-rebuild)。

> 译注：所有目录树中的 `<projects>`、`<home>` 都是布局占位名，不是机器固定目录。需要对照的是应用与工作区、Zephyr 的相对关系，不是复现作者的盘符。原目录树中 `Exported to CMake` 表示已登记，`Not exported to CMake` 表示未登记。

## 2.6\_按版本选择

应用可指定构建所需 Zephyr 版本 `x.y.z`。这对独立应用尤其有用，既能要求最低版本，也能在多套安装之间帮助 CMake 选择。

例如应用 CMake 文件写入：

```cmake
find_package(Zephyr 2.2.0)
project(app)
```

表示至少需要 Zephyr 2.2.0。CMake 搜索导出的候选安装，寻找满足版本条件者。更多规则见 [CMake包版本选择](https://cmake.org/cmake/help/latest/command/find_package.html#version-selection)。

假设有两套已发布版本，各自位于独立工作区：

```text
<projects>/zephyr-workspace-2.a
└── zephyr                       (Exported to CMake)

<projects>/zephyr-workspace-2.b
└── zephyr                       (Exported to CMake)

<home>/app
├── CMakeLists.txt
├── prj.conf
└── src
    └── main.c
```

为要求最低版本 `2.a`，原文示意：

```cmake
find_package(Zephyr 2.a)
project(app)
```

其中 `2.a` 和 `2.b` 都满足该最低要求。若必须精确匹配，加入 CMake 查找参数 `EXACT`：

```cmake
find_package(Zephyr 2.a EXACT)
project(app)
```

若要求不存在的 `2.z`：

```cmake
find_package(Zephyr 2.z)
project(app)
```

则会出现类似以下的包版本不匹配消息：

```text
Could not find a configuration file for package "Zephyr" that is compatible
with requested version "2.z".

The following configuration files were considered but not accepted:

  <projects>/zephyr-workspace-2.a/zephyr/share/zephyr-package/cmake/ZephyrConfig.cmake, version: 2.a.0
  <projects>/zephyr-workspace-2.b/zephyr/share/zephyr-package/cmake/ZephyrConfig.cmake, version: 2.b.0
```

该消息表示找到了列出的配置文件，但其版本不满足请求，因此未接受。

> 译注：`2.a`、`2.b`、`2.z` 是原文表示不同版本的符号示意，实际 CMake 版本参数必须使用数值版本。原例没有加 `REQUIRED`，不能把这段消息一概解释为 `find_package` 自身立即终止配置；需要强制缺包失败时，应使用 `REQUIRED`。这里完整保留原文命令与诊断输出，未实际触发这些构建。

仓库内应用和工作区应用也可以指定版本。这样可以要求所在仓库或工作区满足版本条件，避免只更新工作区一部分之后意外使用不匹配源码构建。

## 2.7\_同一工作区中的多套Zephyr

有时希望保留原工作区的 Zephyr，同时试用新版本；也可能需要同时放置上游版本、厂商版本和自定义版本。例如：

```text
<projects>/zephyr-workspace
├── zephyr
├── zephyr-vendor
├── zephyr-custom
├── ...
└── my_applications
     └── my_first_app
```

此时 `find_package(Zephyr)` 按以下优先顺序选择：

1. 项目名为 `zephyr` 的安装。
2. 其他 Zephyr 项目按**字典序（Lexicographical Order）**排列后的第一个；此例顺序为 `zephyr-custom`、`zephyr-vendor`。

因此 `my_first_app` 默认使用 `<projects>/zephyr-workspace/zephyr`。

应用可通过 CMake 列表变量 `ZEPHYR_PREFER` 指定**偏好列表（Preference List）**：

```cmake
set(ZEPHYR_PREFER "zephyr-custom" "zephyr-vendor")
find_package(Zephyr)

project(my_first_app)
```

列表可含多个 Zephyr 名称。某个候选不存在时会被忽略，继续查找下一候选。

这样可以临时增加测试版本，而无需改动当前 Zephyr。原文示例优先查找 `zephyr-test`：

```cmake
set(ZEPHYR_PREFER "zephyr-test")
find_package(Zephyr)

project(my_first_app)
```

测试结束后，不再保留该临时目录也不会使偏好列表要求它必须存在。

> 译注：这里描述查找机制，未创建或删除任何仓库。切换候选时仍需处理上一节所说的已有构建缓存；仅更改偏好列表并不能证明旧构建目录已经换用另一套 Zephyr。

## 2.8\_Zephyr构建配置包

另有两种 **Zephyr构建配置CMake包（Zephyr Build Configuration CMake Packages）**，用于以更通用方式管理构建设置：

| 包名 | 作用范围 | 提供的配置文件 |
| --- | --- | --- |
| `ZephyrBuildConfiguration` | 工作区中的全部 Zephyr 应用 | `ZephyrBuildConfig.cmake` |
| `ZephyrAppConfiguration` | 当前正在构建的应用 | `ZephyrAppConfig.cmake` |

它们类似可设置[环境变量](https://docs.zephyrproject.org/latest/develop/env_vars.html#env-vars)的用户 `.zephyrrc`，但设置的是 CMake 变量；还能随项目仓库向所有用户共享，或加载附加 CMake 初始化代码。

这些包在 Zephyr 初始化代码已建立初始属性和 `ZEPHYR_BASE` 之后、后续构建 CMake 逻辑之前加载。先加载 `ZephyrBuildConfiguration`，再加载 `ZephyrAppConfiguration`，因此应用配置包可按需要覆盖工作区设置。

可在其中建立或扩展设备树搜索根 `DTS_ROOT`、开发板搜索根 `BOARD_ROOT`、工具链搜索根 `TOOLCHAIN_ROOT`、其他工具链配置、固定覆盖文件等属性，也可包含其他初始化代码。

### 2.8.1\_文件查找规则

由项目维护者创建上表相应配置文件并放到合适位置。此处的 `find_package` 禁用了其他默认 CMake 包搜索路径和提示，也没有实现版本检查，因此不能通过 CMake 用户包注册表登记这两个配置包。

按以下顺序查找：

1. 若设置了 `ZephyrBuildConfiguration_ROOT` 或 `ZephyrAppConfiguration_ROOT`，先在相应前缀下搜索。找到匹配文件则执行；否则进入下一步。
2. 工作区配置包在 `${ZEPHYR_BASE}/../*` 下查找，应用配置包在 `${APPLICATION_SOURCE_DIR}` 下查找。找到则执行；找不到则结束搜索。

推荐使用第二步的默认位置；`<PackageName>_ROOT` 变量提供自定义位置的灵活性。独立应用尤其可能需要它，因为默认工作区配置包路径通常不适用。

可以在 CMake 命令行设置根变量、在 `find_package(Zephyr ...)` 之前设置 CMake 变量、设置环境变量，或通过 `-C` 参数提供的 **CMake缓存初始化文件（CMake Cache Initialization File）**设置。

> 原文注意：这些根变量及默认位置都只是搜索前缀，还会与 CMake 的其他路径后缀组合。任何符合 [CMake包搜索规则](https://cmake.org/cmake/help/latest/command/find_package.html#search-procedure)的组合都有效。

要完全禁用某一配置包搜索，使用特殊 CMake 变量 `CMAKE_DISABLE_FIND_PACKAGE_<PackageName>`，即将 `CMAKE_DISABLE_FIND_PACKAGE_ZephyrBuildConfiguration` 或 `CMAKE_DISABLE_FIND_PACKAGE_ZephyrAppConfiguration` 设为 `TRUE`。

### 2.8.2\_目录与配置示例

可能的文件布局如下；清单仓库名称不限，应用配置文件也可处于图示包目录结构中：

```text
<projects>/zephyr-workspace
├── zephyr
├── ...
├── manifest repo (can be named anything)
│    └── cmake/ZephyrBuildConfig.cmake
├── ...
└── zephyr application
     └── share/zephyrapp-package/cmake/ZephyrAppConfig.cmake
```

以下为 `ZephyrBuildConfig.cmake` 原例。先了解其中路径变量和工具链条件，再对照代码：

> 译注：`get_filename_component(... ABSOLUTE)` 在构建时将基于当前文件位置的相对关系解析为规范路径，并未在文档或源码中硬编码机器安装地址。`APPLICATION_PROJECT_DIR` 是此例定义的项目目录变量，`CMAKE_CURRENT_LIST_DIR` 表示当前 CMake 文件所在目录，`list(APPEND BOARD_ROOT ...)` 将其加入板搜索根。

> 译注：原例的 `../../..` 依赖文件实际层级。如果配置文件按上图放在清单仓库的 `cmake/` 下，向上三级不一定是预期项目根；必须按自己的目录布局核对。工具链分支查找 `arm-none-eabi-gcc`，使用的 `GNU_ARM_GCC` 是该程序路径或未找到标记，`GNUARMEMB_TOOLCHAIN_PATH` 由编译器位置推导而来。这里的 **GNU Arm Embedded（GNU Arm嵌入式工具链产品名）**只是一种示例选择。

> 译注：条件 `if(NOT ENV{ZEPHYR_TOOLCHAIN_VARIANT})` 只检查同名环境变量，没有检查是否已经通过 CMake 缓存设置工具链；因此原注释“没有设置工具链时才给默认值”比代码实际检查范围更宽。集成前应结合当前工具链配置方式核对，不能直接用此例覆盖已有配置。

原例的 `APPEND` 参数表示追加列表项，条件运算符 `NOT` 表示取反，`STREQUAL` 比较字符串；`GNU_ARM_GCC-NOTFOUND` 是未找到编译器时的结果标记。工具链选择由变量 `ZEPHYR_TOOLCHAIN_VARIANT` 控制。

```cmake
# ZephyrBuildConfig.cmake sample code

# To ensure final path is absolute and does not contain ../.. in variable.
get_filename_component(APPLICATION_PROJECT_DIR
                       ${CMAKE_CURRENT_LIST_DIR}/../../..
                       ABSOLUTE
)

# Add this project to list of board roots
list(APPEND BOARD_ROOT ${APPLICATION_PROJECT_DIR})

# Default to GNU Arm Embedded toolchain if no toolchain is set
if(NOT ENV{ZEPHYR_TOOLCHAIN_VARIANT})
    set(ZEPHYR_TOOLCHAIN_VARIANT gnuarmemb)
    find_program(GNU_ARM_GCC arm-none-eabi-gcc)
    if(NOT ${GNU_ARM_GCC} STREQUAL GNU_ARM_GCC-NOTFOUND)
        # The toolchain root is located above the path to the compiler.
        get_filename_component(GNUARMEMB_TOOLCHAIN_PATH ${GNU_ARM_GCC}/../.. ABSOLUTE)
    endif()
endif()
```

## 2.9\_包实现文件

官方 [share/zephyr-package/cmake目录](https://github.com/zephyrproject-rtos/zephyr/blob/main/share/zephyr-package/cmake)包含供 CMake `find_package()` 使用的配置包及导出代码。

| 文件 | 职责 |
| --- | --- |
| `ZephyrConfigVersion.cmake` | 包版本文件。判断安装是否满足 `find_package(Zephyr ...)` 要求，并检测仓库内或工作区内的安装关系。 |
| `ZephyrConfig.cmake` | 包配置入口。对满足要求的包加载 Zephyr 初始化代码。 |
| `zephyr_package_search.cmake` | 检测仓库和工作区候选的共用实现，由前两者使用。 |
| `zephyr_export.cmake` | 执行本章“不通过west导出”中的用户包登记。 |

通用包机制另见 [CMake包手册](https://cmake.org/cmake/help/latest/manual/cmake-packages.7.html)。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：CMake构建系统](P001_CMake构建系统.md) · [本模块主线目录](../reading/build_system.md) · [全部主线](../reading/README.md) · [下一篇：构建与配置入口](P003_构建与配置入口.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：CMake构建系统](P001_CMake构建系统.md) · [返回大纲](大纲.md) · [下一章：构建与配置入口](P003_构建与配置入口.md)

</details>

<!-- reading-navigation:end -->
