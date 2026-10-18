---
id: learning.zephyr-docs.toolchains.tc_custom
title: 自定义CMake工具链
kind: reference
status: maintained
domains: [zephyr, toolchains]
source_url: https://docs.zephyrproject.org/latest/develop/toolchains/custom_cmake.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_自定义CMake工具链

原文：[自定义CMake工具链](https://docs.zephyrproject.org/latest/develop/toolchains/custom_cmake.html)。本次读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 9.1\_外部工具链配置文件

要使用由外部 CMake 文件定义的自定义工具链（Custom Toolchain），设置以下[环境变量](P003_环境变量.md)：

- `ZEPHYR_TOOLCHAIN_VARIANT`：自定义工具链名称。
- `TOOLCHAIN_ROOT`：包含该工具链 CMake 配置文件的目录路径。

Zephyr 随后会包含 `TOOLCHAIN_ROOT` 目录下的这些文件：

- `cmake/toolchain/<toolchain name>/generic.cmake`：配置工具链的通用用途（Generic Use），主要是对生成的[设备树文件（Devicetree）](../devicetree/P013_设备树文档入口.md)运行 C 预处理器。
- `cmake/toolchain/<toolchain name>/target.cmake`：配置工具链的目标用途（Target Use），即构建 Zephyr 和应用源代码。

`<toolchain name>` 必须与 `ZEPHYR_TOOLCHAIN_VARIANT` 中提供的名称一致。有关 `generic.cmake` 与 `target.cmake` 应包含哪些内容，详见官方源码 [cmake/modules/FindHostTools.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/cmake/modules/FindHostTools.cmake) 和 [cmake/modules/FindTargetTools.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/cmake/modules/FindTargetTools.cmake)。

## 9.2\_CMake变量与初始缓存

为 Zephyr 应用生成构建系统时，也可以将 `ZEPHYR_TOOLCHAIN_VARIANT` 与 `TOOLCHAIN_ROOT` 设为 CMake 变量：

```bash
west build ... -- -DZEPHYR_TOOLCHAIN_VARIANT=... -DTOOLCHAIN_ROOT=...
```

```bash
cmake -DZEPHYR_TOOLCHAIN_VARIANT=... -DTOOLCHAIN_ROOT=...
```

此时 CMake 的 [`-C <initial-cache>` 选项](https://cmake.org/cmake/help/latest/manual/cmake.1.html#options)可能很有用。把 `ZEPHYR_TOOLCHAIN_VARIANT`、`TOOLCHAIN_ROOT` 以及其他设置保存在 `my-toolchain.cmake` 中，便可用 `cmake -C my-toolchain.cmake ...` 调用，减少重复输入。

## 9.3\_自定义工具链头文件

Zephyr 包含 `include/zephyr/toolchain.h`，它再根据 `__llvm__`、`__GNUC__` 等编译器标识符（Compiler Identifier），包含工具链专用头文件。

一些自定义编译器会将自身标识为其基础编译器，例如 LLVM，从而包含 `toolchain/llvm.h`；但该文件未必适合自定义工具链。要解决这一问题，改为包含 `include/other.h`，可在 `<TOOLCHAIN_ROOT>/cmake/toolchain/<toolchain name>/` 下的 `generic.cmake` 和／或 `target.cmake` 中加入 `set(TOOLCHAIN_USE_CUSTOM 1)`。

设置 `TOOLCHAIN_USE_CUSTOM` 后，必须在树外（Out-of-tree）提供 `other.h`，并由它包含适合自定义工具链的正确头文件。一个合适位置，是 `TOOLCHAIN_ROOT` 所指目录下的 `include/zephyr/toolchain`。

为了让 Zephyr 构建包含工具链头文件，可以把 `USERINCLUDE` 指向包含目录（Include Directory）：

```bash
west build -- -DZEPHYR_TOOLCHAIN_VARIANT=... -DTOOLCHAIN_ROOT=... -DUSERINCLUDE=...
```

> 源码核对译注：上段“包含 `include/other.h`”保留原页概述。2026-10-14读取的[官方toolchain.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/toolchain.h)在自定义分支实际写的是 `#include <toolchain/other.h>`，与当前仓库的[参照源码](../../../include/zephyr/toolchain.h)一致。因此，若按原文建议把文件放在 `<TOOLCHAIN_ROOT>/include/zephyr/toolchain/other.h`，对应的 `USERINCLUDE` 应指向 `<TOOLCHAIN_ROOT>/include/zephyr`；若文件放在 `<TOOLCHAIN_ROOT>/include/toolchain/other.h`，才指向 `<TOOLCHAIN_ROOT>/include`。包含目录必须与实际布局匹配，不依赖作者机器位置。`...` 是需补齐的工具链名、目录及构建参数，不是可直接执行的完整配置。源码读取摘要见来源记录，`main`后续可能变化。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Arm嵌入式工具链（ATfE）](P008_Arm嵌入式工具链.md) · [本模块主线目录](../reading/toolchains.md) · [全部主线](../reading/README.md) · [下一篇：IAR Arm工具链](P010_IARArm工具链.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P008_Arm嵌入式工具链.md) · [返回大纲](大纲.md) · [下一章](P010_IARArm工具链.md)

</details>

<!-- reading-navigation:end -->
